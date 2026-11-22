# RED FLAG 全流程创作方法论

> **依据**：对 Higgsfield 官方短片 RED FLAG（~2 分钟香港新黑色电影，全部 AI 生成）全部 3524 个生成任务、3508 条提示词（616 条唯一文本）的完整逆向 + 官方 brief 自述的实战方法。交叉验证对账通过（3525 = 3524 job + 1 media_input）。
> 这是**第三种体系**：DETOUR（独立·35mm 街头动作）、ZEPHYR（官方·65mm IMAX 纪实）之后，RED FLAG 是**单场景强风格化黑色电影**——它的价值在于官方亲自示范"怎么打赢模型"。

---

## 〇、项目画像

**故事**：1990s 香港雨夜。独居女人还在考虑新男友值不值得留，午夜有人撬开她虎纹彩绘的门——"贼"是拿花束溜进来给惊喜的男友 Li。Li 不知道：她是深藏不露的武术冠军，而且她刚下定决心。

**工具链**（brief 原文）：Seedance 2.5 全部视频镜头 / Higgsfield Soul Cinema 角色表 / Seedream 5.0 图像编辑。实际数据中还有 soul_cinematic ×674（场景资产主力）。

**项目结构**：扁平六文件夹（root 2330 / scene1 386 / scene2 283 / scene3 252 / assets 214 / test 59）——一场戏一个文件夹。

**时间线**：2026-08-03~08-12 十天完成主体（峰值 08-05 单日 110 条唯一提示词）。

**双语策略**：616 条唯一提示词中 **295 条中文、321 条英文**，另有大量"中文操作指令 + 英文技术段"的混写体——官方实践证明 Seedance 2.5 中英皆可，混写可行。

---

### 0.5 整体画面风格（一眼认出 RED FLAG 的视觉 DNA）

**看片感受**：深绿色调的 90 年代香港新黑色电影——雨夜、钨丝灯、旧公寓的红色灯罩是全片唯一的暖光；Fuji Eterna 胶片的绿色阴影漫过每一帧，杜可风式的广角畸变贴着女主角的脸。

**视觉 DNA 六要素**（词频来自 616 条唯一提示词）：

| 要素 | 定义 | 数据证据 | 提示词落法 |
|---|---|---|---|
| 底片 | 35mm 1.85:1 + Fuji Eterna 500T 偏绿 | 35mm ×378、1.85:1 ×55、Eterna ×7（风格前缀必带） | Arriflex 35 III, Zeiss Super Speed primes, spherical 1.85:1, Fuji Eterna 500T processed cool |
| 双锚点 | 王家卫 + 杜可风 | Wong Kar-wai ×63、Christopher Doyle ×14 | STYLE 句直接署名双人 |
| 色彩 | 冷青绿铁律 + 灯泡内允许暖黄 + 红灯罩剧情色 | green ×196、yellow ×138、red ×278 | The dominant color must be cold teal-green. Yellow exists only inside the lamp bulb and a palm-sized halo beneath it. If the frame turns yellow, the frame is wrong. |
| 光线 | COLOR STAGES 剧情化光照（开灯前后两阶段） | tungsten ×78、fluorescent ×78 | Stage one 漆黑+门缝冷绿光带 → Stage two 红灯罩品红光瞬间点亮 |
| 质感 | 颗粒 + 光晕 + 单光源 | grain ×273、halation ×307（全工作区 halation 最浓） | coarse organic grain, soft halation blooming around practical lights, shallow depth of field, low-light night, crushed and moody |
| 空间 | 一间老公寓 = 整个世界 | 虎纹门/珠帘/花暖水瓶逐件列位 | LOCATION MAP 文字分镜 + 示意图锁几何 |

**画面气质判词**：crushed and moody（压碎的暗调）、lives in green（活在绿色里）——官方亲述选 Eterna 弃 Kodak 的原因就是"这片活在绿色里"。

---


## 一、资产体系：文本+图像成对（brief 自述的核心理念）

> "An asset is a pair: text + image. The text descriptor goes into every prompt word for word; the image anchors the model."

- 资产注册表约 **30 个 @tag 资产**：两个主角+祖母、虎纹门、半开牡丹花束、虎头黄铜钥匙、红色锦缎手袋、四个购物袋、走廊、楼梯间、厨房、夜景天际线 + **一整套走位示意图（staging diagrams）**
- 每个提示词用 **@tag 名**调用，绝不写 "the man"、"the door" 这种通用指代
- **剪影锁定法**：Li 的描述钉死剪影（橄榄色细条纹 90 年代西装 + 酒红衬衫 + 金链）——半部电影他背对镜头，**背影即可辨认**。这是"资产描述怎么写"的官方答案：关键不是脸，是可识别轮廓

---

## 二、风格系统：调色在提示词里，不在后期

### 2.1 风格前缀（每条提示词逐字粘贴）

```text
STYLE: Wong Kar-wai-style Hong Kong neon noir, in the Christopher Doyle
cinematographic tradition. Arriflex 35 III, Zeiss Super Speed primes,
spherical 1.85:1, Fuji Eterna 500T processed cool — coarse organic grain,
soft halation blooming around the practical light sources, shallow depth
of field. Low-light night, crushed and moody.
```

**统计证据**：Arriflex ×55、1.85:1 ×55、Wong Kar-wai ×63、Christopher Doyle ×14、Eterna ×7。
**方法论亮点**：
- **引用导演 + 摄影师双锚点**（王家卫 + 杜可风）——比 ZEPHYR 的只引用摄影师更进一步，风格氛围直接继承
- **胶卷选型做 A/B**：先测 Kodak Vision3 500T，Eterna 胜出的原因官方写明——"its shadows drift green — and this film lives in green"（Eterna 阴影偏绿，而这部片活在绿色里）。**选胶卷的标准是它对主题色彩的偏置**

### 2.2 色彩战争：负面清单无效，正向形式有效（brief 最重要的教训）

问题：Seedance 2.5 反复把冷青绿走廊翻成暖黄。
- **失败方案**：负面清单 "no yellow" —— 无效
- **成功方案**：**正向空间分配**：
```text
The dominant color must be cold teal-green. Yellow exists only inside the
lamp bulb and a palm-sized halo beneath it. If the frame turns yellow,
the frame is wrong.
```
- **参考图污染的解法**：参考图里有删不掉的发光红窗？直接写：**"That window glowing in the reference is switched off in our film."**——模型接受叙述修正
- **色彩阶段化**（COLOR STAGES）：把一场戏的光写成"阶段"——`Stage one — before the lamp is switched on: 漆黑，只有门缝漏进的冷绿光带；Stage two — after she presses the switch: 红色灯罩的品红/正红光瞬间点亮`。**光照按剧情时间轴写，不是静态描述**

---

## 三、几何控制：示意图与照片分工（官方独门）

> "A diagram decides the frame; a location decides the texture."

- **平面示意图**（正视角或俯视、字母代替人物）锁定几何和机位
- **实拍地照片**只供质感和光
- 示意图**最后附上**（attachment 顺序有意义），提示词明说：`Composition and camera = the diagram, not the location photo`
- **模型抓错参考时的终极手段：直接删掉那个参考。Fewer anchors beat better instructions.**（少而准胜过更好的指令）

---

## 四、物理锁：人怎么走、两人怎么并排、镜头怎么匹配

官方给每个"普通动作"都上了锁（这些锁全部可在提示词数据中验证）：

| 问题 | 锁（原文） |
|---|---|
| 滑步/双脚腾空/同脚迈两次 | `heel lands first, strict left-right alternation, one foot always on the ground` |
| 祖母总是漂到前面 | `shoulder to shoulder, on one depth line, both heads the same size` |
| 匹配剪辑两个镜头速度不同（快脚慢背） | `the camera speed of shot 9 equals shot 10, exactly` |
| 物件变成"命名强制对象" | 开场钥匙写成 named, mandatory object，一次只做一个动作 over two to three seconds |

**SCALE 段**（中文样例，7 条）：`SCALE — measure everything against the room, this is critical: The woman is petite, 158cm tall. The front door is 200cm tall and 85cm wide...` ——**用房间尺寸给所有物体定标**，比例错误从源头堵死。

---

## 五、打斗编排：动作协调员的记录本（brief 最精彩的章节）

> "A fight cannot be edited into smoothness."

三个独立 clip 剪在一起必然顿挫——每个 clip 重新猜姿势和节奏，每次剪切都渗进停顿。官方的解法：

1. **帧链接（frame-chaining）**：clip N 的末帧 = clip N+1 的首帧，**动作跨剪切在动作中途**（数据验证：25 条含 first/last frame 语法）
2. **关键连招单条生成**：整个三招组合写成单一时间线，实速，**指名禁用慢动作**（"video models love to slow a fight down on their own"）
3. **招式写法 = 动作协调员笔记，不是氛围词**：
   - 风格即性格：她的动作 soft, circular, chin-na redirects and push-hands（冠军的省力）；他的 straight, heavy and late
   - **每招有名有向量**：`she rolls him over herself with her foot; he lands face toward her, head toward the window` —— 没有向量，他的落地姿势每次都不同
4. **打斗分镜图**：火柴人 blocking diagrams 标注每个关键帧的手脚位置，作为首帧几何附加
5. **局部快切策略**：全身连续性太贵时，切进身体局部——手、腰、脚的快切（jump cuts hide transitions, add impact）——**脚的特写比两人全景难出错得多**
6. **一个镜头干最多活**：从她脚底开始的上摇，摇到一半她把他扫倒

数据验证：`lands ... toward` 向量语法、`MATCH CUT ON ACTION at 5.0s`（在动作中途 5.0 秒处匹配剪辑）都是真实提示词原句。

---

### 5.5 火柴人示意图的生成法（RED FLAG 独家——用 MJ 画 blocking diagram，63 条实证）

brief 说的 "stick-figure maps" 不是手画的——**是用 Midjourney 生成的**，且每张带俄语注解。官方原文（1,966 字完整范本）：

    she is in the foreground her legs are bigger than B's.
    B (ORANGE) = the MAN's legs and lower body, further back / deeper in the frame
    (smaller because farther away), on the LEFT; his knees are bent, off balance,
    being pulled toward her.
    Between them, a hint of her foot/knee reaching in toward B's lower body.
    Simple architecture: a low dark kitchen-counter/cabinet line across the far
    background, thin outline only.
    Labels: "A" (blue) foreground right, "B" (orange) background left.
    Flat 2D, minimal detail — foreground legs (A) big and near, background legs
    (B) smaller and far. --ar 16:9 --style raw --stylize 30 --v 8.1
    --no photorealism, photo texture, realistic lighting, realistic faces,
    shading, extra limbs, extra fingers
    Теги: карте — <<<image_2>>> ; референс — <<<61513ce8...>>>
    Ключ: нижний ракурс СО СТОРОНЫ ДЕВУШКИ; A(синяя)=её ноги на переднем плане,
    крупно/близко, колено начинает подниматься к B; B(оранжев)=ноги мужчины
    дальше в глубине, мельче, колени согнуты, теряет равновесие...

**逐句拆解**：
1. **角色代号系统**：A（蓝）= 女方、B（橙）= 男方——颜色 + 代号，正文和视频提示词共用这套代号
2. **透视写死**：foreground legs big and near / background legs smaller and far——示意图自带纵深逻辑
3. **建筑只留轮廓**：thin outline only——背景一条柜台的线就够
4. **MJ 参数保留**：--ar 16:9 --style raw --stylize 30 --v 8.1——示意图生成也要指定版本与去美化
5. **负面参数**：--no photorealism, photo texture, realistic faces——防 MJ 自作主张画写实
6. **俄语注解段**（Теги=标签 / Ключ=要点）：给团队的接图说明——哪张卡放哪个槽、关键构图是什么
7. **示意图最后附上** + 提示词声明 Composition and camera = the diagram

### 5.6 LENS LOCK 双镜头实战（9,775 字范本，中文项目里第一次见到精确到度的双镜设计）

    SHOT 1 LENS LOCK = 84°: classic wide anamorphic character, camera about 3
    meters from the door, hallway geography readable in the center of frame,
    straight lines rectilinear in the sharp zone, no fisheye.
    SHOT 2 LENS LOCK = 29°: short telephoto detail character, focus locked on
    the sideboard top surface, very shallow depth, the amber lamp and vanity
    mirror dissolving into oval bokeh, side edges blurred.

**两个镜头 = 两个锁定视场角**：84° 宽角交代走廊地理（直线保持直、无鱼眼），29° 长焦拍细节（台面、灯化成椭圆光斑）。**每度的画面后果都写出来**——"84°" 不是数字游戏，是"middle geography readable + rectilinear + no fisheye"的压缩表达。

**Hard camera rule 硬规则段**（同一条提示词）：
    the camera NEVER moves closer or further. No dolly-in, no zoom-in, no
    push-in, no creeping approach, no pull-back.

机位运动被五种"不许"锁死——因为这场戏要的是稳定观察感，模型最常见的失败（偷偷推镜）被提前点名。

---


## 六、双语混写体系（官方示范）

中文样例的真实结构：
```
以图1为完整的场景和构图基础：完全保留图1的门厅透视、门的位置、镜头角度、
家具陈设和灯光气氛，一点都不改动背景。图2 定义女子的面部、发型和服装，
图3 定义红色手袋，图4 定义钥匙，人物不取自图1。     ← 中文：操作指令与参考图分工

Hong Kong, mid-1990s. Interior, evening. ...       ← 英文：场景与技术描述
SCALE — measure everything against the room ...    ← 英文大写段：硬约束
```
**规律**：中文写"怎么用参考图"的操作层，英文写风格/技术层——两种语言各司其职。59 条中英混写提示词验证此模式。

---

## 七、与前两个项目的体系对比（第三种体系）

| 维度 | DETOUR | ZEPHYR | RED FLAG |
|---|---|---|---|
| 类型 | 街头动作喜剧 | 机甲纪录片 | **单场景黑色电影** |
| 画幅/胶片 | 35mm Kodak | 65mm IMAX 8K | **35mm 1.85:1 Fuji Eterna** |
| 风格锚 | 胶片型号 | 摄影师(Hoytema) | **导演+摄影师(王家卫+杜可风)** |
| 核心战场 | 一致性 | 风格前缀 | **打赢模型的每个细节**（色彩/几何/物理/打斗） |
| 提示词语言 | 英文为主 | 英文 | **中英双语混写** |
| 独门武器 | 负面空间约束 | 倒置角色表 | **示意图/帧链接/向量打斗/正向色彩分配** |
| 教训来源 | 版本迭代 | 受控实验 | **brief 亲述每场失败战役** |

**三个项目共通的铁律**（再次验证）：
1. 风格前缀成段逐字复用（三个项目一致）
2. 一致性 = 元素引用 + 命名（@tag / <<<ID>>>，绝不写通用指代）
3. 负面清单必要但不充分——**正向形式 > 负面清单**（RED FLAG 的色彩战争是决定性证据）
4. 物理必须显式锁（走路/并排/镜头速度/比例/招式向量）
5. 失败是常态，方法是如何把失败变成可控变量

---

## 八、复用检查清单（RED FLAG 增补项）

- [ ] 资产是否文本+图像成对、@tag 命名、绝不写 the man/the door？
- [ ] 关键角色是否锁定了剪影（背对镜头也能认出）？
- [ ] 胶卷选型是否按"对主题色彩的偏置"决策？
- [ ] 色彩是否写成正向空间分配（X 只存在于 Y 内）而不是 no-Z？
- [ ] 参考图删不掉的污染源是否用叙述修正（"that window is switched off in our film"）？
- [ ] 光照是否按剧情阶段写（COLOR STAGES）？
- [ ] 几何（示意图）与质感（照片）是否分离、附件顺序是否明确、写明"机位=示意图"？
- [ ] 模型抓错参考时是否敢删参考（少而准 > 好指令）？
- [ ] 动作是否上锁（脚跟落地/左右交替/一脚在地）？
- [ ] 匹配剪辑是否锁了相机速度相等？
- [ ] 比例是否有 SCALE 段（用房间定标）？
- [ ] 打斗是否：帧链接 + 单条时间线实速 + 指名禁慢动作 + 每招有向量？
- [ ] 全身失败时是否切局部快切藏转场？
