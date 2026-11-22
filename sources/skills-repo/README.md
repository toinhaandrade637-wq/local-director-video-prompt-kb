# skills

常用技能仓库。每个技能一个目录，直接位于 `skills/` 下，目录内是可直接加载的完整技能（含 `SKILL.md`、`package.json`，有图标时带 `icon.jpg`）。

## 技能清单

| 目录 | 技能 | 说明 | 版本 |
| --- | --- | --- | --- |
| `skills/character-asset-sheet` | 人物资产图模板 | 把一句角色描述组装成生产级「角色设定集 / 三视图 turnaround」生图 prompt。内置硬约束模板（纯白背景 + 多视图分栏 + 身高标尺 + 无文字无阴影无水印），默认只产出结构化 prompt，不消耗生图额度 | 1.0.0 |
| `skills/fountain-screenplay` | 专业剧本格式 | 工作区里带场次轨和台词块的 `.fountain` 专业剧本。用于「新建一个剧本」「建一份专业剧本」、点名专业剧本格式或 `.fountain`、或修改已有 `.fountain`；不用于分析、改写或视频工作流。含 2 个 references 参考文档 | 1.1.3 |
| `skills/image-text-transcript` | 图片解析 | 只做垂直解析：把图上真实存在的内容整理成事实，看不清就写「看不清」。输出一句话概述、可见文字原样转录、主体 / 场景 / 布局，以及委派问题的直接答案；多图按「第 N 张」分开。 | 1.0.0 |
| `skills/prop-asset-sheet` | 道具资产图模板 | 把一句道具描述组装成生产级「道具设定集 / 三视图 turnaround」生图 prompt。内置硬约束模板（纯白背景 + 多视图分栏 + 比例标尺 + 无文字无阴影无环境），默认只产出结构化 prompt，不消耗生图额度 | 1.0.0 |
| `skills/suno-music-prompts` | Suno 音乐提示词 | Suno AI v5.5 音乐提示词专家。覆盖 Voices 个人声模型、Custom Models、My Taste、颗粒化参数（BPM / Key / Instrumentation / Weirdness / Style Influence / Section Steering）、Stems 分轨与 MIDI 导出。内嵌音乐知识图谱（246 条曲风 × 19 大类、24 种语言、80 个人声标签、799 条乐器×技法 × 17 个家族、20 种曲式结构），含 7 个 references 参考库 | 1.0.0 |