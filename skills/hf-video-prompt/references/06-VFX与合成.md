> **状态**：trial｜**证据分层**：[官方]=官方技能原文 · [案例]=项目实证 · [实测]=全量统计｜**更新**：2026-11-06｜**复审到期**：2027-05-04｜**依据**：seedance-footage-vfx 官方 SKILL.md 原文 17.9K/307 行全读（S14）+ DST 235 条全读逐字（S41，E236-E307） + SBS 285 条全读逐字（S42，E309-E327） + 7L 314 条全读逐字（S43，E329-E358）

# 视频/06 VFX 实拍合成（视频轨）

V2V 的核心难题：**锁定**所有让源片可识别的元素（人物身份/面部/服装/表演/构图/镜头/运动），**只改变**用户指定的那一个元素。锁不够紧→Seedance 重掷面部或相机→编辑不再匹配原始。所以每条提示词同时显式写两半，并在动作结尾复述最脆弱的护栏——通常 **face and identity unchanged**。

## 一、@source 声明 [官方 S14]

```
@source: Original <clip name> — <who/what: subject, wardrobe, setting, action>. Preserve
<identity, face, wardrobe, performance, framing, camera and motion> exactly; <what to change>.
```

需要真实纹理时加第二输入：
```
@creature: Reference photo of a real <animal> — <fur/face/anatomy>. Appearance and
fur/skin texture reference only; ignore the photo's background and lighting.
```

**先检查再写 @source**：读源片时长/fps/宽比/抽帧——从实际画面构建 @source（主体/服装/构图/运动/时间/主光方向），不从用户一句话总结。duration 默认匹配源片实际运行时。

## 二、Specs 行 [官方 S14]

```
Photoreal. <aspect>. <duration = 源片时长>s. <look/grade>. NON-IP — generic <creature/design>. <SFX only | SFX and source dialogue only>.
```

- **时长匹配源片**（除非扩展有理由，如慢速生物转向需 2-3s）
- **NON-IP 护栏**：添加生物/装甲/载具时必写——generic 而非品牌角色
- **音频**：SFX only 或 SFX and source dialogue only

## 三、两种变换模式

### A. 添加元素 [官方 S14]
在已保底片上叠加效果。描述效果的**物理行为随时间变化**：
- 起始点/扩散方式/运动/投射光
- 效果**与底片互动**：火光闪烁在面部+溅射到车漆/玻璃透明手臂折射背景/巨兽在攀附结构上投射真实软边接触阴影
- **比例必须显式**给巨型生物：`enormous, its massive body dwarfing the structure`
- 主体通常 **oblivious / unfazed**，继续中投递——反差即笑点，写明

### B. 替换主体周围环境 [官方 S14]
保持人物/载具/安全带/相机装置和运动，替换全世界。
- 新世界必须**以视差流过**，与原始运动一致
- **暖色定向日光世界比夜晚/霓虹更安全**——后者迫使全帧重新打光，面部漂移风险升高

## 四、光线整合（成败关键）[官方 S14]

先做分叉决策：
- **保留主体光线，只调新元素**——最低身份风险
- **重新打光整帧**——统一电影/商业调。面部风险高，显式锁身份/表情/服装

**仅色彩匹配不够**——最常见的"looks pasted in"失败。超出色彩：
- **光线**：同一主光方向（点名 screen-left/right）、同一柔和度、同一阴影密度和方向
- **环境反弹**：让世界溢到主体——上方冷天光/地面暖反弹/形体交汇处的微 AO
- **光学与大气**：匹配镜头特征与微对比；主体上叠一层场景大气雾（免得过 crisp）；匹配景深/焦点衰减/胶片颗粒
- **边缘与落地**：移除硬扣图边缘/halo/不匹配 rim；用可信深度让主体落地

## 五、真实生物整合 [官方 S14]

- 显式要求 `fully photoreal, real fur with depth and individual strands, true anatomy, never CG, plastic or cartoonish`
- 绑入底片：同一太阳方向/色温/真实软边接触阴影/同层大气雾与深度
- 仍读 CG → 可靠修复 = **第二输入**：真实动物参考照片作为 texture-only reference
- **行为匹配物种**：sloth 慢重移位 / chimp 警觉抽动 / snake 盘绕收紧不眨眼（爬行类用 unblinking stare）

## 六、对白同步相机运动 [官方 S14]

锚定双重保险（语义+数字）：
- **语义**：`On the line "<exact words>," the camera snaps into a hard crash zoom...`（需 SFX and source dialogue only）
- **数字**：`At about <T> seconds...`（T 从源片音频测量，见 references/dialogue-timing.md）

| 类型 | 定义 | 措辞 |
|---|---|---|
| Crash zoom | 快速硬推入 | snaps into a hard crash zoom |
| Smooth push-in | 慢稳滑入 | begins a smooth, steady push-in |
| Snap zoom-out | 快速拉出 | snaps a hard, fast zoom-out |
| Smooth pull-back | 慢稳解压 | slow steady decompression |

**100% 匹配源构图**：着陆时点名匹配属性——同角度/headroom/horizon/镜头特征——否则模型着陆在近失构图上无法与原始剪辑。

## 常见错误

1. @source 不够具体——没从实际画面构建，从用户一句话猜
2. 忘了 NON-IP 护栏——品牌角色/IP 物进入生成
3. 锁面不紧——面部/身份被重掷
4. 添加效果没有物理行为时间线——只有存在性描述
5. 效果不与底片互动——无光线/阴影/反射影响
6. 巨型生物比例不明——模型渲染成等身大小
7. 只做色彩匹配——没有环境反弹/大气/边缘落地
8. 忘了 SFX and source dialogue only——原声对白丢失

## 待验证

- footage-vfx 在 seedance_2_0 vs seedance_2_5 的执行保真度
- REFERENCES/dialogue-timing.md 的时间码测量方法实践
- 添加/替换两模式在不同底片类型（人脸特写 vs 全景航拍）上的效果差异

### 官方错误学补充 [官方 S21]

- 质量填充词 → 替换为 @source 具体描述（从实际画面构建，不从用户一句话猜）
- 情绪标签 → 替换为光线整合配方（same key direction + environmental bounce + optics match + edges grounding）


## 2026-11-04 ai-vs-vfx 官方方法论增补 [官方 S21 ai-vs-vfx 16 块]

- **VFX 单镜头铁律** [案例 16 块全用 ONE UNBROKEN CONTINUOUS SHOT]：任何剪辑点破坏合成视觉
- **动作链编排** [案例 块14 19,430c]：摇头→溅水→擦脸→微笑→拍脖子→加速→离画，每个动作有物理后果和情感递进
- **生物比例类比** [案例 块15]：wingspan of fourteen men laid head to toe, heavy as five elephants——人体类比优于公制单位
- **情感弧线内嵌 VFX** [案例 块12]：恐惧→犹豫→自我鼓励→爆发——VFX 镜头也有戏剧内核
- **四感传达** [案例 块12]：roar（听觉）+ spray（触觉）+ mist+light（视觉）+ wet gleam（地面）——瀑布不在画面但四感在场

## 待验证（生长点）

- 双视频分工（camera vs look）在平台参考槽位下的执行度
- 遮挡即全部交互的瞬时复原是否产生残影
- 连续性定位板（STAGING AND POSITION ONLY）是否被当作渲染风格源

## 短摘录·好在哪·迁移法（2026-11-05 范本对齐）

### 遮挡即全部交互 [案例 DST #85 逐字]

> HIS SOLID PHOTOREAL BODY SIMPLY OCCLUDES THE FLAT DRAWING — the drawing is interrupted where he is, exactly as if a person had stepped in front of a projected image — and THE INSTANT HE IS PAST, THE DRAWING IS WHOLE AGAIN AND COMPLETELY UNCHANGED.

**好在哪**：实人穿画只允许一种交互=遮挡（LIKE WALKING THROUGH FOG）；瞬时复原；显式禁止粒子化/消散/重组/涟漪（NOT dispersed into particles…NOT fade or dissolve）——把"合成交互"收敛到唯一合法形态。
**迁移**：任何实拍×2D 合成的接触规则从"遮挡"出发；受力类位移另立推画法（#87 smear+NO RECOIL）与气流法（#95 slipstream）。

### 双参考分工法 [案例 DST #122/#123 逐字]

> video_1 SUPPLIES THE CAMERA, THE FRAMING, THE MOVE, THE TIMING, THE CUT POINTS AND THE BLOCKING, AND NONE OF ITS APPEARANCE. video_2 SUPPLIES THE LOOK, THE PLACE, THE MATERIALS, THE LIGHT…AND NONE OF ITS CAMERA…If the two videos ever disagree, the camera comes from video_1 and the picture comes from video_2.

**好在哪**：双视频各授半权（camera vs look），并给出冲突仲裁句；配套代理色翻译表（green plane→地面/red cylinder→父/blue→子/yellow→画中人/purple slab→楼，逐件 NEVER）+"proxy colours are deleted"。
**迁移**：camera ref 与 look ref 同给时必须写分工+仲裁；previz 逐元色翻译并声明全删。

## DST 收官蒸馏（2026-11-06 · E260-E307 · S41 全读补全）

### 双渲染模式隔离制（QUARANTINE 总纲）[案例 DST #160/#163/#172/#181 等逐字，全项目最高频块]
> TWO RENDERING MODES IN ONE FRAME — the two human beings are PHOTOREAL and the figure in red is FLAT 2D CEL ANIMATION, and neither ever contaminates the other…THE QUARANTINE: …He is a drawing laid on top of a photograph — he never composites into the light, never picks up the world's colour, never gains realism and never degrades.
**好在哪**：隔离制的总纲句式——先"两种渲染模式同帧"定性，再 QUARANTINE 四不（不入光/不拾色/不变真/不劣化）；每条提示词全文复写。
**迁移**：任何混合渲染项目第一块写"两种模式定性+四不隔离"；隔离方向双向声明（2D 不吃实拍光，实拍也不被 2D 污染）。

### 零重量法 [案例 DST #166/#192 逐字]
> AND HE WEIGHS NOTHING…THE BUILDING DOES NOT MOVE. Nothing shifts, nothing tips, nothing creaks, no grit is dislodged off the concrete ribs, no dust puffs up, no debris falls down any of the square window holes…and the long span does not deflect by a millimetre under any landing…He crosses effortlessly BECAUSE HE WEIGHS NOTHING, and a real body attempting the same crossing would fall and die.
**好在哪**：零重量=负面清单+量化句（not deflect by a millimetre）+因果句（BECAUSE HE WEIGHS NOTHING）+反事实对照（a real body would fall and die）四件。
**迁移**：虚体物理写"结构零回应清单+毫米级量化+反事实警告"三件；与"为何能穿越"互为因果句。

### 黄昏不达法 [案例 DST #181 逐字]
> THE DUSK DOES NOT REACH HIM: he is not backlit, not rim-lit, not silhouetted, not darkened and not warmed by the orange glow behind him…the alley's light does not touch him at all…In a frame where everything else is nearly black, he stays exactly as bright, as clean and as fully saturated as a cel painted on a light table — and that mismatch is the point of the shot.
**好在哪**：环境光专项豁免——五连 not（backlit/rim-lit/silhouetted/darkened/warmed）+"亮桌 cel"比喻+"mismatch is the point"把违和声明为意图。
**迁移**：合成元素写"不接环境光"五连禁+一句比喻定义其亮度态+mismatch is the point 收口。

### 无卡通版声明 [案例 DST #162/#164 逐字]
> THEY ARE PHOTOREAL AND THERE IS NO CARTOON IN THIS CLIP…NO drawn figure, NO cel-animated character, NO flat 2D element, NO cartoon, NO figure in red or silver, and NO third character of any kind anywhere in this sequence at any point.
**好在哪**：双渲染场景的"减员变体"——同一场景模板可派生纯实拍版，禁项清单反向复用（把角色的特征色当禁项：figure in red or silver）。
**迁移**：变体族里做"去掉画中人"版时，其视觉特征（红+银）直接转 NEGATIVE。

### 预演仅动作数据法 [案例 DST #168 逐字]
> THE PREVIS IS MOTION DATA ONLY…Its colour-coded proxy geometry must NEVER render. The RED blocky figure is the boy and renders as the boy. The BLUE blocky figure is the man…NOTHING in the finished footage is flat red, flat blue, flat pink, flat tan…no proxy colours, no primitive shapes, no clay render, no blockout geometry, no viewport look, no ambient-occlusion pass, and NONE of the previs lighting.
**好在哪**：previs 三分法——数据（收）/代理色（逐件翻译成真主体）/光线（全弃）；proxy→real 逐件映射表+成品八连禁。
**迁移**：给 previs 时写"motion data only+色译表+proxy lighting 全弃"；成品负面清单含 viewport/clay/blockout 家族。

### CRT 写实规格与收缩关机法 [案例 DST #172/#201 逐字]
> this is photographic macro cinematography of curved glass — real horizontal scanlines, real phosphor bloom, slight barrel curvature at the corners, a faint rolling refresh bar, mild chroma bleed on saturated reds, real dust and fine scratches on the glass ／ the picture snaps inward to a single bright horizontal white line across the middle of the tube, the line shrinks to a small white dot at the centre, and the dot fades away through green into black over about half a second, the phosphor afterglow decaying slowly.
**好在哪**：屏幕内容=对玻璃的微距摄影（七件物理细节）；关机=线→点→绿→黑的四段衰减+余辉——CRT 死亡有标准解剖学。
**迁移**：拍老屏幕写"曲玻璃微距+扫描线/磷光/滚动刷新条三件套"；关机戏按四段衰减写。

### 吞日制度（三律合体）[案例 DST #169/#171/#220 逐字]
> THE DISC NEVER SHRINKS — IT PASSES BEHIND THE BAR…What changes is only HOW MUCH OF IT IS COVERED…The part still visible keeps its FULL brightness and its FULL colour right up to the last instant ／ THE LIGHT DIES IN STEPS, NOT ON A DIMMER…One dot outlives the others and holds alone for a beat ／ THE HEAT SHIMMER BELONGS TO THE SUN AND NOWHERE ELSE…when the light goes the air goes instantly and completely still.
**好在哪**：天体遮挡三律——直径恒定只变遮量（亮度不减至最后一瞬）/灭光走阶梯不走推子（珠逐一熄灭+末珠独活一拍）/热浪绑定光源（光死则气滞）。BAILY'S BEADS 天文术语直接入文（#220）。
**迁移**：任何"光源被遮挡"事件按三律写：遮量变化+阶梯熄灭+热浪同源绑定。

### 日食永久设定 [案例 DST #193 逐字]
> this world sits under a permanent solar occultation, but THE SKY, THE SUN AND THE ORBITAL BELT ARE OUT OF FRAME. Do not draw them. Only their light reaches this shot: endless totality, dim, cold and directionless, roughly a hundred times weaker than daylight.
**好在哪**：世界观前提一句话入板——permanence 命名+因（Belt）永不入画+果（hundred times weaker）量化。
**迁移**：背景设定写"因不出画/果可量化"双句；板内只画结果。

### 向上面最暗法 [案例 DST #167/#186/#223-#225 逐字]
> Upward-facing surfaces read darkest — the road, the tower's flank, rubble tops sinking toward black — while vertical faces, the chasm walls and the far city catch a faint warm bronze wash.
**好在哪**：360° 地平环光的倒置照度规则——朝天面吸收环光成最暗，立面接环光得暖洗；与"no cast shadows"配套（环光不能投影）。
**迁移**：全向环光场景写"向上面最暗/立面暖洗/零投影"三联；这是该光照体制的签名性判据。

### 束光世界法 [案例 DST #184 逐字]
> WHAT THE BEAM TOUCHES IS SHARPLY LIT AND THROWS LONG HARD-EDGED CAST SHADOWS…this is the ONE place in this world where directional light and real cast shadows are correct…WHAT THE BEAM DOES NOT TOUCH IS ALMOST BLACK…The beam's edge is where the world stops.
**好在哪**：单束光世界的边界声明——束内=唯一允许硬影的地方（世界级豁免），束外=黑；"beam's edge is where the world stops" 一句定世界形状。
**迁移**：独源光场景声明"此处=全世界唯一可硬影处"+束外即黑。

### 地灯轮辐影法 [案例 DST #182 逐字]
> BECAUSE IT IS A LANTERN AND NOT A TORCH, ITS LIGHT IS OMNIDIRECTIONAL AND THERE IS NO BEAM AND NO CONE ANYWHERE IN THIS CLIP…SHADOWS RADIATE OUTWARD AND UPWARD FROM IT LIKE SPOKES, thrown long and hard and enormous up both alley walls…everything near it is lit FROM BELOW.
**好在哪**：光源几何决定全部光形——灯笼=全向无束（对比火把=锥形），影子从地心向外向上呈轮辐；"the whole alley is organised around how far you are standing from it"。
**迁移**：地面全向源写"no beam no cone+spoke shadows+下照脸"；距离即照明设计。

### 眼神光物理法 [案例 DST #182/#184 逐字]
> the pair of glowing eyes is ordinary animal eyeshine, the lantern's light retroreflecting off a living retina…NOTHING supernatural. They are TWO SMALL FLAT DISCS OF PALE GREEN-GOLD…They do NOT emit light…they GROW STEADILY BRIGHTER AND FURTHER APART as it comes, and they blink out…each time it blinks or turns its head.
**好在哪**：兽眼反光=物理（retroreflect）非魔法——平板圆盘/不发光/随接近变亮变分/眨眼即灭四条物理性；红眼白眼魔眼全禁。
**迁移**：暗处兽眼写"retroreflection+flat discs+不发光+接近变亮+眨眼熄灭"，禁一切超自然眼。

### 冷顶光法与余光细条法 [案例 DST #179/#206 逐字]
> It puts a dim cold sheen on upward-facing surfaces only — the crown of a head, the tops of shoulders…the bridge of the nose…and everything beneath any overhang, brow, jaw, lintel or ledge falls into pure black ／ a THIN HORIZONTAL SLIVER of deep burnt orange…It is small, it is low, and it is nearly gone…Faces are not lit. Bodies are not modelled. They are silhouettes with one hot edge.
**好在哪**：夜巷两态——顶光态（只有朝天面得光，眉颌下全黑，眼靠地面反弹保活）与残照态（远端一细条橙光，人=单热边剪影）；光照阶梯第五态。
**迁移**：夜景写顶光清单（crown/shoulders/nose bridge）+悬垂下全黑；将熄场景用 sliver+single hot edge。

### 远端逆光法 [案例 DST #178 逐字]
> far down the canyon…The strip of sky directly overhead…is dark, drained and almost black…A THIN HORIZONTAL SLIVER…works as a distant, weak, soft backlight coming back down the length of the alley toward the lens…NO LIGHT SPILLS OUT OF THE DOORWAY — the interior beyond it is pitch black and stays black.
**好在哪**：单源在画外远端、逆镜头行进——rim 在远缘、面镜侧冷青、地面反弹保脸；门内恒黑三连声明。
**迁移**：逆光巷戏写"source off-frame far end+toward the lens+overhead drained+doorway stays black"。

### 工程遗弃法 [案例 DST #234 逐字]
> micrometeorite impact pits starring the glass, a few cells crazed and dead, faint spiderweb cracks…UV-yellowed white paint, foil torn and lifting at one corner, faded stencilled numbering and warning marks worn illegible. Immaculate engineering left running alone for a very long time…one tile of the machine that took the sun.
**好在哪**：废弃精密物=损伤清单（七项）+一句人格化总结（Immaculate engineering left running alone）+机器命名（the machine that took the sun）。
**迁移**：废弃机械写"磨损七项+精密工艺与孤独运行的对句"；给机器一个"做了什么"的名字。

来源见[来源登记](../../../sources/higgsfield-knowledge-base/维护/来源登记.md)。沉淀样式对齐 imagegen/seedance25 两范本：短摘录逐字→好在哪→迁移法；整节编年版史保留于本页下方各增补节。

## SBS 收官蒸馏（2026-11-06 · E309-E327 · S42 全读）
### 双物理法则五条 [案例 SBS #163/#171 PHYSICS 块全版]
> A. 環境物件→完全遵守真實物理慣性：絨布碎絮輕盈飄浮、石材沉重初速快受重力下墜、木屑噴濺不規則彈跳、金屬銳利直線飛行反光閃爍……碎片彼此之間有真實的碰撞、遮擋與陰影投射關係，不可穿透彼此。B. 幸子、樂手、指揮的身體→完全不受物理影響……碎片飛過他們身側時自然繞開，彷彿他們才是「靜止不變的常數」。C. 所有rim light必須源自畫面中實際存在的舞台光源方向。D. 每一次「炸裂噴飛」必須先以正常速度呈現衝擊瞬間，緊接著（通常在爆發後0.1-0.3秒內）畫面速度才切換為超慢動作……切勿讓整個炸裂過程從頭到尾都以慢動作呈現。E. 幸子的雙軌速度層：表情與肢體全程正常速度——她是這個崩解世界中唯一「未被拖慢」的存在。
**好在哪**：五条分立成文：材质分轨迹四类+碰撞不可穿透／人物免疫（绕开、不扰衣物髮丝）／rim light 光源归属法／冲击-慢动两段式带时间窗（0.1-0.3s）+全慢动作反例警告／主角速度断层=唯一清醒者语义化。
**迁移**：奇幻物理场景写「A 环境分材质轨迹+B 人物免疫+C 光源逻辑+D 两段式速度+E 主角速度层」五条制度；D 条的时间窗与反例警告是防软掉的钥匙。

### 乐手无视条款 [案例 SBS #160]
> 所有樂手不對鏡頭的穿越產生任何反應，如同鏡頭不存在於此空間中。
**好在哪**：穿越镜头的零反应合同——世界对摄影机不可见，梦幻感的技术底线。
**迁移**：FPV/无人机穿越人群写「所有人不对镜头产生反应如同镜头不存在」；配合前景虚化剪影（不可辨識面容）。

### 建筑保全条款 [案例 SBS #237/#285]
> All elements including the specific objects on the shelves, the scroll design, and the rock garden layout, must be preserved.
**好在哪**：场景重建令的元素清单保全——细化到架上具体物件、挂轴纹样、枯山水布局三级。
**迁移**：依参考图重建场景时把「必须保留」的元素写成三级清单（家具级/纹样级/布局级）。

### 水印移除令 [案例 SBS #281]
> All original text and watermarks are removed.
**好在哪**：后期清洁指令显式化——生成令尾部一句，防参考图文字透传。
**迁移**：基于带水印参考图重建时，尾部加 text/watermark removal 一句。

### 权重语法渗透 [案例 SBS #281]
> (Hyper-realistic architectural illustration of a traditional Japanese mansion, washitsu, miniatrue style, intricate detail:1.3)
**好在哪**：Midjourney 式权重语法（:1.3）混入自然语言 prompt——跨工具语法的渗透实录。
**迁移**：见到 :权重 记得是 MJ 语系残留；迁移到非 MJ 模型时改写成文字（如 extremely intricate detail）。

## 7L 收官蒸馏（2026-11-06 · E329-E358 · S43 全读）
### 冻结编排参数族 [案例 7L #9/#14/#46/#40]
> #9：the ring at the tail, the full length of chain, the stake itself — all three turning white and crystalline at the same time ／ #14：the ice begins at two points at once and spreads from both ／ #46：the stake and the rest of the chain...stay exactly as they are, untouched by this
**好在哪**：同一「拉断锁链」节拍五版冻结编排——全三件套同步冰化/先断后双起点冰化/桩不入冰——变体即调参（范围/起点/时序三参数）。
**迁移**：特效节拍做参数族：范围（哪些物件）、起点（几处同步）、时序（先断后冻 or 同步）；每版一条 prompt 实测择优。

### 一体物锁定板 [案例 7L #84/#89]
> <<<da4c4abc>>> locks the tail's ring, chain and ground stake as one single connected object — whenever this whole object is affected, all three parts are treated and rendered as that one unified piece.
**好在哪**：三件散件合成一个资产板——「一体物」声明防模型把它们当独立元素分别变形；联动冻结/断裂时全件同步。
**迁移**：物理联动组件（锁+链+桩）合制一块一体板；prompt 写 whenever this whole object is affected, all parts as one unified piece。

### 缝隙发光法 [案例 7L #115]
> Warm golden light ignites and travels along the thin mortar joints between the stone blocks...tracing the wall's block pattern as fine glowing seams rather than a flat wash of light — the stone blocks themselves stay their natural cold grey, only the joint lines between them burn bright gold.
**好在哪**：能量光写「走缝不走面」——灰缝金线（fine glowing seams）+砖石保冷灰；泛光（flat wash）被点名禁止。
**迁移**：魔法点亮建筑写「only the joints/seams burn bright, surfaces stay cold」；再配门亮线灭条款（door opens → joint-lines extinguish completely leaving only the doorway lit）。

### 断环像素级归位 [案例 7L #300/#301]
> The single broken ring...must be pixel-accurate to the neck ring shown in <<<...>>> — same diameter, same link thickness, same weld point, same forged-iron finish — simply relocated to the ground and shown split open ／ Using <<<499ec7b8>>> as the literal ring object — take this exact ring, unchanged in shape, size, and material.
**好在哪**：断件追责到像素——四同（直径/链环厚/焊点/铁艺）+重定位+开裂数；#301 再进一步给断环独立实物板（literal ring object）。
**迁移**：碎裂物要求「与原物四同」；最稳做法是给碎片单独建板并在 prompt 写 take this exact object, split at one point, not closed。

### 冰样式板 [案例 7L #305]
> Using <<<cd66dd8f>>> as the exact visual reference for the ice's shape and texture — the same jagged, upward-spiking ice crystal formation...matching that reference's ice style precisely. Nothing else in the frame is touched by ice...the metal stake...stays completely untouched by ice.
**好在哪**：冰冻效果自带样式板——形状/纹理/冰晶方向全归参考板；配冰界声明（Nothing else touched by ice）+桩不冻条款（no frost on the stake itself）。
**迁移**：材质特效（冰/火/苔）建独立样式板；prompt 写 matching that reference style precisely+冰界清单（哪些许可冻、哪些禁冻）。

### 空间登记制与两版互斥 [案例 7L #128 vs #177]
> #128：c97156a8...is a distinct, separate symbolic space...the two never appear together ／ #177：4ca94198 and c97156a8 are two camera angles of the SAME real stone corridor — c97156a8 is the reverse angle of that same corridor, in which the tally-mark wall is behind camera and therefore no tally marks appear anywhere in shot.
**好在哪**：同一对板的关系两版并存且互斥——「两个空间永不同框」vs「同一走廊的正反角」；各 prompt 内部自洽、跨 prompt 语义漂移。
**迁移**：板间关系（同景异角 vs 异空间）必须逐条显式声明并在台账记关系版本；引用他条结论前先核对其关系声明版别。

### 影墙入场法 [案例 7L #82]
> A doorway ignites...the amber door closes...a SHADOW appears cast across the cold stone wall — the elongated dark silhouette of a tall standing figure with a jagged, many-pointed crown...thrown flat against the stone as a shadow only...no physical body, no person, and no solid figure anywhere in the chamber. It holds, perfectly still, for a full two seconds.
**好在哪**：反派入场三段递进——关门（安全假象）→纯投影（no physical body 显式）→驻留 2 秒才散；影子=存在预告，本体永不露。
**迁移**：威胁预告写「纯投影+no physical body 声明+驻留配时」；影子细节（冠形轮廓）让身份可读而实体缺席。

### 环境层/建筑层分离 [案例 7L #187]
> @Corridor's own stone arch geometry stays exactly the same as its locked reference — no additional walls, structures, or elements beyond what the reference already contains. Only the environmental layer transforms: frost now coats every surface.
**好在哪**：六环换景的双层模型——建筑层锁死（零增补）+环境层自由变换（frost coats every surface）；「 Only the environmental layer transforms」一句划界。
**迁移**：同景换季/换材质写双层声明：建筑层 no additions+环境层 only transforms；防模型顺手加门加窗。

## 2026-11-07 增补：博客池 B2 批次（E395-E410 · 场景替换与光效）

### 场景替换三步标准流 [案例 thevzn BACKROOMS]
> reference plate→still→swap；**Object Swap not Motion Transfer** 选型区分；只换表面令（Keep the exact camera position, lens, perspective, and framing. **Change only the surfaces**）；融入式重打光三件（soft overhead+warm bounce+contact shadows）+**黑白守恒**（black stays black, white lettering stays clean）。
**好在哪**：场景替换的全流程标准化——板从实拍抽帧、参考图角度对齐相机、still 确认后再 swap。
**迁移**：换景按三步走；still 阶段锁构图；swap 阶段 Relight 三件+颗粒匹配。

### 对齐布景金律 [案例 cadycreates 车道→私人飞机]
> **Build the new scene around the movement you filmed.** If the new steps are in the wrong place, your feet can look like they're floating.
**好在哪**：从实拍抽帧规划新场景图——台阶对齐脚步；四参考图各司其职（近图管近步/宽图管远景/车图管门轴）；分步结尾脚本（低跑车五步上车序）。
**迁移**：换景先抽实拍帧定位；新场景围绕已拍动作搭建；动作差异（SUV→跑车）写分步序。

### depth map 工作流 [案例 alpius Draft Mode 替代法]
> **depth map keeps the motion, your reference images keep the looks** ｜ **Seedance has no seed. Only the upscale keeps your exact pixels…same shot, not the same pixels.**
**好在哪**：Draft 停用后的自建循环（480p 草稿→depth map→A 同像素 upscale 2cr/B 1080p 重渲 160cr/C 4K 220cr）；**depth map 盲区律**（only sees what has shape——250 arrows→empty sky，要么 A 保像素要么 prompt 重描述）；**灰底律**（Grey, not white——cleaner edges+声明 not part of the scene 防渗漏）；**切点实录法**（read off the video itself. **The draft rarely cuts where the prompt asked**）。
**迁移**：草稿-深度图-三 finish 分工；无形状物（粒子/雾）不入 depth map；灰底声明进每条 finish prompt。

### 光效继承与零特效转场 [案例 aeka/kaye PORTAL]
- **光斑五维继承**（aeka）：timing/location/direction/colors/intensity changes+双禁（删光斑救脸/无中生有）
- **零特效门转场**（kaye）：no glowing edges, no sparkles…**as if the door were simply the entrance**——超现实做成完全日常
- **灯类继承**（learnwithkayo GLOWING）：首败=neon outline 游戏感→修法 solid blown-out shape no outline+**real light source**


## 2026-11-13 增补：博客池收官批次 [官博 E435-E796 · 277 件全逐字蒸馏]

### 保留未点名部分论 [案例 官博 ad-multiplier · E777；higgsfield-genjutsu · E778]
> **replace selected elements while preserving the original motion, framing, cuts, timing, and other parts you do not ask it to change** ｜ **Genjutsu presets can do the whole job on their own — No prompt needed**
**好在哪**：换件工具契约=只改被点名项，其余（运动/剪裁/剪切/时序）原样保；presets 可独立完成免 prompt。
**迁移**：换件 prompt 只写改动项；简单换装直接选 preset。

### 实拍转 VFX 四步工作流 [案例 官博 VFX-with-Seedance-4k · 27K]
> **Shoot your raw footage → Let Claude analyze the clip → Describe your idea → Paste prompt and generate**——Claude 先拆解七要素（subject/motion/camera/lens/lighting/timing/aspect）
**好在哪**：实拍+AI 合成的标准管线——真人实拍打底、Claude 拆解、prompt 复刻生成。
**迁移**：真人与 AI 同框戏照走四步；拆解七要素清单照抄。

### 定点局部改论+双源素材 [案例 官博 higgsfield-genjutsu · E778]
> **target a specific element and change it locally, without regenerating or reshooting the rest — works on either real footage or generated video** ｜ 六用例双栏：**anime→live action 双向/同 clip 多 look 试装/raw phone clip→polished commercial**
**好在哪**：局部改定性（免重生成/免重拍）+双源素材（实拍与生成都行）+六用例各配 Change/Stay 双栏。
**迁移**：改一处用 Genjutsu 不整镜重跑；每用例先列改什么/保什么。

### 修复三前法+五判据 [案例 官博 ai-video-restoration-high-quality · E743]
> 前法：**Track down the best available source — re-compressed copies carry artifacts that restoration has to fight against**／**Keep the original frame rate and aspect ratio intact**／**heavily filtered footage can confuse what restoration fixes vs deliberate creative choice** ｜ 判据：**Natural detail not oversharpened / no new flicker by the pass itself / Preserved identity not generic / nothing that reads as clearly AI-generated sitting on top of otherwise real footage**
**好在哪**：修复前三查（最佳源/原参数/滤镜混淆）+五好判据（自然细节/无新闪/干净/身份保持/AI 痕不叠真实）。
**迁移**：修复任务先跑三查；出片按五判据验收。

### 最后放大论+单变量法 [案例 官博 how-to-edit-videos-with-ai · E735]
> **Upscaling comes last, once the content of the clip is settled, so credits aren't spent on enhancing a version that will change** ｜ **change one input at a time: the prompt, a reference image, or a setting** ｜ **Problems are easier to fix in the stage where they appear than after more edits are built on top**
**好在哪**：编辑顺序律（upscale 收尾省 credit）+单变量排查法+叠编辑难修论。
**迁移**：管线把 upscale 放最后；每轮只改一项；问题在哪层出现哪层修。

### 3D 预排布法+真几何论 [案例 官博 oliver-alge · E732；higgsfield-blender-plugin · E753]
> **first blocks the action and camera setup in 3D, then uses that as the basis for generation** ｜ **real, editable geometry, not a rendered image — move, scale, delete like any other object — can feed directly into a Video generation**
**好在哪**：复杂场景先 3D blocking 再生成（职业流程实证）；Blender Scene Builder 出真几何可入视频渲染。
**迁移**：多角色走位复杂时先 3D 排布定机位；Blender 管线直接产可编辑场景。


### 追补 THE_SHAPE_OF_MEMORIES（T3 #42）[E799]
- **video_edit 双任务单 prompt**：extend the scene…by adding a scene+Remove only the background music——延场+音频手术合体
- **照片微活三律**：animate this photo. blinking…dont change camera angle. dont zoom——眨眼微动+机位双禁
- **同帧位回忆切换**：zooming in→changing into another scene <<<image_2>>> with the same position in frame→zooms out
- **伸手抓镜转 POV**：stretches his arm towards camera and takes it——抓镜转第一人称
- **皮肤质感匹配**：adjust the face skin texture to be more like in the reference <<<uuid>>>


### 追补 THE_END_TO_THE_BEGINNING（T3 #43）[E800]
- **生物融合声明**：entirely biological and permanently fused with the creature's anatomy——骨剑手臂+形态排除群（must NOT resemble a claw, talon, hook, finger, tentacle, branch——六排）
- **原创装备三段**：chest-mounted action camera — entirely original and generic — must not resemble any specific commercial camera design
- **装备辨析令**：This is NOT a standard protective vest — must unmistakably look like parachute equipment——正名否定
- **服装拆离法**：Remove the body from the clothes, take the clothes, white background+服装平铺法（completely unfolded…laid completely flat——三件套平铺）
- **神秘光四不像**：must not resemble a normal spotlight, flashlight, fire, explosion, neon light, or obvious digital effect
- **建筑崩塌物理**：realistic structural failure — Do NOT make the building explode instantly——结构失效立法
- **白底定妆照三件**：BACKGROUND: PURE SOLID WHITE. NOTHING ELSE——角色定妆标准件
- **面部纹身设计对**：free of tattoos（无）vs original geometric abstract shapes following the natural contours（有——随轮廓）


### 追补 AURA（T3 #163）[E922]
- **残影到达系统全案**（ARRIVAL PHYSICS 段头四阶编号制）：1. One **leading after-image** appears at the empty destination. 2. Two upper **echoes** collapse downward into the leading silhouette. 3. The physical character descends into the silhouette and **becomes fully solid**. 4. The character lands under full gravity with bent joints, displaced gravel, moving stone, expanding dust, cloth follow-through, and camera vibration——+**垂直残影链**（Two fainter after-images appear directly above it, creating a **short vertical trail**）+**残影保留五件**（prone silhouette, sunglasses, clothing, empty back scabbard——残影含装备）+**残影剥离**（peels upward from his shoulders and dissolves into the wind）+**双曝光回声**（The residual silhouette splits into **two faint exposure echoes** and dissolves）+**残影恒定制金句**（The after-image effect in every teleport is **always a quickly fading, translucent blur** — **soft-edged and brief**——三处传送恒定）+** cloak-shaped shadow 拉入**（a cloak-shaped shadow **pull sharply inward** toward the arrival point）
- **传送特效族**：**手势触发制金句**（makes one sharp, stylish gesture…**on the instant it completes, he vanishes**——手势完成即传送）+**四厘米闪避金句**（position **shifts abruptly — displaced roughly four centimeters**…**pose completely unchanged**…The blade lands exactly where his body used to be——最小闪避）+**flicker 闪移**（Rival **flickers and is simply somewhere else**——无残影版本冲突）+**动模糊光条金句**（a sharp **streak of motion-blurred light and color** marks the path his body just took, already dissolving as the camera settles）+**禁静态复制金句**（**never a static duplicate figure or distinct ghost image**）+**幽灵角色禁令**（without creating duplicate limbs or ghost characters）+**条纹吸主色**（The motion streak **picks up Rival's own charcoal and crimson tones**, smeared and directional）
- **水特效族**：**水冠绽放金句**（The **water crown blooms outward** around the footfall in a slow drifting spray of droplets）+**三层水响应**（water crown→shallow concentric ripples→drifting golden droplets）+**涟漪预到金句**（the lagoon's surface **cracking into sharp ripples ahead of their feet before they even arrive**——脚未至水先裂）+**涟漪揭示镜面水斑**（the expanding ripples…**reveal a smooth mirror-like patch of water**）+**玉色水墙**（circular wall of **jade water**）+**沉积绽放**（Dark underwater sediment **blooms** beneath him）+**水滴弹道四段声明**（leave the wet strands in **one coherent arc, follow ballistic trajectories, catch sunlight, and fall behind** the rock）+**细雾卷须金句**（thin **tendrils of mist** begin curling up from the water's surface）
- **冲击波族**：**力延迟到达金句**（The force **reaches the camera half a beat after** Lamarana leaves——冲击波延迟）+**空震帧**（Hold the **empty shaking frame** for a fraction of a second）+**压力环入画变形云**（A pressure ring **enters the frame from outside and deforms the clouds**）+**螺旋环雾**（Their wake **bends the mist below into spiraling rings**）+**压力抬发**（His perfectly arranged hair **lifts from the pressure**——发型被冲飞）+**画外压力环**+**球形冲击波**（spherical pressure wave）+**能量环**（a visible **ring of energy** rippling outward in a perfect radial wave, flattening the surface for several meters）
- **混合媒体印刷质感全案**（VISUAL STYLE — LIVING ANALOG PRINT）：**八工艺**（gouache 水粉/watercolor 水彩/rough acrylic 丙烯/vintage screen printing 丝网/distressed offset lithography 胶版/coarse CMYK halftone dots 半调/imperfect ink registration 墨注册错位/chromatic color separation 色分离）+**五质感**（visible pigment/paper grain/paint bleeding/broken edges/tactile hand-made print texture）+**五不像声明**（must NOT look like clean digital animation/conventional anime/glossy CGI/polished concept art/简单滤镜照片）+**五元加法配方**（documentary cinematography + expressive painted illustration + vintage editorial poster + underground screen print + imperfect offset-printed graphic novel）+**振荡论金句**（constantly **oscillate between recognizable cinematic imagery and painterly abstraction**）+**非均匀半调**（Do NOT use uniformly applied halftone+**density changes naturally according to light and shadow**）+**颜料污染术语**（pigment contamination）+**高光颜料化**（Instead of polished CGI specular reflections, highlights appear as **broken strokes of bright pigment**）+**水滴颜料化**（Each droplet reads like scattered gouache or ink speckles）+**1-3 帧颜料拉伸**（pigment and halftone may visually stretch for **1–3 frames** into expressive printed motion accents）+**印刷运动重音**+**禁走样九条**（texture crawling 纹理爬行/halftone flicker 半调闪烁/**brush marks teleporting** 笔触瞬移禁）+**24 帧 AI 画禁令金句**（look like a coherent animated painting, **not 24 unrelated AI illustrations every second**——AI 逐帧漂移禁令）+**笔随形金句**（**Brushwork follows the form**. Halftone patterns remain spatially coherent）+**碎解不变形论金句**（Hair, fur, cloth…may partially fragment into painted streaks during movement. **However, character anatomy must NEVER become ambiguous or deformed**）+**漫画三叠法**（chunky graphic linework 粗线描边+cel-adjacent shading 赛邻阴影+printed comic texture）+**印刷漫画入三维金句**（a printed comic page **brought into three dimensions**）+**半调日光**（comic halftone **sunburst** radiating behind him）+**速线图形**（speed-line graphics/impact bursts/sparkle glints——洋红专用 comic accent graphics）+**九步工艺管线金句**（shot on imperfect analog film→enlarged→repainted with gouache and watercolor→overworked with acrylic→color-separated→covered with coarse halftone→screen-printed→misregistered→reproduced through a distressed vintage offset press — **yet somehow brought back to life as fluid animation**）+**可收藏声明**（collectible enough to function as a standalone printed character poster）+**短语堆叠收尾宣言**（Expressive pigment. Coarse halftone. Chromatic shadows. … Fluid action.——十一短语单行堆叠）
- **叶龙特效**：**拟翼制金句**（reading as **wing-like appendages** during flight…without needing literal feathered or membraned wings）+**叶彗尾**（closer to a **comet's tail of leaves** given momentary shape and purpose）+**叶缝透光金句**（Two eyes glow with a warm, soft golden **inner light showing faintly through gaps between the leaves**）+**散尾制**（never fully resolves into a **hard tip, always slightly dispersing**）+**流质体反硬鳞**（coils and flows with a fluid, **wind-driven quality rather than rigid scaled anatomy**）+**静图含动暗示金句**（A subtle, constant internal shift and rustle implied **even in a still reference — no leaf perfectly static**）+**低位捞乘**（sweeps low beneath him, **scooping him cleanly onto its broad back**）+**乘溶而降**（rides the **dissolving form** down）+**闻声不见鸟金句**（Birds call and take wing somewhere within the tree line, **their sound carrying clearly across the valley while they themselves stay unseen**）


### 追补 LATCH（T3 #166）[E925]
- **黑暗实体化奇幻规则全案**：**双不能规则金句**（The DARKNESS is **a physical thing**: a dense ink-black haze, like heavy slow smoke, with no face and no shape. **It cannot enter firelight and it cannot touch bread.**）+**黑海避火金句**（a man **sheltering at a fire in a black sea**）+**黑暗呼吸行为**（stands in a wall at the edge of the light, **swaying slightly**, **leaning in whenever the flames dip and recoiling when they rise**）+**黑暗嘶声**（the dry **hiss of the dark** rising and falling with the flames）+**黑暗贴近影深**（the darkness **leans in toward the shelf**, the photograph's shadows **deepening**）
- **转包金光推黑金句**：turns the loaf a quarter-turn, and as the crust **flares brighter gold** the circle of light **WIDENS a hand's width, pushing the black back**——烤壳金光扩光圈
- **火与面包共同拒夜金句**：the fire and the baking bread **holding the night off together**
- **门缝黑渗+蠕指+吞地纹金句**：BLACK DARKNESS begins to **seep through the gap under the door**: slow, **liquid**, **heavier than smoke**, pooling out over the stone **in thin creeping fingers**, **swallowing the texture of the floor** as it spreads——液态黑渗三属性
- **如水碰玻璃边界金句**：**stops at a clean curved line where the firelight lies on the stone**, **pressing against the light like water against glass, rippling, unable to cross**…**pulsing slowly against the boundary**——黑渗边界力学
- **光圈收缩+火光反推半米金句**：the room DARKENS **from the edges inward**: the corners, the ceiling beams, the window and the door **dissolve one by one** into ink-black…until the only remaining light is a **ragged circle**…**the firelight flares once and pushes the boundary back half a metre. He stays inside the light.**——逐件溶解+退入光圈+火光反推
- **面包光岛金句**：**two slow banks of black haze**…At **a hand's width from the crust** both banks **STOP, held by nothing visible**…**a clean island of warm light in the shape of the loaf's glow**, steam still rising untouched inside it——双岸夹逼+一掌宽止步+光岛+**日出雾退金句**（thins and pulls back **like mist at sunrise**）
- **LATCH 面粉负空间标题卡双机制**：**负空间标题金句**（revealed in the flour **as NEGATIVE SPACE** — the letters are bare dark wood where no flour lies）+**字形参考锁**（the tail of the L extended into a long curved sweep）+**两种显形机制**（**冲击波刮出** the surface **scoured down** in clean shapes to bare dark wood / **落粉沉积** the letters stand open in it as bare dark wood——同一标题两种物理成因）+FRAMING RULE 段头+**No other text 唯一文字声明**
- **面粉穿光金句**：the particles **blazing white as they cross the beam** and **vanishing into shadow** on either side of it——光带白燃影灭+**散成单粒**（thins away into **single drifting motes**）+**面粉波冲声**（the dry **rush** of a flour wave crossing the boards）


### [E926 · #167] VFX/能量体系
- **拟天金句**（破穹）：「the specific visual of **something technological pretending to be sky**」+码格声明（fine grid of light beneath）+楼级码片金句（shards **the size of buildings**…the code structure visible in each shard）+一帧天换金句（orange replaced by clean blue midday sky **in a single instant**）。
- **活字自书金句**（塔尔塔利亚）：「ancient living text **writing itself across bare skin** in warm golden light — line by line, character by character」+**双层同燃金句**（deep red Egyptian beneath and golden Maya script above, both blazing simultaneously）+**纹越界金句**（tattoos **crossing the boundary between skin and metal**）。
- **逆愈金句**：「The cuts **closing in reverse** — each cut sealing from the center outward…the damage **undoing itself visibly**」+金线封裂金句（crack sealing with **a thin warm golden line that fades**）。
- **拔羽体系**：非脱是撕金句（**not a clean detachment, a brutal ripping**）+白缝光裂金句（white seam light **shattering**）+着体红露金句（dark red where the armor **was integrated into the body beneath**）+逐羽残忍金句（**not in handfuls**…each feather grabbed **individually**）+颈环灭金句（white luminescence **cutting to nothing**——the most dramatic tone cut）。
- **天幕码格**：数字天穹段头+层叠透码墙（wall filling edge to edge **no visible top or bottom or sides**）。
- **半球冲击金句**（献音室）：「a **perfect geometric sphere**…**exactly half the bedroom radius**, the sphere's hard geometric boundary stopping at precisely the halfway point」+触毁金句（Everything the sphere physically contacts destroyed simultaneously…**the intact half untouched**）+净线金句（**The destruction line perfectly clean** at the sphere's radius）。
- **能量个体光金句**：亡灵红眼「as **individual practical light sources** throughout the tunnel walls」——群体光点化。
- **黑光金句**（赌场）：「every surface dark **until the UV hits it**, then it blazes electric blue and white」——紫外即显。


### [E927 · #168] 自然 VFX 新制（生物物理约束）
- **草物理段头金句**（IMPORTANT GRASS PHYSICS）：Individual blades bend/Separate/**fold** and sway+**草不速静金句**（does NOT instantly become perfectly still）+**草复原声明金句**（does not remain visibly flattened…stays dense and naturally upright）+**草缓金句**（When the hyenas slow down, the grass gradually settles）+**快慢回金句**（Some blades **return upright quickly**. Other blades continue swaying for a little longer）。
- **草不铺路六禁金句**：disturbed vegetation must **NEVER create a path**——NO flattened pathway/track/corridor/lane/trail/cleared strip——扰动不成径。
- **全野动画四禁金句**：Do NOT animate the entire field/Do NOT create synchronized waves/Do NOT make the grass **ripple like water**/Do NOT create artificial patterns。
- **本地响应金句**：real tall grass **responding locally to real animals moving through it**——局部响应=真实感判据。
- **草物理再升**：**bend, separate, fold and sway** 四动词+**振荡术语金句**（blades continue **oscillating** and slowly settle）。
- **萤火虫星空金句**：THOUSANDS OF TINY BIOLUMINESCENT GLOWWORMS…**a breathtaking natural starfield**——生物光源星空化+**唯一光源声明**（The glowworms provide **the only illumination**）+**无法辨界金句**（impossible to tell where the cave begins or ends）。
- **粒子三禁金句**：fireflies must NOT appear as **particles**/NOT form **geometric patterns**/NOT create **large glowing masses**——生物光禁粒子化。
- **融入金句**：The single firefly visually **blends into the larger natural population**——主角虫融入种群（收束手法）。
- **岩设七件金句**：massive natural **cliff wall**/vertically dominant/Natural weathering/Irregular cracks/Natural erosion/Rough stone texture/Physically realistic geology——岩壁七要素+**纪念碑尺度金句**（monumental sense of scale）。
- **天然天盆金句**：**an OPEN NATURAL BASIN** surrounded by massive vertical rock walls+**天开金句**（NIGHT SKY IS CLEARLY VISIBLE DIRECTLY ABOVE 大写）+**恒见天金句**（The sky must **always remain visible**）+五无顶金句——**穹顶禁律**。
- **天幕声明族**：拟天科技（#167）与天然天盆（#168）对照——人造天穹 vs 自然天盆两种天空叙事。


### [E928 · #169] 道具与屏显新制
- **4:17/WORK 来电叠加金句**："Provide a clean, trackable glimpse of the display for a later 4:17 / WORK incoming-call overlay. Do not invent readable phone lettering."——**片名 4:17 来源=来电显示**；屏显预留后期叠加、禁生成可读 UI。
- **屏换预留金句**（道具参考表）："Keep the screen surface unobstructed and clearly defined for later screen replacement."——黑屏预留后期换屏。
- **吊灯碎裂声谱**：一発の銃声→シャンデリアの一部が砕け→クリスタルの破片が光を受けながら落ちる→照明の本体は天井に残り、一部の灯りだけが消える——半残照明（店全体真っ暗にならない）。
- **一色に染めない金句**（画面全体を一色に染めない/no uniform neon wash）+**局部路灯金句**（localized streetlight）。


### [E929 · #170] 道具与物理新制
- **蝇法三段谱**：蝇法金句 THE FLY LAW flies are on the small dead animal in numbers and on the man's body Both are dead and both have flies——蝇群首现金句 for the first time in this entire film flies are on the animal IN NUMBERS——蝇法兑现金句 (clue one and this is its payoff)——蝇数收敛金句 EXACTLY ONE OR TWO FLIES total must be UNDERSTATED——蝇限半框金句 they stay in HIS half of the frame——蝇脸拍金句 A FLY SETTLES ON HIS CHEEK AND HE LIFTS A HAND——蝇上唇金句+无反应=点金句 That absence is the point of the shot——蝇落人不落驼对照谱。
- **皮记忆褶金句**：holding the memory of the shapes it has been packed into——皮革保留曾经装满的形状。
- **锤面金句**：Faint hammer facets across the shoulder from the beating——hand-beaten brass 锤打黄铜——焊缝金句 A soldered seam runs up one side。
- **铜绿金句**：Dark green-brown patina the verdigris of years never bright never uniform——verdigris 铜绿术语。
- **软硬金属光对比金句**：catches light the way soft metal does warm diffused highlights rather than hard white specular quite unlike steel——软金属光金句——锡硬光金句。
- **若大则败金句**：SIZE ANCHOR ABSOLUTE If it reads as large the asset has failed——尺寸锚段头。
- **实绳水金句**：it pours in a solid rope from the lota breaks over his hands runs down his forearms——水=实绳金句——慷慨倒水声金句。
- **舌润无益金句**：He runs a dry tongue over his split lips and it does not help。
- **入裂金句**：spreading into the split skin rather than beading on top or running off。
- **微错形金句**：slightly wrong in shape against the pale dunes。
- **俯图形化金句**：From this height the figures read as flat graphic shapes the turban a dark red circle the jhool a dusty rust rectangle the canisters four dark squares——头巾=圆/jhool=矩形/罐=四方块。
## #171 DON_CHENTE_S_ABDUCTION（E930）

- **能量场条款**：`its four sides and top formed entirely by a shimmering translucent lavender-violet energy field…held by four chrome corner struts`+`The barrier remains a shimmering translucent field throughout, never solid`——能量场恒闪烁禁实体。
- **能量场熄灭**：`The shimmering energy field of the enclosure flickers and deactivates completely, vanishing`+`not an instant disappearance`——闪烁熄灭禁瞬消。
- **compositing 留白**：`The composition leaves clear open space in the lower-middle to foreground area of the frame, suitable for compositing a spacecraft silhouette in the foreground later`——板留空待合成。
- **意大利面星星**：`las estrellas se deforman alargandose como espaguetis a consecuencia de el salto al hiper espacio`——超空间星体拉伸比喻。
- **紫血条款**：`The alien blood is purple, never red`——外星血色锁定。
- **大气生热**：`genera energia cinetica con calor al aproximarse a la tierra`+`desprende fuego…poco a poco se empieza a ver el cielo azul`——再入生热渐蓝。
- **机械幕启**：`abruptamente se abre una cortina metalica rapidamente de abajo hacia arriba`——下升金属帘。
- **反作用力位移**：`la velocidad lo empuja hacia atras, con rostro de esfuerzo`——加速后仰。
## #172 MISTER_M（E931）

- **石化特效**：`zamienianą w szary kamień`（进行时）→`biały kamienny posąg`（完成态）——灰化→白化两态。
- **黑暗红眼**：`Nagle gasną wszystkie światła…W kompletnej ciemności jarzy się para płonących, pełnych wściekłości oczu`——全灭+唯眼双段（jarzy się 燃烧态眼睛）。
- **渐暗收束**：`scena się przyciemna aż pogrąża się całkowitej ciemności`——渐暗至全黑。
- **烛光逐次亮起**：`Świeczki zapalają się jedna po drugiej`——逐帧点烛揭示（全亮版 wsystkie świece 为变体）。
- **黑中声先行**：`W kompletnej ciemności słychać odgłosy chaotycznych strzałów i głośnych męskich krzyków`——视觉先灭听觉先行。
- **烟雾散去**：`Dym po wystrzał opada`——枪烟沉降开场。
## #173 NIGHTBLOOM（E932）

- **果荚剥开金句**：`splits along its veins and peels open`——never shatters 禁碎裂（有机剥开非爆裂）。
- **液光恒常金句**：`the light does not switch on — it simply gets stronger`+`The light inside a pod only moves position, never changes in strength`+no pod ever dims, fades, flickers, darkens or goes out 五连禁。
- **THE POD IS A LIGHT SOURCE, ALWAYS 段头**：`It is NEVER a dull pale husk` 三连否定+GLOWS SOFTLY THROUGH THE CLOTH FOR THE WHOLE SHOT——布透光恒定。
- **白眼渐变**：`green drains out of the iris and a cold white creeps outward from the pupil`+gradual 1.5s never snaps+matte and dead 版（eyeshine 版本冲突）。
- **花捏灭**：`crushes the flower tightly inside its palm+The petals fold, tear and collapse naturally`。
- **影子局部制**：`Show only a partial, distorted shadow. Do not display a clearly outlined full-body silhouette`。
- **双光源分级**：`Two separate warm sources at different strengths`+`two separate lights of two different characters on the same body`——拳果 4500K vs 肩袋 dimmer。
- **光从地面来**：`All the light comes from BELOW, from a source on the ground that is never visible in frame`。
## #174 RAMIZA（E933）

- **泪中映像四版全案**：v1 MIRRORED REFLECTION shimmers — the soft distorted shapes…dreamlike, upside-down, barely readable+v2 **SUBTLE and DARK…just a ghost of two figures you have to look for**（你得去找的幽灵）+v3 **EXACTLY THE COUPLE FROM THE SECOND REFERENCE IMAGE**（映像绑参考）+His hair is NEVER curly——**The photographs themselves are NEVER directly visible** 全程锁。
- **皮影戏暴力转喻 v2**：THIS IS A SHADOW PLAY ON PLASTER+TWO SHADOW SHAPES（大小双影 MEET and OVERLAP+The smaller outline strains away from the larger）+影子对峙静版（**The two shadows do NOT touch and do not overlap — a clear gap of moonlit plaster stays between them**——影间空隙）。
- **弹丸追踪全案**：**the camera LOCKS ONTO THE PELLET and TRACKS IT in flight**+2x slow motion snap back+**a true tracking shot on a projectile, not a pan**（静版）+铅珠 4mm casting seam+**The ball is soft lead and heavy for its size: it deforms on impact instead of shattering** 软铅变形+**The impact is SMALL and unspectacular**+This is a simple round air-gun ball, NOT a bullet。
- **淤伤谱系**：豌豆淤伤（marks the size of peas, a day old, skin unbroken）→walnut 三色渐变（dark blue-violet middle fading through mauve to grey）+新旧双痕（yellow-green almost healed）→血肿修正模板（a real haematoma the width of a hand+IRREGULAR and blotchy+SOFT DIFFUSE EDGES+NOT as pellet wounds 四误认禁+No finger-shaped marks）。
- **百分百黑帧**：the final full second is PURE BLACK — 100% black frames+黑开场（camera already travelling）。
- **尘尾长逗号**：dust plume trails BEHIND as a long soft comma hanging over the road+the dust never sticks to the vehicle。
- **白三角衬衫**：worn CLOSED with only a small white triangle of shirt showing at the throat。
- **入墙转场族**：passes INTO the wall — half a second of soft warm darkness+like gliding into a tunnel+板缝黑转场。
## #175 RECURSION（E934）

- **泪中映像四版全案**（#174 复用）：MIRRORED REFLECTION/SUBTLE dark ghost（**just a ghost of two figures you have to look for** 金句——你得去找的幽灵）/EXACTLY THE COUPLE 绑参考/His hair is NEVER curly——照片 NEVER directly visible 恒定锁。
- **皮影戏暴力转喻 v2**：THIS IS A SHADOW PLAY ON PLASTER+**The two shadows do NOT touch and do not overlap — a clear gap of moonlit plaster stays between them**——影间空隙声明。
- **弹丸追踪全案**：**the camera LOCKS ONTO THE PELLET and TRACKS IT in flight**+**a true tracking shot on a projectile, not a pan** 金句+**The ball is soft lead and heavy for its size: it deforms on impact instead of shattering** 软铅变形+**This is a simple round air-gun ball, NOT a bullet**+**the flat dry SMACK of lead into hard wood** 大写拟声。
- **淤伤谱系四阶**（豌豆→walnut 三色渐变→血肿修正四误认禁）+百分百黑帧+**尘尾长逗号**金句+白三角衬衫+入墙转场族（like gliding into a tunnel）。
## 葡语 VFX 族（#176 SERVUS）

- **链绞杀物理**：`corrente grossa saindo de dois lados`+`o chão chega a afundar um pouco`+`sangue espirrando`——**链张力使地面下陷**（力量可视化为地形形变）。
- **复活非 CGI 金句**：`Olhos brilhando de CGI barato no lugar da respiração`（PROIBIDO）——**呼吸替代眼睛发光**的反特效声明。
- **蝴蝶碎翅象征场**（行263 seedance_2_0）：`asas vão quebrando e caindo pedacinhos…ela vai perdendo as forças até cair no chão, debatendo com as asas que sobrou`——分段解体+残翅挣扎。
- **月食阶段演化**（行317）：`a lua cobre metade do sol ainda, a lua esta indo pra esquerda, faça as nuvens em uma posição diferente`——**天象进度+云位重排**双变量推进。
- **坠落如雷**（行381）：`cada vez que ele cai, mais ele pega fogo e grita…faz um rastro longo`——坠落过程累计伤害叙事。
## 撞玻璃与翻车物理（#177 SEVEN_MINUTES_LEFT）

- **双尸撞玻璃**（119/390）：`ravenously hungry reanimated corpses are already in their final rush toward the pane`——饿极修辞+已在进行中开场。
- **玻璃破坏计数控**（464-465）：`Initial fracture points: two, each caused at a separate visible contact…Heavy blows in SHOT 2: exactly six`——裂缝网络计数（two fracture networks grown and begun connecting）。
- **翻车前奏链**（121：confrontation, siren, rollover）→474 翻定后 geometry——**翻车三段时序**（对峙→侧翻→翻定）。
- **板随门动**（416 族：`The boards do not block the doorway independently; they are physically attached to the door itself and move with it`）——**钉板物理归属**（板=门组件非门框组件）。
- **siren 闷化**（474：`physically muffled and distorted by the vehicle resting on its side`）——声学随车体姿态变化。
## 皮下光与能量语言（#178 SHADE & FADE）

- **皮下红光双律**（103/429：`FAINT RED LIGHT UNDER THE SKIN…light beneath the surface, never a painted glow on top, never drawn veins, never an aura`）。
- **双色不混制**（11/12/16/24：SHADE GREEN 右手/FADE AMBER-GOLD 左手——`The two colours never blend into each other and neither turns white`——**双刀色彩原子化**）。
- **红能量裂缝**（429：RED ENERGY RUNS IN THE CRACK LINES spreading outward——裂纹=能量通道）。
- **碎玻璃悬浮云**（449：hundreds of individual shards hanging motionless, each one catching a hard specular highlight）。
- **Shockwave ring**（429：CIRCULAR SHOCKWAVE OF RED ENERGY…lifting a low wave of dust）。
- **NO sparks 石咬声明**（26）+**NO shockwave ring 禁**（348 FORBIDDEN——普通踢禁冲击波）。
- **能量充能两版冲突实录**（421 energy blast 版 vs 全片 NO supernatural power 禁令——**同一项目内画风分层实录**）。
## VFX 与环境（#179 SHARDS OF WHEN）

- **PORTAL 8 拍白闪转场**（1-106：八拍白闪门过渡——转场拍数化）。
- **光束 redirects**（1-106：Nyra beam redirect——光束转向弹反）。
- **坍塌物理族**：massive ruined column deliberately brought down（72）+platform 塌陷（121/127）——巨物坍塌=敌人武器化地形。
- **雨环境**（97/494：Three Hunters emerge through the rain）+湿石（199：boots hammer across wet ancient stone, water splashes）。
- **文明穹顶飞船**（282 PULLING INTO SPACE：`colossal circular spacecraft, central transparent dome containing the civilization, enormous concentric ring[s]`）——飞船=携带文明设定。
- **环形行星**（210：the Ringed Planet — with a wide ring system——ASSET BINDING 语义绑定）。
- **金属长廊场景参照**（284：CHAMBER CORRIDOR / CEREMONIAL ENTRANCE — long elevated metallic corridor, reflective dark floor, glass railings）。
## 环境与氛围（#180 SHE NEVER LEFT）

- **ONE warm amber island per frame**——单暖岛律（每帧唯一暖源：standing lamp/ring light/hanging bulb/string lights/scan-monitor）。
- **圣物微光制**（114/142：the frayed pale gray scarf subtly luminous, slightly brighter than everything around it——头巾=圣物微亮标记）。
- **例外暖房**（155：DREAMY CINEMATIC GRAY grade with ONE exception…**the only room in this world where warmth wins**——产科房=全片唯一暖胜冷房间+the pink almost pastel-gray 粉色近褪）。
- **锈饼干盒锚物**（163：pulled halfway out from under it into one strip of light——半抽入光带）。
- **金句尾注族**：a fading memory being told aloud/a memory that still hurts to tell/the safe harbor at the end of a long remembered life/a memory the heart refuses to let go/a memory one wishes to forget/a memory that still aches/the room feels like it is holding its breath——**六种 mood 尾注变体**。
- **死人城空景**（23：qarafa — the City of the Dead+**a city of the departed sleeping inside the city of the living**）。
- **猫大小暖斑**（100：a stray cat-sized patch of warm light——暖斑体量比喻）。
## 海报合成与图层（#181 SIDE B）

- **图层序三明治**（338：recreate this image with the following layer order, from front to back: fingers/hand frontmost, "SIDE B" logo middle——**前中后三层序声明**）+**前景层级注记**（374：which sits on a layer in front of the "SIDE B" logo）。
- **chroma-key green 抠像底**（375/377/446：solid, flat, uniform green chroma-key color (standard chroma-key green, evenly lit, no gradients, no shadows)）。
- **纯黑底规格**（380/516：pure black (RGB 0,0,0), completely flat…zero noise, zero gradient, and zero compression artifacts——**RGB 三零三无**）。
- **删除填充背景延续**（339：Fill in the area where the logo used to be with a seamless continuation of the background — round, soft red/pink bokeh）。
- **HARD TONAL CUT 类**（263：HARD TONAL CUT 婚礼→诊所——此处为婚礼→诊所段内换调；同族确认）。
- **MARGIN 边距声明**（392：Generous plain dark space above title and below feet (see MARGIN). Never fill frame edge-to-edge——**禁满幅+边距段**）。
- **边距恢复声明**（445：to restore empty margin on the right edge of the frame, which has almost disappeared）。
- **故意重叠声明**（298：That overlap with the costume is intentional and fine）
## 特效与合成（#182 SIDE BY SIDE）

- **粒子书法系统**（5/9/32-36/75/79/82/85：彳亍 部首粒子——**中文部首拆字动画**+粒子方向（左下→右上）+粒子质感（乾燥墨粉或極細紙纖維）+二元结构（實體筆畫核心/邊界碎屑帶））。
- **主观限域慢快门**（10 族——滤镜只作用于视点内）。
- **同心旋转模糊**（180）。
- **擦除辅助线**（18——路径参考线成片禁现）
## VFX（#183 SILENCE LAVENDER）

- **烟转场桥接**（14 族 smoke transition bridge——首尾帧烟转场）。
- **删猫填景**（391/420 video_edit：Remove only the black cat from the shot. Delete the black cat and nothing else. Fill the small area…with a natural continuation of whatever kitchen surface is directly behind it——**删物+自然延续填景**）。
- **升清三不**（268/270/389/393：Upscale and enhance clarity without modifying any details, composition, or colors——**升清三不声明**；**sunburst 模型承接 82c 升清**）
## 海报与包装（#184 SIMPLE THINGS）

- **三比例海报族**（21/28：9:16 vertical；27：16:9 YouTube thumbnail；29：21:9 ultra-wide——**竖版/横版/超宽三比例**+**YouTube 缩略图版式首例**）。
- **裸 UUID 三连海报**（21/27/28/29：三 UUID 连排+poster——**UUID 群+版式**）
## 神话地理与生物（#185 SINDBAD）

- **鱼背岛金句**（it is secretly the huge long low back of a sleeping ancient fish…The island must look naturally grown, never arranged or landscaped——**岛=沉睡古鱼之背+自然生长禁布置**）。
- **猴城系统**（ancient monkey city carved directly from dark wet basalt above a cold open sea——黑湿玄武岩崖城+sole architectural reference 唯一建筑参考+同城石凿空房）。
- **墓室保持**（Preserve the attached burial chamber exactly: same dark doorway framing, same low oval stone resting platform, same round oculus with its single soft shaft of daylight, same three deep oil lamps——**天井独光柱+三油灯**+uninhabited and without a body 无尸+褪色靛蓝布非黑布）。
- **Rukh 大鹏设定**（immense, historically plausible marine predator——**历史可信海洋捕食者**+physically believable rather than a fantasy mascot **物理可信非吉祥物**）。
- **地下河/极窄水道**（black water slips beneath a low wet rock ceiling…No lamps 无灯黑水+so low and tight that a person could later only lie flat on a tiny raft——**仅容平躺木筏**）
## VFX 与环境板（#186 SITARA）

- **VFX plate 空板声明**（vfx plate no crowd and audience——**phototrelasitic 笔误**）+**EMPTY of people 板族**（market street/bank/local train interior/chowk——**空人环境四族**）+**densely crowded 反版**。
- **found-footage**（SCENE CONTEXT A found-footage insert）+**16mm top angle**（can you give a wide top angle 16 mm——**16mm 胶片锚**）。
- **peephole 金洪转场**（#186 独有：琥珀洪）+**top-down commode 板族**（Directly overhead top-down photograph——**天花板直下**）
