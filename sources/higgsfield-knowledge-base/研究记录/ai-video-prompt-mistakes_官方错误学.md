# ai-video-prompt-mistakes 官方错误学教材（14 块 · 7 对照对）

> 收割 G5（E170）｜来源：官博提示词块全集_63篇402块.jsonl 中 slug=ai-video-prompt-mistakes
> 官方唯一一个以**错误版 vs 正确版对照**形式呈现的教程——每对展示同一场景的错误写法和正确写法。

## 七组对照对

| 对照 | 场景 | 错误版字数 | 正确版字数 | 核心差异 |
|---|---|---|---|---|
| 1 | 篝火五人 | 702c | 2,975c | 无角色描述→5人各28字描述+计数锁+180轴+BLOCKING坐标 |
| 2 | 1950s 慢舞 | 1,283c | 2,213c | "hands blending"→"five separate visible fingers, never fuse" |
| 3 | 拉力赛 | 625c | 3,197c | "epic cinematic 4k"→SCENE CONTEXT+光影+路面+悬挂物理 |
| 4 | 战斗机 | 1,082c | 2,239c | "insane visuals"→一镜到底+ canyon 几何+相机路径 |
| 5 | 山地车广告 | 1,425c | 3,904c | "studio shots then city"→每 shot 独立 lens/FOV/blocking |
| 6 | 美式足球 | 1,378c | 3,240c | "huge touchdown"→snap-line-pass-catch 逐段物理+身体力学 |
| 7 | （更多场景） | ... | ... | ... |

## 七种错误模式（从对照对提取）

1. **质量填充词**：`Very cinematic, emotional, 4k, hyperrealistic, best quality, 8k, award winning` → 替换为可观察特征（`silver-gelatin contrast, deep blacks, fine grain`）
2. **模糊主体**：`A man and some girls` → 替换为 `five distinct people, no repeated face: P1 man 32 dark-blond...`
3. **让模型决定**：`Add more people if it looks better` / `pick the best composition` → 替换为精确计数锁+相机立法
4. **感觉代替规格**：`Cinematic dolly zoom feel, epic reveal` → 替换为 `crane back at constant eye level 1.5m, 40 degree FOV`
5. **情绪标签**：`Warm nostalgic friendship mood, magical atmosphere` → 替换为物理描述（`fire burns like real wood, fast irregular tongues`）
6. **解剖学不可能**：`hands blending as they hold each other` → 替换为 `five separate visible fingers, never fuse`
7. **光照过度**：`Gorgeous sunlight bursting, pulsing god rays` → 替换为具体光源方向+柔和度

## 正确版共性（七组共有）

1. SCENE CONTEXT 开头（具体地点+时间+氛围）
2. CAST/CHARACTERS 块（每人年龄+外貌+服装，计数锁）
3. BLOCKING/位置声明（坐标+轴线+相机侧）
4. OPTICS AND CAMERA（FOV/距离/高度/手持/快门角度/否定约束）
5. BEATS/ACTION TIMING（逐段对话+动作+时间戳）
6. PHYSICS（物理行为描述）
7. NEGATIVE/排除（不做什么，用正面约束表达）
