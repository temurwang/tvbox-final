// Cloudflare Pages Function: /api/trigger
// 页面上的按钮 -> 这里校验密码 -> 调用 GitHub API 触发 collect-sources 工作流。
// GitHub 令牌只保存在 Cloudflare 的环境变量里，不会出现在网页代码中。
//
// 需要在 Pages 项目 设置 -> 变量和机密 里添加：
//   GH_DISPATCH_TOKEN  (机密) GitHub 细粒度令牌，仅 tvbox-final 仓库，权限 Actions: Read and write
//   TRIGGER_PASSWORD   (机密) 你自己定的触发密码
// 可选（不填则用下面的默认值）：
//   GH_REPO=temurwang/tvbox-final   GH_REF=feat-tvbox-aggregator-ui   GH_WORKFLOW=collect.yml

const JSON_HEADERS = { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" };

const reply = (obj, status = 200) => new Response(JSON.stringify(obj), { status, headers: JSON_HEADERS });

async function sha256(text) {
  return new Uint8Array(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(text)));
}

// 比较两个字符串，耗时不随内容变化
async function safeEqual(a, b) {
  const [x, y] = await Promise.all([sha256(a), sha256(b)]);
  let diff = 0;
  for (let i = 0; i < x.length; i++) diff |= x[i] ^ y[i];
  return diff === 0;
}

function clampInt(value, min, max, fallback) {
  const n = Number.parseInt(value, 10);
  if (!Number.isFinite(n)) return String(fallback);
  return String(Math.min(max, Math.max(min, n)));
}

function ghHeaders(token) {
  return {
    Accept: "application/vnd.github+json",
    Authorization: `Bearer ${token}`,
    "X-GitHub-Api-Version": "2022-11-28",
    "User-Agent": "tvbox-trigger-page",
  };
}

export async function onRequestPost({ request, env }) {
  if (!env.TRIGGER_PASSWORD || !env.GH_DISPATCH_TOKEN) {
    return reply({ ok: false, error: "服务端还没配置 TRIGGER_PASSWORD 和 GH_DISPATCH_TOKEN" }, 500);
  }

  let body;
  try {
    body = await request.json();
  } catch {
    return reply({ ok: false, error: "请求格式不对" }, 400);
  }

  if (!(await safeEqual(String(body.password ?? ""), env.TRIGGER_PASSWORD))) {
    return reply({ ok: false, error: "密码不对" }, 401);
  }

  const repo = env.GH_REPO || "temurwang/tvbox-final";
  const ref = env.GH_REF || "feat-tvbox-aggregator-ui";
  const workflow = env.GH_WORKFLOW || "collect.yml";
  const base = `https://api.github.com/repos/${repo}/actions/workflows/${workflow}`;

  if (body.action === "status") {
    const r = await fetch(`${base}/runs?per_page=3`, { headers: ghHeaders(env.GH_DISPATCH_TOKEN) });
    if (!r.ok) return reply({ ok: false, error: `读取运行状态失败（GitHub ${r.status}）` }, 502);
    const data = await r.json();
    const runs = (data.workflow_runs || []).map((x) => ({
      id: x.id,
      status: x.status,           // queued / in_progress / completed
      conclusion: x.conclusion,   // success / failure / cancelled / null
      created_at: x.created_at,
      event: x.event,
      branch: x.head_branch,
      url: x.html_url,
    }));
    return reply({ ok: true, runs });
  }

  if (body.action === "steps") {
    // 某次运行的各个步骤进度（页面“实时日志”用）
    const runId = String(body.run_id ?? "");
    if (!/^\d{1,20}$/.test(runId)) return reply({ ok: false, error: "run_id 不对" }, 400);
    const r = await fetch(`https://api.github.com/repos/${repo}/actions/runs/${runId}/jobs`, {
      headers: ghHeaders(env.GH_DISPATCH_TOKEN),
    });
    if (!r.ok) return reply({ ok: false, error: `读取步骤失败（GitHub ${r.status}）` }, 502);
    const data = await r.json();
    const steps = [];
    for (const job of data.jobs || []) {
      for (const st of job.steps || []) {
        steps.push({ name: st.name, status: st.status, conclusion: st.conclusion,
                     started_at: st.started_at, completed_at: st.completed_at });
      }
    }
    return reply({ ok: true, steps });
  }

  if (body.action === "trigger") {
    const i = body.inputs || {};
    const inputs = {
      seed_only: i.seed_only === "1" ? "1" : "0",
      max_sites: clampInt(i.max_sites, 1, 500, 150),
      max_latency_ms: clampInt(i.max_latency_ms, 300, 20000, 4000),
    };
    const r = await fetch(`${base}/dispatches`, {
      method: "POST",
      headers: { ...ghHeaders(env.GH_DISPATCH_TOKEN), "content-type": "application/json" },
      body: JSON.stringify({ ref, inputs }),
    });
    if (r.status === 204) return reply({ ok: true, ref, inputs });
    let detail = "";
    try { detail = (await r.json()).message || ""; } catch { /* ignore */ }
    const hint = r.status === 404 ? "（仓库、工作流文件名或分支不对，或令牌没有该仓库的权限）"
               : r.status === 403 || r.status === 401 ? "（令牌无效，或缺少 Actions 读写权限）"
               : r.status === 422 ? "（分支上没有这个工作流，或参数不被接受）" : "";
    return reply({ ok: false, error: `GitHub 返回 ${r.status}${hint} ${detail}`.trim() }, 502);
  }

  return reply({ ok: false, error: "未知操作" }, 400);
}

export async function onRequest() {
  return reply({ ok: false, error: "请使用 POST" }, 405);
}
