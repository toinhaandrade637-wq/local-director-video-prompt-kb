# 本地导演助手 · 视频提示词知识库

面向本地导演助手的配套知识库：把六个来源的视频提示词、方法论、官方教程、技能包与项目数据，整理成**人和 AI 都能快速定位、精确引用**的一套结构。

- **611** 个影片项目 · **174,404** 条去重提示词（原文 816 MB，压缩 214 MB）
- **977** 条多模型提示词 / 运镜器材演技词典 / 教程
- **35** 个方法页文件（Higgsfield 三轨 + Seedance 2.5）
- **8** 个可加载技能 + **11** 套官方技能文本
- **535** 篇创作者博客、**419** 份官方教程文本、**83** 份项目 brief、**18** 篇全流程方法论

> 第一次来，读 [START-HERE.md](START-HERE.md)（5 分钟）。要全貌，读 [INDEX.md](INDEX.md)。让 AI 接手，读 [AGENTS.md](AGENTS.md)。只要机器入口，读 [llms.txt](llms.txt) 或 [MANIFEST.json](MANIFEST.json)。

> **分类提醒**：611 个项目里只有 6 个带 `scenes` 细分，537 个只有 `all`。检索时 `--cat` 返回 0 条，先去掉 `--cat`。详见 [catalog/taxonomy.md](catalog/taxonomy.md)。

---

## 1. 六个来源

| 来源 | 内容 | 规模 | 适合解决 |
|---|---|---|---|
| [Higgsfield 全量语料](sources/higgsfield/) | 611 个影片项目的去重提示词 + brief + 项目 README + 官方 Skill | 174,404 条 | 一部片子从设定到镜头怎么组织；找同题材、同模型的完整写法 |
| [Higgsfield 三轨方法库](sources/higgsfield-knowledge-base/) | 视频 8 页 + 生图 2 页 + 通用 4 页 + 研究记录 + 维护台账 | 410 文件 | 先学怎么写，再动笔；查方法、术语、模型硬约束 |
| [经验内容](sources/experience/) | 官方教程、创作者博客、项目 brief、官方技能包、18 篇全流程方法论 | 1,139 文件 | 学完整工作流；看官方怎么写；找案例拆解 |
| [video-prompt-library](sources/video-prompt-library/) | 主库 339 条成片级提示词 + 通用区 633 条词典 + 教程区 5 篇 | 977 条 | 写单条成片提示词；补运镜、器材、表演零件 |
| [Seedance 2.5 知识库](sources/seedance25-knowledge-base/) | 12 页现行方法、任务/问题导航、来源档案、Skill | 15 页方法 | 建立写作框架；排查生成失败；平台入口差异 |
| [通用技能仓库](sources/skills-repo/) | 角色/道具资产表、专业剧本格式、Suno 音乐提示词、图片解析 | 5 个技能 | 直接加载使用，产出结构化 prompt |

方法正文只保留一份，在 `sources/` 里；顶层 [methods/](methods/) 只做导航，[skills/](skills/) 是可加载副本。同一内容冲突时，以 `sources/` 为准。

---

## 2. 三种用法

### 人：浏览与找参考

1. [START-HERE.md](START-HERE.md) 选路线。
2. [INDEX.md](INDEX.md) 看全局地图。
3. [catalog/higgsfield-projects.md](catalog/higgsfield-projects.md) 按项目主题找片。
4. [catalog/video-prompt-library.md](catalog/video-prompt-library.md) 按题材/词典分类找条目。
5. 打开对应源文件读全文。

### AI：按任务取用

1. 读 [AGENTS.md](AGENTS.md)（作业规则）。
2. 查 [docs/02-任务路由.md](docs/02-任务路由.md)，确定这次读哪几页方法、去哪类语料找参考。
3. 用 [catalog/](catalog/) 的轻量索引定位，不要一次加载整个语料库。
4. 只回读命中的那几行，写完后按统一格式标注来源。

```bash
# 看统计
python tools/kb.py stats

# 搜索（只读索引，不读全文）
python tools/kb.py search --keyword "雨夜" --limit 10
python tools/kb.py search --project DETOUR --cat scenes --type video --limit 10
python tools/kb.py search --source vpl --zone 主库 --cat "动作·打斗" --limit 10

# 按 ID 取全文
python tools/kb.py get --id HFX-DETOUR-000166
python tools/kb.py get --id VPL-sd2-259
```

不知道查询怎么写，看 [docs/07-检索案例.md](docs/07-检索案例.md) 的 8 个真实例子。

### 写作：一条提示词的装配顺序

```text
确定交付与观看目标
  → sources/seedance25-knowledge-base/现行知识/02-通用结构与选用.md
  → 按内容补 03 参考分工 / 04 全局设定 / 05 表演 / 06 动作 / 07 摄影 / 08 光影 / 09 声音
  → 需要平台硬约束时读 sources/higgsfield-knowledge-base/现行知识/通用/02-模型手册.md
  → 从 catalog 找 2–5 条同题型参考，只学关系与笔法
  → 用当前项目的人物、场景、台词重写
  → 按 docs/03-检索手册.md 的引用格式标注来源
```

---

## 3. 目录地图

```text
.
├── START-HERE.md              # 5 分钟上手
├── README.md                  # 本文件：人看的总说明
├── AGENTS.md                  # AI 必读：读取顺序、路由、硬规则、引用格式
├── INDEX.md                   # 全局地图与统计
├── llms.txt                   # 给 AI 的精简入口（llms.txt 规范）
├── index.json                 # 机器可读的源、统计、入口
├── MANIFEST.json              # 每个顶层目录的用途、文件数、入口
├── CHANGELOG.md               # 变更记录
├── NOTICE.md                  # 来源、权利与免责声明
├── LICENSE                    # 说明文字与工具的许可
├── docs/                      # 使用说明
│   ├── 00-文档地图.md
│   ├── 01-快速开始.md
│   ├── 02-任务路由.md
│   ├── 03-检索手册.md
│   ├── 04-字段与格式.md
│   ├── 05-来源版本与版权.md
│   ├── 06-维护与更新.md
│   ├── 07-检索案例.md
│   └── 08-构建与校验报告.md
├── catalog/                   # 统一索引（AI 的主入口）
│   ├── README.md
│   ├── taxonomy.md            # 类别 / 类型 / 模型 / ID 口径
│   ├── higgsfield-projects.md / .json / .csv
│   ├── higgsfield-models.json
│   ├── higgsfield-prompts.index.jsonl
│   ├── video-prompt-library.md
│   ├── video-prompt-library.index.jsonl
│   ├── methods.json
│   └── skills.json
├── methods/
│   └── README.md              # 方法导航（正文在 sources/，避免副本死链）
├── skills/
│   ├── README.md              # 技能清单与选择建议
│   ├── seedance-prompt/
│   ├── hf-video-prompt/
│   ├── hf-image-prompt/
│   ├── character-asset-sheet/
│   ├── prop-asset-sheet/
│   ├── fountain-screenplay/
│   ├── suno-music-prompts/
│   ├── image-text-transcript/
│   └── higgsfield-official/   # 官方技能包文本
├── sources/                   # 六个来源的快照
│   ├── README.md              # 快照范围与裁剪说明
│   ├── higgsfield/            # _ENTRY.md 为入口
│   ├── higgsfield-knowledge-base/
│   ├── experience/
│   ├── video-prompt-library/
│   ├── seedance25-knowledge-base/
│   └── skills-repo/
└── tools/
    ├── build_catalog.py
    ├── kb.py
    └── validate_kb.py
```

---

## 4. 数据口径

| 指标 | 数值 | 说明 |
|---|---:|---|
| Higgsfield 项目 | 611 | 去重后仍有提示词的项目 |
| Higgsfield 提示词 | 174,404 | 项目内按原文 MD5 去重 |
| 原文体量 | 816 MB | 提示词文本字符数 |
| 压缩体量 | 214 MB | 每项目一份 `prompts.jsonl.gz` |
| 其中 `seedance_2_5` | 14,907 | 模型字段明确标注 |
| 其中 `seedance_2_0` | 13,585 | 模型字段明确标注 |
| 其中 `default` | 45,467 | 平台自动选择模型，未细分 |
| 多模型库条目 | 977 | 主库 339 / 通用区 633 / 教程区 5 |
| 方法页文件 | 35 | Higgsfield 20 + Seedance 15 |
| 技能 | 8 | 顶层可加载；另有官方技能文本 11 套 |

完整分布见 [index.json](index.json) 与 [catalog/higgsfield-models.json](catalog/higgsfield-models.json)。

---

## 5. 这个库适合什么、不适合什么

**适合**

- 写分镜与视频提示词时，快速找到同题材、同模型、同镜头类型的参考。
- 学一部影片如何把角色、场景、道具、分镜、视频提示词组织成一套工程。
- 查运镜、器材、表演、光影、模型硬约束的可复用描述。
- 让 AI 在不把 816 MB 原文塞进上下文的前提下，按 ID 精确取用。

**不适合**

- 直接复制参考提示词当成品。参考只提供结构和笔法，人物、场景、台词必须换成当前项目的。
- 把某条提示词当成“模型保证有效”的结论。语料里包含探索、失败与重跑记录，需要自己判断。
- 替代模型官方文档。Seedance 2.5 的官方资料在 `sources/seedance25-knowledge-base/资料库/03_官方参考/`。

---

## 6. 来源、版本与权利

- 主仓库：https://github.com/toinhaandrade637-wq/local-director-video-prompt-kb
- 快照日期：2026-11-22。
- 六个上游来源与提交版本见 [docs/05-来源版本与版权.md](docs/05-来源版本与版权.md)。
- 上游均未声明开源许可证。本库只做学习、检索与创作参考，**不主张对原始提示词的著作权**；权利归原作者/原平台。
- 若权利人要求下架，按 [NOTICE.md](NOTICE.md) 的方式处理。

---

## 7. 维护

```bash
python tools/build_catalog.py        # 从 sources/ 重建全部索引与统计（约 35 秒）
python tools/validate_kb.py          # 完整校验：611 个项目逐项核对
python tools/validate_kb.py --fast   # 快速校验：链接、计数、密钥
```

更新来源、增删条目、修改结构的约定见 [docs/06-维护与更新.md](docs/06-维护与更新.md)，本次构建的数字与已知限制见 [docs/08-构建与校验报告.md](docs/08-构建与校验报告.md)。
