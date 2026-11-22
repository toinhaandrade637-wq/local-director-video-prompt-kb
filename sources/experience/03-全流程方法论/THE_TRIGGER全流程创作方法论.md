# THE TRIGGER 全流程创作方法论

> **依据**：对 Higgsfield 官方写实短片 THE TRIGGER（8:35，双时间线杀手剧）** 100% 全量**逆向——26 个文件夹全部抓到游标尽头，5,429 个 job、5,423 条提示词（773 条唯一）逐类精读，并配合官方 brief（全平台最详细的制作手册，约 42K 字）。
> 这是**第十个体系**：**双时间线写实剧**——官方用一部片同时示范：夜景怎么hold住黑、调度图系统、表演任务系统、资产命名工程学。

---

## 〇、项目画像

**故事**：年迈杀手在餐馆的咖啡与苹果派价目下接收指令；当新订单点名了当年在阿富汗从屋顶把他拖下来的士兵，他必须抉择自己活在两个人生中的哪一个。

**双时间线结构**（官方 brief 原文定调）：
- **现在（纽约夜）**：装修中的大楼狙击巢、距空窗一米架好的步枪、街对面三扇亮灯、餐馆账单上的合同——"几乎什么都不发生，而它发生在黑暗里"
- **过去（阿富汗日）**：屋顶阵地、走进的火线、穿过 Jack 肩膀的那颗子弹
- "两者之间是一张脸，而这部电影就是这两个世界之间的距离"

**数据验证**：纽约线 526 条唯一提示词 / 阿富汗线 213 条；结构 26 夹 = ASSETS（Characters: DAUGHTER/JACK/TEENAGER/TERRENCE + Locations 五处 + Props + Costume）+ SCENE 01-06。

**时间线**：2026-07-16 ~ 08（22 天），模型以 **seedance_2_5 为主**（×2,831）+ soul_cinematic ×1,199 + seedream_v5_pro ×1,016。

---

## 〇.5、整体画面风格（一眼认出 THE TRIGGER 的视觉 DNA）

**看片感受**：一部 90% 画面是"无细节的黑"的夜戏——表演活在一只眼睛、一圈肩光、一只按住开关的手上；2.39:1 变形宽银幕的椭圆光斑和横向涂抹；切到回忆时是 16mm 颗粒的蜜金色阿富汗白天，地平线滚动不平。

**视觉 DNA 六要素**（词频来自 773 条唯一提示词）：

| 要素 | 定义 | 数据证据 | 提示词落法 |
|---|---|---|---|
| 画幅 | 2.39:1 变形宽银幕 | 2.39:1 ×351、anamorphic ×228 | GRADE 段固定块：ANAMORPHIC 2.39:1, shallow focus, oval bokeh, horizontal smear. No starbursts, no flare streaks |
| 双时间线调色 | 纽约：teal 阴影+钠灯暖点+压碎黑；阿富汗：蜜沙金+16mm 颗粒 | teal ×211、sodium ×112、crushed ×203 / 16mm ×190（阿线专属）、35mm ×101（NY线） | GRADE 段逐字粘贴（两套 GRADE 块各绑定时间线）|
| 夜景铁律 | 黑就是黑——模型抬黑/发明暮空/提亮脸都要防 | night ×316 | **烘焙进资产 plate**：曝光跟随首帧；裁掉天空只留砖墙立面 |
| 手持语法 | 阿线暴力手持（地平线滚动/超越回纠/手工追焦），NY 线锁死或慢推 | 官方调色表原文：violently unsteady handheld, rolling horizon, pans overshoot and correct, focus hunted by hand, impacts punch the image, grit on the glass | NY 线：the camera physically travels, never zooms |
| 质感 | 胶片颗粒+光晕 | grain 全线、halation 阿线 gentle | 按时间线分配颗粒型号 |
| 声音 | 无配乐，设计音 | SOUND ×340 | 房间底噪、纸、铜、机械、城市；每次转场一个低频 thud 永不加速 |

**画面气质判词**：职业者的克制——underplay everything（脸部从眉毛往下全松弛，一切从眼睛和呼吸读出）。

---

## 一、资产命名工程学（官方 brief 最系统的章节）

**命名约定**（原文照录）：
```
@char_SN_Jack             character + project + name
@char_SN_Jackarmy         the same man, Afghanistan state
@loc_SN_nest_win          location + project + name
@loc_SN_nest_ext          the same building, exterior
@prop_SN_rifle            prop + project + name
```
**铁律**：`类型_项目缩写_名称`三段式；**一个元素一个名字**；**新状态=新资产**（Jack in diner 和 Jack on Kabul roof 是同一个人的两个不同资产，绝不覆盖）；不守约定则项目长出三个名字的同一扇窗，没人知道哪个是真的。数据实证：80 条提示词含 @SN 标签。

**角色两遍成**：Soul Cinema 出脸（永远特写生成，最大细节锁定身份——这个 close-up 是该角色所有资产的校验锚）；Soul 2 出全身带服装；Seedream 合成表——**硬条件：原始特写肖像永不再次过模型**，一切状态变化（灰尘/汗/肩伤/兜帽）用蒙版逐点融合，底片像素不变，身份才活得下来。

## 二、难题烘焙进资产（"Put the hard things in the plate"）

本片两大死敌——**变形镜头**与**黑夜**——都不在视频提示词里解决，全部前置到资产阶段：

1. **变形镜头进 plate**：视频提示词里写 anamorphic 挡不住光学漂移（逐镜跳变）→ 把镜头性格生成进 location plate（官方提供标准块：STRONG anamorphic lens character: horizontal squeeze and compression, oval elliptical bokeh... NO lens flares, NO light streaks）；**视频提示词只描述 clean glass——Naming a flare summons a flare**（提命名即召唤）。
2. **黑暗进 plate**：视频提示词写 "very dark" 模型还是给暮色 → plate 本身降 2-3 档+压碎黑+单一冷边光（**曝光跟随首帧而非形容词**）；**裁掉天空**（天空永远漂向蓝调时刻）——窗框被对面砖墙填满，画面最亮物是两扇亮窗和一盏门廊灯。

## 三、调度图系统（staging maps，Tigran Mutafyan 方法）

多角色精确站位时文字失效——用**示意图控制空间处置**。数据+brief 全流程：
1. 附目标帧，要求生成**纯示意图**（Seedream）：白底线稿、每角色一种哑色细轮廓、家具简形、淡网格、**图上无任何字母**
2. 示意图接到 Seedance 提示词，配**正向连接块**：`@A = the BLUE figure = @char_SN_Jack → prone on the table, facing frame-left`——并声明示意图**只定位置**（风格/光/脸/服装全来自角色与场景参考）
3. 三条安全细则：**字母只活在提示词文本**（渲染进图里的字母会渗进正片）；**连接块只用正向形式**（写 "no flat illustration" 仍会注入 flat 一词）；**示意图永远是相机视角正视图**，绝不用俯视平面图（视频模型思考画框，不思考蓝图）

## 四、表演任务系统（ACTING TASK，224 条实证）

**核心**：写 sad 得到漫画脸或死脸。每个角色给一个**表演任务**：他投入一个实现目标的战术，情绪从这场搏斗中**长出来**——在画面上，不在形容词里。

官方原文（JACK 肩伤场，全文照录）：
```
ACTING TASK — JACK: he is triaging, not suffering. When he looks at the
shoulder he is checking a piece of equipment. The reaction that follows is
his body overruling him for two seconds, and he lets it pass through rather
than fighting it or performing it. "Shit" is irritation at a tool that broke,
said quietly because there is nobody he wants to say it to. THEN THE RADIO
CALL IS THE OPPOSITE — this is the one moment in the film where he loses his
temper... He is not asking, he is DEMANDING, at full volume. But his body
will not cooperate: no air, hands shaking, adrenaline making him half a beat
slow, so every phrase costs him a breath and he has to stop and take it. He
forces the words out separated and complete anyway, because a man who cannot
be understood gets nothing.
```
**方法论**：
- **任务式诊断**："triaging, not suffering"——先否定情绪标签，再给职业动作（检查一件设备）
- **身体推翻意志的节拍**：身体压过他两秒，他让它穿过而不是表演它
- **台词的任务语义**："Shit" 是对坏掉的工具的恼火，轻声因为没人值得他说
- **眼睛是全部**：aliveness = 眼睛在任务上可见地工作；死鱼眼不用光修，**给眼睛一份工作**就活了
- 本片特别规则：**underplay everything**——十五年的职业者不表演自己的疲惫

## 五、七条铁律（brief 原文 + 数据实证）

1. **说有什么，不说避免什么**——写 American 出旗子，写 no flag 旗子又回来；描述"素净布料"它才消失（负面词会召唤负面物）
2. **几何绑画面不绑物体**——"枪的左侧"被读成画左；弹药带两次出现在两侧；改写"朝向镜头的近侧"才听话
3. **一拍一反应**——模型默认连环反应杀死瞬间；反应一次，然后运动
4. **尺度靠视觉线索**——俯视的车顶、台阶顶、前缩人影；写米数无效
5. **可数事件要证明**——一闪=一火箭，且可见空管；否则四管发九弹
6. **物理按节拍序列**——中弹者只有头先落地、肩不对称、膝内折、手套拖地才像死人；状态清单读起来像机器人
7. **每镜变尺寸与角度**——模型默认永远同高度四分之三侧居中

## 六、声音条件化（AUDIO LOCK）与补录

声音是**写好的条件块**：register/timbre/tempo/manner 定一次、存储、逐字粘贴——**never even a synonym changed**。官方样例：
```
JACK — voice: low dry male baritone, worn and unhurried, slight rasp at the
bottom, minimal dynamic range; speaks under the level the room needs, close
in, one short phrase at a time with real gaps between them; radio discipline
even off the radio. No theatrical colour, no rising ends. American.
```
跨周生成的同声场景：**不与模型搏斗**——画面先生成，Jack 从单一声音参考**专门补录**（画面不动，只换音轨，逐帧对齐口型）。

## 七、十体系对照总表（THE TRIGGER 定稿）

| 维度 | 前九体系 | THE TRIGGER 增量 |
|---|---|---|
| 命名 | @tag / <<<ID>>> / GLOBAL LOCK | **类型_项目_名称三段式 + 新状态=新资产** |
| 镜头性格 | 写进视频提示词/风格前缀 | **烘焙进 location plate**（视频只写 clean glass）|
| 夜景 | 风格段声明 | **曝光跟随首帧 + 裁天**（结构性方案）|
| 表演 | 情绪状态词 / FACS / 五件套 | **ACTING TASK 任务式**（情绪从任务里长出来）|
| 空间 | 示意图 / LOCATION MAP / GEOGRAPHY LOCK | **调度图三安全则**（无字母/正向连接/正视图）|
| 声音 | AUDIO 段 | **AUDIO LOCK 存储块 + 补录流程** |
| 负面 | Avoid/NEGATIVE/POSITIVE | **七铁律第一条=负面词召唤负面物**（FORBIDDEN 段 356 条实证——穷举但知道边界）|

**十体系终极铁律（THE TRIGGER 版收束）**：
1. 难事前置进资产（镜头/黑暗/印刷文字都在 plate 阶段赢，不在视频提示词里吵）
2. 一个元素一个名字；新状态是新资产
3. 你写的词就是你召唤的词——包括 "no" 里面的那个
4. 表演=任务，情绪是副产品
5. 双时间线=两套 GRADE 块+两套颗粒+两套手持语法，逐字存储逐字粘贴

---

## 八、复用检查清单（THE TRIGGER 增补）

- [ ] 命名三段式（类型_项目_名称）立了吗？新状态开新资产了吗？
- [ ] 光学性格（变形/暗部）烘焙进 plate 了吗？视频提示词只写 clean glass？
- [ ] 夜景：plate 降几档？天空裁掉了吗？最亮物是 practical 吗？
- [ ] 双时间线：两套 GRADE 块逐字存储了吗？颗粒型号分开（16mm/35mm）了吗？
- [ ] 调度图：图上无字母？连接块全正向？正视图非俯视？
- [ ] ACTING TASK：先否情绪标签了吗？给了职业动作吗？台词有任务语义吗？眼睛有工作吗？
- [ ] 声音 LOCK 块存储了吗？同声跨周场景走补录了吗？
- [ ] FORBIDDEN 段写了吗？记住负面词会召唤——必要但克制
