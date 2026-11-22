# 全局索引

> 一张图看清：这个库有什么、从哪进、什么问题去哪里。

## 1. 四个入口

| 你是谁 / 要做什么 | 从这里开始 |
|---|---|
| 第一次来 | [START-HERE.md](START-HERE.md) → [README.md](README.md) → 本页 |
| 让 AI 开始干活 | [AGENTS.md](AGENTS.md) → [docs/02-任务路由.md](docs/02-任务路由.md) |
| 只要机器可读入口 | [llms.txt](llms.txt) → [index.json](index.json) → [MANIFEST.json](MANIFEST.json) |
| 只想快速找一条参考 | [catalog/README.md](catalog/README.md) → `python tools/kb.py search` |

全部文档索引：[docs/00-文档地图.md](docs/00-文档地图.md)。

## 2. 库里有什么

| 层 | 目录 | 内容 | 规模 |
|---|---|---|---:|
| 方法 | [sources/higgsfield-knowledge-base/现行知识/](sources/higgsfield-knowledge-base/现行知识/) | 视频 8 页 + 生图 2 页 + 通用 4 页 | 20 文件 |
| 方法 | [sources/seedance25-knowledge-base/现行知识/](sources/seedance25-knowledge-base/现行知识/) | Seedance 2.5 写作方法 | 15 页 |
| 语料 | [sources/higgsfield/prompts/](sources/higgsfield/prompts/) | 611 个项目去重提示词 | 174,404 条 |
| 项目文档 | [sources/higgsfield/projects/](sources/higgsfield/projects/) | brief、README、官方 Skill | 79 项目 |
| 知识库 | [sources/higgsfield-knowledge-base/](sources/higgsfield-knowledge-base/) | 三轨方法、研究记录、维护台账 | 410 文件 |
| 经验 | [sources/experience/](sources/experience/) | 官方教程、创作者博客、brief、技能包、全流程方法论 | 1,139 文件 |
| 语料 | [sources/video-prompt-library/](sources/video-prompt-library/) | 主库 + 通用区 + 教程区 | 977 条 |
| 方法 | [sources/seedance25-knowledge-base/](sources/seedance25-knowledge-base/) | 方法、来源档案、研究记录、Skill | 224 文件 |
| 技能 | [skills/](skills/) | 8 个可加载技能 + 官方技能文本 | 132 文件 |
| 索引 | [catalog/](catalog/) | 项目表、分类表、逐条轻量索引 | 175,381 行 |
| 工具 | [tools/](tools/) | 检索、取全文、重建索引、校验 | 3 个脚本 |

## 3. 按任务进入

| 任务 | 方法 | 参考语料 |
|---|---|---|
| 写单镜提示词 | [SD25 02](sources/seedance25-knowledge-base/现行知识/02-通用结构与选用.md) + [HF 视频 01](sources/higgsfield-knowledge-base/现行知识/视频/01-提示词结构.md) | VPL 主库同题材；项目 `scenes` |
| 写整场连续动作 | [SD25 10](sources/seedance25-knowledge-base/现行知识/10-连续转场与阶段变化.md) + [HF 视频 03](sources/higgsfield-knowledge-base/现行知识/视频/03-运镜与空间.md) | 项目 `scenes`；VPL 创意转场 |
| 角色一致性 | [SD25 03](sources/seedance25-knowledge-base/现行知识/03-参考分工与主体一致性.md) + [HF 视频 02](sources/higgsfield-knowledge-base/现行知识/视频/02-参考分工.md) | 项目 `characters`；VPL 人物类 |
| 图生视频 / 首尾帧 | [SD25 12](sources/seedance25-knowledge-base/现行知识/12-Seedance入口与平台差异.md) | 项目 `image` + `video` |
| 对白 / 表演 | [SD25 05](sources/seedance25-knowledge-base/现行知识/05-表演对白与方言.md) + [HF 视频 07](sources/higgsfield-knowledge-base/现行知识/视频/07-声音与音频.md) | VPL 写实人物·剧情；演技词典 |
| 打戏 / 特效 | [SD25 06](sources/seedance25-knowledge-base/现行知识/06-动作因果与打戏.md) + [HF 视频 04](sources/higgsfield-knowledge-base/现行知识/视频/04-动作与打戏.md) | VPL 动作·打斗 / 玄幻 |
| 运镜 / 长镜头 | [HF 视频 03](sources/higgsfield-knowledge-base/现行知识/视频/03-运镜与空间.md) | VPL 运镜词典；创意转场 |
| 光影 / 风格 | [SD25 08](sources/seedance25-knowledge-base/现行知识/08-光影色彩材质与环境.md) + [HF 通用 01](sources/higgsfield-knowledge-base/现行知识/通用/01-色彩与HEX.md) | VPL 导演风格；同题材项目 |
| 声音设计 | [HF 视频 07](sources/higgsfield-knowledge-base/现行知识/视频/07-声音与音频.md) | 视频提示词声音段 |
| 系列片 / 排故事 | [HF 视频 08](sources/higgsfield-knowledge-base/现行知识/视频/08-叙事与系列方法论.md) | 同作者多项目；教程区 |
| 失败排查 | [SD25 按问题查](sources/seedance25-knowledge-base/现行知识/按问题查.md) | 同模型同题型记录 |
| 生成资产图 / 剧本 / 音乐 | [skills/](skills/) | — |

完整路由（含交付要点）见 [docs/02-任务路由.md](docs/02-任务路由.md)。

## 4. 按来源进入

### Higgsfield 全量 · 611 项目

- [项目总表（按提示词数排序）](catalog/higgsfield-projects.md)
- [项目元数据 JSON](catalog/higgsfield-projects.json)
- [逐条索引](catalog/higgsfield-prompts.index.jsonl)
- [模型分布](catalog/higgsfield-models.json)

体量最大的项目：

| 项目 | 主题 | 提示词 |
|---|---|---:|
| [VENGEANCE_IS_MINE](sources/higgsfield/prompts/VENGEANCE_IS_MINE/) | 复仇动作 | 5,501 |
| [ONEIRIC](sources/higgsfield/prompts/ONEIRIC/) | 梦境/超现实 | 3,247 |
| [CULLY_HILL_BOYS](sources/higgsfield/prompts/CULLY_HILL_BOYS/) | 街头群像 | 3,173 |
| [KOK_BORU_FILM](sources/higgsfield/prompts/KOK_BORU_FILM/) | 中亚马背叼羊 | 2,436 |
| [DETOUR](sources/higgsfield/prompts/DETOUR/) | 街头赛车动作 | 2,173 |
| [HELL_GRIND](sources/higgsfield/prompts/HELL_GRIND/) | 地狱/动作 | 1,861 |

### Higgsfield 方法 · 三轨 14 页

- [方法索引](sources/higgsfield-knowledge-base/现行知识/索引.md)
- [按任务查](sources/higgsfield-knowledge-base/现行知识/按任务查.md)
- [按问题查](sources/higgsfield-knowledge-base/现行知识/按问题查.md)

### 经验内容

- [18 篇全流程方法论](sources/experience/03-全流程方法论/)
- [419 份官方教程文本](sources/experience/05-官方教程/)
- [535 篇创作者博客](sources/experience/05-创作者博客/)
- [83 份项目 brief](sources/experience/05-官方项目brief/)
- [官方技能包文本](sources/experience/05-官方技能包/)

### video-prompt-library · 977 条

- [分类与检索指南](catalog/video-prompt-library.md)
- [逐条索引](catalog/video-prompt-library.index.jsonl)
- [原库 AI 导读索引](sources/video-prompt-library/AI导读索引.md)
- [原库完整手册](sources/video-prompt-library/README.md)

### Seedance 2.5 · 方法与 Skill

- [方法阅读副本](sources/seedance25-knowledge-base/现行知识/)
- [按任务查](sources/seedance25-knowledge-base/现行知识/按任务查.md)
- [按问题查](sources/seedance25-knowledge-base/现行知识/按问题查.md)
- [Skill 源码](skills/seedance-prompt/SKILL.md)
- [原库入口](sources/seedance25-knowledge-base/index.md)

### 通用技能

- [角色资产表](skills/character-asset-sheet/SKILL.md)
- [道具资产表](skills/prop-asset-sheet/SKILL.md)
- [专业剧本格式](skills/fountain-screenplay/SKILL.md)
- [Suno 音乐提示词](skills/suno-music-prompts/SKILL.md)
- [图片解析](skills/image-text-transcript/SKILL.md)

## 5. 按文件类型进入

| 想知道 | 文件 |
|---|---|
| 全部文档怎么分工 | [docs/00-文档地图.md](docs/00-文档地图.md) |
| 5 分钟上手 | [docs/01-快速开始.md](docs/01-快速开始.md) |
| 每条索引有哪些字段 | [docs/04-字段与格式.md](docs/04-字段与格式.md) |
| 怎么搜、怎么回读 | [docs/03-检索手册.md](docs/03-检索手册.md) |
| 真实查询例子 | [docs/07-检索案例.md](docs/07-检索案例.md) |
| 类别 / 模型 / ID 口径 | [catalog/taxonomy.md](catalog/taxonomy.md) |
| 来源、裁剪、版权 | [docs/05-来源版本与版权.md](docs/05-来源版本与版权.md) |
| 怎么更新与校验 | [docs/06-维护与更新.md](docs/06-维护与更新.md) |
| 本次构建与校验结果 | [docs/08-构建与校验报告.md](docs/08-构建与校验报告.md) |
| 变更记录 | [CHANGELOG.md](CHANGELOG.md) |
| 方法页清单（机器可读） | [catalog/methods.json](catalog/methods.json) |
| 技能清单（机器可读） | [catalog/skills.json](catalog/skills.json) |
| 机器可读总表 | [index.json](index.json) |

## 6. 统计口径

```text
Higgsfield   611 项目 · 174,404 条 · 原文 816 MB · 压缩 214 MB
             其中 537 个项目只有 all 类目；79 个项目带 brief / README / 官方 Skill
VPL          977 条（主库 339 / 通用区 633 / 教程区 5）
方法         35 个文件（Higgsfield 20 + Seedance 15）
技能         8 个可加载 + 11 套官方文本
经验         1,139 个文本文件
索引         174,404 + 977 = 175,381 行
```

数字由 `tools/build_catalog.py` 从源文件重新计算，`index.json` 为准。
