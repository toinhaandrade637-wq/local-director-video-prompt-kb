---
name: character-asset-sheet
displayName: 人物资产图模板
description: 人物资产设定集模板——把一句角色描述组装成生产级「角色设定集 / 三视图 turnaround」生图 prompt。当用户要生成或设计一个角色(人物)的资产图、设定集、三视图、立绘、角色概念图，或提到「人物资产、角色设定、character sheet、turnaround、正面/侧面/背面、身高标尺」时使用。内置硬约束模板(纯白背景 + 多视图分栏 + 身高标尺 + 无文字无阴影无水印)，组装公式 =【主体描述】+【强约束模板】。默认只产出结构化 prompt，不主动消耗生图额度。
version: 1.0.0
subCategory: asset
subCategoryLabel: 资产
---

# 人物资产图模板

## Overview

把一句角色描述，组装成生产级「角色设定集 / 三视图 turnaround」生图 prompt。模板锁定五项硬要素——**纯白背景、多视图分栏、身高标尺、无文字无水印、无投影无场景**，保证同一角色在每一格面板中完全一致（不换脸、不换装、不漂移）。

## 触发条件

- 要生成角色的资产图 / 设定集 / 三视图 / 立绘 / 角色概念图
- 提到「人物资产、角色设定、character sheet、turnaround、正/侧/背面、身高标尺」等任一说法

## 组装公式

```
最终 prompt = [主体描述（角色外貌/年龄/气质/服饰，1-2 句）] + "\n\n" + [强约束模板]
```

> 模板段必须**原样拼接**，禁止用「主角设定图」「XX 真人写实版」这类简化描述替代——模型只会照它收到的原文画。

## 强约束模板（复制即用，英文原文）

```
Character design reference sheet, multi-angle turnaround on a clean pure white studio background. Layout: a large front-facing close-up portrait panel (head and shoulders, tall vertical block on the left), two smaller stacked portraits next to it (3/4 view and full side profile, same head and shoulders), and on the right half two full-body turnaround figures — front view and back view — standing in a relaxed neutral pose, feet slightly apart, arms hanging naturally. A vertical height scale ruler with even tick marks and numeric labels runs along the very right edge of the canvas, baseline-aligned with the full-body poses so the figure's feet sit at zero on the ruler. Even soft studio lighting, no cast shadow on the background, photorealistic rendering, production-grade concept art style, identical character across every panel, thin clean dividing lines between panels, no scenery, no environment, no extra props, no logo, no watermark, no decorative border, no text on the canvas except the numeric labels on the height ruler.
```

## 约束拆解（模板锁定了什么）

| 硬约束                                             | 作用                           |
| -------------------------------------------------- | ------------------------------ |
| clean pure white studio background                 | 纯白无缝底，方便抠图入库       |
| 左：正面头部特写 / 中：3/4 + 侧脸 / 右：正背面全身 | 固定 5 格分栏，锁定多视图结构  |
| vertical height scale ruler + feet sit at zero     | 身高标尺，脚底对齐 0 刻度      |
| identical character across every panel             | 强制跨面板一致（不换脸不换装） |
| no cast shadow / no scenery / no props             | 无投影、无场景、无道具         |
| no logo / no watermark / no border                 | 无水印无装饰边框               |
| no text except numeric labels                      | 画布除标尺数字外无任何文字     |

## 可调参数（写进「主体描述」）

- **外貌**：年龄、性别、发型发色、脸型、五官、表情
- **气质**：气场、神态（如「温和的中年母亲」「冷峻的特工」）
- **服饰**：服装风格、配色、材质、配饰
- **风格**：photorealistic 已锁定，如需二次元/国漫/赛璐璐可在此声明（会覆盖模板的 photorealistic 段）
- **身高数值**：如需锁定具体身高，在主体描述中说明（如「身高 170cm」），标尺刻度随之对齐

## 出图后质检铁律

每张出图后核对，缺任一项即用同一 prompt 重出：

1. ① 纯白背景 #FFFFFF
2. ② 5 格分栏（头部特写 / 3-4 侧 / 正侧脸 / 正面全身 / 背面全身）
3. ③ 右侧身高标尺，脚底对齐 0 刻度
4. ④ 同一角色跨面板一致，无文字无水印无投影

## 与其他 skill 的关系

本 skill 是独立的人物资产模板，可单独调用；也供 `ai-ad-drama-studio` 模块 5（资产生成）复用为人物设定集的强约束段。
