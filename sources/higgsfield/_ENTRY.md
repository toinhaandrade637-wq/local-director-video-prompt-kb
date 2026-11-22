# Higgsfield 全量语料 · 入口

> 611 个影片项目的去重提示词，一项目一份压缩 JSONL。这里是本库最大的语料层。

## 1. 规模

| 项 | 数值 |
|---|---:|
| 项目 | 611 |
| 去重提示词 | 174,404 |
| 原文 | 815.7 MB |
| 压缩后 | 213.6 MB |
| 带项目文档（brief / README / 官方 Skill） | 79 |

## 2. 目录

```text
sources/higgsfield/
├── _ENTRY.md              # 本页
├── _INDEX.md              # 78 项目时代的旧索引（历史说明）
├── _SOURCES.md            # 上游项目链接
├── _项目元数据.json        # 项目主题、作者、原链接、语言
├── _统计.json              # 78 项目时代的统计
├── _brief索引.md           # 83 份官方 brief 的总索引
├── prompts/
│   └── <项目>/prompts.jsonl.gz
└── projects/
    └── <项目>/README.md · brief.txt · brief全文.txt · SKILL.md · official_skills/
```

## 3. 一条记录长什么样

```json
{"id":"HFX-DETOUR-000166","cat":"scenes","type":"video","model":"seedance_2_5","prompt":"8秒、21:9超宽银幕……"}
```

字段说明见 [docs/04-字段与格式](../../docs/04-字段与格式.md)。

## 4. 怎么读

```bash
# 找一条
python tools/kb.py search --project DETOUR --cat scenes --type video --limit 10

# 取全文
python tools/kb.py get --id HFX-DETOUR-000166

# 看项目文档
# 打开 projects/DETOUR/README.md 与 brief.txt
```

不要直接解压整个项目文件。大项目单文件上万条，读完会挤掉方法页的上下文。

## 5. 必须先知道

- **537 个项目只有 `all` 类目。** 上游只给了 `_all_prompts.jsonl`，没有分类文件。
- **只有 6 个项目有 `scenes` 细分**，DETOUR 是分类最全的一个。
- **跨项目不去重。** 同一句在多个项目出现，是不同记录。
- **`model=default` 不是模型名**，是平台自动选择。

## 6. 项目表与索引

- 项目总表：[catalog/higgsfield-projects.md](../../catalog/higgsfield-projects.md)
- 可筛选表格：[catalog/higgsfield-projects.csv](../../catalog/higgsfield-projects.csv)
- 单条索引：[catalog/higgsfield-prompts.index.jsonl](../../catalog/higgsfield-prompts.index.jsonl)
- 分类口径：[catalog/taxonomy.md](../../catalog/taxonomy.md)

## 7. 来源

本地工作区 `02_完整提示词数据包`（615 个原始目录，去重后 611 个有提示词），并逐项目核对过与 `YIJUEYIJUE/higgsfield-film-prompts`（78 项目）的关系：78 个都在全量数据中，行数不少于仓库版本，因此不再单独保留旧 JSONL。

详见 [docs/05-来源版本与版权](../../docs/05-来源版本与版权.md)。
