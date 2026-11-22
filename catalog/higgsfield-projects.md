# Higgsfield 全量项目索引

> 611 个项目的去重提示词全集。每个项目一份 `prompts.jsonl.gz`（每行一条，字段 `id/cat/type/model/prompt`），项目文档在 `sources/higgsfield/projects/<项目>/`。
> 检索单条提示词请用 `catalog/higgsfield-prompts.index.jsonl`，不要逐个解压项目文件。

共 **611** 个项目、**174,404** 条去重提示词，原文 **816 MB**，压缩后 **214 MB**。

## 怎么读

1. 按下表找项目，或用 `docs/02-任务路由.md` 先定任务。
2. 单条检索：`python tools/kb.py search --source higgsfield --project <项目> --limit 10`。
3. 取全文：`python tools/kb.py get --id HFX-<项目>-000001`。
4. 整项目通读：`zcat sources/higgsfield/prompts/<项目>/prompts.jsonl.gz`（Windows 用 Python 解压）。

## 项目总表

| 项目 | 主题 | 提示词 | 视频/图片 | 主要模型 | 文档 |
|---|---|---:|---|---|---|
| [VENGEANCE_IS_MINE](../sources/higgsfield/prompts/VENGEANCE_IS_MINE/) | — | 5,501 | 4219/1282 | seedance_2_0×4023、seedream_v5_pro×857、recraft_v4_1×267 | — |
| [ONEIRIC](../sources/higgsfield/prompts/ONEIRIC/) | 梦境家庭剧，GLOBAL LOCK 特性工程学 | 3,247 | 2450/765 | seedance_2_0×2068、soul_cinematic×380、seedream_v5_pro×240 | [docs](../sources/higgsfield/projects/ONEIRIC/) |
| [CULLY_HILL_BOYS](../sources/higgsfield/prompts/CULLY_HILL_BOYS/) | 音乐犯罪喜剧，五件套表演法（OBJECTIVE-TACTIC-SUBTEXT-STA | 3,174 | 0/0 | 未标注 | [docs](../sources/higgsfield/projects/CULLY_HILL_BOYS/) |
| [KOK_BORU_FILM](../sources/higgsfield/prompts/KOK_BORU_FILM/) | 同题材成片版，中文【标签】体系+反光滑铁律 | 2,436 | 0/15 | seedream_v5_pro×9、nano_banana_2×3、seedream_v4_5×2 | [docs](../sources/higgsfield/projects/KOK_BORU_FILM/) |
| [DETOUR](../sources/higgsfield/prompts/DETOUR/) | 街头赛车动作片（导航故障引发的公路竞速），v2-final 三轮对账 6161 件 | 2,173 | 829/1343 | seedance_2_5×784、seedream_v5_pro×707、gpt_image_2×335 | [docs](../sources/higgsfield/projects/DETOUR/) |
| [HELL_GRIND](../sources/higgsfield/prompts/HELL_GRIND/) | 奇幻悲剧，生物五件套设计法 | 1,861 | 600/491 | seedance_2_0×549、nano_banana_2×274、imagegen_2_0×91 | [docs](../sources/higgsfield/projects/HELL_GRIND/) |
| [CHARLIE_BOY](../sources/higgsfield/prompts/CHARLIE_BOY/) | — | 1,723 | 570/1153 | text2image_soul_v2×651、seedance_2_5×569、seedream_v5_pro×335 | [docs](../sources/higgsfield/projects/CHARLIE_BOY/) |
| [ADILIADA](../sources/higgsfield/prompts/ADILIADA/) | 类型模仿语法（黑帮片致敬） | 1,698 | 228/70 | seedance_2_0×190、nano_banana_2×52、soul_cinematic×34 | [docs](../sources/higgsfield/projects/ADILIADA/) |
| [APEIROPHOBIA](../sources/higgsfield/prompts/APEIROPHOBIA/) | — | 1,691 | 460/1230 | nano_banana_2×1114、seedance_2_5×415、gpt_image_2×115 | [docs](../sources/higgsfield/projects/APEIROPHOBIA/) |
| [ONE_THE_MERCY_LEDGER](../sources/higgsfield/prompts/ONE_THE_MERCY_LEDGER/) | — | 1,517 | 0/0 | videotape-alpha×1033、default×399、video_extension×57 | — |
| [ANERNEQ](../sources/higgsfield/prompts/ANERNEQ/) | — | 1,447 | 1178/269 | seedance_2_5×1061、text2image_soul_v2×167、soul_cinematic×116 | — |
| [CANE_MAN](../sources/higgsfield/prompts/CANE_MAN/) | — | 1,367 | 1124/243 | seedance_2_5×1124、seedream_v5_pro×240、nano_banana_2×2 | [docs](../sources/higgsfield/projects/CANE_MAN/) |
| [PASSPORT_RUSH](../sources/higgsfield/prompts/PASSPORT_RUSH/) | — | 1,193 | 891/302 | seedance_2_5×879、text2image_soul_v2×182、seedream_v5_pro×114 | [docs](../sources/higgsfield/projects/PASSPORT_RUSH/) |
| [VOICES_IN_THE_VOID](../sources/higgsfield/prompts/VOICES_IN_THE_VOID/) | — | 1,126 | 302/824 | seedream_v5_pro×494、seedance_2_5×279、seedream_v5_lite×179 | [docs](../sources/higgsfield/projects/VOICES_IN_THE_VOID/) |
| [HARMONY](../sources/higgsfield/prompts/HARMONY/) | — | 1,087 | 496/590 | nano_banana_2×283、seedance_2_5×213、cinematic_studio_video_4_0×206 | [docs](../sources/higgsfield/projects/HARMONY/) |
| [4K_BLOCKBUSTER_BREAKDOWN](../sources/higgsfield/prompts/4K_BLOCKBUSTER_BREAKDOWN/) | 片中片循环大片（场景×分辨率×版本矩阵，全站最大 13491 件） | 1,076 | 903/172 | seedance_2_0×750、soul_cinematic×144、nano_banana_2×70 | [docs](../sources/higgsfield/projects/4K_BLOCKBUSTER_BREAKDOWN/) |
| [AZTEC_REVOLT_ESCAPING_TENOCHTITLAN](../sources/higgsfield/prompts/AZTEC_REVOLT_ESCAPING_TENOCHTITLAN/) | — | 1,072 | 3/0 | default×594、videotape-alpha×421、video_extension×20 | — |
| [AZTEC_REVOLT](../sources/higgsfield/prompts/AZTEC_REVOLT/) | — | 1,069 | 617/452 | seedance_2_5×613、gpt_image_2×419、nano_banana_2×28 | [docs](../sources/higgsfield/projects/AZTEC_REVOLT/) |
| [I_CAN_CARRY_US_BOTH](../sources/higgsfield/prompts/I_CAN_CARRY_US_BOTH/) | — | 1,005 | 0/0 | default×255、video_edit×26、sora-2×1 | — |
| [TYANPA](../sources/higgsfield/prompts/TYANPA/) | — | 961 | 354/607 | seedream_v5_pro×528、cinematic_studio_video_4_0×215、seedance_2_5×125 | [docs](../sources/higgsfield/projects/TYANPA/) |
| [SOULLESS](../sources/higgsfield/prompts/SOULLESS/) | — | 960 | 419/541 | seedance_2_5×409、seedream_v5_pro×405、gpt_image_2×105 | [docs](../sources/higgsfield/projects/SOULLESS/) |
| [FOUND_ME](../sources/higgsfield/prompts/FOUND_ME/) | — | 946 | 0/0 | default×221、videotape-alpha×28、pro×2 | — |
| [A_LIFE](../sources/higgsfield/prompts/A_LIFE/) | — | 893 | 3/0 | default×528、videotape-alpha×215、sunburst×21 | — |
| [THE_COAT](../sources/higgsfield/prompts/THE_COAT/) | — | 842 | 297/545 | seedance_2_5×297、seedream_v5_pro×288、nano_banana_2×235 | [docs](../sources/higgsfield/projects/THE_COAT/) |
| [THE_PROMPTER](../sources/higgsfield/prompts/THE_PROMPTER/) | — | 799 | 401/398 | seedance_2_5×371、nano_banana_2×322、gpt_image_2×33 | [docs](../sources/higgsfield/projects/THE_PROMPTER/) |
| [THE_TRIGGER](../sources/higgsfield/prompts/THE_TRIGGER/) | 双时间线写实，调度图三安全规则+ACTING TASK | 773 | 568/174 | seedance_2_5×461、seedream_v5_pro×144、soul_cinematic×76 | [docs](../sources/higgsfield/projects/THE_TRIGGER/) |
| [PROPHECY_IN_2047](../sources/higgsfield/prompts/PROPHECY_IN_2047/) | — | 762 | 314/447 | seedance_2_5×247、gpt_image_2×198、seedream_v5_pro×148 | [docs](../sources/higgsfield/projects/PROPHECY_IN_2047/) |
| [IF_YOU_STOP_LOVING_ME](../sources/higgsfield/prompts/IF_YOU_STOP_LOVING_ME/) | 混合媒介（Kran 材质宪法：两世界永不光学交互） | 749 | 0/0 | 未标注 | [docs](../sources/higgsfield/projects/IF_YOU_STOP_LOVING_ME/) |
| [BORROWED_WOUNDS](../sources/higgsfield/prompts/BORROWED_WOUNDS/) | — | 736 | 221/515 | nano_banana_2×471、seedance_2_5×178、gpt_image_2×41 | [docs](../sources/higgsfield/projects/BORROWED_WOUNDS/) |
| [MARCEL_S_HEART](../sources/higgsfield/prompts/MARCEL_S_HEART/) | — | 731 | 4/0 | default×647、seedance_2_0×4 | — |
| [COUNT_OF_THREE](../sources/higgsfield/prompts/COUNT_OF_THREE/) | — | 730 | 323/407 | seedance_2_5×323、seedream_v5_pro×142、nano_banana_2×129 | [docs](../sources/higgsfield/projects/COUNT_OF_THREE/) |
| [DEATHS_FIRST_DAY](../sources/higgsfield/prompts/DEATHS_FIRST_DAY/) | — | 708 | 253/455 | seedream_v5_pro×314、seedance_2_5×234、nano_banana_2×120 | [docs](../sources/higgsfield/projects/DEATHS_FIRST_DAY/) |
| [PICK_ME](../sources/higgsfield/prompts/PICK_ME/) | — | 669 | 111/0 | videotape-alpha×388、default×130、seedance_2_0×111 | — |
| [VELMORA_THE_FORGOTTEN_REALMS](../sources/higgsfield/prompts/VELMORA_THE_FORGOTTEN_REALMS/) | — | 665 | 0/0 | videotape-alpha×209、default×202 | — |
| [SUNRISE_THE_PROLOGUE](../sources/higgsfield/prompts/SUNRISE_THE_PROLOGUE/) | — | 657 | 0/0 | default×178、video_extension×52、videotape-alpha×10 | — |
| [FIX](../sources/higgsfield/prompts/FIX/) | — | 640 | 0/0 | default×279、videotape-alpha×5、sunburst×1 | — |
| [RED_FLAG](../sources/higgsfield/prompts/RED_FLAG/) | 港式黑帮爱情，正向颜色分配体系 | 619 | 175/33 | seedance_2_5×135、seedance_2_0×35、seedream_v5_pro×29 | [docs](../sources/higgsfield/projects/RED_FLAG/) |
| [MADSEASON](../sources/higgsfield/prompts/MADSEASON/) | — | 615 | 17/0 | 3db34ab5-3439-4317-9e03-08dc30852e69×495、default×55、5fbabfac-d27b-4751-b550-fea356ed55ac×39 | [docs](../sources/higgsfield/projects/MADSEASON/) |
| [A_YEAR_LATER](../sources/higgsfield/prompts/A_YEAR_LATER/) | — | 597 | 1/0 | default×105、seedance_2_0×1 | — |
| [SITARA](../sources/higgsfield/prompts/SITARA/) | — | 597 | 0/0 | default×282、videotape-alpha×5、video_extension×2 | — |
| [ONE_SMALL_BITE](../sources/higgsfield/prompts/ONE_SMALL_BITE/) | — | 587 | 315/272 | seedance_2_5×312、nano_banana_2×145、seedream_v4_5×118 | [docs](../sources/higgsfield/projects/ONE_SMALL_BITE/) |
| [RORAIMA](../sources/higgsfield/prompts/RORAIMA/) | — | 586 | 295/291 | gpt_image_2×289、seedance_2_5×283、soul_cinematic×7 | [docs](../sources/higgsfield/projects/RORAIMA/) |
| [HALVER](../sources/higgsfield/prompts/HALVER/) | — | 579 | 284/294 | seedance_2_5×283、seedream_v5_pro×162、gpt_image_2×111 | [docs](../sources/higgsfield/projects/HALVER/) |
| [BUZKASHI](../sources/higgsfield/prompts/BUZKASHI/) | — | 534 | 150/384 | nano_banana_2×384、seedance_2_5×123、kling3_0×27 | [docs](../sources/higgsfield/projects/BUZKASHI/) |
| [VARMINTS](../sources/higgsfield/prompts/VARMINTS/) | — | 528 | 379/149 | cinematic_studio_video_4_0×194、seedance_2_5×169、seedream_v5_pro×74 | [docs](../sources/higgsfield/projects/VARMINTS/) |
| [DOMINIO](../sources/higgsfield/prompts/DOMINIO/) | — | 522 | 236/286 | seedance_2_5×204、seedream_v5_pro×145、gpt_image_2×108 | [docs](../sources/higgsfield/projects/DOMINIO/) |
| [31_AUGUST](../sources/higgsfield/prompts/31_AUGUST/) | — | 521 | 3/0 | default×132、videotape-alpha×9、seedance_2_0×3 | — |
| [STONE_GATE](../sources/higgsfield/prompts/STONE_GATE/) | — | 521 | 0/0 | default×222、videotape-alpha×101 | — |
| [THE_GOLDEN_TREE](../sources/higgsfield/prompts/THE_GOLDEN_TREE/) | — | 512 | 0/0 | default×22 | — |
| [VARMINTS_LAS_BODAS_DEL_RIO](../sources/higgsfield/prompts/VARMINTS_LAS_BODAS_DEL_RIO/) | — | 512 | 0/0 | default×286、video_extension×64、videotape-alpha×24 | — |
| [CONTROL](../sources/higgsfield/prompts/CONTROL/) | — | 510 | 405/105 | seedance_2_5×381、seedream_v5_pro×69、nano_banana_2×30 | [docs](../sources/higgsfield/projects/CONTROL/) |
| [THE_PATCH](../sources/higgsfield/prompts/THE_PATCH/) | — | 505 | 357/148 | seedance_2_5×354、seedream_v5_pro×111、nano_banana_2×18 | [docs](../sources/higgsfield/projects/THE_PATCH/) |
| [SIDE_B](../sources/higgsfield/prompts/SIDE_B/) | — | 502 | 0/0 | videotape-alpha×316、default×182 | — |
| [DONT_POISON_IVY](../sources/higgsfield/prompts/DONT_POISON_IVY/) | — | 490 | 343/147 | seedance_2_5×343、seedream_v5_pro×86、nano_banana_2×61 | [docs](../sources/higgsfield/projects/DONT_POISON_IVY/) |
| [ZEPHYR](../sources/higgsfield/prompts/ZEPHYR/) | K-pop 偶像打怪 MV 特辑，IMAX 质感 | 481 | 1/9 | nano_banana_2×8、soul_cinematic×1、gpt_image_2×1 | [docs](../sources/higgsfield/projects/ZEPHYR/) |
| [UNPROMPTED](../sources/higgsfield/prompts/UNPROMPTED/) | — | 475 | 162/313 | seedream_v5_pro×270、cinematic_studio_video_4_0×107、soul_cinematic×55 | [docs](../sources/higgsfield/projects/UNPROMPTED/) |
| [THE_BOY_WHO_RODE_THE_WIND](../sources/higgsfield/prompts/THE_BOY_WHO_RODE_THE_WIND/) | — | 471 | 88/0 | seedance_2_0×88、default×84、videotape-alpha×5 | — |
| [CLEAR_INTENTION](../sources/higgsfield/prompts/CLEAR_INTENTION/) | — | 468 | 311/156 | seedance_2_5×295、text2image_soul_v2×72、nano_banana_2×48 | [docs](../sources/higgsfield/projects/CLEAR_INTENTION/) |
| [DK_BENEATH_THE_EARTH](../sources/higgsfield/prompts/DK_BENEATH_THE_EARTH/) | — | 465 | 0/0 | default×321、videotape-alpha×140、video_extension×1 | — |
| [A_STRONG_CURRENT](../sources/higgsfield/prompts/A_STRONG_CURRENT/) | — | 463 | 73/0 | default×187、seedance_2_0×38、seedance_2_0_fast×35 | — |
| [ORDINARY_DAY](../sources/higgsfield/prompts/ORDINARY_DAY/) | — | 458 | 6/0 | default×269、videotape-alpha×137、video_extension×13 | — |
| [I_HATE_SCIENCE](../sources/higgsfield/prompts/I_HATE_SCIENCE/) | — | 455 | 292/161 | seedance_2_5×256、seedream_v5_pro×93、nano_banana_2×34 | [docs](../sources/higgsfield/projects/I_HATE_SCIENCE/) |
| [ONE_HUNDRED](../sources/higgsfield/prompts/ONE_HUNDRED/) | — | 453 | 0/0 | default×177、videotape-alpha×16、flare×5 | — |
| [YIN_YANG_AGENCY_THUNDER_RISING](../sources/higgsfield/prompts/YIN_YANG_AGENCY_THUNDER_RISING/) | — | 453 | 0/0 | default×57、videotape-alpha×19、minimax×1 | — |
| [TWO_DAYS](../sources/higgsfield/prompts/TWO_DAYS/) | — | 452 | 379/0 | seedance_2_0×379、videotape-alpha×5、video_extension×3 | — |
| [BIRTHDAYS](../sources/higgsfield/prompts/BIRTHDAYS/) | — | 451 | 0/0 | default×170、video_edit×2、pro×1 | — |
| [CHORNOS_THE_CHOSEN](../sources/higgsfield/prompts/CHORNOS_THE_CHOSEN/) | — | 442 | 5/0 | video_extension×201、videotape-alpha×115、default×64 | — |
| [FIVE_SECONDS](../sources/higgsfield/prompts/FIVE_SECONDS/) | — | 442 | 48/0 | videotape-alpha×205、default×120、seedance_2_0×48 | — |
| [MEMORY_WORLD](../sources/higgsfield/prompts/MEMORY_WORLD/) | — | 439 | 2/0 | default×191、sunburst×8、videotape-alpha×3 | — |
| [PRINCESS_GLOW_UP](../sources/higgsfield/prompts/PRINCESS_GLOW_UP/) | — | 438 | 344/94 | seedance_2_5×330、text2image_soul_v2×34、gpt_image_2×24 | [docs](../sources/higgsfield/projects/PRINCESS_GLOW_UP/) |
| [SUMMONED](../sources/higgsfield/prompts/SUMMONED/) | — | 438 | 1/0 | default×303、videotape-alpha×121、seedance_2_0×1 | — |
| [EYES_EARS](../sources/higgsfield/prompts/EYES_EARS/) | — | 433 | 172/0 | seedance_2_0×171、video_extension×50、video_edit×15 | — |
| [TENSORA](../sources/higgsfield/prompts/TENSORA/) | — | 431 | 5/0 | videotape-alpha×139、default×138、sunburst×12 | — |
| [BESA](../sources/higgsfield/prompts/BESA/) | — | 429 | 317/104 | seedance_2_5×305、gpt_image_2×39、nano_banana_2×15 | [docs](../sources/higgsfield/projects/BESA/) |
| [S_T_E_V_E](../sources/higgsfield/prompts/S_T_E_V_E/) | — | 425 | 0/0 | default×154 | — |
| [THE_OTHER_SIDE](../sources/higgsfield/prompts/THE_OTHER_SIDE/) | — | 423 | 0/0 | default×211 | — |
| [HERO](../sources/higgsfield/prompts/HERO/) | — | 422 | 0/0 | default×161、video_extension×44、videotape-alpha×29 | — |
| [TOMORROW_UNDER_REPAIR](../sources/higgsfield/prompts/TOMORROW_UNDER_REPAIR/) | — | 421 | 0/0 | default×253、videotape-alpha×31 | — |
| [THE_FAIREST_ONE](../sources/higgsfield/prompts/THE_FAIREST_ONE/) | — | 420 | 0/0 | default×89、videotape-alpha×3 | — |
| [METEM_PSYCHOSIS](../sources/higgsfield/prompts/METEM_PSYCHOSIS/) | — | 413 | 55/0 | seedance_2_0×55、default×18、video_extension×14 | — |
| [TEGAKI](../sources/higgsfield/prompts/TEGAKI/) | — | 410 | 0/0 | default×206、videotape-alpha×162、video_edit×3 | — |
| [THE_UNMAPPED](../sources/higgsfield/prompts/THE_UNMAPPED/) | — | 409 | 1/0 | default×111、seedance_2_0_fast×1 | — |
| [ISA](../sources/higgsfield/prompts/ISA/) | — | 406 | 0/0 | default×125、video_extension×34、videotape-alpha×19 | — |
| [RUBY](../sources/higgsfield/prompts/RUBY/) | — | 404 | 0/0 | default×256、pro×1 | — |
| [THE_DIVERGION](../sources/higgsfield/prompts/THE_DIVERGION/) | — | 402 | 14/0 | videotape-alpha×110、default×82、video_extension×41 | — |
| [NATIVE](../sources/higgsfield/prompts/NATIVE/) | — | 400 | 0/0 | default×106、videotape-alpha×21 | — |
| [UNDER_THE_SOFA](../sources/higgsfield/prompts/UNDER_THE_SOFA/) | — | 399 | 9/0 | seedance_2_0_fast×9 | — |
| [ON_THIN_ICE](../sources/higgsfield/prompts/ON_THIN_ICE/) | — | 396 | 3/0 | default×270、videotape-alpha×58、video_edit×22 | — |
| [UNSENT](../sources/higgsfield/prompts/UNSENT/) | — | 394 | 0/0 | default×90、video_extension×12、videotape-alpha×4 | — |
| [100_MILLION_RAT](../sources/higgsfield/prompts/100_MILLION_RAT/) | — | 392 | 0/0 | default×193、videotape-alpha×166、sunburst×10 | — |
| [OUT_OF_CREDITS](../sources/higgsfield/prompts/OUT_OF_CREDITS/) | — | 389 | 0/0 | default×60、video_extension×53、videotape-alpha×27 | — |
| [CALEUCHE](../sources/higgsfield/prompts/CALEUCHE/) | — | 386 | 0/0 | default×296、videotape-alpha×79 | — |
| [THE_FORGOTTEN_RINPOCHE](../sources/higgsfield/prompts/THE_FORGOTTEN_RINPOCHE/) | — | 386 | 6/0 | default×145、videotape-alpha×51、sunburst×12 | — |
| [EMBERDANT_SEASON_1_PART_1](../sources/higgsfield/prompts/EMBERDANT_SEASON_1_PART_1/) | — | 385 | 10/0 | videotape-alpha×233、default×137、seedance_2_0×10 | — |
| [UNFASTEN](../sources/higgsfield/prompts/UNFASTEN/) | — | 385 | 1/0 | default×131、seedance_2_0×1、video_edit×1 | — |
| [OPPORTUNITY](../sources/higgsfield/prompts/OPPORTUNITY/) | — | 382 | 0/0 | videotape-alpha×14、default×3 | — |
| [THE_TORTOISE_AND_THE_HARE](../sources/higgsfield/prompts/THE_TORTOISE_AND_THE_HARE/) | — | 382 | 226/141 | seedance_2_5×219、seedream_v5_pro×82、gpt_image_2×58 | [docs](../sources/higgsfield/projects/THE_TORTOISE_AND_THE_HARE/) |
| [YINGNING](../sources/higgsfield/prompts/YINGNING/) | — | 382 | 0/0 | default×203、videotape-alpha×71、video_extension×12 | — |
| [DON_T_SLEEP](../sources/higgsfield/prompts/DON_T_SLEEP/) | — | 381 | 124/0 | videotape-alpha×213、seedance_2_0×116、seedance_2_0_fast×8 | — |
| [ORDER_OF_ASH](../sources/higgsfield/prompts/ORDER_OF_ASH/) | — | 381 | 5/0 | default×334、seedance_2_0×4、seedance_2_0_fast×1 | — |
| [SKIN_TRADE](../sources/higgsfield/prompts/SKIN_TRADE/) | — | 381 | 4/0 | default×192、videotape-alpha×102、video_extension×48 | — |
| [HIGH_SCHOOL_TERROR](../sources/higgsfield/prompts/HIGH_SCHOOL_TERROR/) | — | 380 | 0/0 | default×146、video_extension×55、videotape-alpha×53 | — |
| [SHARDS_OF_WHEN](../sources/higgsfield/prompts/SHARDS_OF_WHEN/) | — | 380 | 50/0 | default×325、seedance_2_0×50、video_edit×5 | — |
| [WORLD_OF_SCARS](../sources/higgsfield/prompts/WORLD_OF_SCARS/) | — | 380 | 26/0 | default×266、video_extension×38、seedance_2_0×26 | — |
| [STREET_FOOD](../sources/higgsfield/prompts/STREET_FOOD/) | — | 379 | 54/0 | seedance_2_0×53、default×46、seedance_2_0_fast×1 | — |
| [RAMIZA](../sources/higgsfield/prompts/RAMIZA/) | — | 378 | 1/0 | default×165、videotape-alpha×8、video_extension×1 | — |
| [BIOSCOPE](../sources/higgsfield/prompts/BIOSCOPE/) | — | 376 | 8/0 | default×141、seedance_2_0×8、videotape-alpha×2 | — |
| [REVOLUTION](../sources/higgsfield/prompts/REVOLUTION/) | — | 375 | 0/0 | default×295、sunburst×13、video_edit×1 | — |
| [THE_KITE](../sources/higgsfield/prompts/THE_KITE/) | — | 375 | 15/0 | default×106、seedance_2_0×15、videotape-alpha×9 | — |
| [THE_ZERO_LINE](../sources/higgsfield/prompts/THE_ZERO_LINE/) | — | 375 | 0/0 | default×55 | — |
| [H2O](../sources/higgsfield/prompts/H2O/) | — | 372 | 0/0 | default×93、videotape-alpha×8、video_edit×1 | — |
| [NO_BAD_DREAMS](../sources/higgsfield/prompts/NO_BAD_DREAMS/) | — | 371 | 334/0 | seedance_2_0×334、videotape-alpha×29、default×2 | — |
| [FUKUSHIMA](../sources/higgsfield/prompts/FUKUSHIMA/) | — | 367 | 88/278 | seedream_v5_pro×191、seedance_2_5×88、gpt_image_2×56 | [docs](../sources/higgsfield/projects/FUKUSHIMA/) |
| [WARDEN](../sources/higgsfield/prompts/WARDEN/) | — | 367 | 98/0 | seedance_2_0×98、default×97、videotape-alpha×87 | — |
| [INVENTORY](../sources/higgsfield/prompts/INVENTORY/) | — | 365 | 166/0 | seedance_2_0×166、videotape-alpha×4 | — |
| [PAUSE](../sources/higgsfield/prompts/PAUSE/) | — | 360 | 3/0 | default×98、videotape-alpha×84、seedance_2_0×3 | — |
| [WITHIN](../sources/higgsfield/prompts/WITHIN/) | — | 360 | 0/0 | default×152、videotape-alpha×12 | — |
| [HIXXA_THE_WORLD_SHE_THREW_AWAY_FANTASY_SHORT_FILM](../sources/higgsfield/prompts/HIXXA_THE_WORLD_SHE_THREW_AWAY_FANTASY_SHORT_FILM/) | — | 359 | 1/0 | video_extension×137、videotape-alpha×115、default×55 | — |
| [LOW_ORBIT](../sources/higgsfield/prompts/LOW_ORBIT/) | — | 358 | 0/0 | default×146、videotape-alpha×21、sunburst×2 | — |
| [NOKU](../sources/higgsfield/prompts/NOKU/) | — | 357 | 3/0 | default×182、videotape-alpha×9、seedance_2_0×3 | — |
| [ALL_THE_GOOD_ONES](../sources/higgsfield/prompts/ALL_THE_GOOD_ONES/) | — | 356 | 0/0 | videotape-alpha×146、video_extension×81、sunburst×48 | — |
| [EREN_THE_LAST_SEED](../sources/higgsfield/prompts/EREN_THE_LAST_SEED/) | — | 356 | 6/0 | videotape-alpha×86、default×73、seedance_2_0×6 | — |
| [KADHAA_2155](../sources/higgsfield/prompts/KADHAA_2155/) | — | 352 | 0/0 | default×127、video_extension×95、video_edit×1 | — |
| [SHADE_FADE_THE_BLACK_SANDS](../sources/higgsfield/prompts/SHADE_FADE_THE_BLACK_SANDS/) | — | 352 | 0/0 | videotape-alpha×23、default×6、elevenlabs×2 | — |
| [THE_LAST_PRINCE](../sources/higgsfield/prompts/THE_LAST_PRINCE/) | — | 352 | 0/0 | default×42、video_extension×5、videotape-alpha×1 | — |
| [LONG_SIGH](../sources/higgsfield/prompts/LONG_SIGH/) | — | 350 | 2/0 | default×219、videotape-alpha×16、video_edit×3 | — |
| [UNIT_SEVEN](../sources/higgsfield/prompts/UNIT_SEVEN/) | — | 350 | 8/0 | videotape-alpha×263、default×76、seedance_2_0×8 | — |
| [GINGER](../sources/higgsfield/prompts/GINGER/) | — | 348 | 22/0 | default×211、videotape-alpha×42、seedance_2_0_fast×19 | — |
| [HARVEST_DAY](../sources/higgsfield/prompts/HARVEST_DAY/) | — | 347 | 1/0 | default×113、videotape-alpha×67、video_extension×17 | — |
| [OOPS_FIRST_CONTACT](../sources/higgsfield/prompts/OOPS_FIRST_CONTACT/) | — | 346 | 8/0 | default×138、seedance_2_0×8、videotape-alpha×1 | — |
| [MIDNIGHT_BLOODLINE](../sources/higgsfield/prompts/MIDNIGHT_BLOODLINE/) | — | 345 | 0/0 | default×91、video_extension×66、pro×9 | — |
| [SEVEN_MINUTES_LEFT](../sources/higgsfield/prompts/SEVEN_MINUTES_LEFT/) | — | 344 | 0/0 | default×158、sunburst×15、videotape-alpha×3 | — |
| [THE_ROOK](../sources/higgsfield/prompts/THE_ROOK/) | — | 344 | 2/0 | default×25、minimax-2.3×3、kling-v2-5-turbo×2 | — |
| [CHARMED](../sources/higgsfield/prompts/CHARMED/) | — | 343 | 171/171 | seedance_2_5×168、seedream_v5_pro×109、nano_banana_flash×61 | [docs](../sources/higgsfield/projects/CHARMED/) |
| [STUFFY_SYNTH](../sources/higgsfield/prompts/STUFFY_SYNTH/) | — | 342 | 0/0 | default×139、sunburst×5、video_edit×5 | — |
| [333](../sources/higgsfield/prompts/333/) | — | 339 | 0/0 | video_extension×170、default×48、videotape-alpha×4 | — |
| [GOTCHA_A_POST_MYSTERY_MURDER](../sources/higgsfield/prompts/GOTCHA_A_POST_MYSTERY_MURDER/) | — | 339 | 71/0 | seedance_2_0×42、seedance_2_0_fast×29、video_extension×11 | — |
| [NEW_KAIJU_CITY](../sources/higgsfield/prompts/NEW_KAIJU_CITY/) | — | 337 | 0/0 | default×166、videotape-alpha×146、video_extension×6 | — |
| [OVERBOARD](../sources/higgsfield/prompts/OVERBOARD/) | — | 336 | 0/0 | default×66、videotape-alpha×25、video_extension×2 | — |
| [RISE_OF_AN_EMPIRE_BY_HOUSE_OF_DI_LORENZO](../sources/higgsfield/prompts/RISE_OF_AN_EMPIRE_BY_HOUSE_OF_DI_LORENZO/) | — | 331 | 21/0 | default×158、video_extension×37、videotape-alpha×27 | — |
| [BEFORE_TIME](../sources/higgsfield/prompts/BEFORE_TIME/) | — | 330 | 2/0 | videotape-alpha×125、seedance_2_0_fast×2 | — |
| [DUSTBIN_INSPIRED_BY_REAL_EVENTS](../sources/higgsfield/prompts/DUSTBIN_INSPIRED_BY_REAL_EVENTS/) | — | 327 | 166/0 | seedance_2_0_fast×164、default×20、seedance_2_0×2 | — |
| [SEVENTY_TONGUES](../sources/higgsfield/prompts/SEVENTY_TONGUES/) | — | 325 | 0/0 | default×150、videotape-alpha×58、video_extension×40 | — |
| [THE_FOREST](../sources/higgsfield/prompts/THE_FOREST/) | — | 325 | 0/0 | default×246、videotape-alpha×2 | — |
| [OUR_DEAD_GUEST](../sources/higgsfield/prompts/OUR_DEAD_GUEST/) | — | 324 | 0/0 | default×164、video_extension×4、video_edit×3 | — |
| [THE_LAST_OATH](../sources/higgsfield/prompts/THE_LAST_OATH/) | — | 324 | 1/0 | default×42、videotape-alpha×34、sunburst×4 | — |
| [SEVENTY_THREE](../sources/higgsfield/prompts/SEVENTY_THREE/) | — | 323 | 1/0 | default×243、videotape-alpha×25、seedance_2_0×1 | — |
| [THE_FAMILY_CHAOS_CLUB](../sources/higgsfield/prompts/THE_FAMILY_CHAOS_CLUB/) | — | 322 | 0/0 | default×248 | — |
| [THE_SEA_CALLS](../sources/higgsfield/prompts/THE_SEA_CALLS/) | — | 322 | 6/0 | default×180、videotape-alpha×41、seedance_2_0×3 | — |
| [THE_SECOND_HAND](../sources/higgsfield/prompts/THE_SECOND_HAND/) | — | 322 | 0/0 | default×169、videotape-alpha×53、video_extension×3 | — |
| [REROUTING](../sources/higgsfield/prompts/REROUTING/) | — | 321 | 6/0 | default×213、videotape-alpha×8、video_extension×4 | — |
| [EAT_PREY_LUV](../sources/higgsfield/prompts/EAT_PREY_LUV/) | — | 320 | 0/0 | 未标注 | — |
| [SAVE_CHANGES](../sources/higgsfield/prompts/SAVE_CHANGES/) | — | 318 | 0/0 | videotape-alpha×224、default×52、sunburst×11 | — |
| [BRATIX](../sources/higgsfield/prompts/BRATIX/) | — | 317 | 0/0 | default×175、sunburst×56、videotape-alpha×14 | — |
| [HUNGER](../sources/higgsfield/prompts/HUNGER/) | — | 317 | 0/0 | default×175、video_edit×3 | — |
| [UNDERHAND](../sources/higgsfield/prompts/UNDERHAND/) | — | 316 | 0/0 | default×88、video_extension×28、video_edit×4 | — |
| [WOKOU_HUNTERS](../sources/higgsfield/prompts/WOKOU_HUNTERS/) | — | 316 | 0/0 | 未标注 | — |
| [THE_SEVENTH_LOOP](../sources/higgsfield/prompts/THE_SEVENTH_LOOP/) | — | 314 | 0/0 | default×100、video_extension×34 | — |
| [ARKYN](../sources/higgsfield/prompts/ARKYN/) | — | 312 | 0/0 | default×226、videotape-alpha×45、video_edit×4 | — |
| [MINA_ONE_MORE_LIFE](../sources/higgsfield/prompts/MINA_ONE_MORE_LIFE/) | — | 311 | 73/0 | default×116、seedance_2_0×73、videotape-alpha×22 | — |
| [LOWER_ROAD](../sources/higgsfield/prompts/LOWER_ROAD/) | — | 310 | 0/0 | sunburst×54、videotape-alpha×25、default×16 | — |
| [STAY_HOME_TOMORROW](../sources/higgsfield/prompts/STAY_HOME_TOMORROW/) | — | 310 | 0/0 | default×130、video_extension×49、video_edit×6 | — |
| [FRACTURED](../sources/higgsfield/prompts/FRACTURED/) | — | 309 | 0/0 | default×62、video_extension×9、sunburst×2 | — |
| [INSIDE_JOKE](../sources/higgsfield/prompts/INSIDE_JOKE/) | — | 309 | 0/0 | default×132、videotape-alpha×127 | — |
| [BLACKWOOD_MANOR](../sources/higgsfield/prompts/BLACKWOOD_MANOR/) | — | 308 | 27/0 | default×102、videotape-alpha×28、seedance_2_0×27 | — |
| [MARIA_MARIA](../sources/higgsfield/prompts/MARIA_MARIA/) | — | 308 | 0/0 | default×155、sunburst×18、videotape-alpha×6 | — |
| [THE_HUNGER](../sources/higgsfield/prompts/THE_HUNGER/) | — | 308 | 29/0 | default×76、seedance_2_0×29、videotape-alpha×3 | — |
| [THE_LAST_ART](../sources/higgsfield/prompts/THE_LAST_ART/) | — | 307 | 8/0 | videotape-alpha×110、default×31、seedance_2_0×8 | — |
| [DAGON](../sources/higgsfield/prompts/DAGON/) | — | 306 | 161/145 | gpt_image_2×145、kling3_0×107、seedance_2_5×54 | [docs](../sources/higgsfield/projects/DAGON/) |
| [QUARTER](../sources/higgsfield/prompts/QUARTER/) | — | 306 | 5/0 | video_extension×93、videotape-alpha×78、default×66 | — |
| [WINGS_ON_FIRE](../sources/higgsfield/prompts/WINGS_ON_FIRE/) | — | 306 | 3/0 | videotape-alpha×83、default×43、pro×19 | — |
| [ONCE_A_KITTEN](../sources/higgsfield/prompts/ONCE_A_KITTEN/) | — | 305 | 1/0 | default×97、sunburst×50、elevenlabs×19 | — |
| [MR_OTTER](../sources/higgsfield/prompts/MR_OTTER/) | — | 304 | 210/93 | seedance_2_5×208、gpt_image_2×93、hf_mult_motion_control×2 | [docs](../sources/higgsfield/projects/MR_OTTER/) |
| [ONE_DAY_WITH_MR_OTTER_HIGGSFIELD_FILM_FESTIVAL](../sources/higgsfield/prompts/ONE_DAY_WITH_MR_OTTER_HIGGSFIELD_FILM_FESTIVAL/) | — | 304 | 0/0 | default×178、videotape-alpha×93、video_edit×29 | — |
| [THE_GRAVE](../sources/higgsfield/prompts/THE_GRAVE/) | — | 304 | 10/0 | default×205、videotape-alpha×40、seedance_2_0×10 | — |
| [DEATH_CAME_TO_DINNER](../sources/higgsfield/prompts/DEATH_CAME_TO_DINNER/) | — | 303 | 7/0 | default×149、videotape-alpha×99、sunburst×16 | — |
| [IN_S](../sources/higgsfield/prompts/IN_S/) | — | 302 | 0/0 | default×178 | — |
| [RELIVE](../sources/higgsfield/prompts/RELIVE/) | — | 302 | 2/0 | default×143、videotape-alpha×22、seedance_2_0×2 | — |
| [THE_CHOSEN](../sources/higgsfield/prompts/THE_CHOSEN/) | — | 301 | 0/0 | default×42 | — |
| [A_LONG_LUNCH](../sources/higgsfield/prompts/A_LONG_LUNCH/) | — | 299 | 0/0 | default×195、videotape-alpha×50、sunburst×42 | — |
| [THE_APPLE](../sources/higgsfield/prompts/THE_APPLE/) | — | 299 | 0/0 | default×67、video_extension×52、videotape-alpha×7 | — |
| [HORSELESS](../sources/higgsfield/prompts/HORSELESS/) | — | 298 | 1/0 | default×91、videotape-alpha×74、video_edit×7 | — |
| [RAKSASA](../sources/higgsfield/prompts/RAKSASA/) | — | 298 | 0/0 | default×86、videotape-alpha×2 | — |
| [VESPER](../sources/higgsfield/prompts/VESPER/) | — | 298 | 0/0 | default×176、videotape-alpha×8 | — |
| [SAMPO](../sources/higgsfield/prompts/SAMPO/) | — | 297 | 2/0 | videotape-alpha×142、default×96、sunburst×22 | — |
| [ECLIPSE](../sources/higgsfield/prompts/ECLIPSE/) | — | 294 | 1/0 | default×178、videotape-alpha×35、sunburst×1 | — |
| [NAMED_FOR_HIM](../sources/higgsfield/prompts/NAMED_FOR_HIM/) | — | 294 | 0/0 | default×134、video_extension×2、Redefine×1 | — |
| [YOU_NEVER_KNEW_ME](../sources/higgsfield/prompts/YOU_NEVER_KNEW_ME/) | — | 294 | 1/0 | default×100、videotape-alpha×13、seedance_2_0_fast×1 | — |
| [THE_CONFLUENCE_OF_THE_BIRDS](../sources/higgsfield/prompts/THE_CONFLUENCE_OF_THE_BIRDS/) | — | 293 | 70/0 | seedance_2_0×70、videotape-alpha×38、default×32 | — |
| [WRECKOON](../sources/higgsfield/prompts/WRECKOON/) | — | 293 | 0/0 | default×72、videotape-alpha×4 | — |
| [AA_MEETING](../sources/higgsfield/prompts/AA_MEETING/) | — | 292 | 2/0 | default×168、video_extension×10、seedance_2_0×2 | — |
| [BLESTYASHCHEE_NEVEZHESTVO](../sources/higgsfield/prompts/BLESTYASHCHEE_NEVEZHESTVO/) | — | 292 | 0/0 | 未标注 | — |
| [PRISONER](../sources/higgsfield/prompts/PRISONER/) | — | 291 | 0/0 | videotape-alpha×16 | — |
| [TAKE_MY_HANDS](../sources/higgsfield/prompts/TAKE_MY_HANDS/) | — | 291 | 2/0 | default×160、videotape-alpha×24、seedance_2_0×2 | — |
| [THE_HOST](../sources/higgsfield/prompts/THE_HOST/) | — | 291 | 0/0 | default×138、videotape-alpha×3 | — |
| [THE_LAST_PALADIN_ACT_I](../sources/higgsfield/prompts/THE_LAST_PALADIN_ACT_I/) | — | 290 | 24/0 | default×120、video_extension×33、seedance_2_0×24 | — |
| [BEYOND](../sources/higgsfield/prompts/BEYOND/) | — | 289 | 0/0 | default×118、videotape-alpha×61 | — |
| [SILENCE_LAVENDER](../sources/higgsfield/prompts/SILENCE_LAVENDER/) | — | 289 | 8/0 | default×152、seedance_2_0×8、videotape-alpha×3 | — |
| [BALLAST](../sources/higgsfield/prompts/BALLAST/) | — | 288 | 151/137 | seedance_2_5×129、nano_banana_2×64、nano_banana_flash×50 | [docs](../sources/higgsfield/projects/BALLAST/) |
| [FLICK](../sources/higgsfield/prompts/FLICK/) | — | 288 | 1/0 | default×171、videotape-alpha×25、video_extension×1 | — |
| [THE_LAST_CUT](../sources/higgsfield/prompts/THE_LAST_CUT/) | — | 288 | 14/0 | default×165、videotape-alpha×20、seedance_2_0×12 | — |
| [BABEL](../sources/higgsfield/prompts/BABEL/) | — | 287 | 0/0 | default×135、video_edit×3、videotape-alpha×1 | — |
| [MODEL_CITIZEN](../sources/higgsfield/prompts/MODEL_CITIZEN/) | — | 287 | 1/0 | default×67、video_extension×31、seedance_2_0×1 | — |
| [RECURSION](../sources/higgsfield/prompts/RECURSION/) | — | 287 | 0/0 | default×96、videotape-alpha×72、sunburst×8 | — |
| [CONCRETE_MEMORIES](../sources/higgsfield/prompts/CONCRETE_MEMORIES/) | — | 286 | 0/0 | default×161、videotape-alpha×89、video_extension×4 | — |
| [THE_FILTER](../sources/higgsfield/prompts/THE_FILTER/) | — | 286 | 0/0 | default×208、videotape-alpha×32、video_edit×2 | — |
| [JANJI_NUSA_A_PROMISE_TO_THE_HOMELAND](../sources/higgsfield/prompts/JANJI_NUSA_A_PROMISE_TO_THE_HOMELAND/) | — | 285 | 0/0 | default×91、videotape-alpha×2、elevenlabs×1 | — |
| [SIDE_BY_SIDE](../sources/higgsfield/prompts/SIDE_BY_SIDE/) | — | 285 | 0/0 | default×109 | — |
| [MEMORY_HEIST](../sources/higgsfield/prompts/MEMORY_HEIST/) | — | 284 | 0/0 | default×124、videotape-alpha×2 | — |
| [THE_FUSE](../sources/higgsfield/prompts/THE_FUSE/) | — | 283 | 0/0 | default×139 | — |
| [HONOR](../sources/higgsfield/prompts/HONOR/) | — | 282 | 0/0 | default×147、sunburst×36、videotape-alpha×14 | — |
| [PLAY_ANYWAY](../sources/higgsfield/prompts/PLAY_ANYWAY/) | — | 282 | 0/0 | default×120、videotape-alpha×32 | — |
| [THE_COLLECTOR](../sources/higgsfield/prompts/THE_COLLECTOR/) | — | 282 | 0/0 | default×209、videotape-alpha×62 | — |
| [ALIENS_DINOSAURS](../sources/higgsfield/prompts/ALIENS_DINOSAURS/) | — | 280 | 0/0 | default×110、video_extension×11、video_edit×4 | — |
| [THE_DEAD_WE_CARRY](../sources/higgsfield/prompts/THE_DEAD_WE_CARRY/) | — | 279 | 0/0 | default×64、videotape-alpha×1、video_extension×1 | — |
| [110_ONLYHOPE](../sources/higgsfield/prompts/110_ONLYHOPE/) | — | 277 | 36/0 | default×148、videotape-alpha×49、seedance_2_0×36 | — |
| [FLINCH](../sources/higgsfield/prompts/FLINCH/) | — | 277 | 0/0 | default×56、video_extension×46、sunburst×5 | — |
| [ONE_DAY_ON_EARTH](../sources/higgsfield/prompts/ONE_DAY_ON_EARTH/) | — | 277 | 19/0 | default×188、video_edit×58、seedance_2_0×19 | — |
| [THE_LOCKED_ROOM](../sources/higgsfield/prompts/THE_LOCKED_ROOM/) | — | 275 | 0/0 | video_extension×108、default×94、videotape-alpha×67 | — |
| [OVERCLOCK](../sources/higgsfield/prompts/OVERCLOCK/) | — | 274 | 0/0 | default×78、videotape-alpha×4、pro×4 | — |
| [THE_ARCHIVIST](../sources/higgsfield/prompts/THE_ARCHIVIST/) | — | 274 | 0/0 | default×150、video_extension×21、videotape-alpha×2 | — |
| [DEAD_ALIVE](../sources/higgsfield/prompts/DEAD_ALIVE/) | — | 272 | 0/0 | default×169、video_edit×6、pro×5 | — |
| [BEAST_RACE](../sources/higgsfield/prompts/BEAST_RACE/) | — | 271 | 0/0 | default×193、videotape-alpha×27 | — |
| [JOURNEY](../sources/higgsfield/prompts/JOURNEY/) | — | 271 | 0/0 | default×114、video_extension×19、video_edit×6 | — |
| [HER_EYES](../sources/higgsfield/prompts/HER_EYES/) | — | 270 | 0/0 | default×119、videotape-alpha×39 | — |
| [ONE_DAY_AT_A_TIME](../sources/higgsfield/prompts/ONE_DAY_AT_A_TIME/) | — | 270 | 0/0 | default×209、videotape-alpha×31、video_extension×29 | — |
| [DEMENTIA](../sources/higgsfield/prompts/DEMENTIA/) | — | 268 | 90/0 | seedance_2_0×90、default×81、videotape-alpha×78 | — |
| [DON_CHENTE_S_ABDUCTION](../sources/higgsfield/prompts/DON_CHENTE_S_ABDUCTION/) | — | 267 | 0/0 | default×121、videotape-alpha×24、sunburst×10 | — |
| [NO_ONE](../sources/higgsfield/prompts/NO_ONE/) | — | 267 | 0/0 | default×168、videotape-alpha×6 | — |
| [NO_ROOM_FOR_TWO](../sources/higgsfield/prompts/NO_ROOM_FOR_TWO/) | — | 267 | 24/0 | default×124、seedance_2_0×24 | — |
| [RELIC](../sources/higgsfield/prompts/RELIC/) | — | 267 | 1/0 | default×178、videotape-alpha×11、seedance_2_0×1 | — |
| [1916_WORLD_WAR](../sources/higgsfield/prompts/1916_WORLD_WAR/) | — | 266 | 0/0 | default×76、videotape-alpha×74、sunburst×1 | — |
| [SEA_OF_FOG](../sources/higgsfield/prompts/SEA_OF_FOG/) | — | 266 | 1/0 | default×147、videotape-alpha×28、video_edit×7 | — |
| [SENTENCE](../sources/higgsfield/prompts/SENTENCE/) | — | 266 | 0/0 | default×113、videotape-alpha×63、video_edit×4 | — |
| [PHOTO_IN_PARIS](../sources/higgsfield/prompts/PHOTO_IN_PARIS/) | — | 265 | 8/0 | default×153、sunburst×10、video_edit×9 | — |
| [PROTOCOL_XCI](../sources/higgsfield/prompts/PROTOCOL_XCI/) | — | 264 | 0/0 | default×67 | — |
| [THE_FINAL_INTERVIEW](../sources/higgsfield/prompts/THE_FINAL_INTERVIEW/) | — | 264 | 2/0 | default×127、sunburst×22、videotape-alpha×18 | — |
| [AZUL_COBALTO](../sources/higgsfield/prompts/AZUL_COBALTO/) | — | 262 | 210/52 | seedance_2_5×206、seedream_v5_pro×28、text2image_soul_v2×17 | [docs](../sources/higgsfield/projects/AZUL_COBALTO/) |
| [THE_LAST_FLOWER](../sources/higgsfield/prompts/THE_LAST_FLOWER/) | — | 262 | 4/0 | videotape-alpha×207、default×42、seedance_2_0×4 | — |
| [BLACK_VEIL_SHORT_HORROR_FILM](../sources/higgsfield/prompts/BLACK_VEIL_SHORT_HORROR_FILM/) | — | 261 | 1/0 | default×82、seedance_2_0_fast×1 | — |
| [HUMAN_ERROR](../sources/higgsfield/prompts/HUMAN_ERROR/) | — | 261 | 25/0 | seedance_2_0×25 | — |
| [SNAP](../sources/higgsfield/prompts/SNAP/) | — | 261 | 13/0 | video_extension×51、default×16、seedance_2_0×13 | — |
| [THE_CLIMB](../sources/higgsfield/prompts/THE_CLIMB/) | — | 261 | 0/0 | default×28、videotape-alpha×12、video_extension×6 | — |
| [WHAT_DO_YOU_NEED_ME_FOR](../sources/higgsfield/prompts/WHAT_DO_YOU_NEED_ME_FOR/) | — | 261 | 3/0 | default×88、videotape-alpha×82、video_extension×12 | — |
| [TAGE_7](../sources/higgsfield/prompts/TAGE_7/) | — | 260 | 0/0 | default×109、videotape-alpha×11、sunburst×1 | — |
| [DEAD_WATER](../sources/higgsfield/prompts/DEAD_WATER/) | — | 259 | 137/0 | seedance_2_0×137、videotape-alpha×82、default×6 | — |
| [GRIMWATCH](../sources/higgsfield/prompts/GRIMWATCH/) | — | 259 | 73/184 | nano_banana_2×92、nano_banana_flash×59、seedance_2_unlimited×52 | [docs](../sources/higgsfield/projects/GRIMWATCH/) |
| [IT_SHOULD_HAVE_BEEN_ME](../sources/higgsfield/prompts/IT_SHOULD_HAVE_BEEN_ME/) | — | 259 | 0/0 | default×142、videotape-alpha×45、video_extension×4 | — |
| [KEEPSAKE](../sources/higgsfield/prompts/KEEPSAKE/) | — | 258 | 0/0 | default×195 | — |
| [NAHUAL_A_STORY_FROM_LA_HUASTECA](../sources/higgsfield/prompts/NAHUAL_A_STORY_FROM_LA_HUASTECA/) | — | 258 | 0/0 | default×66、videotape-alpha×19 | — |
| [ICONIC_BETA](../sources/higgsfield/prompts/ICONIC_BETA/) | — | 257 | 5/0 | videotape-alpha×75、default×51、seedance_2_0×5 | — |
| [SPANNERGIRL](../sources/higgsfield/prompts/SPANNERGIRL/) | — | 257 | 1/0 | default×188、sunburst×6、video_edit×1 | — |
| [THE_PUNCH_BOWL](../sources/higgsfield/prompts/THE_PUNCH_BOWL/) | — | 257 | 1/0 | default×116、videotape-alpha×25、sunburst×13 | — |
| [GLITCH_DAY](../sources/higgsfield/prompts/GLITCH_DAY/) | — | 256 | 0/0 | default×119、video_extension×4 | — |
| [AND_WHERE_ARE_WE_GOING](../sources/higgsfield/prompts/AND_WHERE_ARE_WE_GOING/) | — | 255 | 199/56 | seedance_2_5×199、gpt_image_2×56 | [docs](../sources/higgsfield/projects/AND_WHERE_ARE_WE_GOING/) |
| [AND_STILL_LIFE](../sources/higgsfield/prompts/AND_STILL_LIFE/) | — | 254 | 0/0 | default×180、videotape-alpha×35 | — |
| [ON_MOONLIT_NIGHT](../sources/higgsfield/prompts/ON_MOONLIT_NIGHT/) | — | 254 | 0/0 | default×173、videotape-alpha×24 | — |
| [TV_4K](../sources/higgsfield/prompts/TV_4K/) | 超写实短片拆解（uuid 锚+教学 folder 学） | 254 | 224/30 | seedance_2_0×180、soul_cinematic×40、gpt_image_2×25 | [docs](../sources/higgsfield/projects/TV_4K/) |
| [REWIND](../sources/higgsfield/prompts/REWIND/) | — | 253 | 118/0 | seedance_2_0_fast×114、default×66、videotape-alpha×47 | — |
| [THREAD](../sources/higgsfield/prompts/THREAD/) | — | 253 | 169/84 | seedance_2_5×131、nano_banana_2×60、soul_cinematic×38 | [docs](../sources/higgsfield/projects/THREAD/) |
| [WHAT_THE_THREAD_LEFT_BEHIND](../sources/higgsfield/prompts/WHAT_THE_THREAD_LEFT_BEHIND/) | — | 252 | 0/0 | default×55、videotape-alpha×13、video_extension×2 | — |
| [BETWEEN_TWO_SHORES](../sources/higgsfield/prompts/BETWEEN_TWO_SHORES/) | — | 250 | 0/0 | default×70、video_extension×19、videotape-alpha×8 | — |
| [I_WAS_HERE_FIRST](../sources/higgsfield/prompts/I_WAS_HERE_FIRST/) | — | 248 | 0/0 | default×121、videotape-alpha×1 | — |
| [INVERSION_GENESIS](../sources/higgsfield/prompts/INVERSION_GENESIS/) | — | 247 | 0/0 | default×166、videotape-alpha×45、video_extension×4 | — |
| [MEMORY_THIEF](../sources/higgsfield/prompts/MEMORY_THIEF/) | — | 247 | 0/0 | video_extension×174、default×29、video_edit×29 | — |
| [NADIA_7_OF_9](../sources/higgsfield/prompts/NADIA_7_OF_9/) | — | 247 | 1/0 | default×73、videotape-alpha×58、seedance_2_0×1 | — |
| [ROOTED](../sources/higgsfield/prompts/ROOTED/) | — | 247 | 0/0 | default×88、video_extension×81、videotape-alpha×6 | — |
| [NEUROVERSE_STILL_AGLOW](../sources/higgsfield/prompts/NEUROVERSE_STILL_AGLOW/) | — | 246 | 7/0 | default×30、sunburst×15、seedance_2_0×6 | — |
| [UNCOUNTED](../sources/higgsfield/prompts/UNCOUNTED/) | — | 246 | 99/0 | seedance_2_0×98、videotape-alpha×27、seedance_2_0_fast×1 | — |
| [NIGHTBLOOM](../sources/higgsfield/prompts/NIGHTBLOOM/) | — | 245 | 1/0 | default×168、videotape-alpha×36、video_extension×6 | — |
| [WHISPER](../sources/higgsfield/prompts/WHISPER/) | — | 245 | 1/0 | default×61、videotape-alpha×12、video_edit×1 | — |
| [5_MINUTES](../sources/higgsfield/prompts/5_MINUTES/) | — | 244 | 0/0 | default×124、video_edit×29、videotape-alpha×21 | — |
| [GENERATE](../sources/higgsfield/prompts/GENERATE/) | — | 244 | 0/0 | default×107、video_extension×67、video_edit×1 | — |
| [CARRIED](../sources/higgsfield/prompts/CARRIED/) | — | 243 | 91/0 | seedance_2_0×85、default×36、videotape-alpha×22 | — |
| [STILL_SWEET](../sources/higgsfield/prompts/STILL_SWEET/) | — | 243 | 0/0 | default×121、video_edit×3、videotape-alpha×1 | — |
| [HUNTER_PROTOCOL](../sources/higgsfield/prompts/HUNTER_PROTOCOL/) | — | 242 | 0/0 | default×47、sunburst×1、videotape-alpha×1 | — |
| [HWANDO_SEOL](../sources/higgsfield/prompts/HWANDO_SEOL/) | — | 241 | 1/0 | default×158、videotape-alpha×22、sunburst×21 | — |
| [THE_SEER](../sources/higgsfield/prompts/THE_SEER/) | — | 241 | 153/0 | seedance_2_0×153、minimax×2、flare×1 | — |
| [DREAMER_THE_OTHER_YOU](../sources/higgsfield/prompts/DREAMER_THE_OTHER_YOU/) | — | 239 | 2/0 | default×135、videotape-alpha×3、seedance_2_0×2 | — |
| [LUCID_DREAMS](../sources/higgsfield/prompts/LUCID_DREAMS/) | — | 237 | 0/0 | default×79、videotape-alpha×1、video_edit×1 | — |
| [DAYLIGHT_SAVING_TIME](../sources/higgsfield/prompts/DAYLIGHT_SAVING_TIME/) | — | 235 | 0/0 | default×103、video_extension×69、video_edit×1 | — |
| [KAGEROU](../sources/higgsfield/prompts/KAGEROU/) | — | 235 | 183/52 | seedance_2_5×133、soul_cinematic×41、nano_banana_flash×36 | [docs](../sources/higgsfield/projects/KAGEROU/) |
| [PERSISTENCE](../sources/higgsfield/prompts/PERSISTENCE/) | — | 235 | 53/0 | videotape-alpha×70、seedance_2_0×53、default×16 | — |
| [FAUST](../sources/higgsfield/prompts/FAUST/) | — | 234 | 0/0 | default×160 | — |
| [LAIKA](../sources/higgsfield/prompts/LAIKA/) | — | 234 | 48/0 | seedance_2_0×48、default×1 | — |
| [MAKE_BELIEVE](../sources/higgsfield/prompts/MAKE_BELIEVE/) | — | 234 | 1/0 | default×34、videotape-alpha×34、sunburst×26 | — |
| [BASH](../sources/higgsfield/prompts/BASH/) | — | 233 | 0/0 | default×48、videotape-alpha×14、sunburst×4 | — |
| [OOPS](../sources/higgsfield/prompts/OOPS/) | — | 233 | 0/0 | default×57、videotape-alpha×5 | — |
| [THE_LAST_RIDE](../sources/higgsfield/prompts/THE_LAST_RIDE/) | — | 232 | 156/74 | seedance_2_5×149、seedream_v5_pro×67、seedance_2_0×6 | [docs](../sources/higgsfield/projects/THE_LAST_RIDE/) |
| [IDALIA](../sources/higgsfield/prompts/IDALIA/) | — | 231 | 7/0 | seedance_2_0×7、videotape-alpha×7、sunburst×2 | — |
| [313_INTERNATIONAL](../sources/higgsfield/prompts/313_INTERNATIONAL/) | — | 230 | 0/0 | default×63、video_edit×8、videotape-alpha×3 | — |
| [DISCONNECTED](../sources/higgsfield/prompts/DISCONNECTED/) | — | 230 | 0/0 | default×142 | — |
| [HOW_TO_DIE](../sources/higgsfield/prompts/HOW_TO_DIE/) | — | 230 | 2/0 | default×25、seedance_2_0×2、video_extension×1 | — |
| [THE_MOUSE](../sources/higgsfield/prompts/THE_MOUSE/) | — | 230 | 0/0 | default×95、video_extension×7、videotape-alpha×4 | — |
| [THE_SEVENTH_MONTH_GUEST](../sources/higgsfield/prompts/THE_SEVENTH_MONTH_GUEST/) | — | 230 | 8/0 | videotape-alpha×62、default×58、video_extension×18 | — |
| [ASHES_OF_FREEDOM](../sources/higgsfield/prompts/ASHES_OF_FREEDOM/) | — | 229 | 24/0 | default×59、seedance_2_0×24、videotape-alpha×2 | — |
| [THE_ECHO_OF_US](../sources/higgsfield/prompts/THE_ECHO_OF_US/) | — | 229 | 0/0 | video_extension×134、default×12、videotape-alpha×1 | — |
| [KARNA](../sources/higgsfield/prompts/KARNA/) | — | 228 | 210/0 | seedance_2_0×210、sunburst×2 | — |
| [THE_DAY_I_FAILED](../sources/higgsfield/prompts/THE_DAY_I_FAILED/) | — | 227 | 1/0 | default×109、video_extension×32、videotape-alpha×17 | — |
| [AS_LONG_AS_IT_BLOOMS](../sources/higgsfield/prompts/AS_LONG_AS_IT_BLOOMS/) | — | 226 | 1/0 | default×164、videotape-alpha×17、seedance_2_0×1 | — |
| [MECHDRIVER_1](../sources/higgsfield/prompts/MECHDRIVER_1/) | — | 225 | 4/0 | default×100、seedance_2_0×4、video_edit×2 | — |
| [THE_BREACH](../sources/higgsfield/prompts/THE_BREACH/) | — | 225 | 0/0 | default×120、video_extension×19、videotape-alpha×9 | — |
| [BETWEEN_SOUNDS](../sources/higgsfield/prompts/BETWEEN_SOUNDS/) | — | 224 | 0/0 | default×94 | — |
| [THE_WORLD_WORTH_LIVING_IN](../sources/higgsfield/prompts/THE_WORLD_WORTH_LIVING_IN/) | — | 224 | 0/0 | default×103、video_extension×66、videotape-alpha×1 | — |
| [WOUND](../sources/higgsfield/prompts/WOUND/) | — | 224 | 0/0 | default×92 | — |
| [BREATH](../sources/higgsfield/prompts/BREATH/) | — | 223 | 0/0 | default×95 | — |
| [MORTEM](../sources/higgsfield/prompts/MORTEM/) | — | 223 | 0/0 | default×73、video_extension×25、videotape-alpha×3 | — |
| [BEFORE_THE_GODS](../sources/higgsfield/prompts/BEFORE_THE_GODS/) | — | 222 | 0/0 | default×47、pro×4 | — |
| [DISPENSABLE](../sources/higgsfield/prompts/DISPENSABLE/) | — | 222 | 0/0 | default×76、videotape-alpha×61、video_extension×1 | — |
| [SUBSTRATE](../sources/higgsfield/prompts/SUBSTRATE/) | — | 222 | 1/0 | default×62、videotape-alpha×57、video_extension×4 | — |
| [THE_WEIGHT_OF_THE_MOON](../sources/higgsfield/prompts/THE_WEIGHT_OF_THE_MOON/) | — | 222 | 0/0 | default×178、videotape-alpha×5、Redefine×2 | — |
| [UNHEARD](../sources/higgsfield/prompts/UNHEARD/) | — | 222 | 0/0 | default×106、sunburst×1 | — |
| [GREEN_FLAG](../sources/higgsfield/prompts/GREEN_FLAG/) | — | 221 | 1/0 | default×92、videotape-alpha×5、seedance_2_0×1 | — |
| [DUSK](../sources/higgsfield/prompts/DUSK/) | 三集剧集（seedance_2.5 全锁链 16 段式） | 220 | 165/54 | seedance_2_5×79、seedance_2_0×79、text2image_soul_v2×17 | [docs](../sources/higgsfield/projects/DUSK/) |
| [MAI](../sources/higgsfield/prompts/MAI/) | — | 220 | 2/0 | default×129、videotape-alpha×11、seedance_2_0×2 | — |
| [GILT](../sources/higgsfield/prompts/GILT/) | — | 219 | 0/0 | default×179、videotape-alpha×1 | — |
| [MISHMASH](../sources/higgsfield/prompts/MISHMASH/) | — | 219 | 0/0 | default×105、sunburst×4、videotape-alpha×2 | — |
| [RIFT_RIDER](../sources/higgsfield/prompts/RIFT_RIDER/) | — | 219 | 0/0 | default×73 | — |
| [KOK_BORU](../sources/higgsfield/prompts/KOK_BORU/) | 中亚马背叼羊，手绘 EN 风格 | 218 | 0/0 | 未标注 | [docs](../sources/higgsfield/projects/KOK_BORU/) |
| [HOPE](../sources/higgsfield/prompts/HOPE/) | — | 217 | 40/0 | default×103、seedance_2_0×40、video_edit×2 | — |
| [I_RECOMMEND_FINDING_ANOTHER_PLATFORM_TO_INVEST_YOU](../sources/higgsfield/prompts/I_RECOMMEND_FINDING_ANOTHER_PLATFORM_TO_INVEST_YOU/) | — | 217 | 0/0 | default×49 | — |
| [MARUMAI_25](../sources/higgsfield/prompts/MARUMAI_25/) | — | 216 | 4/0 | default×105、videotape-alpha×63、sunburst×39 | — |
| [ROAR](../sources/higgsfield/prompts/ROAR/) | — | 215 | 62/0 | seedance_2_0×53、seedance_2_0_fast×9、default×3 | — |
| [MY_OWN_DOING](../sources/higgsfield/prompts/MY_OWN_DOING/) | — | 214 | 116/0 | seedance_2_0×116、videotape-alpha×94、default×1 | — |
| [SUB_OBJECT](../sources/higgsfield/prompts/SUB_OBJECT/) | — | 214 | 0/0 | default×130、video_extension×7、videotape-alpha×4 | — |
| [TOGETHER_FOREVER](../sources/higgsfield/prompts/TOGETHER_FOREVER/) | — | 214 | 116/0 | seedance_2_0×116 | — |
| [VORTEX](../sources/higgsfield/prompts/VORTEX/) | — | 213 | 0/0 | default×51、video_extension×24、video_edit×6 | — |
| [ABIOGENE3](../sources/higgsfield/prompts/ABIOGENE3/) | — | 212 | 10/0 | seedance_2_0_fast×8、default×4、seedance_2_0×2 | — |
| [BEYOND_THE_STARS_A_KOREAN_SPACE_OPERA](../sources/higgsfield/prompts/BEYOND_THE_STARS_A_KOREAN_SPACE_OPERA/) | — | 212 | 61/0 | default×107、seedance_2_0×58、videotape-alpha×30 | — |
| [M_TRO_BOULOT_DODO](../sources/higgsfield/prompts/M_TRO_BOULOT_DODO/) | — | 212 | 0/0 | default×2 | — |
| [ONE_LAST_ACT](../sources/higgsfield/prompts/ONE_LAST_ACT/) | — | 212 | 2/0 | default×120、videotape-alpha×22、video_edit×2 | — |
| [THE_WRONG_PROMPT](../sources/higgsfield/prompts/THE_WRONG_PROMPT/) | — | 210 | 3/0 | default×49、videotape-alpha×7、seedance_2_0_fast×3 | — |
| [THE_PERFECT_ONE](../sources/higgsfield/prompts/THE_PERFECT_ONE/) | — | 209 | 3/0 | default×86、seedance_2_0_fast×3 | — |
| [SOMETIME_SOMEWHERE](../sources/higgsfield/prompts/SOMETIME_SOMEWHERE/) | — | 208 | 0/0 | default×103、videotape-alpha×4 | — |
| [THE_KISS](../sources/higgsfield/prompts/THE_KISS/) | — | 207 | 81/126 | nano_banana_2×95、seedance_2_5×69、text2image_soul_v2×15 | [docs](../sources/higgsfield/projects/THE_KISS/) |
| [EDEN](../sources/higgsfield/prompts/EDEN/) | — | 206 | 0/0 | default×127、videotape-alpha×2 | — |
| [PLUS_INTEREST](../sources/higgsfield/prompts/PLUS_INTEREST/) | — | 206 | 0/0 | default×94、video_extension×38、videotape-alpha×1 | — |
| [9091](../sources/higgsfield/prompts/9091/) | — | 205 | 0/0 | default×147、videotape-alpha×4、video_edit×3 | — |
| [EASY_TARGET](../sources/higgsfield/prompts/EASY_TARGET/) | — | 205 | 0/0 | default×146、videotape-alpha×31 | — |
| [SEKOLAH](../sources/higgsfield/prompts/SEKOLAH/) | — | 205 | 2/0 | default×53、videotape-alpha×1、seedance_2_0×1 | — |
| [DECRETUM](../sources/higgsfield/prompts/DECRETUM/) | — | 203 | 138/65 | seedance_2_5×133、nano_banana_flash×39、seedream_v5_lite×12 | [docs](../sources/higgsfield/projects/DECRETUM/) |
| [GABRIEL](../sources/higgsfield/prompts/GABRIEL/) | — | 203 | 13/0 | default×95、seedance_2_0×13、video_edit×5 | — |
| [CAT_STORY](../sources/higgsfield/prompts/CAT_STORY/) | — | 202 | 134/0 | seedance_2_0×134、videotape-alpha×29 | — |
| [AI_FILM_FESTIVAL_A_PROPER_WOMAN_S_GUIDE_TO_MONSTER](../sources/higgsfield/prompts/AI_FILM_FESTIVAL_A_PROPER_WOMAN_S_GUIDE_TO_MONSTER/) | — | 201 | 0/0 | default×159 | — |
| [ECHOES_OF_TOMORROW](../sources/higgsfield/prompts/ECHOES_OF_TOMORROW/) | — | 199 | 1/0 | default×87、videotape-alpha×14、pro×14 | — |
| [REST_FACE](../sources/higgsfield/prompts/REST_FACE/) | — | 198 | 114/84 | seedance_2_5×114、seedream_v5_pro×84 | [docs](../sources/higgsfield/projects/REST_FACE/) |
| [BRIDGE](../sources/higgsfield/prompts/BRIDGE/) | — | 197 | 0/0 | default×96、videotape-alpha×30、video_edit×5 | — |
| [THE_SHAPE_OF_MEMORIES](../sources/higgsfield/prompts/THE_SHAPE_OF_MEMORIES/) | — | 197 | 0/0 | default×47、video_extension×23、video_edit×3 | — |
| [THE_TINTERS](../sources/higgsfield/prompts/THE_TINTERS/) | — | 197 | 28/0 | default×37、seedance_2_0×28、videotape-alpha×1 | — |
| [PETYA](../sources/higgsfield/prompts/PETYA/) | — | 195 | 2/0 | default×106、videotape-alpha×56、seedance_2_0×2 | — |
| [TERMS_CONDEMNATIONS](../sources/higgsfield/prompts/TERMS_CONDEMNATIONS/) | — | 195 | 11/0 | videotape-alpha×49、default×35、video_extension×13 | — |
| [DOUBLE_SIN](../sources/higgsfield/prompts/DOUBLE_SIN/) | — | 194 | 0/0 | videotape-alpha×7、default×3 | — |
| [APOCALYPSE_SQUAD](../sources/higgsfield/prompts/APOCALYPSE_SQUAD/) | — | 193 | 1/0 | default×81、video_extension×76、videotape-alpha×22 | — |
| [INDIGO](../sources/higgsfield/prompts/INDIGO/) | — | 193 | 24/0 | video_extension×48、default×41、seedance_2_0_fast×24 | — |
| [DEEP_CLEAN](../sources/higgsfield/prompts/DEEP_CLEAN/) | — | 192 | 1/0 | default×83、video_extension×24、videotape-alpha×7 | — |
| [EGO](../sources/higgsfield/prompts/EGO/) | — | 192 | 134/0 | seedance_2_0×101、default×36、seedance_2_0_fast×33 | — |
| [THE_LAST_DANCE](../sources/higgsfield/prompts/THE_LAST_DANCE/) | — | 192 | 0/0 | default×87、sunburst×8、videotape-alpha×4 | — |
| [SERVUS](../sources/higgsfield/prompts/SERVUS/) | — | 190 | 10/0 | default×61、seedance_2_0×10、videotape-alpha×9 | — |
| [GUT_PUNCH_LOVE](../sources/higgsfield/prompts/GUT_PUNCH_LOVE/) | — | 188 | 4/0 | video_extension×63、default×40、seedance_2_0×4 | — |
| [THE_BRIDGE_90_MILES_APART](../sources/higgsfield/prompts/THE_BRIDGE_90_MILES_APART/) | — | 188 | 0/0 | default×89 | — |
| [COLD_NOTE](../sources/higgsfield/prompts/COLD_NOTE/) | — | 187 | 6/0 | default×34、video_extension×14、seedance_2_0_fast×6 | — |
| [PHASES](../sources/higgsfield/prompts/PHASES/) | — | 187 | 0/0 | default×148、video_edit×6、videotape-alpha×3 | — |
| [SINDBAD_THE_SEA_REMEMBERS](../sources/higgsfield/prompts/SINDBAD_THE_SEA_REMEMBERS/) | — | 187 | 0/0 | default×62、videotape-alpha×40、video_edit×5 | — |
| [WILD_KIN](../sources/higgsfield/prompts/WILD_KIN/) | — | 187 | 0/0 | default×130、videotape-alpha×53 | — |
| [LATCH](../sources/higgsfield/prompts/LATCH/) | — | 186 | 6/0 | default×88、seedance_2_0×6 | — |
| [NOTHING](../sources/higgsfield/prompts/NOTHING/) | — | 186 | 0/0 | default×92、video_edit×20、videotape-alpha×3 | — |
| [THREE_STEPS](../sources/higgsfield/prompts/THREE_STEPS/) | — | 186 | 0/0 | default×130、video_edit×1 | — |
| [UNDER_SATURN_S_SHADOW](../sources/higgsfield/prompts/UNDER_SATURN_S_SHADOW/) | — | 185 | 3/0 | default×87、videotape-alpha×7、seedance_2_0×3 | — |
| [THE_AVERAGE_JOE](../sources/higgsfield/prompts/THE_AVERAGE_JOE/) | — | 184 | 0/0 | default×90、videotape-alpha×46 | — |
| [THE_LEGEND_OF_VANARA](../sources/higgsfield/prompts/THE_LEGEND_OF_VANARA/) | — | 184 | 0/0 | videotape-alpha×87、default×72、sunburst×2 | — |
| [THE_MEDICAL_NUMBER](../sources/higgsfield/prompts/THE_MEDICAL_NUMBER/) | — | 184 | 0/0 | default×66 | — |
| [THE_MOUNTAIN_KEEPS](../sources/higgsfield/prompts/THE_MOUNTAIN_KEEPS/) | — | 184 | 0/0 | default×73、video_extension×46、videotape-alpha×1 | — |
| [AZAR_THE_IMMORTAL_WOUND](../sources/higgsfield/prompts/AZAR_THE_IMMORTAL_WOUND/) | — | 183 | 0/0 | default×37、videotape-alpha×8、sunburst×3 | — |
| [ONE_MILLION_DOLLARS](../sources/higgsfield/prompts/ONE_MILLION_DOLLARS/) | — | 183 | 1/0 | default×57、videotape-alpha×4、seedance_2_0×1 | — |
| [RAW_AND_REAL](../sources/higgsfield/prompts/RAW_AND_REAL/) | — | 183 | 9/0 | default×68、seedance_2_0×7、videotape-alpha×5 | — |
| [ALL_THE_MONSTERS_WE_COULDN_T_SEE](../sources/higgsfield/prompts/ALL_THE_MONSTERS_WE_COULDN_T_SEE/) | — | 182 | 0/0 | default×32、videotape-alpha×6 | — |
| [THE_AUDITION](../sources/higgsfield/prompts/THE_AUDITION/) | — | 182 | 2/0 | default×74、video_edit×25、seedance_2_0_fast×2 | — |
| [THE_BALLOON](../sources/higgsfield/prompts/THE_BALLOON/) | — | 182 | 0/0 | default×104、videotape-alpha×1 | — |
| [RACER18](../sources/higgsfield/prompts/RACER18/) | — | 181 | 132/49 | cinematic_studio_video_4_0×132、gpt_image_2×49 | [docs](../sources/higgsfield/projects/RACER18/) |
| [WRECK_QUEST](../sources/higgsfield/prompts/WRECK_QUEST/) | — | 181 | 138/0 | seedance_2_0×138、default×2 | — |
| [SUPER_SENIORS](../sources/higgsfield/prompts/SUPER_SENIORS/) | — | 180 | 0/0 | videotape-alpha×156、default×15 | — |
| [TRESPASSER](../sources/higgsfield/prompts/TRESPASSER/) | — | 180 | 7/0 | default×47、videotape-alpha×16、seedance_2_0×7 | — |
| [ONE_DROP](../sources/higgsfield/prompts/ONE_DROP/) | — | 178 | 1/0 | default×77、videotape-alpha×2、pro×1 | — |
| [ABUELO](../sources/higgsfield/prompts/ABUELO/) | — | 176 | 3/0 | default×83、videotape-alpha×31、seedance_2_0×3 | — |
| [BEHIND_THE_LENS](../sources/higgsfield/prompts/BEHIND_THE_LENS/) | — | 176 | 0/0 | default×55、videotape-alpha×12 | — |
| [CAMEL](../sources/higgsfield/prompts/CAMEL/) | — | 176 | 0/0 | default×95、videotape-alpha×55、sunburst×5 | — |
| [FULL_TIME_MOVIE](../sources/higgsfield/prompts/FULL_TIME_MOVIE/) | — | 176 | 0/0 | default×79、videotape-alpha×9 | — |
| [MOREK](../sources/higgsfield/prompts/MOREK/) | — | 176 | 0/0 | default×115、videotape-alpha×1 | — |
| [HERU_OUTSIDE_THE_FEED](../sources/higgsfield/prompts/HERU_OUTSIDE_THE_FEED/) | — | 174 | 0/0 | default×92、videotape-alpha×61、video_extension×6 | — |
| [JIU_JITSU_BEAR](../sources/higgsfield/prompts/JIU_JITSU_BEAR/) | — | 174 | 0/0 | default×100 | — |
| [THANK_YOU_FOR_YOUR_HONESTY](../sources/higgsfield/prompts/THANK_YOU_FOR_YOUR_HONESTY/) | — | 173 | 1/0 | default×67、sunburst×9、videotape-alpha×4 | — |
| [THE_DAY](../sources/higgsfield/prompts/THE_DAY/) | — | 173 | 2/0 | default×71、video_edit×3、videotape-alpha×2 | — |
| [THE_BOY_WHO_KEPT_THE_SUN](../sources/higgsfield/prompts/THE_BOY_WHO_KEPT_THE_SUN/) | — | 171 | 0/0 | videotape-alpha×89、default×80 | — |
| [WHAT_IS_LEFT_IS_WIND](../sources/higgsfield/prompts/WHAT_IS_LEFT_IS_WIND/) | — | 171 | 0/0 | default×60、videotape-alpha×21、video_edit×1 | — |
| [THE_CURE](../sources/higgsfield/prompts/THE_CURE/) | — | 170 | 0/0 | default×88、sunburst×24、video_extension×20 | — |
| [YAKAMOZ](../sources/higgsfield/prompts/YAKAMOZ/) | — | 170 | 0/0 | default×59、video_extension×33、video_edit×2 | — |
| [ONE_OF_US](../sources/higgsfield/prompts/ONE_OF_US/) | — | 168 | 0/0 | default×112、video_edit×3 | — |
| [THIS_ISNT_ART](../sources/higgsfield/prompts/THIS_ISNT_ART/) | — | 168 | 62/102 | cinematic_studio_video_4_0×61、nano_banana×60、nano_banana_2×29 | [docs](../sources/higgsfield/projects/THIS_ISNT_ART/) |
| [YOU_TIED_IT_WRONG](../sources/higgsfield/prompts/YOU_TIED_IT_WRONG/) | — | 168 | 6/0 | default×89、seedance_2_0×6、video_edit×1 | — |
| [DOODLE_DID_IT](../sources/higgsfield/prompts/DOODLE_DID_IT/) | — | 166 | 0/0 | default×102、videotape-alpha×42 | — |
| [INNER_PEACE](../sources/higgsfield/prompts/INNER_PEACE/) | — | 166 | 3/0 | default×54、videotape-alpha×5、sunburst×5 | — |
| [BILL](../sources/higgsfield/prompts/BILL/) | — | 162 | 0/0 | default×103 | — |
| [BUFFALO_FISH_OF_DUKONG](../sources/higgsfield/prompts/BUFFALO_FISH_OF_DUKONG/) | — | 162 | 3/0 | default×82、videotape-alpha×6、veo-3-1-preview×3 | — |
| [KARKINOS](../sources/higgsfield/prompts/KARKINOS/) | — | 161 | 0/0 | default×49、videotape-alpha×2 | — |
| [PON](../sources/higgsfield/prompts/PON/) | — | 161 | 0/0 | default×76、videotape-alpha×4 | — |
| [SKYGAZER](../sources/higgsfield/prompts/SKYGAZER/) | — | 161 | 0/0 | default×71、videotape-alpha×61、video_edit×2 | — |
| [OLFEMIO_COLORS](../sources/higgsfield/prompts/OLFEMIO_COLORS/) | — | 160 | 1/0 | default×88、video_extension×38、seedance_2_0×1 | — |
| [ADAM](../sources/higgsfield/prompts/ADAM/) | — | 159 | 88/0 | seedance_2_0×88、videotape-alpha×3 | — |
| [NESCIO](../sources/higgsfield/prompts/NESCIO/) | — | 159 | 0/0 | default×50、flare×7、video_extension×1 | — |
| [CLAMSHELL](../sources/higgsfield/prompts/CLAMSHELL/) | — | 158 | 0/0 | default×80、videotape-alpha×41 | — |
| [MY_WAY_NAVILLUS](../sources/higgsfield/prompts/MY_WAY_NAVILLUS/) | — | 157 | 0/0 | default×96、videotape-alpha×61 | — |
| [FALLEN_LEAVES](../sources/higgsfield/prompts/FALLEN_LEAVES/) | — | 156 | 127/29 | seedance_2_5×126、gpt_image_2×29、seedance_2_0×1 | [docs](../sources/higgsfield/projects/FALLEN_LEAVES/) |
| [AGAPI_MOU](../sources/higgsfield/prompts/AGAPI_MOU/) | — | 155 | 1/0 | default×40、videotape-alpha×35、seedance_2_0×1 | — |
| [LOAD_BEARING](../sources/higgsfield/prompts/LOAD_BEARING/) | — | 155 | 3/0 | default×111、seedance_2_0×3、video_extension×1 | — |
| [DRACHM_DORS](../sources/higgsfield/prompts/DRACHM_DORS/) | — | 154 | 1/0 | default×48、videotape-alpha×1、seedance_2_0×1 | — |
| [MELEDOF_THE_REBIRTH_OF_A_HERO](../sources/higgsfield/prompts/MELEDOF_THE_REBIRTH_OF_A_HERO/) | — | 154 | 0/0 | videotape-alpha×65、default×65、video_extension×4 | — |
| [THE_LAST_SECOND](../sources/higgsfield/prompts/THE_LAST_SECOND/) | — | 154 | 0/0 | default×54、videotape-alpha×23 | — |
| [THE_SIGNAL_BETWEEN_WORDS](../sources/higgsfield/prompts/THE_SIGNAL_BETWEEN_WORDS/) | — | 153 | 1/0 | default×70、video_edit×2、seedance_2_0×1 | — |
| [DUST_FEATHERS](../sources/higgsfield/prompts/DUST_FEATHERS/) | — | 152 | 0/0 | default×74、videotape-alpha×54、video_extension×2 | — |
| [WHERE_LETTERS_FALL](../sources/higgsfield/prompts/WHERE_LETTERS_FALL/) | — | 152 | 0/0 | default×72、video_extension×31、video_edit×3 | — |
| [NALA_HEADS_DROP](../sources/higgsfield/prompts/NALA_HEADS_DROP/) | 音乐 MV（21:9+Vision3 胶片宪法） | 151 | 143/8 | seedance_2_0×139、nano_banana_2×8、soul_cinematic×4 | [docs](../sources/higgsfield/projects/NALA_HEADS_DROP/) |
| [WELCOME_TO_THE_TEAM](../sources/higgsfield/prompts/WELCOME_TO_THE_TEAM/) | — | 150 | 0/0 | default×61、videotape-alpha×1 | — |
| [THE_LAST_VOW](../sources/higgsfield/prompts/THE_LAST_VOW/) | — | 148 | 0/0 | default×108、videotape-alpha×1 | — |
| [SOUL_CAROUSELS](../sources/higgsfield/prompts/SOUL_CAROUSELS/) | 栏目制轮播美学（短 prompt 氛围堆叠） | 145 | 0/145 | text2image_soul_v2×138、gpt_image_2×6、nano_banana_2×1 | [docs](../sources/higgsfield/projects/SOUL_CAROUSELS/) |
| [THE_NEXT_MOVE](../sources/higgsfield/prompts/THE_NEXT_MOVE/) | — | 145 | 0/0 | default×50 | — |
| [WORD_VS_WORLD](../sources/higgsfield/prompts/WORD_VS_WORLD/) | — | 145 | 28/0 | default×75、seedance_2_0×26、videotape-alpha×4 | — |
| [FOOL_S_GOLD](../sources/higgsfield/prompts/FOOL_S_GOLD/) | — | 144 | 0/0 | default×66、videotape-alpha×1 | — |
| [THE_WEEKEND](../sources/higgsfield/prompts/THE_WEEKEND/) | — | 144 | 0/0 | default×138 | — |
| [LOS_CENTINELAS_DE_LA_RED_THE_NET_SENTINLS](../sources/higgsfield/prompts/LOS_CENTINELAS_DE_LA_RED_THE_NET_SENTINLS/) | — | 143 | 1/0 | default×5、veo-3-1-fast×1 | — |
| [NINE_LIVES_AI_FILM_FESTIVAL](../sources/higgsfield/prompts/NINE_LIVES_AI_FILM_FESTIVAL/) | — | 143 | 0/0 | default×112、videotape-alpha×1 | — |
| [DYING_UNDER_THE_NEON_RAIN_FILM_TEASER](../sources/higgsfield/prompts/DYING_UNDER_THE_NEON_RAIN_FILM_TEASER/) | — | 142 | 1/0 | default×50、video_edit×4、seedance_2_0×1 | — |
| [FLY](../sources/higgsfield/prompts/FLY/) | — | 142 | 0/0 | default×118、video_extension×8、video_edit×7 | — |
| [HELLO_NYC](../sources/higgsfield/prompts/HELLO_NYC/) | — | 141 | 104/0 | seedance_2_0×104、videotape-alpha×21 | — |
| [MISTER_M](../sources/higgsfield/prompts/MISTER_M/) | — | 141 | 0/0 | default×117 | — |
| [THE_LAST_THING_SHE_HELD](../sources/higgsfield/prompts/THE_LAST_THING_SHE_HELD/) | — | 141 | 0/0 | default×44、videotape-alpha×17 | — |
| [IT_WAS_JUST_A_JOKE](../sources/higgsfield/prompts/IT_WAS_JUST_A_JOKE/) | — | 140 | 0/0 | default×102、videotape-alpha×3 | — |
| [UNDO](../sources/higgsfield/prompts/UNDO/) | — | 140 | 0/0 | default×47 | — |
| [BUCK](../sources/higgsfield/prompts/BUCK/) | — | 139 | 0/0 | default×51、videotape-alpha×6、video_extension×1 | — |
| [MOONLIT_TAIL](../sources/higgsfield/prompts/MOONLIT_TAIL/) | — | 138 | 11/0 | default×93、seedance_2_0×11 | — |
| [PINK_TRIANGLE](../sources/higgsfield/prompts/PINK_TRIANGLE/) | — | 137 | 0/0 | video_extension×26、default×19 | — |
| [14_DAYS](../sources/higgsfield/prompts/14_DAYS/) | — | 136 | 0/0 | default×106、video_extension×21 | — |
| [ANIME_PRODUCTION](../sources/higgsfield/prompts/ANIME_PRODUCTION/) | 图库先行动画生产（seedream 图→seedance 动画化） | 136 | 6/130 | seedream_v5_pro×110、text2image_soul_v2×20、seedance_2_0×5 | [docs](../sources/higgsfield/projects/ANIME_PRODUCTION/) |
| [DAYS_OF_LOVE](../sources/higgsfield/prompts/DAYS_OF_LOVE/) | — | 136 | 0/0 | default×45、videotape-alpha×6 | — |
| [QURAN_HEALS_THE_HEARTS](../sources/higgsfield/prompts/QURAN_HEALS_THE_HEARTS/) | — | 136 | 1/0 | default×26、seedance_2_0×1 | — |
| [RECOMMENDED](../sources/higgsfield/prompts/RECOMMENDED/) | — | 136 | 0/0 | video_extension×26、default×17、videotape-alpha×4 | — |
| [LAST_BREATH](../sources/higgsfield/prompts/LAST_BREATH/) | — | 135 | 0/0 | default×99、pro×1 | — |
| [MY_LITTLE_VILLAIN](../sources/higgsfield/prompts/MY_LITTLE_VILLAIN/) | — | 135 | 0/0 | default×75、video_extension×3 | — |
| [A_CALL_FROM_HORMUZ](../sources/higgsfield/prompts/A_CALL_FROM_HORMUZ/) | — | 133 | 0/0 | default×79、video_edit×10、pro×6 | — |
| [PERMANENT](../sources/higgsfield/prompts/PERMANENT/) | — | 133 | 0/0 | video_extension×67、default×37、videotape-alpha×14 | — |
| [THE_NEW_GIRL](../sources/higgsfield/prompts/THE_NEW_GIRL/) | 双线叙事剧集（FINAL 版次管理） | 132 | 71/61 | seedance_2_0×71、nano_banana_2×32、text2image_soul_v2×20 | [docs](../sources/higgsfield/projects/THE_NEW_GIRL/) |
| [THE_WRATH_OF_THE_MONARCH](../sources/higgsfield/prompts/THE_WRATH_OF_THE_MONARCH/) | — | 132 | 0/0 | default×50、videotape-alpha×1 | — |
| [THE_LAST_GARDEN](../sources/higgsfield/prompts/THE_LAST_GARDEN/) | — | 131 | 43/0 | seedance_2_0×43、videotape-alpha×4 | — |
| [BUD_5_1](../sources/higgsfield/prompts/BUD_5_1/) | — | 130 | 0/0 | default×62 | — |
| [BRAMBLE](../sources/higgsfield/prompts/BRAMBLE/) | — | 129 | 1/0 | videotape-alpha×47、default×33、video_extension×33 | — |
| [THE_DREAMER](../sources/higgsfield/prompts/THE_DREAMER/) | — | 129 | 0/0 | default×71、video_edit×1 | — |
| [ATHERIA](../sources/higgsfield/prompts/ATHERIA/) | — | 128 | 0/0 | default×44、video_extension×36、flare×4 | — |
| [QARA_SHANYRAQ](../sources/higgsfield/prompts/QARA_SHANYRAQ/) | — | 123 | 0/0 | default×73、videotape-alpha×7 | — |
| [BARZAKH](../sources/higgsfield/prompts/BARZAKH/) | — | 122 | 0/0 | default×1 | — |
| [NAME_IS_COMET](../sources/higgsfield/prompts/NAME_IS_COMET/) | — | 121 | 1/0 | default×82、videotape-alpha×29、seedance_2_0×1 | — |
| [A_PLACE_CALLED_HOME](../sources/higgsfield/prompts/A_PLACE_CALLED_HOME/) | — | 120 | 0/0 | default×43 | — |
| [TOMMY_ALWAYS_DOES_THE_RIGHT_THING](../sources/higgsfield/prompts/TOMMY_ALWAYS_DOES_THE_RIGHT_THING/) | — | 120 | 0/0 | default×33 | — |
| [THE_LAST_CURE](../sources/higgsfield/prompts/THE_LAST_CURE/) | — | 119 | 0/0 | default×90、videotape-alpha×23 | — |
| [THE_PLAYGROUND](../sources/higgsfield/prompts/THE_PLAYGROUND/) | — | 119 | 2/0 | default×74、seedance_2_0×2 | — |
| [KNOCK_KNOCK_KNOCK](../sources/higgsfield/prompts/KNOCK_KNOCK_KNOCK/) | — | 117 | 0/0 | default×70、videotape-alpha×11、sunburst×6 | — |
| [MORTAL_KOMBAT_ARC_SERIES](../sources/higgsfield/prompts/MORTAL_KOMBAT_ARC_SERIES/) | — | 116 | 0/0 | default×116 | — |
| [IN_A_MINUTE](../sources/higgsfield/prompts/IN_A_MINUTE/) | — | 115 | 92/0 | seedance_2_0×92 | — |
| [THE_ONE_THAT_LOOKED](../sources/higgsfield/prompts/THE_ONE_THAT_LOOKED/) | — | 115 | 2/0 | video_extension×4、seedance_2_0_fast×2、default×2 | — |
| [MARCO_POLO](../sources/higgsfield/prompts/MARCO_POLO/) | — | 114 | 0/0 | default×31 | — |
| [MADA](../sources/higgsfield/prompts/MADA/) | — | 112 | 0/0 | default×38 | — |
| [NOT_A_MONSTER_MOVIE_A_ONE_TAKE_FILM](../sources/higgsfield/prompts/NOT_A_MONSTER_MOVIE_A_ONE_TAKE_FILM/) | — | 112 | 0/0 | video_extension×71、videotape-alpha×28、default×12 | — |
| [CONQUER_THE_WORLD_WITH_YOU](../sources/higgsfield/prompts/CONQUER_THE_WORLD_WITH_YOU/) | — | 111 | 0/0 | default×65、videotape-alpha×41 | — |
| [22_CASES_A_TRUE_CRIME_STORY](../sources/higgsfield/prompts/22_CASES_A_TRUE_CRIME_STORY/) | — | 110 | 0/0 | default×42、video_extension×13、videotape-alpha×8 | — |
| [LAST_CALL](../sources/higgsfield/prompts/LAST_CALL/) | — | 108 | 1/0 | default×51、videotape-alpha×8、seedance_2_0×1 | — |
| [NIGHTFORGE](../sources/higgsfield/prompts/NIGHTFORGE/) | — | 108 | 0/0 | default×55 | — |
| [SANTA_S_HAWAIIAN_VACATION](../sources/higgsfield/prompts/SANTA_S_HAWAIIAN_VACATION/) | — | 107 | 0/0 | default×37 | — |
| [BLACKPINE](../sources/higgsfield/prompts/BLACKPINE/) | — | 106 | 63/43 | seedance_2_5×62、text2image_soul_v2×22、nano_banana_2×18 | — |
| [LIFE_METER](../sources/higgsfield/prompts/LIFE_METER/) | — | 106 | 0/0 | default×60、videotape-alpha×3 | — |
| [YOU_HAD_TO](../sources/higgsfield/prompts/YOU_HAD_TO/) | — | 106 | 0/0 | default×63、videotape-alpha×25 | — |
| [LOST](../sources/higgsfield/prompts/LOST/) | — | 102 | 0/0 | default×57 | — |
| [THE_FESTIVAL](../sources/higgsfield/prompts/THE_FESTIVAL/) | — | 102 | 0/0 | default×76、videotape-alpha×5 | — |
| [THE_PARDON_GAMES](../sources/higgsfield/prompts/THE_PARDON_GAMES/) | — | 102 | 0/0 | default×51 | — |
| [AURA_SOURCE](../sources/higgsfield/prompts/AURA_SOURCE/) | — | 100 | 0/0 | default×40 | — |
| [CHIRAK](../sources/higgsfield/prompts/CHIRAK/) | — | 100 | 0/0 | default×26、video_edit×1 | — |
| [WONDER_AGENT](../sources/higgsfield/prompts/WONDER_AGENT/) | — | 100 | 0/0 | default×51、videotape-alpha×5 | — |
| [AURA](../sources/higgsfield/prompts/AURA/) | — | 99 | 0/0 | default×73 | — |
| [THE_VALLEY_OF_RUINS](../sources/higgsfield/prompts/THE_VALLEY_OF_RUINS/) | — | 99 | 0/0 | video_edit×27、default×4、videotape-alpha×3 | — |
| [TEST_21](../sources/higgsfield/prompts/TEST_21/) | — | 98 | 4/0 | default×55、videotape-alpha×18、seedance_2_0×4 | — |
| [777_THE_LAST_PRIZE](../sources/higgsfield/prompts/777_THE_LAST_PRIZE/) | — | 97 | 2/0 | video_extension×41、default×12、seedance_2_0×2 | — |
| [OUT_OF_FRAME](../sources/higgsfield/prompts/OUT_OF_FRAME/) | — | 96 | 0/0 | default×52、videotape-alpha×15 | — |
| [REVELATION](../sources/higgsfield/prompts/REVELATION/) | — | 96 | 0/0 | default×37、video_extension×4、videotape-alpha×4 | — |
| [THE_WEIGHT_OF_OUR_STEPS](../sources/higgsfield/prompts/THE_WEIGHT_OF_OUR_STEPS/) | — | 96 | 0/0 | default×34、videotape-alpha×2 | — |
| [MORE](../sources/higgsfield/prompts/MORE/) | — | 95 | 0/0 | default×71 | — |
| [SWAPPED](../sources/higgsfield/prompts/SWAPPED/) | — | 95 | 1/0 | default×47、videotape-alpha×21、video_extension×18 | — |
| [BLAKE_HERITAGE](../sources/higgsfield/prompts/BLAKE_HERITAGE/) | — | 93 | 0/0 | default×45、videotape-alpha×1 | — |
| [ILL_SLEEP_EARLY](../sources/higgsfield/prompts/ILL_SLEEP_EARLY/) | — | 93 | 47/46 | seedance_2_5×47、gpt_image_2_5×36、gpt_image_2×10 | [docs](../sources/higgsfield/projects/ILL_SLEEP_EARLY/) |
| [I_LL_SLEEP_EARLY_PROMISE](../sources/higgsfield/prompts/I_LL_SLEEP_EARLY_PROMISE/) | — | 93 | 0/0 | default×45、flare×36、videotape-alpha×10 | — |
| [SOUL_ANGEL](../sources/higgsfield/prompts/SOUL_ANGEL/) | — | 93 | 0/0 | default×45、videotape-alpha×2、video_edit×1 | — |
| [THE_ELEVATOR](../sources/higgsfield/prompts/THE_ELEVATOR/) | — | 93 | 0/0 | default×18、videotape-alpha×4、video_edit×3 | — |
| [JURASSIC_T_REX_ECHO](../sources/higgsfield/prompts/JURASSIC_T_REX_ECHO/) | — | 92 | 62/0 | seedance_2_0×62 | — |
| [DID_WE_HAVE_A_CHOICE](../sources/higgsfield/prompts/DID_WE_HAVE_A_CHOICE/) | — | 91 | 0/0 | default×50 | — |
| [OEDIPUS](../sources/higgsfield/prompts/OEDIPUS/) | — | 91 | 1/0 | default×30、pro×7、videotape-alpha×4 | — |
| [ONE_MORE_TIME](../sources/higgsfield/prompts/ONE_MORE_TIME/) | 音乐片一条流（handheld+hard cut） | 91 | 79/12 | seedance_2_0×79、nano_banana_2×10、text2image_soul_v2×2 | [docs](../sources/higgsfield/projects/ONE_MORE_TIME/) |
| [SOMEWHERE_STILL](../sources/higgsfield/prompts/SOMEWHERE_STILL/) | — | 91 | 0/0 | default×37、videotape-alpha×6 | — |
| [EXODUS](../sources/higgsfield/prompts/EXODUS/) | — | 90 | 0/0 | default×71、videotape-alpha×4、video_extension×1 | — |
| [S_KOU](../sources/higgsfield/prompts/S_KOU/) | — | 90 | 0/0 | videotape-alpha×76、default×13 | — |
| [THE_LITTLE_INTERPRETER](../sources/higgsfield/prompts/THE_LITTLE_INTERPRETER/) | — | 90 | 0/0 | default×51 | — |
| [SUNSHINE_9000M](../sources/higgsfield/prompts/SUNSHINE_9000M/) | — | 89 | 2/0 | flare×7、seedance_2_0×2、default×2 | — |
| [TRIP_TO_DUAT](../sources/higgsfield/prompts/TRIP_TO_DUAT/) | — | 89 | 26/0 | videotape-alpha×50、seedance_2_0_fast×26、default×2 | — |
| [BALI](../sources/higgsfield/prompts/BALI/) | — | 88 | 0/0 | default×19 | — |
| [THE_BEGINNING_TO_THE_END](../sources/higgsfield/prompts/THE_BEGINNING_TO_THE_END/) | — | 88 | 0/0 | default×41 | — |
| [GOODNIGHT_MILWAUKEE](../sources/higgsfield/prompts/GOODNIGHT_MILWAUKEE/) | — | 87 | 25/0 | default×51、seedance_2_0×25、video_edit×2 | — |
| [RESET_ME](../sources/higgsfield/prompts/RESET_ME/) | — | 87 | 0/0 | default×33、video_edit×4、videotape-alpha×1 | — |
| [OTTO](../sources/higgsfield/prompts/OTTO/) | — | 84 | 78/6 | seedance_2_5×72、soul_cinematic×5、gpt_image_2_5×4 | [docs](../sources/higgsfield/projects/OTTO/) |
| [SMALL](../sources/higgsfield/prompts/SMALL/) | — | 84 | 6/0 | default×36、videotape-alpha×7、seedance_2_0×6 | — |
| [DANCE_OF_THE_WRAITH](../sources/higgsfield/prompts/DANCE_OF_THE_WRAITH/) | — | 83 | 0/0 | default×75 | — |
| [PIXEL_BLOOM](../sources/higgsfield/prompts/PIXEL_BLOOM/) | — | 83 | 13/0 | seedance_2_0×13、default×1 | — |
| [CAMPING](../sources/higgsfield/prompts/CAMPING/) | — | 82 | 0/0 | default×59、videotape-alpha×2 | — |
| [THE_LAST_COLOR](../sources/higgsfield/prompts/THE_LAST_COLOR/) | — | 81 | 0/0 | default×54 | — |
| [UNDERRATED_SHORT_MOVIE](../sources/higgsfield/prompts/UNDERRATED_SHORT_MOVIE/) | — | 80 | 0/0 | default×49、videotape-alpha×30 | — |
| [BLINK](../sources/higgsfield/prompts/BLINK/) | — | 79 | 12/0 | default×44、seedance_2_0×12、videotape-alpha×6 | — |
| [THE_DEPARTMENT_OF_FORGOTTEN_THINGS](../sources/higgsfield/prompts/THE_DEPARTMENT_OF_FORGOTTEN_THINGS/) | — | 77 | 29/0 | videotape-alpha×46、seedance_2_0×27、seedance_2_0_fast×2 | — |
| [AFTER_HOURS](../sources/higgsfield/prompts/AFTER_HOURS/) | — | 76 | 0/0 | default×39、video_extension×2、videotape-alpha×2 | — |
| [TOP_UP_CINEMATIC_AD_BREAKDOWN](../sources/higgsfield/prompts/TOP_UP_CINEMATIC_AD_BREAKDOWN/) | — | 76 | 66/0 | seedance_2_0×66、videotape-alpha×4 | — |
| [UNTOLD_STORIES](../sources/higgsfield/prompts/UNTOLD_STORIES/) | — | 76 | 3/0 | default×55、seedance_2_0×3 | — |
| [HUNTRESS_TALE](../sources/higgsfield/prompts/HUNTRESS_TALE/) | 猎魔女战巨蛇奇幻动作（SHOT1-5 分镜结构） | 75 | 48/27 | seedance_2_0×48、nano_banana_2×16、text2image_soul_v2×7 | [docs](../sources/higgsfield/projects/HUNTRESS_TALE/) |
| [THE_PILL](../sources/higgsfield/prompts/THE_PILL/) | — | 74 | 0/0 | default×36 | — |
| [TOP_UP_AD](../sources/higgsfield/prompts/TOP_UP_AD/) | 机甲实拍广告拆解（官方教程句式实战迁移） | 74 | 68/6 | seedance_2_0×64、soul_cinematic×4、gpt_image_2×4 | [docs](../sources/higgsfield/projects/TOP_UP_AD/) |
| [THE_SEAM](../sources/higgsfield/prompts/THE_SEAM/) | — | 73 | 0/0 | default×56、video_edit×1、videotape-alpha×1 | — |
| [BLOOD_PASSAGES_THE_RETURN_OF_THE_CRIMSON_KING](../sources/higgsfield/prompts/BLOOD_PASSAGES_THE_RETURN_OF_THE_CRIMSON_KING/) | — | 72 | 0/0 | default×44、video_extension×2 | — |
| [COMING_BACK](../sources/higgsfield/prompts/COMING_BACK/) | — | 72 | 0/0 | default×19 | — |
| [IT_S_ME](../sources/higgsfield/prompts/IT_S_ME/) | — | 72 | 0/0 | default×17 | — |
| [THE_LAST_HARVEST](../sources/higgsfield/prompts/THE_LAST_HARVEST/) | — | 72 | 0/0 | default×46 | — |
| [TOKYO_4_17](../sources/higgsfield/prompts/TOKYO_4_17/) | — | 72 | 0/0 | default×52、videotape-alpha×5 | — |
| [KAI_CENAT_SU2_VFX](../sources/higgsfield/prompts/KAI_CENAT_SU2_VFX/) | — | 71 | 40/30 | seedance_2_0×39、nano_banana_2×23、gpt_image_2×7 | [docs](../sources/higgsfield/projects/KAI_CENAT_SU2_VFX/) |
| [THE_KNIFE](../sources/higgsfield/prompts/THE_KNIFE/) | — | 71 | 0/0 | video_extension×43、videotape-alpha×18、default×8 | — |
| [THE_LAST_BIT](../sources/higgsfield/prompts/THE_LAST_BIT/) | — | 71 | 0/0 | default×27 | — |
| [AGBOGBLOSHIE](../sources/higgsfield/prompts/AGBOGBLOSHIE/) | — | 70 | 0/0 | default×21 | — |
| [DETECTIVE_STORY](../sources/higgsfield/prompts/DETECTIVE_STORY/) | — | 70 | 0/0 | videotape-alpha×16、default×15 | — |
| [THE_STAFF](../sources/higgsfield/prompts/THE_STAFF/) | — | 70 | 0/0 | default×69 | — |
| [BATTLE_FOR_THE_MONOLITH](../sources/higgsfield/prompts/BATTLE_FOR_THE_MONOLITH/) | — | 69 | 0/0 | default×44 | — |
| [FOUR_YEARS_AND_SOME_FREAKS](../sources/higgsfield/prompts/FOUR_YEARS_AND_SOME_FREAKS/) | — | 68 | 1/0 | default×31、video_extension×4、video_edit×1 | — |
| [REWIND_CLUB](../sources/higgsfield/prompts/REWIND_CLUB/) | — | 68 | 30/0 | seedance_2_0×30 | — |
| [SEEDREAM_5_PRO_PAINTED_EDITORIAL](../sources/higgsfield/prompts/SEEDREAM_5_PRO_PAINTED_EDITORIAL/) | — | 68 | 0/0 | 未标注 | — |
| [THE_JOURNEY](../sources/higgsfield/prompts/THE_JOURNEY/) | — | 68 | 0/0 | videotape-alpha×20、default×11 | — |
| [THE_LIFE_HE_DIDN_T_LIVE](../sources/higgsfield/prompts/THE_LIFE_HE_DIDN_T_LIVE/) | — | 68 | 0/0 | 未标注 | — |
| [BY_YOUR_SIDE](../sources/higgsfield/prompts/BY_YOUR_SIDE/) | — | 66 | 0/0 | default×60、videotape-alpha×2、flare×1 | — |
| [SEED_AUDIO_1_0_LAUNCH_VIDEO](../sources/higgsfield/prompts/SEED_AUDIO_1_0_LAUNCH_VIDEO/) | — | 66 | 41/0 | seedance_2_0×41、videotape-alpha×1 | — |
| [SIMPLE_THINGS](../sources/higgsfield/prompts/SIMPLE_THINGS/) | — | 66 | 0/0 | default×46 | — |
| [MARY_MICKAEL_BRIDEWOOD_AI_FILM_FESTIVAL_2026](../sources/higgsfield/prompts/MARY_MICKAEL_BRIDEWOOD_AI_FILM_FESTIVAL_2026/) | — | 64 | 6/0 | default×12、seedance_2_0_fast×3、seedance_2_0×3 | — |
| [QUEEN_NOIR](../sources/higgsfield/prompts/QUEEN_NOIR/) | — | 64 | 0/0 | default×32、video_extension×16、videotape-alpha×13 | — |
| [SHE_NEVER_LEFT](../sources/higgsfield/prompts/SHE_NEVER_LEFT/) | — | 63 | 0/0 | default×21、videotape-alpha×6 | — |
| [GIRLS_DEMONS](../sources/higgsfield/prompts/GIRLS_DEMONS/) | — | 62 | 51/11 | seedance_2_0×25、soul_cinematic×14、cinematic_studio_video_4_0×9 | [docs](../sources/higgsfield/projects/GIRLS_DEMONS/) |
| [LEADVILLE](../sources/higgsfield/prompts/LEADVILLE/) | — | 62 | 0/0 | default×35、elevenlabs×19 | — |
| [POWER](../sources/higgsfield/prompts/POWER/) | — | 61 | 0/0 | default×37 | — |
| [THE_THREAD](../sources/higgsfield/prompts/THE_THREAD/) | — | 60 | 0/0 | default×5、videotape-alpha×1 | — |
| [BURNING_TOWN](../sources/higgsfield/prompts/BURNING_TOWN/) | — | 59 | 0/0 | default×37 | — |
| [SEEDANCE_2_0_4K_SHOWCASE](../sources/higgsfield/prompts/SEEDANCE_2_0_4K_SHOWCASE/) | — | 56 | 56/0 | seedance_2_0×56 | — |
| [THE_LAST_TRANSMISSION](../sources/higgsfield/prompts/THE_LAST_TRANSMISSION/) | — | 56 | 0/0 | default×48、video_edit×8 | — |
| [TO_LIVE_ANOTHER_MORNING](../sources/higgsfield/prompts/TO_LIVE_ANOTHER_MORNING/) | — | 56 | 0/0 | default×30、videotape-alpha×3 | — |
| [THE_END_TO_THE_BEGINNING](../sources/higgsfield/prompts/THE_END_TO_THE_BEGINNING/) | — | 53 | 0/0 | default×21 | — |
| [THE_WRONG_GURDIAN](../sources/higgsfield/prompts/THE_WRONG_GURDIAN/) | — | 53 | 0/0 | default×42 | — |
| [WORTH](../sources/higgsfield/prompts/WORTH/) | — | 53 | 0/0 | video_edit×43、default×2、videotape-alpha×1 | — |
| [RAYEN](../sources/higgsfield/prompts/RAYEN/) | — | 52 | 0/0 | default×26 | — |
| [THE_ZERO_SLASHER](../sources/higgsfield/prompts/THE_ZERO_SLASHER/) | — | 52 | 0/0 | default×27、video_extension×4、video_edit×2 | — |
| [SUNSHINE_V2_6_56](../sources/higgsfield/prompts/SUNSHINE_V2_6_56/) | — | 49 | 0/0 | 未标注 | — |
| [OCEAN](../sources/higgsfield/prompts/OCEAN/) | — | 48 | 2/0 | default×44、seedance_2_0×2 | — |
| [THE_LITTLE_WILD](../sources/higgsfield/prompts/THE_LITTLE_WILD/) | — | 47 | 0/0 | default×29、video_extension×7 | — |
| [INSIDE_AI_COMMERCIAL](../sources/higgsfield/prompts/INSIDE_AI_COMMERCIAL/) | — | 46 | 0/0 | default×36 | — |
| [CTRL_HOLD_MV](../sources/higgsfield/prompts/CTRL_HOLD_MV/) | — | 45 | 29/16 | seedance_2_5×29、seedream_v5_pro×15、nano_banana_2×1 | [docs](../sources/higgsfield/projects/CTRL_HOLD_MV/) |
| [HIGGSFIELD_ACADEMY_ASKAR](../sources/higgsfield/prompts/HIGGSFIELD_ACADEMY_ASKAR/) | — | 42 | 32/0 | seedance_2_0×32 | — |
| [HIGGSFIELD_ACADEMY_PROJECT](../sources/higgsfield/prompts/HIGGSFIELD_ACADEMY_PROJECT/) | 教学演示项目 | 42 | 35/7 | seedance_2_0×32、text2image_soul_v2×4、nano_banana_2×3 | [docs](../sources/higgsfield/projects/HIGGSFIELD_ACADEMY_PROJECT/) |
| [THE_COMPANION](../sources/higgsfield/prompts/THE_COMPANION/) | — | 40 | 27/13 | seedance_2_5×27、nano_banana_2×7、gpt_image_2×6 | [docs](../sources/higgsfield/projects/THE_COMPANION/) |
| [BEYOND_THE_RIFT_A](../sources/higgsfield/prompts/BEYOND_THE_RIFT_A/) | — | 39 | 32/7 | seedance_2_5×32、gpt_image_2×7 | [docs](../sources/higgsfield/projects/BEYOND_THE_RIFT_A/) |
| [ONE_LAST_THREAD](../sources/higgsfield/prompts/ONE_LAST_THREAD/) | — | 38 | 0/0 | default×21、videotape-alpha×17 | — |
| [PLANET_47](../sources/higgsfield/prompts/PLANET_47/) | — | 38 | 0/0 | default×37 | — |
| [EMBERDANT_SEASON_1_PART_1_TRAILER](../sources/higgsfield/prompts/EMBERDANT_SEASON_1_PART_1_TRAILER/) | — | 37 | 8/0 | default×21、seedance_2_0×8、videotape-alpha×7 | — |
| [SEEDANCE_2_5_DONUT_COMMERCIAL](../sources/higgsfield/prompts/SEEDANCE_2_5_DONUT_COMMERCIAL/) | — | 35 | 0/0 | default×5、videotape-alpha×4 | — |
| [TOKYO_DRIFT](../sources/higgsfield/prompts/TOKYO_DRIFT/) | — | 35 | 0/0 | default×27、sunburst×8 | — |
| [CHANDLER_ROLLERBLADE_COMMERCIAL](../sources/higgsfield/prompts/CHANDLER_ROLLERBLADE_COMMERCIAL/) | — | 34 | 14/0 | seedance_2_0×14、videotape-alpha×4 | — |
| [NEXUS_MARK_OF_THE_VEIL_EPISODE_1](../sources/higgsfield/prompts/NEXUS_MARK_OF_THE_VEIL_EPISODE_1/) | — | 32 | 0/0 | default×32 | — |
| [SUNSHINE_V1_6_34_PIXAR_STYLE_AI_SHORT_FILM](../sources/higgsfield/prompts/SUNSHINE_V1_6_34_PIXAR_STYLE_AI_SHORT_FILM/) | — | 31 | 0/0 | 未标注 | — |
| [FULL_PHOTO](../sources/higgsfield/prompts/FULL_PHOTO/) | — | 26 | 0/0 | default×26 | — |
| [GOTHIC_BEACH](../sources/higgsfield/prompts/GOTHIC_BEACH/) | — | 26 | 16/0 | seedance_2_0×16 | — |
| [WHIMSY_BAG](../sources/higgsfield/prompts/WHIMSY_BAG/) | — | 24 | 9/15 | seedance_2_5×9、nano_banana_2×8、text2image_soul_v2×4 | — |
| [SPACE_CHORES](../sources/higgsfield/prompts/SPACE_CHORES/) | — | 20 | 12/0 | seedance_2_0×12、videotape-alpha×2 | — |
| [SEEDANCE_2_GLOW_MASK_COMMERCIAL](../sources/higgsfield/prompts/SEEDANCE_2_GLOW_MASK_COMMERCIAL/) | — | 18 | 10/0 | seedance_2_0×10 | — |
| [SEEDANCE_4K_VS_1080P_PRODUCT_COMMERCIALS](../sources/higgsfield/prompts/SEEDANCE_4K_VS_1080P_PRODUCT_COMMERCIALS/) | — | 17 | 6/0 | videotape-alpha×7、seedance_2_0×6 | — |
| [EMERALD_VANGUARD](../sources/higgsfield/prompts/EMERALD_VANGUARD/) | — | 16 | 9/0 | seedance_2_0×9 | — |
| [TODAY_IS_YOUR_DAY](../sources/higgsfield/prompts/TODAY_IS_YOUR_DAY/) | — | 16 | 5/11 | text2image_soul_v2×8、seedance_2_5×4、seedream_v5_pro×3 | — |
| [EVERYTHING_NICE](../sources/higgsfield/prompts/EVERYTHING_NICE/) | — | 15 | 9/6 | seedance_2_5×7、nano_banana_2×4、seedream_v5_pro×2 | [docs](../sources/higgsfield/projects/EVERYTHING_NICE/) |
| [EVERYTHING_NICE_HAPPENS_WHEN_I_SLEEP](../sources/higgsfield/prompts/EVERYTHING_NICE_HAPPENS_WHEN_I_SLEEP/) | — | 15 | 0/0 | default×6、video_extension×2 | — |
| [THE_CABAL](../sources/higgsfield/prompts/THE_CABAL/) | — | 15 | 0/0 | default×11 | — |
| [SEEDANCE_2_FRAGRANCE_COMMERCIAL](../sources/higgsfield/prompts/SEEDANCE_2_FRAGRANCE_COMMERCIAL/) | — | 14 | 7/0 | seedance_2_0×7、videotape-alpha×4 | — |
| [STRAWBERRY_SUMMER](../sources/higgsfield/prompts/STRAWBERRY_SUMMER/) | — | 13 | 6/7 | seedance_2_0×6、text2image_soul_v2×5、seedream_v5_pro×2 | [docs](../sources/higgsfield/projects/STRAWBERRY_SUMMER/) |
| [DRY_AGED_DREAMS](../sources/higgsfield/prompts/DRY_AGED_DREAMS/) | — | 11 | 0/0 | default×10 | — |
| [CALM_DOWN_X_KAYE_CREATIVES](../sources/higgsfield/prompts/CALM_DOWN_X_KAYE_CREATIVES/) | — | 10 | 0/0 | default×8 | — |
| [ESPACIO_VERDE](../sources/higgsfield/prompts/ESPACIO_VERDE/) | — | 8 | 0/0 | 未标注 | — |
| [LOL](../sources/higgsfield/prompts/LOL/) | — | 8 | 0/0 | 未标注 | — |
| [LOST_IN_SPACE](../sources/higgsfield/prompts/LOST_IN_SPACE/) | — | 8 | 0/0 | 未标注 | — |
| [MIRA_AND_THE_DRAGON](../sources/higgsfield/prompts/MIRA_AND_THE_DRAGON/) | — | 8 | 0/0 | default×4、sunburst×1 | — |
| [BBAL_PLAYER](../sources/higgsfield/prompts/BBAL_PLAYER/) | — | 7 | 0/0 | 未标注 | — |
| [POU](../sources/higgsfield/prompts/POU/) | — | 7 | 0/0 | 未标注 | — |
| [SERZHAN_CHE_TAM](../sources/higgsfield/prompts/SERZHAN_CHE_TAM/) | — | 6 | 0/0 | 未标注 | — |
| [CUBO](../sources/higgsfield/prompts/CUBO/) | — | 5 | 0/0 | 未标注 | — |
| [A_PRO_LEVEL_NOOB_ORIGNAL_THE_VOID](../sources/higgsfield/prompts/A_PRO_LEVEL_NOOB_ORIGNAL_THE_VOID/) | — | 4 | 0/0 | default×4 | — |
| [BBBALL](../sources/higgsfield/prompts/BBBALL/) | — | 4 | 0/0 | 未标注 | — |
| [GJENSKINN](../sources/higgsfield/prompts/GJENSKINN/) | — | 4 | 0/0 | default×4 | — |
| [FFFFFFFFF](../sources/higgsfield/prompts/FFFFFFFFF/) | — | 3 | 0/0 | 未标注 | — |
| [CV](../sources/higgsfield/prompts/CV/) | — | 1 | 0/0 | 未标注 | — |
| [HOTLINE](../sources/higgsfield/prompts/HOTLINE/) | — | 1 | 0/0 | default×1 | — |
| [NEW_PROJECT](../sources/higgsfield/prompts/NEW_PROJECT/) | — | 1 | 0/0 | 未标注 | — |

## 分类口径

| cat | 含义 | 条数 |
|---|---|---:|
| `all` | 仅见于全量文件、未归入上述类别 | 136,169 |
| `assets` | 图生视频素材与重跑记录 | 32,087 |
| `scenes` | 分镜 / 镜头 / 场面调度 | 4,109 |
| `props` | 道具设定 | 1,226 |
| `characters` | 角色设定 | 509 |
| `locations` | 场景设定 | 304 |

## 分类覆盖

**注意：不是每个项目都有分类文件。** 很多项目上游只给了一份 `_all_prompts.jsonl`，因此这些项目的全部提示词都落在 `all`。检索前先看本表，确认项目有没有 `scenes` / `characters` 等细分。

| cat | 有该类目的项目数 |
|---|---:|
| `all` | 545 |
| `assets` | 71 |
| `scenes` | 6 |
| `props` | 3 |
| `characters` | 1 |
| `locations` | 1 |

- 只有 `all` 一个类目的项目：**537** 个。
- 带项目文档（brief / README / 官方 Skill）的项目：**79** 个。

## 说明

- 同一项目内按提示词原文 MD5 去重；跨项目不去重（不同项目复用同一句是有效信息）。
- `cat` 取该提示词在分类文件中的最高优先归类：scenes > characters > locations > props > assets > cover > all。
- `type` 由模型名推断，空值表示模型未标注。
- 611 个项目来自本地全量数据包；原 78 项目 GitHub 仓是其子集，已并入，不再单独保留。
- 需要按列筛选时用同目录的 `higgsfield-projects.csv`。
