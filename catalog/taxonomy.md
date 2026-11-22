# 分类与命名口径

> 索引里的 `cat` / `type` / `model` / `id` 是怎么来的、能信到什么程度。读数据前先看这一页。

## 1. 三个层级

| 层级 | 例子 | 含义 |
|---|---|---|
| 来源 source | `sources/higgsfield`、`sources/video-prompt-library` | 一份独立语料 |
| 项目 project | `DETOUR`、`VPL 主库` | 一部片子 / 一个库分区 |
| 条目 entry | `HFX-DETOUR-000166`、`VPL-sd2-259` | 一条可独立取用的提示词 |

## 2. `cat`：提示词属于哪类素材

| 值 | 含义 | 条目数 | 有该类目的项目数 |
|---|---|---:|---:|
| `all` | 上游只有全量文件，未能细分 | 136,169 | 545 |
| `assets` | 图生视频素材、重跑、局部修改 | 32,087 | 71 |
| `scenes` | 分镜 / 镜头 / 场面调度 | 4,109 | 6 |
| `props` | 道具、车辆、武器、产品 | 1,226 | 3 |
| `characters` | 角色设定 | 509 | 1 |
| `locations` | 场景、空间、光线、天气 | 304 | 1 |

### 重要限制

- **537 个项目只有 `all`。** 上游数据包里这些项目只提供 `_all_prompts.jsonl`，没有分类文件，无法可靠拆分。
- 只有 **DETOUR** 一个项目同时具备五类细分；`scenes` 细分只覆盖 6 个项目。
- 因此：`--cat scenes` 返回 0 条是正常现象，不代表库里没有相关内容。去掉 `--cat`，改用 `--keyword`。

### 归类优先级

同一项目内，一条提示词若同时出现在多个分类文件，按以下顺序取第一个：

```text
scenes > characters > locations > props > assets > cover > all
```

原因是分镜与角色设定比“素材重跑”更有创作参考价值。

## 3. `type`：图片还是视频

| 值 | 判断方式 |
|---|---|
| `video` | 模型名以 `seedance_`、`cinematic_studio_video`、`kling3`、`kling_o3`、`veo`、`wan`、`grok_video`、`minimax_h3`、`flux_3_video`、`soul_cinema`、`soul_cinematic`、`hf_mult_motion_control` 开头 |
| `image` | 模型名含 `image`、`seedream`、`nano_banana`、`recraft`、`flux`、`grok_image` |
| 空 | 模型未标注，无法判断 |

`type` 是由模型名推断的，不是上游原字段。同一段文字用图片模型和视频模型各跑一次，会得到两条不同 `type` 的记录。

## 4. `model`：模型名保留上游原样

Top 12：

| 模型 | 条目数 | 说明 |
|---|---:|---|
| `default` | 45,467 | 平台自动选择，**不是具体模型** |
| `seedance_2_5` | 14,907 | Seedance 2.5 |
| `seedance_2_0` | 13,585 | Seedance 2.0 |
| `videotape-alpha` | 12,874 | 平台内测视频模型 |
| `seedream_v5_pro` | 6,945 | 即梦图片模型 |
| `nano_banana_2` | 5,157 | 图片模型 |
| `video_extension` | 3,927 | 视频延长，不是独立生成 |
| `gpt_image_2` | 3,085 | 图片模型 |
| `text2image_soul_v2` | 1,713 | 图片模型 |
| `soul_cinematic` | 1,287 | 视频模型 |
| `cinematic_studio_video_4_0` | 966 | 视频模型 |
| `sunburst` | 831 | 平台视频模型 |

完整分布见 [higgsfield-models.json](higgsfield-models.json)。

### 使用建议

- 写 Seedance 2.5，优先筛 `seedance_2_5`；写 2.0，筛 `seedance_2_0`。
- `default` 的写法可以参考结构，但不能拿它推断模型能力。
- `video_extension` 是延长任务，不是完整镜头，别当分镜模板。
- 模型名有大小写与别名差异（VPL 里是 `Seedance 2.0`），跨来源检索时不要写死一种写法。

## 5. `id`：稳定定位

| 来源 | 格式 | 例子 |
|---|---|---|
| Higgsfield | `HFX-<项目>-<六位行号>` | `HFX-DETOUR-000166` |
| video-prompt-library | `VPL-<原库 id>` | `VPL-sd2-259` |

- `HFX` 的行号指向 `sources/higgsfield/prompts/<项目>/prompts.jsonl.gz` 的第 N 行（1-based）。
- 行号会随源文件增删变化；引用时写 `id`，不要只写行号。
- `VPL` 的 id 来自原库，重跑索引不会变。

## 6. 五个常见误读

| 误读 | 实际 |
|---|---|
| “`default` 是一个模型” | 是“平台自动选择”的占位值 |
| “`all` 是没分类的垃圾” | 是上游只给了全量文件，内容完整，只是没有细分 |
| “`assets` 可以直接当分镜” | 多数是素材重跑与局部修改，叙事不完整 |
| “一条记录 = 一个镜头” | 长记录常含多个镜头，看 00:00–00:15 这样的时间码 |
| “同 ID 前缀就是同一部片” | `HFX-` 后是项目名，不同项目可能同名不同片 |

## 7. 判断一条提示词适不适合参考

按顺序问四个问题：

1. **模型对得上吗？** 写 2.5 就看 2.5；跨代参考只学结构。
2. **题型对得上吗？** 单镜、整场、角色设定、素材重跑，不能混。
3. **长度量级对吗？** 200 字的零件句和 8,000 字的完整段落，用法完全不同。
4. **项目目标接近吗？** 广告的节奏套不进文艺片，反之亦然。

四条都过，再读原文；只过一两条，只学局部笔法。

## 8. 相关文件

- 项目总表与覆盖：[higgsfield-projects.md](higgsfield-projects.md)
- 模型与类别分布：[higgsfield-models.json](higgsfield-models.json)
- 字段逐项说明：[docs/04-字段与格式](../docs/04-字段与格式.md)
- 检索写法：[docs/03-检索手册](../docs/03-检索手册.md)
