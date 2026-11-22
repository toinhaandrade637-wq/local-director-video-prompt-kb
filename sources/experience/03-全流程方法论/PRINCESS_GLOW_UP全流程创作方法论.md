# PRINCESS GLOW UP 全流程创作方法论

> 社区项目 @ailaa · 精英学院素颜奖学金女生"变身"短剧系列（5 集 + 万圣节特辑）
> 数据底座：2,298 job 全量（零丢失，官方面板"生成记录 2 298"直接印证）/ 2,291 带提示词 / **438 条唯一去重提示词**
> 捕获 2026-10-27

## 〇 项目档案

| 项 | 值 |
|---|---|
| 链接 | https://higgsfield.ai/zh/@ailaa/projects/princess-glow-up |
| 体量 | 生成记录 2 298 · 消耗积分 655 477 · 项目 69.9 GB · 浏览 4 506 · 赞 67 |
| 剧集 | Ep1 2:23 / Ep2 2:27 / Ep3 2:59 / Ep4 2:46 / Ep5 2:52 / Halloween party 2:53 |
| 技术栈 | Seedance 2.5 **93.5%**（2,109/2,298）+ text2image_soul_v2 41 · gpt_image_2 38 · soul_cinematic 22 · nano_banana_2 21 · seedream_v5_pro 14 等（+9） |
| 文件夹 | ROOT 主创作区 1,994 · 1-5 episode（40/15/43/19/90）· EP1 Vertical 9x16 tracking prompt 14 · assets 83 · 2 个剪辑夹（video_input） |

**实测 vs 官方计数对账**：文件夹计数总和 2,310 = 2,298 个生成 job（全部捕获）+ 8 个 video_input 上传参考素材（无提示词）+ 4 条跨文件夹引用重复计数。**零丢失**。7 条 job 服务器端 prompt=null（与 DETOUR Props 同性质）。

## 〇.5 整体画面风格 DNA（词频实测 + 官方声明双证）

**官方 Style Prefix 逐字**（brief 原文）：

> Soft K-drama pastel look — bright diffused daylight, palette of peach, powder blue, cream, gold and pink marble, gentle low contrast, natural skin texture with visible pores and no beauty smoothing, very light grain, unhurried stillness. 50mm lens feel, soft background bokeh. Naturalistic, intimate. Steady, level, well-composed framing — flat true horizon, no tilt; the camera holds still and lets a moment breathe.

**官方 Visual Constraints 逐字**（节选）：

> Photoreal live-action — no 3D render, no game-engine gloss, no cartoon or anime read. Hard positive locks in every prompt: headcounts, seating and screen geography, prop states, screen-direction, and wardrobe continuity are written into the prompt, not left to chance. Faces blink and breathe, never masklike… Enju's face stays bare and unretouched until the glow-up… No music. Only SFX.

**词频实测**（2,152 条视频提示词，去停用词 top）：`shot:45,210 · one:32,319 · image:26,063 · frame:25,779 · face:25,322 · eyes:25,198 · camera:24,591 · back:22,073 · chen:21,449 · him:19,424 · ryan:18,319 · two:18,084 · enjee:17,695 · white:16,693 · behind:16,312`

词频印证三大风格特征：① `shot` 均值每条 20+ 次——**每条提示词就是一支多镜头微短片**（非单镜头）；② `image` 高频对应 93.5% 的提示词带 `<<<image_N>>>` 标签引用；③ `face/eyes` 高位对应"表演发生在眼睛里"的表演任务体系；④ 四位主角人名全部进 top20——**角色名即锁定符**。

**实测差异提示**：官方声称 Style Prefix 段"opens every prompt"，但 2,298 条实测 0 命中该词组——Style Prefix 实际存在于其 Claude 提示词构建 skill 的系统层，**不写进生成提示词本体**。学其体系时应把它当作"全局常量"另置，而非逐条粘贴。

## 一 工作管线（官方 brief 逐字整理）

1. **参考资产先行**："Every character, prop and location in the series is locked to an actual reference photo"——Enju 素颜三视图转台、变装后转台、Ryan/Chen/Jenny 各双造型、女生群像 mood board、场地空镜（cafeteria/atrium/corridor/bedroom）。连续性锚帧也打标（cafeteria master two-shot、staircase group blocking），返场场景**从图片重建而非凭记忆**。
2. **标签引用制**：`@image1 through @image19+`，按标签拉入任何需要的提示词，并明令"never to re-describe or expand the environment beyond what the photo already shows"。
3. **两大风险点（官方自述）**：① **场地漂移是最大单一风险**——"given a pastel palace, the model's instinct is to make it grander"（加吊灯、加宽大厅、食堂饭变餐厅菜），靠 location lock 压制；② **服装串 borrow**——"an unlocked background extra will quietly borrow a named character's silhouette"。
4. **系统提示词工作流**："we write our system prompts in a Claude chat loaded with a custom Seedance 2.5 prompt-building skill, alongside the full script"——全剧本 in-context，"a shot knows what beat it's serving, what just happened, and what the character is feeling"。
5. **音频策略**：生成期"No music. Only SFX."，音乐后期另做。

## 二 提示词结构：14 段式多镜头模板（全站最规整）

段头实测频次（2,298 条）：`ACTIVE REFERENCES 2,050 · SCENE 2,048 · FORMAT 2,033 · POSITIVE CONSTRAINTS 1,969 · LIGHTING 1,967 · QUALITY 1,962 · FIRST FRAME 1,938 · PHYSICS 1,904 · LOCATION 1,609 · ACTION 1,416 · ACTING TASK 224`。SCENE CONTEXT 开头 1,448 条（63%）；视频提示词长度中位 **15,429 字符**、P90 24,741、最长 43,155。

标准段序（万圣节舞会样本，7,629 字符）：

```
SCENE CONTEXT        场景语境：一句交代时空与剧情节点
ACTIVE REFERENCES    <<<image_1..5>>> 逐角色"100% match the reference"锁定（含"非主角勿认领"条款）
LOCATION MAP         空间地图精确到米（"dance floor about 30 m long""doorway…about 25 m"）
CROWD DIRECTION      群演调度："They react one by one, never in sync."
FIRST FRAME          首帧画面逐元素定义
FORMAT MODE          "Multi-shot sequence, 20 seconds, hard cuts."
ACTION TIMING        SHOT 1..8 逐镜：秒数区间 + 机角度数（47°/63°/84°）+ 台词原文
ACTING TASK          每角色四要素表演任务（见 §三）
PHYSICS              重量与机械真实（人群密度、聚光灯机械 pan、披风摆动）
LIGHTING             光源清单 + "no flat front light"
AUDIO                音效清单 + "exact lines only, one speaker at a time" + 声线设定
STYLE                风格一句话（"Glossy teen K-drama party scene…"）
QUALITY              180 度快门节奏、运动模糊解析、no ghosting/flicker/重复肢体
POSITIVE CONSTRAINTS 硬性正锁定：人数、唯一性（"Jenny is the only bunny"）、屏幕地理
```

**机角度数语法**：47°（中近特写）/ 63°（过肩或低角）/ 84°（大全景俯视）——三档度数复用贯穿全项目，是自建的可复现机位语言。

## 三 ACTING TASK 四要素表演语法（本项目独家强项）

每个出场角色一段：`MOTIVE（动机）→ GOAL（目标）→ OBSTACLE（障碍）→ TACTIC（策略）`，附官方安全网条款：

> (Safety: gaze always engaged in the task — never a frozen, glassy, unfocused stare; natural blink cadence, actors blink now and then to moisturize their eyes.)

样本逐字（Chen）：

> CHEN — MOTIVE: the person this whole night is for hasn't come. GOAL: find Enjee in the crowd. OBSTACLE: a sea of faces in the dark. TACTIC: he scans row by row; for a second he gives up — then the sight of her at the door wipes everything else away.

与 THE_TRIGGER / HELL_GRIND 的表演体系同源但更规整——**把"表演课斯坦尼斯拉夫斯基动作分析"直接写进提示词**，是三项目共证的"AI 导演给演员说戏"范式。

## 四 官方风格铁律（brief 逐字可复用）

1. 场地只渲染参考图所示，"never widened, re-furnished or made grander; the cafeteria stays a school canteen with orange compartment trays inside a grand hall, never a restaurant"。
2. "Background students stay in soft focus inside their own conversations and never look at camera."
3. "Slow motion appears only where scripted and returns to full speed on a hard cut, never a ramp."
4. "Dialogue is only the exact scripted lines, one voice at a time, delivered at ordinary conversational pace with real pauses."
5. "No music. Only SFX."（音乐后期；音效点名：fog-muffled ambience / distant rifle crack / breath / footsteps on wet ground / crowded corridor hum）
6. "Ryan's watch stays an ordinary object in ordinary light — no glint, no bloom, no push-in."（反 AI 滤镜倾向条款）

## 五 与既有体系的关系

- **场地锁定** ← HELL_GRIND cinedance_v4 的场地纪律 → 本项目升格为 `LOCATION MAP` 独立段（米制空间地图）。
- **表演四要素** ← THE_TRIGGER tig-acting / HELL_GRIND ACTING_SYSTEM → 本项目同构 MOTIVE/GOAL/OBSTACLE/TACTIC，为三重印证的通用范式。
- **多镜头 ACTION TIMING** ← PASSPORT_RUSH 16 段式 → 本项目收敛为 14 段式 + 秒表级分镜（SHOT 1..N 每镜带时长区间与硬切点）。
- **参考图标签** ← RED_FLAG / DETOUR 的 `<<<image_N>>>` 同款语法，本项目做到 93.5% 覆盖率（2,150/2,298）。

## 六 可复用清单

1. **14 段式模板**（§二段序）——多镜头短片提示词的完整骨架，可直接换皮。
2. **三档机角度数语言**（47°/63°/84°）——自定义可复现机位词表。
3. **ACTING TASK 四要素 + Safety 条款**——每角色一段，防"玻璃眼"呆滞 stares。
4. **LOCATION MAP 米制空间地图**——防场地漂移的最强实践（官方自述第一风险）。
5. **POSITIVE CONSTRAINTS 唯一性条款**——"X is the only Y"句式防群演抢主角轮廓。
6. **反美化三连**：no flat front light / no glint no bloom no push-in / never make it grander。
7. **Style Prefix 全局常量化**——系统层定义不进提示词本体（实测 0 命中的教训）。
8. **抽卡经济学**：2,298 job → 438 唯一提示词（≈5.2 倍抽卡率），同配方多抽选优是 AI 短剧常态，数据包两层均保留。
