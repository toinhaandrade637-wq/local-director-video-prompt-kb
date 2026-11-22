# IF YOU STOP LOVING ME, I'LL DIE（内部名 Kran）全流程创作方法论

> **依据**：对 Higgsfield 官方无声动画短片 Kran（4:42，两人团队，4,202 个资产）的** 100% 全量**逆向——57 个文件夹全部抓到游标尽头，4,165 条提示词（749 条唯一）逐类精读。
> 这是**第九个体系**：**混合材质动画（mixed-media）**——与 KOK BORU 的纯手绘不同，它把两种矛盾材质放进同一帧，是官方的"生成视频弱点研究项目"。

---

## 〇、项目画像

**故事**：Tolik 只有一样天赋——死。任何拒绝（多小都行）当场杀死他，得逞瞬间复活。妻子多年复活他后拎箱出走；只剩他、没人修的滴水龙头、和敲门的邻居。**无声哑剧：4:42 无一句对白——一切靠动作、节奏与声音。**

**团队规模**：**两人**（导演/美术/资产/生成/后期一人，邻居戏提示词另一人）——全工作区最小官方团队，却是最精细的工艺研究。

**结构**（57 夹）：`Development`（前期 1,627：Animation/Characters/Locations/Props/Scenes/Stills 六类测试）→ `PT-1`（Part 1，1,842：sc0 标题 + sc1 十一镜 + sc2 五镜 + sc3）→ `PT-2`（Part 2，224：厨房戏四镜）→ `PT-3`（Part 3，335：结尾九镜）。

**时间线**：2026-07-20 ~ 08-19（31 天），尾声加速（08-19 单日 88 条）。

**模型**：seedance_2_0 ×2,582 + seedream_v5_pro ×597 + nano_banana_2 ×517 + text2image_soul_v2 ×212 + minimax_h3 ×103。

---

## 〇.5、整体画面风格（一眼认出 Kran 的视觉 DNA）

**看片感受**：一幅会动的水粉插画贴在精致的伪 3D 布景上——角色像剪贴的贴纸，颜色无论站亮处暗处都一样（颜料不参与场景光学）；背景是干净的 CG 房间，带自己的光和影子；4:3 的老画幅，一拍二的顿挫节奏，全片只有水龙头的滴答声。

**视觉 DNA 六要素**（词频来自 749 条唯一提示词）：

| 要素 | 定义 | 数据证据 | 提示词落法 |
|---|---|---|---|
| 双层材质 | 扁平 2D 水粉角色 + CG 伪 3D 背景，**同帧永不光学混合** | gouache ×590、hand-painted ×581、flat ×677、sticker ×16 | STYLE 段：two separate worlds in one frame that NEVER interact optically |
| 角色光学豁免 | 角色颜料不参与场景光——无高光无色温无阴影变暗 | 官方原文：The scene light does not exist for them: no highlights from the window, no rim light, no cast light, no color temperature shift... pixel-constant whether they stand in light or in shade | **角色颜色逐帧像素恒定**是核心锁 |
| 画幅 | 4:3（全库 562 条） | 4:3 ×562 | 老动画比例写死 |
| 节奏 | ON TWOS 一拍二（355 条声明）——但 brief 说是**后期做**、不要求模型 | on twos ×355 | 模型出 24fps 平滑，后期抽帧；提示词只写动作 swap 感 |
| 动作语言 | 角色动作 = 剪纸替换 | 官方原文：Every action of a character is a SWAP of one flat drawing for another — never a rotation of a form in space, never a turning volume | **swap 不 rotate**——防模型把平面角色转成 3D 体积 |
| 声音 | 无对白，水龙头是"第二主角" | silent ×49、tap ×390、rhythm ×84 | 龙头写法拟人化（见 §三） |

**画面气质判词**：死面喜剧（deadpan）+ 物件的固执存在——一只黄铜双十字把手的龙头立在画面中央，滴答声贯穿全片。**道具即叙事**：妻子走后没人修的龙头 = 没人管的生活。

---

## 一、双层材质的核心写法（14,404 字范本，官方原文全文）

    STYLE — READ FIRST
    Mixed-media animation exactly in the manner of flat hand-painted 2D
    characters composited over a stylized 3D-rendered set: flat 2D cartoon
    characters composited over a 3D-rendered background — two separate
    worlds in one frame that NEVER interact optically. The characters are
    stickers laid on top of the picture: constant flat gouache fill and
    dry-brush paper texture, identical in every frame, with their own
    painted shadows baked into the artwork. The scene light does not exist
    for them: no highlights from the window, no rim light, no cast light,
    no color temperature shift, no darkening in shadow areas — their colors
    and texture stay pixel-constant whether they stand in light or in shade.
    Every action of a character is a SWAP of one flat drawing for another
    flat drawing — a new pose is a new cutout shape, never a rotation of a
    form in space, never a turning volume. Zero 3D on characters, zero CGI
    shading, no roundness, not photorealistic. The background alone is a
    clea[n 3D set...]

**逐句拆解——混合材质提示词的七条铁律**：
1. **STYLE — READ FIRST**：风格段最顶加阅读优先级声明
2. **两种世界声明**：two separate worlds in one frame that NEVER interact optically——一句话立宪
3. **角色=贴纸**：stickers laid on top of the picture + painted shadows **baked into** the artwork（影子画进颜料里，不是场景投的）
4. **光学豁免清单**：no highlights / no rim light / no cast light / no color temperature shift / no darkening in shadow areas——**穷举一切光学会发生的错误**
5. **像素恒定**：colors and texture stay pixel-constant whether they stand in light or in shade——最强锁：同一角色在窗光下与暗处颜色完全一样
6. **SWAP 不 ROTATE**：every action is a SWAP of one flat drawing for another——never a rotation, never a turning volume——**动作语言与 3D 完全绝缘**
7. **背景才是 3D**：The background alone is a clean 3D set——只有背景吃场景光

**方法论**：这不是"手绘风格"提示词——是**材质宪法**。任何混合材质项目（2D 角色过 3D 场景 / 剪纸定格 / 黏土过实景）都该从这七条派生自己的宪法。

---

## 二、叙事段落结构：动作专用段落

26,552 字最长镜头的段落标签（官方全大写专用段）：`REFERENCE CONTROL / THE ACTION / HIS EYES — HOW BIG THEY ARE / HOW HE GOES DOWN / THE DRIPPING TAP / TIMING / LAYER ORDER / RIGIDITY AND CONSISTENCY / STILL ENVIRONMENT / MOTION LANGUAGE / VISUAL STYLE / REFERENCES`

**要点**：
- **HIS EYES — HOW BIG THEY ARE**——表情段直白命名（眼睛多大=死亡时刻的表情语言）
- **HOW HE GOES DOWN**——死亡姿态单独成段（本片的核心动作）
- **LAYER ORDER**——图层顺序段（材质分层的实施层）
- **RIGIDITY AND CONSISTENCY / STILL ENVIRONMENT**——刚性与环境静止段（背景 CG 的绝对稳定）
- **MOTION LANGUAGE**——运动语言独立成段（swap 语法的细则）

**方法论**：无声喜剧的段落命名**直接以表演内容命名**，不用抽象泛称——因为整部片没有台词救场，每个表情细节都是叙事。

---

## 三、道具即主角：水龙头的写法（390 条）

龙头不是布景——是"第二主角"。写法特征：
- **位置语言**：the brass tap standing up in the middle of the picture seen from behind with its two cross handles out to either side——从背后看、双十字把手分展两侧（**像一个小人张开双臂**）
- **声场**：滴答声是全片节拍器（rhythm ×84）——TIMING 段常以滴答对齐
- **拟态**：龙头在构图中被安排在"人物位置"（画面中央），与角色共享空间语法

**方法论**：当你有一个"贯穿性道具"（本片龙头、DETOUR 的花束、RED FLAG 的红灯罩），给它**人物级的镜头待遇**：独立构图位、节拍器功能、状态变化（没人修→主角修→修好=挽留失败）。

---

## 四、后期定格（ON TWOS）与模型分工

brief 原文：**"The animation runs on twos: each phase is held for two frames, so movement reads as a change of drawings rather than a smooth glide. This is done in post, not requested from the model."**

**方法论**：与 KOK BORU 相反——KOK BORU 要求模型直接输出 12fps 一拍二；Kran 让模型输出平滑 24fps、**后期抽帧**实现一拍二。为什么？因为 Kran 的角色是"贴纸 swap"，模型先出平滑运动，后期抽帧后每两帧的差异正好呈现"换了一张画"的感觉。**技术路线选择取决于动作语言**：KOK BORU 的动作是"重绘"（模型直接做），Kran 的动作是"替换"（后期做更可控）。

---

## 五、九体系对照总表（Kran 定稿后）

| 维度 | KOK BORU | Kran |
|---|---|---|
| 手绘路线 | 纯手绘油画（全帧手绘） | **混合材质**（2D 角色过 CG 背景） |
| 一拍二实现 | 模型直接输出 12fps | **模型 24fps + 后期抽帧** |
| 双层时间 | 大气 smooth / 人物 twos | **材质双层**（角色光学豁免） |
| 团队 | 4 人 | **2 人** |
| 对白 | 少量 | **零**（纯哑剧） |

**九体系终极铁律（Kran 增补）**：
8. **混合材质需要材质宪法**（两种世界声明 + 光学豁免清单 + 像素恒定 + swap 不 rotate + 图层顺序）
9. **技术路线按动作语言选**：重绘型给模型做帧率，替换型给后期做抽帧
10. **贯穿性道具给人物级待遇**（构图位 + 节拍器 + 状态弧光）
11. **无声叙事的段落直接以表演内容命名**（HIS EYES — HOW BIG THEY ARE）

---

## 六、复用检查清单（Kran 增补——混合材质专用）

- [ ] 两种材质的"两个世界"声明写了吗（NEVER interact optically）？
- [ ] 角色光学豁免清单齐了吗（no highlights / rim / cast / 色温 / 阴影变暗）？
- [ ] 角色颜色像素恒定声明了吗（pixel-constant in light or shade）？
- [ ] SWAP 不 ROTATE 了吗（never a turning volume）？
- [ ] 图层顺序（LAYER ORDER）写了吗？
- [ ] 背景的 3D 光照归属写了吗（background alone）？
- [ ] 贯穿性道具有人物级待遇吗？
- [ ] 帧率技术路线按动作语言选了吗（重绘 vs 替换）？
- [ ] 无声段落是否以表演内容直白命名？
