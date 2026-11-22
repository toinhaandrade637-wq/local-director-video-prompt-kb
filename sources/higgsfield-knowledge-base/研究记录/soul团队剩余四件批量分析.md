# 官方小品组续：soul 团队剩余四件批量分析

> 收割 #5（E159）｜REWIND_CLUB 71 / SPACE_CHORES 22 / GOTHIC_BEACH 48 / CAT_STORY 1,169

## 一、CAT_STORY（1,169 行，soul 最大，5.8× 迭代）

### 结构化模板 + POSITIVE LOCKS 命名法则全量实证

FORMAT MODE×988 / POSITIVE LOCKS×986 / SCENE CONTEXT×960 / ACTIVE REFERENCES×935 / PHYSICS×604

**POSITIVE LOCKS 内部结构**（代表 4,703c 逐字分析）：
- `LOCATION MAP + 180-DEGREE LINE`——空间地理+轴线法则合并块
- `LENS LOCKS: SEGMENT 1 = telephoto detail insert, razor-thin focus. SEGMENT 2 = standard normal.`——逐段镜头锁
- `SHOT-BY-SHOT (edited sequence)`——逐镜分段（SEGMENT 1 | 0.0s to 5.0s | HARD CUT out at 5.0s）

**细粒度立法**（全库最深）：
> `The bandage is applied to her right cheek specifically, not the left. The application in Segment 1 is quick and efficient — one motion, one press, done — not a slow, repeated smoothing or lingering gesture.`

**侧面/方向立法**：左颊 vs 右颊、动作次数、速度、重复性全部锁定。

## 二、GOTHIC_BEACH（48 行，结构化模板 + 三区分解）

CAMERA×101 / OPTICS×92 / PHYSICS×53 / ACTION×49 / LOCATION MAP×29

### ACTIVE REFERENCES 角色分工声明 [官方]
> `<<<image_1>>> — Reference controls face identity, hair, and full outfit throughout. Reference does not control beach environment or lighting color.`
> `<<<image_2>>> — Reference controls environment, color saturation, and atmospheric brightness.`
> `<<<image_3>>> — Reference controls umbrella design. In this scene it stays closed under her arm for the entire shot.`

**每个 UUID 显式声明"控制什么/不控制什么"**——参考分工精细化到单一道具级别。

## 三、REWIND_CLUB + SPACE_CHORES

- REWIND_CLUB（71 行，散文体，1.0× 迭代）：无命名块，直接叙事，最低复杂度
- SPACE_CHORES（22 行，SUBJECT LOCK×2 / SHEET LAYOUT×2）：角色锁+表布局块，微型项目

## 四、soul 团队模板家族谱系

| 项目 | 行数 | 块型 | 复杂度 |
|---|---|---|---|
| CAT_STORY | 1,169 | FORMAT MODE+POSITIVE LOCKS+SCENE CONTEXT+ACTIVE REFERENCES+PHYSICS | ★★★★★ |
| SOUL_ANGEL | 500 | ACTING TASK+TACTIC+OBSTACLE+MOTIVE+FORMAT.4+SHOT 1-8+CUT LIST | ★★★★ |
| GOTHIC_BEACH | 48 | SCENE CONTEXT+ACTIVE REFERENCES+LOCATION MAP+CAMERA+OPTICS+PHYSICS | ★★★ |
| REWIND_CLUB | 71 | 散文体（无命名块） | ★ |
| SPACE_CHORES | 22 | SUBJECT LOCK+SHEET LAYOUT | ★ |

同一团队在不同体量项目上使用不同复杂度的模板——**模板复杂度与项目体量正相关**。

## 五、新增方法 → K 页生长

1. **POSITIVE LOCKS 三块合并**（LOCATION MAP+轴线 / LENS LOCKS / SHOT-BY-SHOT）→ K03 重建时纳入
2. **UUID 角色分工声明**（"Reference controls X. Does not control Y."模式）→ K02 重建时纳入
3. **侧面/方向立法**（right cheek not left / one motion one press）→ K04 重建时纳入
4. **模板复杂度与项目体量正相关**——soul 团队谱系表 → 全量收割计划方法论注记
