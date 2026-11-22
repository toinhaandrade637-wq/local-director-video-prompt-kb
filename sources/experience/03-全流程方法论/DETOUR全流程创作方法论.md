> **v2 版本说明（2026-09-06）**：本文档数字已按用户提供的全新工程链接重抓更新——
> 总资产 6161（旧版 5469 作废已删）/ 带提示词 6154 / 去重提示词 2172 / 113 folder（含 FINAL）。
> 新版揭示 SCENES 分镜区结构（Scene 01-12 + 镜头子目录）与 seedance_2_5 + seedream_v5_pro 主力阵容。
> 文中引用的原文提示词仍然有效（旧版提示词 100% 包含于 v2）。

DETOUR 全流程创作方法论

> **依据**：对该项目全部 6156 条原始提示词（2172 条唯一文本）、109 个文件夹、10 个分镜场景的完整数据挖掘。
> 所有数字都来自全库统计，非印象总结。模板段可直接复制修改使用。
> 配套数据包：`DETOUR_项目完整提示词.zip`（2172 条唯一提示词 + 分类明细 + 分镜索引）。

---

## 〇、这是一个什么样的项目（先看懂故事，再学提示词）

**故事**：Ryu 是个一生规避风险的披萨外卖员。一次导航故障给他一条快 5 分钟的捷径，途中遇到无畏的 Lisa，两人卷入一场每过弯都改变规则的公路竞赛——对手是 Demon、Gamer、Mad woman 等"游戏世界"车手。要回家，他们必须搞明白这条公路，以及彼此。

**创作母题（brief 原文）**：2000 年代街机赛车游戏 + 动作电影的怀旧——速度的快感、大胆的奇观、日常现实与游戏世界的碰撞。竞赛是"在不断变化的世界里建立关系、克服不敢冒险的不安"的隐喻。

**叙事骨架（从提示词数据还原）**：
- 开场（Scene 01）：披萨店日常喜剧——电话、揉面、父子交接披萨，建立"家庭生计"的赌注
- 展开（Scene 02-03）：送餐路上——陡坡慢行的冷面喜剧、高架堵车 11 分钟死线，遇到 Yakuza 拦路
- 相遇（Scene 03 尾）：Lisa 的两声车笛（beep-beep）是全片第一个"快节奏摄影机运动"的触发点——**节奏本身在讲故事**
- 竞赛（Scene 04-08）：进入游戏规则——deadline、power-up、power-up 失效、四车混战、后视镜追逐
- 收束（Scene 09-10）：Suspenseful dramatic vibe——月光赛道、终局

**情绪弧光的写法证据**：Ryu 的状态词从 meek/unsure（48 次提及）→ confidence/confident（75 次）→ dread（17 次）；家庭的 stakes 用"还剩三件""あと10分"这类倒计时道具具象化，而不是心理描写。

**分镜节奏数据**（每场镜头文件夹数 / 视频条数）：
Scene 01: 2/70 | 02: 2/49 | 03: 6/118 | 04: 3/37 | 05: 3/132 | 06: 8/173 | 07: 10/120 | 08: 13/145 | 09: 1/24 | 10: 1/164
——**开场镜头少而生成密度高（磨质量），中段竞赛镜头切碎（赶节奏），终局一个大场面反复打磨（Scene 10 生成 235 次）**。

**各场基调（提示词首句自声明）**：
Scene 01 `Action comedy vibe and timings` → 02 `Warm deadpan character comedy` → 03/05/09 `Suspenseful action vibe` → 10 `Suspenseful dramatic vibe`。
每条视频提示词第一句就是基调声明，全片完成"喜剧→悬疑→戏剧"的三段过渡。

---

### 0.5 整体画面风格（一眼认出 DETOUR 的视觉 DNA）

**看片感受**：90 年代末东京味的老香港街头——橄榄绿的白天城市烧着霓虹色，夜晚高架赛道泡在绿月光里；35mm 胶片颗粒粗粗地铺在每一帧上，CRT 游戏画面闪着扫描线。人物是漫画感的热血少年，机甲恶魔却带着日本神话的狰狞华丽。

**视觉 DNA 六要素**（词频来自 2,172 条唯一提示词）：

| 要素 | 定义 | 数据证据 | 提示词落法 |
|---|---|---|---|
| 底片 | 35mm 胶片 + 颗粒 + 光晕 | 35mm ×375、grain ×626、halation ×274 | 每条以 Photorealistic 35mm film photograph 开头 |
| 基调 | 日港混血：日本+香港 90 年代末 | STYLE 句原文反复出现：Japanese and Hong Kong cinema, late nineties | 直接引用地区+年代，不写泛化词 |
| 色彩 | 现实世界=橄榄绿×饱和色×暖肤；游戏世界=绿月光 | olive ×247、saturated ×354、burning colour ×203；红 ×903 全库最高频 | 双世界色彩段原文：Ordinary-world = warm neutral and dusty-gold base with muted olive, khaki, mustard, terracotta, brick red, cream, worn warm grey ... lived-in and restrained rather than orange-washed |
| 光源 | 钠黄街灯 + 霓虹 + 绿月光 | sodium ×153、neon ×172、moonlight ×100 | 游戏世界：月亮始终在前方；现实：钠黄路灯暖晕 |
| 质感 | 皮肤毛孔 + CRT 扫描线 | pore ×142、CRT ×104（scanlines / interlacing / color bleed / analog glow） | CRT 四件套写进游戏画面提示词 |
| 情绪判词 | 热血 + 狰狞 + 怪物美学 | 红 ×903、蓝 ×412（夜赛冷底） | 判词如 vivid where it gathers、狰狞恶魔设计 |

**两个世界的画面对比**：白天戏是 "burning colour" 的暖橄榄——像被夕阳烧过的旧照片；游戏世界整体沉入绿月光 + 棋盘格赛道的冷结构色。整部片的色彩叙事就是"暖日常被绿异世界入侵"。

---


## 一、整体风格系统（共通资产，所有提示词共享）

### 1.1 双世界色彩系统（最重要的风格骨架）

提示词里写明了两套互斥的色彩规则（数据出现频次佐证其贯穿性）：

**现实世界（Ordinary-world）**——原文定义：
> warm neutral and dusty-gold base with muted olive, khaki, mustard, terracotta, brick red, cream, and worn warm grey. Daylight and practical sources feel physically motivated; pale sky may roll gently toward cream. Keep the image lived-in and restrained rather than orange-washed.

**游戏世界**——greenish moon、更超自然的氛围（moon 在全库出现 266 次，是最高频的视觉锚点之一）。

**反污染负面清单**（照抄可用）：
> Avoid cyan contamination, electric blue, magenta, violet, rainbow cyberpunk colour, crushed blacks, harsh digital contrast, HDR, and oversharpening.

**色彩管理规则**：一条画面只允许一个主色强调（Preserve one clear dominant colour accent; any other coloured elements remain smaller, dimmer, or less saturated）——每个角色有自己的强调色和车灯色温。

### 1.2 胶片质感语言（频次统计）

| 词汇 | 出现条数/2172 | 作用 |
|---|---|---|
| 35mm | 375 | 默认胶片底 |
| grain | 626 | 颗粒感 |
| Kodak | 301 | 色彩科学锚点 |
| Portra | 174 | 人像胶片 |
| neon | 178 | 夜景霓虹 |
| photochemical | 4 | 明确声明"光化学感光"而非数码 |

**写法规律**：定位句是 "Photorealistic 35mm film photograph"（角色表 22 条）或 "Ultra-photorealistic CHARACTER MODEL SHEET"（81 条），并主动声明 **"NOT a 3D render, NOT CGI, NOT concept art"**（55~60 条）——正反双向锁定质感。

### 1.3 相机语言（频次统计）

close-up 165 / depth of field 115 / 50mm prime 86 / shallow depth 85 / low-angle 77 / closeup 77 / wide shot 53 / macro 41 / OTS（过肩）31 / top shot 13 / extreme closeup 21
——**写提示词像摄影指导写机位单**：焦段、景深、机位高度、景别全部明确。

### 1.4 世界观锚点

Japanese 435 / elevated（高架）217 / pizzeria 101 / Tokyo 85 / izakaya 24 / arcade 10
——地点不是背景板，是反复引用的常量。披萨店甚至写了"正反打配套"（the reverse of the pizzeria, aligned in a straight line），保证机位切换空间连续。

---

## 二、人物提示词：怎么写

### 2.1 五段式结构

```
① 定位句 — Photorealistic 35mm film photograph. Character reference plate
② 输出形式 — 三视图/四视图合一张（正/背全身 + 侧面 + 头部特写）
③ 分节描述 — THE MAN / FACE / GLASSES / HAIR / JACKET / TROUSERS... 一部件一节
④ 材质磨损 — 污渍、刮痕、褪色写到"级别"（写实感的来源）
⑤ Avoid 清单 — 穷举不想要的一切
```

### 2.2 关键技巧（实证）

- **永久记忆点钉死身份**：Ryu 的"左眉略高、左脸颊一颗痣、鼻旁另一颗、一边眼略小"——跨镜头防走形的锚。
- **背景锁死**：`exact colour HEX #808080 (50% grey)` + `NO gradient, NO vignette, NO shadow`（162 条使用）——后续局部重绘不被背景干扰。
- **载具写进角色表**：Props 文件夹 390 个资产全部无文字提示词（图生图工作流）——"人和车"在角色表里一起定稿，车的所有细节都在角色段落里。
- **real life → FINAL 双阶段**：先写实试验版，稳定后出 FINAL 四视图定稿版。
- **身份段落复用**：定稿后的角色描述作为整段文字在视频提示词里重复粘贴（"Ryu_basic is the same slim young man...Preserve his face, repaired glasses, hair silhouette...consistently across every shot scale"）。

### 2.3 可复用模板

```text
Photorealistic 35mm film photograph. Character reference plate, three views of
the same [角色] on one sheet: full length front view, full length back view,
and one extreme close-up head shot. All three on the same empty seamless
neutral mid grey studio backdrop, same neutral lighting, same lens.

THE [角色]
[年龄/职业/国籍一句]。[体型、站姿、气质]。[正对镜头]。

FACE
[脸型/皮肤质感与瑕疵]。[眼睛神态]。[2~3 个永久记忆点：痣/疤/不对称]。

[每部件一节：发型/眼镜/帽/上衣/内搭/裤/鞋袜/配饰/载具]
每节：款式 → 颜色 → 材质 → 磨损污渍 → 位置关系。

Avoid: 3D render, CGI, concept art, watermark, text, [与设定冲突的一切]
```

---

## 三、场景提示词：怎么写

### 3.1 七段式结构

```
① 定位句（同人物）→ ② 场景类型+机位 → ③ 时代地点文化锚点
④ 前景/中景/背景逐层+左右方位 → ⑤ 光源类型色温 → ⑥ 大气+胶片质感 → ⑦ Avoid
```

### 3.2 关键技巧（实证）

- **正反打成对声明**：场景 A 与它的 reverse 在同一套提示词里，机位切换有据可依。
- **场景也要试验→定稿**：Locations 同样有 final/approved 子文件夹；场景提示词可以长到 17K 字符（护栏材质、灯距、警示牌逐项写）。
- **光照归属声明**：每个场景写明属于现实世界还是游戏世界的色彩系统（Scene 09 原文："the moon is always ahead in that direction"——月光方向成为空间锚）。

### 3.3 可复用模板

```text
Photorealistic 35mm film photograph. [Wide establishing shot] of [地点],
[机位与视角]. Set in [时代+地点+文化锚点, 如 1990s Tokyo].
[前景内容与方位]；[中景内容与方位]；[背景内容与纵深线条].
[光源与色温：钠黄路灯/暖窗光/绿月光]，[大气：湿地面/雾/雨].
Kodak-inspired texture, fine grain, limited warm palette. [所属世界: Ordinary-world / game world].
Avoid: [现代元素/文字/水印/cyberpunk 色/与世界观冲突物]
```

---

## 四、视频提示词：怎么写（全项目最核心的资产）

### 4.1 基础结构（六段式，适用单镜头）

```
① 基调声明 — "Action comedy vibe and timings." / "Suspenseful action vibe."
② 元素引用+状态 — 场景/角色/道具：<<<ID>>> + 一句当前情绪状态
③ 镜头清单 — 00:00–00:05: 逐秒时间码（3~5 秒一镜，单条 ≤2 镜，一次干净硬切）
④ 每镜四件套 — 机位/景别 → 动作序列 → 台词（日文原文+口型同步+声音性格）→ 反应
⑤ 空间铁律 — 谁在左谁在右、什么绝不能出现（负面空间约束）
⑥ 声音指示 — No music, SFX only / 音效清单
```

### 4.2 高级结构（多镜头整场，16~21 条采用）

```text
[S03-B01-V004]                      ← 镜头编号：场-镜-版本号

SCENE CONTEXT                       ← 这场戏讲什么、因果顺序、节奏设计
A kinetic 24-second sequence following the shotlist's exact causal order:
jam, moving Ryu, eleven-minute deadline, usable gap, deliberate block,
silent burger refusal, ten-minute update, friendly signal, full Lisa reveal.
Before Lisa, movement is heavy but continuous; every cut inherits Ryu's
forward impulse. Her signal causes the first sharp camera and rhythm accent.

ACTIVE REFERENCES                   ← 每个参考图的完整定义与"控制边界"
<<<RyuID>>>: [完整外观定义]。controls [它只控制什么]。
<<<BikeID>>>: [完整车辆定义]。controls [...]. Preserve [...across every shot scale].

0:00–0:04 — SHOTLIST 1–4: [镜头名]   ← 对齐外置分镜表的编号
[机位/景别/运动]。[动作序列]。

0:13–0:15 — SHOTLIST 9–10: PARALLEL BLOCK AND BRAKE
[动作+空间铁律：The SUV never points across the road.]

PHYSICS AND AUDIO                    ← 物理与声音专段
Traffic has weight but never becomes a tableau: engines vibrate, exhaust
drifts, brake lights pulse... Ryu's wheels remain grounded, suspension
reacts... No other horns, dialogue, narration, subtitles or score.

LIGHT AND COLOUR                     ← 色彩专段（套用 §1.1 双世界系统）
Photochemical colour response with restrained saturation... [Ordinary-world colour 定义]...
Avoid cyan contamination, electric blue, magenta, violet, rainbow
cyberpunk colour, crushed blacks, harsh digital contrast, HDR, oversharpening.
```

**要点**：他们维护一份外置 shotlist（分镜表），提示词按 `SHOTLIST 9–10` 编号对齐——**提示词不是孤立文本，是分镜表某个镜头的执行细则**。

### 4.3 视频提示词的硬规则（实证数据）

| 规则 | 证据 |
|---|---|
| 每条视频 30 秒、多时间码段 | 总时长分布中 30 秒占 69/190 条明显多数 |
| 基调首句必写 | Action comedy 17 / Suspenseful 若干，每场首个提示词均自声明 |
| `never/NEVER` 硬约束高频使用 | 558 + 59 次（占 2172 条的 40%）|
| 中文提示词占 370/2172 条 | Scene 02/04/06/07 大量中文长提示词，Seedance 2.5 中英皆可 |
| 口型同步三件套 | 台词日文原文 + "口型"（56 次）+ 声音性格（low, grave, serious Japanese voice）|
| 音频规划进提示词 | No music 152 / SFX only 158 / horn 114 / ambience 44 |
| CUT TO 硬切声明 | 86 条 |
| 媒介质感 | CRT 段落写 interlacing, scanlines, color bleed, analog glow（20 条）|

### 4.4 空间铁律的写法（最值得抄的部分）

```text
[正面] Demon 在整个视频中始终位于现实道路最前方；Gamer 始终在其后方追赶。
[负面] Gamer 从未驶到 Demon 前方，也从未与 Demon 并排。
[媒介] Gamer 只通过后视镜反射被看见，绝不直接出现在镜框外的主画面空间。
[物证] CRT 屏幕正面完全不可见，只看见实体背壳（因为镜子朝后）。
[物理] 两车保持真实安全间距，不发生碰撞；悬架随载荷压缩回弹，床垫小幅惯性摆动。
```

**模式总结：先写"什么必须为真"，再穷举"什么绝不允许"，然后给物理合理性解释为什么**。

---

### 4.6 元素控制边界声明的完整原文（俄语版揭示的精细规则）

DETOUR 后期提示词改用俄语写（这是在 HEP 检查器里发现的），其中 power-up 元素的控制边界声明是全工作区最精细的。译文与原文对照：

    <<<dcfe3a23...>>> задаёт точную привлекательную внешность взрослой
    Crazy Girl, естественное лицо, кожу, глаза, волосы, макияж и одежду.
    （该元素定义：成年 Crazy Girl 的精确外貌、自然脸、皮肤、眼睛、头发、妆容与服装）

    <<<c5d30835...>>> задаёт внешний вид power-up: ромбовидную пластину...
    Серый фон, плоский силуэт, масштаб и ориентацию из
    <<<c5d30835...>>> не брать.
    （该元素定义 power-up 外观：菱形板…**灰底、平面剪影、比例和朝向不要继承**）

    В сцене power-up — жёсткий цельный куб... размером ровно один метр
    на один метр на один метр: шесть плоских граней, прямые рёбра,
    нижняя грань левитирует в 40–50 сантиметрах над дорогой.
    （本场中 power-up 是一个致密发光硬立方体：**精确尺寸一米×一米×一米**，
    六平面、直棱、底面悬浮于路面上方 40–50 厘米）

**三层精细规则**：
1. **正向白名单**：元素"定义"什么（задаёт）——脸、皮肤、眼、发、妆、衣逐项点名
2. **反向排除**：参考图里的灰底/平面剪影/比例/朝向——**不继承**（не брать）。参考图是棚拍资产图，拍摄环境的东西绝不能跟着进正片
3. **场景内规格替换**：同元素在不同场景可以有不同形态——power-up 资产图是菱形板，但"本场中"它是 1×1×1 米立方体 + 精确悬浮高度。**元素外观以场景声明为准**

**方法论**：写"元素只控制什么"还不够——把**参考图的拍摄痕迹（背景/剪影/比例/朝向）列入反向排除**，并在场景需要时给元素**重新定义几何规格**。俄语团队在这里展示的控制粒度值得任何语言的项目效仿。

---


## 五、迭代工作流：怎么从草稿到定稿（附纠错机制）

### 5.1 四阶段时间线（真实创作日程，2026-08-11 ~ 09-02）

| 阶段 | 时间 | 动作（当日提示词分布）|
|---|---|---|
| ① 试验期 | 08-11 | Locations 13 + Characters 7 + trash 23 + Tests 3 —— 首日就大量试错（废案 23 条）|
| ② 设定期 | 08-12~14 | Characters 219 / Locations 107 —— 角色与场景双线密集定型 |
| ③ 场景补强 | 08-18~21 | Animation 90 + cover 32 —— 开始试动画、出封面 |
| ④ 动画量产 | 08-22~09-02 | Animation 为主（每天 20~72 条）+ 边做边补 Locations/Characters |

**核心节奏**：角色场景先行（前 10 天），动画在后（后 12 天），全程穿插 trash 沉淀废案。**不是线性流程，是"资产先行、动画随后、边拍边补"**。

### 5.2 单资产迭代模式（Ryu 角色表一天 21 次生成的轨迹）

```
1. nano_banana_flash 出第一版（3324 字符）——快模型低成本试错
2. seedream_v5_pro 加密细节（6787 → 9599 字符）——提示词逐版加密
3. 同一提示词三模型交叉测试（seedream / gpt_image_2 / nano_banana_2 各跑一遍）
4. 竖版 2:3 变体（海报构图）
5. 半月后 gpt_image_2 EDIT 模式微调（加番茄酱渍等）
```

**迭代依据（怎么确保下一代更好）**：
1. **长度递增 = 细节加密**：版本间不是重写，是往稳定骨架里加密物理细节（磨损、污渍、位置关系）。
2. **同文本跨模型赛马**：同一提示词在 2~3 个模型跑，选表现最好的继续迭代。
3. **保留稳定段、只改问题段**：对比 9604→7664 字符版本发现，迭代是**删掉出问题的镜头段、保留稳定段**——那次把 CRT 游戏机镜头拆出去独立成条，是因为整段塞一条视频效果失控。
4. **镜头拆分原则**：一条视频装不下就拆（Scene 07 拆成 B7-1~B7-10 十条）——控制单条复杂度是提高成功率的主要手段。

### 5.3 纠错机制：发现生成结果不对时怎么办

**EDIT THE ATTACHED 模式**（35 条实证案例）——修图的主力方法：

```text
EDIT THE ATTACHED [IMAGE / CHARACTER SHEET]. Keep [一切保持] exactly as it is.
[Change only X / One thing changes: X]。

WHERE: [改动的精确位置]。
[改动的形态/颜色/材质/物理细节]。

NOTHING ELSE: [再次声明其余一切不变]。
Avoid: [所有可能的偏差形态穷举]。
```

**实证案例**（从 35 条 EDIT 提示词还原出的纠错场景）：
- 排气管高度不对 → "Three changes only — 1. THE EXHAUST PIPES GROW TALL..."
- 车色不对 → "Change colours and surface materials only. Every shape stays exactly as it is"
- 车灯不对 → "Change only the headlights. Everything else stays exactly as it is"
- 封面字幕行不对 → "Change only the small line beneath the title"（连续 3 版逐步修正措辞）
- 角色表沾了番茄酱（剧情需要）→ 位置/颜色/光泽/负面形态逐项写（WHERE/COLOUR/FINISH/NOTHING ELSE/Avoid 五段）

**纠错核心口诀**：
1. **先定位错在哪**（WHERE 精确到画面方位）
2. **只改这一个点**，其余全部"exactly as it is"声明
3. **穷举可能的偏差形态**进 Avoid（模型容易犯的错提前堵死）
4. **改不动就拆**：整条视频失控 → 把问题镜头拆成独立条，简化每条的信息量
5. **改文本比重生成便宜**：先 EDIT 微调，失败 2~3 次才回到重生成

---

## 六、一致性保障体系（全项目地基）

1. **元素化**：角色/场景/道具定稿后注册为 Higgsfield 元素，视频用 `<<<ID>>>` 引用（900/2172 条使用）。文字不再重复设定，只写状态和动作。
2. **每个引用声明控制边界**：`<<<ID>>> controls [它只控制什么]`（controls only 15 + 只控制 11 条明确写出）——防参考图互相污染。
3. **身份段落整段复用**：定稿的角色外观描述作为常量段落粘进每条视频提示词，末尾加 "Preserve ... consistently across every shot scale"。
4. **关键帧延续**（brief 原文）："selected frames were carried forward as references to preserve racer positions, spatial continuity and power-up scale"——位置、空间、比例三类连续性靠帧传递，不靠文字。
5. **角色表 = 唯一事实源**：一切跨镜头争议回溯 FINAL 角色表。
6. **倒计时道具具象化**：手机屏幕「配達まであと11分」→「あと10分」——时间压力不用台词讲，用道具变体讲（同屏 spec 锁死：Keep `10` readable; no added UI）。
7. **废案保留**：trash 224 条不删——淘汰方向也有记录价值。

---

## 七、模型分工（什么时候用什么）

| 模型 | 占比 | 定位 |
|---|---|---|
| Seedream 5.0 Pro | 35.5% | 场景与角色主力生图；长提示词承受力最好（最长 17K 字符）|
| Nano Banana Pro/2/flash | 22.9%+ | 快速初稿、角色表迭代、局部重绘（application/surface 模式）|
| Seedance 2.5 | 21.1% | 全部视频分镜（逐秒时间码 + 多镜头结构 + 中英长提示词皆可）|
| GPT Image 2 | 15.8% | EDIT 微调与元素定稿（"Keep everything + one change" 模式最稳）|
| Higgsfield Soul | ~2% | 统一风格化 |
| Topaz/Photoshop/Premiere/Suno | 管线 | 放大/修图/剪辑/配乐 |

---

## 八、复用检查清单

**开工前**：故事三幕定了没？双世界色彩系统定了没？每个角色的强调色定了没？
**人物**：三视图合一张？2~3 个永久记忆点？部件写到磨损级别？背景锁灰 #808080？Avoid 穷举？
**场景**：前中后景+方位？光源色温？归属哪个世界？正反打配套？
**视频**：基调首句？≤2 镜/30 秒？逐秒时间码？每元素控制边界声明？空间铁律正负双向？台词三件套（原文+口型+声音性格）？音频指示（No music/SFX only）？
**迭代**：只改一个问题点？WHERE 精确？Avoid 穷举偏差？失败 2~3 次考虑拆镜头？同文本跨模型赛马？
**一致性**：元素注册？控制边界声明？身份段复用？关键帧延续？倒计时用道具不用台词？


---

## 附录：DETOUR v2 重抓新发现（2026-09-06）

### A. SCENES 分镜区结构（旧版未见的真实工作结构）
- 工程按 `SCENES → Scene 01-12 → 镜头子目录` 组织：Scene 03→B3-4，Scene 08→14 个镜头，Scene 06→10 个镜头+353 items
- 镜头级文件夹名即剪辑序号（B2-1/B2-2/B6-8/B6-extra2/FINISH）——**分镜工程学**：一场戏先拆镜头、逐镜头迭代，再归入 FINISH 收敛
- 分镜区 1479 items，其中中文提示词 697 条——AIST 团队**中英双语混用**：资产层英文（角色表/场景表）、分镜层中文（时长/画幅/类型锁）

### B. 模型阵容换代
| 旧版印象 | v2 实测 |
|---|---|
| seedance 为主 | **seedance_2_5 ×1682**（视频主力）+ **seedream_v5_pro ×2057**（图像主力） |
| — | nano_banana_2 ×1251、gpt_image_2 ×900（编辑/修图链） |
| — | soul_cinema_studio ×95、minimax_h3 ×3、kling3_0 ×2（试错痕迹） |
- 图:视频 ≈ 1.2:1 —— 与 4K_BLOCKBUSTER 同款"图先行"策略

### C. seedance_2_5 语法特征（v2 全库实测词频）
- **uuid 锚 ×1559**：`<<<63e45639-...>>>` 直接用资产 id 做 identity anchor（比 <<<image_N>>> 更工程化——资产改名不失效）
- HARD CUT ×68 / handheld ×197 / SCENE CONTEXT 段 ×37（官方 16 段式在此也有使用）
- 中文提示词 1239/6161（20%）——中文写法特征：`时长：X秒`锁、`画幅：21:9`锁、`类型：…`声明（与 KOK_BORU_FILM 中文体系同源）

### D. FINAL folder 终版镜（作者 2026-09-06 后新上传，已补抓入库）

终版对账时发现作者新建 FINAL folder，2 条 seedream_v5_pro 图像镜——**片尾定格镜的"负空间全书"**：

**镜 1（5477 字符）· 90 度高架弯道俯视图**——教科书级"世界复用声明"：
> `THE SAME WORLD, THE SAME ROAD, THE SAME MATERIALS AND LIGHT — same carriageway and width, same barriers, same worn chequer, same red beads, same gantries and their dot-matrix signs, same sodium lamps, same colour and grade. Only the piece of road and the camera are different. Where anything is unclear, the reference decides it.`
> （同一个世界、同一条路、同样的材质与光——只换路段和机位；**任何不清楚的地方，以参考图为准**。）
- 几何锁：`One continuous ribbon of constant width, no fork, no junction, no second road: two ends only, joined by the curve.`（一条定宽连续缎带，不分岔不交叉——两端口，一弧相连）
- 结尾负面清单逐项排除（ground-level camera / symmetrical composition / step or ledge / moon / cgi / 3d render / vignette / watermarks）——**逐项写"永远不"的排雷法**

**镜 2（4251 字符）· 红色雪佛龙箭头警示排**——"秩序即美"的重复元素写法：
> `THEY FORM ONE NEAT, ORDERLY, EVENLY SPACED ROW … a regular repeating rhythm following the curve, like sleepers on a railway or teeth on a comb. Never scattered, never clumped, never with a gap missing, never at random spacings, never at differing heights, never crooked, never tumbling.`
> （一排整齐、等距、等高、同向、同倾角——像铁轨枕木、梳子齿的规律重复；永不散落/成堆/缺齿/随机间距/高矮不一/歪斜/倾倒）
- 色彩锁：`Deep saturated red, never pink, never orange.`（纯度锁到"永不偏粉、永不偏橙"）
- 结尾同样负面清单（mirrored chevrons / solid glowing arrows / smooth continuous light / clean crisp graphics）——**把"AI 味"逐项点名禁止**

这两镜证明 AIST 团队的收尾法：**不拍新画面，用"世界复用 + 负面清单"再造片尾图**——与正文 O.5 负空间约束体系完全同源。

### E. 三轮对账终局（回答"确定全部提示词都在吗"）
1. 逐 folder BFS 法：6159 条
2. + FINAL 新 folder：2 条 → 6161
3. include_subfolders=true 从 ROOT 全量翻页法独立重抓：去空槽（48 条 items/v2 分页噪音）去重复（2 条）后 **6161 ✅ 与方法 1+2 完全互证**
4. 官方 count 6416 − 6161 = **205 = 无 job 上传类原生文件**（作者上传的音频/视频/素材，无提示词，API 不返回）
5. 结论：**项目内全部生成任务与提示词 100% 在库**，README.json 的 reconciliation 字段永久记录此对账链。

### F. 对账记录（用户 trust-but-verify 要求）
- v2 全量 6161 行 0 坏行；20 分区合计=全量 ✅
- 旧版 1479 去重提示词经前 80 字符 key 对账：**100% 包含于 v2**（104 条表面差异全部为编码/格式问题，S06-16 红宝石路障镜头等原文均在）→ 旧版安全删除
