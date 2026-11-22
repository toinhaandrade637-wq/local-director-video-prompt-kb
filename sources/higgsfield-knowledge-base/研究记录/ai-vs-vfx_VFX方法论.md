# ai-vs-vfx 官方 VFX 合成方法论（16 块）

> 收割 G5（E177）｜来源：官博提示词块全集 slug=ai-vs-vfx，16 块共 ~90K 字符
> **官方 VFX 合成提示词方法论**：龙+骑士+瀑布+洞穴的完整 VFX 场景，全部单镜头连续拍摄。

## 核心方法

### 1. VFX 单镜头铁律 [官方 块14 原文 19,430c]
> `ONE UNBROKEN CONTINUOUS SHOT — a single take with zero cuts`

**VFX 镜头绝不切割**——任何剪辑点都会破坏合成视觉。与叙事视频的多镜头相反，VFX 必须一镜到底。

### 2. UUID 引用标签体系 [官方 全部]
@waterfall_location_v1 / @dragon_v1 / @adil_sheet_v2 / @cave_test / @video1——每个参考件有唯一 UUID 标签，全篇按标签引用。

### 3. 动作链编排 [官方 块14]
> `the dragon gives one quick dog-like head-shake, its trailing fan of spray sweeps back and drenches Adil's face... he sputters a startled "oh-oh-oh!", clamps down in real fear... steals a glance at the drop, risks a one-hand face-wipe and presses himself flatter — then a smile blooms and breaks into a raw, joyful adrenaline yell, he gives the dragon's neck two light grateful pats`

**动作链 = 逐个物理动作**（摇头→溅水→擦脸→瞥一眼→微笑→拍脖子→加速→离画）——每个动作有明确的物理后果和情感递进。

### 4. 生物比例类比 [官方 块15]
> `wingspan of fourteen men laid head to toe, heavy as five elephants`

**不用数字**（wingspan 14m），而用**人体类比**（14 men / 5 elephants）——模型理解人体尺度比理解公制单位更准确。

### 5. 情感弧线内嵌于 VFX [官方 块12]
> `genuinely scared, wrestling his own fear out loud before jumping... a false start he aborts, a shaky laugh at himself, one last deep inhale-exhale — and he explodes into a sprint`

VFX 镜头也有**情感弧线**（恐惧→犹豫→自我鼓励→爆发）——不是纯特效展示而是有戏剧内核的合成镜头。

### 6. 瀑布物理整合 [官方 块12]
> `a deep constant roar filling the cave, fine spray drifting in on the air, mist hanging in the bounce light, wet gleam on the gravel`

瀑布不在画面里但**其存在通过四感传达**：听觉（roar）/触觉（spray）/视觉（mist + bounce light）/地面（wet gleam）。

## 七组块概要

| 块 | 字数 | 内容 |
|---|---|---|
| 1 | 163 | 角色表请求（3 角度） |
| 2 | 1,153 | 龙三面板角色表 |
| 3 | 2,397 | V2V 角色替换 |
| 4 | 1,241 | 场地标定（瀑布峡谷） |
| 5 | 2,035 | @video1 背景底版声明 |
| 6 | 2,307 | 三面板合并角色表 |
| 7 | 5,988 | 6s 无人机推入瀑布 |
| 8 | 2,118 | 三面板角色表（变化） |
| 9 | 1,950 | 编辑：加入骑士 |
| 10 | 2,996 | 8K IMAX 风格声明 |
| 11 | 2,669 | 反角度同场地 |
| **12** | **17,799** | **洞穴内瀑布后连续镜头（恐惧→跳跃）** |
| 13 | 4,834 | 8K IMAX 风格（峡谷版） |
| **14** | **19,430** | **穿瀑布而出+骑龙飞离（一镜到底）** |
| 15 | 9,226 | 峡谷追逐→180° 转身揭示 |
| 16 | 7,897 | 8K IMAX 风格（峡谷追逐版） |

## VFX 块频 [全部 16 块]

ACTIVE REFERENCES×12 / SCENE CONTEXT×12 / 100% matches×12 / CAMERA×10 / LIGHTING×8 / STYLE×8
