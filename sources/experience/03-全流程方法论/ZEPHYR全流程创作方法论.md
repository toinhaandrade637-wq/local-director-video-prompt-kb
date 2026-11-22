# ZEPHYR: Special 全流程创作方法论

> **依据**：对 Higgsfield 官方团队短片 ZEPHYR: Special（5:07，官方全开源项目）全部 4837 个生成任务、4831 条提示词（471 条唯一文本）的完整逆向。ID 级对账零缺漏。
> 本方法论与 DETOUR（独立团队）形成对照——两个项目代表两种成熟体系，配合阅读收获最大。
> 配套数据包：`02_完整提示词数据包\ZEPHYR\` + `ZEPHYR_项目完整提示词.zip`。

---

## 〇、项目画像：官方团队的工作方式

**故事**：Zephyr 小队队员身陷绝境，一位神秘客座角色（Jasmine）介入，她的机甲战斗造诣超越小队最精英战士的想象。

**角色阵容**：Haru Min（驾驶员）、Reina（狙击手）、Naomi、Jasmine（客座角色）、Mira、Zero + 各自的机甲。每个角色有永久视觉锚点（如 Haru 的"holographic nose strip (permanent)"全息鼻贴）。

**官方 brief 自述的三个关键信息**：
1. Seedance 2.5 + Cinema Studio 场景控制 = "完全的自由"，团队专门规划了多个"**不可能镜头**"并全部实现
2. **倒置角色表技巧**：Naomi 被困机甲倒置的镜头，纯提示词描述物理效果不佳 → **把角色表图像本身倒置**，把物理"烘焙"进输入，提示词反而可以写得更随意（"change the input, not the prompt"）
3. 资产全开源：bloopers/失败镜头与最终剪辑并存

**时间线（6-25 → 6-27 → 6-29 三天完成主体，8-11 补重生成实验）**：
- 6-25：81 条唯一提示词（开搞）
- 6-26：118 条
- 6-27：163 条（峰值，全部主要镜头）
- 6-29：99 条（收尾）
- 8-11：10 条 + regenerations 文件夹 90 条（Seedance 2.5 发布后的重生成实验，34 分钟内密集跑完）

**模型分工**：seedance_2_0 ×3553（主力视频）/ soul_cinematic ×553（道具特写）/ nano_banana_2 ×346 / gpt_image_2 ×250（角色表/包装设计）/ seedance_2_5 ×90（重生成实验）/ text2image_soul_v2 ×41。

**与 DETOUR 的结构差异**：官方项目是**扁平结构**（根直属 4747 + regenerations 90，无分类文件夹）——靠提示词内的 metadata 自组织，而不是靠文件夹分类。

---

### 0.5 整体画面风格（一眼认出 ZEPHYR 的视觉 DNA）

**看片感受**：一部用 IMAX 摄影机拍的机甲"纪录片"——65mm 大画幅的奶油景深、泛着光晕的有机颗粒、纪录片式手持呼吸；阴天柔光下的机库与指挥舱，全息鼻贴闪着暖窗光，巨型机器人带着真实的重量感。

**视觉 DNA 六要素**（词频来自 471 条唯一提示词）：

| 要素 | 定义 | 数据证据 | 提示词落法 |
|---|---|---|---|
| 底片 | 65mm IMAX 大画幅 + 有机颗粒 + halation | 65mm ×202、IMAX ×202、grain ×330、halation ×240 | Style: 8K IMAX, photorealistic. Real organic film grain and halation. Shot on large-format film. High dynamic range |
| 摄影师 | Hoyte van Hoytema 自然主义（Nolan 系御用） | Hoytema ×111 | OPERATING STYLE — HOYTE VAN HOYTEMA: expansive realism with intimate handheld closeness |
| 运动 | 手持 + 纪录片构图 | handheld ×239、documentary ×160 | intimate ultra-handheld closeness, immersive in-camera feel |
| 色彩 | 70/20/10 ACCENT DOCTRINE：绿灰底 + 暖橙强调 + 冷蓝对位 | green ×227、blue ×297、red ×344（机甲红）、overcast ×148 | ~70% desaturated green-grey room tone + ~20% warm orange/yellow accent + ~10% cool daylight-blue counter-note |
| 光线 | 阴天柔光 + 现场光源（暖窗光/舱内面板） | overcast ×148、haze ×200 | source-motivated natural light, single soft key, desaturated rich earthy colour, faithful skin tones |
| 质感 | 毛孔级皮肤 + 全息元素 | pore ×209、holographic ×115（全息鼻贴） | pore-level realism ... half the face often falling into shadow |

**画面气质判词**：纪录片真实 + 大画幅华丽 + 略带动漫喜剧节奏（Room for anime-style comedic timing）——三种气质在同一帧里共存是 ZEPHYR 的独特配方。

---


## 一、ZEPHYR 的提示词格式体系（与 DETOUR 最大的差异点）

### 1.1 双格式系统

**格式 A：Markdown 大纲式**（主力，~400 条）——用于叙事镜头：

```markdown
# ZEPHYR — SEEDANCE 2.0 PROMPT
## SCENE: "Overwatch Lunch" — Reina snipes for Haru · FULL (both notes) · 4 shots · ~14–15s · 4K

**Reference binding (load these):**
`<<<image_1>>>` → **@broken_bridge** (location) · `<<<image_2>>>` → **@Haru_battle** ...

### STYLE PREFIX          ← 一大段风格定义（见 §2）
### SCENE SUMMARY         ← 这场戏一句话
### INSTRUCTION BLOCKS
### ASSETS (this scene)   ← 本场用到的元素清单和身份描述
### SCENE NOTE — "..." (Shots 1–4, ~14s)

## SHOT 1 — INT. CABIN, LOW 3/4 ANGLE (~3.5s; handheld): looking up at Reina...
## SHOT 2 — SIDE VIEW, LENS-DISTORTION ONLY (~4s; NO UI): ...
## SHOT 3 — ...
## SHOT 4 — ...

## NEGATIVE PROMPT (paste into Seedance's negative field if available)
```

**格式 B：JSON 结构式**（50 条，产品/道具特写）——用于包装设计、中控面板等：

```json
{
  "concept": "Front packaging artwork for spicy instant noodles, brand ZEZE...",
  "brand": { "name_latin": "ZEZE", "name_hangul": "제제", "placement": "...", "lettering_style": "..." },
  "illustration_style": { "technique": "...", "shading": "...", "line_quality": "..." },
  ...
}
```

**格式 C：Tags: 头部引用**（45 条）——最简格式，元素绑定：
```
Tags: <<<image_1>>> = Haru Min (pilot) · <<<image_2>>> = Reina (sniper) · ...
GLOBAL STYLE
...
```

### 1.2 SHOT 段的写法（每镜自成一体）

```markdown
## SHOT 2 — SIDE VIEW, LENS-DISTORTION ONLY (~4s; NO UI): Haru LEFT → fast swipe-pan → the bug running at her

**SCENE CONTEXT** A clean cinematic **side shot** on **@broken_bridge** (`<<<image_1>>>`):
**@Haru_battle** (`<<<image_2>>>`) sits on the **LEFT**, eating on her seated rest-mode **@Haru_mecha**.
The only stylistic treatment is a **mild barrel lens distortion**...
**It is a normal full photographic frame — absolutely NO screen, NO visor, NO HUD, NO reticle...**

**ACTIVE REFERENCES** `<<<image_2>>>` (Haru, clean torso, nose strip, red ramen) 100%; ...
```

**要点**：镜头标题行包含 机位+时长+关键约束 三个信息（`INT. CABIN, LOW 3/4 ANGLE (~3.5s; handheld)`）；每个 SHOT 段内重复 SCENE CONTEXT / ACTIVE REFERENCES 小节——**镜头级自包含**，单镜重生成不用带全上下文。

---

### 1.5 Markdown 主力格式的完整拆解（21,781 字标准范本逐段教）

官方在 Overwatch Lunch 场景的提示词是全项目结构最完整的教科书，本方法论在 1.1 已给出格式骨架，这里补 **ZEPHYR 独有的三段锁与负面镜像**（全部官方原文）：

**① REFERENCE HYGIENE（引用卫生段）—— 跨场景资产混用的防火墙**：

每张参考图在不同上下文里该取什么、不该取什么，逐条写明：机舱图只给轮廓和内饰——别把驾驶舱安全带复制到桥上的 Haru 身上；她在舱内系带是对的，在外面就是错的（do NOT copy any cockpit seatbelt harness onto Haru out on the bridge）。

**② WARDROBE / FOOD 命名锁——连道具状态也上锁**：

服装被锁为命名锁：正面描述 + 大写禁令（NO harness/seatbelt/vest/body-armor/backpack）+ 保住记忆点（全息鼻贴）。连拉面也上锁：必须红油火辣——NOT pale, NOT clear（道具的错误状态也点名）。

**③ NEGATIVE PROMPT 独立段——每条正面锁都有负面镜像**：

负面词库按失败类别分组（皮肤/手/服装/食物/台词/音乐），且 WARDROBE 锁的负面清单对应列 harness/seatbelt/vest、FOOD 锁对应列 pale/clear broth。**写负面清单的顺序 = 检查正面锁的顺序。**

**④ SHOT 段八字段自包含**（标题行打包机位+景别+时长+手持；SCENE CONTEXT 结尾带情绪判词 arrogant, sensual, in control + 禁令 NO words；COLOUR 行按 70/20/10 现场配比——这镜的 10% 暖是烟头微光；AUDIO 只写音效）。

### 1.6 倒置输入法（官方 brief 亲述的最重要技巧，数据实证）

brief 原文：Naomi 被困机甲倒置的镜头，纯提示词写物理效果不佳 → 把角色表本身倒置。数据验证：58 条提示词含 inverted/upside，视频段物理变为 the inverted mech sways gently; the leg-wrap bites; concrete crumbs trickle from the strained anchor——物理已烘焙进输入，提示词只需写状态与表演（This freed us to prompt more casually）。遇到特殊物理（倒置/失重/反常），改图不改词。

### 1.7 regenerations 实验区 = 参数化风格前缀

8-11 的 90 条 Seedance 2.5 实验把 STYLE PREFIX 从 Markdown 炼成 JSON 字段（style_prefix 对象含 style/operating_style/lighting/color_accent_doctrine/texture/camera_lens 六字段）——风格前缀的最终形态是可序列化的参数对象，团队在用代码化的方式管理风格系统。

---


## 二、风格系统：STYLE PREFIX（ZEPHYR 最核心的发明）

每个场景提示词开头是一段可复用的**风格常量**（官方在 regenerations 里把它存成了 JSON 字段 `style_prefix`，证明这是参数化复用的）：

```text
STYLE PREFIX — SCENE / "HARU'S STORY"

Style: 8K IMAX, photorealistic. Real organic film grain and halation.
Shot on large-format film. High dynamic range. NOT 3D render, NOT game
engine, NOT game-cutscene aesthetic, NOT cartoon.

OPERATING STYLE — HOYTE VAN HOYTEMA: expansive realism with intimate
handheld closeness, immersive in-camera feel, tactile textures,
atmospheric haze and volumetric light. Shallow depth of field on the
face, documentary-grounded framing, photochemical look. Room for
anime-style comedic timing in the performance.

Lighting: source-motivated natural light, single soft key, desaturated
rich earthy colour, faithful skin tones, gentle roll-off, no heavy grade.

Color — ACCENT DOCTRINE: ~70% desaturated green-grey room tone + raw
concrete; ~20% warm orange/yellow accent (motivated by ...); ~10% cool
daylight-blue counter-note from the windows.

Texture: matte non-reflective surfaces, lived-in worn materials ...,
organic 65mm film grain, no digital sheen, no plastic gloss.

Camera/Lens: large-format 65mm spherical prime, 180° shutter natural
motion blur; shallow large-format depth of field with creamy focus
falloff, natural halation ..., subtle lens breathing. No artificial
lens flares, no anamorphic streaks.

Skin: pore-level realism — visible pores, fine vellus hair, natural
asymmetry, no smoothing, no retouching. Half the face often falling
into shadow.

Acting: restrained naturalism carrying comedic timing — micro-behaviour
over performed emotion, the camera catching the moment rather than the
actor projecting it. Natural eye blinking throughout; active forehead
and brow micro-expression; no frozen mask-face, no dead eyes.

Physics: real gravity, inertia and mass; beanbag compresses and
re-settles under weight, head hangs off the beanbag edge under real
gravity, hair falls straight down toward the floor, nothing floats or
slides unnaturally.

Composition: spontaneous documentary framing; off-centre,
non-symmetrical compositions welcome.
```

**这套前缀的统计证据**（471 条唯一提示词中出现次数）：
- IMAX ×202、65mm ×202 —— 大画幅是默认底色（DETOUR 是 35mm）
- HOYTEMA（Hoyte van Hoytema，《奥本海默》摄影师）×111/90 —— **直接引用真实摄影师作为"操作风格"**，DETOUR 只引用胶片型号
- ACCENT DOCTRINE ×134 —— 色彩配比精确到百分比：`~70% green-grey + ~20% warm accent + ~10% cool counter-note`
- handheld ×239、documentary ×160 —— 纪录片手感
- Acting: ×75、eye blink ×79、micro-behaviour ×26 —— **表演指导进提示词**（眨眼、微表情、"摄影机捕捉而非演员表演"）
- Physics: ×76 —— 物理段独立成节

**NEGATIVE PROMPT 独立段**（28 条，且明示"paste into Seedance's negative field"）：
```text
plastic skin, waxy skin, rubbery skin, airbrushed skin, over-smoothed
skin, poreless skin, doll, mannequin, wax figure, CGI face, 3D render,
video-game character, uncanny valley, glossy plastic face,
beauty-filter, over-retouched, mushy AI texture, warped face,
asymmetric melted features, dead eyes, no catchlights; melting hands,
extra fingers, fused fingers, deformed hands...
```
——专门针对 AI 视频的常见失败模式（蜡感皮肤、恐怖谷、融手）。

---

## 三、镜头规划数据（节奏证据）

**单镜时长标注**（~Ns 出现次数）：~4s×155、~3s×126、~6s×125、~5s×106、~10s×98、~8s×67、~12s×15、~15s×10、~24s×2
——**典型节奏是 3~6 秒一镜**，比 DETOUR（固定 30 秒多镜头）更碎、更电影感。

**每条视频的镜头数**：2 shots×8、3 shots×12、4 shots×2、5 shots×7 —— 单条 2~5 镜。

**分辨率声明**：8K×170、4K×80 —— 官方直接要 8K（大画幅 + 8K 是 ZEPHYR 的质感来源）。

**倒装镜头的直接证据**（视频提示词原文）：`the inverted mech sways gently; the leg-wrap bites; concrete crumbs trickle from the strained anchor` —— 倒置状态下的物理细节（缓摆、咬合、混凝土碎屑）都被逐一规划。

---

## 四、迭代与实验方法（官方的"科学实验"）

1. **regenerations 文件夹 = 受控实验区**：90 条全部是 Seedance 2.5（8-11 当天 16:16~16:50，34 分钟密集重跑）。旧提示词（Seedance 2.0 时代的）直接喂给新模型做 A/B——**模型升级时的标准动作：老资产全量重测**。
2. **style_prefix 参数化**：实验时把风格前缀从 Markdown 提炼成 JSON 字段（`"style_prefix": {"style": ..., "operating_style": ...}`）——风格系统从"段落复用"进化成"结构化参数"。
3. **倒置角色表**（brief 自述的核心技巧）：输入比提示词更有力。需要特殊物理（倒置/失重/反常）时，**修改输入图像**（把角色表倒过来），提示词只写状态和表演——"This freed us to prompt more casually"。
4. **bloopers 保留**：失败镜头与成片剪辑并存于同一项目——官方也把失败当资产。

---

## 五、与 DETOUR 的体系对比（两个项目对照表）

| 维度 | DETOUR（独立团队） | ZEPHYR（官方团队） |
|---|---|---|
| 提示词组织 | 平文本六段式（SCENE CONTEXT 等大写标题） | **Markdown 大纲 + JSON 结构双格式** |
| 镜头节奏 | 单条 30s 固定、多镜头 | **单镜 3~6s 更碎**、单条 2~5 镜 |
| 胶片语言 | 35mm + Kodak/Portra | **65mm IMAX + 8K** + halation |
| 风格锚点 | 引用胶片型号 | **直接引用摄影师**（Hoyte van Hoytema） |
| 色彩系统 | 双世界（现实暖金 vs 游戏绿月光） | **ACCENT DOCTRINE 百分比配比**（70/20/10） |
| 表演指导 | 状态词（meek/confident） | **Acting 节：眨眼/微表情/表演哲学** |
| 道具制作 | 图生图无文字提示词 | **JSON 结构化产品级描述**（包装/中控面板） |
| 特殊物理 | 后视镜反射等负面空间约束 | **倒置角色表（改输入不改提示词）** |
| 负面清单 | 散在 Avoid | **独立 NEGATIVE PROMPT 段**（专打 AI 失败模式） |
| 文件夹管理 | 多级分类（角色/场景/分镜） | **扁平 + 提示词内自组织 metadata** |
| 迭代方式 | 跨模型赛马 + EDIT 微调 | **regenerations 受控实验区 + style_prefix 参数化** |

**两套体系共通的底层规律**（跨项目验证的结论）：
1. 风格系统必须**成段可复用**（DETOUR 的色彩段 / ZEPHYR 的 STYLE PREFIX）
2. 一致性靠**元素引用 + 控制边界声明**（两个项目都用 `<<<ID>>>` + "只控制什么"）
3. 负面约束是主战武器（DETOUR never×558 / ZEPHYR never×246 + 独立负面段）
4. 物理/表演/声音都要**显式写**进提示词
5. **改输入 > 加提示词**：ZEPHYR 的倒置角色表是这一条的最强证据

---

## 六、复用检查清单（ZEPHYR 补充项，叠加在 DETOUR 清单上）

- [ ] 风格前缀是否参数化了（可整体复用、可存 JSON）？
- [ ] 是否引用了真实摄影师/摄影指导作为"操作风格"锚点？
- [ ] 色彩是否精确到百分比配比（70/20/10）而不只是形容词？
- [ ] 表演节是否写了（眨眼/微表情/表演哲学"捕捉而非表演"）？
- [ ] NEGATIVE PROMPT 是否独立成段、专打 AI 失败模式（蜡皮肤/融手/死眼）？
- [ ] 单镜时长是否 3~6 秒、镜头标题是否含 机位+时长+约束 三要素？
- [ ] 特殊物理需求是否考虑过"改输入图像"而不是堆提示词？
- [ ] 模型升级时是否用 regenerations 区做全量重测？
- [ ] 产品级道具是否用 JSON 结构描述？
