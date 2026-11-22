# seedance4k-breakdown 生产管线全解（27 块 · 官方最大博客块集）

> 收割 G5（E172）｜来源：官博提示词块全集 slug=seedance4k-breakdown，27 块共 ~130K 字符
> **全库最完整的生产管线示范**：角色→道具→场地→场景→VFX→现实串联，每环节有独立提示词。

## 一、生产管线九环节

| 环节 | 块号 | 内容 |
|---|---|---|
| 1. 主角角色表 | 1 | 三板格式 + 鼻贴花装饰 |
| 2. 配角角色表（母） | 2 | 面部 DNA 继承声明 + 三视图 |
| 3. 场地空场 | 3 | 青少年起居室（lived-in vibe，非 showroom） |
| 4. 道具参考 | 4 | TV remote 三视图（front/side/back） |
| 5. 场景提示词 | 5 | 单镜头连续（回家开电视）+ @ADIL + @REMOTE |
| 6. 奇幻生物参考 | 6 | 龙-鸟混合坐骑（emerald/jade/turquoise/gold 羽毛色板） |
| 7. 精灵角色参考 | 7 | 森林精灵（花冠+有机服装） |
| 8. 骑龙飞行 | 8 | **14,841c 巨型场景**（90° 瀑布俯冲+蝴蝶群+猴群穿越） |
| 9. 客厅反应 | 9 | 回家场景变体（hyped 版） |
| 10. 航拍山景 | 10 | 雪山山脉空镜（518c 极简航拍） |
| 11. 雪豹缩放 | 11 | 广角→特写连续变焦（super-telephoto 到 snow leopard） |
| 12. 配音 | 12 | 86c 极简：wildlife documentary voiceover |
| 13. 雪怪角色表 | 13 | 三视图（PORTRAIT/FRONT/REAR） |
| 14. 雪地卡车道具表 | 14 | **2×2 四视图**（FRONT/SIDE/REAR/UNDERCARRIAGE） |
| 15. **雪地卡车追逐** | 15 | **20,515c 全库最大块**——冰怪+卡车+双主角+暴风雪追逐 |
| 16-19. 客厅变体 | 16-19 | 不同角度/情绪的看电视场景 |
| 20-23. 兽人/精灵设计 | 20-23 | Orc portrait×2 + 沼泽战士双 panel + 精灵军队 |
| 24-26. FPV 无人机战斗 | 24-26 | **规模转换**：军队战斗→钻入草丛→手掌大小对决 |
| 27. 客厅结尾 | 27 | 看电视场景（母亲走来看到电视内容） |

## 二、核心方法提取

### 1. 角色表继承链 [官方 块2]
> She must read instantly as his mother — same heritage and facial DNA, older generation

角色表之间有**遗传关系声明**——母子/姐弟的血缘相似性通过 DNA 继承声明锁定。

### 2. 幻想/现实交织结构 [官方 全部]
整个博客在**幻想场景**（骑龙/雪怪/精灵军队）和**现实场景**（看电视/回家）之间交替——幻想镜头的输出（电视上播放的内容）成为现实镜头中屏幕上的内容。这种**嵌套结构**是叙事性 AI 视频的高级技巧。

### 3. 规模转换 [官方 块24-26]
> The drone flies fast through the middle of the clash... then dives down between TALL blades of grass to ground level — where two tiny, palm-sized fighters duel one-on-one while the army battle rages above.

FPV 无人机从**军队规模**急速下潜到**手掌大小**的微距对决——单镜头内的极端尺度转换。

### 4. 四视图道具表 [官方 块14]
> FRONT VIEW (top-left), SIDE VIEW (top-right), REAR VIEW (bottom-left), BOTTOM / UNDERCARRIAGE VIEW (bottom-right)

道具参考从三板扩展到**四视图**（加底视图），用于复杂机械道具。

### 5. 非品牌护栏 [官方 块4]
> no streaming-app shortcut buttons (no Netflix, Prime Video, YouTube, Disney), no mic button

道具设计明确**排除品牌按钮**——NON-IP 护栏在道具级别的实例。

### 6. 生物物种行为匹配 [官方 块8]
> Wordless throughout, she steers with her body and pure joy — laughing and whooping

骑龙飞行的行为匹配——**用身体操控**（非缰绳）+ **纯快乐**（非恐惧）的情感立法。

### 7. 极简航拍 [官方 块10]
518 字符极简航拍——**最短的场景提示词**，证明不是所有提示词都需要长篇立法。

### 8. 配音指令 [官方 块12]
> Analyze the video and create a voiceover for it in the style of wildlife documentaries

86 字符极简配音指令——用视频做输入，模型生成配音。

## 三、块长度分布

| 长度 | 块数 | 代表 |
|---|---|---|
| <1K | 4 | 航拍/配音/战场空镜 |
| 1-3K | 8 | 角色表/道具/兽人肖像 |
| 3-6K | 6 | 场景/生物参考/FPV |
| 6-10K | 5 | 骑龙飞行/雪豹/FPV 战斗 |
| 10-20K | 3 | 雪地卡车/骑龙完整版/Blender previz |
| 20K+ | 1 | 雪地卡车追逐（20,515c） |

**20K+ 单条提示词的存在**证明：当场景复杂度足够时（多角色+多阶段+多约束），提示词长度无上限。

## 四、生产管线 → K 页生长

1. **角色表遗传继承声明** → K16 多主体调度增补
2. **四视图道具表** → K09 场景资产卡扩展
3. **规模转换**（FPV 军队→微距）→ K13 运镜动词库增补
4. **幻想/现实嵌套结构** → 视频轨叙事结构新维度
5. **20K 单条提示词** → K09 长度标准"密集场景不设上限"的实证
