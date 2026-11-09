#!/usr/bin/env python3
"""TVBox config builder with MacCMS site validation (run by GitHub Actions).

The output follows the format of scripts/seed.json (a full TVBox config):
every top-level field of the seed (spider, wallpaper, logo, parses, doh, lives,
headers, proxy, hosts, ads, rules, ...) is copied unchanged and only "sites" is
rebuilt:

    sites = seed sites that are not MacCMS API sites (csp_ ..., kept as-is)
          + validated MacCMS API sites (type 1), fastest first

Inputs
  * scripts/seed.json      : your trusted TVBox config (required for the format)
  * scripts/api_sites.json : optional trusted list of MacCMS API sites
                             ("api_site" dict and/or "sites" list, type 0/1)
  * scripts/sources.txt    : optional, one raw config URL per line (untrusted)
  * GitHub code search     : untrusted, skipped when SEED_ONLY=1

Outputs (in OUT_DIR, default "frontend")
  subscribe.json        -> the TVBox config described above
  subscribe-check.json  -> per-site detection results
  subscribe-report.json -> summary statistics
  sites-check.csv/.md   -> one row per collected site: usable?, latency, reason
  sources-check.json/.md -> one row per source file (download status, sites found,
                            how many passed), plus the code-search request log

A MacCMS site passes validation when ?ac=list returns a non-empty "class" list
and ?ac=detail&pg=1 returns a non-empty "list" of videos within the latency
threshold. Trusted sites (seed.json / api_sites.json) are kept even when they
fail (TRUST_SEED=1, default) because the check runs from GitHub's overseas
datacenters; set TRUST_SEED=0 to drop them.
"""
import copy
import ipaddress
import json
import os
import re
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from functools import lru_cache
from urllib.parse import parse_qsl, urlencode, urljoin, urlparse

import requests

GH_TOKEN = os.environ.get("GH_TOKEN", "")
MAX_LATENCY_MS = int(os.environ.get("MAX_LATENCY_MS", "4000"))  # drop anything slower
MAX_SITES = int(os.environ.get("MAX_SITES", "150"))             # max MacCMS API sites added
MAX_SOURCES = int(os.environ.get("MAX_SOURCES", "100"))
MAX_CANDIDATES = int(os.environ.get("MAX_CANDIDATES", "1500"))
WORKERS = int(os.environ.get("WORKERS", "40"))
# SEED_ONLY=1: no GitHub search / sources.txt, only seed.json and api_sites.json.
SEED_ONLY = os.environ.get("SEED_ONLY", "0") == "1"
# Keep trusted sites even if they fail validation from the GitHub runner.
TRUST_SEED = os.environ.get("TRUST_SEED", "1") == "1"
# Base URL used to resolve "./xxx" paths of seed sites (e.g. the folder of the
# original config on raw.githubusercontent.com). Without it such sites are dropped.
SEED_BASE_URL = os.environ.get("SEED_BASE_URL", "").strip()
OUT_DIR = os.environ.get("OUT_DIR", "frontend")
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SEARCH_LOG = []  # one entry per code-search request (for the per-source report)

# Site names containing any of these (case-insensitive) are skipped.
# Override with the EXCLUDE_KEYWORDS env var (comma separated); set it empty to disable.
DEFAULT_EXCLUDE = "🔞,18+,18禁,成人,福利,情色,色情,涩,黄色"
EXCLUDE_KEYWORDS = [k.strip().lower()
                    for k in os.environ.get("EXCLUDE_KEYWORDS", DEFAULT_EXCLUDE).split(",")
                    if k.strip()]
# Auto-found (untrusted) sites on these domains and their subdomains are skipped.
BLOCKED_HOSTS = [x.strip().lower() for x in os.environ.get(
    "BLOCKED_HOSTS",
    "serv00.net,qzz.io,workers.dev,pages.dev,vercel.app,netlify.app,ngrok.io,trycloudflare.com",
).split(",") if x.strip()]

SEARCH_QUERIES = [
    "sites spider extension:json tvbox",
    "sites api csp_ extension:json",
    "api_site cache_time extension:json",
]
UA_API = "Mozilla/5.0 (Linux; Android 11) TVBox-Aggregator"
UA_SITE = "okhttp/3.15"  # what TVBox-style apps send
# Query parameters the apps add themselves; removed from stored api URLs.
DROP_PARAMS = {"ac", "pg", "t", "h", "ids", "wd", "pagesize"}


def suspicious_url(api):
    """Reason string if an untrusted API URL looks untrustworthy, else None."""
    p = urlparse(api)
    host = (p.hostname or "").lower()
    if p.scheme != "https":
        return "not_https"
    try:
        ipaddress.ip_address(host)
        return "ip_host"
    except ValueError:
        pass
    if p.port not in (None, 443):
        return "custom_port"
    if "http" in p.query.lower():
        return "proxy_wrapped"
    if any(host == b or host.endswith("." + b) for b in BLOCKED_HOSTS):
        return "blocked_host"
    return None


# ----------------------------------------------------------------- GitHub search
def gh_get(params):
    """Call the code search API, retrying up to 3 times when rate limited."""
    headers = {"Accept": "application/vnd.github+json", "User-Agent": UA_API}
    if GH_TOKEN:
        headers["Authorization"] = f"Bearer {GH_TOKEN}"
    r = None
    for attempt in range(6):
        r = requests.get("https://api.github.com/search/code", params=params,
                         headers=headers, timeout=30)
        if r.status_code in (403, 429) and attempt < 5:
            wait = int(r.headers.get("Retry-After") or 0)
            reset = r.headers.get("X-RateLimit-Reset")
            if not wait and reset:
                wait = max(0, int(reset) - int(time.time())) + 2
            wait = min(max(wait, 30), 120)
            print(f"  rate limited ({r.status_code}), waiting {wait}s ...")
            time.sleep(wait)
            continue
        return r
    return r


def search_sources():
    urls, seen = [], set()

    # Optional manual sources: one raw config URL per line in scripts/sources.txt
    extra = os.path.join(SCRIPT_DIR, "sources.txt")
    if os.path.exists(extra):
        with open(extra, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("http") and line not in seen:
                    seen.add(line)
                    urls.append(line)
        print(f"   loaded {len(urls)} manual sources from sources.txt")

    for q in SEARCH_QUERIES:
        stop = False
        for page in (1, 2, 3):
            r = gh_get({"q": q, "per_page": 100, "page": page})
            SEARCH_LOG.append({"query": q, "page": page, "http_status": r.status_code,
                               "items": len(r.json().get("items", [])) if r.ok else None})
            if not r.ok:
                print(f"  search '{q}' page {page} failed: HTTP {r.status_code} {r.text[:200]}")
                stop = r.status_code in (403, 429)
                break
            items = r.json().get("items", [])
            for it in items:
                raw = (it["html_url"]
                       .replace("https://github.com/", "https://raw.githubusercontent.com/")
                       .replace("/blob/", "/"))
                if raw not in seen:
                    seen.add(raw)
                    urls.append(raw)
            if len(items) < 100:
                break
            time.sleep(7)  # code search is limited to ~10 requests/minute
        if stop:
            print("  still rate limited, skipping remaining search queries")
            break
    return urls[:MAX_SOURCES]


# --------------------------------------------------------------------- Download
def parse_json_lenient(text):
    text = text.lstrip("\ufeff")
    try:
        return json.loads(text)
    except ValueError:
        pass
    cleaned = re.sub(r"(?m)^\s*//.*$", "", text)
    cleaned = re.sub(r"/\*.*?\*/", "", cleaned, flags=re.S)
    try:
        return json.loads(cleaned)
    except ValueError:
        return None


def download_source(url):
    """-> (url, data or None, reason)."""
    try:
        r = requests.get(url, headers={"User-Agent": UA_API}, timeout=15)
        if not r.ok:
            return url, None, f"http_{r.status_code}"
        data = parse_json_lenient(r.text)
        if isinstance(data, dict):
            return url, data, "ok"
        return url, None, "not_json_object"
    except requests.Timeout:
        return url, None, "timeout"
    except Exception:
        return url, None, "download_error"


def load_json_file(name):
    path = os.path.join(SCRIPT_DIR, name)
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as f:
        data = parse_json_lenient(f.read())
    if isinstance(data, dict):
        print(f"   loaded scripts/{name}")
        return data
    print(f"   scripts/{name} could not be parsed, ignoring it")
    return None


# ---------------------------------------------------------------- Normalisation
def is_api_site(site):
    """A plain MacCMS API site: type 0/1 with an http(s) api."""
    return (isinstance(site, dict) and site.get("key")
            and isinstance(site.get("api"), str)
            and str(site.get("type")) in ("0", "1")
            and site["api"].startswith(("http://", "https://")))


def collect_sites(data, src_url, trusted, label=""):
    """MacCMS API sites from a "sites" list and/or an "api_site" dict."""
    raw = list(data["sites"]) if isinstance(data.get("sites"), list) else []
    api_site = data.get("api_site")
    if isinstance(api_site, dict):
        for k, v in api_site.items():
            if isinstance(v, dict) and isinstance(v.get("api"), str):
                raw.append({"key": str(k), "name": v.get("name") or str(k),
                            "api": v["api"], "type": 1})
    out = []
    for site in raw:
        if isinstance(site, dict) and isinstance(site.get("api"), str):
            api = site["api"]
            if api.startswith(("./", "../")) and src_url:
                site = dict(site, api=urljoin(src_url, api))
        if not is_api_site(site):
            continue
        out.append({"key": str(site["key"]),
                    "name": str(site.get("name") or site["key"]).strip(),
                    "api": site["api"], "trusted": trusted,
                    "source": label or src_url})
    return out


def split_seed_sites(seed):
    """Seed sites that are NOT plain API sites (csp_, js, ...), kept verbatim.

    Sites whose api/ext start with ./ or ../ cannot work from our host, so they
    are resolved with SEED_BASE_URL or dropped.
    """
    keep, dropped = [], []
    for site in seed.get("sites") or []:
        if not isinstance(site, dict) or is_api_site(site):
            continue  # API sites are validated separately
        s = copy.deepcopy(site)
        rel = [f for f in ("api", "ext")
               if isinstance(s.get(f), str) and s[f].startswith(("./", "../"))]
        if rel:
            if SEED_BASE_URL:
                for f in rel:
                    s[f] = urljoin(SEED_BASE_URL, s[f])
            else:
                dropped.append({"key": s.get("key"), "name": s.get("name"),
                                "reason": "relative path (set SEED_BASE_URL to keep)"})
                continue
        keep.append(s)
    return keep, dropped


def normalize_api_url(api):
    """Turn a TVBox type 0/1 api into a plain MacCMS JSON endpoint.

    Keeps proxy-style query strings (e.g. ?url=...), removes parameters the apps
    add themselves (ac, pg, ...), drops the /at/xml suffix and merges slashes.
    """
    p = urlparse(api)
    if not p.netloc:
        return None
    path = re.sub(r"/at/xml/?$", "", p.path)
    path = re.sub(r"/{2,}", "/", path).rstrip("/")
    query = urlencode([(k, v) for k, v in parse_qsl(p.query, keep_blank_values=True)
                       if k.lower() not in DROP_PARAMS])
    if not path and query:
        path = "/"
    return f"{p.scheme}://{p.netloc}{path}" + (f"?{query}" if query else "")


def build_candidates(sites):
    out, seen = [], set()
    for s in sites:
        api = normalize_api_url(s["api"])
        if not api or api in seen:
            continue
        if any(k in s["name"].lower() for k in EXCLUDE_KEYWORDS):
            continue
        if not s["trusted"] and suspicious_url(api):
            continue  # only filters untrusted sites
        seen.add(api)
        out.append({"key": s["key"], "name": s["name"], "api": api, "trusted": s["trusted"],
                    "source": s.get("source", "")})
    return out


# ------------------------------------------------------------------- Validation
def _get_json(api, params):
    """-> (data, reason). reason is "ok" or a short failure code."""
    r = requests.get(api, params=params, headers={"User-Agent": UA_SITE}, timeout=(4, 8))
    if r.status_code >= 400:
        return None, f"http_{r.status_code}"
    try:
        data = r.json()
    except ValueError:
        return None, "not_json"
    if not isinstance(data, dict):
        return None, "not_json"
    return data, "ok"


@lru_cache(maxsize=None)
def probe_maccms(api):
    """-> (latency_ms or None, reason).

    Requires ?ac=list to return a non-empty category list ("class") and
    ?ac=detail&pg=1 to return a non-empty video list ("list").
    """
    reason = "unknown"
    for _ in range(2):  # one retry
        try:
            t0 = time.perf_counter()
            lst, reason = _get_json(api, {"ac": "list", "pg": 1})
            if lst is None:
                continue
            if not isinstance(lst.get("class"), list) or not lst["class"]:
                reason = "no_class"
                continue
            t1 = time.perf_counter()
            det, reason = _get_json(api, {"ac": "detail", "pg": 1})
            if det is None:
                continue
            if not isinstance(det.get("list"), list) or not det["list"]:
                reason = "empty_list"
                continue
            first = det["list"][0]
            if not isinstance(first, dict) or not (first.get("vod_id") or first.get("vod_name")):
                reason = "bad_item"
                continue
            t2 = time.perf_counter()
            return int(max(t1 - t0, t2 - t1) * 1000), "ok"
        except requests.Timeout:
            reason = "timeout"
        except requests.RequestException:
            reason = "connection_error"
        except Exception:
            reason = "error"
    return None, reason


@lru_cache(maxsize=None)
def probe_url(url):
    """Latency in ms until the first body chunk arrives, or None if unreachable."""
    for _ in range(2):  # one retry
        t0 = time.perf_counter()
        try:
            with requests.get(url, headers={"User-Agent": UA_SITE},
                              timeout=(4, 8), stream=True) as r:
                if r.status_code >= 400:
                    continue
                if not next(r.iter_content(1024), b""):
                    continue
                return int((time.perf_counter() - t0) * 1000)
        except Exception:
            continue
    return None


# ----------------------------------------------------------------------- Output
def unique_key(raw, used):
    base = str(raw).strip() or "site"
    key, n = base, 1
    while key in used:
        n += 1
        key = f"{base}_{n}"
    used.add(key)
    return key


def write_json(name, data):
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, name), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


REASON_TEXT = {
    "ok": "可用", "too_slow": "太慢(超过阈值)", "timeout": "超时", "connection_error": "连接失败",
    "not_json": "返回的不是JSON", "no_class": "没有分类列表", "empty_list": "视频列表为空",
    "bad_item": "视频条目格式不对", "error": "其他错误", "unknown": "未知",
}


def write_sites_report(now, checks):
    """sites-check.csv / sites-check.md: one row per collected site -> usable? how fast?"""
    def label(c):
        if c["passed"]:
            return "可用"
        return REASON_TEXT.get(c["reason"], c["reason"] if not c["reason"].startswith("http_")
                               else "HTTP错误 " + c["reason"][5:])

    rows = sorted(checks, key=lambda c: (not c["passed"],
                                         c["latency_ms"] if c["latency_ms"] is not None else 10**9))
    import csv
    os.makedirs(OUT_DIR, exist_ok=True)
    head = ["名称", "API地址", "来源", "是否可用", "耗时(ms)", "原因", "是否信任", "是否进入输出"]
    with open(os.path.join(OUT_DIR, "sites-check.csv"), "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(head)
        for c in rows:
            w.writerow([c["name"], c["api"], c["source"], "是" if c["passed"] else "否",
                        c["latency_ms"] if c["latency_ms"] is not None else "",
                        label(c), "是" if c["trusted"] else "否",
                        "是" if c.get("in_output") else "否"])
    ok = sum(1 for c in rows if c["passed"])
    lines = [f"# Site check ({now})", "",
             f"可用 {ok} / 共检测 {len(rows)}（可用 = 分类列表和视频列表都能返回，且耗时不超过 {MAX_LATENCY_MS}ms；"
             f"耗时取两次请求中较慢的一次）", "",
             "| 名称 | API地址 | 可用 | 耗时(ms) | 原因 | 进入输出 |", "|---|---|---|---|---|---|"]
    for c in rows:
        lines.append(f"| {c['name']} | {c['api']} | {'✅' if c['passed'] else '❌'} | "
                     f"{c['latency_ms'] if c['latency_ms'] is not None else '-'} | {label(c)} | "
                     f"{'是' if c.get('in_output') else '否'} |")
    with open(os.path.join(OUT_DIR, "sites-check.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def write_source_report(now, seed, extra_trusted, sources, download_reason,
                        found_per_source, checks, kept_seed_sites, dropped_seed_sites,
                        live_checks):
    """sources-check.json / sources-check.md: one row per source file."""
    by_source = {}
    for c in checks:
        st = by_source.setdefault(c["source"], {"candidates": 0, "passed": 0, "in_output": 0,
                                                "fastest_ms": None})
        st["candidates"] += 1
        st["passed"] += 1 if c["passed"] else 0
        st["in_output"] += 1 if c.get("in_output") else 0
        if c["passed"] and (st["fastest_ms"] is None or c["latency_ms"] < st["fastest_ms"]):
            st["fastest_ms"] = c["latency_ms"]

    rows = []

    def add(label, trusted, status, note=""):
        st = by_source.get(label, {})
        rows.append({
            "source": label, "trusted": trusted, "status": status, "note": note,
            "api_sites_found": found_per_source.get(label, 0),
            "api_candidates": st.get("candidates", 0),
            "api_passed": st.get("passed", 0),
            "api_in_output": st.get("in_output", 0),
            "fastest_ms": st.get("fastest_ms"),
        })

    if seed:
        add("seed.json", True, "loaded",
            f"{len(kept_seed_sites)} non-API sites kept as-is, {len(dropped_seed_sites)} dropped")
    if extra_trusted:
        add("api_sites.json", True, "loaded")
    for u in sources:
        why = download_reason.get(u, "unknown")
        add(u, False, "parsed" if why == "ok" else why)

    summary = {"generated_at": now, "sources_total": len(sources),
               "sources_parsed": sum(1 for u in sources if download_reason.get(u) == "ok"),
               "search_requests": SEARCH_LOG}
    write_json("sources-check.json", {**summary, "sources": rows,
                                      "seed_sites_dropped": dropped_seed_sites,
                                      "lives": live_checks})

    lines = [f"# Source check ({now})", "",
             f"- untrusted source files: {summary['sources_parsed']}/{summary['sources_total']} parsed",
             f"- code-search requests: {len(SEARCH_LOG)}", ""]
    for q in SEARCH_LOG:
        lines.append(f"  - `{q['query']}` page {q['page']}: HTTP {q['http_status']}, "
                     f"items {q['items']}")
    lines += ["", "| source | trusted | status | found | candidates | passed | in output | fastest ms |",
              "|---|---|---|---|---|---|---|---|"]
    for r in rows:
        status = r["status"] + (f" ({r['note']})" if r["note"] else "")
        lines.append(f"| {r['source']} | {'yes' if r['trusted'] else 'no'} | {status} | "
                     f"{r['api_sites_found']} | {r['api_candidates']} | {r['api_passed']} | "
                     f"{r['api_in_output']} | {r['fastest_ms'] if r['fastest_ms'] is not None else '-'} |")
    lines += ["", "## Live sources", "", "| name | url | reachable | ms |", "|---|---|---|---|"]
    for lc in live_checks:
        lines.append(f"| {lc['name']} | {lc['url']} | {'yes' if lc['reachable'] else 'no'} | "
                     f"{lc['latency_ms'] if lc['latency_ms'] is not None else '-'} |")
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "sources-check.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


# ------------------------------------------------------------------------- Main
def main():
    print(f"== 1/4 collecting sources (SEED_ONLY={'1' if SEED_ONLY else '0'}, "
          f"TRUST_SEED={'1' if TRUST_SEED else '0'})")
    seed = load_json_file("seed.json")
    extra_trusted = load_json_file("api_sites.json")
    if SEED_ONLY and not seed and not extra_trusted:
        sys.exit("SEED_ONLY=1 but seed.json / api_sites.json are missing; keeping previous files")
    sources = [] if SEED_ONLY else search_sources()
    print(f"   {len(sources)} untrusted source files from search / sources.txt")

    print("== 2/4 downloading sources")
    with ThreadPoolExecutor(WORKERS) as ex:
        downloads = list(ex.map(download_source, sources))
    ok_sources = [(u, d) for u, d, _ in downloads if d]
    download_reason = {u: why for u, _, why in downloads}
    print(f"   {len(ok_sources)}/{len(sources)} parsed")

    # Trusted first so they win de-duplication and survive the candidate cap.
    entries = []
    if seed:
        entries.append(("", seed, True, "seed.json"))
    if extra_trusted:
        entries.append(("", extra_trusted, True, "api_sites.json"))
    entries += [(u, d, False, u) for u, d in ok_sources]
    all_sites = []
    found_per_source = Counter()
    for src_url, data, trusted, label in entries:
        found = collect_sites(data, src_url, trusted, label)
        found_per_source[label] += len(found)
        all_sites.extend(found)

    candidates = build_candidates(all_sites)[:MAX_CANDIDATES]
    trusted_n = sum(1 for s in candidates if s["trusted"])
    kept_seed_sites, dropped_seed_sites = split_seed_sites(seed) if seed else ([], [])
    print(f"   {len(candidates)} MacCMS API candidates ({trusted_n} trusted); "
          f"{len(kept_seed_sites)} other seed sites kept as-is, "
          f"{len(dropped_seed_sites)} dropped")
    for d in dropped_seed_sites:
        print(f"   dropped seed site: {d['name']} [{d['reason']}]")

    print("== 3/4 validating sites (content + latency)")
    live_list = [l for l in (seed or {}).get("lives") or []
                 if isinstance(l, dict) and str(l.get("url", "")).startswith("http")]
    with ThreadPoolExecutor(WORKERS) as ex:
        results = list(ex.map(lambda s: probe_maccms(s["api"]), candidates))
        live_lats = list(ex.map(lambda l: probe_url(l["url"]), live_list))

    checks, good_api = [], []
    for (lat, reason), s in zip(results, candidates):
        passed = lat is not None and lat <= MAX_LATENCY_MS
        if lat is not None and not passed:
            reason = "too_slow"
        keep = passed or (s["trusted"] and TRUST_SEED)
        if keep:
            good_api.append((lat if passed else MAX_LATENCY_MS, s))
        checks.append({
            "name": s["name"], "api": s["api"], "trusted": s["trusted"],
            "source": s.get("source", ""), "passed": passed, "reason": "ok" if passed else reason,
            "latency_ms": lat, "kept": keep,
        })
    # trusted sites first, then fastest first
    good_api.sort(key=lambda x: (not x[1]["trusted"], x[0]))
    good_api = good_api[:MAX_SITES]
    final_apis = {s["api"] for _, s in good_api}
    for c in checks:
        c["in_output"] = c["api"] in final_apis

    reasons = Counter(c["reason"] for c in checks)
    passed_n = sum(1 for c in checks if c["passed"])
    print(f"   result: {passed_n}/{len(checks)} API sites passed, reasons: {dict(reasons)}")
    order = sorted(checks, key=lambda c: (not c["passed"],
                                          c["latency_ms"] if c["latency_ms"] is not None else 10**9))
    for c in order:
        status = "PASS" if c["passed"] else ("FAIL(kept)" if c["kept"] else "FAIL(drop)")
        lat = f"{c['latency_ms']}ms" if c["latency_ms"] is not None else "-"
        print(f"   [{status:<10}] {lat:>7} {c['reason']:<16} {c['name']}  {c['api']}")
    live_checks = [{"name": l.get("name"), "url": l["url"], "reachable": lat is not None,
                    "latency_ms": lat} for l, lat in zip(live_list, live_lats)]
    for lc in live_checks:
        print(f"   [live {'OK  ' if lc['reachable'] else 'FAIL'}] {lc['name']}  {lc['url']}")

    print("== 4/4 writing output")
    used_keys = {str(s.get("key")) for s in kept_seed_sites}
    api_entries = [{
        "key": unique_key(s["key"], used_keys),
        "name": s["name"],
        "type": 1,  # MacCMS JSON API
        "api": s["api"],
        "searchable": 1,
        "quickSearch": 1,
        "filterable": 1,
    } for _, s in good_api]
    final_sites = kept_seed_sites + api_entries
    if not final_sites:
        sys.exit("no sites to publish; keeping previous files")

    # Same format as seed.json: every field is copied, only "sites" is rebuilt.
    out = ({k: copy.deepcopy(v) for k, v in seed.items() if k not in ("api_site", "cache_time")}
           if seed else {})
    out["sites"] = final_sites
    write_json("subscribe.json", out)
    print(f"   subscribe.json: {len(kept_seed_sites)} seed sites + {len(api_entries)} API sites")

    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    write_source_report(now, seed, extra_trusted, sources, download_reason,
                        found_per_source, checks, kept_seed_sites, dropped_seed_sites,
                        live_checks)
    write_sites_report(now, checks)
    lats = [c["latency_ms"] for c in checks if c["passed"]]  # passed sites only
    write_json("subscribe-check.json", {
        "generated_at": now,
        "note": "Checks run from GitHub's overseas runner; FAIL(kept) entries are trusted sites "
                "kept because TRUST_SEED=1 (they may block datacenter IPs). csp_/js seed sites "
                "need the app runtime and are not checked.",
        "summary": {
            "api_total": len(checks),
            "api_passed": passed_n,
            "api_failed": len(checks) - passed_n,
            "api_in_output": len(api_entries),
            "seed_sites_kept": len(kept_seed_sites),
            "seed_sites_dropped": len(dropped_seed_sites),
            "reasons": dict(reasons),
        },
        "results": order,
        "seed_sites_dropped": dropped_seed_sites,
        "lives": live_checks,
    })
    write_json("subscribe-report.json", {
        "generated_at": now,
        "seed_only": SEED_ONLY,
        "seed_loaded": bool(seed),
        "untrusted_sources_parsed": len(ok_sources),
        "api_candidates": len(candidates),
        "api_passed": passed_n,
        "api_in_output": len(api_entries),
        "seed_sites_kept": len(kept_seed_sites),
        "seed_sites_dropped": len(dropped_seed_sites),
        "total_sites_in_output": len(final_sites),
        "trust_seed": TRUST_SEED,
        "validation_reasons": dict(reasons),
        "latency_ms": ({"min": min(lats), "median": sorted(lats)[len(lats) // 2], "max": max(lats)}
                       if lats else None),
        "threshold_ms": MAX_LATENCY_MS,
    })
    print(json.dumps(json.load(open(os.path.join(OUT_DIR, "subscribe-report.json"),
                                    encoding="utf-8")), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
