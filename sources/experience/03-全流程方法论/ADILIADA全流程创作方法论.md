# ADILIADA 全流程创作方法论

> **依据**：对 Higgsfield 官方短片 ADILIADA（6:16 黑色科幻喜剧，"每死一次换一个宇宙"）全部 11279 个生成任务、10688 条提示词（1692 条唯一文本）的完整逆向。229 个文件夹全数抓完。
> 这是**第六个体系**：类型片戏仿宝库——**21 个电影致敬彩蛋的完整提示词工程**。

---

## 〇、项目画像

**故事**：Adil 意外获得超能力：每次死亡就在新宇宙以另一个自己重生——他注定跳跃于世界之间，试图阻止所有世界的终结。（评论区戏称"基于 Morgenhtern"、"Jumper 加强版"）

**结构**（229 文件夹，教科书级 shot 组织）：
- 4 个编号场景：`1. COLD OPEN "The Crow Hunt"` → `2. MAIN TITLE SEQUENCE` → `3. SPACE SCENES` → `4. MEETING THE VILIAN`
- 每场下 shot 级编号文件夹（1.1~2.14），**每 shot 内再分 Generations / Assets / Locations**——三层：场→镜→生成记录
- TITLE SEQUENCE 内嵌 **21 个电影致敬 Easter Eggs**：Casino Adil、Reservoir Adils、Plenty of Time to Die、Adil Runner、Adils War、Adilth、Adil Unchained、Adil and the Frog、Rex v Adil、La La Adil、Unbreakadil、Adiplash、Once Upon a Time in Adil、The Hateful Five、Morklight、Kill Dill、A-Men: First Class、The Lord of the Adils、Rex and Mia、The King、Adil-Noir

**模型**：seedance_2_0 ×7588 主力 + nano_banana_2 ×1469 + soul_cinematic ×810 + soul_location ×236。

**时间线**：2026-06-29 ~ 08（36 天），峰值 07-04 单日 129 条唯一。

---

### 0.5 整体画面风格（一眼认出 ADILIADA 的视觉 DNA）

**看片感受**：黑色科幻喜剧的"变奏蒙太奇"——主线是 anamorphic 宽银幕的现代伦敦冷调，但每次死亡重生就换一个类型片宇宙：太空舱的实用主义白光、黑色电影的雨夜霓虹、每个宇宙都像同一个人换了灵魂住进去。

**视觉 DNA 六要素**（词频来自 1,692 条唯一提示词）：

| 要素 | 定义 | 数据证据 | 提示词落法 |
|---|---|---|---|
| 底片 | anamorphic + 35mm + 颗粒 | anamorphic ×281、35mm ×134、grain ×988 | Cinematic anamorphic widescreen, film grain |
| 运动感 | Constant strong sense of speed 是标志句 | STYLE 原文 ×多段：the world outside streaks past in motion blur, power-line poles whip by | 速度感写死：never parked, 外景必须 streaking |
| 色彩 | 暖青底 + 每宇宙一变（红 ×1253 最高频——血色死亡主题） | red ×1253、blue ×660、green ×485、teal ×293 | 主题色"死亡红"贯穿：每次死亡都是红色意象（血浆死亡/红色枪/红酒） |
| 光线 | 按情绪写光：auditor 检查制度 | 原文：overcast blizzard = soft diffused cold light, low contrast, face READABLE on reveal. Do NOT force contre-jour silhouette (auditor: face read required) | 光线写法带"验收条件"——脸必须可读，否则算错 |
| 质感 | 43K 字符极限长文的密度 | grain ×988、haze ×347、overcast ×80 | STYLE 段结尾写"戏眼"：The man inside it is plainly bigger, calmer and colder than the people filming him, and the whole shot is the moment they find that out |
| 戏仿色 | 21 个彩蛋各有类型片调色 | Casino 厕所戏（硬光打斗）/ Reservoir 仓库（茶色） / La La（紫夜） | 每个彩蛋按被模仿片的标志性场景 3 秒定调 |

**画面气质判词**：dream register underneath — the air a fraction too still, the black carrying weight, the pace unhurried past comfort（梦境质感：空气过分静止、黑色有重量、节奏慢过舒适）——不堆滤镜词，写体感。

---


## 一、类型片戏仿的提示词工程（本片独有价值）

21 个彩蛋每个都是**一段完整的类型片语法**，同一个演员（Adil）置换进不同电影宇宙：

```text
# SEEDANCE 2.0 — RESTROOM FIGHT (single generation, 3 segments, 2 HARD CUTS)

## SCENE CONTEXT
A public restroom fight. A one-eyed super-agent and a criminal battle among
the toilet stalls. First the agent front-kicks the criminal backward through
a louvered stall door. Then, seen from directly overhead, the agent grabs
the criminal by the collar... drives him like a battering ram through four
adjacent stall partitions, one after another, moving left.
```

**方法论**：
1. **戏仿先抓"标志性场景"**（007 的厕所打斗、落水狗的仓库对峙、洛奇的台阶、La La Land 的星空舞、指环王的军团）——不是模仿整片，是模仿"每个片最被记住的那 3 秒"
2. **打斗写法继承 RED FLAG**：逐拍+向量+`drives him like a battering ram through four adjacent stall partitions, one after another, moving left`
3. **单条生成内分段**：`single generation, 3 segments, 2 HARD CUTS` —— 用段内硬切代替多条拼接

---

### 1.5 戏仿打斗的完整结构拆解（Casino Adil 9,157 字，官方原文三段教学）

**① 角色反差设计**（ACTIVE REFERENCES 段）——戏仿打斗的成败在人物反差：

    <<<image_2>>>: man in his 30s, curly black hair, mustache and short goatee,
    black leather eye patch over one eye, black turtleneck sweater, black
    leather dou... Fierce, controlled fury. 100% matches the reference.
    <<<image_3>>>: man in his 30s, tousled wavy black medium-length hair,
    mustache and small goatee, green blazer over a rust-orange shirt with a
    dark tie, sleeves rolled, green trousers. He is the one kicked, then
    hoisted by the collar and used as the battering ram. He reacts with
    shock, pain and snarling defiance, legs kicking as he is lifted.

独眼特工（007 系）vs 绿西装罪犯——**外观反差 + 反应反差**（controlled fury vs shock, pain and snarling defiance）。戏仿打斗的两人必须有"力量等级差"，这是喜剧的引擎。

**② LOCATION MAP 的"破坏面"设计**：

    ## LOCATION MAP
    Tiled public restroom in a warm neutral tone. A long row of toilet
    stalls with white louvered wooden swinging doors and white vertical
    divider posts runs along one wall... Depth cue: the closed louvered
    stall doors and thin partition panels are the main vertical planes
    the bodies smash through.

**Depth cue** 字段是本片独有发明：**明确指出这个场景里"会被打穿的面"**——隔间门板就是人体冲撞的破坏面。场景描述不只写有什么，写**什么会被破坏**。

**③ 引用图的相机继承豁免**：

    <<<image_1>>>: public restroom location reference. Controls room geometry,
    tiled wall and floor materials, warm neutral palette... Reference controls
    geometry, materials, atmosphere, and the existing practical ceiling light
    only. Its camera angle, framing and shot order are not inherited.

最后一句是关键：**参考图相机的角度、构图、镜头顺序不被继承**——只继承几何、材质、氛围、顶灯。位置资产复用时的"相机豁免"标准句。

---


## 二、结构体系：与 ONEIRIC 同源的八段式 + 43K 极限长文

段落统计（1692 条唯一）：ACTIVE REFERENCES ×595、SCENE CONTEXT ×593、PHYSICS ×592、LIGHTING ×576、AUDIO ×570、FORMAT MODE ×568、OPTICS ×533、CAMERA ×463、ACTION TIMING ×437、LOCATION MAP ×419、**POSITIVE CONSTRAINTS ×352 / POSITIVE LOCKS ×242**（两种正向锁命名并存）。

**43K 字符的极限长文**（Remembering the Trauma 镜头）示范了提示词的天花板：从 SCENE CONTEXT 一路写到 STYLE 收尾——
```text
STYLE
Documentary handheld on an Alexa Mini through vintage primes, framed
carelessly by a person stepping backwards and then standing his ground: one
hard warm source, deep low key, form readable in the shadows, real smoke
crossing the beam, human imperfection in the framing and the focus. Dream
register underneath — the air a fraction too still, the black carrying
weight, the pace unhurried past comfort, and the ending arriving as a
physical fact rather than as an effect. The man inside it is plainly bigger,
calmer and colder than the people filming him, and the whole shot is the
moment they find that out.
```
——**STYLE 段结尾直接写"这场戏的情绪意义"**（"整个镜头就是他们发现他比他们更冷更强的那一刻"）——风格段不止是光学参数，是**戏眼**。

---

## 三、六体系对照总表

| 维度 | DETOUR | ZEPHYR | RED FLAG | KOK BORU | ONEIRIC | ADILIADA |
|---|---|---|---|---|---|---|
| 定位 | 独立·街头动作 | 官方·IMAX | 官方·黑色 | 官方·手绘 | 官方·19min长片 | 官方·类型片戏仿 |
| 规模 | 5.5K | 4.8K | 3.5K | 2.7K | 41K | 11.3K |
| 核心武器 | 负面空间约束 | 风格前缀参数化 | 正向色彩+示意图 | 帧率锁+双层时间 | GLOBAL LOCK 体系 | **类型片语法置换** |
| 正向锁 | — | — | — | — | POSITIVE LOCKS | **POSITIVE CONSTRAINTS/LOCKS 双命名** |
| 组织 | 多级分类 | 扁平 | 场景夹 | 每镜一夹 | 四级树 | **场→镜→Generations 三层** |
| 提示词极值 | 20K | 22K | 10K | 25K | 37K | **43K** |
| 周期 | 22天 | 3天 | 10天 | 45天 | 36天 | 36天 |

**六体系共同铁律（最终版，全工作区验证）**：风格段成段复用；元素引用+控制边界；正向形式>负面清单；对抗模型默认行为（含"dream register"这种高级用法——写"梦境质感"而非堆滤镜词）；物理逐帧显式；音频约束进提示词；锁是问题驱动的。

---

## 四、复用检查清单（ADILIADA 增补）

- [ ] 戏仿是否抓住了"标志性场景 3 秒"而不是泛泛模仿？
- [ ] 单条生成内的多段是否用 `N segments, M HARD CUTS` 声明？
- [ ] STYLE 段结尾是否写了这场戏的"戏眼"（情绪意义）？
- [ ] 环境氛围是否用高级质感词（dream register / the air too still / black carrying weight）？
- [ ] shot 级文件夹是否分 Generations/Assets/Locations 三层？
- [ ] 彩蛋/致敬镜头是否也走完整八段式（不因短而降级）？
