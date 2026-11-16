
/**
 * Cloudflare Pages 全站密码保护 Middleware
 *
 * 访问方式：
 * https://xxx.pages.dev/?k=123456
 *
 * 环境变量（Cloudflare Dashboard 设置）：
 *
 * PASSWORD    : 网站访问密码
 * AUTH_SECRET : Cookie 签名密钥（建议 32 字节以上随机密钥）
 *
 * Cookie 有效期：7 天
 */

async function getAuthToken(env) {
    const encoder = new TextEncoder();

    // 使用 HMAC-SHA256 生成授权 Token
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

    // 转换为十六进制字符串
    return Array.from(new Uint8Array(signature))
        .map(b => b.toString(16).padStart(2, "0"))
        .join("");
}

export async function onRequest(context) {

    const { request, env, next } = context;

    // ==========================================
    // 1. 检查环境变量
    // ==========================================

    if (!env.PASSWORD || !env.AUTH_SECRET) {
        return new Response("Server configuration error", {
            status: 500
        });
    }

    const url = new URL(request.url);

    // ==========================================
    // 2. 生成授权 Token
    // ==========================================

    const authToken = await getAuthToken(env);

    // ==========================================
    // 3. 获取 URL 中的密码参数 k
    // ==========================================

    const inputPassword = url.searchParams.get("k");

    if (inputPassword !== null) {

        // 密码错误
        if (inputPassword !== env.PASSWORD) {
            return new Response(
                "403 Forbidden - Wrong Password",
                {
                    status: 403,
                    headers: {
                        "Content-Type": "text/plain; charset=UTF-8",
                        "Cache-Control": "no-store"
                    }
                }
            );
        }

        // ======================================
        // 4. 密码正确，设置授权 Cookie
        // ======================================

        const headers = new Headers();

        headers.append(
            "Set-Cookie",
            `pages_auth=${authToken}; Path=/; Max-Age=604800; HttpOnly; Secure; SameSite=Strict`
        );

        // 删除 k 参数，避免密码留在地址栏
        // 保留 URL 中的其他查询参数
        url.searchParams.delete("k");

        // 跳转到清理后的 URL
        headers.set("Location", url.toString());

        return new Response(null, {
            status: 302,
            headers
        });
    }

    // ==========================================
    // 5. 检查 Cookie 授权
    // ==========================================

    const cookie = request.headers.get("Cookie") || "";

    const match = cookie.match(
        /(?:^|;\s*)pages_auth=([a-f0-9]+)/
    );

    // Cookie 正确，允许访问
    if (match && match[1] === authToken) {
        return next();
    }

    // ==========================================
    // 6. 未授权，禁止访问
    // ==========================================

    return new Response(
        `<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
                "Content-Type": "text/html; charset=UTF-8",
                "Cache-Control": "no-store"
            }
        }
    );
}
