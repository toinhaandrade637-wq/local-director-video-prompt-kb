# sources · 来源快照

> 原文层。**只读**，不改写、不删减内容；整理与裁剪规则见本页。

## 1. 六个来源

| 目录 | 来源 | 内容 | 处理 |
|---|---|---|---|
| `higgsfield/` | 本地工作区 `02_完整提示词数据包` + 78 项目 GitHub 仓 | 611 项目去重提示词、brief、README、官方 Skill | 项目内去重；提示词压缩为 `prompts.jsonl.gz` |
| `higgsfield-knowledge-base/` | `toinhaandrade637-wq/higgsfield-knowledge-base` | 视频 8 页 + 生图 2 页 + 通用 4 页、研究记录、维护台账、Skill 果实层 | 原样同步，去掉 `.git` / `.mimosa` |
| `experience/` | 本地工作区 `03_全流程方法论` + `05_经验类内容` | 官方教程、创作者博客、项目 brief、官方技能包、全流程方法论 | **只收文本**（md/txt/json/jsonl）；图片、PDF、ZIP、视频不收 |
| `video-prompt-library/` | `YIJUEYIJUE/video-prompt-library` | 主库 / 通用区 / 教程区、原库手册、脚本 | 原样同步，去掉 `.github` |
| `seedance25-knowledge-base/` | 原私有库 `seedance25-knowledge-base` | 方法、资料库、研究记录、维护、Skill | 原样同步，去掉 `.github` |
| `skills-repo/` | 原私有库 `YIJUEYIJUE/skills` | 5 个技能目录 + README | 原样同步 |

## 2. Higgsfield 的裁剪与压缩

原始数据包每个项目有多个重叠文件（`all_assets` / `all_unique_prompts` / 分类文件 / 分场景文件），合计 3.9 GB、547,274 行。

处理规则：

1. 逐项目读取全部 `*.jsonl`，取 `prompt` 字段。
2. 项目内按提示词原文 MD5 去重。
3. 按文件类型归入 `cat`，优先级：`scenes` > `characters` > `locations` > `props` > `assets` > `cover` > `all`。
4. 只保留 `id / cat / type / model / prompt` 五个字段。
5. 每项目输出一份 `prompts.jsonl.gz`（UTF-8，每行一条 JSON）。

结果：174,404 条唯一提示词，816 MB 原文，214 MB 压缩。

**没有丢弃任何项目级内容**：brief、README、官方 Skill 单独放在 `higgsfield/projects/<项目>/`。

## 3. 去重口径

| 范围 | 是否去重 | 原因 |
|---|---|---|
| 同一项目内 | 是 | 同一提示词会同时出现在全量文件与分类文件 |
| 跨项目 | 否 | 不同项目复用同一句是有效信息（可看谁抄谁、谁在迭代） |
| 同一项目不同模型 | 否 | 同一段文字用不同模型跑，是不同记录 |

## 4. 编码与换行

- 全部 UTF-8。
- JSONL 一行一条，行内不换行。
- 原文中的 CRLF 保留为 `\r\n` 转义。
- 少数上游文件有 U+FFFD 替换字符，保留原样，不静默修复。

## 5. 没有收进来的东西

| 内容 | 原因 | 去哪找 |
|---|---|---|
| 项目封面图、生成结果图、视频 | 体积大，且不影响提示词检索 | 原 Higgsfield 项目页 |
| PDF 教材、ZIP 技能包、Academy 视频 | 二进制，GitHub 不适合放 | 本地工作区 `05_经验类内容` |
| `.mimosa` 会话缓存 | 工具运行时缓存，不是知识 | — |
| `_legacy_作废_深读笔记系` | 已作废的旧体系 | 本地工作区 `06_知识库` |
| `tmp_batch3_out` | 批次中间产物 | 本地工作区 |
| 78 项目仓的重复 JSONL | 已被 611 项目全量语料覆盖 | `sources/higgsfield/prompts/` |

## 6. 校验

```bash
python tools/validate_kb.py
```

会检查：每个项目的压缩文件行数与索引一致、Markdown 链接可解析、没有令牌/密钥、文档不含本机绝对路径。
