# ANERNEQ 全量分析（官方 Originals 北极短片 · 20 分钟）【完整版】

> 收割 #1（E127 立 / E135 完整版）｜全量 11,961 资产：生图 2,558（唯一 387）｜视频 9,374（唯一 1,062）｜其他 29
> 模型：seedance_2_5 9,366 (78%)｜soul_cinematic 864｜text2image_soul_v2 716｜seedream_v5_pro 376｜nano_banana_2 261｜gpt_image_2 252
> 迭代率：生图 6.6×，视频 8.8×（同模板反复渲染选优）
> 题材：1920s 楚科奇北极猎手父女，鲸骨巷朝圣。视觉基准《The Revenant》(Iñárritu/Lubezki)。
> 深挖方法：全语料块头频次统计（生图 84 签名类/224 首行族，视频 29 块型）+ 家族最长代表全文精读。

## 一、生图线：Plate Master 体系（七法）

### 1. 场景资产卡先定义后复用 [案例 160×]
> `TUNDRA_DUSK_TO_NIGHT — vast arctic snow tundra at the moment polar evening dies into night... NO moon, the light visibly leaving the world.`
> `FAR_HILLS — a chain of LOW rolling arctic hills far on the horizon, 5-10 km away... NOT towering peaks.`
距离、占比、否定项写进定义，帧内按名引用。

### 2. 光态资产族（同地点多光态变体）[案例 全语料 21 资产卡]
同一冻原按光态立卡：TUNDRA_TRAPLINE_NIGHT×64 / TUNDRA_DUSK_TO_NIGHT×40 / TUNDRA_CLOUDBROKEN_NIGHT×12 / TUNDRA_LAST_SUNSET×8 / TUNDRA_POLAR_EVENING×8 / TUNDRA_BRIGHT_POLAR_NIGHT×8 / TUNDRA_NIGHT_RAYS×4——**地点不变，光态各自成卡**。

### 3. STYLE PREFIX 一行全局锁
> `STYLE PREFIX — SC.1 LOCATION MASTER / SNOW TUNDRA WITH LOW HILLS ON THE HORIZON, DUSK DYING INTO NIGHT — EXTREME WIDE STILL, VERY LOW CAMERA BEHIND A SNOW RIDGE, FOUR DEPTH PLANES — ANAMORPHIC 21:9 "REVENANT", NO PEOPLE, NO ANIMALS, NO TEXT`

### 4. 曝光第一立法 [案例 `EXPOSURE — THE KEY OF THIS FRAME`]
> `The WHOLE frame is dim: the brightest snow anywhere in the image is a muted MID-GREY — NO bright silver crests, NO glowing snow, NO white highlights`

### 5. LOCATION PLATE 空场版 + 方位构图 [案例 32×]
> `LOCATION PLATE — SC.6 / SEA ICE... No people, no animals, no structures, no tracks.`
构图按 `— FAR LEFT` / `— CENTRE` / `— FOREGROUND` 逐方位立法。

### 6. 一棚多格角色表（STRICT CONSISTENCY）[案例 85× gpt_image_2]
> `the SAME real person photographed multiple times in one studio session... do not redesign or alter anything between panels.`
衣妆 copy EXACTLY + 磨损演进叙事（`This is her dead mother's parka, inherited and not her own size. Heavily worn condition... sinew stitching visible`）。

### 7. LANDSCAPE PLATE 一比一复刻 [案例 40×]
> `THIS IS A LANDSCAPE PLATE — REPRODUCE THE ATTACHED FRAME ONE TO ONE... THE COMPOSITION, LEFT TO RIGHT — BUILD IT EXACTLY:`

## 二、生图线补充维度（深挖新增）

### 8. HEX 色值立法
天空直接给十六进制：`a bright overcast sky rendered by that uncorrected stock as DEEP STEEL BLUE, approximately #5E7D95. Matte, cold, absolutely uniform edge to edge — no clouds, no gradient`（见视频线一镜到底模板，生图同源）。

### 9. NEGATIVE 栈分类学（全语料 Top40）
**画质反 AI 族**：watermark×892 / 3d render×766 / over-sharpened×711 / cgi×461 / hdr×550+glow×298 / sky banding×296 / milky blacks×278 / digital clean×292 / ghosting×264 / vignette×303 / high contrast×243
**极夜时刻法**：aurora×597 / moon×577 / sun×409 / daylight×338 / golden hour×315 / sunbeams×297 / sunset×239 / northern lights×258 / dense starfield×260（极夜禁日出日落月光极光！）
**卫生条款**：text×675 / subtitles×585 / captions×507 / on-screen text×344 / people×464 / figures×297 / animals×591 / footprints×475 / trees×283 / buildings×261
**画幅法**：vertical frame×579 / square frame×567 / wrong aspect ratio×256

### 10. 风格 DNA 词频（Top35）
snow×10519 / dark×6110 / light×6029 / blue×6018 / grey×5600 / horizon×5332 / real×4511 / film×4442 / grain×3655 / wind×3624 / bone×3551 / cold×3538 / anamorphic×3261 / stars×3215 / pale×3432 / night×3103——极夜美学四柱：**冷色系+低照度+胶片颗粒+骸骨场景**。

## 三、视频线：块型分类学（全语料 29 块型）

NEGATIVE×10204（近全覆盖，count_blocks.js 口径）/ KEEP THE LOGIC×4850（含 — AND THE RESTRAINT×847）/ VOICES×5144 / FILM LOOK×2810 + **FILM LOOK REPRISE×3636（REPEAT AND OBEY——风格在单条内说两遍）** / CAMERA×3066 + CAMERA — REVENANT HANDHELD×860（TREMBLING×361）/ THE SHOT×3441 / AUDIO — DIEGETIC ONLY×3291 / MULTISHOT×2856 / PHYSICS×1372 / HYPER-REAL CAPTURE×1311 / HARD ANAMORPHIC "REVENANT" LENS (KEY)×1232 / NO SUBTITLES×1064 / ANTI-AI-TELL DIRECTIVE (KEY)×776 / LIGHT — EXPOSED FOR THE DUSK, NOT THE FIRE×758（**曝光以环境为准而非光源**）/ REFERENCE SCOPE (KEY)×656 / SPOKEN LINE×660 / SHOT SIZE×954 / LIVING FACE/EYES (KEY)×559 / SKY — EXACTLY THE WHALE-GRAVEYARD PLATE×552（**天空锚定生图底版**）/ COLOUR AND LIGHT LOCK×466 / 人物名块（FATHER×340/DAUGHTER×311/THE KNIFE×344——**被摄体按剧名立块**）。

## 四、视频线：一镜到底模板全解（家族代表 24,192 字符）

结构（━━━ 分隔线分节）：
1. **时长与剪辑语气立法**：`ONE CONTINUOUS SHOT — NO CUTS, ~40 SECONDS` + `LONG, PATIENT, UNBEARABLE. THE CAMERA REFUSES TO LOOK AWAY AND REFUSES TO HURRY.`
2. **TIME, PLACE AND STOCK**：未校正钨丝片法则——`SHOT ON TUNGSTEN-BALANCED 3200K FILM STOCK IN DAYLIGHT, WITHOUT AN 85 CORRECTION FILTER, AND PRINTED UNCORRECTED. This is the entire reason the image is blue... only the white balance is wrong.`（**把色彩科学的因果讲给模型听**）
3. **HEX 锁**：`DEEP STEEL BLUE, approximately #5E7D95. Matte, cold, absolutely uniform — no gradient`
4. **价值阶梯**：`THE VALUE LADDER, BRIGHTEST TO DARKEST, AND IT NEVER CHANGES: snow → her lit face → sky → fur → bone. THE SNOW IS THE BRIGHTEST THING IN THE FRAME. THE SKY IS CLEARLY DARKER THAN THE SNOW.`
5. **RGB 通道法则**：`THE BLUE CHANNEL IS THE STRONGEST AND THE RED CHANNEL THE WEAKEST IN EVERY PART OF THE IMAGE WITHOUT EXCEPTION, INCLUDING HER SKIN.`
6. **BLOCKING — THE PHYSICAL TRUTH**：身体力学逐手立法——`SHE TURNS HIS HEAD FOR HIM: her left hand cups his jaw and rotates his face gently away... This is the only place she can use, and the whole geometry of the shot follows from it.`
7. **FRAMING 锁**：`HER FACE, LOCKED, NEVER WIDENS, NEVER TILTS DOWN` + 焦外安排（his head SOFT AND OUT OF FOCUS）
8. **克制立法**：`SHE NEVER STRIKES. No blow, no wind-up... she drives it in SLOWLY — one single continuous descent of her locked arm and sinking body, four to five seconds long, unbroken`

## 五、可复用方法 → K 页生长（已完成）

K09 七法 + K01（双层否定/全局头复用/价值阶梯/RGB 通道法则/一镜时长与剪辑语气立法）+ K03（资产卡/光态资产族/LOCATION PLATE/曝光立法）+ K06（一棚多格）——见各页 2026-11-03 增补节。


> **作废令注（2026-11-04）**：本笔记中"→ K 页生长"段落所引用的 K01-K08 页面已全部作废（见 _legacy_作废/）。笔记中的 verbatim 原文提取与模式发现**继续有效**（来自原文），仅 K 页路由目标已失效。重建时以本笔记 verbatim 为源素材重新入页。


---

## 十一、逐字阅读批注（第一批 60 条 / 1,447 条 · 2026-11-04）

### 新发现 1：俄语编辑指令体系 [案例 15 条]

编辑工作流全部用**俄语短句**（14-50 字符）直接操作 nano_banana_2 / seedream_v4_5 / seedance_2_5：
- удали девушку（移除女孩）
- удали свет огня（移除火光）
- сделай еще реалистичнее（更写实）
- сделай текстуру как на футаже 2（材质像镜头 2）
- в футаж 1 добавь больше костей как в футаже 2（镜头 1 加更多骨头像镜头 2）
- пусть в видео инпуте небо будет таким же светом и цветом что и в фотоинпуте（让视频输入的天空与照片输入同色）

**指令极短（<50 字符）但精确**——跨模型（nano_banana_2/gpt_image_2/seedance_2_5/seedream_v4_5）统一用俄语，非英语工作流确认。

### 新发现 2：物件选优迭代模式 [案例 原始绳索 ×5+]

同一物件（rawhide rope）生成 5+ 个略有差异的版本（text2image_soul_v2），每次微调构图/光照/背景角度——**物件的模型选优通过迭代完成**。与 ANERNEQ 8.8× 总迭代率一致。

### 新发现 3：编辑后 NEGATIVE 栈 [案例 4×]
编辑提示词有独立的 NEGATIVE 列表（不同于生成提示词的全局 NEGATIVE 栈）：
> NEGATIVE: bright red blood, scarlet, pouring, dripping streams, splatter, gore, pool of blood, glossy paint look, ketchup, blood on background, changed lighting, changed background, text, watermark.

编辑模式的 NEGATIVE 聚焦于**编辑结果可能出现的错误**（如血太红/太亮/太多），而非全局风格排除。

### 新发现 4：HEX 数组 [案例 1×]
> HEX VALUES: ["#0a0d0e", "#131b20", "#0d1113", "#161f25", "#0f171b", "#1b252b", "#212c34", "#2a353d"]

8 个 hex 色值作为数组列出（非单个）——夜scene全色调色板锁定。

### 新发现 5：物理状态变化编辑 [案例 1×]
> The ONLY change: the trap is now SPRUNG / CLOSED — the two toothed semicircular jaws have snapped SHUT...

机械状态变化（捕兽夹从张开→闭合）通过**前后状态对比编辑**实现。

### 新发现 6：物件摄影棚风格 [案例 12×]
物件特写（bone amulet / rawhide rope / hunting knife / snowshoes）使用**产品摄影棚风格**：isolated on a neutral gray background + soft diffused lighting + product catalog mood。场景镜头则用 65mm anamorphic film still。两种风格泾渭分明。

### 新发现 7：火场多版本 [案例 3×]
burning yaranga 场景生成 3+ 版本（text2image_soul_v2），每版角度/烟雾/火光细节不同——场景选优同物件选优一样通过迭代完成。


---

## 十二、全量结构分析（1,447 条唯一提示词 100% 覆盖 · 2026-11-04）

### 光线分布
fire_present 51% / none 21% / dawn 16% / dusk 9% / 其余 5%——**一半以上在火光附近，符合极夜叙事**

### 相机运动分布
handheld 47% / static 30% / orbit 11% / pan 11%——**手持为主（Revenant 风格），static 用于角色表和场景版**

### 场景主题分布
whale_bone_alley 33% / yaranga 19% / tundra 14% / cave 8% / snow 8% / props 6% / sea_ice 5% / unknown 7%——**鲸骨巷是核心场景**

### 块频 Top15（全部 1,447 条中的出现次数）
FILM LOOK×406 (28%) / NEGATIVE×371 (26%) / CAMERA×303 (21%) / VOICES×231 (16%) / THE SHOT×226 (16%) / NO SUBTITLES×206 (14%) / STYLE PREFIX×192 (13%) / TAGS CAST & ASSETS×187 (13%) / MULTISHOT×155 (11%) / COMPOSITION×148 (10%) / LIGHT×140 (10%) / AUDIO DIEGETIC ONLY×111 (8%) / KEEP THE LOGIC×99 (7%) / FILM LOOK REVENANT NIGHT HIGH×96 (7%) / LIGHT EXPOSED FOR DUSK×55 (4%)

### 全量分析结论
ANERNEQ 的 1,447 条唯一提示词构成一个完整的**极夜叙事系统**：光线以火光为主（51%）、相机以手持为主（47%）、场景以鲸骨巷为核心（33%）。FILM LOOK 块在 28% 的提示词中出现，NEGATIVE 在 26%——这意味着约 1/4 到 1/3 的提示词有正式的风格/否定立法块，其余用散文内嵌约束。全量数据存 tmp_batch3_out/_anerneq_all_analysis.json。


---

## 十三、中篇逐字批注（1000-3000c · 275 条中的前 20 条 · 2026-11-04）

### 新发现 8：DO NOT START FROM THE ATTACHED FRAME [案例]
> DO NOT START FROM THE ATTACHED FRAME. Any reference image is for the characters and the location only — do not use it as the first frame, do not reproduce its composition or its camera position. Build a new, closer angle.

**参考图用途反向约束**——显式禁止模型把参考图当首帧。参考图管角色/场地，不管构图。

### 新发现 9：鲸骨坟场迭代 ×8 [案例]
同一鲸骨坟场场景生成 8+ 变体（text2image_soul_v2），每版微调：相机高度（膝高/地面）、前景物件（弯曲骨/立柱骨）、雾密度、雪花覆盖量。**场景级选优迭代确认。**

### 新发现 10：REFERENCE USAGE 块 [案例 Seedance 2.5 专用]
> REFERENCE USAGE (Seedance 2.5): the ATTACHED FRAME <<<image_1>>> is the FRAMING AND LIGHT REFERENCE — match it: LOW ANGLE... 

**Seedance 2.5 的参考分工声明独立块**——逐个声明每个参考图的用途（FRAMING AND LIGHT REFERENCE / identity / keyframe）。

### 新发现 11：KEYFRAME 起帧法 [案例]
> the attached still <<<image_2>>> IS THE KEYFRAME — the shot STARTS from this exact frame

图生视频以**精确帧**为起点（非风格参考而是起点帧）。

### 新发现 12：LINKED LOCATION ASSET [案例 12×]
> LOCATION ASSET — INSIDE THE BURNT YARANGA <<<image_1>>>, THE MORNING AFTER. This is the INTERIOR of the dead collapsed dwelling from the camp exterior asset <<<80d01cde-...>>> — same world, same hour, same weather.

内景版本通过 UUID 链接外景版本——跨资产一致性声明（same world, same hour, same weather）。


---

## 十四、全量七维提取（1,447 条 100% 覆盖 · 2026-11-04）

### 方法短语频次（全部 1,447 条）
FILM LOOK×763 (53%) / REFERENCE USAGE×359 (25%) / STYLE PREFIX×265 (18%) / keyframe+KEYFRAME×310 (21%) / MATCH THE×67 / location asset×26 / blockout×24 / HEX×9 / VALUE LADDER×9 / BLUE CHANNEL×9 / RED CHANNEL×9 / Do NOT start×14 / 3D PREVISUALIZATION×5 / TEXTURE PASS×2 / Keep everything identical×1

### 主题关键词频次（全部 1,447 条）
fire×1095 (76%) / snow×1088 (75%) / bone×867 (60%) / camp×521 (36%) / sled×519 (36%) / whale×360 (25%) / yaranga×311 (21%) / bear×222 (15%) / tundra×217 (15%) / trap×189 (13%) / drum×182 (13%) / shaman×176 (12%) / hunting×124 (9%) / cave×119 (8%) / frostbite×92 (6%) / fox×92 (6%)

### 全量分析结论
ANERNEQ 的 1,447 条唯一提示词构成一个完整的极夜叙事系统：
- **FILM LOOK 是第一支柱**：53% 的提示词有正式胶片语言立法块
- **REFERENCE USAGE 是第二支柱**：25% 有参考分工声明
- **keyframe 是第三支柱**：21% 是图生视频（以帧为起点）
- **STYLE PREFIX 是第四支柱**：18% 有项目级风格前缀
- 四大支柱互相配合：STYLE PREFIX 定全局调 → FILM LOOK 定光线 → REFERENCE USAGE 定分工 → keyframe 定起点

### 叙事词汇分布
fire 76% + snow 75% + bone 60% = **极夜+骸骨+火光三元素**是全部提示词的视觉基底。camp/sled 是流动场景的两根轴。whale 25% + yaranga 21% 是两大地标。bear 15% + trap 13% + drum 13% + shaman 12% 是叙事节拍器。

**数据存盘**：tmp_batch3_out/_anerneq_findings.json（1,447 条 × 7 维度）+ tmp_batch3_out/_anerneq_all_analysis.json
