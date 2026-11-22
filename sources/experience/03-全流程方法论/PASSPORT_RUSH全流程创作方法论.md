# PASSPORT RUSH 全流程创作方法论

> 来源：官方 studio 新开源工程 PASSPORT_RUSH_ANIM（14,612 件，全站最大），02 区 12,093 件生成资产 / 1,193 条去重提示词全部入库 + 官方 brief 全文 13.5KB。
> 定位：**全站首部官方 3D 动画片工程**——Blender 手调动画 + AI 生成的混合管线，"cartoony" 运动语法的官方标准。

---

## 〇 项目档案

| 维度 | 内容 |
|---|---|
| 片名 | PASSPORT RUSH（护照狂奔） |
| 导演方 | higgsfield.studio（官方） |
| Logline | 登机前几分钟，女孩发现护照落在家——穿越末日狂奔赶飞机 |
| 五幕 | Seq1 Airport / Seq2 Taxi Driver / Seq3 Cop / Seq4 Ninja / Seq5 Home-Airport |
| 体量 | 官方 count 14,612（实拉 jobs 12,093；差额 2,519 为上传素材）；**Ninja 序列最重：3,776 件占故事档 44.3%**，Taxi 次之 2,203——两大动作戏占 70.1% |
| 模型 | seedance_2_5×7,323（61%）+ text2image_soul_v2×3,697（图先行）+ seedream_v5_pro×942 |
| 语言 | 英文为主 + **中文 372 条**（含 blockout 中文超长块）+ 俄文 130 条 |

## 〇.5 整体画面风格 DNA（词频实测 + 官方声明双证）

### 核心公式（官方 brief 原文，逐字）
> **"Clean 3D props + watercolor environments."**
> **"Watercolor location + golden-hour lighting."**

即：**干净的 3D 角色/道具 + 水彩环境 + 黄金时刻光**。词频实测完全对应：

| 风格元素 | 词频 | 证据原文 |
|---|---|---|
| uuid 资产锚 | ×2,100 | `<<<asset-uuid>>>` 全库通用 |
| 水彩/墨线 | ink ×1,763 | `a painted original — paper grain, soft watercolor washes and blooms, fine dark ink linework on edges; the lines carry a gentle hand-drawn wobble` + `Ink follows the surface / fabric surface`（墨线跟随表面——水彩贴图不被 3D 运动撕碎的锁） |
| 十二动画原则 | twelve principles ×64；squash ×508 / stretch ×897 / anticipation ×475 / follow-through ×429 / secondary action ×366 / appeal ×262 | `FULL 12 PRINCIPLES applied throughout (squash & stretch, anticipation, staging, pose-to-pose, follow-through & overlap, ease in-out, arcs, secondary action, timing, exaggeration, solid drawing, appeal)` |
| **ON TWOS 二帧律** | on twos ×722 / stepped 12 ×160 / 12 fps ×203 / held frame ×205 | `animation ON TWOS (every key pose held exactly 2 frames, stepped pose-to-pose, no mushy interpolation)`——全站首次出现的**帧率风格化锁** |
| 拉伸中间帧 | smear ×408 | smear frames（美式动画的拖影帧写法） |
| 画幅 | 16:9 ×495（主）+ 2.39 ×46 + 9:16 ×14（竖版物料） | 16:9 cinematic 为主流声明 |
| 官方光前缀 | golden-hour | `Late-afternoon golden-hour lighting, low warm sun, long dramatic shadows, warm highlights, strong depth and dimensionality.`（官方建议直接复用的 style prefix） |

### 造型语言（官方设计笔记原文）
- 女主：夸张比例——**细腿、细脖、圆头**，"comfy airport look"，幽默感来自**脸和耳朵**的 awkward charm；早期版本"太傻"，最终版在 funny 与 cool 之间取平衡
- 逆向教训：车用水彩贴图在运动中"像平 PNG 拉伸在几何体上"→ 车改纯 3D，水彩只留给环境
- **360 度转身视频替代角色表**：`Instead of a traditional character sheet, we used a 360-degree character turnaround video that also included facial expressions and voice.`（含表情+配音的角色视频表——比静态表更强的身份锚）

## 一 工作管线（官方 brief 逐字整理）

```
Pre-Production：idea + script + 传统分镜（全片 storyboard PDF）+ 资产
   ├─ 角色：Soul 系生成 → 手工精修（调色/加细节/修伪影/加铅笔线强化剪影）
   ├─ 环境：水彩风（多次试错险些放弃，最终"clean 3D + watercolor 环境"定案）
   └─ 资产先行动测试（静图好看 ≠ 资产合格，必须视频态验证）
Blender（复杂动作专供）：
   ├─ 动画师手调为主（cartoony 运动必须手键——AI 直出会写实化）
   ├─ Higgsfield 插件生成 3D 道具（出租车/环境/背景车辆）
   └─ 选型标准原文："anything that would be harder to describe to Claude and take longer to get right through generation"（难描述给 Claude 的动作交给 Blender）
Production（双阶段目录）：
   ├─ Art_direction：Characters 1,229 + Locations 844 + Props 2,694 + Video checks 1,545
   └─ 五序列目录 Seq1-5 → 各场景子目录 → 镜号段目录（19-25 / 34-50…）
      全片粗剪 → 逐场景重生成（序列目录出现多次的原因）
Post：内部调色师全片手工统一 + 原创配乐 + 声音设计
```

## 二 提示词结构两大流派（1,193 块实测）

### 流派 A：官方 16 段式动画扩展版（535 条英文长块 >3K）
段落频次实测：AUDIO ×484 / PHYSICS ×387 / HARD CUT ×385 / CAMERA ×385 / LIGHTING ×353 / OPTICS ×337 / ACTIVE REFERENCES ×267 / SCENE CONTEXT ×246 / ACTION TIMING ×189 / **ANIMATION STYLE ×116** / MICRO-ACTING（新增段）……

最长块（44,103 字符，Scene 12 游行戏）骨架：
```
SHOT 1 → ORIENTATION → FIRST FRAME → ACTION TIMING → MICRO-ACTING → PHYSICS →
CAMERA → OPTICS → AUDIO → SHOT 2 → … → HARD CUT — MATCH ON EMOTION → SHOT 3 → …
```
**与写实系 16 段式的三大差异**：
1. 新增 **ANIMATION STYLE** 段——声明 ON TWOS / 12 原则 / stepped pose-to-pose
2. 新增 **MICRO-ACTING** 段——卡通表演的微动作层
3. 剪辑点写 **HARD CUT — MATCH ON EMOTION**（情绪匹配剪辑，动画表演专用）

### 流派 B：Blockout 视频驱动（99 条）
`<<<video_1>>> — NEW blocking layout, controls CAMERA and RHYTHM only: match its per-shot camera framing, movement, shot order, pacing and the screen positions of its blockout figures: YELLOW figure = the heroine…; BLACK figure = the ninja groom…; RED figures = the ninja crowd…` + `The blockout is geometric and never controls style.`

彩色小人 blockout 视频只锁**机位/节奏/走位**，明确声明"不控制风格"——ONEIRIC Diagram Skill 的视频版进化：从"平面示意图"升级为"Blender 排版视频"。

### 流派 C：中文块（372 条）含 [cite:] 标注残留
最长中文块 12,106 字符带 `[cite: format]` `[cite: quality, mood]` 标注——**Claude 生成痕迹直接入库未清洗**，反证官方团队确实用 Claude 写 Seedance prompt（与教程声明一致）。

## 三 官方五大风格铁律（brief "Learnings" 逐字）

1. **动的东西纹理要简**——"Clean 3D props + watercolor environments"（重水彩贴图在运动帧间保不住，会变成平贴图拉伸）
2. **资产必须先动起来测**——"A finished-looking image is not enough to validate an asset. It needs to be tested in video."（静图 ≠ 合格资产）
3. **角色参考必须挂全**——早期没挂角色表时"模型自己发明了出租车里的随机乘客"；"The model may invent missing information"（模型会脑补缺失信息——所有该出现的角色必须明示）
4. **用光统一风格**——正午光让水彩变平；队友在 prompt 加了一句 "evening light" 救了全片 → "Watercolor location + golden-hour lighting" 成为视觉公式
5. **光的语言全片锁死**——同一个光前缀复用到尾："Repeating a stable lighting formulation helps separate shots feel like they belong to the same film."（建议前缀原文：`Late-afternoon golden-hour lighting, low warm sun, long dramatic shadows, warm highlights, strong depth and dimensionality.`）

## 四 ON TWOS 动画语法卡片（全站独家）

官方在写实模型上做卡通动画的完整写法（可直接抄）：
```
ANIMATION STYLE
Animation ON TWOS: every key pose held exactly 2 frames, stepped pose-to-pose,
no mushy interpolation. FULL 12 PRINCIPLES applied throughout (squash & stretch,
anticipation, staging, pose-to-pose, follow-through & overlap, ease in-out, arcs,
secondary action, timing, exaggeration, solid drawing, appeal).
Smear frames allowed on fast transitions. Secondary action on every held pose.
[运动物体] keeps cartoon weight: squash on impact, stretch in motion, follow-through settles.
Output at 24fps (animation stepped at 12fps on twos).
```
配套反锁：`NO slow motion`（写实模型爱加慢动作，动画喜剧必须实时速度）；`NOT photoreal, NOT photographic`（反复声明反写实）。

## 五 与既有体系的关系

- **谱系位**：官方第 12 开源工程；KOK_BORU 系手绘 2D 的 **3D 动画对应物**；Blender 工作流教程（01 区手册）的**官方实战成品**
- **Blockout 谱系**：RED_FLAG 火柴人图 → ONEIRIC Diagram Skill → **PASSPORT_RUSH 彩色小人 Blender blockout 视频**（三代进化）
- **帧率锁谱系**：KOK_BORU_FILM 的 24fps 写实锁 → 本片 **ON TWOS 12fps 卡通锁**（同概念反向用）
- 中文超长块 + [cite:] 残留 = "Claude 写 prompt"工作流的直接物证

## 六 可复用清单

1. 动画片头声明模板（§四卡片）
2. 水彩+3D 混合的材质分工规则（动物体 clean 3D / 环境水彩 + `Ink follows the surface` 锁）
3. 官方黄金时刻光前缀（逐字可用）
4. 360 度转身视频角色表法
5. "资产先动测再投产"验收流程
6. 五序列×镜号段的工程目录学（含"全片粗剪→逐场景重生成"的双轮生产法）
