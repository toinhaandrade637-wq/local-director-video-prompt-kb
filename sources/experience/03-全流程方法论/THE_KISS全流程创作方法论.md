# THE KISS 全流程创作方法论

> 社区项目 @seifhussam · 社区榜赞数第 1（1210 赞 / 61,447 播放）· AI Film Festival 参赛 top50 · 3.6 分钟恐怖短片
> 数据底座：391 job 全量（零丢失）/ 383 带提示词 / **206 条唯一去重提示词** / 捕获 2026-10-27

## 〇 项目档案

| 项 | 值 |
|---|---|
| 链接 | https://higgsfield.ai/zh/@seifhussam/projects/the-kiss |
| 数据 | 官方计数 393 = 391 job + 6 非 job 上传件；图 282 / 视 109 |
| 结构 | ROOT 17 · Test_Images 229 · Test_Videos 94 · Characters 17 · Props 14 · Locations 8 · Editing 7 · Watermarks 4 · Scene_01/02/03/05 |
| 模型 | nano_banana_2 161（41%）· seedance_2_5 94（24%）· soul_cinematic 38 · text2image_soul_v2 36 · seedream_v5_pro 22 · gpt_image_2 19 等 11 种 |

## 〇.5 创作主题 DNA（官方 brief 逐字）

> This project explores a feeling that all of us have experienced and understand: jealousy.
> Sometimes, a person can become jealous of you even when you have done absolutely nothing to them… it can slowly turn into hatred — to the point where they may even wish you were gone.
> What begins as two brothers simply playing a game together and trying to win gradually turns into conflict, resentment, and eventually a situation where one of them wants to get rid of the other.

一句话：**"嫉妒"作为整部片子的唯一引擎**——母亲的一个外部动作点燃两兄弟的嫉妒，游戏演变成杀意。Logline（官方原文）：One brother got the kiss. The other got a phone ringing — and a nightmare built out of everything he was afraid it meant.（获奖短片公式：单一情绪 × 家庭场景 × 恐怖类型外壳。）

## 一 工作管线（实测数据还原）

1. **先图定调、后视频生成**：图像模型 job 占 282/391（72%），nano_banana_2 一家 161 条——用图像模型反复试角色/场景/氛围（Test_Images 229 张），锁定后再进 seedance_2_5 出视频（94 条）。
2. **抽卡经济学**：391 job → 206 唯一提示词（1.9 倍抽卡率），Test_Videos 94 条即同配方多次生成的产物。
3. **六大素材夹**：Characters / Props / Locations / Editing / Sound / Watermarks——官方工作区模板（与 Higgsfield Studio 12 部同构），Sound 夹仅 1 条上传件（音效后期做）。
4. **测试留痕**：Test_Images/Test_Videos 不删——整个探索过程在项目里可回放，本身就是"提示词炼金日志"。

## 二 与既有体系的关系

- **官方工作区模板** ← Higgsfield Studio 12 部的 Characters/Locations/Props/Scenes 夹结构 → 社区作者直接沿用，说明官方模板已内化为社区标准工作流。
- **抽卡率对比**：PRINCESS_GLOW_UP 5.2 倍（逐镜多抽选优）vs 本片 1.9 倍（探索型抽卡为主）——剧情短片（多集）与 3 分钟单线短片的抽卡结构差异。
- **11 种模型混用**：本项目是库内模型种类最多的项目之一（11 种），含 cinematic_video_editor（后期编辑模型）与 Watermarks 夹——记录了从生成到成片的完整工具链。

## 三 可复用清单

1. **单一情绪引擎**：一部 3 分钟短片只讲一种情绪（jealousy），brief Context 全文只写情绪的演化链——评委可一句话复述。
2. **先图后视**：图像模型定调（占比 72%）→ seedance 出片，图像试错成本远低于视频。
3. **测试区公开**：Test_Images/Test_Videos 留存=提示词迭代日志，学习者可直接看"哪条配方被选中"。
4. **家庭场景 × 恐怖类型**：日常物（电话、游戏）作为恐怖载体，低成本高共鸣。
