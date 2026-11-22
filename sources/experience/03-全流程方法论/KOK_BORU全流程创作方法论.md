# KOK BORU 全流程创作方法论

> **依据**：对 Higgsfield 官方动画短片 KOK BORU（哈萨克游牧题材，手绘×AI 混合管线）全部 2716 个生成任务、2716 条提示词（218 条唯一文本）的完整逆向 + 官方 brief 自述。ID 级对账零缺零多。
> 这是**第四种体系**：前三个是写实路线（35mm 街头 / 65mm IMAX / 霓虹黑色），KOK BORU 是**手绘定格动画路线**——官方示范"AI 怎么做手绘动画"。

---

## 〇、项目画像

**故事**：哈萨克草原游牧生活与民间传说——两个母亲（一个女人、一只母狼）因一个失踪的孩子相连，几乎零对白叙事。
**混合管线**（brief 原文）：手绘定义每镜的外观、表演、情感意图 → AI 负责中间帧、环境、群体与动物运动（狼群/战斗/暴风雪）、光效迭代。
**结构**：每镜头一个文件夹（SH01~SH10）+ FULL10MIN（成片）+ Персонаэи（俄语"角色"）。
**时间线**：2026-05-27 ~ 07-02，峰值 06-09~06-12 四天 138 条唯一（手绘动画管线节奏较慢但每条极长：中位 **10114 字符**，最长 25K）。
**模型**：seedance_2_0 ×2656 绝对主力 + 少量 seedream/gpt_image_2 做资产。

---

### 0.5 整体画面风格（一眼认出 KOK BORU 的视觉 DNA）

**看片感受**：一幅会动的手绘油画——哈萨克草原的暴风雪在 12fps 的笔触颤动里翻滚，人物像传统动画一样一拍二地跳跃，而雪雾和炊烟却流畅地真实流动；颜色是褪色的羊皮纸暖调，母狼的眼睛是全画面最亮的一点。

**视觉 DNA 六要素**（词频来自 218 条唯一提示词）：

| 要素 | 定义 | 数据证据 | 提示词落法 |
|---|---|---|---|
| 底片 | 8K IMAX 声明 + hand-painted 油画质感 | 8K ×142、IMAX ×128、painterly ×108 | traditional hand-drawn 2D animation, hand-painted oil-brush texture on every drawing |
| 帧率 | True 12fps / ANIMATED ON TWOS / 笔触颤动 | 12fps ×159、boil ×163 | each pose held two frames then snapping, never gliding. Constant painterly BOIL |
| 摄影师 | Lubezki × Deakins 双引用（动画也用真人摄影师） | Lubezki ×133、Deakins ×121 | Cinematography: Emmanuel Lubezki × Roger Deakins |
| 双层时间 | 大气 smooth + 人物 stepped | 全库固定声明 | Atmospheric motion (drifting snow, breath-vapor, smoke) moves SMOOTHLY; figures step on twos |
| 色彩 | 褪色羊皮纸暖调 + 无月光的平灰蓝暴风雪 | yellow ×65、blue ×153、moonlight ×30（且明令 no moonlight on faces） | flat dim diffuse ambient glow from the storm itself, pale grey-blue ... no direct moonlight reaching the ground |
| 负面铁律 | NO 3D / NO interpolation / NO motion blur | stop-motion ×58 | NOT clay, NOT puppets, NOT 3D ... motion is the redrawing of strokes, not AI slop |

**画面气质判词**：残酷而温柔的游牧史诗——暴风雪的暴力（violent buran, hurricane-force gusts）衬托一拍二人物的笨拙温情。这是全工作区唯一的非写实画面体系。

---


## 一、风格系统：定格动画的三重锁

每条视频提示词的 Style 段（数据验证：STOP-MOTION ×120、12fps ×159、ANIMATED ON TWOS ×62、boil ×163、hand-painted ×187）：

```text
Style: 8K IMAX, traditional hand-drawn 2D animation, animated on twos at
12 frames per second — each drawing held for two frames then replaced,
choppy stepped motion cadence, visible pose-to-pose timing, distinct
keyframe drawings with no smooth in-between interpolation, hand-painted
oil-brush texture on every drawing, brushstrokes shifting and redrawn
from frame to frame, line jitter and boil between frames, no 3D render,
no game engine, no CGI smoothness, no high-framerate fluidity.
```

**三层反 AI 味锁**：
1. **帧率锁**：True 12fps、ANIMATED ON TWOS（一拍二）、每张画停留两帧再切换——直接对抗视频模型默认的 24fps 平滑插值
2. **质感锁**：painterly BOIL（笔触颤动）、每帧重绘的笔触、line jitter——"motion is the redrawing of strokes, not AI slop"
3. **负面锁**：NOT clay, NOT puppets, NOT 3D, NO smooth interpolation, NO motion blur, NO morphing, NO liquid or melting surfaces

**摄影师引用**：Emmanuel Lubezki ×133 + Roger Deakins ×121——**动画也引用真人电影摄影师**，用他们的光影语言定调。

---

### 1.5 DIRECTOR'S NOTES 导演注体系（115 条实证，KOK BORU 的隐藏核心）

KOK BORU 每条提示词在 STYLE 段之后有一段大写的 **DIRECTOR'S NOTES — non-negotiable for every frame and every cut**（导演注——每一帧每一剪不可协商）。这是把"导演阐述"直接嵌进提示词的结构。官方原文（雪崩场）：

    DIRECTOR'S NOTES:
    1. THE SCENE — the catastrophe, the heart of the whole story, and it MUST
    READ through a precise CHAIN OF CAUSE AND EFFECT, with composition and
    camera telling the cruel story. As ANA climbs the snowy cliff one-armed
    with her infant, her foot dislodges a slab of packed snow high on the
    slope; the slab breaks loose and roars DOWN the cliff as an AVALANCHE
    straight toward little UMAI... UMAI sees it coming down at her and
    freezes in quiet fear; the avalanche engulfs her and sweeps her away.
    ANA, high above, sees it and screams, helpless. No wolves, no rock —
    a slab of mountain snow becomes an avalanche pouring down the cliff...

**要点**：第一条不是镜头，是**因果链**（CHAIN OF CAUSE AND EFFECT）——这场戏的悲剧逻辑必须作为一个完整事件被理解，结尾还写了排除项（No wolves, no rock——这不是狼袭也不是落石，就是雪）。**提示词在教模型"读故事"**。

    2. CAMERA LAW (LUBEZKI handheld craft, applied WITHIN each shot — hard
    cuts between shots stay, but each shot is shot like Lubezki) — every shot
    is ONE continuous, motivated, flowing HANDHELD move, never static, never
    locked: (a) HANDHELD HUMAN PRESENCE — the camera is held in human hands,
    a living breathing presence inside the scene, a soft organic sway and
    drift, jolts and corrections, buffeted by the wind gusts, never
    gimbal-smooth, never tripod-locked, never mechanical; (b) CONTINUOUS
    MOTIVATED MOVEMENT — each shot moves for a reason driven by the action:
    it climbs with ANA, it tilts and falls following the avalanche, it
    cranes and reframes with UMAI, it reels with the scream — one fluid
    motivated camera move per shot; (c) IMMERSED IN THE ELEMENT — the camera
    is INSIDE the storm with the characters...

**CAMERA LAW 三条子法**：(a) 手持人感——镜头是"人手持的活物"，被风撞击、会呼吸，永不开抖火棉布平滑（never gimbal-smooth）；(b) 动机运动——每次移动都有戏剧理由（跟着 ANA 爬、跟着雪崩倒、跟着尖叫摇晃）；(c) 沉浸在元素里——镜头在暴风雪内部。**"每镜一次连续有动机的手持运动"是镜头法律**。

### 1.6 ANTI-DISNEY 反向风格锁（手绘动画的生死线）

同一段 DIRECTOR'S NOTES 开头：

    1. STYLE FIDELITY — ANTI-DISNEY: the faces must match the rough painterly
    authorial style of the reference paintings <<<image_2>>> <<<image_3>>>
    exactly. NOT Disney, NOT Pixar, NOT 3D, NOT cute, NOT a pretty
    symmetrical face, NOT large round eyes, NOT anime eyes, NOT smooth glossy
    rendered skin, NOT soft air...

**ANTI-DISNEY 锁**：对手绘动画而言，最大的敌人不是"画不好"而是"画得太漂亮"——AI 默认输出大眼萌系。所以负面清单不是技术性的而是**审美性的**：NOT Disney, NOT Pixar, NOT cute, NOT a pretty symmetrical face, NOT large round eyes, NOT anime eyes。**风格忠实 = 反潮流审美**，这条原则适用于一切"风格独特"的项目：你要的越怪，防"默认漂亮"的锁就要越重。

---


## 二、双层时间：大气 smooth，人物 stepped（最独特的发明）

brief 原文规律，在全部提示词中贯彻：

```text
Atmospheric motion (drifting snow, breath-vapor, smoke, ember-glow
flicker) moves SMOOTHLY; figures and any drawn snow step on twos with
secondary action.
```

**同一个画面里两种时间流速**：雪、雾、光按真实时间平滑流动（营造空间真实感）；人物按 12fps 一拍二跳动（保持手绘感）。这是"AI 手绘动画不像廉价 GIF"的关键——**环境用模型的连续性优势，角色用动画的离散美学**。

---

## 三、提示词结构：SHOT 段 + 尾部锚点复述

每条视频提示词 = Style 前缀 → SHOT 1/2/3/4 各自完整描述（HARD CUT 分隔）→ **尾部把全部风格锚点用一段话复述一遍 + Constraints 段**：

```text
HARD CUT to SHOT 3 — tight close-up on the mother's face from
<<<image_2>>>, [完整光照+微表演+物理描述], Camera: handheld, very
slight unsteady motion.

Style anchors across all shots: [12fps on twos / every micro-expression
drawn as its own held pose / blinks as distinct closed-eye frames /
brushstroke boil / ...]

Constraints: every character animated on twos, no moonlight on faces,
no rim light, ... avoid identity drift between cuts, avoid limb
distortion, no frozen masklike faces, no floating props.
```

**方法论要点**：
- **首尾双声明**：开头 Style 段 + 结尾 Style anchors 复述——长提示词（10K+ 字符）里模型可能"忘记"开头，结尾再钉一遍
- **Constraints: 段 194/218 条**——几乎每条都有独立约束段（官方 brief 说的 Style Prefix + Constraints 双固定段）
- **每镜末尾重申动画锁**（Animated on twos, choppy stepped motion, hand-drawn brushstroke boil）——每个 SHOT 段自带风格复述
- **微表演写法**：`eyelids snapping shut for two frames then snapping open`、`nostrils flaring with each ragged breath`——**连眨眼都按帧写**（这是 on twos 美学的必然延伸）

---

## 四、混合管线的资产方法（brief 自述）

1. **Canvas 铺资产**：角色表/道具表/环境先在 Canvas 铺开
2. **AI 生成 → 人工手绘覆盖**：Photoshop + Higgsfield 插件逐张修——保证文化准确性（哈萨克服饰等），笔触保持松弛
3. **质感影响表演**：brief 原文提示"quality of textures would affect the character performance later on"——手绘纹理质量直接决定后续视频生成质量
4. **剧本驱动**：15 页正式剧本（内部编剧）随系统提示词一起喂给 Higgsfield Claude MCP——提示词由 AI 起草、人工按镜头需求微调
5. **音频约束**：`No music. Only SFX.`（133 条）——音乐全部后期制作

---

## 五、四体系对照（DETOUR / ZEPHYR / RED FLAG / KOK BORU）

| 维度 | DETOUR | ZEPHYR | RED FLAG | KOK BORU |
|---|---|---|---|---|
| 路线 | 35mm 街头动作 | 65mm IMAX 纪实 | 霓虹黑色电影 | **手绘定格动画** |
| 美学敌人 | 走形/不一致 | 蜡感/CG味 | 色彩漂移/物理崩 | **AI 平滑插值味** |
| 核心武器 | 负面空间约束 | 风格前缀参数化 | 正向色彩/示意图 | **帧率锁+双层时间** |
| 提示词长度 | 3-10K | 3-20K | 1-10K | **10K+ 中位最长** |
| 摄影师引用 | 胶片型号 | Hoytema | 王家卫+杜可风 | **Lubezki+Deakins** |
| 人工环节 | 后期修图 | regen 实验 | 示意图绘制 | **手绘覆盖每张资产** |
| 双语 | 英文 | 英文 | 中英混写 | 英文 |

**四体系共通铁律（全部验证）**：
1. 风格前缀成段、首尾双声明
2. 一致性 = 元素引用 + @tag 命名
3. 正向形式 > 负面清单，但负面锁必须有
4. 每个领域的"AI 默认行为"都要显式对抗（smooth/慢动作/黄移/CG味）
5. 音频约束写进提示词（No music, SFX only）
6. 物理与微表演逐帧级显式

---

## 六、复用检查清单（KOK BORU 增补——AI 手绘动画专用）

- [ ] 帧率锁了吗？（True 12fps / on twos / held two frames）
- [ ] 笔触锁了吗？（painterly boil / 每帧重绘 / line jitter）
- [ ] 反 AI 平滑锁了吗？（NO interpolation / NO motion blur / NO morphing / NO melting）
- [ ] 双层时间声明了吗？（大气 smooth / 人物 stepped）
- [ ] 长提示词结尾复述风格锚点了吗？
- [ ] 每镜段末重申动画锁了吗？
- [ ] 微表演按帧写了吗？（眨眼 = 闭眼帧 in/out）
- [ ] 资产是否 AI 生成 + 人工手绘覆盖（文化准确性）？
- [ ] 是否有正式剧本随提示词一起喂（MCP 工作流）？
