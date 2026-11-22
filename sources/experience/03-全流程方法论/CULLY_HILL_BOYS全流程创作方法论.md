# CULLY HILL BOYS 全流程创作方法论（深度教学版）

> **依据**：对 Higgsfield 官方 114 分钟长片 CULLY HILL BOYS（全平台最大项目：473,600 资产、137 场戏、4 幕）的分层抽样完整逆向——PRE PROD 前期制作**全量** 34,379 条 + 四幕代表样本 + Regenerations，合计 37,340 个 job、37,277 条提示词、3,174 条唯一文本，逐类精读。
> 本文档是**教学手册**：每个体系都配官方原文片段 → 逐句拆解 → 可直接套用的模板 → 常见错误。写作 AI 可直接按此操作。

---

## 〇、项目画像与规模认知

**故事**：三个伦敦下层说唱少年（Cal、Ollie 等 "Ninety-five crew"）想出名，意外卷入毒品战争。快节奏、搞笑、节拍驱动的犯罪片——忠诚、友谊、拒绝隐形。1995 校园天才是开场的时代锚点，主线在 2011 年东南伦敦。

**规模感受**（这决定了它方法论的独特性）：
- 473,600 资产 = 前六个项目总和的 **30 倍**；473,214 次生成；114 分钟
- 结构：`PRE PROD`（74 夹，前期制作**独立成区**）→ `1 ACT (1-49)` → `2 ACT (50-93)` → `3 ACT (93-120)` → `4 ACT_Epilogue (121-137)` → `0 Regenerations`
- 每场戏（scene）文件夹内再分 shot 级、生成记录级（1053 夹总共）
- 时间线 2026-06-09 ~ 08（**54 天做完 114 分钟**），日均 8800 次生成——这是"剧集速度做电影"
- **角色阵容庞大**：主角团 + SIDE CHAR（配角系列）+ prostitutes + doberman + 大量群演，每个有独立资产

**为什么值得学**：它是七体系里唯一展示了——①前期制作的完整工程（角色测试、服装版本、道具转盘、场景锚点）；②音乐与画面的互锁（歌词即时间轴）；③真实电影摄制语法被逐条翻译成提示词（180° 轴线、视场角、镜头失误都写进去）。

---

## 〇.5、整体画面风格（一眼认出这部片的视觉 DNA）

> 每个项目都有一种"从第一帧到最后一帧统一"的画面感觉。CHB 的画面风格定义如下——所有提示词的风格段都从这个 DNA 派生。

### 看片感受（一句话）

**阴冷潮湿的伦敦秋天，一部用 ARRI Alexa 拍的"华丽脏乱"犯罪音乐片**：华美的摄影机对着粗野主义的混凝土公寓楼和油腻的路边小店，冷青绿的世界里点缀着酒红色校服与金色武器刻花，1995 年的 DV 回忆段落像翻旧录像带。

### 视觉 DNA 六要素（数据实锚，词频来自 3,174 条唯一提示词）

| 要素 | 定义 | 数据证据 | 写提示词时怎么落 |
|---|---|---|---|
| **底片** | ARRI Alexa + 老式球面定焦 + 轻微变形宽银幕 | Alexa ×971、vintage spherical primes ×611、anamorphic ×919 | `ARRI Alexa, vintage spherical primes, subtle anamorphic, widescreen`——设备三件套每场都写 |
| **时代** | 2011 秋天的南伦敦（主线）+ 1995（校园回忆） | `2011` ×1000、`autumn 2011` ×20、`1995` ×86、`South-East London` ×55、`no modern tech` 明令 | 时代词+地名词+科技禁令三件套：`late-September 2011 SE London, no modern tech` |
| **色彩** | **冷青绿为主 + 酒红/金色作强调**的 60:30:10 | teal ×639、maroon ×405、gold ×700、blue ×1097；60:30:10 配比 ×823 | `60% teal-green tile and chairs / 30% maroon blazers / 10% white jacket + warm skin`——每档绑定具体物体 |
| **光线** | 自然光+现场光源派：荧光灯管、钠灯、逆光剪影、薄雾 | fluorescent ×378、sodium ×234、contre-jour（逆光）、haze ×701、overcast ×195 | `Natural light only — contre-jour backlight, camera on shadow side, atmospheric haze throughout`；或市场场景 `the fluorescent strip supplies the dominant cold ambient, the single caged bulb supplies the only small warm accent` |
| **质感** | 皮肤毛孔级哑光、金属真实反光、湿混凝土 | Pore-level ×131、MATTE skin 变体 ×7、no grain ×589 vs grain ×1385（DV段落才有颗粒） | `Skin: pore-level realism, vellus hair, asymmetric moles, capillary flush` / 正片**无颗粒**、**只有 1995 DV 段才有 interlaced consumer video 颗粒** |
| **运动** | 手持呼吸感 + Ritchie 式暴力剪辑（crash-zoom/定格） | handheld ×950、crash-zoom ×193、freeze-frame ×68、Guy Ritchie ×313 | 手持是默认运动；高潮时刻切换 `low glide → crash-zoom + freeze → top-down snap-cuts` |

### 画面风格的三个"世界"（同片三调）

CHB 的巧妙在于**一部片里有三种画面质感**，各管一段：

1. **正片世界（2011 主线）**：ARRI Alexa 球面定焦的"干净冷调写实"——`Low warm-tungsten grade against deep green, blacks rich but not crushed. Clean and sharp, no grain`。深绿墙壁（The Lamp 酒吧）、冷钢蓝市场、薄雾逆光——**华丽但阴冷**。
2. **反派世界**：`Photoreal predatory nocturnal grandeur — new money: lacquered-perfect, everything matching and a touch too perfect, grotesque opulence`（漆光完美、处处刻意、俗艳的奢华）vs 老钱 `cold working market`——**用"过分干净"表现危险**。
3. **1995 回忆世界**：DV 摄录机质感全套（camcorder ×133、VHS ×51）——`60 FPS output carrying the visible field-motion character of interlaced consumer video` + 儿童手持抖动 + 失焦两秒 + 自动曝光过曝——**载体缺陷即怀旧**。

**写法示范**（把"画面感觉"翻译成提示词风格段的思路）：
- 感觉"伦敦秋天阴冷潮湿"→ `overcast, wet concrete, damp realism, atmospheric haze 12–15%`
- 感觉"底层但堂皇"→ `Guy Ritchie punchy — high contrast, saturated teal-vs-maroon clash, crushed mids, NOT flat`
- 感觉"皮肤真实不网红"→ `MATTE skin with true texture — no shine, no gloss, no dewy highlight, natural warm brown tones`

### 风格判词（这个片子的"气质词表"）

官方风格句里的情绪判词（可直接借用造句）：`deadpan, mundane menace, dry melancholy`（冷面、平庸的威胁、干涩忧郁）、`indifferent, exact, lethal`（冷漠、精确、致命）、`grotesque opulence`（怪诞的富丽）、`lived-in surfaces`（住过人的旧感）、`HUMILIATION-AS-CORONATION`（羞辱即加冕——主题级判词）。**风格句的结尾允许甚至应该写判词**——这是机器最难自发产生、最需要人写的部分。

---

## 一、人物提示词：从"长相"进化到"表演工程"

### 1.1 角色测试（Character Test）——PRE PROD 的核心工序

PRE PROD/Character Test 文件夹 611 条，每条是一次**完整的表演测试**（不是静态角色表）。官方原文（9,195 字样例，老年俱乐部老板）：

```text
SCENE CONTEXT
An elderly, immaculately dressed English club owner crosses an empty Victorian
fish market hall door to door at cold dawn, delivering an old-fashioned
theatrical monologue aloud to the empty stalls with flamboyant, grandiose
gestures — one unbroken take, the camera traveling with him in constant
medium framing and swinging around him mid-hall to follow from behind.

ACTIVE REFERENCES
<<<1bd3e51f...>>> — British male, late 60s, gaunt severe face, deep-set pale
eyes, grey hair swept back, dark navy pinstripe double-breasted three-piece
suit, white shirt, deep burgundy tie, tan leather oxford shoes. Upright
unhurried regal carriage, slow feet, still head, enormous expansive arm
gestures.
OBJECTIVE: to crown himself before an imaginary audience — make the empty
hall applaud.
TACTIC (beat 1): proclaim. (beat 2): seduce the stalls like a crowd.
(beat 3): weigh the words privately. (beat 4): defy an invisible enemy.
(beat 5): release — let the verdict hang in the echo.
SUBTEXT: a dangerous man amusing himself; the performance is a display of
total ownership of this place.
STATUS: high — the gestures are huge but the gait and head never hurry.
FACS: AU1+AU2 theatrical brow lift on the opening line; AU4 bilateral —
brows pulled down and together on "patience is a coin"; AU12 unilateral —
slow one-sided smile as the final verdict lands.
100% matches the reference.
```

**逐句拆解**——这段就是全工作区最先进的"表演提示词工程"：

| 段 | 作用 | 翻译成拍摄现场的话 |
|---|---|---|
| 外观（REFERENCE 行内） | 身份锁定 | 服装/体态/动作气质（`Upright unhurried regal carriage, slow feet, still head, enormous expansive arm gestures`——四短语立起"帝王派头"） |
| **OBJECTIVE** | 这场戏的目标 | 导演讲戏："给自己加冕，让空大厅鼓掌" |
| **TACTIC (beat 1-5)** | 分拍战术 | 每拍一个动作动词：proclaim → seduce → weigh → defy → release——**表演被拆成节拍** |
| **SUBTEXT** | 潜台词 | "危险的人在自娱，表演是对此地绝对所有权的展示" |
| **STATUS** | 权力姿态 | "高位——手势巨大但步态和头从不匆忙"（高 status 的表演法：越大越慢） |
| **FACS (AU 编码)** | 精确表情 | 用面部动作编码系统指定：AU1+AU2 眉上提、AU4 双眉皱下、AU12 单侧微笑——**表情精确到肌肉单元，且绑定台词**（"patience is a coin" 皱眉、"final verdict" 单侧笑） |

全库 48 条 OBJECTIVE/SUBTEXT、54 条 FACS——这是**表演指导的完整五件套**（目标/战术/潜台词/地位/表情编码），此前六体系都只有"状态词"级别。

### 1.2 声音克隆：精确到赫兹、精确到真人

官方原文（9,270 字样例，主角测试）：

```text
Voice: the speaking voice of Israel Adesanya, the Nigerian–New Zealand UFC
middleweight champion known as "The Last Stylebender" — reproduce his real
interview voice precisely. Male, 36 years old. Medium-high light agile
tenor, median pitch around 175 Hz — noticeably higher and brighter than his
athletic frame suggests — ranging from about 110 Hz on low emphatic drops
up to 300–350 Hz spikes on laughs and excited peaks; clear, sharp and highly
resonant, slightly nasal, forward-placed, completely free of gravel or
roughness.
```

以及**声音参考视频**的绑定写法：
```text
@video1 — voice carrier reference: the audio track of this clip is the exact
voice for the speaking character — match its timbre, pitch placement, accent,
burst phrasing and pause rhythm precisely. Ignore the visual content of
@video1 entirely; it contributes sound only.
```

**方法论**：
1. **声音三选一或全用**：真人名（Israel Adesanya）+ 物理参数（175Hz 中位、110-350Hz 区间）+ 参考视频载体（`@video1` 绑定音轨、`Ignore the visual content`）
2. **"contributes sound only"** 是关键句——防模型把参考视频的**画面**也学进去
3. 参数链完整：`timbre（音色）、pitch placement（音高位置）、accent（口音）、burst phrasing（爆发式断句）、pause rhythm（停顿节奏）`——五个维度全写

### 1.3 服装版本学（Costume Versioning）

PRE PROD/Costumes 下每角色 V1~V8 独立文件夹（327 条服装相关唯一提示词）。俄语原文（服装资产标准写法）：

```text
сделай мне 2 фото на 5D Mark 2 с объективом 85mm этого костюма и обуви на
сером манекене среднего телосложения на сером фоне с мягким освещением.
3 фото: 1- полный рост спереди, 2- полный рост сзади. добавь микродетали в
текстуру ткани и реалистичные легкие следы износа.
```
（译文：用 5D Mark II + 85mm 拍这套服装和鞋：灰背景、中等体型人台、柔光。两张：正面全身、背面全身。加面料微细节和真实的轻度磨损。）

**方法论**：
1. **服装与角色分离**——服装资产用**人台**拍（不占角色额度），角色表演时引用服装资产
2. **真实器材进提示词**（5D Mark II + 85mm）——比"professional photo"有效得多
3. **版本文件夹即修改史**：V1→V8 序列，每版一个文件夹，角色试装全程可回溯
4. 与 DETOUR 的区别：DETOUR 把载具写进角色表；CHB 把**服装**也独立成资产——颗粒度更细

---

## 二、场景提示词：锚点 + 全景投影 + 布局锁

### 2.1 VISUAL ANCHOR（视觉锚点）

场景资产与场景镜头统一用**锚点**钉住识别特征（官方原文）：

```text
LOCATION / FIRST FRAME. UK school canteen: teal-green tiled servery counter,
stainless hot-food station, teal plastic chairs, formica tables, exposed
brick, fluorescent strip lights. 3/4 angle.
VISUAL ANCHOR = the long teal-tiled servery counter with its stainless steel
sneeze-guard rail.
```

每个场景一个 VISUAL ANCHOR 等号句——**镜头再多，锚点物在，场景就在**。

### 2.2 全景图的正确用法（反投影污染）

鱼市大厅样例（9,195 字）里的**全景图声明**是全工作区最详细的：

```text
The reference image is a 360-degree equirectangular panorama: extract from
it only the real hall geometry — long central aisle along a recessed floor
drain channel, whitewashed brick columns, tall brick end wall with a huge
arched iron-framed window glowing dawn-blue, rows of market stalls...
The panoramic projection itself must never appear in the output: no curved
warped lines, no bending verticals, no stretched edges, no fisheye curvature
at any point of the camera's travel. The generated footage is rendered
through a normal rectilinear lens in every frame; all architectural lines
stay straight.
```

**方法论**：用 360° 全景图喂场景时，必须声明"**只提取几何**"+**穷举投影伪影的禁令**（curved lines/bending verticals/stretched edges/fisheye）+ **正面声明渲染方式**（rectilinear lens, architectural lines stay straight）。这是全景资产的标准安全写法。

### 2.3 LOCATION MAP：文字分镜图（RED FLAG 示意图法的纯文本版）

```text
LOCATION MAP
Long market hall with a door at each end. At one end: the open...
```
配合 pub 样例（8,766 字）的**逐物件清单**：
```text
Centre-left: ONE curved dark buttoned-leather chesterfield banquette with
ONE round wooden pedestal table in front of it — this single booth is the
ONLY place the three men sit. Dartboard on the dado, framed black-and-white
photos and a wall sconce on the green wall, two warm shaded pendant lamps.
Screen-left: open maroon GENTS door with a glowing white-tiled toilet...
```

**方法论**：方位词（Centre-left / Screen-left）+ 大写数词（ONE/ONLY）——**座位位置也是锁**。这与 RED FLAG 的示意图方案二选一：能画图就画图，画不了就用"方位 + 唯一性大写锁"。

---

## 三、道具提示词：产品级转盘（Props Turnaround）

Vernon's shotgun 样例（3,530 字）——**道具四视图转盘**的标准范本：

```text
Create a four-panel product reference sheet (a "props sheet" turnaround) of
the exact same luxury engraved side-by-side break-action shotgun from the
attached reference image. Keep the gun's identity, proportions, engraving
pattern, materials and finish perfectly identical to the reference in every
panel. Lay it out as a 2x2 grid on one continuous, seamless solid neutral
medium-grey background, hex #808080...

Panel layout:
- Top-left — full left-side profile, medium-wide establishing shot. The
  whole shotgun lies horizontally, buttstock to the left and long blued
  barrels to the right... gilded, finely floral-scroll-engraved action and
  lockplates, deep blued side-by-side barrels with a top rib, ornate gold
  trigger guard with twin triggers...
  The buttstock is wrapped in a distinctive warm chocolate-brown crocodile /
  alligator leather with raised scale segmentation...
- Top-right — extreme close-up macro of the LEFT lockplate. The engraved
  cursive surname "Moody" must appear large, sharp and clearly legible...
  This is the ONLY panel where the name appears.
- Bottom-left — full right-side profile, the opposite (off-side) face...
```

**方法论**：
1. **2×2 网格转盘**：左侧全身 / 左锁板特写 / 右侧全身 / （第四格）细节——**道具也有角色表**
2. **刻字处理**：`the engraved cursive surname "Moody" must appear... This is the ONLY panel where the name appears`——文字只出现一次且指明在哪个 panel（防乱码复制）
3. 背景同角色表（#808080）、身份锁（`perfectly identical to the reference in every panel`）
4. 对比 DETOUR：DETOUR 的 Props 无文字提示词（图生图）；CHB 证明**关键道具值得写完整转盘**——贵重/有剧情意义的道具才这么干（shotgun 是剧情关键），廉价群具仍走图生图

---

## 四、视频提示词：三种结构格式与完整摄制语法

CHB 同时存在**三种结构格式**（按镜头复杂度选用）——这是"按需选格式"的实证：

### 4.1 格式 A：分节符式（REFERENCE → STYLE → LOCK → SHOTS/TIMELINE）

用 `═══════` 分节 + 编号节（141 条分节符、13 条完整四节式）。LOCK BLOCK 官方原文：

```text
3. LOCK BLOCK
SEQUENCE INTENT: Guy Ritchie hero-introduction of Horace — the bold
"badass reveal" treatment ironically applied to a meek giant slopping mash
in a school canteen. Establish the geography and his low status, crown him
with a freeze-frame, then run the machine-rhythm of the job.
THEME = HUMILIATION-AS-CORONATION.
DEFINING GESTURE: the mechanical ladle slap, caught in a freeze-frame.
VOICE MATRIX: none — no dialogue in Part A. Horace silent, deadpan.
COLOR TRAJECTORIES (60-30-10): 60% teal-green tile and chairs / 30% maroon
school blazers in the queue / 10% Horace's white jacket plus cream mash
and warm skin.
Axis (180° rule): camera on the diners' side of the counter; the queue moves
screen-left → screen-right (directions from camera POV). Held across all
internal cuts.
Camera mode: low gliding push → crash-zoom + freeze → top-down snap-cuts.
WB: 4500K cold institutional fluorescent, held identical across all segments.
Atmosphere: faint steam off the hot mash, haze 12–15%.
Grade: Guy Ritchie punchy — high contrast, saturated teal-vs-maroon clash,
crushed mids, NOT flat.
PHYSICS LAWS: trays slide with momentum and stop with friction; the ladle
has real weight and slaps mash with a viscous wet splat; steam rises as a
real gas...
```

**逐句拆解 LOCK BLOCK**——这是"一场戏的导演阐述"被结构化：
- **SEQUENCE INTENT + THEME**：这场戏的意图与主题（"羞辱即加冕"——irony 写进提示词）
- **DEFINING GESTURE**：这场戏的记忆点动作（机械感的汤勺拍击，定格呈现）
- **VOICE MATRIX**：这场戏的声音矩阵（无对白则明说 none）
- **COLOR TRAJECTORIES (60-30-10)**：色彩轨迹按 60/30/10 展开，且**每个百分比绑定具体物体**
- **Axis (180° rule)**：轴线规则进提示词！`camera on the diners' side; queue moves screen-left → screen-right; held across all internal cuts`——**越轴问题的根治方案**
- **WB 精确色温**：4500K + `held identical across all segments`
- **Atmosphere 量化**：`haze 12–15%`
- **PHYSICS LAWS**：物理律逐条（托盘滑动摩擦、汤勺真实重量+粘稠湿拍击、蒸汽是真实气体）

### 4.2 格式 B：SHOTS/TIMELINE 时间轴（单生成内多镜头）

```text
4. SHOTS / TIMELINE (single 15s generation, internal cuts)

[0:00–0:05] ЗАЯВОЧНЫЙ ESTABLISH — low gliding push down the queue, 84°
SUBJECT: ...
ACTION: A fast Guy Ritchie low glide pushes at 1.2 m/s down the tray-line
on the diners' side, maroon sleeves and trays whipping past the close
foreground left and right, the teal-tiled counter unspooling, arriving on
the servery where Horace stands caged behind the station, deadpan, ladle
in hand.
CAMERA: LENS LOCK 84° wide. NOT 63°, NOT 107°. Handheld low glide at
counter-edge height, operator on diners' side / shadow side, axis straight
down the queue, trays hypertrophied in the near foreground (snake-cam).
STYLE: Ritchie punchy, WB 4500K; teal vs maroon; haze 12%.
CONSTRAINTS: ... match input 100%; hold 84°; geography reads; no fade.
LENS CHECK: 84° held.

[CUT — match on arrival | motivation: crash into the subject]
```

**逐句拆解**：
- 每个镜头块五个字段：SUBJECT / ACTION / CAMERA / STYLE / CONSTRAINTS——**块内自包含**
- **LENS LOCK 84° wide. NOT 63°, NOT 107°**——视场角精确锁 + **错误值点名排除**（全库 135 条 LENS LOCK）：比"wide shot"精确 100 倍
- **运镜速度量化**：`pushes at 1.2 m/s`——速度写数字
- **[CUT — match on arrival | motivation: crash into the subject]**——**剪辑点带动机注释**：什么匹配（arrival）+ 为什么剪（撞进主体）

### 4.3 格式 C：歌词互锁式（音乐片核心）

title scene 36,599 字样例——音乐片提示词的天花板：

```text
LYRICS: "the opening chorus, UNISON on both mouths: 'BOUNCE! BOUNCE!
Ninety-five crew! / BOUNCE! BOUNCE! What you gonna do?! / Drop the
backpack! Smash it to the ground! / Six graders running this London town!'
— the REAL BACKPACK DROP lives in this part, exactly on its own words."

Use the song from the given video and the characters from the given images:
two schoolkids perform at their 1995 school talent show, captured in ONE
CONTINUOUS TAKE by an amateur camcorder HELD IN THE HANDS of a sixth-grade
schoolboy PLANTED on one spot of the hall floor.
Both performers shout the exact lyrics in unison, with exact visible lip
sync to the voices from <<<video_1>>>.
```

尾段的对象清单（原文）：
```text
Exactly TWO backpacks exist.
Both come from <<<47be4c46...>>>.
Both begin correctly worn with two attached shoulder straps.
Both remain on the shoulders through the first two chorus lines.
Both come completely off during the actual sounded words "Drop the
backpack!"
Both hit the wooden stage boards on the actual sounded word "Smash."
Both skid approximately one hand-span, settle and remain untouched...
```

**逐句拆解**：
1. **歌词=时间轴**：`the REAL BACKPACK DROP lives in this part, exactly on its own words`——动作**精确落在唱出来的那个词上**（"Drop" 扔包、"Smash" 砸地）
2. **口型双保险**：歌词全文写进提示词 + `<<<video_1>>>` 音轨绑定 + `exact visible lip sync`
3. **镜头载体角色化**：`amateur camcorder HELD IN THE HANDS of a sixth-grade schoolboy PLANTED on one spot`——DV 机在一个站在原地的小学生手里。**镜头的运动缺陷全是表演**
4. **载体缺陷全写**（尾段原文）：`constant young-hand tremor, tired-arm sway... horizon begins 3–5 degrees off level, drifts and receives one wrong-way correction... motor zooms happen in the middle of lyrics and never land cleanly on beats... autofocus remains confused for roughly two seconds...`——**晃动、歪平、失误性变焦、失焦 2 秒**都被逐条指定。要"真实 DV 感"不是写" shaky cam"，是把每种失误写成剧本
5. **数量锁**：`Exactly TWO backpacks exist / Every person and object exists exactly once / The same face never appears twice in one frame`——数量、唯一性、防复制脸，三层防错

### 4.4 电影语法统计（可直接抄的词汇表）

| 语法 | 出现 | 用法示例 |
|---|---|---|
| Guy Ritchie 风格引用 | 313 | `Grade: Guy Ritchie punchy — high contrast, crushed mids` |
| crash-zoom | 193 | `low gliding push → crash-zoom + freeze` |
| freeze-frame | 68 | `crown him with a freeze-frame`（Ritchie 式定格出场） |
| 180° 轴线 | 307 | `axis (180° rule): camera on diners' side... held across all cuts` |
| LENS LOCK 视场角 | 135 | `LENS LOCK 84° wide. NOT 63°, NOT 107°` |
| camcorder 质感 | 133 | `60 FPS output carrying interlaced consumer video field-motion` |
| 口音指定 | 1147 | `dialogue in working-class British (Essex) accent` |

---

## 五、风格系统：三层结构（STYLE 段 + mini 前缀 + 60:30:10）

### 5.1 标准 STYLE 段（214 种变体——每场戏一个）

官方样例（每条都是完整可复用模板）：
```text
Style: 8K IMAX. Photorealistic — no 3D render, no game engine, no
game-cutscene aesthetic.
Cinematography: Emmanuel Lubezki × Roger Deakins.
Lighting: Natural light only — contre-jour backlight, camera on shadow side,
atmospheric haze throughout. Key light from sky and windows only.
Color: 60:30:10 — dominant / secondary / accent.
Camera: Physical cine lens. 180° shutter motion blur.
Skin: Pore-level realism — vellus hair, asymmetric moles, capillary flush,
pore-shadow matching on-set light.
Acting: Hollywood — micro-pauses before reactions, precise eye-line, wet
living eyes with catch-lights, visible breath and chest rise.
Physics: Gravity and inertia respected — mass has real weight, correct
contact shadows. No floating props.
Composition: Rule of thirds + golden ratio. Every person moving from frame one.
Continuity: Characters, props, environment identical across every cut. No
identity drift.
Technical: 24fps smooth motion. 8K detail. No jitter.
Audio: Environmental SFX only. No music. No subtitles.
```

**这是全工作区最完整的单段风格前缀**——把 ZEPHYR 的风格前缀、RED FLAG 的色彩律、KOK BORU 的物理锁、ONEIRIC 的连续性锁**浓缩成 12 行内联段**，每个字段一行。

### 5.2 60:30:10 色彩配比（823 条——RED FLAG 70/20/10 的进化）

RED FLAG 是"主色 + 光晕内允许色"；CHB 进化为**三档百分比 + 物体绑定**：
```text
COLOR TRAJECTORIES (60-30-10): 60% teal-green tile and chairs / 30% maroon
school blazers in the queue / 10% Horace's white jacket plus cream mash and
warm skin.
```
配 atmosphere 量化（`haze 12–15%`）和 WB 精确值（`4500K`）——色彩系统三件套：**配比 + 浓度 + 色温**。

### 5.3 每场一调的风格库（样例三则）

```text
Grounded naturalistic photoreal cinema, late-September 2011 SE London, no
modern tech. ARRI Alexa, vintage spherical primes, subtle anamorphic,
widescreen. Low warm-tungsten grade against deep green, blacks rich but
not crushed.

Photoreal cold post-Soviet realism — deadpan, mundane menace, dry
melancholy, lived-in surfaces, violence delivered plainly and without
glamour. Flat realism over kinetic punch — indifferent, exact, lethal.

Photoreal predatory nocturnal grandeur — new money: lacquered-perfect,
everything matching and a touch too perfect, grotesque opulence.
```
**方法论**：风格句=**质感定语 + 摄影器材 + 调色 + 情绪判词**（"indifferent, exact, lethal"/"grotesque opulence"——风格段允许写判词）。

---

## 六、多语言生产体系（俄 606 + 中 158 + 英 2410）

| 语言 | 用途 | 何时用 |
|---|---|---|
| **俄语** | 资产/服装操作指令 | 母语团队写操作层更准更省 |
| **中文** | 大场面动作调度 | `他贴在混凝土墙角与桥墩后躲避，用一把 AK-47 向特种部队还击，同时面无表情地哼唱俄语歌曲《喀秋莎》；偶尔在枪响时微微眯眼；当他扣动扳机开火时，他唱得更大声` |
| **英语** | 结构标准件（段落标签/风格段/锁） | 全大写段落标签语言 |

中文样例完整展示了中文的强项：**动作链 + 表演细节**（躲→还击→哼唱→眯眼→大声唱）一气呵成。官方用中文写枪战、用俄语写资产、用英文写结构——**按内容类型分工语言**，全库三语零冲突。

---

## 七、七体系对照总表（CHB 定稿后）

| 维度 | DETOUR | ZEPHYR | RED FLAG | KOK BORU | ONEIRIC | ADILIADA | **CHB** |
|---|---|---|---|---|---|---|---|
| 定位 | 独立·街头 | 官方·IMAX | 官方·黑色 | 官方·手绘 | 官方·长片 | 官方·戏仿 | **官方·114min音乐犯罪片** |
| 规模 | 5.5K | 4.8K | 3.5K | 2.7K | 41K | 11.3K | **473K** |
| 人物工程 | 记忆点+元素 | 身份段复用 | 剪影锁定 | 质感定表演 | 状态锁覆盖 | 一人多界变体 | **OBJECTIVE/TACTIC/SUBTEXT/STATUS/FACS 五件套+声音Hz** |
| 场景 | 方位文字 | 附件顺序 | 示意图 | —— | LOCATION MAP+x% | 同源 | **VISUAL ANCHOR+全景反投影+180°轴线** |
| 道具 | 图生图 | JSON产品 | —— | —— | 群演资产化 | 变体资产 | **四视图转盘+刻字单现** |
| 视频结构 | 六段式 | Markdown | MATCH CUT | SHOT+锚点复述 | 八段+GLOBAL LOCK | 八段+戏眼 | **三格式按需+LENS LOCK+歌词互锁** |
| 色彩 | 双世界 | 70/20/10雏形 | 正向分配 | 冷暖双界 | POSITIVE | —— | **60:30:10+物体绑定+WB量化+haze百分比** |
| 语言 | 英 | 英 | 中英 | 英 | 英 | 英 | **俄中英三语分工** |
| 周期 | 22天 | 3天 | 10天 | 45天 | 36天 | 36天 | **54天/114min** |

**七体系终极铁律（最终确认版）**：
1. 风格/约束成段复用，段落标签全大写
2. 一致性 = 元素引用 + `controls`/`100% matches` 控制边界声明
3. 正向形式 > 负面清单，且以 POSITIVE 段收尾
4. 物理/表演/音频逐项显式——CHB 证明表演可精确到 FACS 肌肉单元
5. 语言按内容分工（操作母语/动作中文/结构英文）
6. 一切可量化处写数字：Hz、°、K、%、m/s
7. 音乐片：动作精确落在唱出的词上，口型绑音轨视频
8. 迭代管理：版本文件夹 / regen 实验区 / PRE PROD 独立成区

---

## 八、复用检查清单（CHB 版——音乐犯罪片专用）

**人物**：
- [ ] 表演五件套写了吗（OBJECTIVE/TACTIC 分拍/SUBTEXT/STATUS/FACS 表情编码）？
- [ ] FACS 是否绑定台词（哪句皱眉哪句笑）？
- [ ] 声音：真人名+Hz 参数+参考视频三选一？"contributes sound only" 写了吗？
- [ ] 服装独立资产（人台+器材参数+磨损）+ 版本文件夹？

**场景**：
- [ ] VISUAL ANCHOR 等号句写了吗？
- [ ] 全景图是否声明"只提取几何"+禁投影伪影+rectilinear 渲染？
- [ ] 180° 轴线声明了吗（camera side + movement direction + held across cuts）？
- [ ] 座位/物件唯一性大写锁（ONE/ONLY）？

**道具**：剧情关键道具是否 2×2 转盘（侧/特写/反侧/细节）+ 刻字单现声明？

**视频**：
- [ ] 按复杂度选格式：分节式（导演阐述）/ 时间轴式（多镜）/ 歌词互锁（音乐）？
- [ ] LENS LOCK 视度角 + 点名排除错误值（NOT 63°, NOT 107°）？
- [ ] 运镜速度量化（1.2 m/s）？剪辑点带动机注释？
- [ ] 音乐：歌词全文+动作落词+音轨视频+口型双保险？
- [ ] 载体缺陷是否剧本化（tremor/歪平/失误变焦/失焦秒数）？
- [ ] 数量锁（Exactly TWO / exists exactly once / never twice）？

**风格**：
- [ ] 12 行内联 STYLE 段（Style/Cine/Lighting/Color/Camera/Skin/Acting/Physics/Composition/Continuity/Technical/Audio）？
- [ ] 60:30:10 三档 + 物体绑定 + WB 开尔文 + haze 百分比？
- [ ] 情绪判词允许进风格句（indifferent, exact, lethal）？
