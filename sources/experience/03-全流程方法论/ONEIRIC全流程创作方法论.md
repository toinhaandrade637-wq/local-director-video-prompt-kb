# ONEIRIC 全流程创作方法论

> **依据**：对 Higgsfield 官方长片 ONEIRIC（19:48，四大学生脑机接口"任意时空一日游"，三个类型片幻想各成 vignette）全部 41096 个生成任务、40791 条提示词（3247 条唯一文本）的完整逆向。137 个文件夹全数抓完、每文件夹游标到尽头。
> 这是**第五个体系、也是工业化的巅峰**：19 分钟长片、四个世界观（宿舍/特洛伊/太空/童话）、40K 生成任务——**大片量产的完整工程学**。

---

## 〇、项目画像

**故事**：四个大学生在宿舍讨论"Oneiric 技术"（大脑接入任意时空）——Bob 要去特洛伊战争亲眼见海伦，Sam 要做深空银河海盗，Rudie 要在童话世界当骑狮鹫的法师。每个幻想用**各自的类型片语法**展开。

**结构**（137 文件夹，工业级组织）：
- 12 个 SCENE 场（kitchen/livingroom/TROY/COSMOS/FAIRYTALE/LAB/TITLE SEQUENCE）
- 每场内 shot 级子文件夹（shot 1~8、Transition s5-s6、VO Bob）
- **ASSETS 资产大库按世界分子树**：ANIMALS（羚羊/蛇怪/蝴蝶/狮鹫/蜘蛛）、CHARACTERS（Main: Alfie/Bob/Rudie/Sam + Supporting: Ajax/Alien/医生/大猩猩/Helen）、EXTRAS（群演：童话王室/骷髅骑手/太空守卫/特洛伊军队——**群演也全部资产化**）、LOCATIONS（每个世界内的每个房间单独文件夹）、PROPS（每世界每道具）
- regenerations 实验区 + 每资产自己的 test 子夹

**模型分布**：seedance_2_0 ×19304（主力）+ soul_cinematic ×11093（场景资产）+ seedream_v5_pro ×2791 + nano_banana_2 ×2044 + gpt_image_2 ×1929 + text2image_soul_v2 ×1845 + seedance_2_5 ×292。

**时间线**：2026-06-24 ~ 08（36 天），日均 ~90 条唯一——**长片按日历稳定推进，无爆发期**，这就是连续剧式生产节奏。

---

### 0.5 整体画面风格（一眼认出 ONEIRIC 的视觉 DNA）

**看片感受**：anamorphic 宽银幕的"暖青撞色"大学宿舍——四个世界各有自己的调子但共享同一副 35mm 胶片的血脉：宿舍的暖乱、特洛伊的尘金、太空的深蓝机舱光、童话的森绿奇幻。当世界切换时，画幅不变，光变了。

**视觉 DNA 六要素**（词频来自 3,247 条唯一提示词）：

| 要素 | 定义 | 数据证据 | 提示词落法 |
|---|---|---|---|
| 底片 | 35mm + anamorphic 2.39:1 + 颗粒 | 35mm ×1345、anamorphic ×2173、2.39:1 ×710、grain ×1834 | 全片统一底色：anamorphic + 35mm + warm-and-teal grade |
| 四色世界 | 宿舍暖乱 / 特洛伊尘金 / 太空深蓝 / 童话森绿 | red ×2526、blue ×1502、green ×792、teal ×510、neon ×367 | 各世界在自己的 SCENE 文件夹内自定调色，但共享画幅与胶片声明 |
| 特洛伊专属 | VERY STRONG anamorphic 畸变 + 纵队士兵软焦 | OPTICS 段原文：heavily pronounced oval/elliptical bokeh, marked horizontal stretch | Bob sharp always; the massed battle, banners, haze and dust melt into very heavy soft anamorphic bokeh |
| 宿舍专属 | 107° 广角 rectilinear + 物体近大远小 | OPTICS 原文 | 107° diagonal field of view with a strong rectilinear wide-angle perspective ... straight edges remain straight, no fisheye |
| 童话专属 | Photoreal VFX + volumetric mist + 羽毛/布料物理 | STYLE 原文：Photoreal cinematic fantasy, feature-film VFX | realistic feather/fur/cloth/water dynamics, volumetric mist and light, strong sense of mass, scale and speed |
| 质感 | 毛孔皮肤 + POSITIVE LOCKS 收尾 | pore ×361、photoreal ×1301 | 每条以 POSITIVE LOCKS 正向锁收尾（identity stable / no ghosting / no flicker） |

**画面气质判词**：梦境感（dream ×353）是全片底色——VO 旁白缝合四个世界，画幅胶片是"现实层"，各世界的光色才是"幻想层"。

---


## 一、GLOBAL LOCK 体系（ONEIRIC 的核心发明，全库 380+ 个命名锁）

全大写、带名字、常带"READ FIRST / OVERRIDES THE REFERENCE"的**全局锁**，置于提示词最顶部：

```text
GLOBAL LOOK LOCK ×253     —— 全局外观锁
GLOBAL AUDIO LOCK ×203    —— 全局音频锁
GLOBAL RUDY LOCK ×127     —— 单角色锁
GLOBAL GRIFFON TAIL LOCK ×130 —— 单生物部件锁！
GLOBAL BASILISK LOCK ×122
GLOBAL MAX ANAMORPHIC LOCK ×53
GLOBAL RUDY HOOD-OFF LOCK ×32 / HOOD-ON ×5 / HOOD-UP ×11 —— 同一角色的状态锁细分
GLOBAL SPIDER-SIZE LOCK / SPIDER-ALREADY-FLYING LOCK / SPIDER-ALWAYS-BACK-TO-CAMERA LOCK
GLOBAL ULTRA-EXTREME-SLOW-MOTION LOCK
GLOBAL EYES-LEAD-THE-BODY LOCK ×14  —— 表演原则也做成锁
```

**三条工程学规律**：
1. **锁可以覆盖参考图**：`GLOBAL RUDY HOOD-ON LOCK — ABSOLUTE HIGHEST PRIORITY, READ FIRST (OVERRIDES THE REFERENCE): Rudy's reference image shows him BARE-HEADED — IGNORE / OVERRIDE that here. In THIS scene Rudy's large cloak HOOD is PULLED FULLY UP`——参考图错了不用重做资产，用锁覆盖
2. **锁按场景需求动态命名**：不搞一套固定模板，而是每个难题现场造锁（SPIDER-DUCK-DIVE 序列、CURSED-SPEAR 锁、MUSHROOM-DISINTEGRATION 锁）——**锁是问题驱动的，不是美学驱动的**
3. **复用锁有计数规律**：ASSET 锁（RUDY-ASSET/GRIFFON-ASSET ×13-14）在每个使用该资产的镜头重复出现——高频锁 ≈ 该片的核心难题（追逐场面锁最多：镜头几何/视线引导/时间提前量全被锁死）

---

## 二、八段标准结构（SCENE CONTEXT 到 POSITIVE LOCKS）

全库段落标签统计（3247 条唯一提示词）：

| 段名 | 出现 | 内容 |
|---|---|---|
| SCENE CONTEXT | 1191 | 这场戏一句话 + 基调 |
| ACTIVE REFERENCES | 1236 | 每个参考图 + 身份描述 + `100% matches the reference` |
| LOCATION MAP | 775 | **方位地图**：Camera 位于南端胸部高度朝北门，左墙=灶台+水壶+花窗帘，右墙=台面+水池+脏碗，地板=旧镶木，光从右侧窗 |
| FIRST FRAME / SPATIAL BLOCKING | 820/723 | 首帧精确构图 + 人物调度（0.5s 门开，人物从中景走向相机） |
| ACTION TIMING | 693 | 逐秒动作时序 |
| OPTICS / CAMERA | 816/825 | 光学段 + 运镜 |
| PHYSICS | 1177 | 物理段 |
| LIGHTING | 1324 | 光照段 |
| AUDIO | 1077 | 音频段（含 No music） |
| **POSITIVE LOCKS** | 1251 | **结尾正向锁段**：Exactly one person present, identity stable; window key stays screen-right; no ghosting, no flicker |

**方法论**：DETOUR 是六段式、KOK BORU 是首尾双声明，ONEIRIC 把它推到 **11 段流水线**——每段职责单一、全大写命名、几乎每条提示词都全。而且**结尾用 POSITIVE LOCKS 替代负面清单**（"identity stable"而不是"no identity drift"）——与 RED FLAG 的"正向形式 > 负面清单"结论跨项目互证。

---

### 2.5 ACTION TIMING 逐秒时间轴实战范本（投石机场景，官方原文）

    ACTION TIMING
    0.0–1.6s (SEG 1): Bob clambers up the catapult frame toward the cocked
    sling, timber creaking.
    1.6–2.8s: the Trojan grabs his LEGS, hauling down — Bob clings, kicks
    once, twice — the soldier tumbles off into the dust.
    2.8–3.6s: Bob settles into the sling pouch, grins, raises his sword.
    HARD CUT.
    3.6–4.4s (SEG 2): lungs full — "FULL SEND!" — the sword SLASHES the
    release rope.
    4.4–8.0s: the arm WHIPS, Bob LAUNCHES — screaming all the way, arms
    wide, the battlefield shrinking, one weightless blissful beat at the top
    of the arc — then over and DOWN, howl rising.
    HARD CUT.
    8.0–9.0s (SEG 3): the Trojan squad slams into the square shield
    formation, roof locked, braced, eyes up — the frame holds square below,
    sky above.
    9.0–10.2s: Bob FALLS INTO FRAME from above, screaming, growing from a dot
    to a plummeting body — and CRASHES onto the shield-roof...

**逐句拆解**：
1. **SEG 编号 + 时间窗**：单条生成内的分段也编号
2. **关键动词全大写**：SLASHES / WHIPS / LAUNCHES / CRASHES——每拍的动作核心词必须跳出来
3. **HARD CUT. 单独一行**：剪辑点自己占一行
4. **节奏的修辞**：one weightless blissful beat at the top of the arc（弧顶一拍失重的极乐停顿）——写节奏的呼吸，不只写位置
5. **构图写进时间轴**：the frame holds square below, sky above——每秒的画面安排都在时间轴里

### 2.6 AUDIO 段的声音角色工程（官方原文）

    AUDIO (timbre only — no words here)
    BOB's voice: warm boisterous American baritone with a light gravelly
    edge and big dynamic range, Jack Black-style — theatrical, playful,
    over-excited, punching key words and dropping into a mock-confidential
    murmur, a laugh under the words. Delivers only the scripted lines,
    nothing else.
    Battlefield wall of sound — clashing metal, shields, shouting, wind,
    dust; the catapult's timber CREAK under Bob's climb, the grabbing
    Trojan's grunts and his tumbling thud...

**声音四件套**：音色定义（声学特征）+ 真人参照（Jack Black-style）+ 表演方式（punching key words / mock-confidential murmur / a laugh under the words）+ 音效按时间轴排列（木材吱呀→闷哼→摔落闷响），并用 Delivers only the scripted lines, nothing else 防加戏。

### 2.7 GLOBAL LOCK 覆盖参考图的完整四要素（兜帽锁原文）

    GLOBAL RUDY HOOD-ON LOCK — SCENE 7, ABSOLUTE HIGHEST PRIORITY, READ
    FIRST (OVERRIDES THE REFERENCE): Rudy's reference image shows him
    BARE-HEADED — IGNORE / OVERRIDE that here. In THIS scene Rudy's large
    cloak HOOD is PULLED FULLY UP and OVER his head...

**四要素**：优先级声明（ABSOLUTE HIGHEST PRIORITY, READ FIRST）+ 覆盖声明（OVERRIDES THE REFERENCE）+ 指出参考图错误（shows him BARE-HEADED）+ 正确状态完整描述。**参考图与剧情冲突时，锁是修正器**——不重做资产，用文字覆盖。

---


## 三、 LOCATION MAP：用屏幕方位做构图（对示意图方案的文本化）

RED FLAG 用示意图图像锁几何，ONEIRIC 用**纯文本方位地图**：

```text
LOCATION MAP
Camera sits at the near (south) end of a narrow galley kitchen at roughly
chest height, facing the cream-painted back door in the deep background,
center, x50%.
Screen-left wall: gas hob with a grey kettle, oven below, stacked plates,
a red floral curtain, a dish rack.
Screen-right wall: a long counter under a daylit window, sink with tap...
Daylight enters from the window on screen-right; the rest sits in soft teal shade.
```

**要点**：机位（方向+高度+朝向）→ 逐面墙的物件清单 → 光源方位。**x50% 百分比坐标**直接给出。配合 FIRST FRAME（首帧即定稿帧）与 SPATIAL BLOCKING（0.5s 门开、人物从背景中心 x50% 走向相机）——**时间轴写进空间**。

---

## 四、群演资产化（大片规模战斗的实现方式）

群演不是"一队士兵"，而是**全部走 ASSETS/EXTRAS 子树**：Troy/Army、Troy/Escort、Fairytale/Royal Family、Fairytale/Royalguard、Fairytale/Sceleton riders、Space/Guards、Space/Robots、Space/Guard command——每个群演单位一个文件夹、独立资产表，镜头里整队引用。

群演镜头写法（Army 实例）：
```text
SCENE CONTEXT: A line of Greek soldiers advances straight toward camera
across the plain. Partway through, Bob joins their ranks from the side.
They all march forward with grim resolve, then raise their swords and
spears and roar a battle cry to charge. Single continuous take.
OUTPUT SETTINGS: Single continuous take. Real-time motion. No subtitles, no music.
```
——**主角混入群演队列**的调度写明（"Bob joins their ranks from the side"），群演统一动作（march→raise→roar→charge 三拍）。

---

## 五、类型片语法切换（一个项目里跑四种风格）

统一底色：anamorphic ×2173、35mm ×1345（全片宽银幕胶片感）+ warm-and-teal grade。
各世界在上面叠自己的类型语法：
- **宿舍**：grounded handheld realism（手提纪实）
- **特洛伊**：史诗战争（冲锋扬尘、长矛军旗、"camera shakes"）
- **太空**：cylinder hall 里的科幻构图（前景虚焦机械臂+背景伤者）
- **童话**：奇幻追逐（BASILISK/GRIFfon/SPIDER 生物追逐 + ULTRA-EXTREME-SLOW-MOTION 喜剧时刻）

**VO 旁白体系**：voice-over ×59、off-screen voice ×82、V.O. ×26——场景间用 VO 缝合（VO Bob / VO Sam 文件夹）。

---

## 六、五体系对照总表（本工作区全部研究的集大成）

| 维度 | DETOUR | ZEPHYR | RED FLAG | KOK BORU | ONEIRIC |
|---|---|---|---|---|---|
| 定位 | 独立·街头动作 | 官方·IMAX纪实 | 官方·黑色电影 | 官方·手绘动画 | 官方·19min长片 |
| 规模 | 5.5K | 4.8K | 3.5K | 2.7K | **41K** |
| 结构 | 多级分类 | 扁平 | 场景文件夹 | 每镜头一夹 | **世界/资产/群演/shot 四级树** |
| 核心武器 | 负面空间约束 | 风格前缀参数化 | 正向色彩分配+示意图 | 帧率锁+双层时间 | **GLOBAL LOCK 体系** |
| 负面形式 | Avoid 清单 | NEGATIVE 段 | 正向>负面 | 反AI平滑锁 | **POSITIVE LOCKS 收尾** |
| 几何控制 | 文字方位 | 附件顺序 | 示意图图像 | —— | **LOCATION MAP 文本方位+x%坐标** |
| 提示词中位 | 3.9K | 3.9K | 2.2K | **10.1K** | 4.3K |
| 语言 | 英 | 英 | 中英混写 | 英 | 英 |
| 周期 | 22天 | 3天+实验 | 10天 | 45天 | **36天稳定推进** |

**五体系共同的铁律（最终版）**：
1. 风格段成段复用（前缀/锚点/复述，位置随体系而变）
2. 一致性 = 元素引用 + 命名（@tag / <<<ID>>>）+ 控制边界声明
3. **正向形式 > 负面清单**（RED FLAG 色彩战争 + ONEIRIC POSITIVE LOCKS 双重确证）
4. 每个"模型默认行为"都要显式对抗（慢动作/平滑/色彩漂移/插值）
5. 物理与微表演逐帧显式
6. 音频约束写进提示词
7. **锁/约束是问题驱动的**：遇到什么问题就造什么锁（ONEIRIC 的 380 个锁全是有故事的）

---

## 七、复用检查清单（ONEIRIC 增补——长片工程）

- [ ] 复杂状态是否用 GLOBAL LOCK 覆盖参考图（而不是重做资产）？
- [ ] 长片是否按世界/角色/群演/道具/每镜头的四级树组织？
- [ ] 群演是否资产化（每队一文件夹一资产表）？
- [ ] 构图是否用 LOCATION MAP（机位方位+逐墙清单+x% 坐标+光源方位）？
- [ ] 是否定义了 FIRST FRAME（首帧=定稿帧）？
- [ ] 调度是否写进时间轴（0.5s 门开，人物从 x50% 走向相机）？
- [ ] 结尾是否用 POSITIVE LOCKS 正向收尾（替代散装负面词）？
- [ ] 多类型片切换时统一底色（画幅/胶片/调色）是否声明？
- [ ] 长片节奏是否日均稳定推进（不靠爆发）？
- [ ] 每个追逐/动作难题是否现场造了命名锁？
