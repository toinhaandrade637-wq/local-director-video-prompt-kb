# AGENTS.md · AI 作业卡

> 这是本知识库的**唯一必读入口**。先读完本页，再决定读哪些文件。
> 不要从 `sources/higgsfield/prompts/` 里随便解压一个大文件开始读。

## 0. 一句话

这是一个“**方法 + 语料 + 索引**”三层结构的知识库：方法正文在 `sources/*/现行知识/`，`sources/` 其余部分存原文，`catalog/` 让你只读需要的那几行。

## 1. 读取顺序（不要跳）

| 顺序 | 读什么 | 目的 |
|---:|---|---|
| 1 | 本文件 | 知道规则、路由、引用格式 |
| 2 | [docs/02-任务路由.md](docs/02-任务路由.md) | 按这次任务确定阅读路线 |
| 3 | [catalog/README.md](catalog/README.md) | 知道索引文件各自装什么 |
| 4 | 路由指定的 1–3 页方法 | 建立写作框架 |
| 5 | 索引筛出的 2–5 条参考 | 学结构，不抄内容 |
| 6 | 需要时再回读源文件对应行 | 核对原文与上下文 |

**不要**：一次解压全部 611 个项目、把 816 MB 原文塞进上下文、用 `cat` 扫全库。

## 2. 三条硬规则

1. **定位优先于加载。** 先用 `catalog/*.index.jsonl` 找到项目与行号，再只读那一行。单条提示词可能上万字，读错十条就浪费了整个上下文。
2. **参考不是模板。** 可以迁移结构、镜头关系、段落节奏、描述粒度；人物、场景、道具、台词、动作结果必须换成当前项目的。禁止整段照抄后只改名字。
3. **不知道就说不知道。** 语料里没有的模型能力、参数、平台限制，不要根据记忆补。平台问题先查 `sources/higgsfield-knowledge-base/现行知识/通用/02-模型手册.md`、`sources/seedance25-knowledge-base/现行知识/12-Seedance入口与平台差异.md` 与官方资料目录。

## 3. 任务路由

先在下表找到最接近的任务，再按“读什么”一列执行。更细的版本见 [docs/02-任务路由.md](docs/02-任务路由.md)。

| 这次要做什么 | 先读方法 | 再找参考 | 交付时注意 |
|---|---|---|---|
| 从剧本/分镜写单镜提示词 | [SD25 02 通用结构](sources/seedance25-knowledge-base/现行知识/02-通用结构与选用.md) → [HF 视频 01 提示词结构](sources/higgsfield-knowledge-base/现行知识/视频/01-提示词结构.md) | 主库同题材 3 条；同项目 `scenes` | 按观看顺序组织；结尾有落点 |
| 写整场多镜 / 连续动作 | [SD25 10 连续转场](sources/seedance25-knowledge-base/现行知识/10-连续转场与阶段变化.md) → [HF 视频 03 运镜与空间](sources/higgsfield-knowledge-base/现行知识/视频/03-运镜与空间.md) | 同项目 `scenes`；VPL 创意转场 | 每镜有承接；阶段变化不误写成切镜 |
| 角色一致性 / 参考图分工 | [SD25 03 参考分工](sources/seedance25-knowledge-base/现行知识/03-参考分工与主体一致性.md) → [HF 视频 02 参考分工](sources/higgsfield-knowledge-base/现行知识/视频/02-参考分工.md) | 同项目 `characters`；VPL 人物类 | 说清保留什么、替换什么、缺什么 |
| 图生视频 / 首尾帧 / 延长 | [SD25 12 入口差异](sources/seedance25-knowledge-base/现行知识/12-Seedance入口与平台差异.md) → [SD25 09 跨镜衔接](sources/seedance25-knowledge-base/现行知识/09-声音与跨镜衔接.md) | 同项目 `image` + `video` | 分清画面匹配、状态接续、真实延长 |
| 对白 / 表演 / 方言 | [SD25 05 表演对白](sources/seedance25-knowledge-base/现行知识/05-表演对白与方言.md) → [HF 视频 07 声音与音频](sources/higgsfield-knowledge-base/现行知识/视频/07-声音与音频.md) | VPL 写实人物·剧情；通用区 演技词典 | 目的与触发进节拍；听者反应连续 |
| 打戏 / 法术 / 特效 | [SD25 06 动作因果](sources/seedance25-knowledge-base/现行知识/06-动作因果与打戏.md) → [HF 视频 04 动作与打戏](sources/higgsfield-knowledge-base/现行知识/视频/04-动作与打戏.md) → [HF 视频 06 VFX](sources/higgsfield-knowledge-base/现行知识/视频/06-VFX与合成.md) | VPL 动作·打斗 / 玄幻；项目 KOK_BORU、HELL_GRIND、VENGEANCE_IS_MINE | 动作有应对和结果；关键关系可见 |
| 运镜 / 长镜头 / 转场 | [HF 视频 03 运镜与空间](sources/higgsfield-knowledge-base/现行知识/视频/03-运镜与空间.md) → [SD25 07 摄影空间](sources/seedance25-knowledge-base/现行知识/07-摄影运镜与空间.md) | VPL 通用区 运镜词典；创意转场 | 运动有动机；起幅落幅清楚 |
| 光影 / 色彩 / 材质 / 风格 | [SD25 08 光影材质](sources/seedance25-knowledge-base/现行知识/08-光影色彩材质与环境.md) → [HF 通用 01 色彩与HEX](sources/higgsfield-knowledge-base/现行知识/通用/01-色彩与HEX.md) | VPL 导演风格；同题材项目 | 光有方向；材质受力有反应 |
| 声音 / 音效 / 配乐 | [HF 视频 07 声音与音频](sources/higgsfield-knowledge-base/现行知识/视频/07-声音与音频.md) → [SD25 09 声音](sources/seedance25-knowledge-base/现行知识/09-声音与跨镜衔接.md) | 视频提示词里的声音段 | 声音服务叙事；不堆音效 |
| 广告 / 产品 / 电商 | [HF 视频 01 提示词结构](sources/higgsfield-knowledge-base/现行知识/视频/01-提示词结构.md) → [HF 生图 01 生图方法](sources/higgsfield-knowledge-base/现行知识/生图/01-生图提示词方法.md) | VPL 微距·FPV / 产品·商业片；项目 TOP_UP_AD | 卖点进动作；产品细节可验证 |
| 动画 / 国漫 / 仙侠 | [HF 视频 04 动作与打戏](sources/higgsfield-knowledge-base/现行知识/视频/04-动作与打戏.md) → [HF 视频 08 叙事与系列](sources/higgsfield-knowledge-base/现行知识/视频/08-叙事与系列方法论.md) | VPL 国风·国漫 / 玄幻；项目 ANIME_PRODUCTION | 风格统一；特效服务动作因果 |
| 分镜设计 / 镜头切分 | [HF 视频 03 运镜与空间](sources/higgsfield-knowledge-base/现行知识/视频/03-运镜与空间.md) → [SD25 07 摄影空间](sources/seedance25-knowledge-base/现行知识/07-摄影运镜与空间.md) | 同项目 `scenes`；VPL 教程区 | 每镜一个主要信息；轴线与视线匹配 |
| 写系列片 / 排故事 | [HF 视频 08 叙事与系列方法论](sources/higgsfield-knowledge-base/现行知识/视频/08-叙事与系列方法论.md) | 同作者多项目；教程区 | 留存优先；每集有独立钩子 |
| 生成失败 / 画面崩坏排查 | [SD25 按问题查](sources/seedance25-knowledge-base/现行知识/按问题查.md) → [SD25 11 连续性](sources/seedance25-knowledge-base/现行知识/11-连续性约束与去重复.md) | 同模型、同题型的失败/重跑记录 | 先描述可观察偏差，再区分原因假设 |
| 找同题材整片参考 | [HF 视频 01 提示词结构](sources/higgsfield-knowledge-base/现行知识/视频/01-提示词结构.md) | [项目总表](catalog/higgsfield-projects.md) | 先读项目 README + brief，再读提示词 |
| 直接生成资产图 / 剧本 / 音乐 | 对应技能页 | — | 先读技能，再调用 |

### 检索前必看：分类覆盖

`--cat scenes` 不是随时可用。611 个项目里 **537 个只有 `all`**，只有 6 个带 `scenes` 细分。

- 先试 `--cat`，返回 0 条就**去掉 `--cat`**，用 `--keyword` 或直接读 `all`。
- 不要因为 `scenes` 为空就判断“库里没有”。
- 项目分类覆盖见 [catalog/higgsfield-projects.md](catalog/higgsfield-projects.md) 的「分类覆盖」节。

## 4. 检索流程（四步）

### 第 1 步：搜轻量索引

```bash
python tools/kb.py search --keyword "雨夜" --limit 10
python tools/kb.py search --project DETOUR --cat scenes --type video --limit 10
python tools/kb.py search --model seedance_2_5 --min-length 2500 --limit 10
python tools/kb.py search --source vpl --zone 主库 --cat "动作·打斗" --limit 10
```

没有 Python 时，直接检索索引文件（每行一条，不含全文）：

```bash
rg -n "雨夜" catalog/higgsfield-prompts.index.jsonl
rg -n '"project":"DETOUR"' catalog/higgsfield-prompts.index.jsonl
rg -n '"cat":"动作·打斗"' catalog/video-prompt-library.index.jsonl
```

### 第 2 步：拿到 `id` 与 `line`

索引行示例：

```json
{"id":"HFX-DETOUR-000123","project":"DETOUR","cat":"scenes","type":"video","model":"seedance_2_5","len":7216,"line":123,"head":"Suspenseful action vibe..."}
```

### 第 3 步：只回读那一行

```bash
python tools/kb.py get --id HFX-DETOUR-000123
python tools/kb.py get --id HFX-DETOUR-000123 --json
```

### 第 4 步：需要上下文时再读邻行

同一项目、同一 `cat` 的相邻条目往往属于同一场戏。只在确实需要时读前后 1–3 行，不要扩大到整个项目（大项目单文件超 1 万条）。

## 5. 引用格式

写进交付物时，参考来源统一放在末尾，使用稳定 ID：

```text
参考来源
- [HFX-DETOUR-000123 · seedance_2_5 · scenes] 镜头段落结构
- [VPL:sd2-240 · Seedance 2.0] 微距 FPV 的运动描述
- [SD25:07] 摄影运镜与空间
- [HF:视频/03] 运镜与空间
```

规则：

- Higgsfield 全量：`HFX:<项目>#<六位行号>`，例如 `HFX:DETOUR#000123`。
- video-prompt-library：`VPL:<原 id>`，例如 `VPL:sd2-240`。
- Seedance 方法：`SD25:<页序号>`，例如 `SD25:07`。
- Higgsfield 方法：`HF:<轨道>/<页序号>`，例如 `HF:视频/03`。
- 只引用真正读过的条目。不要凭索引摘要编造原文。

## 6. 写提示词的装配流程

1. **定交付**：文生视频、图生视频、首尾帧还是延长？成片多长？画幅？有没有对白？
2. **定观看顺序**：观众先看到什么、再看到什么、最后停在哪。
3. **搭骨架**：生成目标 → 参考分工与全局设定 → 按镜头/阶段的综合小段 → 结束状态与约束。
4. **填内容**：人物目的、动作、表演、摄影、环境、声音写在同一个小段里，不分开列清单。
5. **找参考**：只找 2–5 条同题型，读结构，不读表面形容词。
6. **重写**：换成当前项目的事实；删掉参考里与当前项目无关的细节。
7. **自检**：主体是否一致？动作是否有因果？空间是否可见？声音是否服务叙事？有没有重复堆砌？

输出建议：

```text
【提示词】
……

【参考来源】
……

【假设与待确认】
- 未指定的画幅/时长/平台
- 需要补充的参考图或首帧
```

## 7. 权威顺序

发生冲突时，按以下顺序取：

1. 当前项目的剧本、设定、用户本轮指令。
2. `sources/*/现行知识/` 里的现行方法（方法正文只有这一份，`methods/README.md` 只是导航）。
3. `sources/` 里的参考提示词（只是案例，不是规范）。
4. 模型官方文档。
5. 其他二手资料。

同一件事，项目事实永远压过通用方法；通用方法压过某条参考提示词的个人习惯。

## 8. 目录速查

| 你要找 | 去哪里 |
|---|---|
| 5 分钟上手 / 全部文档分工 | [START-HERE.md](START-HERE.md) / [docs/00-文档地图.md](docs/00-文档地图.md) |
| 任务该读哪几页 | [docs/02-任务路由.md](docs/02-任务路由.md) |
| 索引字段与检索命令 | [docs/03-检索手册.md](docs/03-检索手册.md) |
| 真实查询例子 | [docs/07-检索案例.md](docs/07-检索案例.md) |
| 各来源数据格式 | [docs/04-字段与格式.md](docs/04-字段与格式.md) |
| 类别 / 模型 / ID 口径 | [catalog/taxonomy.md](catalog/taxonomy.md) |
| Higgsfield 项目总表 | [catalog/higgsfield-projects.md](catalog/higgsfield-projects.md) |
| 多模型库分类 | [catalog/video-prompt-library.md](catalog/video-prompt-library.md) |
| 方法页清单 | [catalog/methods.json](catalog/methods.json) |
| 技能清单 | [catalog/skills.json](catalog/skills.json) |
| 每个来源的入口 | [sources/higgsfield/_ENTRY.md](sources/higgsfield/_ENTRY.md) 等 `sources/*/_ENTRY.md` |
| 官方教程 / 博客 / brief | [sources/experience/](sources/experience/) |
| 来源、裁剪与版权 | [docs/05-来源版本与版权.md](docs/05-来源版本与版权.md) |
| 怎么更新、怎么校验 | [docs/06-维护与更新.md](docs/06-维护与更新.md) / [docs/08-构建与校验报告.md](docs/08-构建与校验报告.md) |

## 9. 什么时候更新知识库

- 拿到一批新提示词或新项目：先放进 `sources/higgsfield/prompts/<项目>/prompts.jsonl.gz`，再跑 `python tools/build_catalog.py`。
- 方法页有修订：直接改 `sources/*/现行知识/`；`methods/README.md` 的链接不需要动（除非增删页）。
- 每次更新后跑 `python tools/validate_kb.py`，全绿再提交。
- 不要在 `catalog/` 里手改生成结果；改源文件或生成脚本。

## 10. 禁止事项

- 禁止把 `sources/` 里的原文改写成“更适合检索”的版本。原文是证据，索引才是导航。
- 禁止把私人聊天、令牌、密钥、本机绝对路径写进知识库。
- 禁止在没有来源的情况下声称“某模型支持/不支持某能力”。
- 禁止把参考提示词整段复制到公开交付物而不标注来源。
