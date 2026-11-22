# HELL GRIND 全流程创作方法论

> **依据**：对 Higgsfield 官方 96 分钟长片 HELL GRIND（115,451 资产，全平台第二大项目）的分层抽样完整逆向——Assets 前期制作 + COLD OPEN + Flashbacks + 13 个战斗/关键场景 + Series 序列片全量或样本，合计 10,486 个 job、10,469 条提示词（1,861 条唯一文本）逐类精读。
> 这是**第八个体系**：奇幻动作悲剧——与 ADILIADA 的喜剧戏仿相对，它示范**奇幻生物体系 + 尺寸工程 + 悲剧节奏**怎么做。

---

## 〇、项目画像

**故事**：博物馆偷窃夜，Roko 触发无名古物分裂四片，四人各获之力；骨甲恶魔掳走怀孕的 Lulu 入地狱。Roko 为救她穿越地狱、跨过界限（杀死守护者）、被朋友隐瞒背叛、独行至终局。官方 brief 定调：**"奇幻即悲剧，动作即悲恸，友谊是人与他正在变成的东西之间最后一道防线。"**

**规模**：96 分钟；115,451 资产；2026-04-06 启动（全工作区最早），32 天密集生产；1,861 条唯一提示词中位 3,851 字、最长 38,823 字。

**结构**（162 文件夹）：Assets（前期制作 16 夹）→ Scene 1-74（含 Fight/Fall/Assault/vs 战斗标记）→ Flashbacks（回忆层 8 夹）→ Regenerations → Series（序列片 6 夹）→ Credits。

**模型**：seedance_2_0 ×5568 主力 + nano_banana_2 ×2450 + soul_cinematic ×854 + imagegen_2_0 ×699 + gpt_image_2 ×267。

**三语**：英文 1,624 / 中文 145 / 俄语 92——继 CHB 后再次验证多语言分工。

---

## 〇.5、整体画面风格（一眼认出 HELL GRIND 的视觉 DNA）

**看片感受**：一场被 Kodak 胶片颗粒包裹的地狱弥撒——16mm/35mm Kodak 500T 的厚重颗粒压在每一帧上，Lubezki 式手持跟着四个街头少年冲进博物馆；恶魔是紫罗兰皮肤里透着电蓝裂纹的三米巨人，回忆段落是孤儿院天窗下的逆光剪影，全片泡在阴天雾霭与深红水晶光里。

**视觉 DNA 六要素**（词频来自 1,861 条唯一提示词）：

| 要素 | 定义 | 数据证据 | 提示词落法 |
|---|---|---|---|
| 底片 | 16mm/35mm Kodak 500T + 厚颗粒（回忆用 16mm 更粗） | 35mm ×808、Kodak ×558、grain ×821、halation ×180 | `16mm Kodak 500T, heavy grain`（Flashbacks）/ `35mm Kodak 500T, Lubezki handheld`（正片）——**同胶卷两种画幅区分回忆与现实** |
| 摄影师 | Lubezki × Deakins 双引用 | Lubezki ×745、Deakins ×499 | `Lubezki handheld. Natural light only from clerestory windows — contre-jour, characters backlit, faces in shadow` |
| 光线 | 自然光 + 天窗逆光 + 阴天雾 | 全 STYLE 段：natural overcast light only, contre-jour backlit, haze and smoke throughout every frame | 逆光剪影是默认：`characters backlit, faces in shadow`——**脸在阴影里是风格不是事故** |
| 色彩 | 现实=青灰雾调；地狱/恶魔=紫罗兰+电蓝裂纹+深红水晶 | crimson ×241、gold ×474、teal ×101、demon ×223 | `During crystal growth deep crimson light`——色彩按**剧情物件**（水晶）点亮 |
| 质感 | 手持 + 雾 + 烟贯穿每帧 | handheld ×867、bone ×500 | 骨甲恶魔的 `bone` 是最高频质感词——**生物设计决定材质词汇** |
| 情绪判词 | dark ×1274（全库最高密度） | 悲剧基调 | 正片提示词的 SCENE CONTEXT 常以情绪结局收尾 |

**画面气质判词**：奇幻恐怖的华美 + 少年草根的粗粝——3 米紫皮恶魔的电蓝裂纹与街头少年的红色连帽衫同框，这种**尺度与质感的碰撞**就是本片的画面签名。

---

## 一、奇幻生物体系：从资产到尺寸工程（本片独有价值）

### 1.1 恶魔资产的定义法（Cold_open_B 38,823 字范本，官方原文）

    EXACT 2 CHARACTERS

    <<<160c936b...>>> [img_soroh] — Tall lean demon figure approximately 3
    meters tall (~300 cm) — comparable in height to other demon characters in
    the cold open, only slightly shorter than the 3.5 m Monster (about 50 cm
    height difference). PURPLE-VIOLET skin marked by dark blue vein-like
    cracks running across body and face. Bald shaved head crowned with twin
    elaborate curved horns rising back from the temples on an ornate
    dark crown-like base. Glowing electric-blue eyes with luminous internal
    light. Wears flowing dark drapery/robes wrapped around the lower body,
    bare chest exposed showing tribal skin patterns. No armor. LEFT
    HAND/FOREARM is special — the skin is heavily charred and blackened,
    cracked open like obsidian, with electric-blue lightning energy glowing
    through the cracks pulsing along his forearm and fingers. Right hand is
    normal purple-violet skin with claws. Calm, deliberate, power type —
    never wastes movement. CHARACTER REF — appearance only.

**逐句拆解——奇幻生物定义的九要素**：
1. **EXACT 2 CHARACTERS** 开头第一行锁人数——生物场面人数失控是头号敌人
2. **精确高度 + 相对高度**：`approximately 3 meters tall (~300 cm) — comparable in height to other demon characters, only slightly shorter than the 3.5 m Monster (about 50 cm height difference)`——**每个生物的高度都锚定在其他生物上**（差 50cm 都写明），这是 449 条高度标注的体系
3. **皮肤即故事**：PURPLE-VIOLET 底 + dark blue vein-like cracks——颜色分层写（底色+裂纹色）
4. **发光规则**：Glowing electric-blue eyes with luminous internal light——**哪些部位发光、发什么光、光从哪来**（internal）
5. **不对称设计**：LEFT HAND/FOREARM is special——charred + obsidian + 电蓝闪电脉动；Right hand is normal——**一半焦黑一半正常**，标志性设计单独点名
6. **行为气质**：Calm, deliberate, power type — never wastes movement——生物的性格写进资产定义（从不浪费动作=每次动作都致命）
7. **引用边界**：CHARACTER REF — appearance only——参考图只管外观
8. **禁止项**：No armor——防模型自作主张加装备
9. **着装**：flowing dark drapery——下身暗布上身赤裸 + tribal skin patterns

**方法论**：奇幻生物不是"画个酷怪物"——是**高度锚定体系（449 条 cm 标注）+ 皮肤分层 + 发光规则 + 不对称标志 + 行为气质**五件套。每个生物至少有一个"专属错误不可能"的不对称特征。

### 1.2 尺寸工程：多生物同框的透视控制

全库 449 条精确高度标注的规律：
- **主角 vs 恶魔**：人类 170-180cm vs 恶魔 300cm vs Monster 350cm——**三档尺寸体系**
- **相对差写明**：不只是"很高"，是"比 Monster 矮 50cm"——模型需要相对值才能在群像中保持透视
- **同框声明**：EXACT 2 CHARACTERS / EXACT 4 CHARACTERS 开头锁人——生物战斗场面的人数上限

---

## 二、Flashbacks 回忆层：同片双画幅（16mm vs 35mm）

回忆段 413 条的独立风格系统（官方 STYLE 行原文）：

- **回忆**：`16mm Kodak 500T, heavy grain, natural overcast light only, contre-jour backlit, haze and smoke throughout every frame`——**16mm 更粗颗粒**，天窗逆光，孤儿院场景
- **正片**：`35mm Kodak 500T, Lubezki handheld`——35mm，博物馆/地狱

**方法论**：**同胶卷型号、不同画幅**区分时空层——比换胶卷更微妙：观众能"感到"回忆更粗糙，但两者同属一部片的色彩血缘。中文写法也用于回忆（YoungRoko 中文资产定义：`男孩，深色波浪发及耳，红色连帽衫，黑色工装裤，红白Jordan球鞋，肩上一个红色旧布包，脸颊泪痕，瘦削`——**童年角色用中文写**，微表演细节更密）。

---

## 三、视频提示词结构

### 3.1 段落统计

SCENE CONTEXT ×106、STYLE ×300、LOCK ×252、AUDIO ×162、beat ×510（beat 结构近三分之一）、lip ×693（口型密度高——对白驱动叙事）、POSITIVE ×11（少量）。

### 3.2 对白与口型

693 条含 lip 描述——本片对白密集（悲剧靠台词推进）。写法沿用 CHB 的 AUDIO 声音角色体系：台词 + 声音 timbre + 口型同步三件套。

### 3.3 中文大场面动作（145 条）

与 CHB 同模式：中文写枪战/打斗/多生物混战——动作链与微表演的密度优势。

---

## 四、八体系对照总表

| 维度 | DETOUR | ZEPHYR | RED FLAG | KOK BORU | ONEIRIC | ADILIADA | CHB | HELL GRIND |
|---|---|---|---|---|---|---|---|---|
| 定位 | 街头动作 | IMAX 机甲 | 港式黑色 | 手绘史诗 | 长片工程 | 戏仿喜剧 | 音乐犯罪 | **奇幻悲剧** |
| 规模 | 5.5K | 4.8K | 3.5K | 2.7K | 41K | 11.3K | 473K | **115K** |
| 生物/怪物 | — | 机甲 | — | 狼 | 群演 | 外星人 | 群演 | **双恶魔尺寸体系** |
| 画幅分时空 | — | — | — | — | — | — | DV段 | **16mm回忆 vs 35mm正片** |
| 高度工程 | — | — | — | — | SCALE房定标 | — | — | **449条cm锚定** |
| 语言 | 英 | 英 | 中英 | 英 | 英 | 英 | 俄中英 | **英中俄** |
| 周期 | 22天 | 3天 | 10天 | 45天 | 36天 | 36天 | 54天 | **32天**（最早启动） |

**八体系终极铁律（含本片新增）**：奇幻生物=五件套（高度锚定+皮肤分层+发光规则+不对称标志+行为气质）；时空分层可用同胶卷换画幅；多生物同框开头锁 EXACT N CHARACTERS。

---

## 五、复用检查清单（HELL GRIND 增补）

**奇幻生物**：
- [ ] 高度锚定了吗（绝对cm + 相对差）？
- [ ] 皮肤分层了吗（底色+裂纹/纹理色）？
- [ ] 发光三问了吗（哪里发光/什么光/光从哪来）？
- [ ] 有不对称标志特征吗？
- [ ] 行为气质写了吗（power type / never wastes movement）？
- [ ] 引用边界（appearance only）+ 禁止项（No armor）写了吗？

**时空分层**：
- [ ] 回忆与现实是否同胶卷换画幅（16mm vs 35mm）？
- [ ] 回忆角色是否用中文写微表演？

**多生物场面**：
- [ ] EXACT N CHARACTERS 开头锁人了吗？

**悲剧节奏**：
- [ ] SCENE CONTEXT 是否以情绪结局收尾？
