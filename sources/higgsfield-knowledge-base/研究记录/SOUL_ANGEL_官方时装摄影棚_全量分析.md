# SOUL_ANGEL 全量分析（官方 Originals · soul 团队时装摄影棚片）

> 收割 #4（E158）｜全量 500 资产（唯一 93，迭代率 5.4×）
> 模型：default×287 / ?×209 / videotape-alpha×2（schema 无明确模型标注，需按内容判型）
> 团队：soul（四官方账号之一）

## 块头分类学（count_blocks.js 口径）

ACTING TASK×846 / TACTIC×846 / OBSTACLE×834 / MOTIVE×444 / FORMAT. 4×265 / SHOT 1-8×~1,600 / CUT LIST×72

**ACTING TASK 占比 = 全库最高**（846/500≈1.7 块/条）。每条提示词含 ACTING TASK + TACTIC + OBSTACLE 三联块（表演任务三件套），MOTIVE 约半数出现。

## 代表 prompt 分析（25,040 字符）

SCENE CONTEXT（SOUL photo studio / Lucy walk-in / 23 seconds / ELEVEN shots / ten hard cuts）→ ACTIVE REFERENCES（6 个 <<<image_N>>> UUID 标签：Lucy/Raphael/Luca/French导演/造型师/化妆师，每人外观档案+保真契约）→ **VOICES 块**（French accent 逐角色声音立法：`r's softened and made at the back of the throat, "th" leaning toward a soft "z"`）→ ACTING TASK（23 秒 11 镜逐镜分解）→ TACTIC/OBSTACLE（表演约束）→ SHOT 1-11（每镜块含 camera position/framing/action）→ CUT LIST（硬切清单）

### 特色发现

1. **VOICES 块**：口音逐音素立法（r 的喉音化/th 的 z 化/元音圆唇化）——ANERNEQ/VENGEANCE 无此维度
2. **ACTING TASK 超密度**：每条提示词 1.7 个 ACTING TASK 块，全库最高
3. **多角色（6 人）**：远超其他项目的 2-3 角色
4. **CUT LIST 独立块**：剪辑清单独立成块（其他项目在 ACTION TIMING 内联）
5. **FORMAT. 4**：格式声明带小数点编号——多格式并行

## 结论 → K 页生长

SOUL_ANGEL 的 **ACTING TASK 超密度**和 **VOICES 声音立法块**是两个新发现。ACTING TASK 密度已确认（结构化模板 soul 团队标配）。VOICES 块是新维度——声音/口音逐音素立法，当前 K05（已作废）覆盖了 audio 策略但重建时需纳入 VOICES 块模式。

**方法重建状态**：本批 raw_analysis_done ✅ / method_rebuilt ⏳（视频轨待重建时以本笔记 verbatim 为源素材）
