# 变更记录

## v1.1.0 · 2026-11-22 · 结构整理与迁移

**迁移**

- 公开仓库从 `YIJUEYIJUE` 迁到 `toinhaandrade637-wq/local-director-video-prompt-kb`。
- 旧仓保留只读，避免两处同时维护；内容以本仓为准。

**新增导航**

- `START-HERE.md`：5 分钟上手，三条路线 + 五个高频动作 + 三个数据事实。
- `docs/00-文档地图.md`：每份文档解决什么问题、谁读、什么时候读。
- `docs/07-检索案例.md`：8 个真实查询，从需求到结果到下一步。
- `docs/08-构建与校验报告.md`：本次构建的数字、校验项、已知限制。
- `catalog/taxonomy.md`：类别、类型、模型、ID 的口径与边界。
- `catalog/higgsfield-projects.csv`：项目总表的表格视图。
- `skills/README.md`：8 个技能 + 官方文本清单与选择建议。
- 六个来源各加 `_ENTRY.md`：规模、先读什么、怎么读、注意。
- `MANIFEST.json`：顶层目录的用途、文件数、入口，由构建脚本生成。
- `NOTICE.md` 与 `LICENSE`：来源、权利、下架流程与许可。

**修正**

- 删除 `methods/` 下的重复副本，改为单一导航页；方法正文只保留 `sources/*/现行知识/`，消除 30 处相对链接死链。
- 15 个 brief 文件名不规范的临时目录归并到规范项目目录，`projects/` 与项目名一一对应。
- `higgsfield-projects.json` 的 `docs_path` 改为只在目录真实存在时给出。
- 补齐 `sources/seedance25-knowledge-base/.github/workflows/validate.yml`，修复原库内部链接。
- 技能 references 指向方法库的相对链接改为 canonical 路径。
- 明确记录分类覆盖：537 个项目只有 `all`，只有 6 个有 `scenes`；检索工具在 0 结果时给出提示。

**工具**

- `tools/validate_kb.py` 新增 `--fast`：跳过 611 个项目逐项核对，供 CI 使用。
- `tools/kb.py` 在 0 结果时提示分类覆盖与放宽条件。
- 新增 `.github/workflows/validate.yml`：每次推送跑快速校验。

## v1.0.0 · 2026-11-22 · 首版

**语料**

- 合并 611 个 Higgsfield 项目、174,404 条去重提示词（原文 815.7 MB，压缩 213.6 MB）。
- 合并 977 条 video-prompt-library 条目。
- 合并 Higgsfield 三轨方法库（视频 8 / 生图 2 / 通用 4）。
- 合并 Seedance 2.5 知识库（12 页方法 + 资料库 + 研究记录 + Skill）。
- 合并经验内容：18 篇全流程方法论、419 份官方教程文本、535 篇创作者博客、83 份 brief、81 份官方技能文本。
- 合并通用技能仓 5 个技能。

**索引**

- `catalog/higgsfield-prompts.index.jsonl`：174,404 行。
- `catalog/video-prompt-library.index.jsonl`：977 行。
- 项目总表、模型分布、方法清单、技能清单。

**工具**

- `tools/kb.py`：stats / search / get。
- `tools/build_catalog.py`：重建索引与统计。
- `tools/validate_kb.py`：链接、计数、密钥、绝对路径校验。
