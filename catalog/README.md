# catalog · 索引层

> 这是 AI 检索的主入口。**所有索引都不含全文**，只含定位信息与短摘要。

## 1. 文件清单

| 文件 | 行数 | 用途 |
|---|---:|---|
| `higgsfield-prompts.index.jsonl` | 174,404 | Higgsfield 全量单条索引 |
| `higgsfield-projects.md` | — | 611 项目总表（人读） |
| `higgsfield-projects.json` | — | 611 项目结构（机器读） |
| `higgsfield-models.json` | — | 模型 / 类别 / 类型分布 |
| `video-prompt-library.index.jsonl` | 977 | VPL 单条索引 |
| `video-prompt-library.md` | — | VPL 分区、分类树、模型分布 |
| `methods.json` | 35 | 方法页清单与路径 |
| `skills.json` | 8 | 可加载技能清单 |

## 2. Higgsfield 索引字段

```json
{"id":"HFX-DETOUR-000123","project":"DETOUR","cat":"scenes","type":"video","model":"seedance_2_5","len":7216,"line":123,"head":"Suspenseful action vibe..."}
```

| 字段 | 含义 |
|---|---|
| `id` | 稳定 ID：`HFX-<项目>-<六位行号>` |
| `project` | 611 个项目之一 |
| `cat` | `scenes` / `characters` / `locations` / `props` / `assets` / `cover` / `all` |
| `type` | `video` / `image` / 空（模型未标注） |
| `model` | 原始模型名；`default` = 平台自动选择 |
| `len` | 提示词字符数 |
| `line` | 在 `sources/higgsfield/prompts/<项目>/prompts.jsonl.gz` 中的行号（1-based） |
| `head` | 压缩空白后的前 80 字 |

回读方式：

```bash
python tools/kb.py get --id HFX-DETOUR-000123
```

或直接解压：

```bash
python -c "import gzip;print(gzip.open('sources/higgsfield/prompts/DETOUR/prompts.jsonl.gz','rt',encoding='utf-8').readlines()[122])"
```

## 3. VPL 索引字段

```json
{"id":"VPL-sd2-240","zone":"主库","model":"Seedance 2.0","cat":"微距·FPV特写","sub":"动物·生灵","name":"蜻蜓·毒气温室生死突围","desc":"……","tags":["微距","FPV"],"lang":"zh","length":830,"line":1,"head":"超广角微距FPV……"}
```

| 字段 | 含义 |
|---|---|
| `zone` | `主库` / `通用区` / `教程区` |
| `cat` / `sub` | 题材或词典分组 |
| `tags` | 3–6 个标签 |
| `length` | 原文字符数 |
| `line` | 在 `sources/video-prompt-library/AI-全库.jsonl` 中的行号 |

## 4. 常用查询

```bash
# 关键词
python tools/kb.py search --keyword "赛博" --limit 20

# 某项目的分镜视频提示词
python tools/kb.py search --project DETOUR --cat scenes --type video --limit 20

# 某模型的长提示词
python tools/kb.py search --model seedance_2_5 --min-length 3000 --limit 20

# VPL 主库动作类
python tools/kb.py search --source vpl --zone 主库 --cat "动作·打斗" --limit 20

# VPL 通用区运镜词典
python tools/kb.py search --source vpl --zone 通用区 --cat "运镜词典" --limit 20

# 按标签
python tools/kb.py search --source vpl --tags "微距,FPV" --limit 20
```

## 5. 索引的边界

- `head` 只有 80 字，只用于筛选，不能当原文。
- `len` 是字符数，不是 token 数；中英文比例不同。
- 行号会随源文件增删变化；引用时用 `id`。
- 跨项目不去重：同一句提示词出现在两个项目里，是两条记录。
- 若 `get` 报“第 N 行不存在”，说明源文件变了，重跑 `tools/build_catalog.py`。

## 6. 重建

```bash
python tools/build_catalog.py
```

只读源文件，不修改 `sources/`。重建后跑 `python tools/validate_kb.py`。
