# video-prompt-library · 入口

> 977 条多模型视频提示词：主库成片级提示词 + 通用区词典 + 教程区。原库有严格的追加与校验规则。

## 1. 规模

| 分区 | 条数 | 用途 |
|---|---:|---|
| 主库 | 339 | 可直接改写的成片级完整提示词，按题材分类 |
| 通用区 | 633 | 运镜、器材、演技、构图等可复用零件 |
| 教程区 | 5 | 完整工作流案例 |

模型分布：Seedance 2.0 × 268、Seedance 2.5 × 60、可灵 3.0 × 6、海螺 H3 × 5、未标注 × 638（多为通用区词典）。

## 2. 文件

| 文件 | 内容 |
|---|---|
| `AI-全库.jsonl` | 全量条目，每行一条，含 `original` 逐字原文与 `zh` 译文 |
| `AI导读索引.md` | 原库的轻量导读，一行一条摘要 |
| `README.md` | 原库完整手册：铁律、流程、分类、坑清单 |
| `AGENTS.md` | 原库的 AI 作业卡 |
| `视频提示词库-多模型.html` | 网页版，含 data / general / tutorials 三块 |
| `已入库/` | 历史批次原件与 URL 引用 |
| `待入库/` | 待自动入库的 JSON |
| `*.py` | 原库的追加、校验、勘误、导出脚本 |

## 3. 一条记录

```json
{"区":"主库","id":"sd2-259","model":"Seedance 2.0","cat":"动作·打斗","sub":"近身·格斗",
 "name":"雪地女特工·近身搏斗","desc":"冬季战术女特工雪地基地近身格斗，冲击波纹与呼白气","tags":["格斗","特工","雪地","写实"],
 "lang":"zh","original":"激烈的近距离格斗片段……","zh":"","src":"……"}
```

字段说明见 [docs/04-字段与格式](../../docs/04-字段与格式.md)。

## 4. 怎么读

```bash
python tools/kb.py search --source vpl --zone 主库 --cat "动作·打斗" --limit 10
python tools/kb.py search --source vpl --zone 通用区 --cat "运镜词典" --limit 10
python tools/kb.py get --id VPL-sd2-259
```

## 5. 原库铁律（不要破坏）

1. 只追加，不删改老条目；修正走 `勘误更新.py`。
2. `original` 逐字不可变，有 SHA-256 指纹。
3. 一切写入走 `追加提示词.py`，禁止手改 data / meta 块。
4. `main` 是唯一真源，改前拉最新，改后回读校验。
5. 通用区 / 教程区走 `扩展区工具.py`，不能投给 `追加提示词.py`。

本库只做**快照与索引**，不参与原库的写入流程。要新增条目，回原库按上述规则操作，再同步过来。

## 6. 来源

`YIJUEYIJUE/video-prompt-library`，commit `2b5c36c`（2026-11-01）。

原库未声明开源许可证；本库只做学习与检索，权利归原作者。

## 7. 相关

- 分区与分类树：[catalog/video-prompt-library.md](../../catalog/video-prompt-library.md)
- 单条索引：[catalog/video-prompt-library.index.jsonl](../../catalog/video-prompt-library.index.jsonl)
