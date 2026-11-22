---
name: prop-asset-sheet
displayName: 道具资产图模板
description: 道具资产设定集模板——把一句道具描述组装成生产级「道具设定集 / 三视图 turnaround」生图 prompt。当用户要生成或设计一个道具、物品、武器、载具、服装单品的资产图、设定集、三视图、道具概念图，或提到「道具资产、道具设定、prop sheet、turnaround、顶视/侧视、比例标尺」时使用。内置硬约束模板(纯白背景 + 多视图分栏 + 比例标尺 + 无文字无阴影无水印)，组装公式 =【主体描述】+【强约束模板】。默认只产出结构化 prompt，不主动消耗生图额度。
version: 1.0.0
subCategory: asset
subCategoryLabel: 资产
---

# 道具资产图模板

## Overview

把一句道具描述，组装成生产级「道具设定集 / 三视图 turnaround」生图 prompt。模板锁定五项硬要素——**纯白背景、多视图分栏、比例标尺、无文字无水印、无投影无环境**，保证同一道具在每个视角面板中完全一致（不臆造部件、配色、尺寸）。

## 触发条件

- 要生成道具/物品/武器/载具/服装单品的资产图 / 设定集 / 三视图 / 概念图
- 提到「道具资产、道具设定、prop sheet、turnaround、顶视/侧视、比例标尺」等任一说法

## 组装公式

```
最终 prompt = [主体描述（道具外观/材质/配色/尺寸，1-2 句）] + "\n\n" + [强约束模板]
```

> 模板段必须**原样拼接**，禁止用「宝矿力商品图」这类简化描述替代。若道具需与实物严格一致（如真实商品），须在主体描述中声明「以参考图为准」，并走图生图附参考图。

## 强约束模板（复制即用，英文原文）

```
Prop design reference sheet, multi-angle turnaround on a clean pure white studio background. Layout: a large front-facing close-up view of the prop (tall vertical block on the left), two smaller detail panels stacked next to it (3/4 angled view and top-down view), and on the right half a full-scale front view and side view of the prop standing upright on a flat ground plane. A vertical height scale ruler with even tick marks and numeric labels runs along the very right edge of the canvas, baseline-aligned with the prop's bottom edge so the zero sits at the base. Even soft studio lighting, no cast shadow on the background, photorealistic rendering, production-grade concept art style, identical prop across every panel, thin clean dividing lines between panels, no scenery, no environment, no extra props, no logo, no watermark, no decorative border, no text on the canvas except the numeric labels on the height ruler.
```

## 约束拆解（模板锁定了什么）

| 硬约束                                               | 作用                                   |
| ---------------------------------------------------- | -------------------------------------- |
| clean pure white studio background                   | 纯白无缝底，方便抠图入库               |
| 左：正面特写 / 中：3/4 角度 + 顶视 / 右：正面 + 侧面 | 固定 5 格分栏，锁定多视图结构          |
| height scale ruler + zero sits at the base           | 比例标尺，底部对齐 0 刻度              |
| identical prop across every panel                    | 强制跨面板一致（不臆造部件/配色/尺寸） |
| no cast shadow / no environment / no extra props     | 无投影、无环境、无额外道具             |
| no logo / no watermark / no border                   | 无水印无装饰边框                       |
| no text except numeric labels                        | 画布除标尺数字外无任何文字             |

## 可调参数（写进「主体描述」）

- **外观**：形状、结构、部件细节
- **材质**：金属 / 木质 / 塑料 / 布料 / 玻璃等
- **配色**：主色、辅色、表面纹理
- **尺寸**：如「总高 30cm」，标尺刻度随之对齐
- **风格**：photorealistic 已锁定，如需手绘/三渲二/赛璐璐可在此声明（会覆盖模板的 photorealistic 段）
- **与实物一致性**：真实商品须声明「以参考图为准」并走图生图

## 出图后质检铁律

每张出图后核对，缺任一项即用同一 prompt 重出：

1. ① 纯白背景 #FFFFFF
2. ② 5 格分栏（正面特写 / 3-4 角 / 顶视 / 正面 / 侧面）
3. ③ 右侧比例标尺，道具底部对齐 0 刻度
4. ④ 同一道具跨面板一致，无文字无水印无投影

## 与其他 skill 的关系

本 skill 是独立的道具资产模板，可单独调用；也供 `ai-ad-drama-studio` 模块 5（资产生成）复用为道具设定集的强约束段。
