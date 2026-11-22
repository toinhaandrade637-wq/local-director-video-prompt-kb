<!-- 去敏副本：仅移除媒体访问标识和签名地址，提示词正文保留。 -->
<title>【实践手册】Doubao-Seedance-2.5：企业级业务场景实践指南</title>



<callout emoji="🎞️">
Doubao-Seedance-2.5 是豆包大模型团队推出的，新一代**专业级多模态视频创作模型**。
模型支持单段 **30 秒视频直出，**单次可输入图像/音频/视频 **最多50 个参考素材**，具备更强的指令控制，专业级可控的视频编辑与延长能力；同时，原生支持生成 **10 余种语言** ，保障专业级叙事在全球化场景中稳定落地，让视频生成 迈入「**长叙事 × 强参考 × 准编辑 × 多语言**」的工业级新阶段。
模型创作能力持续深化，画面 **真实感** 显著增强，在**光影表现**、**表演理解与执行**、**镜头运动**上都更**接近真实拍摄**，成片质感与叙事可信度大幅提升，为专业创作者与企业客户提供更高效、更可控的视频生产能力。
点击直达 ➡️ [方舟体验中心](https://console.volcengine.com/ark/region:cn-beijing/experience/gen_video?model=doubao-seedance-2-5-260628)
</callout>



# 「 🌟Summary 」Seedance 2.5 关键更新 

<table><colgroup><col/><col/><col/></colgroup><thead><tr><th vertical-align="middle">#</th><th vertical-align="middle">维度</th><th vertical-align="middle">一句话记忆点</th></tr></thead><tbody><tr><td vertical-align="middle">1</td><td vertical-align="middle"><b>核心定位</b></td><td vertical-align="middle">新一代专业级多模态视频创作模型，「<b>长叙事 × 强参考 × 准编辑 × 多语言</b>」四大能力升级</td></tr><tr><td vertical-align="middle">2</td><td vertical-align="middle"><b>四大能力升级</b></td><td vertical-align="middle"><ul><li><b>30s 直出</b>　单段直出从 15s 提升到 30s，全球第一</li><li><b>50个 参考素材 </b>单次最多 50 个素材联合输入，全球最多</li><li><b>专业级可控编辑</b>　锁定整体画面不变、只改局部</li><li><b>原生多语言    </b>支持 10 余种语言</li></ul></td></tr><tr><td vertical-align="middle">3</td><td vertical-align="middle"><b>生成效果提升</b></td><td vertical-align="middle">模型生成效果全面提升，从高阶影视创作这个最严苛的视角来检验：<b>光、镜头运动、表达及感染力 </b>都有明显进步，AI 感大幅减弱，生成结果更接近真实拍摄</td></tr><tr><td vertical-align="middle">4</td><td vertical-align="middle"><b>🌟全模态参考</b></td><td vertical-align="middle"><ul><li>一次可投喂 <b>50 个参考素材 = 30 张图 + 10 段视频 + 10 段音频</b>，音/视频总时长最长 30s</li></ul><blockquote><p>相比 2.0（图 9→30、音视频 3→10 段、总时长 15s→30s）</p></blockquote><ul><li>本次<b>新增</b><b>「只参考音频」</b>：可直接用一段 BGM / 人声 / 音效驱动画面节奏、卡点与口型对齐</li></ul></td></tr><tr><td vertical-align="middle">5</td><td vertical-align="middle"><b>典型应用场景</b></td><td vertical-align="middle">能力升级既解锁全新场景，也让原有场景的创作效率再上一个台阶。最能体现模型能力的三类：<b>高阶影视创作、知识创作、复杂广告 Demo。</b>完整「场景 × 能力」矩阵见第四部分</td></tr><tr><td vertical-align="middle">6</td><td vertical-align="middle"><b>模型价格</b></td><td vertical-align="middle">〔待补充〕</td></tr></tbody></table>



# 「对客文档总览」一键直达

<table><colgroup><col/><col/></colgroup><thead><tr><th vertical-align="middle">文档</th><th vertical-align="middle">直达链接</th></tr></thead><tbody><tr><td vertical-align="middle"><b>国内对客 One Page</b></td><td vertical-align="middle"><cite doc-id="SUNxwqAdGil0LRkokjHcqgajnTc" file-type="wiki" title="【对客】豆包视频生成模型  Doubao-Seedance-2.5-中文（价格未更新）.pdf" type="doc"></cite></td></tr><tr><td vertical-align="middle"><b>海外对客 One Page</b></td><td vertical-align="middle"><cite doc-id="D6j4b38i3odYhcxRfa3cSNVxnIh" file-type="file" title="[External] Dreamina-Seedance-2.5 Brochure.pdf" type="doc"></cite></td></tr><tr><td vertical-align="middle"><b>海外实践手册</b></td><td vertical-align="middle"><cite doc-id="O3mXwSFm5i48IJkjXdNcHsqDnfd" file-type="wiki" title="「Practice Guide」Dreamina-Seedance-2.5 Enterprise Use Case Guide" type="doc"></cite></td></tr></tbody></table>



# **一、能力升级**

## 1.1 ｜突破叙事边界：30s 视频直出，高保真时序延长

- Seedance 2.5 支持单段 **30 秒视频直出**，镜头表达更连贯，无需后期拼接即可呈现完整的情绪起伏与剧情推进；
- 同时具备 **高保真时序延长** 能力，可在保持人物、场景、镜头一致性的前提下，把短素材自然延展为更长成片，大幅提升创作效率与成片品质。尤其适配广告 TVC、短剧、品牌故事片等对叙事完整度要求高的场景。

<table><colgroup><col/><col/><col/></colgroup><thead><tr><th vertical-align="top">Seedance 2.5 · 30s</th><th vertical-align="top">Seedance 2.0 · 15s</th><th>Prompt</th></tr></thead><tbody><tr><td vertical-align="middle"><figure view-type="Preview"><source name="1ca529c7100f90a83f030898f10df273_raw.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="3858184" token="[媒体标识已移除]"/></figure></td><td vertical-align="middle"><figure view-type="Preview"><source name="1ca529c7100f90a83f030898f10df273_raw.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="1518174" token="[媒体标识已移除]"/></figure></td><td vertical-align="middle"><pre caption="Seedance 2.5&#xA;" lang="HTML" wrap="true"><code>以 @视频1 为原片，保持沙发、配色、光影与运镜逻辑完全一致，在其结尾自然延长时序、无缝续接暖光客厅生活场景：女主人穿米白针织家居服坐在同一张沙发上读书、腿上搭米白毯，把咖啡杯轻放到茶几；猫轻轻跳上坐垫；孩子跑入靠到肩上，女主人低头微笑；夜晚落地灯亮起，三者安静靠在沙发上，镜头缓慢后拉定格，画面留出品牌标识空间。</code></pre></td></tr><tr><td colspan="3" vertical-align="middle"><blockquote><p>参考 2.0 的 15s 成片，将广告延长至 30s ，在纯影棚产品展示之后，衔接暖光客厅的生活场景，把一条广告从「只有产品」讲成「产品 + 使用故事」</p></blockquote></td></tr></tbody></table>



## 1.2 ｜全模态参考扩容：支持上传 50 个全模态参考素材

- 2.5 将单次输入素材上限提升至 **50 个全模态素材**（图片 / 视频 / 音频自由组合），让创作者可以一次性投喂完整的角色集合、场景集合、参考镜头与品牌音乐，模型综合理解后输出高度贴合创意意图的成片；

<table><colgroup><col/><col/><col/></colgroup><thead><tr><th><b>能力点</b></th><th vertical-align="middle"><b>影视群像戏</b></th><th vertical-align="middle"><b>多场景连贯性</b></th></tr></thead><tbody><tr><td vertical-align="middle"><b>参考素材</b><b>多</b><br/>多主体一次投喂，跨镜头稳定保持</td><td vertical-align="middle"><figure view-type="Preview"><source name="舞会-420音乐.mov" mime="video/quicktime" origin-height="1080.000000" origin-width="1920.000000" size="59624380" token="[媒体标识已移除]"/></figure><blockquote><p>各角色面孔、神态、服饰跨镜头稳定保持</p></blockquote></td><td vertical-align="middle"><figure view-type="Preview"><source name="石榴引入 0622.mp4" mime="video/mp4" origin-height="1080.000000" origin-width="1920.000000" size="62705422" token="[媒体标识已移除]"/></figure><blockquote><p>同一主体跨多个场景切换，形象与风格始终统一</p></blockquote></td></tr></tbody></table>

- 对高复杂度素材的 **稳定保持能力** 同步增强，专业级 3D 白模、产品包装、品牌 VI 等资产均可精准承接，实现 **结构**、材质与镜头调度逐帧还原。

<table><colgroup><col/><col/><col/></colgroup><thead><tr><th><b>能力点</b></th><th vertical-align="middle"><b>高难度白模预演</b></th><th vertical-align="middle"><b>结构拆解/还原</b></th></tr></thead><tbody><tr><td vertical-align="middle"><b>参考能力</b><b>强</b><br/>高复杂度资产逐帧高保真承接</td><td vertical-align="middle"><figure view-type="Preview"><source name="飞船-594音乐.mp4" mime="video/mp4" origin-height="1080.000000" origin-width="1920.000000" size="38425751" token="[媒体标识已移除]"/></figure><blockquote><p>复杂 3D 白模的结构与镜头调度逐帧承接，渲染出成片质感</p></blockquote></td><td vertical-align="middle"><figure view-type="Preview"><source name="多模态参考视频生成6.23.mp4" mime="video/mp4" origin-height="1080.000000" origin-width="1920.000000" size="127787159" token="[媒体标识已移除]"/></figure><blockquote><p>不止外观一致，参考图中的搭建结构与逻辑也被精准还原</p></blockquote></td></tr></tbody></table>



## 1.3 ｜准确视频编辑：专业级打磨，创作显著提效

- Seedance 2.5 具备强大的 **视频局部编辑** 能力，在维持整体画面、镜头与节奏不变的前提下，对画面内的背景、商品、人物等局部元素进行精准修改，实现「一次创作、多版交付」

<table><colgroup><col/><col/></colgroup><thead><tr><th>年龄/表情 替换</th><th>风格替换</th></tr></thead><tbody><tr><td><figure view-type="Preview"><source name="视频编辑·表情年龄6.23.mp4" mime="video/mp4" origin-height="1080.000000" origin-width="1920.000000" size="107583790" token="[媒体标识已移除]"/></figure></td><td><figure view-type="Preview"><source name="多风格替换6.23B.mp4" mime="video/mp4" origin-height="2160.000000" origin-width="3840.000000" size="113983542" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>



## 1.4 ｜拥抱全球创作者：原生支持 10余种语言

- Seedance 2.5 原生支持 **10 余种 语言** ，全球创作者均可以母语描述创意意图，无需借助翻译或额外的语言转换；

  > 中文、英语、西班牙语、印度尼西亚语、马来语、泰语、阿拉伯语、葡萄牙语、越南语、日语、韩语等
- 同时大幅强化 **指令理解与控制** 能力，对复杂镜头调度、情绪转折与多层次场景描述都能更精准遵循，真正服务**面向全球的创作与商业化场景**。

<table><colgroup><col/><col/><col/></colgroup><thead><tr><th>能力点</th><th vertical-align="middle"><b>美妆广告 </b></th><th vertical-align="middle"><b>家居广告</b></th></tr></thead><tbody><tr><td vertical-align="middle"><b>多语种 书写/发音</b><br/>不仅能按目标语言实现准确的书写与发音，还能依据语种替换匹配的人物面孔等元素</td><td vertical-align="middle"><figure view-type="Preview"><source name="demo-口红.mov" mime="video/quicktime" origin-height="1080.000000" origin-width="1920.000000" size="35688286" token="[媒体标识已移除]"/></figure><blockquote><p>母语口播自然流畅，卖点节奏与镜头指令精准遵循，广告级质感一次到位</p></blockquote></td><td vertical-align="middle"><figure view-type="Preview"><source name="多语言生成6.23.mp4" mime="video/mp4" origin-height="2160.000000" origin-width="3840.000000" size="107679878" token="[媒体标识已移除]"/></figure><blockquote><p>多语种旁白与安装步骤逐句对齐，复杂指令控制精准还原</p></blockquote></td></tr></tbody></table>



# 二、关键能力详解 



## 2.1 ｜能力界定：视频参考 🆚 视频编辑/延长

Seedance 2.5 具备全模态参考能力，视频生成在准确率与效率上均有显著提升，让成片效果更贴近创作者的心中所想。

- 基于**全能参考生成**，进一步延伸出**视频编辑**与**视频延长**两类能力：模型支持视频与图片、音频等参考素材的自由组合，再结合文本指令的精细化描述，编辑过程可获得更强的可控性，实现更精准的局部改写与续写。



但在实际创作中，参考、编辑、延长这三类能力常被混用，导致 Prompt 错位、素材引用方式失当，最终影响生成结果的可控性与稳定性。

- **参考生成：无既有成片，以图片 / 视频 / 音频作为参考素材，从0生成一段全新视频**

  > 📐Prompt = 生成要求（文本）+ 参考素材（ @视频N @图片N @音频N）

  | 子能力 | 含义 | Prompt 示意 |
  |-|-|-|
  | **主体参考** | 参考人 / 物 / 场景 / 虚拟角色等主体的外观 ID 或声音，可通过主体图、主体音视频或组合参考 | 以 @图片1 中的女性主角为主体形象，生成其在城市街道漫步的视频 |
  | **运动参考** | 参考图 / 视频的运动及动态信息，包括动作、表情、运镜、创意、特效等；可与主体参考组合 | 参考 @视频1 的运镜方式与主角奔跑节奏，主体形象采用 @图片1，重新生成一条产品广告 |
  | **白模参考 / 渲染** | 输入粗粒度或细粒度白模视频，参考其动态信息并进行渲染；可与主体参考、场景参考组合 | 基于 @视频1 白模的运动轨迹渲染成片，主体形象参考 @图片1，场景参考 @图片2 |
  | **风格参考** | 参考图 / 视频的风格；可与主体参考组合 | 画面风格参考 @视频1 的冷蓝夜景与颗粒感调色，主角形象参考 @图片1 |
  | **音频参考** | 参考音频的音乐 / 旋律 / 台词 / 音色等声音信息；可与主体参考组合 | 音乐氛围参考 @音频1，画面主体参考 @图片1，生成一条节奏契合的短片 |
  | **宫格分镜 / 故事板参考** | 参考分镜图的主体 / 动作 / 剧情等信息，支持多宫格分镜或分镜 + 主体组合 | 依据 @图片1 的四宫格分镜顺序展开，主角形象参考 @图片2，逐格推进主角的一天 |
  | **关键帧参考** | 输入单个或多个图片作为关键帧生成视频，支持关键帧分镜参考生视频、首帧生视频、首尾帧生视频 | 以 @图片1 为首帧、@图片2 为尾帧，中间补全主角由室内走向室外的过渡 |
  | **一键成片** | 输入多段图片 / 视频素材，模型串联生成短片，可添加文字、贴纸、转场等；支持素材一键成片或素材 + 参考视频一键成片 | 将 @视频1、@视频2、@图片1 依次串联为 15 秒短片，加入片头文字与转场 |
- **视频编辑：已有一段成片，对其中局部内容进行改写、替换或增删**

  > 📐Prompt =修改要求（文本）+ @视频1（原片）+ 可选 @图片N / @音频N

  | 子能力 | 含义 | Prompt 示意 |
  |-|-|-|
  | **视频指令编辑** | 通过文本对视频画面进行增删改编辑，支持输入时间戳指定编辑生效时段 | 将 @视频1 中 0:02–0:05 时段的场景替换为中世纪石堡平台，人物动作与节奏保持不变 |
  | **参考图编辑** | 通过文本 + 参考图对视频画面进行增删改编辑，支持输入时间戳指定编辑生效时段 | 将 @视频1 中深色衣着男子的服饰替换为 @图片2 的服饰，其余画面保持不变 |
  | **新增主体** | 在原片中增补人物、道具或特效元素，其余画面保持一致 | 保持 @视频1 的人物、环境、构图不变，人物手中出现能量弓 @视频1 |
  | **删除主体** | 移除原片中的水印、穿帮或指定对象，并对空缺区域自然补全 | 删除 @视频1 中的无人机与前景轨道，对删除区域进行自然补全，其余保持不变 |
  | **音频编辑** | 对视频声音进行增删改，包括替换 BGM、增补音效、修改人声等 | 保持 @视频1 的画面与运镜不变，将背景音乐替换为 @音频1 |
- **视频延长：已有一段成片，模型基于原片的画面、节奏与风格续写新片段，包括向后续写、向前续写，两段或三段视频中间补全**

  > 📐Prompt =修改要求（文本）+ @视频1（原片）+ 可选 @图片N / @音频N

  | 子能力 | 含义 | Prompt 示意 |
  |-|-|-|
  | **向后延长** | 以原片尾帧为起点，向后续写新的片段，可要求画面 / 音频无缝衔接；可与主体参考组合 | 以 @视频1 的尾帧为起点，续写 6 秒：主角走出画面，天色渐暗，路灯次第亮起，画面与音频无缝衔接 |
  | **向前延长** | 以原片首帧为起点，向前补齐前情片段，可要求画面 / 音频无缝衔接；可与主体参考组合 | 以 @视频1 的首帧为终点，向前补 4 秒前情：主角自远处步入镜头前的场景，画面风格与首帧一致 |
  | **视频无缝转场** | 输入两段视频，模型生成补全间隙实现无缝转场 | 在 @视频1 与 @视频2 之间生成 3 秒过渡段，实现画面、色调与运镜的无缝衔接 |

## 2.2 ｜参考素材上限及组合方式

### 💬 50 参 = 30图 + 10视频 + 10音频

Seedance 2.5 将参考素材的总量、单类配额与单段时长同时扩容，一次生成最多可承载 **50 个**参考素材，涵盖图片、视频、音频三类模态，为角色、场景、镜头、音乐等信息的完整表达提供了充足的输入空间。

<callout emoji="📌">
 **50 个参考素材 = 30 张图 + 10 段视频 + 10 段音频**
- **参考图**

  - **0～30 张**，4K 以内，单张图不超过 30MB
  - 格式支持 jpeg、png、webp、bmp、tiff、gif、**heic**、**heif**
- **参考视频**

  - **0～10 个**参考视频，支持480p-4k，单个视频不超过  200 MB
  - 格式支持 mp4、mov
  - 单个视频时长 [2, 30]s，全部视频总时长 ≤ 30s
- **参考音频**

  - **0～10 个**参考音频，单个音频不超过 15MB
  - 格式支持 mp3、wav
  - 单个音频时长 [2, 30]s，全部音频总时长 ≤ 30s
⚠️ 注：视频时长与音频时长分开计算， 分别可上传30s
</callout>



### 🎵 支持仅音频参考，图/音/视频自由组合



在 Seedance 语言体系中，**通过 @ 符号 投喂素材**，来锁定画面信息，达到理想标准态。

- 每引用一个素材就紧跟一句使用声明，当有多个人物或多段视频时，**必须明确对应关系**，否则模型会混淆（避免 “参考 @图片1” 这类无头无尾的写法），一般来说：



- 2.5 **新增支持只参考音频，**共 7 种模态组合：只参考图片、只参考视频、**【新增】**只参考音频；组合参考图片+视频、组合参考音频+视频、组合参考图片+音频；组合参考音频+图片+视频

<table><colgroup><col/><col/><col/><col/><col/></colgroup><thead><tr><th vertical-align="middle"><b>组合方式</b></th><th vertical-align="middle"><b>搭配组合示例</b></th><th><b>参考素材</b></th><th><b>生成结果</b></th><th><b>Prompt</b></th></tr></thead><tbody><tr><td vertical-align="middle"><b>单模态</b></td><td vertical-align="middle"><b>只参考音频</b><b>（本次新增）</b></td><td><grid><column width-ratio="0.500000"><figure view-type="Preview"><source name="音色大.MP3" mime="audio/mpeg" size="48951" token="[媒体标识已移除]"/></figure></column><column width-ratio="0.500000"><figure view-type="Preview"><source name="小音色.MP3" mime="audio/mpeg" size="53966" token="[媒体标识已移除]"/></figure></column></grid><figure view-type="Preview"><source name="环境底噪.MP3" mime="audio/mpeg" size="119586" token="[媒体标识已移除]"/></figure><figure view-type="Preview"><source name="背景音乐.mp3" mime="audio/mpeg" size="97434" token="[媒体标识已移除]"/></figure></td><td><figure view-type="Preview"><source name="声音case.mov" mime="video/quicktime" origin-height="1080.000000" origin-width="1920.000000" size="27230024" token="[媒体标识已移除]"/></figure></td><td><pre caption="Seedance 2.5&#xA;" lang="SQL" wrap="true"><code>【两只守宫的越狱会议 — 3D 动画 | 马戏团后台 | 约 20 秒】<br/><br/>【一句话梗概】 开场先留一段环境空镜交代"这是马戏团后台"，随后两只守宫（一只胖胖的、一只小小的）商量逃出马戏团的策略，爆发简短争执，最后达成一致；以放大的马戏团后台环境音底噪为主，背景音乐几乎全程铺底、在关键情绪点加强。<br/><br/>【角色参考（外形 100% 保持一致，全程不漂移）】<br/>——胖胖：一只体型胖圆的守宫，圆滚滚的肚子、四肢短粗、皮肤是暖褐带斑点的哑光鳞纹，尾巴又粗又短、储着脂肪显得肉墩墩，趾垫宽大，脸颊鼓鼓、大眼圆睁，表情憨厚，动作慢半拍；性格谨慎、怕事、爱吃，但关键时刻能鼓起勇气想出办法。<br/>——小小：一只体型娇小的幼年守宫，眼睛又大又亮、几乎占满小脑袋，皮肤是浅黄绿的鲜嫩鳞色、带细小斑点，尾巴细而灵活，趾尖能吸附攀爬，动作机灵跳脱；性格急躁、冲动、天不怕地不怕，是提出越狱的那一个。<br/><br/>【声音参考（每角色声线固定）】<br/>胖胖：低沉憨厚的中年雄性嗓音，语速偏慢，带点胆怯的颤音。参考【音频1】。<br/>小小：又高又快的少年嗓音，尖锐冲动，情绪一上来就破音。参考【音频2】。<br/>【环境音效参考】<br/>——环境：全程铺一层马戏团后台的环境音底噪（远处帐篷内的嘈杂、隐约的动物响动、帆布被风吹动、木架吱呀、远处人声混响等），作为场景氛围底噪；环境音效音量整体放大，尤其在开场空镜段落最为突出，是全片的主要声场；环境音效参考【音频 3】。<br/><br/>【背景音乐参考】<br/>——点缀：一段背景音乐（俏皮悬疑、轻快带一点紧张感），几乎全程铺底、出现时长较长，从开场空镜就轻轻淡入，在提议、争执高潮、结尾定格处音量加强；仅在对白密集时短暂压低，让位给台词，但不完全消失，不覆盖对白、不喧宾夺主；音乐参考【音频4】。<br/>【场景锁定（几何恒定，全程不漂移）】<br/>马戏团后台：一个昏暗杂乱的马戏团后台帐篷内，环境音底噪参考环境音效 —— 左侧是一排关动物的铁笼（冷光从笼缝透入），中央是几只堆叠的道具箱与卷起的彩色帐篷布，右侧是通往外面的帆布帘出口（缝隙透出夜色蓝光）与一盏摇晃的暖黄挂灯，地面是踩脏的木屑与稻草。布局锁定：两只守宫围着中央一只当桌子用的大道具箱 —— 胖胖 趴在箱子左侧（x~30%），背靠铁笼；小小 攀 / 蹦在箱子上方或右侧（x~65%），最活跃，趾尖时不时吸附在箱面上。出口在画面最右。<br/>【3D 动画风格 / 画面质感】 高品质 3D 动画，鳞片与皮肤精细渲染（可见每片鳞纹的细腻质感、皮肤微光泽与肌肉运动、趾垫吸附的柔软感），角色表情夸张而生动、富有卡通表演张力；夜晚马戏团后台的氛围 —— 冷蓝色环境光为主、右侧暖黄挂灯为辅，teal-and-amber 冷暖对比，浅景深，电影级打光，55mm 虚拟镜头。<br/><br/>【镜头语言】 手持感的灵动运镜带真实操作重量；剪辑节奏由情绪驱动，情绪爆发点可与【音频4】点缀 加强的重拍呼应。开场用环境空镜交代场景，随后每个段落先用一个定位广角交代两只守宫的相对位置，再切入覆盖镜头。适度使用节奏性调度：快速甩镜在两个说话者之间切换、猛推特写（crash-in）卡在情绪爆发点、争执时快切正反打。面部特写要拍到眼神、竖瞳收缩、喉部鼓动、趾尖抓握与嘴型；视线互相对视、绝不看镜头；自然的眨眼（含守宫式舔眼）与眼神流动。硬切，无叠化。<br/>【硬性锁定】 全程只有两只具名守宫，无第三只守宫、无群众、无分身克隆；两者体型差异（胖圆 / 娇小）每一帧都保持；对白逐字念出（英文），同一时刻只有一个主要说话者（争执高潮允许短暂抢话重叠）；开场空镜段落无对白；音轨层次：放大的 【音频3】环境底噪为主、【音频4】点缀 背景音乐长时间铺底并在关键点加强、不覆盖对白；无字幕 / 画面文字；3D 写实鳞片皮肤、稳定、无多余肢体或重影。<br/><br/>镜头 1（0–3 秒）· 环境空镜（无对话）<br/>纯环境镜头，无角色对话：镜头缓慢扫过马戏团后台帐篷内部——左侧关动物的铁笼冷光、中央堆叠的道具箱与卷起的彩色帐篷布、右侧透出夜色蓝光的帆布帘出口与摇晃的暖黄挂灯、地上踩脏的木屑稻草。此段 环境音底噪音量最大、最突出（帐篷嘈杂、远处动物响动、帆布被风吹动、木架吱呀），从这里轻轻淡入铺底，明确交代"这里是马戏团后台"。硬切。<br/><br/>镜头 2（3–7 秒）· 定位 + 提议<br/>定位广角带出两只守宫围着中央道具箱。硬切。—— 手持中景推近 小小（音色参考【音频2】），它蹦到箱子上、趾尖啪地吸住箱面（伴清脆吸附音效），压低又急促:"Tonight — we break out of here!" —— 反打 胖胖（音色参考【音频1】）面部特写，喉部一缩、竖瞳一颤，颤声:"B-break out? It's dangerous…"<br/><br/>镜头 3（7–13 秒）· 争执对抗（高潮）<br/>争执快切正反打，允许短暂抢话重叠，—— 小小（音色参考【音频2】）跳脚，尾巴甩动，指着胖胖，破音:"You're just a coward!" ——胖胖（音色参考【音频1】）罕见地拔高音量盖过它，快哭了:"Stop shouting — the guard'll hear us!" 面部特写：两张脸各自的怒与慌，竖瞳收缩、喉部与尾巴剧烈抖动；争执尖峰处音乐与环境底噪短暂压低，突出两只的争执声。<br/><br/>镜头 4（13–18 秒）· 转机 + 达成一致<br/>——胖胖（音色参考【音频1】）忽然壮起胆子，认真:"I'll block the guard. You slip out and open the door." —— 甩镜到小小，愣了一下，竖瞳松动，咧嘴一笑:"…That actually works!"（音乐回暖、音量重新抬起）<br/><br/>镜头 5（18–20 秒）· 定格击掌<br/>慢推两守宫并肩双人镜头：两只守宫伸出小爪（趾垫相贴）叠在一起（伴轻轻的趾垫相碰音效），眼神一致望向右侧出口，【音频4】点缀 收尾一记加强的重拍收束。小小（音色参考【音频2】）低声:"Midnight. We move." 帆布帘缝的夜光映在两张下定决心的脸上，画面在它们坚定的表情中定格，放大的环境底噪与音乐一同缓缓收尾。<br/><br/>【负向约束】 不得出现第三只守宫或任何群众 / 克隆；两者体型与外形不得互相漂移或换脸；不得复制道具；无镜面倒影中的角色分身；无字幕、无画面文字、无文字叠层；仅硬切、无叠化；开场空镜段落不得出现角色对白；保持 "环境铺垫→提议→争执对抗→达成一致" 的情绪曲线，结尾必须落在两方一致、下定决心上；音轨层次固定为放大的环境底噪为主、背景音乐长时间铺底并在关键点加强、不覆盖对白。角色说英文（All characters speak English）。</code></pre></td></tr><tr><td vertical-align="middle"><b>双模态</b></td><td><b>图片 + 视频</b></td><td vertical-align="top"><grid><column width-ratio="0.500000"><figure view-type="Preview"><source name="6月14日(2).mov" mime="video/quicktime" origin-height="1080.000000" origin-width="1920.000000" size="22005744" token="[媒体标识已移除]"/></figure><p>               视频1</p></column><column width-ratio="0.500000"><img name="image.png" caption="图片1&#xA;" mime="image/png" scale="0.217969" src="WLVebLB37oqQcuxhL8GcnLPJnvd"/></column></grid></td><td vertical-align="top"><figure view-type="Preview"><source name="换耳机.mp4" mime="video/mp4" origin-height="1080.000000" origin-width="1920.000000" size="26850934" token="[媒体标识已移除]"/></figure></td><td><pre caption="Seedance 2.5&#xA;" lang="HTML" wrap="true"><code>参考 @视频1 的运镜方式与剪辑节奏，生成一条<b>耳机@图片</b>的广告短片。适配符合产品调性的场景，强调现代、简洁、科技感。产品特写与场景全景的切换点与原片一致，保持同样的运动速度与转场方式。 </code></pre></td></tr><tr><td vertical-align="middle"><b>三模态</b></td><td><b>图片 + 音频 + 视频 同时参考</b><blockquote><p>支持指定其中的参考图用作 首/尾帧 </p></blockquote></td><td><ul><li><b>参考图</b><grid><column width-ratio="0.200000"><img name="人物去水印.png" caption="图片1&#xA;" mime="image/png" scale="0.386243" src="FFjKbfMzKoHxEWxbCU8c5vB3n9e"/></column><column width-ratio="0.200000"><img name="tat_l-EWx3uJvjS9S6nxb.jpeg" caption="图片2&#xA;" mime="image/jpeg" scale="0.356445" src="BRZFbmkk6oOgaJx98bxcR5bunVf"/></column><column width-ratio="0.200000"><img name="风衣.png" caption="图片3&#xA;" mime="image/png" scale="0.386243" src="ZR6Tb4dSTotLNKxZoGEcTlMqn9e"/></column><column width-ratio="0.200000"><img name="喷火去水印.png" caption="图片4&#xA;" mime="image/png" scale="0.386243" src="WxWqbQ3PJoG2asxMGPvcl7CInRh"/></column><column width-ratio="0.200000"><img name="肉铺去水印.png" caption="图片5&#xA;" mime="image/png" scale="0.386243" src="EygIbzFAgoSuWQxVNYBcjrDunGf"/></column></grid><grid><column width-ratio="0.250000"><img name="抱孩子去水印.png" caption="图片6&#xA;" mime="image/png" scale="0.386243" src="AueXb1JUqonfRfxyKNKcinednnd"/></column><column width-ratio="0.250000"><img name="reference10.png" caption="图片7&#xA;" mime="image/png" scale="0.386243" src="LDhubYpeYoIqaQx7cJ4c2DNcnpd"/></column><column width-ratio="0.250000"><img name="秋天去水印.png" caption="图片8&#xA;" mime="image/png" scale="0.386243" src="LP9ubVtwSoYkNZxnnEUc4KqKnyc"/></column><column width-ratio="0.250000"><img name="hf_20260707_023326_aec0c183-3be3-4eb8-938e-2886e4b4342a.png" caption="图片9&#xA;" mime="image/png" scale="0.356445" src="A0JMbZZkaoKTG4xOQA2cu054nrh"/></column></grid><grid><column width-ratio="0.250000"><img name="冬天去水印.png" caption="图片10&#xA;" mime="image/png" scale="0.386243" src="QuwxbzNvBo820IxoG6ncMfWSnYg"/></column><column width-ratio="0.250000"><img name="S1FmOK_2L7WBsIMD6c5xp.png" caption="图片11&#xA;" mime="image/png" scale="0.356445" src="QS1Jbr7PEo9xq5xwKtGcYKzgn9b"/></column><column width-ratio="0.250000"><img name="夜晚去水印.png" caption="图片12&#xA;" mime="image/png" scale="0.386243" src="KTuxbEw9qoOCTPxmpJxc7iEsnBh"/></column><column width-ratio="0.250000"><img name="烟花去水印.png" caption="图片13&#xA;" mime="image/png" scale="0.386243" src="N4yqbYos8olyHMx3xwncSC5snlf"/></column></grid></li><li><b>参考视频</b></li></ul><grid><column width-ratio="0.333333"><p>长镜头街头跟拍</p><figure view-type="Preview"><source name="02178105855767500000000000000000000ffffac191c1f3076ee.mp4" mime="video/mp4" origin-height="1080.000000" origin-width="1920.000000" size="5454387" token="[媒体标识已移除]"/></figure></column><column width-ratio="0.333333"><p>跟随环绕镜头</p><figure view-type="Preview"><source name="环绕镜头.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="4247094" token="[媒体标识已移除]"/></figure></column><column width-ratio="0.333333"><p>市集纪实参考</p><figure view-type="Preview"><source name="市井.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="4480566" token="[媒体标识已移除]"/></figure></column></grid><ul><li><b>参考音频</b></li></ul><figure view-type="Preview"><source name="烟花声音.MP3" mime="audio/mpeg" size="81552" token="[媒体标识已移除]"/></figure></td><td><figure view-type="Preview"><source name="走路.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="30031878" token="[媒体标识已移除]"/></figure></td><td><pre caption="中文提示词&#xA;" lang="Plain Text" wrap="true"><code>核心指令： 全程 26 秒一镜到底（One-Shot）叙事短片，稳定跟拍，参考【视频1】与平滑环绕运镜，参考【视频2】交织。平滑行进感。镜头内实现昼夜交替与四季流转。主角是一位欧洲女人【图片1】，置身充满烟火气的人海，凸显极致的孤独感与电影摄影质感。<br/>分段运镜与场景描述：<br/>0-3 秒（平稳背跟）： 老旧木门【图片2】“吱呀”推开，镜头紧随欧洲女人穿着【图片3】的背影步出。他在门槛处微停，前方街巷光影斑驳，叫卖与人潮声扑面而来。她神情疏离，缓缓迈步融入街道。<br/>3-6 秒（背侧方跟拍）： 镜头保持平滑跟进，她步入拥挤的早市，氛围参考【视频3】。两侧挤满色泽浓郁的水果摊与香料铺，一队街头杂耍艺人正喷吐火龙，参考【图片4】，火光照亮人群，但她目不斜视，步伐匀速穿过。<br/>6-9 秒（侧面平滑环绕）： 镜头开始向侧前方平滑环绕，捕捉主角的侧脸。她走过喧闹的肉铺【图片5】，一位年轻母亲抱着婴儿【图片6】与他擦肩，婴儿好奇地紧盯她，她却只是微微垂下眼眸避开视线，没有丝毫停留。<br/>9-12 秒（正前方倒退跟拍）： 镜头继续绕至主角正前方，进行倒退跟拍。前方人群突然如摩西分海般自然退至两侧，一只披着华丽红布的巨大大象【图片7】迈着沉稳的步伐，从画面右侧出现，占据了大半个画面。<br/>12-15 秒（缝隙穿透与绕回）： 女人与大象即将相撞的瞬间，镜头巧妙地贴着大象与女人之间的狭窄缝隙滑过，重新绕回她的背影。大象庞大而安静地掠过，顽童们欢呼追逐。象铃声、笑声鼎沸，她却连脚步都未曾放缓。<br/>15-18 秒（环境光影渐变）： 伴随她的行走，长镜头内的光影奇幻变幻——盛夏的刺眼阳光瞬间柔和，一阵微风卷起漫天金黄的落叶【图片8】，季节在同一个长镜头中无缝过渡至深秋。落叶拂过她的肩膀。<br/>18-21 秒（360度沉浸环绕）： 前方骤然陷入一场盛大的街头庆典【图片9】。空中喷吐出漫天彩带与碎纸，摊贩探出身子欢呼。镜头在此刻展开一段连贯的 360 度环绕运镜，将安静孤寂的主角与狂热的周遭形成极其强烈的视觉撕裂。<br/>21-24 秒（绕回侧后方）： 当镜头环绕一周结束回到她侧后方时，飘落的彩带已悄然化作漫天飞雪——瞬间入冬【图片10】。行人们纷纷撑起伞或戴上兜帽，女人微微瑟缩，竖起大衣衣领，服装变成【图片11】，在雪地中继续孤身前行。<br/>24-26 秒（慢推跟拍）： 随着她走向长街尽头，天色在行进中以肉眼可见的速度暗下，白昼无缝沉入黑夜。两侧昏黄的路灯与小摊的灯泡次第亮起【图片12】，小贩收拾货物，喧闹声仿佛被大雪慢慢吸收、拉远，她的脚步逐渐放缓。夜空骤然绽放盛大的烟花【图片13】，烟花绽放声音参考【音频1】五彩光斑在楼墙与她的眼眸中闪烁跳跃。世界热闹依旧，而她安静仰望，镜头缓缓拉远，在此温柔收束。</code></pre></td></tr></tbody></table>



## 2.3｜合理的参考素材配比，有效提升创作质量

尽管 2.5 支持上传 50 个参考素材，但在实际创作中，**合理的素材配比** 能够有效提升 生成稳定性与成片效果。经大量评测验证：



- 若主体参考素材为**音视频，建议** **主体素材 ≤ 5 个** ，如创作需要， **可尝试上传 6～10 个主体**

  - **同时，视频 & 音频 单段素材建议控制在 5～10 秒，是识别度与稳定性的最佳区间**过短（如 2s）因信息量不足、特征不完整，难以被稳定识别与参考；过长（如 30s）则易导致关键特征被稀释、噪声增多
- 若为**主体图**，**建议** **主体素材 ≤ 8 个** ，如创作需要， **可尝试上传 9～12 个主体**

  - 当**主体图 ≤ 5**张，上传「单视图」「多视图」均可
  - **超过5主体** 时，「单视图」效果较稳定，如需输入多视角，建议拆分为多张不同视图输入,而非输入一张包含多视角的图
- 当素材偏多、担心超载时，按以下优先级取舍：**核心角色 ＞ 关键产品 / 道具 ＞ 场景环境 ＞ 整体风格**

<callout emoji="❓">
附 如何理解**「主体素材」**
主体，即画面里希望模型稳定还原、贯穿全片的「核心元素」，包括 **人物角色、关键产品/道具、场景环境、整体风格**等。
  
🌰 举例：
- **单主体 人物角色：**口播/人物宣传片里，模特或出镜人物即视频主体。一般只需上传模特的多视图（5 张内），如为多个模特（6-10 个），则上传各模特的单视图
- **多主体 人+道具+场景：**画面里同时有人物、道具、被作用的对象。比如“一个人在森林里拉弓射中一只兔子”，其中主人公（人）、弓箭（道具）、被射中的兔子（对象）都各算一个主体，都需要稳定还原
</callout>



## 2.4｜更准确可控的视频编辑

视频编辑与延长，本质上是 **R2V能力 的延伸，**把已有视频用 `@视频1` 作为原片喂入，通过 Prompt 控制局部编辑，模型即可在锁定原片其余画面 的前提下，完成局部改写或延长。

<callout emoji="📚">
**【重点关注】**
在使用**视频编辑/延长、首尾帧**能力时，模型会 **依据参考素材自动锁定部分生成参数，不支持自定义。** 
- **视频编辑：**

  - 输出视频的**画面比例会严格对齐原片**，不会因为改写内容而变形或裁切
  - **输出时长 基本对齐原片** (由于模型对输入的处理机制，时长可能出现轻微差异)，视频主体内容仍与原片保持完整、不变
- **视频延长**

  - 输出视频的**画面比例会严格对齐原片**，以确保延长片段与原片在同一画幅下自然衔接；
  - **延长片段的时长支持用户自定义**，可通过 Prompt 明确指定
- **首帧 / 首尾帧生视频**—— 当以 1 张图作为首帧（I2V），或以 2 张图分别作为首帧与尾帧生成视频时

  - 输出视频的**画面比例会对齐首帧图的画幅**
  - 如果尾帧与首帧画幅不一致，尾帧会被拉伸对齐，因此建议输入画幅一致的首尾帧，避免出现形变
  - **时长，支持用户自定义**
</callout>

<callout emoji="💡">
**视频编辑 写法三步**
① 用 `@视频1` 指入待编辑的原片
② 圈定要改动的对象与目标，替换主体可配 `@图片N` 提供参考形象，增删元素直接描述对象与位置（可选，也可用文字指令描述）
③ 限制提示词 “其余保持不变” 锁定未改动区域，避免模型连带改动
</callout>

<table><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th><b>能力点</b></th><th vertical-align="middle"><b>输入（原始视频&amp;更改内容）</b></th><th>输出（编辑后视频）</th><th vertical-align="middle">Prompt</th></tr></thead><tbody><tr><td><b>增加特效</b></td><td><figure view-type="Preview"><source name="火车输入.mov" mime="video/quicktime" origin-height="1080.000000" origin-width="1920.000000" size="14444680" token="[媒体标识已移除]"/></figure></td><td><figure view-type="Preview"><source name="火车出战.mov" mime="video/quicktime" origin-height="1080.000000" origin-width="1920.000000" size="18597558" token="[媒体标识已移除]"/></figure></td><td><pre caption="Seedance 2.5&#xA;" lang="Plain Text" wrap="true"><code>风格： 超真实电影感写实风格，照片级真实的实拍影像质感，强调冲出实体（蒸汽火车）的现实可信度；不要 CGI 光泽感，不要游戏引擎感，不要风格化 3D 外观。金属、蒸汽、木质与烟尘的细节要细腻真实，能对环境光做出可信的反应。严格遵循真实物理规律：有重量、有摩擦、有惯性、有接触阴影、有物体受压反馈，不能漂浮，不能卡通化夸张。保留【@视频1】原本的构图、放映厅光线、手持镜头状态和自然瑕疵感。<br/>原视频锁定： 将【@视频1】完整保留为基础画面。老式放映厅、成排背对镜头戴帽的观众、放映机投出的锥形光束、银幕位置、周围物体、环境光、反射、整体色调、手持镜头运动都保持不变。不要修改节奏、画幅、镜头特性、运动轨迹或调色。唯一新增的内容是：从银幕里冲出的实体（火车）、它带来的光影变化、银幕的破裂、以及冲击对放映厅空间与前排观众区域的轻微物理影响。<br/><b>画面转色规则（核心新增）：</b> 影片开始时严格保持【@视频1】原本的<b>黑白老电影质感</b>（颗粒、划痕、闪烁、单色调）。当火车车头<b>真正突破银幕、冲入现实空间的那一瞬间</b>，画面<b>从黑白骤然转为饱满真实的彩色</b>—— 转色以火车冲出点为中心、如冲击波般向整个画面扩散，火车的黑色钢铁车身、红铜色锅炉光泽、橙黄的蒸汽灯火、木质车厢的暖棕、白灰色蒸汽与放映厅的暖褐色调随之显色。转色干脆有力、与破幕的爆发瞬间精确同步；转色后维持照片级真实彩色直到结束。银幕上尚未冲出的残余投影区域可仍带一点黑白电影残影，强化 "从旧影像撕裂进现实" 的对比。<br/><b>银幕破裂锁定（核心新增）：</b> 银幕表现为一块真实存在、有织物张力的白色投影幕布，而非普通平面。火车冲出时，幕布沿车头轮廓<b>被强行撕裂、爆开</b>—— 布面出现放射状裂口、边缘翻卷撕扯、碎布与纤维向外飞扬、幕布残片剧烈摆荡，破口处透出后方结构。破裂的张力感、撕扯方向与火车冲出的力量和方向一致，全程保留清晰可见的 "荧幕被撞破" 的破裂感。<br/>主体： 一列老式蒸汽火车车头正从银幕中强行冲出。黑色钢铁车身、圆筒锅炉、前置排障器、冒着白灰色蒸汽的烟囱、明亮的车头灯，金属表面有真实的磨损、油污、铆钉与湿润反光。它带着巨大的重量与惯性向前冲，符合可信的机械结构与真实火车的体量感。<br/>场景： 完全沿用【@视频1】的现实放映厅环境。银幕表现为一层真实的、有厚度与阻力的投影幕布，在火车冲出时被撕裂、翻卷、飞散，并在银幕与放映厅空间的边界处产生明显的破裂张力、蒸汽扩散与光线扭曲。<br/>动作： 一列蒸汽火车从老电影银幕中突破，冲进现实的放映厅空间。<br/>镜头要求： 完全继承【@视频1】原本的手持运动。不要平滑，不要重定时，不要重新构图。冲出的火车必须始终正确锁定在银幕与放映厅空间中，随着镜头移动保持正确视差和遮挡关系。任何进入放映厅前方空间的车体，都必须产生贴地阴影与合理的接触压迫感。<br/>视觉基调： 以真实性为第一优先。转色前忠实呈现黑白老电影质感（颗粒、闪烁、划痕）；破幕瞬间干脆转为真实彩色。放映厅原有的暖色实景光仍是主光源，放映机光束与车头灯作为强光源。金属与蒸汽表面应自然同时接收环境暖光与投影冷光。重点表现可信的阴影过渡、反射、蒸汽扩散、飞散碎布，以及与周围材质之间的细微互动。<br/>声音： 不要音乐。只保留真实现场音效。继承【@视频1】原本的放映厅环境音（放映机哒哒声、观众轻微骚动），并新增幕布被撕裂爆开的布料撕扯声、蒸汽喷涌声、钢铁车轮与机械轰鸣声、冲击气浪声。整体听感必须近距离、物理化、可信。<br/>总时长与【@视频1】完全一致。基础视频画面在转色前不得改变，除火车本身、其物理互动、银幕破裂与破幕瞬间的转色外不新增其他内容。银幕必须表现为具有厚度和阻力的真实幕布入口并被真实撕裂，而不是简单贴图或叠加特效。转色必须与破幕瞬间精确同步、干脆有力。不要慢动作，不要魔法感，不要风格化恐怖设计，不要过度夸张。最终效果应像是在一个老式放映厅里，被真实相机偶然拍到的一段极其诡异又异常真实的 "火车撞破银幕、黑白瞬间转为彩色" 的画面。</code></pre></td></tr><tr><td vertical-align="middle"><b>替换场景、人物服装</b></td><td vertical-align="middle"><grid><column width-ratio="0.500000"><img name="reference2.png" caption="图片 1&#xA;" mime="image/png" scale="0.356445" src="DoDXbFDxQo4pPIxlikCc2P7Rn7c"/></column><column width-ratio="0.500000"><img name="reference4.png" caption=" 图片 2&#xA;" mime="image/png" scale="0.356445" src="MUDCbrgtSoDt0lxHkSscA2WEnsC"/></column></grid><grid><column width-ratio="0.422414"><img name="reference3.png" caption=" 图片 3&#xA;" mime="image/png" scale="0.356445" src="U1HIb6IRqoTYB6x3UK1cstAGnnb"/></column><column width-ratio="0.577586"><figure view-type="Preview"><source name="reference1.mp4" mime="video/mp4" origin-height="1248.000000" origin-width="1664.000000" size="7391502" token="[媒体标识已移除]"/></figure><p>                   视频 1</p></column></grid></td><td vertical-align="middle"><figure view-type="Preview"><source name="output.mp4" mime="video/mp4" origin-height="834.000000" origin-width="1112.000000" size="4163093" token="[媒体标识已移除]"/></figure></td><td vertical-align="middle"><pre caption="Seedance 2.5&#xA;" lang="HTML" wrap="true"><code>将两人武打素版视频 @视频1 替换为冷兵器对决前的空手试探风。<br/>场景替换为中世纪石堡平台、古老庭院平地、山间堡垒外平台或简洁石砖决斗场，背景为古堡墙体、风、雾、远处山线，地面平整石质 @图片1 。<br/>视频中深色衣服的男子的服饰替换为 @图片2 ，视频中浅色衣服的男子替换为 @图片3。动作仍然保持不变，不改变原始节奏。<br/>AI 特效仅做环境和质感强化：风吹衣摆、轻雾、接触点少量尘土、金属冷色反光质感、轻微颗粒和史诗感调色。整体风格为克制、真实、古典硬派决斗氛围。背景音乐卡点</code></pre></td></tr><tr><td vertical-align="middle"><b>删除主体（影视bug）</b></td><td vertical-align="middle"><figure view-type="Preview"><source name="o4uBXJ6ftNO1iASxEZPoezaBgio7CWQGBgJ4E2_a=0&amp;ch=0&amp;cr=0&amp;dr=0&amp;er=0&amp;lr=default&amp;&amp;br=11608&amp;bt=11608&amp;cs=0&amp;ds=4&amp;mime_type=video_mp4&amp;qs=13&amp;rc=M3Qza2s5cnd2PDczNGllM0BpM3Qza2s5cnd2PDczNGllM0BoZmgtMmRjbTNhLS1kXy9zYSNoZmgtMmRjbTNhLS1kXy9zcw%3D%3D&amp;cqu (1).mp4" mime="video/mp4" origin-height="1080.000000" origin-width="1920.000000" size="25013515" token="[媒体标识已移除]"/></figure></td><td vertical-align="middle"><figure view-type="Preview"><source name="教堂编辑后.mov" mime="video/quicktime" origin-height="1080.000000" origin-width="1920.000000" size="23705831" token="[媒体标识已移除]"/></figure></td><td vertical-align="middle"><pre caption="Seedance 2.5&#xA;" lang="Python" wrap="true"><code>视频编辑：删除 @视频1 中的所有人，除了主角。</code></pre></td></tr></tbody></table>



# 三、生成效果提升

除了客观的能力参数升级， 2.5 在生成效果上巨大跃迁，在美感和叙事可信度上，均大幅接近真实拍摄水准。



## 3.1｜光 Lighting

光线的理解与生成上，Seedance2.0已经可以生成符合光照逻辑、皮肤质感真实的画面。而Seedance2.5 表现的更加出色，光源方向高度统一，光线的衰减（Light off）非常的细腻、自然，符合真实拍摄的特点。

<table><colgroup><col/><col/></colgroup><thead><tr><th vertical-align="top">Seedance 2.0</th><th vertical-align="top">Seedance 2.5</th></tr></thead><tbody><tr><td vertical-align="top"><figure view-type="Preview"><source name="02178445720013400000000000000000000ffffac181a9149e6c6.mp4" mime="video/mp4" size="8174040" token="[媒体标识已移除]"/></figure></td><td vertical-align="top"><figure view-type="Preview"><source name="a9f4bca0c34b45f7aa5f2ff79b238ab9_a=0&amp;ch=0&amp;cr=0&amp;dr=0&amp;er=0&amp;lr=default&amp;&amp;br=7850&amp;bt=7850&amp;cs=0&amp;ds=3&amp;mime_type=video_mp4&amp;qs=13&amp;rc=ajo2ZWRvOjlkPDczNGllM0Bpajo2ZWRvOjlkPDczNGllM0Bib2Q2YWFmZWJhLS1kXy9zYSNib2Q2YWFmZWJhLS1kXy9zcw%3D%3D&amp;cquery=102y&amp;dy_.mp4" mime="video/mp4" size="10090604" token="[媒体标识已移除]"/></figure></td></tr><tr><td colspan="2"><blockquote><p>侧向光源下，2.5 的关键光方向高度统一，光线衰减细腻自然；细看人物两只眼球，左右眼接收到的光线强弱不同，虹膜与瞳孔的明暗差异被真实还原。从宏观的打光逻辑，到微观的眼神光，Seedance 2.5 都在向真实拍摄的质感靠近。</p></blockquote></td></tr></tbody></table>

<table><colgroup><col/><col/><col/></colgroup><thead><tr><th><ul><li>牧羊女孩（侧逆光）</li></ul></th><th vertical-align="top"><ul><li>车窗流动光（真实性）</li></ul></th><th vertical-align="top"><ul><li>车站告别（眼神光）</li></ul></th></tr></thead><tbody><tr><td><figure view-type="Preview"><source name="2.1.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="17316078" token="[媒体标识已移除]"/></figure></td><td vertical-align="top"><figure view-type="Preview"><source name="3B 叮叮车窗光-V2-V2.5-2.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="4672915" token="[媒体标识已移除]"/></figure></td><td vertical-align="top"><figure view-type="Preview"><source name="3A 眼神光大特写-V3-V2.5.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="27772885" token="[媒体标识已移除]"/></figure></td></tr><tr><td><blockquote><p>暖金色低角度侧逆光下，女孩抬头的瞬间，额前发丝呈半透明漫反射，面部轮廓在光的照射下明暗交界过渡细腻。转头时，眼球表面浮起清晰的眼神光，面部受光侧与背光侧对比鲜明，暗部细节真实保留。</p></blockquote></td><td><blockquote><p>随着电车行进，车窗外的光影不断扫过女孩的侧脸，明暗过渡自然、贴合车厢环境，不会跳脱成漂浮的光斑。真实的流动光让画面更像实拍，光照的物理逻辑经得起推敲。</p></blockquote></td><td><blockquote><p>暖调站台光落在人物脸上，眼睛里的高光与湿润感清晰自然，眼神里的情绪也被这点眼神光烘托得更立体，人物更显真实、有神采。</p></blockquote></td></tr></tbody></table>



## 3.2｜镜头运动 Camera movement

2.5 的**镜头运动**控制精度大幅提升，推拉摇移等经典运镜手法的轨迹更加丝滑稳定，复杂的组合运镜（如跟随 + 升降 + 旋转）也能平稳执行，避免出现抖动、跳帧或轨迹漂移的问题。

<table><colgroup><col/><col/><col/></colgroup><thead><tr><th><ul><li>平原探险</li></ul></th><th vertical-align="top"><ul><li>个人独舞</li></ul></th><th><ul><li>长镜头运动员入场</li></ul></th></tr></thead><tbody><tr><td><figure view-type="Preview"><source name="飞书20260713-145653.mp4" mime="video/mp4" size="6903730" token="[媒体标识已移除]"/></figure></td><td vertical-align="top"><figure view-type="Preview"><source name="11accb0b5a8a44cb81af2ec84ea06b33_a=0&amp;ch=0&amp;cr=0&amp;dr=0&amp;er=0&amp;lr=default&amp;&amp;br=26741&amp;bt=26741&amp;cs=0&amp;ds=3&amp;mime_type=video_mp4&amp;qs=13&amp;rc=M3FrOjRrbzc1PDczNGllM0BpM3FrOjRrbzc1PDczNGllM0A2ZGFjcWcvXjJhLS1kXy9zYSM2ZGFjcWcvXjJhLS1kXy9zcw%3D%3D&amp;cquery=102y&amp;d.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="102859220" token="[媒体标识已移除]"/></figure></td><td><figure view-type="Preview"><source name="9e263017277a43ca963cafa773f6d6e4_a=0&amp;ch=0&amp;cr=0&amp;dr=0&amp;er=0&amp;lr=default&amp;&amp;br=24775&amp;bt=24775&amp;cs=0&amp;ds=3&amp;mime_type=video_mp4&amp;qs=13&amp;rc=M3I2bjVrbzg0PDczNGllM0BpM3I2bjVrbzg0PDczNGllM0A1XzZtcWdmYzRhLS1kXzBzYSM1XzZtcWdmYzRhLS1kXzBzcw%3D%3D&amp;cquery=102y&amp;d.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="54042574" token="[媒体标识已移除]"/></figure></td></tr><tr><td><blockquote><p>开场焦距从虚到实，摄影机运动缓慢、克制；当人物察觉异样缓缓抬头时，镜头不抢戏、先等人物抬头再上摇；陨石掠过瞬间，镜头从平稳切换为轻微手持晃动，带来沉浸的现场感；陨石划过后又迅速回归克制。</p></blockquote></td><td><blockquote><p>镜头跟随独舞者移动，推拉摇移的轨迹丝滑稳定，30 秒长镜头里没有明显抖动或跳帧，运镜节奏服务于表演，画面连贯耐看。</p></blockquote></td><td><blockquote><p>一镜到底跟随运动员穿过通道入场，跟随、升降、旋转等复杂组合运镜衔接平稳，空间关系始终清晰不错乱，长镜头的调度可控性更强。</p></blockquote></td></tr></tbody></table>



## 3.3｜表演 Expression

模型能够更准确地把握角色在叙事中的位置和情绪走向，**剧情理解**能力显著增强；在**执行层面**，角色的**情绪**演绎更加**细腻**，**微表情**的呈现（如眼角的颤动、嘴唇的轻抿）更加完整。

<table><colgroup><col/><col/></colgroup><thead><tr><th>Prompt</th><th vertical-align="top">Seedance 2.5 </th></tr></thead><tbody><tr><td><pre caption="&#xA;" lang="HTML" wrap="true"><code>剧场观众席，一名年轻女孩双手交叠贴近下巴，凝望台上的表演。她的情绪复杂而混合，眼里有骄傲、有心疼、有隐忍的泪光，嘴唇轻抿，睫毛颤动，泪水在眼眶打转却强忍不落。核心呈现看着最亲的人发光时那种五味杂陈的真实情绪。</code></pre></td><td vertical-align="top"><figure view-type="Preview"><source name="看表演复杂情绪2.5.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="5702481" token="[媒体标识已移除]"/></figure><blockquote><p>2.5 对这类复杂情绪的把握更到位，眼里的骄傲、心疼与泪光层次更分明，泪水打转却强忍不落的分寸也拿捏得更自然，整体情绪更连贯。</p></blockquote></td></tr><tr><td><pre caption="Prompt&#xA;" lang="Plain Text" wrap="true"><code>A young East Asian woman sits by a study window at dusk, facing a laptop, warm golden side/back light on her face. Her performance is deeply restrained, with emotion conveyed through her eyes, shallow breathing, a choked throat, and trembling fingertips. She moves from disbelief to tearful suspension; as one tear falls, a faint smile appears, ending in quiet relief as she looks outside. Slow, steady camera movement, close-ups for micro-expressions, a slight push-in at the moment the tear gives way to a smile, soft focus on " Acceptance Letter," 35mm film texture, shallow depth of field, low-light grain.</code></pre></td><td><figure view-type="Preview"><source name="e40a2950-3468-4764-b6f8-1ed8998f9bfd.mp4" mime="video/mp4" size="5400212" token="[媒体标识已移除]"/></figure><blockquote><p>从紧张期待→确认被录取的凝滞悬停→泪笑交叠→释然，几秒内完成三层递进。仅需一段自然语言描述，Seedance 2.5 就能读懂角色内心的五味杂陈，并将复杂情绪有层次地呈现出来。</p></blockquote></td></tr></tbody></table>





## 3.4｜感染力 Emotional impact

Seedance 2.5 在画面真实感上实现了显著跃升。人物的皮肤质地、毛发光泽、面部微动等细节更趋近真实世界的观感；画面整体的**镜头感染力**也同步提升，情绪化场景的氛围渲染更具沉浸感，更好地调动观众的情绪共鸣。

<table><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th><ul><li>恐龙破屏 // 实拍级真实感</li></ul></th><th><ul><li>虚拟乐队演出</li></ul></th><th><ul><li>鲨鱼破窗</li></ul></th><th vertical-align="top"><ul><li>香水广告</li></ul></th></tr></thead><tbody><tr><td><figure view-type="Preview"><source name="ccc1097637914533807445fc4ead1987_a=0&amp;ch=0&amp;cr=0&amp;dr=0&amp;er=0&amp;lr=default&amp;&amp;br=9248&amp;bt=9248&amp;cs=0&amp;ds=3&amp;mime_type=video_mp4&amp;qs=13&amp;rc=M3J2NTVvOng6PDczNGllM0BpM3J2NTVvOng6PDczNGllM0AuX3FfYWFmMWBhLS1kXzBzYSMuX3FfYWFmMWBhLS1kXzBzcw%3D%3D&amp;cquery=102y&amp;dy_.mp4" mime="video/mp4" size="17807455" token="[媒体标识已移除]"/></figure></td><td><figure view-type="Preview"><source name="乐队mv修改.mp4" mime="video/mp4" origin-height="1080.000000" origin-width="1920.000000" size="108562837" token="[媒体标识已移除]"/></figure></td><td><figure view-type="Preview"><source name="0761951e-70a4-4a76-90e5-1090ecd07993.mp4" mime="video/mp4" origin-height="1080.000000" origin-width="1920.000000" size="6856721" token="[媒体标识已移除]"/></figure></td><td vertical-align="top"><figure view-type="Preview"><source name="香水广告-成品7.7.mp4" mime="video/mp4" origin-height="1080.000000" origin-width="1920.000000" size="38395425" token="[媒体标识已移除]"/></figure></td></tr><tr><td><blockquote><p>破屏裂纹的走向、光线从缝隙中溢出的层次，AI 感被大幅削弱。</p></blockquote></td><td><blockquote><p>自拍视角下，人物的皮肤质感、发丝光泽与手部动作都真实自然，30 秒内演出状态始终稳定不漂移，几乎看不出 AI 痕迹；真人感十足，接近真实拍下的现场。</p></blockquote></td><td><blockquote><p>鲨鱼破窗而出的瞬间，玻璃碎裂、水流飞溅与鲨鱼的材质细节都遵循真实物理，冲击力可信。即便是这样天马行空的超现实场景，模型也能做到「假得逼真」</p></blockquote></td><td><blockquote><p>暖调低光下，人物的皮肤、发丝与面部微动细腻真实，光影氛围高级而克制。镜头的情绪渲染极具感染力，安静的画面里透出沉浸的高级质感。</p></blockquote></td></tr></tbody></table>



# 四、应用场景



## 🔑  更强的模型，解锁更多的创作新可能

<table><colgroup><col/><col/><col/><col/><col/></colgroup><thead><tr><th vertical-align="middle">场景 \ 能力</th><th vertical-align="middle">30s 30 秒直出</th><th vertical-align="middle">全模态参考</th><th vertical-align="middle">视频编辑</th><th vertical-align="middle">多语种</th></tr></thead><tbody><tr><td vertical-align="middle"><b>影视创作</b></td><td vertical-align="middle"><ul><li>30s 直出完整剧情段落</li><li>长镜头表演连贯不断层</li><li>复杂情节一镜到底</li><li>……</li></ul></td><td vertical-align="middle"><ul><li>投喂多位演员资产演群像戏</li><li>3D 白模分镜预演</li><li>真人 × IP 角色融合</li><li>……</li></ul></td><td vertical-align="middle"><ul><li>替换演员 / 道具服装</li><li>修穿帮 bug(威亚 / 器材)</li><li>改微表情与年龄(25→60 岁)</li><li>换画风(赛璐璐 / 水墨 / 黑白)</li><li>影片光源重布</li><li>……</li></ul></td><td vertical-align="middle"><ul><li>一条母版出多语言配音版</li><li>口型随语种对齐</li><li>……</li></ul></td></tr><tr><td vertical-align="middle"><b>广告电商</b></td><td vertical-align="middle"><ul><li>TVC / 品牌故事片一镜叙事</li><li>短剧式带货连续演绎</li><li>……</li></ul></td><td vertical-align="middle"><ul><li>锁定商品外观与品牌 VI</li><li>商品多场景演绎</li><li>保持模特形象一致</li><li>……</li></ul></td><td vertical-align="middle"><ul><li>替换 SKU / 模特 / 人种</li><li>改写价签 / 文案 / 角标</li><li>出海本地化改片</li><li>一片多渠道版本化</li><li>……</li></ul></td><td vertical-align="middle"><ul><li>多语种带货口播</li><li>出海市场本地化配音</li><li>……</li></ul></td></tr><tr><td vertical-align="middle"><b>知识科普</b></td><td vertical-align="middle"><ul><li>30s 讲清一个知识点</li><li>历史 / 文化情景重现</li><li>……</li></ul></td><td vertical-align="middle"><ul><li>结构拆解 / 原理还原</li><li>科学原理可视化</li><li>知识 IP 形象统一</li><li>……</li></ul></td><td vertical-align="middle"><ul><li>风格化课程片头 / 转场</li><li>替换讲解人物</li><li>微调实验步骤演示</li><li>……</li></ul></td><td vertical-align="middle"><ul><li>一套内容多语种分发</li><li>多语言口播讲解</li><li>……</li></ul></td></tr><tr><td vertical-align="middle"><b>工业制造</b></td><td vertical-align="middle"><ul><li>完整演示装配 / 操作流程</li><li>设备维护指引长视频</li><li>……</li></ul></td><td vertical-align="middle"><ul><li>3D 资产产品预演</li><li>产线 SOP 标准化</li><li>多型号产品统一呈现</li><li>……</li></ul></td><td vertical-align="middle"><ul><li>产品多型号批量出片</li><li>替换铭牌 / 规格信息</li><li>改写包装信息</li><li>……</li></ul></td><td vertical-align="middle"><ul><li>多语种安全培训片</li><li>视频说明书多语版</li><li>……</li></ul></td></tr><tr><td vertical-align="middle"><b>多元场景</b></td><td vertical-align="middle"><ul><li>游戏 CG / 预告片长叙事</li><li>短片扩展为系列番剧</li><li>……</li></ul></td><td vertical-align="middle"><ul><li>虚拟偶像 / 数字人表演</li><li>投喂角色集 / 场景集</li><li>真人 × IP 联动</li><li>……</li></ul></td><td vertical-align="middle"><ul><li>改角色年龄 / 表情演绎</li><li>风格化二创</li><li>活动 / 节日限定皮肤片</li><li>……</li></ul></td><td vertical-align="middle"><ul><li>多语种虚拟主播</li><li>互动剧多分支多语配音</li><li>……</li></ul></td></tr></tbody></table>



##  4.1 ｜影视创作 🎬



### 无对白叙事 // 30s 直出

> 从写信、出门、穿过向日葵田到寄信，镜头在室内浅景深、门廊光影转换和金色山谷全景之间连续切换，画面调性与情绪走向从头到尾保持一致。

<table><colgroup><col/><col/></colgroup><thead><tr><th>Prompt</th><th>Seedance 2.5 生成结果</th></tr></thead><tbody><tr><td><pre caption="Prompt&#xA;" lang="Plain Text" wrap="true"><code>一段30秒的无字视觉故事，带着法国乡村的静谧优雅，发生在普罗旺斯某个夏日午后。一位年轻女子身着米白色亚麻连衣裙，在石砌小屋内一张老木桌旁写完一封手写信，随后走出门外，沿着碎石小径穿过向日葵花田，来到村庄边缘一个复古黄色邮箱前，轻轻将信塞入其中。镜头从室内桌面的浅景深特写开始，穿过门廊——光线渐渐让位于阴影——最终上升拉开，呈现出金色山谷的全景宽画面。全程只有环境音——蝉鸣、风声、笔触纸面的沙沙声，以及邮箱轻轻合上的咔哒声——像是寄出一封远方书信后，久久停留的那一片寂静。</code></pre></td><td><figure view-type="Preview"><source name="一封信1.mp4" mime="video/mp4" size="99013900" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>



### 概念短片  // 30s 直出 + 全模态参考

> 单段 30s 内串联梦境般的多重场景，镜头连续流转。而氛围、光感与叙事基调始终统一，适合 MV、概念片等强视觉表达。

<table><colgroup><col/><col/><col/></colgroup><thead><tr><th>Prompt</th><th>参考素材</th><th>Seedance 2.5 生成结果</th></tr></thead><tbody><tr><td><pre caption="Prompt&#xA;" lang="Plain Text" wrap="true"><code>电影级品牌概念短片。@<b>图片1</b>为首帧，画面微微晃动，镜头逐渐推近，来到窗外快速后退的树影，树影后退速度越来愈快，突然切到@<b>图片2</b>，速度突然放缓，镜头顺着溪流缓缓前进，鸟语花香。<br/>镜头下移，来到水下，音效有水中气泡的声音，一群橙色的水母从镜头前优美地游过@<b>图片3</b>，镜头缓缓后拉，有一群小鱼晃过镜头后从水里穿到窗内@<b>图片4</b>，少女左看右看，在观赏小鱼<br/>镜头缓缓后拉，画面虚焦，随后又重新对焦画面变清晰，跟随音乐节奏切换：中式园林花窗@<b>图片5</b>光线转圈、教堂玻璃彩窗、飞机舷窗、穹顶天窗、飘窗、百叶窗、欧洲老虎窗、门上猫眼、相机取景框、鸟类眼睛、人类眼睛特写。<br/>画面停留在人类眼睛特写，随后眼睛闭上，画面黑屏，再突然一睁眼，眼睛中央出现“seedance”带重音。</code></pre></td><td><grid><column width-ratio="0.499857"><img name="关键帧1.png" alt="这张图片是一份带金属边框的舷窗式窗户，嵌在深色的内部空间上，透过窗户可以看到模糊的树林影像，画面呈现出动态模糊效果，该树林素材对应企业级业务场景实践指南中“无对白叙事//30s直出”影视创作板块的参考素材。这份指南是关于Doubao-Seedance 2.5的企业级业务场景实践内容，其中“无对白叙事//30s直出”板块提供了影视创作的Prompt、参考素材及对应模型生成结果，此图片便是该板块中的参考素材，契合无对白叙事的创作主题，通过动态模糊的树林视觉效果，为相关影视创作提供参考样本。" caption="&#xA;" mime="image/png" scale="0.520685" src="SCJobdAUIoe0CnxvyTEclVlXn8e"/></column><column width-ratio="0.500143"><img name="花去水.png" alt="图片展示了一幅森林场景，阳光透过树叶洒下斑驳光影。画面中，水面漂浮着粉色花瓣，周围环绕着茂密的绿色植被，点缀着红色、粉色等花朵。左侧有一朵橙色的花，画面整体色彩丰富，光影交错，营造出一种梦幻般的氛围。该图片与文档中“影视创作”应用场景下“无对白叙事//30s直出”内容相关，作为参考素材，用于展示Doubao-Seedance-2.5在无对白叙事场景下的生成效果。" mime="image/png" scale="0.386243" src="WhAVbHX4TouQC4x4sPQcSCyJnhc"/></column></grid><grid><column width-ratio="0.500000"><img name="水母水.png" alt="图片展示的是Doubao-Seedance 2.5在影视创作中无对白叙事场景下的30s直出生成结果。画面中，多个色彩斑斓的水母在深蓝色的海底环境中游动，水母主体呈透明或浅黄色，边缘带有红色或橙色的光晕，触须细长且透明。背景中隐约可见水下建筑结构，周围还有其他生物。该图片与上下文紧密相关，直观呈现了Doubao-Seedance 2.5在无对白叙事场景下的生成效果。" mime="image/png" scale="0.386243" src="TlUgbdVKMoNuyHxegaScdfGMn8c"/></column><column width-ratio="0.500000"><img name="舷窗去水.png" alt="图片展示了一位坐在圆形窗前的女性，窗外是海底世界。女性身着深色服装，侧身面向窗外，双手合十，似乎在祈祷或沉思。窗外的海底场景中，有岩石、珊瑚和成群的鱼类，阳光从水面洒下，营造出一种神秘而宁静的氛围。该图片与文档中“无对白叙事//30s直出”应用场景相关，可能是用于生成30秒无对白叙事视频的参考素材。" mime="image/png" scale="0.386243" src="VpaAbSTr5oMhLnxGZdIcVvupnTg"/></column></grid><img name="花窗去水.png" alt="图片展示的是影视创作中无对白叙事的30s直出场景。画面中，室内光线昏暗，墙壁斑驳，有一扇八角形的窗，窗格上有精美的图案。窗前摆放着一盆盛开的红色花朵，旁边是木质的桌子和椅子。阳光从窗外斜射进来，形成一道道光束，营造出一种静谧而神秘的氛围。该图片与上下文对应，直观呈现了无对白叙事场景中室内环境的视觉效果。" mime="image/png" scale="0.386243" src="Upefblg4Ao6AKpx0EGYcBjxinNm"/></td><td><figure view-type="Preview"><source name="窗外-4k.mov" mime="video/quicktime" origin-height="1080.000000" origin-width="1920.000000" size="44714691" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>



### 多角色群像戏   // 全模态参考

> 多名演员与环境设定并稳定保持

<table><colgroup><col/><col/></colgroup><thead><tr><th>Prompt</th><th>Seedance 2.5 生成结果</th></tr></thead><tbody><tr><td><pre caption="Prompt&#xA;" lang="Python" wrap="true"><code>30秒，16:9，一镜到底，真实电影感，欧式宫殿宴会厅派对群像镜头。场景参考 @图片8、@图片13、@图片17，主吊灯细节参考 @图片15，香槟杯参考 @图片1 和 @图片10，香槟塔参考 @图片3 和 @图片6，彩带参考 @图片19。人物为：男1参考 @图片2，男2参考 @图片11，男3参考 @图片4，男4参考 @图片7，女1参考 @图片9，女2参考 @图片5，男5参考 @图片16，女3参考 @图片18，男6参考 @图片12，女4参考 @图片14，男7参考 @图片20，其余背景宾客保持同一晚宴风格补足群像。 <br/> <br/>镜头从男2端着托盘开始。男2双手端托盘，托盘在胸前，托盘上放数只香槟杯。男1从画面左前方伸出右手，用右手拿起一只香槟杯，举到右肩前方，面向前方宾客大声说："Everyone, enjoy this party!"（音色参考 @音频1）说话时右手举杯，左手张开，头略微上扬。说完后立刻张嘴大笑，先看左边，再看右边。镜头同时向后拉成五人群像。男1站中间，右手举杯，左手张开。男3站男1左后方，右手举杯到肩膀高度，看向男1。男4站男1右后方，左手拿杯放在胸前，右手向上挥拳一次，看向男1。女1站男1左侧，双手在胸前鼓掌两次。女2站男1右侧，右手举杯，左手抬起欢呼。后景宾客也跟着举杯、鼓掌、转头看向男1。 <br/> <br/>男2完成递酒后，双手继续端托盘，从开场五人组前方向画面右侧走，托盘始终保持水平。镜头跟着男2向右移动，前景掠过礼服裙摆、持杯的手、人物肩膀和侧脸，背景持续能看到吊灯、帷幕、立柱、舞池和香槟塔。男2走到第二组群像前停下，站在中前景，双手端托盘。 <br/> <br/>第二组群像保持同一画面同一空间。画面左侧是碰杯组。男5站在女3对面，右手从男2托盘上拿起一只香槟杯，抬到胸前，看向女3说："Cheers to tonight."（音色参考 @音频2）女3右手拿着自己的香槟杯，抬起右手与男5轻碰一次，然后把杯子收回胸前。画面右侧是邀舞组。男6和女4面对面站立，两个人都空手，不拿香槟杯。男6看着女4，右手向前伸出，手掌朝上，说："May I have this dance?"（音色参考 @音频3）女4先停顿一瞬间，再抬眼看男6，露出笑容，然后把左手放到男6右手上。这个画面里同时存在左侧碰杯、右侧邀舞、服务生端托盘和背景宾客活动。 <br/> <br/>女4接受邀请后，男6右手牵着女4左手，带她走向舞池中央，两个人全程空手。女4右手提起裙摆方便移动。镜头跟着他们进入舞池。舞池边人群开始响应：有人鼓掌，有人举杯，有人身体轻摆。男6到达舞池中央后，左手牵女4右手，右手扶到女4背后，女4左手搭到男6肩部附近，进入舞蹈姿态。男7站舞池边鼓掌，其余背景宾客沿舞池外圈做鼓掌、举杯、轻摆动作。 <br/> <br/>镜头随后围绕男6和女4顺时针环绕。男6带女4完成两段舞蹈动作：第一段，男6带女4转半圈；第二段，男6抬高手，让女4原地转一整圈，女4红色裙摆展开。背景中的人群沿舞池外圈继续鼓掌、举杯、摆动，男1和开场五人组也在背景里继续举杯和欢呼。彩带在这一段从舞池正上方落下，位置集中在舞池中央和男女主头顶上方，数量少，只落少量细长彩带，垂直下落，不铺满整个大厅。镜头最后继续环绕两位舞者，保持他们在画面中心，背景是舞池、人群、吊灯、帷幕和少量下落的彩带，形成收尾画面。</code></pre></td><td><figure view-type="Preview"><source name="舞会-420音乐.mov" mime="video/quicktime" origin-height="1080.000000" origin-width="1920.000000" size="59624380" token="[媒体标识已移除]"/></figure></td></tr><tr><td><pre caption="Prompt&#xA;" lang="Python" wrap="true"><code>[0-3s] 近景拍摄，镜头聚焦在 @图1 正在拨动 @图2 古琴琴弦的手上。左侧一尊青铜香炉 @图3 青烟袅袅。背景中，一名白衣男子 @图4 模糊的身影正在吹奏 @图5。音效参考 @音效1，场景设定在水面 @图6 的小船 @图7 上，远景的山参考 @图8。 <br/>[3-5s] 白衣男子 @图4 立【于船头/起身】…一个圆形异象，@图9 的女子持 @图10 袭来，音效参考 @音效2。<br/>[5-10s] 白衣男子与红衣女子在湖面上空激烈交火，音效参考 @音效3。红衣女子持红伞，男子持扇 @图11。下方的水面被强大的真气激起巨大的环状浪花，音效参考 @音效4，如同一场水之风暴，特效参考 @视频1。 <br/>[10-20s] 白衣男子追逐红衣女子进入竹林 @图12，在水面上施展轻功 ……（后续段落被视频封面遮挡，未继续显现） </code></pre></td><td><figure view-type="Preview"><source name="32参-武侠群像.mp4" mime="video/mp4" origin-height="2160.000000" origin-width="3840.000000" size="159085521" token="[媒体标识已移除]"/></figure></td></tr><tr><td><pre caption="Prompt&#xA;" lang="SQL" wrap="true"><code>Create a 30-second video with realistic cinematic texture, 16:9 aspect ratio, documentary street photography style, warm and everyday lifelike atmosphere.<br/>Street scene environment references @image1: late-afternoon street corner, red brick buildings, pedestrian zebra crossings, storefronts along the road, roadside vehicles and passersby, soft directional afternoon sunlight, transparent natural color tones without heavy color grading filters.<br/>Figures and outfits of the main dancers reference @image2; appearances of pedestrian dancers reference @image3, @image4, @image5, @image6. All characters have distinct natural facial features, no uniform performance costumes.<br/>Smooth multi-angle handheld one-shot long take camera movement: high oblique overhead shot, sidewalk tracking shot, shoulder close-up shot, low-angle shot focusing on footwork.<br/>Background music audio track references @audio1, upbeat rhythmic street pop music that aligns perfectly with the dance beats.<br/>Plot: A girl wearing an orange knit beanie and over-ear headphones crosses the street, dancing gently alone to the music rhythm. Passersby are gradually drawn to the groove and join the casual group dance with loose, natural movements. There is motion blur on flowing hair and clothes, and background pedestrians fill out the street crowd.<br/>Restore the authentic textures of brick walls, asphalt roads, knit fabrics and denim, delivering a lively and laid-back overall mood.<br/>Avoid distorted human bodies, duplicate faces, neon night lighting, fantasy special effects, stage performance aesthetic, watermarks and subtitles.</code></pre></td><td><figure view-type="Preview"><source name="群舞 0715.mp4" mime="video/mp4" size="11608036" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>



### 3D 白模分镜预演   // 全模态参考

> 专业级 3D 资产 + 材质参考输入，结构与镜头调度原样承接。

<table><colgroup><col/><col/></colgroup><thead><tr><th>Prompt</th><th>Seedance 2.5 生成结果</th></tr></thead><tbody><tr><td><pre caption="Prompt&#xA;" lang="Python" wrap="true"><code>保持 @视频1 中的镜头运动、时长、构图、景别、空间关系、物体位置、模型结构和运动轨迹不变，以 @图片1 作为材质、光照、色彩和整体氛围参考，将 @视频1 中的白膜材质替换为接近 @图片1 的真实材质，加入自然光影、接触阴影、环境光、反射、高光和空间层次，整体呈现真实电影级渲染质感。</code></pre></td><td><figure view-type="Preview"><source name="飞船-594音乐.mov" mime="video/quicktime" origin-height="1080.000000" origin-width="1920.000000" size="38390298" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>



### 猩猩攀岩动作迁移 // 全模态参考

> 以真人攀岩视频为参考，将同一套攀爬动作、发力节奏与身体结构精准迁移到一只猩猩身上，画面兼具电影质感与生物合理性。

<table><colgroup><col/><col/><col/></colgroup><thead><tr><th>Prompt</th><th>参考素材</th><th>Seedance 2.5 生成结果</th></tr></thead><tbody><tr><td><pre caption="Prompt&#xA;" lang="Python" wrap="true"><code>将@视频1 中的动作迁移到一只在悬崖上攀岩的大猩猩身上，不改变运镜节奏及动作。</code></pre></td><td><figure view-type="Preview"><source name="攀岩-2.mp4" mime="video/mp4" origin-height="1112.000000" origin-width="834.000000" size="31031156" token="[媒体标识已移除]"/></figure></td><td><figure view-type="Preview"><source name="9a14f2c0b2a04129f29ff0f4340d99c5.mp4" mime="video/mp4" size="3149086" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>



### 影片光源重布 // 视频编辑

> 在保留原片构图、人物与运镜的前提下，一次性重写整段影片的光源布局：光位、色温、明暗层次与阴影方向同步变化，气氛从原版切换到全新光影语言。

<table><colgroup><col/><col/><col/></colgroup><thead><tr><th>Prompt</th><th>参考素材</th><th>Seedance 2.5 生成结果</th></tr></thead><tbody><tr><td><pre caption="Prompt&#xA;" lang="Python" wrap="true"><code>参考@视频1的光线从正午刺眼的顶光，改为日落时的侧光。</code></pre></td><td><figure view-type="Preview"><source name="天气对话.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="20055591" token="[媒体标识已移除]"/></figure></td><td><figure view-type="Preview"><source name="SG demo 视频编辑UX (1).mp4" mime="video/mp4" origin-height="1080.000000" origin-width="1920.000000" size="57101145" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>





### 更换演员表情&年龄       // 视频编辑

> 画面、镜头与节奏不变，仅对演员年龄与微表情精准编辑，一镜连续完成。

<table><colgroup><col/><col/><col/></colgroup><thead><tr><th vertical-align="top">Prompt</th><th vertical-align="top">参考素材</th><th>Seedance 2.5 生成结果</th></tr></thead><tbody><tr><td vertical-align="top"><pre caption="&#xA;" lang="Python" wrap="true"><code>保留@视频1的构图、机位、光线与表演节奏，只改写画面里女主的样貌与神情：让她从二十多岁自然地老去到六十岁，眼神里的隐忍慢慢化开，泪光滑过眼角，嘴角一点点扬起，最后破涕为笑。全程一镜到底，不跳切、不闪烁，五官随年龄渐变而不漂移。</code></pre></td><td vertical-align="top"><figure view-type="Preview"><source name="对镜含泪凝视.mp4" mime="video/mp4" origin-height="2160.000000" origin-width="3840.000000" size="22598418" token="[媒体标识已移除]"/></figure></td><td><figure view-type="Preview"><source name="表情变化.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="7231061" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>



### 调整影片风格   // 视频编辑

> 构图与运镜完全不变，一键切换实拍写实、插画、漫画等整体视觉风格

<table><colgroup><col/><col/></colgroup><thead><tr><th>Prompt</th><th>Seedance 2.5 生成结果</th></tr></thead><tbody><tr><td><pre caption="Prompt&#xA;" lang="Python" wrap="true"><code>保持@视频1 的运镜和节奏，将画面风格依次改为 黑白漫画风格、日本动漫风格、美式硬核风格、水墨动画风格。</code></pre></td><td><figure view-type="Preview"><source name="多风格替换6.23B.mp4" mime="video/mp4" origin-height="2160.000000" origin-width="3840.000000" size="113983542" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>

### 短素材延长成片   // 视频编辑

> 高保真时序延长，把短镜头自然延展为更长成片。

<table><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>初始视频</th><th>第1️⃣次 续写 </th><th>第2️⃣次 续写 </th><th>第 3️⃣次 续写 </th></tr></thead><tbody><tr><td><figure view-type="Preview"><source name="0615 发芽.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="2970975" token="[媒体标识已移除]"/></figure><br/> 视频1</td><td><pre caption="基于视频1 续写，生成视频2&#xA;" lang="Python" wrap="true"><code>在@视频 1 的基础上续写 5 秒的视频，讲一只蜜蜂飞来落在画上，接着微距特写蜜蜂腿部和腹部沾满金黄色花粉颗粒,蜜蜂振翅起飞,镜头跟随它飞向另一朵同种花上,慢镜头中,花粉从蜜蜂绒毛上抖落,精准落入花蕊——授粉瞬间被放大。</code></pre><figure view-type="Preview"><source name="视频节点 2 (1).mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="2465285" token="[媒体标识已移除]"/></figure><br/>  视频2  </td><td><pre caption="基于视频2续写，生成视频3&#xA;" lang="Python" wrap="true"><code>在@视频2的基础上，续写 5 秒的视频，内容是延时摄影质感:原本的黄色花瓣缓缓凋谢,花蕊位置开始膨胀,从青涩小果实逐渐生长、转色、饱满,最终成为一颗成熟的豆荚。豆荚表面挂着晨露,在阳光下泛着柔和高光<br/><br/>在@视频 3 的基础上续写 5 秒的视频延时摄影，背景闪过白天黑夜，成熟果实自然裂开,一颗种子顺势滑落掉下，镜头跟随它划过空气、落入湿润的泥土@图片 1 中。</code></pre><figure view-type="Preview"><source name="视频节点 3.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="2153206" token="[媒体标识已移除]"/></figure><br/>  视频3</td><td><pre caption="基于视频3续写，继续生成&#xA;" lang="Python" wrap="true"><code>在@视频 3 的基础上，续写 5 秒的视频延时摄影，背景闪过白天黑夜，成熟果实自然裂开,一颗种子顺势滑落掉下，镜头跟随它划过空气、落入湿润的泥土@图片 1 中。</code></pre><figure view-type="Preview"><source name="视频节点 4 (1).mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="2883165" token="[媒体标识已移除]"/></figure><br/>  视频4</td></tr></tbody></table>

### 多人多场景快切   // 全模态参考+多语种

<table><colgroup><col/><col/><col/></colgroup><thead><tr><th><b>Prompt</b></th><th><b>参考素材</b></th><th><b>生成结果</b></th></tr></thead><tbody><tr><td vertical-align="middle"><pre caption="Seedance 2.5&#xA;" lang="HTML" wrap="true"><code>真人实拍风格，快速剪辑，电影感，4K，24fps，温暖自然光，真实人物表演，自然口型同步，无字幕。以一朵鲜花的传递作为整支视频的核心视觉线索，花从一个国家快速传到下一个国家，串联全球不同地域与人群。每到一个场景，都有一个人物接过花、露出真诚微笑，并用当地语言说 “谢谢”。整体节奏轻快流畅，镜头富有动感，强调真实街头 / 生活气息、跨文化温暖连接、人与人之间的善意传递。<br/><b>转场方式：</b>以前一个人物把花递出画面，下一镜头由另一个人物在新场景中接住花<br/>或使用快速甩镜、运动模糊、前景遮挡完成无缝转场<br/>保持花在画面中的视觉连续性，形成 “一镜传全球” 的感觉<br/><b>镜头风格：</b>手持跟拍、轻微镜头晃动、快速推拉、近景与中景结合、真实环境音氛围、电影级街拍质感。背景音乐温馨、轻快、有世界旅行感，结尾温柔淡出。<br/><b>场景 1 【@图片1】</b>中国花店内，真实生活化场景。女孩接过一枝玫瑰，看向镜头微笑，自然地说：“谢谢！”镜头跟随花从画面右侧递入，女孩接花后轻轻扬起花束。<br/><b>场景 2【@图片2】</b>英格兰街头，微凉天气，街景自然。男士接过一枝康乃馨，微笑点头，说：“Thank you!”通过甩镜转场，花从上一场景甩入这一场景。<br/><b>场景 3 【@图片3】</b>墨西哥市场，色彩丰富，充满烟火气。阿姨接过一束万寿菊，双手合十，温暖地说：“¡Gracias!”镜头快速掠过摊位与人群，定格在接花瞬间。<br/><b>场景 4 【@图片4】</b>印尼乡村，自然阳光洒落。孩子接过一朵鸡蛋花，开心微笑，微微鞠躬，说：“Terima kasih!”镜头带一点奔跑感，氛围纯真自然。<br/><b>场景 5 【@图片5】</b>泰国街头，热闹市井。摊贩接过一串茉莉花环，双手合十，亲切地说：“ขอบคุณค่ะ!”镜头轻快推进，花环在阳光下微微摆动。<br/><b>场景 6 【@图片6】</b>阿拉伯庭院，光影柔和，环境雅致。女士接过一枝沙漠玫瑰，抚胸微笑，说：“شكراً!”画面安静而温暖，人物神情真挚。<br/><b>场景 7 【@图片7】</b>巴西社区，氛围热情鲜活。男孩接过一朵非洲菊，十分开心，说：“Obrigado!”镜头富有节奏感，充满生命力。<br/><b>场景 8 【@图片8】</b>日本街道，上班族接过便当上的一朵小花，礼貌鞠躬，说：“ありがとう！”镜头短促利落，保留都市节奏感。<br/><b>场景 9 【@图片9】</b>韩国街头，现代都市感。女青年接过一枝杜鹃花，双手自然合拢，微笑说：“감사합니다!”镜头在她微笑的瞬间稍作停留，随后画面柔和淡出。</code></pre></td><td vertical-align="middle"><grid><column width-ratio="0.250000"><img name="image.png" alt="图片展示了一位泰国花市的花贩，她身着花色上衣，面带微笑，双手递出一串白色茉莉花。画面中还可见其他色彩鲜艳的鲜花，如红色、绿色等。背景是湿漉漉的街道和店铺，路边有泰国国旗。图片与上下文“影视创作”中“多人多场景快切”场景相关，展示了泰国花市的场景，体现了多语种、全模态的参考素材。" mime="image/png" scale="0.570312" src="C3uabE721o2Ov1xpWRYckNTXntg"/></column><column width-ratio="0.250000"><img name="reference4.png" alt="这张图片呈现了一处充满生活气息的户外庭院场景，一位身着粉色印花上衣的东南亚小女孩面带笑意，正伸出张开的手掌，准备接过他人递来的一朵白黄相间的鸡蛋花。画面右侧的人物仅露出手臂，正将花朵伸向小女孩，背景可见木质的老旧门框、绿植、开着粉红花簇的植物，还有带有瓦片屋顶的民居建筑，整体氛围自然温馨，符合影视创作相关的场景参考需求。" mime="image/png" scale="0.356445" src="L8t2bJxeYoNjEyxB13vcm0l0nIe"/></column><column width-ratio="0.250000"><img name="reference6.png" alt="图片展示了一位身着浅色长袍、头戴头巾的女性，她手持一朵橙色花朵，背景为古色古香的建筑庭院，有拱形门廊、绿植和流水。画面右下角有“AI生成”标识。该图片位于文档中“多人多场景快切//全模态参考+多语种”应用场景部分，作为生成结果示例，与上下文提到的视频编辑、多人多场景快切等内容相呼应，体现了影视创作中视频编辑的多模态参考能力。" mime="image/png" scale="0.356445" src="T0jjb7hsSojtIrxE5EycYrWenbb"/></column><column width-ratio="0.250000"><img name="reference8.png" alt="图片展示了一位身穿白色衬衫、打着黑色领带、背着双肩包的男子，他面带微笑，手里拿着一束黄色的花。背景为一个室内场景，天花板上有蓝色的横梁，远处有“승승산서버리”字样的标识牌。图片下方有“AI生成”字样。该图片位于文档中“多人多场景快切//全模态参考+多语种”应用场景部分，可能是用于展示视频编辑或全模态参考等场景下的生成结果。" mime="image/png" scale="0.356445" src="T9n2bryJ9oR6auxTvnpcqtDOnPd"/></column></grid><grid><column width-ratio="0.200000"><img name="reference3.png" alt="图片展示了一位正在卖花的女性。她身着深色带有小花图案的上衣，面带微笑，右手递出一束橙色的花。背景中堆放着多种颜色的鲜花，有橙色、红色等，旁边还挂着一些装饰品。这张图片与文档中“多人多场景快切//全模态参考+多语种”应用场景相关，可能是用于生成视频素材的参考图片之一。" mime="image/png" scale="0.356445" src="CoTibF329oAIZYxfVddcwqavnJd"/></column><column width-ratio="0.200000"><img name="reference7.png" alt="这张图片出现在影视创作应用场景相关的内容中，呈现出阳光明媚的街巷场景，一位面带笑容的男孩站在石板路上，伸手递出一朵淡紫色的花朵，他身着蓝灰拼色的短袖T恤，周围是色彩明亮的民居建筑与绿植，画面传递出温暖的氛围，契合影片风格调整或视频编辑相关的实践展示场景。" mime="image/png" scale="0.356445" src="LvNEbKeysohsInxB0gucxNxCnAh"/></column><column width-ratio="0.200000"><img name="reference1.png" alt="这张图片呈现的是一家氛围温馨的花店内部场景，一位身着米白色针织开衫的年轻女士正笑着从他人手中接过一支包装好的浅粉色玫瑰，她身侧斜挎着黑色小包。店内摆放着各类鲜花，包括盛放的满天星、红玫瑰等，搭配木质货架，暖调灯光与自然光线结合，还原了日常购花的温馨画面。该图片用于配合文档中“多人多场景快切//全模态参考+多语种”相关的内容，作为影视创作调整影片风格相关实践的参考场景素材。" mime="image/png" scale="0.356445" src="X6Zobh6Zxo7dp3x0iwFc8noFnRc"/></column><column width-ratio="0.200000"><img name="reference9.png" alt="图片展示了一位女士，她面带微笑，手持一朵紫色的花，花茎细长，叶片呈绿色。女士穿着浅色上衣，肩上背着一个米色的包，背景是一条街道，街道旁有建筑物，墙上画有卡通图案，还摆放着一些绿植。图片位于文档中“多人多场景快切//全模态参考+多语种”应用场景部分，可能是用于展示生成结果。" mime="image/png" scale="0.356445" src="IUBfbxj7ho3mmhxmuahcJB0Fn7e"/></column><column width-ratio="0.200000"><img name="reference2.png" alt="图片展示了一位年轻男子站在花店前，手里拿着一束粉色康乃馨。他穿着灰色外套，面带微笑，低头看着手中的花。背景是铺满鹅卵石的小路，两侧是排列整齐的花店，花店外摆放着各种鲜花，还有写着“BLOOM WILD”的招牌。图片与上下文提到的“多人多场景快切”“全模态参考+多语种”等内容无关，可能是作为素材或示例图片。" mime="image/png" scale="0.356445" src="XJKPbkmdEogXHDxwbHjcGp7gnCe"/></column></grid></td><td vertical-align="middle"><figure view-type="Preview"><source name="output.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="11196686" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>

### 多语种版本同步发行   // 多语种

> 电影预告片宣发，一次创作输出多语种口播版本

<table><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th vertical-align="middle"><b>Prompt</b></th><th vertical-align="middle"><b>生成结果-英语</b></th><th><b>生成结果-日语</b></th><th><b>生成结果-法语</b></th></tr></thead><tbody><tr><td><pre caption="转换语种提示词&#xA;" lang="Markdown" wrap="false"><code>将声音、台词、旁白、标题字幕中的任何英语都改为法语/日语，其他均保持一致</code></pre><figure view-type="Preview"><source name="预告片A-去旁白版.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="55571041" token="[媒体标识已移除]"/></figure></td><td><figure view-type="Preview"><source name="预告片A.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="51887473" token="[媒体标识已移除]"/></figure></td><td><figure view-type="Preview"><source name="预告片A-日语.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="56848680" token="[媒体标识已移除]"/></figure></td><td><figure view-type="Preview"><source name="预告片A-法语.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="55646498" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>



## 4.2 ｜广告电商 🛍️



### 实拍广告 TVC    // 30 秒直出

> 单段 30s 完整承载从产品细节到场景演绎的品牌叙事。

<table><colgroup><col/><col/></colgroup><thead><tr><th>Prompt</th><th>Seedance 2.5 生成结果</th></tr></thead><tbody><tr><td><pre caption="Prompt&#xA;" lang="Python" wrap="true"><code>制作一支30秒竖屏家居广告。主产品为浅灰绿色模块组合沙发，圆润弧形线条，低矮厚实坐垫，搭配米白毯和棕色抱枕。<br/>前15秒为纯白无缝影棚产品展示：沙发完整陈列，镜头依次慢推近、水平横移、侧向平移展示轮廓与形态，最后后拉至全景定格。布光均匀柔和，背景纯白干净，不扫光、不闪白。<br/>后15秒转入暖光客厅傍晚：女主人穿米白针织家居服坐在沙发上读书，腿搭米白毯；轻放咖啡杯，猫跳上沙发；孩子跑入靠在肩上，女主人低头微笑；夜晚落地灯亮起，三者安静靠在沙发上，镜头缓慢后拉定格，留出品牌标识空间。整体风格克制、温柔、干净，画面真实自然。</code></pre></td><td><figure view-type="Preview"><source name="沙发.mp4" mime="video/mp4" origin-height="2160.000000" origin-width="3840.000000" size="106721445" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>



### 3D 动画广告   // 30 秒直出

<table><colgroup><col/><col/><col/></colgroup><thead><tr><th vertical-align="top"> Prompt</th><th vertical-align="top">参考素材</th><th>生成结果</th></tr></thead><tbody><tr><td vertical-align="top"><pre caption="Prompt&#xA;" lang="Plain Text" wrap="true"><code>3D 动画广告风，色彩明亮通透，果肉和汁水要有强烈的清爽感与冲击力。整体气质像高质量商业动画短片，带一点夸张幽默。沙漠角蜥角色可爱、灵动，表情丰富，参考【图片1】。画面质感参考图中那种柔和自然光、细腻绒毛 / 表皮质感、梦幻微距景深、真实中带一点童趣 的感觉。<br/>0-3 秒：画面一片被烈日暴晒的沙漠。空气热得扭曲，沙地发烫，远处像在冒烟。一只沙漠角蜥 趴在滚烫的沙子上，舌头微微吐着，眼神涣散，快被晒干了。它走两步就晃一下，整只沙漠角蜥像快要 “蒸发” 了。<br/>音效热浪呼呼声，轻微夸张的干裂声。<br/>3-6 秒：画面沙漠角蜥突然停住，鼻子动了动。它低头一看，沙子里竟然埋着一颗 冰凉饱满、带着水珠的葡萄柚。葡萄柚在阳光下晶莹发亮，表皮细腻，像沙漠里突然出现的奇迹。<br/>表演蜥蜴眼睛瞬间瞪大，像看到救命稻草。<br/>音效“叮” 一下的发现音效。<br/>6-8 秒：画面沙漠角蜥一个飞扑冲过去，双手死死抱住葡萄柚，整张脸贴在果皮上。它露出 “终于活过来了” 的幸福表情。画面定住 1 秒，形成一个夸张又好笑的广告记忆点。<br/>音效扑通一声，随后安静半秒。<br/>8-11 秒：画面沙漠角蜥抓住葡萄柚。葡萄柚果皮裂开，里面饱满的果肉闪着透亮光泽。下一瞬间，汁水不是流出来，而是像海啸一样喷涌而出。<br/>音效“咔嚓” 咬开声，接一声夸张的果汁爆开声。<br/>11-16 秒：画面橙粉色、清透发亮的葡萄柚汁水疯狂涌出，顺着沙丘倾泻，迅速淹没整片沙漠。干燥的黄沙瞬间变成一片 清凉、闪光、带着果香感的夏日海洋。沙漠里的仙人掌、石头、小沙丘纷纷被果汁海浪吞没，画面夸张又梦幻。<br/>表演沙漠角蜥刚开始还很兴奋，下一秒发现不对，表情从惊喜变成惊恐。<br/>16-20 秒：画面沙漠角蜥差点被 “葡萄柚海” 淹没，慌忙死死抱住半颗葡萄柚，像抱着救生圈一样漂浮在海面上。它湿漉漉地探出头，表情一脸懵。海面波光粼粼，颜色像被阳光照亮的果汁。<br/>音效夸张扑腾声，海浪声，带一点喜剧感。<br/>20-23 秒：画面突然切白屏。屏幕正中出现品牌字样和 slogan：“Seedance 葡萄柚，咬开的是果肉，涌出来的是夏天。”<br/>旁白念出整句：“Seedance 葡萄柚，咬开的是果肉，涌出来的是夏天。”<br/>音效干净清爽的品牌提示音。<br/>23-29 秒：画面白屏切回。沙漠角蜥已经悠闲地坐在漂浮的葡萄柚上，戴着一副小墨镜，抱着吸管杯，慢悠悠漂在 “果汁海面” 上度假。周围漂着橙色果肉、小冰块、清凉水花，天空变得湛蓝，气氛一下子从 “求生” 变成 “度假”。最后沙漠角蜥满足地靠在葡萄柚上，镜头拉远，定格在清爽、明亮、好玩的夏日画面里。<br/>音效轻松夏日音乐，海浪轻拍声。<br/>字幕可只保留品牌名，不必加太多字。</code></pre></td><td vertical-align="top"><img name="image.png" alt="图片展示了一只卡通风格的刺猬，位于沙漠环境中。刺猬身体呈浅棕色，背部和四肢上有明显的刺，刺尖呈黄色。它的眼睛大而圆，表情呆萌，背景是黄色的沙丘，远处有几棵仙人掌。图片与文档中“实拍广告TVC//30秒直出”及“3D动画广告//30秒直出”应用场景相关，可能是用于生成相关广告素材的示例图片。" mime="image/png" scale="0.134375" src="VZnGbGIjboQKRqxyAoIcBADanQH"/></td><td><figure view-type="Preview"><source name="葡萄柚zzz.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="32079012" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>



### 时尚品牌小片   // 全模态参考

> 一次性投喂服装、手袋、鞋履等多组单品与模特、场景参考，模型自由组合输出多套穿搭与多场景时尚成片，商品细节与模特形象全程稳定保持。

<table><colgroup><col/><col/></colgroup><thead><tr><th>Prompt</th><th>Seedance 2.5 生成结果</th></tr></thead><tbody><tr><td><pre caption="Prompt&#xA;" lang="Python" wrap="true"><code>请生成一条30秒的一镜到底视频，脚本：6 位模特依次接力入画，整段运镜穿梭到底，配乐卡点切换造型。@图片1 戴着 @图片2 在 @图片3 的场景中，音效参考 @音效1。@图片3 穿着 @图片4，戴着 @图片五 的帽子，戴上了 @图片6 墨镜，端着咖啡走出来，背景是 @图片7 摆放着 @图片8，音效参考 @音效2。@图片9 在 @图片10 的场景中，穿着 @图片11 和 @图片12 摆 pose。@图片13 拎着 @图片14，穿着 @图片15 在 @图片16 中走，音效参考 @音效3。@图片17 头戴 @图片18，拎着 @图片19，在 @图片20 走来，音效参考 @音效4。@图片21 戴着 @图片22 在 @图片23 走秀，音效参考 @音效5。</code></pre></td><td><figure view-type="Preview"><source name="多人多造型.mp4" mime="video/mp4" origin-height="2160.000000" origin-width="3840.000000" size="146333259" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>





### 商品使用指导视频 // 30s 直出+参考

<table><colgroup><col/><col/><col/></colgroup><thead><tr><th>Prompt</th><th>参考素材</th><th>Seedance 2.5 生成结果</th></tr></thead><tbody><tr><td><pre caption="Prompt&#xA;" lang="Python" wrap="true"><code>产品是@图片1,安装使用说明是@图,2,创作一段蒸烤一体机的首次使用全流程视频。</code></pre></td><td><img name="image.png" alt="图片展示的是一个蒸烤一体机。主体为黑色，边缘和顶部有金属质感的装饰。机器正面配有透明玻璃门，门内有金属托盘和旋转烤架。上方显示屏显示“200℃”温度。该图片位于介绍广告电商应用场景中“实拍广告TVC//30秒直出”部分，可能是用于展示产品外观，辅助说明广告中所展示的蒸烤一体机。" mime="image/png" scale="0.570312" src="YeYyb1e2RomrrKxnyiHcsblonuf"/><img name="ea26981fbf4868e4bca8f2ccede76271.png" alt="图片是DISO智能电烤箱的使用指导手册，分为产品规格说明、摆放与准备、使用方法、清洁维护、功能参考、安全注意事项、收纳等七个部分。如产品规格说明中列出产品类型、控制方式、加热方式、使用环境等；摆放与准备部分提示平放平台、禁放重物；使用方法包括1. 开始烹饪、2. 功能参考；清洁维护有1. 用后清洁、2. 保养提示；安全注意事项涵盖使用前检查、使用中安全、使用后安全等；收纳部分提示存放于干燥、通风处。" mime="image/png" scale="0.650045" src="H6zlbhQB6oL8lUxOdw4c91HdnVc"/></td><td><figure view-type="Preview"><source name="蒸烤一体机.mp4" mime="video/mp4" origin-height="2160.000000" origin-width="3840.000000" size="64668327" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>



### 爆款视频复用 // 全模态参考

<table><colgroup><col/><col/><col/></colgroup><thead><tr><th>Prompt</th><th>参考素材</th><th>Seedance 2.5 生成结果</th></tr></thead><tbody><tr><td><pre caption="Prompt&#xA;" lang="HTML" wrap="true"><code>参考 @视频1 的运镜方式与剪辑节奏，生成一条<b>耳机@图片</b>的广告短片。适配符合产品调性的场景，强调现代、简洁、科技感。产品特写与场景全景的切换点与原片一致，保持同样的运动速度与转场方式。 </code></pre></td><td><figure view-type="Preview"><source name="6月14日(2).mov" mime="video/quicktime" origin-height="1080.000000" origin-width="1920.000000" size="22005744" token="[媒体标识已移除]"/></figure><img name="image.png" alt="这张图片展示了一款头戴式耳机，从三个不同视角呈现：左侧为正面视角，可看到耳罩、头梁内侧的软垫；中间为侧面视角，能呈现耳机整体的弧度与两侧耳罩的轮廓；右侧为背面视角，可看到头梁背部的结构以及耳壳侧部的控制按钮。该耳机整体为银灰色，设计简约流畅，属于爆款视频复用场景下全模态参考的素材，是Seedance 2.5生成相关内容时的参考素材。" caption="&#xA;" mime="image/png" scale="0.217969" src="Q4Qmb6mHqoTqFjx8ae5c3cP1nTg"/></td><td><figure view-type="Preview"><source name="换耳机.mp4" mime="video/mp4" origin-height="1080.000000" origin-width="1920.000000" size="26850934" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>



### 电商 SKU 批量复用   // 参考+视频编辑

> 同一镜头内批量替换商品款式 / 颜色，一次拍摄覆盖整条 SKU。

<table><colgroup><col/><col/></colgroup><thead><tr><th>Prompt</th><th>Seedance 2.5 生成结果</th></tr></thead><tbody><tr><td><pre caption="Prompt&#xA;" lang="Python" wrap="true"><code>汽水饮品图是@图片1,场景图@图片2，通过特写、近景、中景、远景镜头对汽水饮品进行展示,镜头衔接连贯,主体保持一致。<br/><br/>把@视频1中的汽水饮料瓶替换成@图片3粉色饮料瓶<br/><br/>把@视频2中的汽水饮料瓶替换成@图片4紫色饮料瓶<br/><br/>把@视频3中的汽水饮料瓶替换成@图片5绿色饮料瓶</code></pre></td><td><figure view-type="Preview"><source name="视频编辑·主体替换.mp4" mime="video/mp4" origin-height="2160.000000" origin-width="3840.000000" size="113165947" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>





### 出海广告本地化适配   // 多语种+视频编辑

> 镜头与节奏不变，快速更换人种 / 商品 / 文案产出多地区版本。

<table><colgroup><col/><col/><col/></colgroup><thead><tr><th>Prompt</th><th>参考素材</th><th>Seedance 2.5 生成结果</th></tr></thead><tbody><tr><td><pre caption="原始视频生成 Prompt&#xA;" lang="Python" wrap="true"><code>@图片 1 是产品图，@图片 2是主播和场景图。主播在说台词的同时，双手和台词进行同样的挥动讲解。表情真实自然。<br/>0-2 秒：@图片 2 固定镜头，主角对着镜头说中文，台词是「清晨第一杯咖啡，等不了。」。<br/>(2–5s)按下开关，固定镜头，台词是「按一下，3 秒出杯。」<br/>(5–9s)继续看着镜头说，台词是「办公室、出差、深夜赶稿——现磨咖啡随身就有。」<br/>(9–12s)看着镜头说，台词是「打工人续命神器，限时直降。」</code></pre><pre caption="视频编辑 Prompt&#xA;" lang="Python" wrap="true"><code>将视频中的人物换成美国女性，将文案旁白改成英语。<br/>将视频中的人物换成西班牙男性，将文案旁白改成西班牙语。<br/>将视频中的人物换成印度尼西亚女性，将文案旁白改成印度尼西亚语。<br/>将视频中的人物换成马来西亚男性，将文案旁白改成马来西亚语。</code></pre></td><td><img name="中国.png" alt="图片展示了一位女性在厨房场景中，她身着浅棕色上衣，佩戴项链，左手轻触咖啡机，右手比划着，面带微笑。背景为现代简约厨房，橱柜整齐，台面上摆放着咖啡杯、咖啡豆等物品，墙上置物架上陈列着咖啡壶、杯子等。此图位于介绍电商SKU批量复用应用场景的文档中，可能是用于展示广告电商相关视频编辑的参考素材，体现轻松愉悦的氛围。" mime="image/png" scale="0.570312" src="Y57jbgLP7oRUqbxgMkdchDBIndb"/><img name="image.png" alt="图片展示的是HIBREW咖啡机。主体为白色，顶部有银色按钮，侧面印有“HIBREW”品牌标识。机器底部装有咖啡胶囊，下方放置着一杯装有深色咖啡的透明玻璃杯。该图片位于文档中“电商SKU批量复用//参考+视频编辑”应用场景介绍部分，可能是用于展示电商平台上销售的咖啡相关商品，与电商SKU批量复用的场景相契合。" mime="image/png" scale="1.000000" src="CDtAbUvfxohDo0x5DfXcwz0dn7d"/></td><td><figure view-type="Preview"><source name="74109337d8b899db0876d1d8357f3a51_raw.mp4" mime="video/mp4" origin-height="2160.000000" origin-width="3840.000000" size="44401073" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>







### 家居装修方案演示 //参考+视频编辑

> 仅凭一句简单提示词，模型即可在同一空间基础上重新演绎全新装修风格：墙面材质、家具形制、软装配色、灯光氛围整体切换，同时保持房型结构与镜头调度不变，让设计师能在客户沟通现场快速试装、比对多套方案。

<table><colgroup><col/><col/></colgroup><thead><tr><th>Prompt</th><th>Seedance 2.5 生成结果</th></tr></thead><tbody><tr><td><pre caption="Prompt&#xA;" lang="SQL" wrap="true"><code>Use the input video as the exact source and preserve the original camera movement, timing, composition, room layout, lighting, shadows, furniture positions, and all objects.<br/>Only edit two materials in the living room:<br/>1. Replace the light fabric sofa on the right side of the room with a rich brown leather sofa. Keep the exact same sofa shape, size, position, cushion layout, armrests, backrest, and perspective. The new sofa should look like realistic brown leather, with natural leather grain, subtle wrinkles, stitching, soft glossy highlights, and physically believable reflections from the window light.<br/><br/>2. Replace the visible warm wooden floor with polished white marble flooring. Keep the exact same floor plane, perspective, scale, and room geometry. The marble should be white to light gray with natural subtle veins, realistic seams, and controlled polished reflections. The marble reflections should respond to the window light, furniture legs, plants, sofa base, and room shadows.<br/><br/>Everything else must remain unchanged: the window, curtains, walls, wall art, TV, TV console, plants, rug, coffee table, books, radiator, shelves, doorframe, lighting, shadows, camera motion, and overall warm interior atmosphere. The rug and coffee table stay exactly where they are, on top of the new marble floor. The edit should look like a realistic interior renovation, not a new generated room.<br/><br/>Maintain temporal consistency across the full video. The sofa and floor materials must remain stable from frame to frame with no flickering, warping, melting, or object changes. Preserve the original video’s natural daylight, warm tone, soft shadows, lens behavior, and smooth camera movement.<br/>Negative Prompt<br/>Do not change the room layout. Do not move furniture. Do not add or remove objects. Do not change the rug, coffee table, TV, plants, curtains, window, wall art, shelves, radiator, or doorframe. Do not change the camera movement. Do not change the sofa shape or size. Do not make the leather look plastic. Do not make the marble overly reflective like a mirror. Do not create broken or chaotic marble veins. Do not replace the rug with marble. Do not alter the walls or ceiling. No people, no text, no logo, no UI, no selection mask, no fantasy effect, no melting transition, no flickering.</code></pre></td><td><figure view-type="Preview"><source name="家具+配乐07132227.mov" mime="video/quicktime" size="33625984" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>





## 4.3 ｜知识科普 📚

### 货币的演变 // 30秒直出

> 用木质桌面上的微缩世界，把从以物易物、贝币铜钱、宋代交子、现金卡片一路讲到今天移动支付的五千年货币史，串成一个连续镜头，可用作科普短视频或课堂开场素材。

<table><colgroup><col/><col/></colgroup><thead><tr><th>Prompt</th><th>Seedance 2.5 生成结果</th></tr></thead><tbody><tr><td><pre caption="Prompt&#xA;" lang="Python" wrap="true"><code>一段30秒的定格动画微缩视频，用英文讲解。在一张温暖的木桌上，五个微型世界从左到右依次排开——以物换物、贝壳与铜钱、宋代纸币、现代现金与银行卡、当今移动支付。镜头缓缓横移，扫过这条手工打造的货币时间线，画面中有黏土小人、移轴镜头，配以平静的英文旁白。五千年货币史，在一个连续长镜头中娓娓道来——从握在手心的重量，到放在口袋里的轻盈。</code></pre></td><td><figure view-type="Preview"><source name="输出V2.mp4" mime="video/mp4" size="41840138" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>



### 天文知识可视化   // 30秒直出

> 将抽象原理转化为连续可视化视频

<table><colgroup><col/><col/></colgroup><thead><tr><th>Prompt</th><th>Seedance 2.5 生成结果</th></tr></thead><tbody><tr><td><pre caption="Prompt&#xA;" lang="Python" wrap="true"><code>生成一条科普视频，在讲月球是如何诞生的。画面质感要有电影感，视觉效果要强，在爆炸/汇聚的过程中要有视觉的张力。要符合事实情况，遵循科学依据。<br/><br/>0-2s：太空远景，画面下方是地球弧面与蓝色大气层，上方远处有一颗暗红色小天体悬在黑色宇宙中，镜头基本静止，缓慢呈现地球与天体的距离关系<br/>2-3s：切到近景，一颗表面布满橙红熔岩裂缝的巨大天体靠近地球边缘，地球大气层在右下方形成蓝色弧线，镜头静止，天体压迫感增强<br/>台词：45亿年前，地球被一颗火星大小的天体撞击<br/>3-5s：熔岩天体撞击地球边缘，强烈白橙色爆光从接触点喷发，大量炽热碎片和火焰沿地球表面向外飞散，镜头跟随爆炸冲击连续推进<br/>5-8s：撞击后的炽热物质在太空中汇聚成发光的橙红熔融球体，周围有碎片和尘埃盘旋，背景可见地球一侧，镜头由近到远缓慢拉开<br/>8-10s：地球旁边出现发光的环状熔融物质与碎片带，橙红色物质围绕地球轨道分布，黑色太空背景，镜头保持远景观察<br/>台词：撞击让两者部分熔化，物质被甩入地球轨道<br/>10-12s：切到月面近景，灰色坑洼地表上布满橙红色熔融裂缝，碎石和尘埃散落，画面从灼热裂缝逐渐过渡到冷却的灰色表面<br/>12-14s：灰色月面继续成形，坑洼地貌更稳定，画面右侧出现月球边缘和暗面，镜头缓慢拉远，表现月球从碎片中聚合完成<br/>台词：碎片在几千万年内，聚成了月球，你头顶的月亮，就是这次撞击的产物<br/>14-21s：地球与月球同框，镜头拉远，月球在远离地球的方向上运动。地球和月球中间出现标尺，标尺上有数字的不停生长<br/>台词：它至今仍以每年3.8厘米的速度远离地球</code></pre></td><td><figure view-type="Preview"><source name="月球科普素材-加字幕.mp4" mime="video/mp4" origin-height="1080.000000" origin-width="1920.000000" size="38949823" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>





### 儿童科普动画   // 30 秒直出

> 国风插画长卷配合旁白逐句讲解，画面随讲述连续展开。

<table><colgroup><col/><col/></colgroup><thead><tr><th>Prompt</th><th>Seedance 2.5 生成结果</th></tr></thead><tbody><tr><td><pre caption="Prompt&#xA;" lang="Python" wrap="true"><code>儿童向丝路文化科普动画短片，敦煌壁画与丝路长卷风格，岩彩平面动画，矿物颜料质感，赭石、绢白、石青、石绿、黛青、朱砂、金线点缀，平面分层，长卷式流动构图，不要真实摄影，不要 3D 写实，不要幼稚卡通。重点突出石榴的由来与传播，不强调现代饮用方式，现代部分控制在 7 秒以内。<br/>00:00-00:04，一幅丝路长卷缓缓展开，枝头出现一颗轻轻晃动的石榴。口播：“你知道吗？我们今天常见的石榴，其实很早很早以前，就来自中国西边很远的地方 —— 西域。”<br/>00:04-00:08，一只手轻轻摘下石榴，把它捧起，远山、纹样和道路展开。口播：“一开始，它生长在阳光充足的土地上。后来，人们把它带上旅途，准备去更远的地方。”<br/>00:08-00:15，驼队带着石榴穿过沙漠、绿洲和城门。口播：“石榴跟着驼队慢慢往前走。一路上，它要穿过沙漠，经过绿洲，还要走过高高的城门。这条很长很长的路，就是古代有名的丝绸之路。”<br/>00:15-00:20，石榴随着商旅进入更多城镇与生活场景。口播：“丝绸之路运送的，不只有丝绸。很多远方的水果、香料和种子，也会沿着这条路来到新的地方。石榴就是这样，慢慢被更多人认识了。”<br/>00:20-00:23，石榴被切开，露出像红宝石一样的果粒。口播：“后来，人们发现，石榴不仅好看，里面还藏着许多像红宝石一样的小果粒。”<br/>00:23-00:27，长卷中的古代场景慢慢过渡到今天，石榴出现在现代桌面，一群小朋友围坐在一起吃石榴。口播：“就这样，经过很长很长的传播，石榴从西域出发，最后走进了今天的生活。”<br/>00:27-00:30，枝头石榴、驼队、沙漠、绿洲、城门和今天桌上的石榴在长卷中汇合。口播：“所以，一颗小小的石榴，也藏着一段跨越土地和时间的旅行。”</code></pre></td><td><figure view-type="Preview"><source name="石榴.mp4" mime="video/mp4" origin-height="2160.000000" origin-width="3840.000000" size="176044736" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>





### 真人口播知识讲解   // 30 秒直出

> 真人全程口播配合实物道具自然演示，口型与节奏连贯。

<table><colgroup><col/><col/></colgroup><thead><tr><th>Prompt</th><th>Seedance 2.5 生成结果</th></tr></thead><tbody><tr><td><pre caption="Prompt&#xA;" lang="Python" wrap="true"><code>扎羊角辫的6岁小女孩坐在沙发上，面前摆着各朝代瓷器小模型，举着模型一一介绍： ①举粗陶小罐：「最早的瓷器是从陶器变来的哦，商朝就有原始瓷啦」，背景淡入商朝原始瓷文物画面； ②举青釉小碗：「唐朝越窑的青瓷、邢窑的白瓷最有名，还有花花的唐三彩」，背景淡入唐三彩文物画面； ③举天青色小碟子：「宋朝的瓷器最好看，汝窑的天青色要等雨过天晴才能烧出来哦」，背景淡入汝窑文物画面； ④举青花瓷小瓶：「明清的时候青花瓷、珐琅彩就都有啦，还卖到全世界呢」，背景淡入青花瓷文物画面。 最后小女孩举着自己画的青花瓷画对着镜头笑，配轻快儿童BGM。</code></pre></td><td><figure view-type="Preview"><source name="小女孩0622.mp4" mime="video/mp4" origin-height="1080.000000" origin-width="1920.000000" size="49955385" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>





### 结构拆解与原理还原   // 全模态参考

> 参考视频运镜与节奏，还原参考图背后的结构与逻辑。

<table><colgroup><col/><col/><col/></colgroup><thead><tr><th>Prompt</th><th>参考素材</th><th>Seedance 2.5 生成结果</th></tr></thead><tbody><tr><td><pre caption="Prompt&#xA;" lang="Python" wrap="true"><code>参考@视频1的创意生成视频，要求 还原@图片1 @图片2 @图片3 @图片4 房子组装全过程。</code></pre></td><td><grid><column width-ratio="0.501002"><img name="img_v3_0212t_e3dafc85-b24a-47c4-9175-25f1a90d431g.png" alt="图片展示了一栋位于海滩边的两层木屋。房屋主体为浅棕色木结构，带有深色屋顶，设有多个阳台和露台。房屋前方有木质楼梯通向沙滩，周围有绿植点缀。背景是广阔的蓝天和碧海，海面上有几只海鸥飞翔，远处还有白云飘浮。此图与文档中知识科普应用场景相关，可能用于展示与自然、度假等主题相关的生成结果。" mime="image/png" scale="0.265262" src="VTcabmBIaoKjE5xySHgcACqpnxe"/></column><column width-ratio="0.498998"><img name="img_v3_0212t_d3dab385-7225-4bf4-a125-4aef0431828g.png" alt="图片展示了一处位于海滩边的建筑。建筑主体为蓝绿色，带有阳台，阳台上摆放着盆栽。建筑前设有自动售货机和黄色的门，门口摆放着绿植。建筑右侧有两棵高大的棕榈树，背景是蓝天白云和远处的海面，海面上有几只飞翔的海鸥。该图片与文档中知识科普应用场景的内容相关，可能是用于展示相关场景或作为素材参考。" mime="image/png" scale="0.501374" src="LtpZbHIZ8ocs5nxN73Cc36zrnIf"/></column></grid><grid><column width-ratio="0.333333"><img name="img_v3_0212t_036e60a3-9e84-4b5d-87d9-5e0cd54046dg.png" alt="图片展示了一处海边的场景。画面中有一栋黄色的两层建筑，建筑前有两张红色的自动售货机，旁边摆放着一些绿植。建筑两侧各有一棵高大的香蕉树，树下还摆放着几盆绿植。背景是蓝天白云，远处是蓝色的海面，海面上有几只飞翔的海鸥。这张图片与文档中“知识科普”应用场景下的结构拆解与原理还原内容相关，可能用于辅助说明或展示相关内容。" mime="image/png" scale="0.501374" src="VKrNbMybMoE2OvxhM1ScZQVCnqg"/></column><column width-ratio="0.333333"><img name="img_v3_0212t_f21c3507-b382-4fac-ac10-95293a0207cg.png" alt="图片展示了一栋位于海边的建筑。建筑主体为米白色，带有红色屋顶，外观呈对称结构，有多个窗户和阳台，阳台上有栏杆。建筑前方有台阶，背景是清澈的蓝天和平静的海面，海面与天空交界处有一条分界线。图片与文档中“知识科普”应用场景下“结构拆解与原理还原”部分内容相关，可能用于辅助说明相关概念或原理。" mime="image/png" scale="0.501374" src="SSWEb7ocyotKylxOKAEcdITTnnh"/></column><column width-ratio="0.333333"><figure view-type="Preview"><source name="cc88c7aa0d479bb1cb5d5215a1258479.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="1698541" token="[媒体标识已移除]"/></figure></column></grid></td><td><figure view-type="Preview"><source name="多模态参考视频生成6.23.mp4" mime="video/mp4" origin-height="1080.000000" origin-width="1920.000000" size="127787159" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>





### 航海纪念馆多语言讲解 // 多语言 

> 同一位讲解员穿行于航海纪念馆不同展区，面对不同文物自然切换 **英语 → 新加坡口音中文 → 马来语 → 日语**，人物形象、口型、语速与情绪全程一致。

<table><colgroup><col/><col/></colgroup><thead><tr><th>Prompt</th><th>Seedance 2.5 生成结果</th></tr></thead><tbody><tr><td><pre caption="Prompt&#xA;" lang="Python" wrap="true"><code>30s multilingual Southeast Asian heritage museum documentary. One guide leads through four connected galleries about trade, migration, craft, and Singapore's regional history. Warm, authentic museum realism, not tourism advertising.<br/>0-7.5s Port Model Gallery, English.Singapore harbor and Malacca Strait model, moving ship lights, blue map wall. Guide: "Singapore has always been a meeting point, not just a destination."<br/>7.5-15s Ceramics &amp; Spice Room, Mandarin.Blue-white porcelain, spice jars, cinnamon, cloves, pepper, wooden crates, warm light. Guide: "这些瓷器和香料，记录的是一条从海上长出来的生活方式。"<br/>15-22.5s Malacca Trade Gallery, Malay.Teak walls, ship model, batik, pewter, route maps, brass lanterns. Guide: "Di Selat Melaka, kapal, rempah dan bahasa bertemu. Perdagangan menghubungkan banyak budaya."<br/>22.5-30s Travel Objects Gallery, Japanese.Suitcases, letters, textiles, family photos in glass cases, soft paper light. Guide: "旅の品物は、場所を移すたびに、新しい意味を持ちます。"<br/>Camera: 16:9 warm documentary style, slow museum walkthrough, guide moments mixed with object close-ups.</code></pre></td><td><figure view-type="Preview"><source name="9151382433480913833.mp4" mime="video/mp4" size="11510489" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>





## 4.4 ｜工业 / 制造业场景 🏭



### 无人机第一视角飞行 // 30秒直出+全模态参考

<table><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th vertical-align="top">场景</th><th vertical-align="top">Prompt</th><th vertical-align="top">参考素材</th><th vertical-align="top">Seedance 2.5 生成结果</th></tr></thead><tbody><tr><td>无人机穿越山谷瀑布</td><td><pre caption="&#xA;" lang="Python" wrap="true"><code>总设定：第一人称 FPV 竞速无人机视角，电影级实拍质感，一镜到底无剪辑，总时长 25 秒。晴天，通透蓝天，真实光照与大气透视。镜头始终朝无人机前进方向，高速带轻微机身姿态倾斜与惯性摆动。空间关系严格按红线单向推进：起点（左下山坡）→ 瀑布顶 ① → 瀑布底 → 村庄 ② → 远处两座山之间的缝隙 ③ → 山谷深处远景，全程向前、不回头、不倒飞、不绕回起点。<br/>运动路径（按顺序连续衔接）：<br/>无人机从峡谷左下方绿色山坡上低空启动，贴坡加速爬升，朝左侧崖壁上倾泻而下的大瀑布飞去；沿瀑布左侧崖壁一路向上攀升，绕到瀑布顶端，从上方俯瞰跌水口与源头溪流（对应标记 ①）。<br/>越过瀑布顶后，无人机压低机头，沿瀑布外侧崖壁向下俯冲，掠过飞溅的水雾边缘（不进入水帘），落到瀑布底部的河面上方；随即转向右侧，沿蜿蜒河流以流畅波浪线高速前飞，贴着屋顶掠过山谷中段的石屋村落（对应标记 ②）。<br/>穿过村庄后继续沿河谷向右深入，全速冲向远景中最高的两座山，从两座峰之间的 V 形缝隙正中央穿过（对应标记 ③），出画进入开阔山谷远景，稳定收尾。<br/>负向限制：不出现任何画面文字 / 标记 / 红线 / 编号；不要从正面穿过水帘、不要钻进水雾里；）；不朝后飞、不无故盘旋停滞；天气光照全程一致；总时长严格 25 秒，不得中途黑场或加速跳切。</code></pre></td><td><img name="image" alt="这张图片是无人机第一视角飞行的路线示意图，以红色箭头标注出飞行路径，路径起点在左下角位置。图中用数字1、2、3分别标记了三个关键节点：节点1对应左侧峭壁间的瀑布，节点2对应河流旁的村镇，节点3对应右侧高耸的峰林。背景呈现出山川、河流、植被与远处雪山融合的自然风光，整体清晰展示了无人机从起点出发，依次经过瀑布、村镇，最终抵达峰林的飞行路线，契合文档中无人机第一视角飞行30秒直出的实践内容。" mime="image/jpeg" scale="1.000000" src="BclrbOuHCombYzxuomCcukA8nDf"/></td><td><figure view-type="Preview"><source name="110216aa00e049eaa85591267c0ea251_a=0&amp;ch=0&amp;cr=0&amp;dr=0&amp;er=0&amp;lr=default&amp;&amp;br=13638&amp;bt=13638&amp;cs=0&amp;ds=3&amp;mime_type=video_mp4&amp;qs=13&amp;rc=amV2M2dvOml3PDczNGllM0BpamV2M2dvOml3PDczNGllM0BeYjZqYWFmYWRhLS1kXy9zYSNeYjZqYWFmYWRhLS1kXy9zcw%3D%3D&amp;cquery=102y&amp;d.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="43741332" token="[媒体标识已移除]"/></figure></td></tr><tr><td>无人机穿越上海</td><td><pre caption="&#xA;" lang="Python" wrap="true"><code>生成一段 15 秒第一人称 FPV 视角的超高速无人机穿梭视频，电影级，一镜到底。镜头从黄浦江江面 / 东方明珠电视塔底座附近的低空起点出发，先极速拉升并流畅环绕东方明珠的塔身、下球体、上球体与塔尖天线，再按照图片中红线轨迹的空间关系高速飞越黄浦江，冲向陆家嘴金融区，在上海中心大厦、上海环球金融中心（SWFC）、金茂大厦三件套之间左右穿梭、上下起伏，最后沿图片箭头方向，（但是不要出现红线，只是引导作用）向浦东天际线右前方冲刺，在开阔的城市远景中结束。</code></pre></td><td><img name="image.png" alt="图片展示了上海外滩的标志性建筑，背景是蓝天白云。图中用红色数字标注了3个位置，①处为东方明珠塔，②处为上海中心大厦，③处为金茂大厦。起点位于东方明珠塔附近。图片与上下文关系紧密，是对上文“无人机穿越东京”场景中参考素材的补充说明，直观呈现了上海外滩的建筑布局，为无人机穿越场景提供视觉参考。" mime="image/png" scale="1.000000" src="Fjnwb4mgooj4jsx3f1LczZgDngh"/></td><td><figure view-type="Preview"><source name="7684d49e7c6041a49c1ba1f971e56d7a_a=0&amp;ch=0&amp;cr=0&amp;dr=0&amp;er=0&amp;lr=default&amp;&amp;br=10730&amp;bt=10730&amp;cs=0&amp;ds=3&amp;mime_type=video_mp4&amp;qs=13&amp;rc=Mzw6c2RvOnR2PDczNGllM0BpMzw6c2RvOnR2PDczNGllM0BpbTNrYWFeaGZhLS1kXy9zYSNpbTNrYWFeaGZhLS1kXy9zcw%3D%3D&amp;cquery=102y&amp;d.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="20700488" token="[媒体标识已移除]"/></figure></td></tr><tr><td>无人机穿越<br/>东京</td><td><pre caption="&#xA;" lang="Python" wrap="true"><code>生成一段 15 秒第一人称 FPV 视角的超高速无人机穿梭视频，电影级，一镜到底。镜头从东京塔底座附近的低空起点出发，先极速拉升并流畅环绕东京塔的红白塔身、大展望台与塔尖，再按照图片中红线轨迹的空间关系，高速掠过港区与涩谷密集的城市屋顶，冲向新宿超高层建筑群，在都厅、Mode 学园茧塔与玻璃幕墙高楼之间左右穿梭、上下起伏，最后沿图片箭头方向向新宿天际线右前方冲刺，在黄昏金色余晖下的东京远景中结束。（但是不要出现红线，只是引导作用）</code></pre></td><td><img name="image.png" alt="图片展示了东京城市景观，东京塔位于画面左侧，其周围有红色箭头标注的飞行路线。路线从起点开始，绕过东京塔，向右上方延伸，途经多个地标建筑区域，最终到达画面右上角。图片与上下文“无人机穿越东京”场景相关，直观呈现了无人机穿越东京的飞行路径，为30秒直出+全模态参考的Seedance 2.5生成结果提供了视觉参考。" mime="image/png" scale="1.000000" src="E2WCbFIm1ouDK6x8bMVcd9VKnl2"/></td><td><figure view-type="Preview"><source name="e9c13308772b45199b2d74fbd31da9fd_a=0&amp;ch=0&amp;cr=0&amp;dr=0&amp;er=0&amp;lr=default&amp;&amp;br=11255&amp;bt=11255&amp;cs=0&amp;ds=3&amp;mime_type=video_mp4&amp;qs=13&amp;rc=M3A2bTtvOjN2PDczNGllM0BpM3A2bTtvOjN2PDczNGllM0BxYmtpYWEvaWZhLS1kXy9zYSNxYmtpYWEvaWZhLS1kXy9zcw%3D%3D&amp;cquery=102y&amp;d.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="21671448" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>



### 机器人动作交互  // 30秒直出

<table><colgroup><col/><col/></colgroup><tbody><tr><td vertical-align="top"><b>Prompt</b></td><td vertical-align="top"><b>生成结果</b></td></tr><tr><td><pre caption="&#xA;" lang="Python" wrap="true"><code>灶台上从左到右摆着：装一颗白色鸡蛋的小白瓷碗、燃气灶、白色圆形瓷盘。灶台后方立着敞口不锈钢油壶（无盖）、木柄锅铲、黑色不粘平底锅。这些物件从始至终都在画面里。<br/>一台白色人形双臂家务机器人站在灶台前。右手握住锅柄把不粘平底锅放到灶眼上，左手食指与拇指捏住燃气灶旋钮，逆时针缓慢拧动，随着旋钮转动的动作，灶眼上升起稳定的蓝色火焰。右手拿起油壶倒极少量油入锅，仅够在锅底薄薄铺开一层油膜，看不到明显的液态油面，把油壶放回原位。<br/>右手从小白瓷碗中稳稳捏起鸡蛋，横移到锅口上方。镜头缓慢推近到鸡蛋和锅沿的近景特写，右手把鸡蛋侧面在锅沿上轻轻磕一下，能明显看到蛋壳接触锅沿、蛋壳出现横向裂缝、边缘微微翘起；左手过来，双手拇指和食指分别捏住两半蛋壳向两侧掰开，蛋液滑入锅中，蛋清凝固泛白，蛋黄居中。镜头缓慢拉回原机位。双手把两半空蛋壳分别放到灶台右侧一角，并排摆放。<br/>机器人左手握住锅柄稳住锅，右手拿起木柄锅铲，用铲头轻轻推推蛋边整理形状；此时锅中煎蛋朝上的一面是白色蛋清覆盖着一颗凸起的完整黄色蛋黄。等蛋底部凝固后，铲头从蛋底整体铲起，把煎蛋向上一抛并翻面，蛋落回锅中；翻面之后朝上的一面是均匀的浅金黄色、表面平整、边缘微焦，蛋黄被压在下方看不见；翻面完成后煎蛋保持这一面朝上继续在锅中煎一小会，机器人不再做第二次翻面。<br/>现代开放式厨房，浅灰色橱柜，晨光从右侧窗户照入，暖调。第三人称固定广角中景，机位在灶台正前方稍高处；仅磕蛋掰壳时镜头缓慢推近做近景特写，随后拉回原机位，一镜到底。声音：旋钮拧动的轻微咔哒声、点火 "啵" 声、蛋壳磕锅沿的清脆响声、油煎持续滋滋声、锅铲金属摩擦声。</code></pre></td><td><figure view-type="Preview"><source name="ed5898f71876445cab73e5e9946ea793_a=0&amp;ch=0&amp;cr=0&amp;dr=0&amp;er=0&amp;lr=default&amp;&amp;br=5620&amp;bt=5620&amp;cs=0&amp;ds=3&amp;mime_type=video_mp4&amp;qs=13&amp;rc=amVvZWdvOmRnPDczNGllM0BpamVvZWdvOmRnPDczNGllM0BuNjZwYWEvc2VhLS1kXzBzYSNuNjZwYWEvc2VhLS1kXzBzcw%3D%3D&amp;cquery=102y (1).mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="14181493" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>



### 3D 资产产品演示   // 全模态参考

> 专业级 3D 白模 + 材质参考原样承接，生成结构功能演示

<table><colgroup><col/><col/></colgroup><thead><tr><th>Prompt</th><th>Seedance 2.5 生成结果</th></tr></thead><tbody><tr><td><pre caption="Prompt&#xA;" lang="Python" wrap="true"><code>产品是@图片1,产品组装内容是@图2@图片3,帮我生成一条工业安装视频,画面要统一,步骤要清晰,组装要有逻辑。</code></pre></td><td><figure view-type="Preview"><source name="无人机.mp4" mime="video/mp4" origin-height="2160.000000" origin-width="3840.000000" size="87682671" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>



### 合成机器人训练数据  // 全模态参考

<table><colgroup><col/><col/></colgroup><thead><tr><th>Prompt</th><th>Seedance 2.5 生成结果</th></tr></thead><tbody><tr><td><pre caption="&#xA;" lang="Python" wrap="true"><code>修改@视频1,将左侧机械臂和夹爪替换为@图片1中的银色机械手;<br/>将抓取的物品替换为一片全麦吐司;将原本的绿色墙面和蓝色桌替换为干净的白灰色工业实验室环境,背景有金属设备架、灰白工作台和白色实验室灯光。</code></pre></td><td><figure view-type="Preview"><source name="2880717718774482505.mp4" mime="video/mp4" origin-height="1080.000000" origin-width="1920.000000" size="7364337" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>



## 4.5 ｜ 多元场景 🌐

### 人物多场景穿梭 

<table><colgroup><col/><col/><col/></colgroup><thead><tr><th>Prompt</th><th>参考素材</th><th>Seedance 2.5 生成结果</th></tr></thead><tbody><tr><td><pre caption="&#xA;" lang="Plain Text" wrap="true"><code>一镜到底，镜头平稳跟随一个穿黑色大衣的人，参考【图片1】，从左向右穿过六个相连的不同色调、不同氛围的房间。每个房间结构相同：白墙、人字拼浅色木地板、法式双开落地窗、白纱帘，参考【图片2】但窗外风景和室内氛围完全不同。主角全程匀速走动，穿过墙壁上敞开的每一扇门。<br/>0-5秒，第一个房间，主题为美漫打斗，主角进入屋内与人物【图片3】打斗，人物落败；<br/>5-10秒，第二个房间，主题为温暖，毛毡风格，窗外场景为向日葵田【图片4】，室内光线暖橙柔光，有一个画家正在画向日葵【图片5】。主角进入后也变成毛毡风格；<br/>10-15秒，第三个房间，主题为悲伤，整个画面为黑白漫画定格动画风格，窗外阴雨，室内光线冷灰低沉，一个人独自坐在空房间中央地板上，低头抱膝，身旁一只手机亮着无人接听的通话界面。主角进入房间后关上房间的灯，马上开灯，房间内变为彩色，瞬间生长出满屋鲜花；<br/>15-20秒，第四个房间，主题为欢乐，整个场景为浸泡在海里的房间，参考【图片6】，主角游进房间，身旁有美丽的珊瑚礁和鱼群；<br/>20-25秒，第五个房间，主题为惊喜，窗外场景漫天烟花夜空，参考【图片7】，室内光线彩色闪烁映射，主角被卷入欢呼气氛。<br/>25-30秒，最后主角来到一个空白房间，站在中央打了个响指，同时音效为响指声。<br/>整体电影质感，高级时装广告风格，光线完全由窗外场景决定形成强烈情绪反差，画面无文字。</code></pre></td><td><grid><column width-ratio="0.333333"><img name="reference1.png" alt="这张图片出现在《实践手册》中“人物多场景穿梭”的相关内容里，作为对应的参考素材呈现。图片主体是一位有着浅棕色头发、面部带有浅须的男性，他身着黑色翻领毛呢大衣，背景为纯白色。该图片是配合多元场景应用下的人物多场景穿梭需求，作为Seedance 2.5生成相关内容时的参考素材使用，和该手册中介绍的企业级业务多元场景实践的内容相呼应。" mime="image/png" scale="0.386243" src="H2hhbKRUioZWHBxSzf2ciiYYnzh"/></column><column width-ratio="0.333333"><img name="bfj.png" alt="这张图片对应的是手册中人物多场景穿梭功能的参考素材，呈现的是一处室内空间：房间的地板是人字拼样式的浅色木地板，墙面为纯白色，正中央的窗户挂着半透明的白色窗帘，两侧分别是白色的开放式门和带玻璃格的白色门框，整体是简洁明亮的家居场景。该素材用于演示Doubao-Seedance 2.5在人物多场景穿梭场景下的制作参考，对应的生成结果可通过链接查看。" mime="image/png" scale="0.386243" src="Qmu5bOfBboOzjMxv5gtcOqf1nWd"/></column><column width-ratio="0.333333"><img name="image.png" alt="图片展示了一位穿着时尚的男性角色。他身着一件色彩斑斓的风衣，内搭黄色衬衫，下身是蓝色带有图案的裤子，腰间系着皮带，脚边放着一个行李箱。角色有着黑色短发，面带微笑，整体造型充满未来感与科技感，与上下文提到的“人物多场景穿梭”及“多元化场景”相契合，体现了角色在不同场景中的多变形象。" mime="image/png" scale="0.386243" src="PMQYbqg1oo0R4bxD1Xmcs47enYd"/></column></grid><grid><column width-ratio="0.250000"><img name="image.png" alt="图片展示了一片向日葵田，背景是蓝天白云。向日葵花朵呈黄色，花心为棕色，花瓣边缘有绿色的花蕊。向日葵茎部为绿色，叶子呈椭圆形。画面整体色彩鲜艳，给人一种生机勃勃的感觉。该图片与文档中“人物多场景穿梭”应用场景相关，可能用于体现多元化场景的视觉效果，或作为参考素材展示相关内容。" mime="image/png" scale="0.386243" src="UA6FbzwjaonxPLxAiX9cO7sYneG"/></column><column width-ratio="0.250000"><img name="image.png" alt="图片展示了一位艺术家正在创作的场景。艺术家戴着黑色帽子，留着红色络腮胡，穿着蓝色外套和黄色内衬。他手持画笔，正在画架上绘制一幅向日葵的画作。画作背景为浅蓝色，画面中有一束黄色的向日葵，花瓶为粉色。该图片与文档中“人物多场景穿梭”应用场景相关，展示了Doubao-Seedance 2.5在生成人物场景方面的应用效果。" mime="image/png" scale="0.386243" src="IwDubCEzPo0YgjxXN9HcqvfCnlc"/></column><column width-ratio="0.250000"><img name="image.png" alt="这张图片呈现了水下场景，将原本室内的空间替换为海底环境，原本的建筑门框、走廊结构仍保留，整个空间被海水覆盖，顶部可见水面透出的光线，海底分布着色彩丰富的珊瑚、海草与沙地，是Seedance 2.5生成的人物多场景穿梭相关素材，对应文档中人物多场景穿梭的多元场景实践展示内容，体现了将室内空间切换为海洋场景的创意效果。" mime="image/png" scale="0.386243" src="MrP3bwhrYon48AxWypeclMgMnYc"/></column><column width-ratio="0.250000"><img name="image.png" alt="这是一张呈现于深蓝色夜空背景下的烟花照片，画面中有两款不同形态的烟花。左侧为放射状的金色烟花，线条规整、舒展，右侧是绽放得更为繁茂的粉红色烟花，色彩鲜亮，两种烟花在暗背景的衬托下视觉效果醒目，符合文档中提及的人物多场景穿梭相关的多元场景展示要求，是Seedance 2.5生成结果的参考素材。" mime="image/png" scale="0.386243" src="UhZ1bi0rMooWHVxx8NycEYVMngd"/></column></grid></td><td><figure view-type="Preview"><source name="石榴引入 0622.mp4" mime="video/mp4" origin-height="1080.000000" origin-width="1920.000000" size="62705422" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>





### 拟人化 IP 角色片  

> 拟物角色与真实场景无缝融合，形象、动作、口音全程统一，把想象里的角色搬进现实剧情。

<table><colgroup><col/><col/></colgroup><thead><tr><th vertical-align="top"> Prompt</th><th vertical-align="top">Seedance 2.5 生成结果</th></tr></thead><tbody><tr><td vertical-align="top"><pre caption="Prompt&#xA;" lang="Python" wrap="true"><code>中景画面中，拟人化向日葵组成一支特色花植乐队，植株整齐排布。温暖阳光倾泻而下，金黄花瓣在光影下明艳亮眼。微风掠过花丛，花叶轻晃，传来细碎沙沙声响。 队伍前方的向日葵面前架设立式麦克风，它用右“手”叶片下压麦克风调整成适合的高度，用低沉柔和的英式口音说：“伙伴们，让我们用歌声传递美好。” 其余向日葵各自持有不同乐器，开始演奏各自的乐器：有的向日葵用叶片敲打着圆鼓，有的背着吉他，还有的搭配吹奏类乐器，各司其职默契配合。领头向日葵摆正身形，正对立麦，伸长叶片在头顶卡着节奏拍手，准备开启演唱。</code></pre></td><td vertical-align="top"><figure view-type="Preview"><source name="c34c11911002420abe0398739c8dae6e_a=0&amp;ch=0&amp;cr=0&amp;dr=0&amp;er=0&amp;lr=default&amp;&amp;br=5413&amp;bt=5413&amp;cs=0&amp;ds=2&amp;mime_type=video_mp4&amp;qs=13&amp;rc=ajM2bTNrb2lkPDczNGllM0BpajM2bTNrb2lkPDczNGllM0Axb2ZwcWdeYDVhLS1kXzBzYSMxb2ZwcWdeYDVhLS1kXzBzcw%3D%3D&amp;cquery=102y&amp;dy_.mp4" mime="video/mp4" origin-height="480.000000" origin-width="854.000000" size="10422895" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>

<table><colgroup><col/><col/></colgroup><thead><tr><th vertical-align="top"> Prompt</th><th vertical-align="top">Seedance 2.5 生成结果</th></tr></thead><tbody><tr><td vertical-align="top"><pre caption="Prompt&#xA;" lang="Python" wrap="true"><code>美国西部片风格。烈日黄沙小镇，一只戴迷你牛仔帽、穿流苏皮马甲的橘猫推门而入，门轴“吱呀”一声带起尘土。镜头立刻快推：站在吧台后擦杯子的络腮胡老板，看到橘猫后手一抖，杯子碎落在地；角落三位牛仔同时转头，嚼烟草的嘴定格，特写他们瞪大的眼珠子与抽动的胡茬，背景配“嗖嗖”三声鞭梢抽风特效。镜头回到橘猫中景，它用后爪蹬了蹬木地板的灰尘，抬下巴，奶凶却拖长调子带着美式口音：“鲜奶，兄弟。没人出来迎我一下吗?” 全场静半秒，随即牛仔们齐刷刷摘下帽子，发出“哇哦——”拉长惊叹，口琴滑音上扬。镜头360°环绕橘猫拍摄，展现它走向吧台，跳上长脚凳后傲娇的小表情。</code></pre></td><td vertical-align="top"><figure view-type="Preview"><source name="c150e9331e7745fbac9ef40876fc3f91_a=0&amp;ch=0&amp;cr=0&amp;dr=0&amp;er=0&amp;lr=default&amp;&amp;br=10999&amp;bt=10999&amp;cs=0&amp;ds=3&amp;mime_type=video_mp4&amp;qs=13&amp;rc=amQ5bTNrb25lPDczNGllM0BpamQ5bTNrb25lPDczNGllM0BrNmZwcWdeMzVhLS1kXzBzYSNrNmZwcWdeMzVhLS1kXzBzcw%3D%3D&amp;cquery=102y&amp;d.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="28248197" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>



### 舞蹈动作迁移

> 以真人舞者动作视频作为参考，将动作精准迁移到目标角色身上：动作轨迹、节拍与肢体细节高度对齐，同时保留敦煌造型的服饰、发饰与身法韵律。

<table><colgroup><col/><col/><col/></colgroup><thead><tr><th vertical-align="top"> Prompt</th><th>参考素材</th><th vertical-align="top">Seedance 2.5 生成结果</th></tr></thead><tbody><tr><td vertical-align="top"><pre caption="Prompt&#xA;" lang="Python" wrap="true"><code>参考@视频1中的人物动作，生成在莫高窟前穿着敦煌元素服饰的舞蹈视频。</code></pre></td><td><figure view-type="Preview"><source name="f092d03b8048405c8b6eeb1c18a6c797_a=0&amp;ch=0&amp;cr=0&amp;dr=0&amp;er=0&amp;lr=default&amp;&amp;br=7997&amp;bt=7997&amp;cs=0&amp;ds=3&amp;mime_type=video_mp4&amp;qs=13&amp;rc=amc0bWZrb2hlPDczNGllM0Bpamc0bWZrb2hlPDczNGllM0A1ajFscWdeaF5hLS1kXzBzYSM1ajFscWdeaF5hLS1kXzBzcw%3D%3D&amp;cquery=102y&amp;dy_.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="20538601" token="[媒体标识已移除]"/></figure></td><td vertical-align="top"><figure view-type="Preview"><source name="aee8598793094fe3ab0e710924ced536_a=0&amp;ch=0&amp;cr=0&amp;dr=0&amp;er=0&amp;lr=default&amp;&amp;br=14250&amp;bt=14250&amp;cs=0&amp;ds=3&amp;mime_type=video_mp4&amp;qs=13&amp;rc=anBsNzNrbzl5PDczNGllM0BpanBsNzNrbzl5PDczNGllM0A2L2JlcWcvNF5hLS1kXy9zYSM2L2JlcWcvNF5hLS1kXy9zcw%3D%3D&amp;cquery=102y&amp;d.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="36597845" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>

### 动画镜头渲染

<table><colgroup><col/><col/></colgroup><thead><tr><th vertical-align="top"> Prompt</th><th vertical-align="top">Seedance 2.5 生成结果</th></tr></thead><tbody><tr><td><pre caption="&#xA;" lang="Markdown" wrap="false"><code>### 分镜1（0:00-0:02.5）<br/>【运镜】镜头从散落一地的毛线球与猫玩具之间低机位缓缓滑行，穿过桌腿后发现一名渺小骑士正抱着一罐金属猫罐头，小心翼翼向客厅深处前进。镜头继续跟随骑士绕过障碍，直到巨大的猫王座逐渐映入画面，庞大的猫正闭眼沉睡，压迫感扑面而来。【转场】镜头不停机，骑士继续前进自然进入下一镜。<br/><br/>### 分镜2（0:02.5-0:05）<br/>【运镜】镜头绕到骑士侧前方缓慢推进，骑士停下脚步，将猫罐头轻轻放在地面，双手缓缓推向巨猫方向。镜头越过猫罐头继续向前，焦点逐渐转移到巨猫脸部。猫鼻尖微微抽动，耳朵轻轻转动，空气仿佛安静下来。【转场】镜头继续推近猫鼻尖，无剪辑衔接。<br/><br/>### 分镜3（0:05-0:07.5）<br/>【运镜】超近景停留在猫鼻子与胡须，随着一次轻微吸气，胡须微微颤动。镜头缓慢抬升来到猫眼，一只眼睛缓缓睁开，瞳孔迅速收缩锁定远处那罐食物。镜头顺着猫视线快速拉远，看见远处的骑士已经开始缓缓后退。【转场】利用猫眼中的倒影Match Cut切到动作镜。<br/><br/>### 分镜4（0:07.5-0:10.5）<br/>【运镜】镜头突然高速后撤，巨大的猫身体猛地跃起冲向前方，镜头险些被扑倒，骑士立刻转身逃跑。摄影机贴地跟拍，两者高速穿梭于猫爬架、纸箱和家具之间，猫的巨爪不断从镜头上方掠过，带来强烈压迫感。【转场】骑士钻进纸箱，镜头跟着冲入黑暗。<br/><br/>### 分镜5（0:10.5-0:13）<br/>【运镜】镜头从纸箱另一侧冲出，发现骑士已经躲在角落喘息。镜头慢慢升起，只见那只巨猫根本没有追他，而是趴在刚才的位置，正专心致志地用两只前爪抱着猫罐头，开心地不停舔食，完全沉浸其中。【转场】镜头缓慢推向骑士视角。<br/><br/>### 分镜6（0:13-0:15）<br/>【运镜】镜头从骑士身后缓缓推近，他轻轻站起，看向远处毫无防备、沉迷吃罐头的巨猫。骑士绕过它的身后，继续朝王座更深处走去，镜头缓缓升高，露出王座后方隐藏着一扇通往巨大宫殿深处的门。骑士的身影越来越小，画面停留在巨猫依旧认真吃着罐头，而真正的冒险才刚刚开始。</code></pre></td><td><figure view-type="Preview"><source name="白模.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="21642178" token="[媒体标识已移除]"/></figure></td></tr><tr><td><pre caption="&#xA;" lang="Markdown" wrap="true"><code>将视频画面渲染为电影级质感，消除建模布线，保持原本的运镜和画面。渲染成精致的动画大片风格，彩色的动画电影，毛茸茸的猫咪。</code></pre></td><td><figure view-type="Preview"><source name="6a58d7a02e684a7cb805247d564fda69_a=0&amp;ch=0&amp;cr=0&amp;dr=0&amp;er=0&amp;lr=default&amp;&amp;br=20157&amp;bt=20157&amp;cs=0&amp;ds=3&amp;mime_type=video_mp4&amp;qs=13&amp;rc=ajdvaTNrb21tPDczNGllM0BpajdvaTNrb21tPDczNGllM0A2YmNncWcvZzRhLS1kX2FzYSM2YmNncWcvZzRhLS1kX2.mp4" mime="video/mp4" origin-height="720.000000" origin-width="1280.000000" size="38831092" token="[媒体标识已移除]"/></figure></td></tr></tbody></table>



# 五、快速上手指南



## 5.1｜开通门槛及调用价格

- 免费额度：Seedance 2.5 模型 **没有**免费额度。
- Seedance 2.5 开通门槛 与 2.0 系列模型一致，开通前，请确保**满足以下任一条件** ：

  - 账户余额 > 200 元（[前往充值](https://console.volcengine.com/finance/fund/recharge?_vtm_=a106466.b106468.0_0.0_0.0.1086_7646310968578557482)）
  - 已购买Seedance 2.0 或 2.5 系列的资源包，且资源包有余量



- 模型价格

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td>模型</td><td colspan="2">在线推理 元/百万token</td></tr><tr><td>doubao-seedance-2.5<blockquote><p>按输入是否包含视频区分定价</p></blockquote></td><td><ul><li>输出视频分辨率为 480p，720p<ul><li>输入不含视频：<b>70.00</b></li><li>输入包含视频：<b>42.00</b></li></ul></li></ul></td><td><ul><li>输出视频分辨率为 1080p<ul><li>输入不含视频：<b>77.00</b></li><li>输入包含视频：<b>46.00</b></li></ul></li></ul></td></tr><tr><td colspan="2"> 请关注<a href="https://www.volcengine.com/docs/82379/1544106?redirect=1&amp;lang=zh#02affcb8">火山引擎官方价格文档</a></td><td></td></tr></tbody></table>



## 5.2｜提示词指南

<callout emoji="🎹"><p><cite doc-id="Tvdtw2Xlpi1dSokYL2fcY9akneb" file-type="wiki" title="Seedance 2.5 多模态生视频使用指南" type="doc"></cite></p></callout>

## 📚 任务使用说明

Seedance 2.5 从传入素材最终是否会锁定输出视频的属性，把任务区分为两类（Seedance 2.0没有这个区分）：

- 有锁定：素材会严格成为输出视频时间轴上的一段，是模型输出去适应传入的素材，因此会锁定输出视频的宽高比、甚至时长；

  <table><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th vertical-align="top"><b>任务类型</b></th><th vertical-align="top">任务详细定义</th><th vertical-align="top">对输出视频锁定的说明</th><th vertical-align="top">触发关键词</th></tr></thead><tbody><tr><td vertical-align="middle"><b>视频编辑</b></td><td vertical-align="middle">输入视频，要求对视频的画面或音频进行增删改等编辑操作，支持额外输入图片/视频/音频引导编辑结果</td><td vertical-align="middle"><ul><li><b><u>锁定输出视频的宽高比</u></b><u>，严格对齐用户输入视频的宽高比；参数ratio 必须等于 adaptive</u></li><li><b><u>锁定输出视频的时长</u></b><u>，*基本对齐*用户输入视频的时长，参数duration 必须为 </u><b><u>-1</u></b><p>受模型输入帧处理机制影响，输出视频时长可能与输入存在轻微差异（最大约 0.3 秒），但只是部分过渡帧被压缩，输出视频内容*基本对齐*输入、保持完整/不变</p><p>如果使用seedance 2.5生成的视频作为编辑输入，输出时长不会有差距</p></li><li>建议<b>output_format</b>使用mov格式</li></ul></td><td vertical-align="middle"><b>编辑视频</b>、增加/加上、删除/去掉、修改/替换/改成...或其他相关描述<blockquote><p>@video1 中加一些小动物；把 @video1 的人物修改为 @image1；删掉 @video1 的背景音乐</p></blockquote></td></tr><tr><td vertical-align="middle"><b>首帧/首尾帧</b></td><td vertical-align="middle">输入 1 张图作为首帧生成视频/I2V，或输入 2 张图分别作为首帧和尾帧生成视频</td><td vertical-align="middle"><ul><li><b><u>锁定输出视频的宽高比</u></b><u>，严格对齐用户输入视频的首帧图；参数ratio 必须等于 adaptive</u><ul><li>如果输入尾帧与首帧画幅不一致，尾帧会被拉伸，因此建议输入画幅一致的首帧和尾帧</li></ul></li><li>时长，支持用户自定义</li></ul></td><td vertical-align="middle">通过 content.role  取值控制，需设置为 first_frame/last_frame</td></tr><tr><td vertical-align="middle"><b>视频延长</b></td><td vertical-align="middle">输入视频进行向前/向后延长， 通过 prompt 描述延长生成的内容，支持额外输入图片/视频/音频</td><td vertical-align="middle"><ul><li><b><u>锁定输出视频的宽高比</u></b><u>，严格对齐用户输入视频的宽高比；参数ratio 必须等于 adaptive</u></li><li>时长，支持用户自定义</li><li>建议<b>output_format</b>使用mov格式</li></ul></td><td vertical-align="middle">向前/向后延长、延续、续写...或其他相关描述<blockquote><p>向后延长 @video1，@image1 的角色从天而降...; 续写 @video1 前 5s， @video2 女人入画说...</p></blockquote></td></tr></tbody></table>
- 无锁定：仅对素材进行语义上的参考，因此用户可以指定输出视频的宽高/时长属性。基本上所有的参考类任务对于输出视频的宽高比和时长都没有来自输入素材的锁定，其中有两类需要注意也是没有锁定的：

  <table><colgroup><col/><col/><col/></colgroup><thead><tr><th vertical-align="middle"><b>R2V 能力</b></th><th vertical-align="top">推理策略说明</th><th vertical-align="top">示意图</th></tr></thead><tbody><tr><td vertical-align="middle"><b>多宫格分镜/故事板</b></td><td vertical-align="middle"><ul><li><b>生成画面不是严格对齐分镜图：</b>输入多宫格分镜图（即多个分镜合并在一张图）， 生成视频画面不会严格对齐分镜图（比如分镜中具体的画面细节），分镜图主要提供大致的剧情参考</li><li><b>推荐使用相对简约的线稿分镜图</b>， 并通过 prompt 补齐分镜图中没有的信息（如动作、运镜和风格等基础信息）</li></ul></td><td vertical-align="middle"><img name="image.png" alt="图片展示了一组漫画分镜图，共六格画面。画面中，一位长发女子与一位男子在室内对话，女子手持书本，男子神情专注。画面背景为室内场景，有窗户、桌椅等。画面下方标注了景别、视角、构图、运镜等信息，如“景别：全景 视角：平视 构图：三分构图 运镜：固定镜头”等。该图片与文档中“多宫格分镜/故事板”部分内容相关，用于说明生成画面不严格对齐分镜图，可推荐使用相对简约的线稿分镜图。" mime="image/png" scale="1.000000" src="Z00ubu76xowmwSxNv75czCzWn8d"/><br/>多宫格分镜图</td></tr><tr><td vertical-align="middle"><b>关键帧</b></td><td vertical-align="middle"><ul><li><b>生成画面对齐关键帧</b>：将多张独立的分镜图（可能包含首/尾帧分镜图）作为关键帧输入， 生成视频画面相对严格对齐输入图</li><li>时长，支持用户自定义</li></ul></td><td vertical-align="middle"><grid><column width-ratio="0.142850"><img name="image.png" alt="图片展示了一幅色彩斑斓的山水画。画面中，一座古色古香的楼阁坐落在山巅，周围环绕着绿树和红顶建筑。山间云雾缭绕，山脚下有蜿蜒的河流，河中有一艘小船。画面左侧有一条飞舞的鱼，其身体呈蓝紫色，尾部有红色斑点。山间和水中有许多彩色的花瓣状图案，整体色调柔和，充满梦幻色彩，与上下文介绍的多宫格分镜/故事板生成画面不严格对齐分镜图的内容相契合。" mime="image/png" scale="0.475260" src="UAHdb35VnoMMXTxJBHPcpilmnYb"/></column><column width-ratio="0.142850"><img name="image.png" alt="图片展示了一幅色彩斑斓的插画，画面中有一座建在山坡上的古色古香的建筑群，建筑以红色和白色为主，屋顶为黄色。山坡上分布着许多房屋，房屋的屋顶和墙面色彩丰富，有红色、蓝色等。山坡两侧有茂密的树木，远处是连绵的山脉，山间云雾缭绕。画面整体色调柔和，充满了梦幻与诗意，与上下文介绍的多宫格分镜/故事板生成画面不严格对齐分镜图，推荐使用相对简约线稿分镜图等内容相契合。" mime="image/png" scale="0.475260" src="PeUYbFfO8oVw0ox5dOkcVMjBnDg"/></column><column width-ratio="0.142901"><img name="image.png" alt="这是一张多宫格分镜图，画面中以蓝天为背景，中心是一座飞檐翘角的多层中式塔楼，旁侧还有一座欧式风格的尖顶教堂，二者坐落于错落有致的建筑群中，建筑周边点缀着松树与花卉。画面下半部分布满了大量色彩丰富、样式各异的圆形图案，类似带有精美纹样的传统油纸伞，整体融合了中式与欧式的建筑风格，风格偏向简约线稿风，可作为分镜参考的素材，契合多宫格分镜任务对简约线稿分镜图的使用要求，用于为生成视频提供大致的剧情参考。" mime="image/png" scale="0.570312" src="LUYMbuxEookB7Ox0IbFcBLKjnRd"/></column><column width-ratio="0.142850"><img name="image.png" alt="图片展示的是一个中式风格的室内场景。画面中央有一个圆形水池，池边摆放着几只花纹瓷瓶。室内装饰精美，有木质桌椅，桌上摆放着花瓶等物品。窗边有盆栽绿植，窗外是山峦和湖泊，远处有云雾缭绕。室内悬挂着灯笼，墙上挂有画作，地面铺有地毯，整体色调柔和，光线从窗外洒入，营造出宁静雅致的氛围。此图可能用于说明多宫格分镜或关键帧生成画面的参考示例。" mime="image/png" scale="0.475260" src="A4d7b5Iwnoa352xluvPcBPIpn7d"/></column><column width-ratio="0.142850"><img name="image.png" alt="图片展示的是一个中式风格的室内场景。画面中央是一个圆形水池，池边摆放着几只青花瓷瓶。室内装饰精美，有木质桌椅、花瓶等，桌上摆放着绿植。窗边有盛开的粉色樱花，窗外是山峦和云雾缭绕的景色。天花板上悬挂着一个圆形灯笼，整体色调柔和，光线从窗外透入，营造出宁静雅致的氛围。此图可能用于说明多宫格分镜或关键帧生成画面时的参考场景。" mime="image/png" scale="0.475260" src="PWq2b2Hjyo4OVkxrZ6rcyE5ynge"/></column><column width-ratio="0.142850"><img name="image.png" alt="图片展示了一个室内场景，中央是一个圆形水池，池中有一条色彩斑斓的锦鲤在游动。水池周围摆放着多盆绿植和花瓶，地面铺有花纹瓷砖。背景是窗户，窗外是山峦和河流，画面整体色调柔和，具有传统中式风格。该图片与文档中关于多宫格分镜/故事板的说明相关，作为示意图，用于说明输入多宫格分镜图（即多个分镜合并在一张图）时，生成视频画面不会严格对齐分镜图，分镜图主要提供大致的剧情参考。" mime="image/png" scale="0.475260" src="RTQebKhYaoE24kxiCMBcV7Ihnsb"/></column><column width-ratio="0.142850"><img name="image.png" alt="这是一张与指南中“多宫格分镜图”示例相关的图片，画面呈现石质古寺室内场景，一位身着僧衣的老者背对观者，正望着面前的大幅画作。画作内是中式传统雅致厅堂，厅堂中央有圆形水池，布局贴合中式风格，周边点缀花瓶、盆栽、窗棂等元素，厅堂外可见开阔景致，画作两侧配有书法楹联。这一示例对应指南中关于多宫格分镜的说明，体现了参考类任务中分镜图需提供大致剧情、作为内容创作参考的作用。" mime="image/png" scale="0.475260" src="FEkFbB3iAoBskUxQmftchujynSf"/></column></grid><br/>多张独立的分镜图/关键帧</td></tr></tbody></table>



## ✍️ Prompt 写作建议

<callout emoji="💡">
**把 Seedance 2.5 当作一个视觉内容生产者，用导演的思维书写 [ 结构化 Prompt ]** 
</callout>

### 基础写作

**`（R2V）素材指代`**

明确每个图/视频/音频的编号（按照上传顺序） 与用途（谁是形象、谁是音色、谁是动作、谁是场景...) 

**`一句话概述`**

主体 + 地点 + 事件 + 题材/风格 + 特殊运镜...

**`具体情节描述`**

镜头顺序/时间轴（均可）：用时间戳或"镜头 N"切分，逐段描述画面具体内容、运镜、动作、台词、音效等， 尽量使用正向描述 ； 

反向描述支持 : 字幕、音频控制 ， 比如“不要字幕”，“不要 bgm”

**`结尾`**

补充说明一些贯穿始终的画面细节， 比如机位/运镜， 环境/场景， 声音， 氛围等

<grid><column width-ratio="0.500000"><pre caption="案例示意&#xA;" lang="Plain Text" wrap="true"><code>写实自然纪录片风格，电影级真实光影，温暖的午后, 在森林草坡上, 一只圆滚滚的熊猫幼崽从坡上滚下来. <br/><br/>熊猫黑白毛发蓬松真实，体型小而胖，动作笨拙可爱。场景为绿色森林斜坡，地面覆盖青草、苔藓、三叶草、泥土、小石块、枯枝和少量小黄花，虚化背景中有高大树干与树林。镜头为低机位中远景，轻微手持感，整体基本固定，始终保持熊猫在画面中。<br/><br/>0s-3s：一只熊猫幼崽趴在绿色草坡上，身体圆滚滚, 它刚开始顺着斜坡慢慢侧滚，动作笨拙，草叶被身体轻轻压弯。微风拂过, 阳光从左上方穿过树林，形成斑驳光影。<br/>3s-8s：熊猫滚到画面右下方，动作逐渐停止，从侧躺变成趴卧。它的圆脸朝向镜头，前爪压在草地上，熊猫趴在前景草丛中，身体调整到舒服的姿势，头部小幅抬起又放低, 发出轻微哼唧声。<br/><br/>低机位，轻微手持感，轻微跟随熊猫向右下方移动。景深自然，前景草叶轻微虚化，熊猫主体清晰，背景树林柔和虚化。自然环境音，风声、熊猫滚动时轻微柔软的扑通声, 整体温暖、真实、自然。</code></pre></column><column width-ratio="0.500000"><readonly-block href="[媒体访问链接已移除]" type="iframe"></readonly-block></column></grid>

<table><colgroup><col/><col/><col/></colgroup><thead><tr><th vertical-align="middle"><b>类型</b></th><th colspan="2" vertical-align="top"><b>写法要点</b></th></tr></thead><tbody><tr><td rowspan="4" vertical-align="middle"><b>参考类</b><br/><b>（多素材映射）</b></td><td colspan="2" vertical-align="top">参考素材变多后， <b><u>素材的映射和指代关系说明非常重要</u></b><br/>按照上传素材的顺序对应编号（图 1 / 视频 1 / 音频 1），每个素材进行文本绑定 ， <b>不建议只在图片里呈现映射信息</b>， 比如主角图片上写“张三”， 然后 Prompt 中直接写“张三在学校里 xxxx”， 容易导致多人混淆或重复角色</td></tr><tr><td vertical-align="top">🌟多主体逐一列清映射关系， 人数多时用清单罗列，避免混淆。</td><td vertical-align="top"><em>"图 1 的侠客"</em><br/><em>"img1-2 是人物 1，对应音频 1 ； img3-4 是人物 2， 对应音频 2"</em><br/><em>"图片 1 是主角张三， 图片 1 使用音频 1 音色"</em></td></tr><tr><td vertical-align="top">🌟分工要具体到"参考什么"， 如果是部分参考， 要写明"参考哪一部分"</td><td vertical-align="top"><em>"参考视频 1 中施法的动作， 视频 2 的环绕式运镜"</em><br/><em>"参考图片 1 的光影和滤镜"</em></td></tr><tr><td vertical-align="top">🌟当参考素材本身已足够精准时，建议只做 "指代"、减少画面复述。</td><td vertical-align="top"><em>"严格参考视频 1 的动作与运镜， 顺序与视频保持一致" </em>（不需要在 prompt 中写 "先抬手、再转身、镜头缓慢环绕……"等等具体细节， <em>不必额外描述</em>）</td></tr><tr><td vertical-align="middle"><b>编辑类</b></td><td vertical-align="top">明确需要修改的范围和内容， 可以配合时间戳进行部分编辑， 尽可能说明修改内容从 A-&gt;B 的过程</td><td vertical-align="top"><em>"仅编辑视频 1 中男人的台词， 修改为 「你不要过来啊」， 口音调整为东北口音…"</em><br/><em>"把视频 1 中 4-6 秒男人喝咖啡的动作改变为拖地， 其余内容不要变化"</em><br/><em>"编辑任务： 把视频 1 中右侧的亚洲女生改为图片 1 中的黑人女生"</em></td></tr><tr><td vertical-align="middle"><b>首尾帧</b></td><td vertical-align="top"><ul><li>优先使用参数设置图片的role为：first_frame/last_frame; 注意此方式会<b><u>锁定输出视频的宽高比，严格对齐用户输入视频的首帧图</u></b></li><li>也支持设置 role 为 reference_image，在 prompt 中指定具体图片为首帧&amp;尾帧。注意此方式<b><u>不会锁定输出视频的宽高比，视频效果与首帧&amp;尾帧参考图相近,但不完全匹配</u></b>。</li></ul></td><td vertical-align="top"><em>"图片 1 为首帧"</em><br/><em>"图片 3 为首帧， 图片 5 为尾帧"</em></td></tr><tr><td rowspan="4" vertical-align="middle"><b>时间戳</b></td><td colspan="2" vertical-align="top">时间戳可以更好的理清故事剧情发展， 以“1 秒”为单位<ul><li>指定时间段内剧情如果较少， 模型会进行一定自由发挥 ； </li><li>指定时间段内容过多， 则会导致过度剪切或剧情遗漏， 请注意时长安排的合理性</li><li>不建议用时间戳控制频率/频次， 比如“一秒摇头 3 次”</li></ul></td></tr><tr><td vertical-align="top">🌟支持明确的时间区间<br/> [ 注意时间轴的连续性， 避免出现"0-3 秒...5-6 秒..."表达 ] </td><td vertical-align="top"><em>"0-3 秒......3-7 秒.....7-15 秒"</em><br/><em>"[1s-4s]....[4s-8s]....[8s-12s]"</em></td></tr><tr><td vertical-align="top">🌟支持时间点控制</td><td vertical-align="top"><em>"第 5s 快速向左横移转场"</em><br/><em>"第 2 秒一道金雷能量自画面顶部破空直落..."</em></td></tr><tr><td vertical-align="top">🌟支持相对时间控制</td><td vertical-align="top"><em>"张三呆滞的站在原地， 3 秒后周围的人纷纷摇头。"</em><br/><em>"....主角按下快门后画面定格 1 秒"</em></td></tr><tr><td rowspan="2" vertical-align="middle"><b>负向控制</b></td><td vertical-align="top">🌟支持负向控制字幕</td><td vertical-align="top"><em>"不额外加入对白字幕"</em><br/><em>"不要字幕"</em></td></tr><tr><td vertical-align="top">🌟支持负向控制音频： <p>支持更细维度的单独控制： 音效、背景音乐（bgm）、对白</p></td><td vertical-align="top"><em>"无 bgm，只生成环境音和动作音"</em><br/><em>"不要任何声音"</em></td></tr></tbody></table>

### 进阶写作

<table><colgroup><col/><col/><col/></colgroup><thead><tr><th vertical-align="middle"><b>类型</b></th><th colspan="2" vertical-align="top"><b>写法要点</b></th></tr></thead><tbody><tr><td vertical-align="middle"><b>镜头语言</b></td><td colspan="2" vertical-align="top"><ul><li>基础的通识性内容可以直接写， 比如景别（大全景/全景/中景/近景/特写）、运镜（推/拉/摇/移/跟/环绕/俯冲/后拉/上摇/手持晃动）、机位（低角度/俯视/第一人称）</li><li>热门的运镜方式可以直接写， 比如一镜到底， 希区柯克变焦， 航拍视角， FPV， 子弹时间， 手持镜头， 回弹变速等</li><li>过于小众、专业的名词需要转换为[名词 + 描述性解释]， 比如 "移焦， 画面焦点发生平滑转变，原本在前景清晰的树木变模糊，背景中的人物由模糊逐渐变得清晰。"</li><li>转场镜头写清触发点与方式。如「第 5s 快速向左横移转场（向左擦除+自然叠化）」， 尽可能把转场时间、方式都写明</li></ul></td></tr><tr><td vertical-align="middle"><b>动作/表情描述</b></td><td colspan="2" vertical-align="top"><ol><li seq="1">动作： 优先用概括性描述（如“连续做了几组高抬腿和空翻”“双方展开近身搏斗”），只在少数有记忆点的动作上写出具体细节，不建议重复写相同的动作。</li><li>表情 :建议写描述性语句， 减少成语使用， 比如“津津有味地吃饭”写为“脸上带着满足的笑容，大口地吃饭”。</li></ol></td></tr><tr><td vertical-align="middle"><b>白模参考/渲染</b></td><td vertical-align="top"><ol><li seq="1">文本中写明希望参考白模视频中的什么元素。例如，输入白模中没有光影变化，只希望参考运镜和运动，写“参考[视频 1]的运镜、动作...”; 如白模有光影变化且需要参考，则写“参考[视频 1]的光影变化和...”. </li><li>如果叠加输入了参考图，需写明参考图和白模的对应关系。如“将[图片 1]中穿灰色衣服的男人对应[视频 1]中的红色模型、[视频 2]中的红发少女替换[视频 1]中的绿色模型 2”。</li><li>输入了白模视频，也<b><u>建议在 Prompt 中详细描述希望生成的视频内容</u></b>，以获得更好的效果，并且注意文本描述需要和白模内容相吻合；对于没有叠加参考图/视频的白模主体，详细描述主体外表/特征效果更佳。</li></ol></td><td vertical-align="top"><em>参考[视频 1]的光影方向及变化，镜头运镜、角色站位和音乐音效，画面节奏生成一段动画。</em><br/><em>将[视频 1]中的粉色模型替换为[图 3]的女孩天野阳菜，灰色模型替换为[图 2]的男孩森岛帆高。背景场景完全使用[图 1]的楼顶天台和天空。</em><br/><em>首先，天野阳菜双手合十闭眼祈祷，阳光从画面左上角逐渐照射到她的脸上和远处的建筑物。随着镜头切换，森岛帆高微微惊讶的发出的{あっ？}向画面右侧转身并吃惊的后仰，他看着画面右上方洒下的阳光，光从画面左下的地面向右上扩散并将男孩衣服照亮。接着全景切换到参考图 1，俩位主角背对镜头，男生展开双臂，惊讶的发出{啊～}。女生保持祈祷的姿势不变。</em><br/><em>新海诚风格的日系动画，光影要有阳光穿透云层的唯美感，画面氛围要充满希望和感动。人物形象严格参考[图 2]和[图 3]，保持全片一致性，不要变脸。音频保持不变，要求高画质、高细节，画面稳定流畅。</em></td></tr><tr><td vertical-align="middle"><b>多宫格分镜/故事板</b></td><td colspan="2" vertical-align="top"><ul><li><b>减少超多分镜输入</b>：多宫格目前更适用于 <b>15 个以下分镜</b>， 单次输入过多（比如 18 宫格）容易出现静止、顺序错乱等问题， 同时分镜图会限制模型发挥， 请确保分镜准确、合理；</li><li><b>避免脏/锐化的分镜图：</b>不推荐过度锐化、杂乱的 AI 直出分镜图 ； 不推荐在分镜图上写过多文字；</li></ul><grid><column width-ratio="0.374114"><img name="image.png" caption="❌ badcase&#xA;" mime="image/png" scale="0.475570" src="SkR7bj6ccocZkwxzpjoc9MaDnre"/></column><column width-ratio="0.251533"><img name="image.png" alt="这组图片呈现了黄昏石板路场景下，青年与中年男性的互动递进过程，共16个分镜。从青年与中年男性擦肩而过，到两人先后转身、四目相对起争执；青年先后尝试解释、试图缓和，中年男性从质问、语气加重再到希望让步，青年始终摆手拒绝沟通；随后青年试图挽留却被中年男性强硬推开，青年踉跄后退，最终两人保持距离、陷入沉默。整体围绕黄昏街道的光影背景，展现了一场逐步升级后冷却的人际对峙。" mime="image/png" scale="0.582137" src="MJh1brO1ZoWzSwxJm1XcJkconDg"/><p>❌ badcase</p></column><column width-ratio="0.374354"><img name="image.png" alt="图片展示了电影《无间道》中的一段场景拍摄信息。画面分为镜号、景别、运镜、画面描述、时长五个部分。镜号从1到4，景别有极远景、全景、中景、俯拍大远景，运镜有俯冲镜头（高速下落）、定镜、横移镜头、定镜（高角度），画面描述详细描述了各场景的拍摄情况，如极远景镜头从高空俯冲而下，穿过厂房的房梁与光束等，时长分别为5秒、5秒、3秒、6秒。该图与上下文关于电影拍摄的描述相呼应，直观呈现了场景拍摄的细节。" mime="image/png" scale="0.475260" src="ZyKMbcWuKoXBUzxl0aJcGxVGnec"/><p>❌ badcase</p></column></grid><ul><li><b>prompt 避免前后矛盾：</b>注意避免 prompt 前后矛盾或运镜、运动设计不合理等问题；</li><li><b><u>宫格图并不会严格对齐分镜内容</u></b>， 视频会有一定自主性发挥， 如需严格按照分镜图生成时， 推荐使用多关键帧参考方式； </li><li><b>火柴人/线稿分镜使用 [推荐]:</b><grid><column width-ratio="0.500000"><ul><li>推荐使用相对简约的线稿分镜图， 并通过 prompt 进行指令控制： step1 : 写明参考素材的指代关系step2 : 写整体故事梗概step3 : 按照分镜完整描述情节内容， 至少补齐分镜图中没有的信息， 可以考虑组合时间戳明确剧情逻辑， 以右侧 case 为例， 需要有场景、材质、运镜、动作、风格等全部基础信息；</li></ul><pre caption="prompt 案例&#xA;" lang="Plain Text" wrap="true"><code>素材绑定：故事板分镜@图片1，卧室@图片2，李天@图片3，李倩@图片4，《快快乐乐》书籍@图片5。<br/>镜头一：<br/>【全景固定镜头，平视三分构图】冬夜落雪房间，落地窗前，男子双手插裤兜侧立望向窗外飞雪，少女站在身侧静静看向男子，氛围安静克制，雪花持续落在玻璃窗。<br/>镜头二：<br/>【中景过肩镜头】少女后背作为前景，男子转头温和看向少女，少女微微低头沉默，窗外落雪持续。 <br/>镜头三：<br/>【中近景，对角线构图】男子捧着书籍《快快乐乐》缓缓递出，少女抬手接过书本。 <br/>镜头四：<br/>【少女面部近景，中心构图】少女把书本抱紧在胸口，眼眶泛红，泪珠缓缓滑落，神色感伤。<br/>镜头五：<br/>【男子面部近景，斜向构图】男子温柔浅笑，静静注视落泪少女，眼底带着怅然。 <br/>镜头六：<br/>【全景固定镜头】少女转身缓步走出画面，窗前只剩男子独自伫立，双手插兜望向漫天风雪，房间空旷寂静。</code></pre></column><column width-ratio="0.500000"><img name="image.png" alt="这是一组日系手绘风格的分镜插画，还原了动画制作的分镜设计逻辑。画面展现了夜晚飘雪的室内场景，分镜中以男孩森岛帆高、女孩天野阳菜为核心角色，二者互动的情节逐步推进：先是并排站立的场景，接着男孩向女孩递出印有图案的物品，之后女孩抱着写有“快快乐乐”的书本，最后男孩独自站在室内窗边。分镜标注了景别、视角、构图等制作要点，契合文档中要求的新海诚日系动画风格，完整呈现了对应动画段落的分镜设计内容。" mime="image/png" scale="1.000000" src="QvwSbxAD6oPe2xxF3PTcupeFnBU"/><p></p><img name="image.png" caption="其他参考图片&#xA;" mime="image/png" scale="1.000000" src="EROmbKx9To4tjPxvLZAciwPFn5b"/><p></p></column></grid></li><li><b>概念分镜使用 :</b><grid><column width-ratio="0.500000"><ul><li><b>推荐简写 prompt：</b>如果分镜是概念分镜或关键帧设计， 可以直接简写 prompt，  例如 ；<em>“按照分镜图的顺序， 构建一个完整的故事剧情， 运镜合理连贯”</em></li></ul><p></p></column><column width-ratio="0.500000"><img name="fb62ebd6-6296-443b-aa21-b52e7d11c84a.png" alt="图片展示了新海诚风格的动画场景，画面中有一只可爱的熊猫。上排左起，熊猫在古风建筑前，接着在木桌上休息，然后站在木桌上。中排左起，女子在木桌旁与熊猫互动，熊猫在木桌上玩耍，女子看向远处。下排左起，熊猫在藤蔓桥上，女子在木桌旁，最后熊猫在木桌上倒茶。这些画面与上下文提到的参考视频1的光影、镜头运镜、角色站位等信息相呼应，是动画创作的参考素材。" mime="image/png" scale="0.217773" src="CXLPbvjEFooIc2x0wCFcGCXunah"/><p>概念分镜参考图</p></column></grid></li></ul></td></tr><tr><td vertical-align="middle"><b>关键帧参考</b></td><td colspan="2" vertical-align="top">视频需要严格按照分镜图生成时使用， 关键帧参考就是将分镜按照独立参考输入， 并按照顺序传入 ， prompt 需要在第一句写明 “以图片 x 至图片 x 的顺序作为关键帧”， 参考案例 :<br/><em>“</em><b><em><u>以图片 1 至图片 7 的顺序作为关键帧， </u></em></b><em>在云海群山间，蓝粉长尾灵鱼凌空遨游，镜头缓缓推向依山而建的古镇，聚焦山顶古塔；画面一转进入雅致中式厅堂，灵鱼穿窗飞入，落入厅堂中央圆池悠然游动；最终视角切至幽暗古寺，白须老僧背对而立，静静凝望巨幅画框，画内正是厅堂与池中灵鱼，新国风浮世绘插画风格。”</em><grid><column width-ratio="0.142850"><img name="image.png" alt="图片展示了一幅色彩斑斓的奇幻画面。画面中，一座古色古香的楼阁坐落在山巅，周围环绕着郁郁葱葱的树木和五彩斑斓的花朵。山间云雾缭绕，山脚下有蜿蜒的河流，河中有一艘小船。画面左上方有一条色彩斑斓的飞鱼，其身体呈现出蓝、粉、白等色彩，尾部有红色的眼睛。整体画面色彩丰富，充满梦幻与唯美感，与文档中对新海诚风格日系动画的描述相契合。" mime="image/png" scale="0.475260" src="Ut9xbg0FForhg2xGnKOczHJynUd"/></column><column width-ratio="0.142850"><img name="image.png" alt="图片展示了一幅色彩斑斓的动画场景。画面中，一座古色古香的红白相间建筑坐落在山顶，周围环绕着许多白色房屋。山间点缀着各种颜色的伞形图案，山脚有河流蜿蜒，远处是连绵的山脉，天空中云彩飘逸。整体画面色彩丰富，具有新海诚风格的日系动画特点，与文档中关于动画场景的描述相契合，可能是参考图1中的楼顶天台和天空场景。" mime="image/png" scale="0.475260" src="BSDgbC84ToIibNxVr3scaxTNnUb"/></column><column width-ratio="0.142901"><img name="image.png" alt="图片展示了一幅色彩鲜艳的建筑群景观。画面中央是一座高耸的红白相间的塔楼，塔顶为金色，周围环绕着风格各异的建筑。山间点缀着绿树，地面上摆放着多把色彩斑斓的油纸伞。背景是蓝天白云，整体画面色彩丰富，具有浓厚的东方建筑风格，与上下文提到的“新海诚风格的日系动画”相契合，可能作为参考图用于动画创作。" mime="image/png" scale="0.570312" src="Z8RabO0ShoYIPOxsGXucTIARnQg"/></column><column width-ratio="0.142850"><img name="image.png" alt="这张图片是一间融合中式古典元素的雅致室内空间，空间中央设有带精美蓝白纹样的圆形水池，铺有复古花纹地砖，周边摆放着中式木桌、矮榻，搭配瓷瓶、盆栽、灯笼、书画、樱花摆件等装饰。房间正面的大花格窗户向外敞开，窗外是层叠山峦、溪流与充满日式风格的彩色坡地建筑，整体氛围静谧唯美，兼具中式古典韵味与日式清新美感。" mime="image/png" scale="0.475260" src="U1Crb8AR7ow87DxrLMJcfLtnnNc"/></column><column width-ratio="0.142850"><img name="image.png" alt="这张图片呈现的是新海诚风格的中式古风室内场景，空间内布置有多处中式传统器物，包括绘有花纹的陶瓷瓶、带雕花的古式木柜、摆放在桌上的盆栽，还有摆放在地面与矮桌的瓷枕。房间中央设有圆形水池，池壁带有精致纹样，透过房间的花格窗，能看到远处层叠的山峦、蓝天白云，还有一只粉蓝相间的灵鸟状生物飞在空中，整体氛围唯美静谧，带有新海诚作品特有的温柔治愈感，与文档中要求的新海诚风格日系动画的光影感和画面氛围相契合。" mime="image/png" scale="0.475260" src="QzwqbT3iAoA0sNx95fPc4lWFndh"/></column><column width-ratio="0.142850"><img name="image.png" alt="图片展示的是一个室内场景，画面中央是一个圆形的水池，池中有一条色彩斑斓的锦鲤在游动。水池周围摆放着一些装饰品，如花瓶、盆栽等。背景是带有传统图案的屏风，窗外是山川河流的景色。整个画面色调柔和，光线从窗外透进来，营造出一种宁静祥和的氛围。此图可能作为参考图，用于指导创作与渲染相关内容。" mime="image/png" scale="0.475260" src="Wd1QbGrzjoImr8xAWBQchNXDnZb"/></column><column width-ratio="0.142850"><img name="image.png" alt="图片展示了一位白发老者背对镜头，面对一幅古风画作的场景。画中是一个古色古香的室内环境，有圆形水池、桌椅、花瓶等摆设，窗外是山川景色。画面右侧有竖排古文。画作左侧墙上有一尊佛像，佛像前有蜡烛。老者身穿棕色长袍，脖子上戴着项链，画面整体色调偏暖，营造出一种静谧的氛围。此图可能用于参考文档中关于白模参考/渲染的描述，体现新海诚风格的日系动画场景特点。" mime="image/png" scale="0.475260" src="SkKjboLfMobYWoxV1cacqW7Pn9b"/></column></grid></td></tr></tbody></table>



<callout emoji="♦️">
### 与**Seedance 2.0的**差异点
1. 响应时间戳：2.0不响应时间戳只响应镜头序号，而2.5响应整数秒的时间戳；
2. 支持多视图：2.0不建议使用多视图作为主体参考，而2.5是可以支持的；
3. 自由宽高比：2.0的输出宽高比只有固定的6档，2.5可以通过控制输入素材的方式支持 [0.4, 2.5] 之间的任意宽高比输出；
4. 提升V2V的画质：2.5的输出支持MOV格式，在延长/编辑任务中更好地保持颜色与亮度一致性、声画一致性。
</callout>



## 5.3｜方舟体验中心试用

<callout emoji="📍">
8月7日起，**全量用户**可在方舟体验中心试用 Seedance2.5 模型，体验文生视频、参考生成（图片、语音、视频）、视频编辑、视频延长、首尾帧等功能。
点击直达 ➡️ [方舟体验中心](https://console.volcengine.com/ark/region:cn-beijing/experience/gen_video?model=doubao-seedance-2-5-260628)
</callout>

<figure view-type="Preview"><source name="体验中心全流程录屏.mov" mime="video/quicktime" origin-height="1802.000000" origin-width="3386.000000" size="50037483" token="[媒体标识已移除]"/></figure>

<table><colgroup><col/><col/><col/></colgroup><tbody><tr><td><b>找到模型卡片</b></td><td>打开<a href="https://console.volcengine.com/ark/region:ark+cn-beijing/model?vendor=Bytedance&amp;view=LIST_VIEW">方舟模型广场</a>，找到【Doubao-Seedance-2.5】模型卡片，点击立即体验，开始生成</td><td><img name="image.png" alt="这是Doubao-Seedance-2.5模型方舟体验中心的操作界面，页面顶部显示模型名称“Doubao-Seedance-2.5”，页面核心区域配有“体验视频生成，让创意摇动”的标题，下方有提示使用@符号快速引用文件生成视频的说明。界面底部可设置模式为“参考生成”，还能调整视频参数，包括比例为16:9、分辨率720P、格式MP4、时长为智能时长、输出带声音，生成数量设为1条，同时标注了0.07元/千tokens的费用信息。" mime="image/png" scale="1.000000" src="F1FDbr9LyoCy32xNDMLcD0t3nWd"/></td></tr><tr><td><b>模版库/素材库</b></td><td>体验中心提供模版库/素材库<ul><li>模版库，一键复用，即可生成视频</li><li>素材库，自由组合 图片/视频/音频  生成自定义视频</li></ul></td><td><grid><column width-ratio="0.567270"><img name="image.png" caption="素材库&#xA;" mime="image/png" scale="0.296507" src="AMhUb21REoC65nx6tpYcSY0tnDg"/></column><column width-ratio="0.432730"><img name="image.png" caption="模版库&#xA;" mime="image/png" scale="0.296989" src="EoGNbwTziojgxxxzwrCcupQGnpb"/></column></grid></td></tr><tr><td><b>设定 模型参数</b></td><td><ul><li>模式 可选「 参考生成」、「首尾帧」、「视频编辑」、「视频延长」</li><li>依次设置：分辨率（480p/720p/1080p）、视频比例、视频时长、视频格式、是否输出声音、生成数量</li></ul></td><td><img name="image.png" caption="设置模型参数&#xA;" mime="image/png" scale="1.000000" src="AZXRbBnkfo0R5pxJfyhcziLanzc"/></td></tr><tr><td vertical-align="middle"><ol><li seq="1"><b>参考生成</b></li></ol></td><td><ul><li>参考素材数量上限、生成时长上限提升</li></ul><blockquote><p>支持最多 50 参考素材 + 30s 生成时长，可快速定位引用素材</p></blockquote><ul><li>提供高质量预置示例</li></ul><blockquote><p>预置示例覆盖多参考生成、视频编辑等场景，支持快速验证模型能力</p></blockquote></td><td><img name="CPT2607072253-960x351.gif" alt="这张图片展示的是Doubao-Seedance-2.5体验中心的视频生成操作界面，标题为“体验视频生成，让创意摇动”。界面核心区域明确标注了生成视频的核心指令：全程26秒一镜到底（One-Shot）的叙事短片，需稳定稳拍，指定参考4段视频素材。下方呈现了0-3秒、3-6秒的分段运镜与场景描述，还标注了对应参考图片素材的位置，界面底部显示了智能比例设为720P、智能时长1条、有配音等参数，同时列出了“参考生成”“智能比例”“智能时长”等操作选项。" caption="&#xA;" mime="image/gif" scale="1.000000" src="QI16b8v4foXc5rxqqZNcpZH4nVh"/><img name="CPT2607072254-1114x533 (1).gif" alt="图片展示的是方舟体验中心试用中视频生成界面。上方标题为“体验视频生成，让创意摇动”。下方有核心指令，包括镜头、氛围、场景等详细描述。画面中呈现了多帧视频帧，如“老旧木门吱呀推开”“身穿欧洲女人”等场景。界面底部有版权库、模版库、素材库、虚拟人傀库、我的等标签栏，当前选中“模版库”。右下角显示0.0003元/千tokens，有蓝色的“+”按钮。该图片与上下文介绍的方舟体验中心试用中视频生成操作相关，直观呈现了视频生成界面及部分操作选项。" mime="image/gif" scale="1.000000" src="GtZjbUQ8roqrINxydtxcmPVKnL1"/><img name="CPT2607072256-965x514.gif" alt="图片展示的是Doubao-Seedance-2.5模型体验中心试用的视频生成界面。画面中呈现了“体验视频生成，让创意摇动”的标题，下方有核心指令，包括全程26秒一镜到底（One-Shot）叙事短片、稳定跟拍、参考素材等内容。画面右侧有“参考生成”按钮，下方显示生成时长、分辨率、视频时长、生成数量等信息，还标注了“当前花费0.132元”。该图片与上下文介绍的方舟体验中心试用中模版库/素材库、设定模型参数等功能相呼应，直观呈现了视频生成操作界面。" mime="image/gif" scale="1.000000" src="BO8ZbfKSiodQYYxfsOsclS4Oncb"/><img name="image.png" alt="图片展示的是Doubao-Seedance-2.5模型在方舟体验中心的界面。左侧为导航栏，有模型管理、API Key管理等选项。右侧上方显示模型名称及版本，下方有参考素材区，可设置参考素材数量、生成时长等参数。中部是模版库/素材库，有多个视频和图片缩略图，如“你好”“你好，世界”等。右侧有“生成”按钮，可进行视频生成操作。该图与上下文介绍的方舟体验中心试用内容相关，直观呈现了模型的使用界面及功能。" mime="image/png" scale="1.000000" src="OUarbNW6YoKxOOx2IZ4cpqgZnke"/></td></tr><tr><td><ol><li seq="2"><b>视频编辑</b></li></ol></td><td>对输入视频的画面或音频进行增删改等编辑操作。</td><td><img name="image.png" alt="这张图片展示的是方舟体验中心中选择「视频编辑」模式的视频生成相关操作界面，该模式可对输入视频的画面或音频进行增删改等编辑操作，例如给视频添加元素、修改内容、删除背景音乐等。界面显示的参数设置包含：模式为「视频编辑」，视频参数分别为智能比例720P、格式MP4，视频时长为智能时长，设置输出有声视频1条，还标注了该生成操作的费用为0.07元每千tokens，左侧设置参考内容可关联对应素材来开展编辑操作。" mime="image/png" scale="1.000000" src="CS1sbwN6io8mkrxkXOgc2UcTnXf"/><img name="image.png" caption="视频编辑&#xA;" mime="image/png" scale="1.000000" src="MVEibzxEboQ0NFx0dN3cv8m8nkc"/></td></tr><tr><td><ol><li seq="3"><b>视频延长</b></li></ol></td><td>对输入视频进行向前/向后延长。</td><td><img name="image.png" alt="这张图片展示了方舟体验中心的视频延长功能界面，该功能可对输入视频进行向前或向后延长，示例为向后延长@视频1，@图片1的角色从天而降，或续写@视频1前5s、@视频2中角色走进画面等内容。界面显示当前选中的功能为视频延长，还包含智能比例、720P、MP4、智能时长、有声等设置选项，以及“0.07元/千 tokens”的费用信息，对应文档中视频延长的操作说明，能直观呈现该功能的使用输入界面与相关设置项。" mime="image/png" scale="1.000000" src="EuRCbSGS9okUTUx44MScXP0jnvc"/><img name="image.png" caption="视频延长&#xA;" mime="image/png" scale="1.000000" src="IXLHb2NKYowtVJxsENVcjEqanVb"/></td></tr><tr><td vertical-align="middle"><ol><li seq="4"><b>首尾帧生成</b></li></ol></td><td>输入1张图作为首帧生成视频,或输入2张图分别作为首帧和尾帧生成视频。</td><td><img name="image.png" caption="首尾帧生成&#xA;" mime="image/png" scale="1.000000" src="SG1JbNIp4onj75x98pXcyGrrn5e"/></td></tr><tr><td vertical-align="middle"><b>费用确认弹窗</b></td><td><ul><li>新增生成前消耗确认弹窗</li></ul><blockquote><p>支持生成前查看预计消耗 token 及预计花费金额，帮助提前掌握成本、按需生成，避免超预算消耗</p></blockquote></td><td><img name="image.png" alt="这是火山方舟平台的方舟体验中心相关界面，中间弹出了「本次生成预计花费」的费用确认弹窗，清晰展示了生成视频所需消耗的token数量及对应的预计花费金额，弹窗底部有取消按钮和紫色确认按钮，还带有“不再显示”的勾选选项。该弹窗属于文档中提到的生成前消耗确认弹窗，作用是让用户提前掌握生成视频的成本，避免超预算消耗。" caption="&#xA;" mime="image/png" scale="1.000000" src="H892bs2EloknTnxaUfncYAkZnNf"/></td></tr></tbody></table>



## 5.4｜API 调用

<callout emoji="📍">
Seedance 2.5 API 于 **8月7日** 全量公开
API调用方式 详见官网：[Doubao Seedance 2.5 教程](https://docs.volcengine.com/docs/82379/2607688?lang=zh)
</callout>