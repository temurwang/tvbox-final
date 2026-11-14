/**
 * MISSAV - OK影视 / drpy2 规则
 *
 * 来源：XPTV 原始 missav.js
 * 适用：OK影视 type=3
 *
 * 功能：
 * 1. 首页分类
 * 2. 分类视频列表
 * 3. 视频搜索
 * 4. 视频详情
 * 5. m3u8 播放地址解析
 *
 * 注意：
 * - 本规则使用 drpy2 内置的 request、pdfa、pdfh、pd 等函数。
 * - 原站可能存在 Cloudflare 验证，遇到验证页面时可能无法获取数据。
 */

var rule = {
    title: 'MISSAV',
    host: 'https://missav.ai',

    // 分类列表地址
    url: '/fyclass?page=fypage&sort=released_at',

    // 搜索地址
    searchUrl: '/cn/search/**?page=fypage',

    searchable: 2,
    quickSearch: 1,
    filterable: 1,

    // 播放地址为直接 m3u8
    play_parse: true,
    lazy: $js.toString(() => {
        input = {
            jx: 0,
            parse: 0,
            url: input,
            header: {
                'User-Agent': rule.headers['User-Agent'],
                'Referer': HOST + '/'
            }
        };
    }),

    headers: {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/604.1.14 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1',
        'Referer': 'https://missav.ai/'
    },

    // 分类名称
    class_name:
        '中文字幕&最近更新&新作上市&无码流出&VR&今日热门&本週热门&本月热门&' +
        'SIRO&LUXU&GANA&PRESTIGE PREMIUM&S-CUTE&ARA&FC2&HEYZO&东京热&一本道&' +
        'Caribbeancom&Caribbeancompr&10musume&pacopacomama&Gachinco&XXX-AV&人妻斩&' +
        '顽皮 4610&顽皮 0930&麻豆传媒&TWAV AV&Furuke AV',

    // 分类对应的站点路径
    class_url:
        'dm265/cn/chinese-subtitle&' +
        'dm513/cn/new&' +
        'dm509/cn/release&' +
        'dm561/cn/uncensored-leak&' +
        'dm2091/cn/genres/VR&' +
        'dm242/cn/today-hot&' +
        'dm168/cn/weekly-hot&' +
        'dm207/cn/monthly-hot&' +
        'dm23/cn/siro&' +
        'dm20/cn/luxu&' +
        'dm17/cn/gana&' +
        'dm14/cn/maan&' +
        'dm23/cn/scute&' +
        'dm19/cn/ara&' +
        'dm95/cn/fc2&' +
        'dm628/cn/heyzo&' +
        'dm29/cn/tokyohot&' +
        'dm58345/cn/1pondo&' +
        'dm124158/cn/caribbeancom&' +
        'dm1442/cn/caribbeancompr&' +
        'dm58632/cn/10musume&' +
        'dm668/cn/pacopacomama&' +
        'dm135/cn/gachinco&' +
        'dm26/cn/xxxav&' +
        'dm24/cn/marriedslash&' +
        'dm19/cn/naughty4610&' +
        'dm22/cn/naughty0930&' +
        'dm34/cn/madou&' +
        'dm17/cn/twav&' +
        'dm15/cn/furuke',

    limit: 24,

    // 请求头
    headers: {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_2 like Mac OS X) AppleWebKit/604.1.14 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1',
        'Referer': 'https://missav.ai/'
    },

    // 推荐页
    推荐: '*',

    /**
     * 一级页面：分类视频列表
     */
    一级: $js.toString(() => {
        var html = request(input, {
            headers: rule.headers
        });

        VODS = [];

        // 原始 XPTV 使用的列表选择器
        var items = pdfa(html, '.thumbnail');

        items.forEach(function (it) {
            var url = pd(
                it,
                '.text-secondary&&href',
                HOST
            );

            var title = pdfh(
                it,
                '.text-secondary&&Text'
            );

            var pic = pd(
                it,
                '.w-full&&data-src',
                HOST
            );

            var remark = pdfh(
                it,
                '.left-1&&Text'
            );

            var duration = pdfh(
                it,
                '.right-1&&Text'
            );

            if (!url || !title) {
                return;
            }

            VODS.push({
                vod_id: url,
                vod_name: title.trim().replace(/\s+/g, ' '),
                vod_pic: pic || '',
                vod_remarks: [
                    remark,
                    duration
                ].filter(Boolean).join(' ')
            });
        });
    }),

    /**
     * 搜索
     */
    搜索: $js.toString(() => {
        var html = request(input, {
            headers: rule.headers
        });

        VODS = [];

        var items = pdfa(html, '.thumbnail');

        items.forEach(function (it) {
            var url = pd(
                it,
                '.text-secondary&&href',
                HOST
            );

            var title = pdfh(
                it,
                '.text-secondary&&Text'
            );

            var pic = pd(
                it,
                '.w-full&&data-src',
                HOST
            );

            var remark = pdfh(
                it,
                '.left-1&&Text'
            );

            var duration = pdfh(
                it,
                '.right-1&&Text'
            );

            if (!url || !title) {
                return;
            }

            VODS.push({
                vod_id: url,
                vod_name: title.trim().replace(/\s+/g, ' '),
                vod_pic: pic || '',
                vod_remarks: [
                    remark,
                    duration
                ].filter(Boolean).join(' ')
            });
        });
    }),

    /**
     * 二级页面：视频详情和播放地址
     */
    二级: $js.toString(() => {
        var detailUrl = input;

        var html = request(detailUrl, {
            headers: rule.headers
        });

        // 视频标题
        var title =
            pdfh(html, 'h1&&Text') ||
            pdfh(html, 'title&&Text') ||
            'MISSAV';

        // 视频封面
        var pic =
            pdfh(html, 'meta[property="og:image"]&&content') ||
            pdfh(html, 'meta[name="twitter:image"]&&content') ||
            '';

        // 视频描述
        var desc =
            pdfh(html, 'meta[name="description"]&&content') ||
            '';

        var playUrls = [];

        /*
         * 原始 XPTV 的 UUID 提取方式：
         *
         * surrit.com\/UUID\/seek\/_0.jpg
         *
         * 网页中可能出现转义形式，也可能出现普通 URL 形式，
         * 因此这里分别匹配。
         */
        var uuidMatch = html.match(
            /surrit\.com\\\/([^\\/"']+)\\\/seek\\\/_0\.jpg/i
        );

        if (!uuidMatch) {
            uuidMatch = html.match(
                /surrit\.com\/([^\/"']+)\/seek\/_0\.jpg/i
            );
        }

        // 备用匹配
        if (!uuidMatch) {
            uuidMatch = html.match(
                /surrit\.com\\\/([^\\/"']+)/i
            );
        }

        if (!uuidMatch) {
            uuidMatch = html.match(
                /surrit\.com\/([^\/"']+)/i
            );
        }

        if (uuidMatch && uuidMatch[1]) {
            var uuid = uuidMatch[1];

            // 播放列表地址
            var playlistUrl =
                'https://surrit.com/' +
                uuid +
                '/playlist.m3u8';

            var playlist = request(playlistUrl, {
                headers: {
                    'User-Agent': rule.headers['User-Agent'],
                    'Referer': detailUrl
                }
            });

            var lines = String(playlist || '').split(/\r?\n/);

            // 提取不同清晰度的视频流
            lines.forEach(function (line) {
                line = line.trim();

                if (!line || line.indexOf('/video.m3u8') < 0) {
                    return;
                }

                var name = line
                    .replace('/video.m3u8', '')
                    .replace(/^.*\//, '')
                    .replace(/[^a-zA-Z0-9_-]/g, '');

                if (!name) {
                    name = '默认清晰度';
                }

                var playUrl;

                if (/^https?:\/\//i.test(line)) {
                    playUrl = line;
                } else {
                    playUrl =
                        'https://surrit.com/' +
                        uuid +
                        '/' +
                        line.replace(/^\/+/, '');
                }

                playUrls.unshift(
                    name + '$' + playUrl
                );
            });

            // 自动播放列表
            playUrls.push(
                '自动$' + playlistUrl
            );
        }

        VOD = {
            vod_id: detailUrl,
            vod_name: title.trim(),
            vod_pic: pic,
            vod_content: desc,
            vod_play_from: playUrls.length ? 'MISSAV' : '',
            vod_play_url: playUrls.join('#')
        };
    })
};
