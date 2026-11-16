# Source check (2026-11-16T11:35:22+00:00)

- untrusted source files: 86/100 parsed
- code-search requests: 9

  - `sites spider extension:json tvbox` page 1: HTTP 200, items 100
  - `sites spider extension:json tvbox` page 2: HTTP 200, items 100
  - `sites spider extension:json tvbox` page 3: HTTP 200, items 100
  - `sites api csp_ extension:json` page 1: HTTP 200, items 100
  - `sites api csp_ extension:json` page 2: HTTP 200, items 100
  - `sites api csp_ extension:json` page 3: HTTP 200, items 100
  - `api_site cache_time extension:json` page 1: HTTP 200, items 100
  - `api_site cache_time extension:json` page 2: HTTP 200, items 100
  - `api_site cache_time extension:json` page 3: HTTP 200, items 17

| source | trusted | status | found | candidates | passed | in output | fastest ms |
|---|---|---|---|---|---|---|---|
| seed.json | yes | loaded (41 non-API sites kept as-is, 0 dropped) | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/once678/looktv/eb7a8709934f54c969db84f26f949e7d2fbd6029/tvbox.json | no | parsed | 4 | 1 | 0 | 0 | - |
| https://raw.githubusercontent.com/2hacc/TVBox/404e001bb06605a5e35ef8feed4d5db0b0d6bc96/oktv.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/qist/tvbox/f05cfcdfb266b6841dca3d1e42dfff50a18b6b3c/XYQ.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/qist/tvbox/f05cfcdfb266b6841dca3d1e42dfff50a18b6b3c/367.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/qist/tvbox/f05cfcdfb266b6841dca3d1e42dfff50a18b6b3c/0821.json | no | parsed | 7 | 6 | 4 | 4 | 183 |
| https://raw.githubusercontent.com/gaotianliuyun/gao/8213bb046f4dce746b5f2ddcddb13a336d0b0d60/XYQ.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/gaotianliuyun/gao/8213bb046f4dce746b5f2ddcddb13a336d0b0d60/0821.json | no | parsed | 7 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/Qiuyebai-1226/LittleTools/cd9f839366e2375dfe495fb97fdd8fb094a3e57d/tvbox.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/Dong-learn9/TVBox-zyjk/adb3ff7df4e0465c23bdf62b2c9536de25c08db2/18.json | no | parsed | 41 | 28 | 4 | 4 | 147 |
| https://raw.githubusercontent.com/cspoh123/tvbox/cbab4e0ed2ed85254c3010e277f8addaf9dc35ba/tvbox.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/gaotianliuyun/gao/8213bb046f4dce746b5f2ddcddb13a336d0b0d60/js.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/jessic01/box1/bb7d749d3eb60b5b5cbf83527eba65ab0db6a37f/tvbox.json | no | parsed | 27 | 3 | 0 | 0 | - |
| https://raw.githubusercontent.com/swirldawn/swirldawn.github.io/efe8c649f8f175a3352b9474ff6215efb7c1cc0c/tvbox.json | no | parsed | 50 | 26 | 4 | 4 | 87 |
| https://raw.githubusercontent.com/ylxdy/IPTV/a12b085cfe580069830c7aa7e7394213d80e03d8/tvbox.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/cyao2q/files/c0ffe93dc110fd4f3f703a7dc07cd1f3fb97d91c/xs.json | no | parsed | 2 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/Dong-learn9/TVBox-zyjk/adb3ff7df4e0465c23bdf62b2c9536de25c08db2/19.json | no | parsed | 22 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/FreeDTV/FreeD/2511407b95ec434cf5d9e65f36aac63141c4a7ba/box.json | no | parsed | 1 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/qcfree/BOXZY/2bf39cf14e83f6939d92cdd4cbb09a5ba63b244b/tvbox.json | no | parsed | 27 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/qirenzhidao/tvbox18/86e1e39338ae41fcbceb9d0d3896a7618ced6cd6/ok/ok.json | no | parsed | 5 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/franksun1211/TVBOX/8c617b6324645fd33e6bb70cc007b4a45fe29822/sun.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/franksun1211/TVBOX/8c617b6324645fd33e6bb70cc007b4a45fe29822/fuli.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/xiongjian83/TvBox/a09f1306102b577bf4f9b620abe822b3838b7f2a/19.json | no | parsed | 126 | 52 | 5 | 5 | 319 |
| https://raw.githubusercontent.com/xiongjian83/TvBox/a09f1306102b577bf4f9b620abe822b3838b7f2a/YZ.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/franksun1211/TVBOX/8c617b6324645fd33e6bb70cc007b4a45fe29822/box.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/Mainstayz/box/dc3f999dd5caf6b1b917873295256c99ae5b773c/tvbox.json | no | parsed | 14 | 4 | 0 | 0 | - |
| https://raw.githubusercontent.com/xiongjian83/TvBox/a09f1306102b577bf4f9b620abe822b3838b7f2a/X.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/shichuanenhui/TvBox/244c9d86055f93ad73cd8590030932f0c5f79e0e/fty.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/lubin776/0/b86cfa69ee20783d5c9ca24cbe6c7f68024561bc/0/c.json | no | parsed | 58 | 38 | 30 | 30 | 68 |
| https://raw.githubusercontent.com/niubihu1/tvbox/e8f569259d7dfa889b3f477258b64897fd35a643/1.json | no | parsed | 22 | 7 | 7 | 7 | 110 |
| https://raw.githubusercontent.com/alantang1977/pg/13667cbec4903e1444c6aa05ec4af2d6de779d82/all.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/AlanTse1314/Dong-learn9-TVBox-zyjk/a833ae2d536a600c736bf403117ad322f5fe6cbf/tvbox2.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/dlgt7/TVbox-interface/c759b853c633aa1f8a41b518b0f7988bfadbc017/jj.json | no | parsed | 23 | 14 | 6 | 6 | 237 |
| https://raw.githubusercontent.com/swhtv/111/86d67db59d229aea487c3bbf1cc4533836bb63a8/hua2.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/cysk003/Yoursmile7_TVBox/135b44c68587dfe980c8f2be996edccf63f0108b/XC.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/franksun1211/TVBOX/8c617b6324645fd33e6bb70cc007b4a45fe29822/FZL.json | no | parsed | 4 | 1 | 0 | 0 | - |
| https://raw.githubusercontent.com/cymcn/myTVBox/77eca3f31b4ff026043b664b8be81ce8607205fc/XC.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/yohaa0/yscang/046e0008e718d3457e4d31c198eb000ee4bf377a/XC.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/lubin776/tvbox/27ec79a0c39beaaf23dc8d668213e6a26dfe891f/0/b.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/zyscdx/tvbox/e5f6e290f664356ba6c4132f6b5fa088dacabc5d/fhvk.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/jyoketsu/tv/935e9113f1972b5b2ee0cfa4abb974a93dc78de4/m.json | no | parsed | 15 | 11 | 1 | 1 | 2520 |
| https://raw.githubusercontent.com/bluefriendCN/set/95e8952dad7c31a450b754a3b665c6221526e460/ma.json | no | parsed | 29 | 15 | 13 | 13 | 132 |
| https://raw.githubusercontent.com/tiantaiyx/tvbox/d97a57c12bc0ac189cda5acfe530394e03d80371/0706.json | no | parsed | 2 | 1 | 0 | 0 | - |
| https://raw.githubusercontent.com/lubin776/0/b86cfa69ee20783d5c9ca24cbe6c7f68024561bc/0/x5.json | no | parsed | 57 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/tiantaiyx/tvbox/d97a57c12bc0ac189cda5acfe530394e03d80371/0701.json | no | parsed | 3 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/cnnbgo/tvbox/cf31cb7a0186eab20588db391e7b83695d71918a/x.json | no | parsed | 74 | 8 | 0 | 0 | - |
| https://raw.githubusercontent.com/hanhan8127/TVBox/b90234729fc311a1ab928401ccf139d4ce335b0a/hanXC.json | no | parsed | 9 | 4 | 4 | 4 | 107 |
| https://raw.githubusercontent.com/1771245847/TvBox/e603cf6938131963cb906e0ee34b78550a5a9edf/cyys.json | no | parsed | 8 | 5 | 1 | 1 | 1072 |
| https://raw.githubusercontent.com/franksun1211/TVBOX/8c617b6324645fd33e6bb70cc007b4a45fe29822/0903.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/yueer59/Tvbox/74ee1483b67e73767fe67bf3a2d4d6502c4cafcd/api.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/lmlmi/xxxx/453b2de69db1bc9a2221a9662766d7461b4f7c08/wq18.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/ne7359/tvurl/5162772cef009612992dea2f6387ee8356ac7c13/js.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/wlcmc1972/tvbox/d4280d0b88dda6a4891a08fad224a551c4442924/t2.json | no | parsed | 14 | 2 | 0 | 0 | - |
| https://raw.githubusercontent.com/swhtv/111/86d67db59d229aea487c3bbf1cc4533836bb63a8/hua.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/a736240087/tvbox/5e6ebbfc744747104f9c214a33935ee533a15ad5/2.json | no | parsed | 5 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/13998394872/TVBox/b01776dccb8d49b6b8fca60657a95bfd84196d44/PF.json | no | parsed | 69 | 7 | 2 | 2 | 709 |
| https://raw.githubusercontent.com/lmlmi/xxxx/453b2de69db1bc9a2221a9662766d7461b4f7c08/888.json | no | parsed | 86 | 1 | 0 | 0 | - |
| https://raw.githubusercontent.com/bluefriendCN/set/95e8952dad7c31a450b754a3b665c6221526e460/md.json | no | parsed | 15 | 2 | 0 | 0 | - |
| https://raw.githubusercontent.com/yueer59/Tvbox/74ee1483b67e73767fe67bf3a2d4d6502c4cafcd/api2.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/s14685/tv/ba297bfa6cc669ab89a55dc8c543831af1c022c4/xc.json | no | parsed | 4 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/guot55/yg/0e6ace4a7aafe49cf2b12d718f0b8cb11eeee6eb/jsm.json | no | parsed | 8 | 2 | 1 | 1 | 289 |
| https://raw.githubusercontent.com/lubin776/tvbox/27ec79a0c39beaaf23dc8d668213e6a26dfe891f/gx/0.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/habao260/zy/287cebc8a02d04faa5772b4c99a778f9d59f8110/2023.json | no | parsed | 4 | 1 | 0 | 0 | - |
| https://raw.githubusercontent.com/hd9211/Tvbox1/8249890a2651ec3c64a36b9a40d3cfba304eab30/cr.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/jj00780078/jj00780078.github.io/421b6d514e5d5adfa1c5cdae9fd99efc75cdefd4/a5.json | no | parsed | 1 | 1 | 0 | 0 | - |
| https://raw.githubusercontent.com/c120487/00/557e71b0753c5e6702023d683fa7d4fb7ab7bdd7/vip.json | no | parsed | 41 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/lmlmi/xxxx/453b2de69db1bc9a2221a9662766d7461b4f7c08/PRO.json | no | parsed | 47 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/phoenix7750/iptv/3ec65ac32b10e3a9b4d25d22075eecdfdfa3b281/tsq.json | no | parsed | 1 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/swhtv/111/86d67db59d229aea487c3bbf1cc4533836bb63a8/fj.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/wxz52155/TVBOXZY3/1dead3d0078ba6864d9dc8ded5eb4b46f2570b7b/sp.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/kcjsd/TVBOXZY/1fe21df6951ac329ec80fce9e26956440992cdb9/18.json | no | parsed | 41 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/treysiz/treysiz.github.io/76b8bbaf78bf30cb28c05bbc47fa2aa9ac3185ca/NEW.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/tv189ymail/2023/733130dbe85b924da2d7092be1e69b97bb877cce/6/18.json | no | parsed | 53 | 6 | 0 | 0 | - |
| https://raw.githubusercontent.com/13998394872/TVBox/b01776dccb8d49b6b8fca60657a95bfd84196d44/PG.json | no | parsed | 10 | 2 | 1 | 1 | 214 |
| https://raw.githubusercontent.com/ellondoa/Yoursmile7-TVBox/42a9a6b6db2d01d1f8eabf40eb525cc1aa652696/XC.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/yw88075/tvbox/5df857abc263fda3c3e6cb1c285229f4d5e02230/yw.json | no | parsed | 20 | 4 | 0 | 0 | - |
| https://raw.githubusercontent.com/xiaolvdouya/zhiboyuan/7c6d1feb56604819b16c1d4751a40a32c04ae625/N1.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/Newtxin/tvbox/d07b4c987056fba4af1ce5ca7c139161c9b11972/015.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/nxjonson/za/aa762e4c3ef75ea026915ad7a05853cbcc858085/XC.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/jigedos/geekcomputers/37b365174b6e3205dc881880c4396f2ef2e75028/0717.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/jane3824/TV/84d2da9193231bc34dda9c95780e4cb36c635e1b/fm.json | no | parsed | 5 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/ncnc8388/ncnc8388.github.io/287820ea92cb6c65fd18cd6df5a9a5fa5e11ac8e/0805.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/ncnc8388/ncnc8388.github.io/287820ea92cb6c65fd18cd6df5a9a5fa5e11ac8e/0806.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/chengxue2020/Cat-ports/422ee53167adebf2f22d708bc9e38e594ccd3eed/alist.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/SuperTreasure/tvbox/323f88979740aabb9b7792456cb13a9b035c0fe0/api.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/ciihom/tvbox/5d9bc285000dbec5008b48d2166068c8f09c5936/box.json | no | parsed | 21 | 10 | 3 | 3 | 59 |
| https://raw.githubusercontent.com/ncnc8388/ncnc8388.github.io/287820ea92cb6c65fd18cd6df5a9a5fa5e11ac8e/alist.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/guot55/yg/0e6ace4a7aafe49cf2b12d718f0b8cb11eeee6eb/pro.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/520ad/tvbox/804a8642f4e8bf660752217f75e0cd804f5ee71a/2.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/c120487/00/557e71b0753c5e6702023d683fa7d4fb7ab7bdd7/js0.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/hutiang/MyTvBox/e6d622a219f752db908ba06b90678536f04bcb30/1.json | no | parsed | 1 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/swhtv/111/86d67db59d229aea487c3bbf1cc4533836bb63a8/jl2.json | no | not_json_object | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/Yoursmile77/TVBox/99d8bb1a28116725329434c5f8bc83a6c558dab8/XC.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/jane3824/TV/84d2da9193231bc34dda9c95780e4cb36c635e1b/ok.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/13998394872/TVBox/b01776dccb8d49b6b8fca60657a95bfd84196d44/FM.json | no | parsed | 12 | 2 | 0 | 0 | - |
| https://raw.githubusercontent.com/mrhuanglearn/jdk_jar/0dc4850188755a2c4fbe489e438a39031048a093/XC.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/Newtxin/tvbox/d07b4c987056fba4af1ce5ca7c139161c9b11972/0501.json | no | parsed | 9 | 2 | 1 | 1 | 1125 |
| https://raw.githubusercontent.com/lmlmi/xxxx/453b2de69db1bc9a2221a9662766d7461b4f7c08/vip.json | no | parsed | 41 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/cnnbgo/tvbox/cf31cb7a0186eab20588db391e7b83695d71918a/zh/x.json | no | parsed | 74 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/cc202110/33/248621fb9c5b2e4de5d976b86c5190e6c18acf81/db.json | no | parsed | 0 | 0 | 0 | 0 | - |
| https://raw.githubusercontent.com/smallmi18/smallmi/c764bdde2ae6e32e5a61f85b2ed6e56abbfadd67/js.json | no | parsed | 0 | 0 | 0 | 0 | - |

## Live sources

| name | url | reachable | ms |
|---|---|---|---|
| Gather「果」 | https://tv.tmxk.kdns.fr/yplrnuc7 | no | - |
