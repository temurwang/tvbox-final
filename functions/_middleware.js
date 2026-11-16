
/**
 * Cloudflare Pages 全站密码保护
 *
 * 访问方式：
 * https://xxx.pages.dev/frontend/subscribe.json?k=1234567890
 *
 * 环境变量：
 * PASSWORD    : 网站访问密码
 * AUTH_SECRET : Cookie 签名密钥
 *
 * 特点：
 * 1. 不再使用 302 重定向
 * 2. URL 参数 k 正确时直接返回请求内容
 * 3. 浏览器可以使用 Cookie 授权
 * 4. 兼容不支持 Cookie 的订阅客户端
 */

// 生成 HMAC-SHA256 授权 Token
async function getAuthToken(env) {
    const encoder = new TextEncoder();

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

    // 1. 检查环境变量
    if (!env.PASSWORD || !env.AUTH_SECRET) {
        return new Response("Server configuration error", {
            status: 500
        });
    }

    const url = new URL(request.url);

    // 2. 获取 URL 密码参数
    const inputPassword = url.searchParams.get("k");

    // 3. URL 携带密码时，直接验证
    if (inputPassword !== null) {

        // 密码错误
        if (inputPassword !== env.PASSWORD) {
            return new Response("403 Forbidden - Wrong Password", {
                status: 403,
                headers: {
                    "Content-Type": "text/plain; charset=UTF-8",
                    "Cache-Control": "no-store"
                }
            });
        }

        // 密码正确，直接执行后续请求
        // 不重定向，不删除 k 参数
        const response = await next();

        // 同时设置 Cookie，方便浏览器后续访问
        const authToken = await getAuthToken(env);

        const newResponse = new Response(
            response.body,
            response
        );

        newResponse.headers.append(
            "Set-Cookie",
            `pages_auth=${authToken}; Path=/; Max-Age=604800; HttpOnly; Secure; SameSite=Lax`
        );

        return newResponse;
    }

    // 4. 没有 URL 密码时，检查 Cookie
    const cookie = request.headers.get("Cookie") || "";

    const match = cookie.match(
        /(?:^|;\s*)pages_auth=([a-f0-9]+)/
    );

    if (match) {
        const authToken = await getAuthToken(env);

        if (match[1] === authToken) {
            return next();
        }
    }

    // 5. 未授权，禁止访问
    return new Response(
        "403 Forbidden - Access Denied",
        {
            status: 403,
            headers: {
                "Content-Type": "text/plain; charset=UTF-8",
                "Cache-Control": "no-store"
            }
        }
    );
}
