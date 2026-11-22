# 技能清单

> 8 个可直接加载的技能 + 1 个官方技能文本目录。每个技能都是独立目录，入口为 `SKILL.md`。

## 1. 写作类

| 技能 | 解决什么问题 | 入口 | 不做什么 |
|---|---|---|---|
| `seedance-prompt` | 按 Seedance 2.5 写、改、检查视频提示词；含 12 页方法参考 | [SKILL.md](seedance-prompt/SKILL.md) | 不替你从零编故事 |
| `hf-video-prompt` | Higgsfield 视频工艺：结构、运镜、动作打戏、多主体、VFX、声音 | [SKILL.md](hf-video-prompt/SKILL.md) | 同上 |
| `hf-image-prompt` | Higgsfield 生图工艺：Plate Master 结构、色彩 HEX、质感与后期 | [SKILL.md](hf-image-prompt/SKILL.md) | 不做视频分镜 |

## 2. 资产类

| 技能 | 解决什么问题 | 入口 |
|---|---|---|
| `character-asset-sheet` | 把一句角色描述组装成生产级角色设定集 / 三视图 prompt | [SKILL.md](character-asset-sheet/SKILL.md) |
| `prop-asset-sheet` | 把一句道具描述组装成生产级道具设定集 / 三视图 prompt | [SKILL.md](prop-asset-sheet/SKILL.md) |

两个资产技能默认**只产出结构化 prompt，不消耗生图额度**。硬约束：纯白背景、多视图分栏、比例标尺、无文字无阴影无水印。

## 3. 剧本与音乐

| 技能 | 解决什么问题 | 入口 |
|---|---|---|
| `fountain-screenplay` | 建 / 改带场次轨与台词块的 `.fountain` 专业剧本 | [SKILL.md](fountain-screenplay/SKILL.md) |
| `suno-music-prompts` | Suno v5.5 音乐提示词：曲风、乐器、人声、BPM、结构、分轨 | [SKILL.md](suno-music-prompts/SKILL.md) |

`suno-music-prompts` 内嵌音乐知识图谱：246 条曲风 × 19 大类、24 种语言、80 个人声标签、799 条乐器×技法 × 17 个家族、20 种曲式结构。

## 4. 图像解析

| 技能 | 解决什么问题 | 入口 |
|---|---|---|
| `image-text-transcript` | 把图片解析成结构化所见：概述、文字原样转录、主体、场景、布局 | [SKILL.md](image-text-transcript/SKILL.md) |

只做垂直解析，看不清就写“看不清”，不推测、不补全。

## 5. 官方技能文本

| 目录 | 内容 |
|---|---|
| `higgsfield-official/` | 11 套官方技能文本：acting、fight-scene、prompt-engine、seedance-prompt、shotlist-director、shotlist-builder、seedance-footage-vfx、seedance-director、prompt-builder-2-5、prompt-writter、cineimage-soul，另有 ADMAKER、client-finder、motion、timed-prompts、ugc 等单页 |

入口：[higgsfield-official/_索引.md](higgsfield-official/_索引.md)

这些是**上游原文**，用于查官方口径；日常写作优先用上面 8 个成品技能。

## 6. 怎么选

```text
写视频提示词 → seedance-prompt（Seedance 2.5）或 hf-video-prompt（Higgsfield 通用）
写生图提示词 → hf-image-prompt
做角色 / 道具资产表 → character-asset-sheet / prop-asset-sheet
建剧本 → fountain-screenplay
写音乐 → suno-music-prompts
读图 → image-text-transcript
查官方怎么说 → higgsfield-official/
```

## 7. 加载方式

技能目录可以整体放入宿主的技能目录（如 `.claude/skills/`、`.codex/skills/`），或直接把 `SKILL.md` 作为提示词读入。

`package.json` 是给支持技能市场的宿主用的元数据，不影响手动加载。

## 8. 机器可读清单

见 [catalog/skills.json](../catalog/skills.json)：名称、入口路径、描述、文件数。
