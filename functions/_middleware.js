
/**
 * Cloudflare Pages 全站密码保护
 *
 * 访问方式：
 * https://xxx.pages.dev/?password=123456
 *
 * 环境变量：
 * PASSWORD    : 网站访问密码
 * AUTH_SECRET : Cookie 签名密钥
 */

async function getAuthToken(env) {
    const encoder = new TextEncoder();

    // 使用 HMAC-SHA256 生成授权 Cookie
    const key = await crypto.subtle.importKey(
        "raw",
        encoder.encode(env.AUTH_SECRET),
        {
            name: "HMAC",
            hash: "SHA-256"
        },
        false,
        ["sign"]
    );

    const signature = await crypto.subtle.sign(
        "HMAC",
        key,
        encoder.encode("pages-auth:" + env.PASSWORD)
    );

    return Array.from(new Uint8Array(signature))
        .map(b => b.toString(16).padStart(2, "0"))
        .join("");
}

export async function onRequest(context) {
    const { request, env, next } = context;

    // 必须配置两个环境变量
    if (!env.PASSWORD || !env.AUTH_SECRET) {
        return new Response("Server configuration error", {
            status: 500
        });
    }

    const url = new URL(request.url);
    const inputPassword = url.searchParams.get("k");

    const authToken = await getAuthToken(env);

    // 1. 用户通过 URL 参数输入密码
    if (inputPassword !== null) {

        if (inputPassword !== env.PASSWORD) {
            return new Response("403 Forbidden - Wrong Password", {
                status: 403,
                headers: {
                    "Content-Type": "text/plain; charset=UTF-8"
                }
            });
        }

        // 密码正确，设置授权 Cookie
        const headers = new Headers({
            "Location": url.origin + url.pathname +
                (url.hash || "")
        });

        headers.append(
            "Set-Cookie",
            `pages_auth=${authToken}; Path=/; Max-Age=604800; HttpOnly; Secure; SameSite=Strict`
        );

        // 去掉 URL 中的密码，避免继续暴露
        return new Response(null, {
            status: 302,
            headers
        });
    }

    // 2. 检查已有 Cookie
    const cookie = request.headers.get("Cookie") || "";

    const match = cookie.match(/(?:^|;\s*)pages_auth=([a-f0-9]+)/);

    if (match && match[1] === authToken) {
        return next();
    }

    // 3. 未授权访问
    return new Response(
        `<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>403 Forbidden</title>
</head>
<body>
<h2>访问被拒绝</h2>
<p>请使用正确的密码访问网站。</p>
</body>
</html>`,
        {
            status: 403,
            headers: {
                "Content-Type": "text/html; charset=UTF-8"
            }
        }
    );
}

