# DON'T POISON IVY 全流程创作方法论

> 社区项目 @joeysnoisygroup · Higgsfield 精选 · 1069 赞 / 62,413 播放 · 无对白风格化 3D 动画短片
> 数据底座：553 job 全量（零丢失）/ 552 带提示词 / **490 条唯一去重提示词** / 捕获 2026-10-27

## 〇 项目档案

| 项 | 值 |
|---|---|
| 链接 | https://higgsfield.ai/zh/@joeysnoisygroup/projects/don-t-poison-ivy |
| 对账 | 官方 608 = 553 job + 40 audio_input（Score 夹音乐件）+ 15 上传件；图 150 / 视 403 |
| 模型 | seedance_2_5 402（73%）· seedream_v5_pro 88 · nano_banana_2 62 · cinematic_video_editor 1 |
| 团队 | KY / BYDANY / MARYPAUL 编剧，JOEY 导演（brief 尾制作名单） |

## 〇.5 创作方法 DNA（官方 brief 章节）

该 brief 是社区项目里**结构最完整**的之一（多数作者只填 Context，本项目填满 LOGLINE / THE WORLD / THE FILM / THEME / LOOK / BUILDING IT / THE MEMOJI PROBLEM 等），含大量 @引用（@cityview、@home-coda-plants、@living-room-reverse、@girl-black-hoodie——参考资产命名工程学）。核心章节：

- **LOGLINE** + 风格声明："Stylized 3D animated. No dialogue."——**无对白**是本片第一约束，全部叙事靠画面与音乐（Score 夹 40 条音乐生成提示词支撑）。
- **THE MEMOJI PROBLEM**：用 Memoji 风格角色引发的风格难题及其解法（详见 brief 全文）。
- **BUILDING IT**：场景搭建实录（客厅等 @tag 引用锁定）。

## 一 工作管线（实测）

1. **视频主导**：seedance_2_5 占 73%（402 条）——与 THE_KISS 的"先图后视"（图像 72%）相反，本项目视频直出为主，图像模型仅用于角色/道具定调（seedream_v5_pro 88 + nano_banana_2 62）。
2. **无对白纯视觉叙事**：提示词内嵌完整场景描述（每条自成一体，不用 SCENE CONTEXT 段式），依赖 @tag 引用保持连续性。
3. **音乐也是生成的**：Score 夹 40 条 audio_input——音乐不后期外包，用站内音乐模型按镜头情绪生成（job 类型带 prompt，已入库）。
4. **抽卡率 1.1 倍**（553→490）：高命中工作流，与团队分工制（编剧/导演分名）匹配——先写好再生成，极少废片。

## 二 与既有体系的关系

- **@tag 引用锁定** ← RED_FLAG/DETOUR/PRINCESS 的 `<<<image_N>>>` 语法 → 本项目用 @handle 式资产名（@cityview、@living-room-reverse），命名即语义。
- **无对白约束** ← NALA_HEADS_DROP（全 AI 音乐 MV）→ 本片"音乐承载叙事"的姊妹实践。
- **官方工作区六夹模板**（Characters/Locations/Props/Score/Watermarks/Video Generations）完全沿用 Studio 体系。

## 三 可复用清单

1. **无对白短片公式**：Stylized 3D + No dialogue 声明置顶 → 全部叙事压到画面构图与配乐。
2. **@tag 资产命名法**：`@场景-细节` 格式（@home-coda-plants），引用即锁图。
3. **THEMEMOJI 问题意识**：风格化角色（Memoji 系）与写实质感冲突时，在 brief 里显式记录问题与解法。
4. **音乐生成件单独夹管理**：Score 夹按镜头顺序存音乐 prompt，混音时逐条对位。
