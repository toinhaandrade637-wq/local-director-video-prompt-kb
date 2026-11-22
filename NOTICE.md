# NOTICE · 来源与使用边界

本仓库是**学习与创作参考用的提示词语料库**，不是商业发行物。

- 主仓库：https://github.com/toinhaandrade637-wq/local-director-video-prompt-kb

## 1. 内容来源

| 来源 | 路径 | 状态 |
|---|---|---|
| Higgsfield 611 项目全量提示词 | `sources/higgsfield/` | 本地工作区公开项目数据整理 |
| Higgsfield 三轨方法库 | `sources/higgsfield-knowledge-base/` | 来自公开仓库 toinhaandrade637-wq/higgsfield-knowledge-base |
| 官方教程 / 创作者博客 / brief / 技能包 | `sources/experience/` | Higgsfield 官网与创作者公开发布内容的文本存档 |
| video-prompt-library | `sources/video-prompt-library/` | 来自公开仓库 YIJUEYIJUE/video-prompt-library |
| Seedance 2.5 知识库 | `sources/seedance25-knowledge-base/` | 原私有库，经库主确认后公开 |
| 通用技能仓 | `sources/skills-repo/` | 原私有库 YIJUEYIJUE/skills，经库主确认后公开 |

## 2. 权利

- 原始提示词、教程、博客、图片、视频的著作权归原作者与平台所有。
- 本仓库不主张对上述原文的著作权，只提供整理、索引与检索结构。
- 仓库中由整理者撰写的说明文件（README、AGENTS、docs、catalog 说明、tools）采用 MIT 许可，详见 `LICENSE`。

## 3. 使用边界

- 可以：学习、检索、改写、作为创作参考、训练内部工作流。
- 不可以：把原文整段作为自己的原创发表；移除原作者署名；用于违法或侵权内容。
- 商业使用前，请自行确认对应原始内容的授权条款。

## 4. 下架与更正

如果你是权利人，认为某部分内容不应公开：

1. 在 GitHub 提 Issue，标题写「下架请求」。
2. 注明具体路径或 ID（如 `HFX-DETOUR-000123`、`VPL-sd2-240`）。
3. 说明权利依据。

确认后会尽快移除对应内容，并同步更新 `catalog` 索引。

## 5. 数据准确性

- 语料来自公开页面与既有整理，**不保证每条提示词都经过生成验证**。
- 模型名、分类、时长等字段保留上游原样，可能存在空值、别名或错误。
- 索引由 `tools/build_catalog.py` 生成；发现计数或定位错误，请提 Issue。
