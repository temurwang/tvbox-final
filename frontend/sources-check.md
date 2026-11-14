# Source check (2026-11-14T03:15:58+00:00)

- untrusted source files: 83/100 parsed
- code-search requests: 9

  - `sites spider extension:json tvbox` page 1: HTTP 200, items 100
  - `sites spider extension:json tvbox` page 2: HTTP 200, items 100
  - `sites spider extension:json tvbox` page 3: HTTP 200, items 100
  - `sites api csp_ extension:json` page 1: HTTP 200, items 100
  - `sites api csp_ extension:json` page 2: HTTP 200, items 100
  - `sites api csp_ extension:json` page 3: HTTP 200, items 100
  - `api_site cache_time extension:json` page 1: HTTP 200, items 100
  - `api_site cache_time extension:json` page 2: HTTP 200, items 100
  - `api_site cache_time extension:json` page 3: HTTP 200, items 19

| source | trusted | status | found | candidates | passed | in output | fastest ms |
|---|---|---|---|---|---|---|---|
| seed.json | yes | loaded (40 non-API sites kept as-is, 0 dropped) | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/once678/looktv/eb7a8709934f54c969db84f26f949e7d2fbd6029/tvbox.json | no | parsed | 4 | 1 | 0 | 0 | - |
| https://raw.githubusercontent.com/Qiuyebai-1226/LittleTools/cd9f839366e2375dfe495fb97fdd8fb094a3e57d/tvbox.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/cspoh123/tvbox/cbab4e0ed2ed85254c3010e277f8addaf9dc35ba/tvbox.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/jessic01/box1/bb7d749d3eb60b5b5cbf83527eba65ab0db6a37f/tvbox.json | no | parsed | 27 | 17 | 2 | 2 | 302 |
| https://raw.githubusercontent.com/swirldawn/swirldawn.github.io/efe8c649f8f175a3352b9474ff6215efb7c1cc0c/tvbox.json | no | parsed | 50 | 27 | 5 | 5 | 141 |
| https://raw.githubusercontent.com/ylxdy/IPTV/a12b085cfe580069830c7aa7e7394213d80e03d8/tvbox.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/cyao2q/files/c0ffe93dc110fd4f3f703a7dc07cd1f3fb97d91c/xs.json | no | parsed | 2 | 1 | 1 | 1 | 1300 |
| https://raw.githubusercontent.com/zys8119/react/7c18a538839e5f6b81aeebf2daa8e692290faadc/tvbox.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/FreeDTV/FreeD/2511407b95ec434cf5d9e65f36aac63141c4a7ba/box.json | no | parsed | 1 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/qcfree/BOXZY/2bf39cf14e83f6939d92cdd4cbb09a5ba63b244b/tvbox.json | no | parsed | 27 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/qirenzhidao/tvbox18/86e1e39338ae41fcbceb9d0d3896a7618ced6cd6/ok/ok.json | no | parsed | 5 | 4 | 2 | 2 | 106 |
| https://raw.githubusercontent.com/franksun1211/TVBOX/aac9dfb5393890d61b9566b6c09d7d710b8f1347/sun.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/franksun1211/TVBOX/aac9dfb5393890d61b9566b6c09d7d710b8f1347/fuli.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/xiongjian83/TvBox/3b438d985cef3923068243c28d12e5d9f242b46d/19.json | no | parsed | 126 | 62 | 7 | 7 | 625 |
| https://raw.githubusercontent.com/xiongjian83/TvBox/3b438d985cef3923068243c28d12e5d9f242b46d/YZ.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/franksun1211/TVBOX/aac9dfb5393890d61b9566b6c09d7d710b8f1347/box.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/qirenzhidao/tvbox18/86e1e39338ae41fcbceb9d0d3896a7618ced6cd6/adult.json | no | parsed | 76 | 13 | 3 | 3 | 177 |
| https://raw.githubusercontent.com/Mainstayz/box/dc3f999dd5caf6b1b917873295256c99ae5b773c/tvbox.json | no | parsed | 14 | 4 | 0 | 0 | - |
| https://raw.githubusercontent.com/xiongjian83/TvBox/3b438d985cef3923068243c28d12e5d9f242b46d/X.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/shichuanenhui/TvBox/244c9d86055f93ad73cd8590030932f0c5f79e0e/fty.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/artxia/artxia.github.io/2fb7a503f868a52ba239e5f0511aed38c30f3c9a/tvbox.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/Henrytuan/tvbox/72894eca97dbc88d0c4a9bd3eb098d1fc75a0757/tvbox.json | no | parsed | 1 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/zhuxinfu88/tvlist/cea7e42b01dc89f57b894d54cbac511c5bf4e61b/jar/0.json | no | parsed | 4 | 2 | 1 | 1 | 179 |
| https://raw.githubusercontent.com/AlanTse1314/TVBox-18/1d88f6dc52a0de19a217d477f131cd8afd963f43/tvbox2.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/alantang1977/pg/1f1dfba29adc052a245b3aeac38b8df6b7fb7a58/all.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/AlanTse1314/Dong-learn9-TVBox-zyjk/a833ae2d536a600c736bf403117ad322f5fe6cbf/tvbox2.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/swhtv/111/86d67db59d229aea487c3bbf1cc4533836bb63a8/hua2.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/jigedos/geekcomputers/37b365174b6e3205dc881880c4396f2ef2e75028/630.json | no | parsed | 2 | 1 | 0 | 0 | - |
| https://raw.githubusercontent.com/cysk003/Yoursmile7_TVBox/135b44c68587dfe980c8f2be996edccf63f0108b/XC.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/cymcn/myTVBox/77eca3f31b4ff026043b664b8be81ce8607205fc/XC.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/yohaa0/yscang/046e0008e718d3457e4d31c198eb000ee4bf377a/XC.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/lubin776/tvbox/27ec79a0c39beaaf23dc8d668213e6a26dfe891f/0/b.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/jyoketsu/tv/935e9113f1972b5b2ee0cfa4abb974a93dc78de4/m.json | no | parsed | 15 | 12 | 2 | 2 | 264 |
| https://raw.githubusercontent.com/tiantaiyx/tvbox/d97a57c12bc0ac189cda5acfe530394e03d80371/0706.json | no | parsed | 2 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/tiantaiyx/tvbox/d97a57c12bc0ac189cda5acfe530394e03d80371/0701.json | no | parsed | 3 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/cnnbgo/tvbox/cf31cb7a0186eab20588db391e7b83695d71918a/x.json | no | parsed | 74 | 9 | 0 | 0 | - |
| https://raw.githubusercontent.com/hanhan8127/TVBox/b90234729fc311a1ab928401ccf139d4ce335b0a/hanXC.json | no | parsed | 9 | 6 | 5 | 5 | 366 |
| https://raw.githubusercontent.com/zyscdx/tvbox/e5f6e290f664356ba6c4132f6b5fa088dacabc5d/fhvk.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/1771245847/TvBox/573561625caeca03d90381af36911972eefb76af/cyys.json | no | parsed | 8 | 5 | 2 | 2 | 994 |
| https://raw.githubusercontent.com/franksun1211/TVBOX/aac9dfb5393890d61b9566b6c09d7d710b8f1347/0903.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/yueer59/Tvbox/74ee1483b67e73767fe67bf3a2d4d6502c4cafcd/api.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/lmlmi/xxxx/453b2de69db1bc9a2221a9662766d7461b4f7c08/wq18.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/ne7359/tvurl/81d0ddce5731a773ff559835778cb198499e63f0/js.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/wlcmc1972/tvbox/d4280d0b88dda6a4891a08fad224a551c4442924/t2.json | no | parsed | 14 | 6 | 4 | 4 | 111 |
| https://raw.githubusercontent.com/swhtv/111/86d67db59d229aea487c3bbf1cc4533836bb63a8/hua.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/13998394872/TVBox/b01776dccb8d49b6b8fca60657a95bfd84196d44/PF.json | no | parsed | 69 | 9 | 4 | 4 | 76 |
| https://raw.githubusercontent.com/a736240087/tvbox/5e6ebbfc744747104f9c214a33935ee533a15ad5/2.json | no | parsed | 5 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/lmlmi/xxxx/453b2de69db1bc9a2221a9662766d7461b4f7c08/888.json | no | parsed | 86 | 3 | 0 | 0 | - |
| https://raw.githubusercontent.com/yueer59/Tvbox/74ee1483b67e73767fe67bf3a2d4d6502c4cafcd/api2.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/guot55/yg/0e6ace4a7aafe49cf2b12d718f0b8cb11eeee6eb/jsm.json | no | parsed | 8 | 2 | 1 | 1 | 112 |
| https://raw.githubusercontent.com/s14685/tv/ba297bfa6cc669ab89a55dc8c543831af1c022c4/xc.json | no | parsed | 4 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/ncnc8388/ncnc8388.github.io/705bc46fd1ecc911cce265699d4f0f768d9f009d/0730.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/lubin776/tvbox/27ec79a0c39beaaf23dc8d668213e6a26dfe891f/gx/0.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/habao260/zy/287cebc8a02d04faa5772b4c99a778f9d59f8110/2023.json | no | parsed | 4 | 1 | 0 | 0 | - |
| https://raw.githubusercontent.com/FeiWang1119/dotfiles/9fe37adc5acf910ee4bed17a41de6a859f8533a8/tvbox/n.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/jj00780078/jj00780078.github.io/5a4fe1d3819292772c6f0930f6f7c880a3d3e177/a5.json | no | parsed | 1 | 1 | 0 | 0 | - |
| https://raw.githubusercontent.com/KTogithub/TVBox/f7e0d83bffe8eb719389fd103f90b8c05440dabb/JS/js.json | no | parsed | 2 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/c120487/00/557e71b0753c5e6702023d683fa7d4fb7ab7bdd7/vip.json | no | parsed | 41 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/lmlmi/xxxx/453b2de69db1bc9a2221a9662766d7461b4f7c08/PRO.json | no | parsed | 47 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/phoenix7750/iptv/3ec65ac32b10e3a9b4d25d22075eecdfdfa3b281/tsq.json | no | parsed | 1 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/swhtv/111/86d67db59d229aea487c3bbf1cc4533836bb63a8/fj.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/wxz52155/TVBOXZY3/1dead3d0078ba6864d9dc8ded5eb4b46f2570b7b/sp.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/kcjsd/TVBOXZY/1fe21df6951ac329ec80fce9e26956440992cdb9/18.json | no | parsed | 41 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/treysiz/treysiz.github.io/76b8bbaf78bf30cb28c05bbc47fa2aa9ac3185ca/NEW.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/tv189ymail/2023/733130dbe85b924da2d7092be1e69b97bb877cce/6/18.json | no | parsed | 53 | 6 | 0 | 0 | - |
| https://raw.githubusercontent.com/13998394872/TVBox/b01776dccb8d49b6b8fca60657a95bfd84196d44/PG.json | no | parsed | 10 | 2 | 2 | 2 | 48 |
| https://raw.githubusercontent.com/ellondoa/Yoursmile7-TVBox/42a9a6b6db2d01d1f8eabf40eb525cc1aa652696/XC.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/yw88075/tvbox/5df857abc263fda3c3e6cb1c285229f4d5e02230/yw.json | no | parsed | 20 | 6 | 3 | 3 | 153 |
| https://raw.githubusercontent.com/Newtxin/tvbox/d07b4c987056fba4af1ce5ca7c139161c9b11972/015.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/yw88075/tvbox/5df857abc263fda3c3e6cb1c285229f4d5e02230/dr/js.json | no | parsed | 2 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/nxjonson/za/aa762e4c3ef75ea026915ad7a05853cbcc858085/XC.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/xiaolvdouya/zhiboyuan/7c6d1feb56604819b16c1d4751a40a32c04ae625/N1.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/jigedos/geekcomputers/37b365174b6e3205dc881880c4396f2ef2e75028/0717.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/jane3824/TV/84d2da9193231bc34dda9c95780e4cb36c635e1b/fm.json | no | parsed | 5 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/chengxue2020/Cat-ports/422ee53167adebf2f22d708bc9e38e594ccd3eed/alist.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/SuperTreasure/tvbox/323f88979740aabb9b7792456cb13a9b035c0fe0/api.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/ciihom/tvbox/5d9bc285000dbec5008b48d2166068c8f09c5936/box.json | no | parsed | 21 | 12 | 4 | 4 | 86 |
| https://raw.githubusercontent.com/jixiejishu/zytzx/ef0d8ce1a08bb4ef250feb32788b1deae012236c/ftyzx.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/ncnc8388/ncnc8388.github.io/705bc46fd1ecc911cce265699d4f0f768d9f009d/0805.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/ncnc8388/ncnc8388.github.io/705bc46fd1ecc911cce265699d4f0f768d9f009d/0806.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/guot55/yg/0e6ace4a7aafe49cf2b12d718f0b8cb11eeee6eb/pro.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/520ad/tvbox/804a8642f4e8bf660752217f75e0cd804f5ee71a/2.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/c120487/00/557e71b0753c5e6702023d683fa7d4fb7ab7bdd7/js0.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/hutiang/MyTvBox/e6d622a219f752db908ba06b90678536f04bcb30/1.json | no | parsed | 1 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/ncnc8388/ncnc8388.github.io/705bc46fd1ecc911cce265699d4f0f768d9f009d/alist.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/cc202110/33/248621fb9c5b2e4de5d976b86c5190e6c18acf81/db.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/swhtv/111/86d67db59d229aea487c3bbf1cc4533836bb63a8/jl2.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/hjcmcn/z/82367491b4d7d4233030f62dd880e7737e7a8ee5/qj.json | no | parsed | 20 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/Yoursmile77/TVBox/99d8bb1a28116725329434c5f8bc83a6c558dab8/XC.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/Newtxin/tvbox/d07b4c987056fba4af1ce5ca7c139161c9b11972/0501.json | no | parsed | 9 | 2 | 1 | 1 | 1151 |
| https://raw.githubusercontent.com/jane3824/TV/84d2da9193231bc34dda9c95780e4cb36c635e1b/ok.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/13998394872/TVBox/b01776dccb8d49b6b8fca60657a95bfd84196d44/FM.json | no | parsed | 12 | 2 | 0 | 0 | - |
| https://raw.githubusercontent.com/mrhuanglearn/jdk_jar/0dc4850188755a2c4fbe489e438a39031048a093/XC.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/jessic01/box1/bb7d749d3eb60b5b5cbf83527eba65ab0db6a37f/xbpq.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/lmlmi/xxxx/453b2de69db1bc9a2221a9662766d7461b4f7c08/vip.json | no | parsed | 41 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/cnnbgo/tvbox/cf31cb7a0186eab20588db391e7b83695d71918a/zh/x.json | no | parsed | 74 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/smallmi18/smallmi/c764bdde2ae6e32e5a61f85b2ed6e56abbfadd67/js.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/fkaf1/fk/67e232dde107b43c422fa692e415ce02a5cfcc33/XC3.json | no | parsed | 1 | 1 | 1 | 1 | 170 |
| https://raw.githubusercontent.com/xibao999/x/c836dd27a08687548b3f5ba1061a2fc9dfa4b0d7/b.json | no | parsed | 2 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/hjcmcn/z/82367491b4d7d4233030f62dd880e7737e7a8ee5/18.json | no | not_json_object | 0 | 0 | 0 | 0 | - |

## Live sources

| name | url | reachable | ms |
|---|---|---|---|
| Gather「果」 | https://tv.tmxk.kdns.fr/yplrnuc7 | no | - |
