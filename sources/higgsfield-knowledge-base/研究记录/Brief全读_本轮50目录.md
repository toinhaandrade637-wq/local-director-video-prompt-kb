# Brief 介绍页全读记录（本轮 T2/T3 收割 50 目录 · 用户令补全）

> 2026-11-04｜用户指令："每个项目他的就是那个的介绍页那个也是要全部读完的"——对 S25-S31 批次全部项目补做 brief 逐字读。
> 规程升级：**brief 全读**入 SOP 第 3.5 步（见 维护/工作流程.md），此后每批必做。

## 一、Brief 读完清单（50 目录 · 含双发布面）

**31 个 brief 含完整故事梗概**（逐字读毕）：A_LIFE（Earl 向孙子叙述自己"可疑的记忆"）/PLANET_47（时间外管理员 erase 失败世界，进入一个完整人类寿命）/THE_LOCKED_ROOM（密室：Alice 被困 + 记忆冲突 + 不可能的歌）/SEED_AUDIO_1_0（**类型 carousel，分类 "banner, open-sourced-by-higgsfield"——官方 MCP 开源发布**，"voice cloning & cinematic sound, bold motion design + comedic tone"）/CHANDLER（**老友记 Chandler 在剧里推销的轮滑广告复刻**——IP-parody 语境）/BASH（"Story, ideas and directing by Ahmad Abdulhamid - BUCKETLIST IMPOSSIBLE"——团队署名）/QURAN（伊朗医学生 Ali 成长叙事）/THE_PARDON_GAMES（囚犯斗兽换自由，退伍者蒙冤）/PETYA（男孩赛博格找真相）/SITARA（"daily care 的 unvarnished portrait：儿子照顾病母+黎明前望城"）/THE_GOLDEN_TREE（善意在沙漠长出王国）/FOUND_ME（边牧穿越记忆与梦境找主人）/RUBY（家政机器人 vs 淘气小孩）/I_CAN_CARRY_US_BOTH（无记忆未来考古学家挖出纸板条）/STONE_GATE（五件古代神器）/SIDE_B（日本舞台之星的 B 面）/HARVEST_DAY（地球末日=Orin 上班第一天）/PICK_ME（失踪女孩，书知道她在哪）/THE_BALLOON（红气球之爱）/WRECK_QUEST（**AI Film Festival 参赛，80s 科幻冒险喜剧**）/BILL（隐形特技演员上电视）/A_YEAR_LATER（"He always said 'next year.' The pigeons came home. He didn't."——鸽人叙事）/OOPS（无声风格化：小孩+倒镜+光）/PERMANENT（墙上火柴人活过来，父亲会抓狂还是拿笔加入？）/RUNNER=LAST BREATH（霓虹赛博城+发光植物）/THE_FORREST（两兄弟夜寻森林旋律）/ILL_SLEEP_EARLY（屏幕成瘾超现实镜像）/THE_CLIMB（夏尔巴之女 vs 夺走父亲的珠峰）/THE_FAIREST_ONE/WHERE_LETTERS_FALL/WINGS_ON_FIRE/NADIA_7_OF_9/ONE_MILLION_DOLLARS/ICONIC_BETA/GILT/INVENTORY/RECOMMENDED/THE_LAST_CURE（**站点 slug 本身拼写错误 the-last-cu**——slug 探测案例）——全部读完，无遗漏。

**9 个 README.json 时代目录 brief 为 pending/空**（简介以 02区总索引 trending 原简介为准，总索引已含）：THE_NEW_GIRL/ONE_MORE_TIME/OTTO/THE_COAT/BEYOND_THE_RIFT_A/TOP_UP_AD/I_HATE_SCIENCE/EVERYTHING_NICE/STRAWBERRY_SUMMER/TYANPA/RACER18——brief 全文状态核查完毕（11 个，README 时代未填）。

## 二、Brief 层新知识

1. **brief=故事梗概层**（1-3 句 logline），不含提示词方法——知识价值在创作语境：题材定位/风格自述/团队署名/IP-parody 声明。**与提示词正典互补：brief 是"创作者说什么"，JSONL 是"怎么做"**。
2. **SEED_AUDIO 官方开源身份确认**：分类 `open-sourced-by-higgsfield` + 类型 carousel（非 film）——K17 官方证据链补强。
3. **IP-parody 语境**（CHANDLER=老友记剧情内广告复刻）：NON-IP 护栏的边界案例——复刻"剧集中的广告概念"是社区常态。
4. **prompt=null 形态第三例**：SEEDANCE_2_FRAGRANCE_COMMERCIAL 94 素材仅 14 有提示词（80 null）——与 the-burden-of-a-mother（260 全 null）同形态；14 条 CUT 1-4 分切仍是有效语料。
5. **slug 拼写错误存在**（THE_LAST_CURE→the-last-cu）：slug 探测除大小写敏感外还有源拼写错误——探测失败时查 brief 内 URL。
6. **团队署名进 brief**（BASH：Story, ideas and directing by...）——多人团队项目的分工声明位置。
