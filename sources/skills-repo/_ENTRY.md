# 通用技能仓 · 入口

> 5 个独立技能的上游快照。顶层 `skills/` 是可直接加载的副本，这里保留原始目录与 README。

## 1. 有什么

| 技能 | 用途 |
|---|---|
| `skills/character-asset-sheet` | 角色设定集 / 三视图 prompt 模板 |
| `skills/prop-asset-sheet` | 道具设定集 / 三视图 prompt 模板 |
| `skills/fountain-screenplay` | 专业 `.fountain` 剧本 |
| `skills/suno-music-prompts` | Suno 音乐提示词 + 知识图谱 |
| `skills/image-text-transcript` | 图片垂直解析 |

每个目录含 `SKILL.md`、`package.json`，部分带 `icon.jpg` 与 `references/`。

## 2. 和顶层 skills/ 的关系

| 位置 | 角色 |
|---|---|
| `sources/skills-repo/` | 上游原文快照，不动 |
| `skills/` | 加载用的工作副本，可补充本库自己的技能 |

两者内容一致时以 `sources/` 为准；本库新增的技能只在 `skills/`。

## 3. 怎么用

直接读对应 `SKILL.md`，或把整个目录放进宿主的技能目录。

完整清单与选择建议见 [skills/README.md](../../skills/README.md)。

## 4. 来源

原私有库 `YIJUEYIJUE/skills`，commit `f6e283e`（2026-11-05）。原 README 见 [README.md](README.md)。
