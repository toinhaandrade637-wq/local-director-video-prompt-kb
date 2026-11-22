# MR_OTTER（One Day with Mr. Otter）全流程创作方法论

> 来源：@fotachu 社区高赞项目（Higgsfield Originals 收录），02区 725 件资产 / 304 条去重提示词 / brief 全文 7.5K。

## 〇 项目档案

| 维度 | 内容 |
|---|---|
| 片名 | One Day with Mr. Otter |
| 导演方 | @fotachu（个人创作者） |
| 类型 | 22 分钟动画动作喜剧——间谍大片 × 动物 |
| Logline | 水獭 Mr. Otter 被卷入任务：阻止鳄鱼与长颈鹿炸毁自由女神像 |
| 体量 | 官方 772（实拉 725 jobs / 304 去重 / 43 folders；差额为上传件） |
| 模型 | seedance_2_5×395 + gpt_image_2×317（图先行） |

## 〇.5 整体画面风格 DNA

（从 304 条提示词 + brief 提取）

- **动物拟人间谍大片**：经典 spy blockbuster 视觉语法（邦德式）+ 全动物卡司——反差喜剧核心
- 图先行的角色体系：gpt_image_2 出角色/场景设定（317 图），seedance_2_5 动画化（395 视频）
- 22 分钟 = 长片级工程管理：43 个 folder 按序列/资产分区

## 一 工作流（brief 原文要点）

One Day With Mr. Otter is a 22-minute animated action-comedy that takes the classic spy blockbuster and hands it over to the animals. At its center is Mr. Otter... an otter — who somehow ends up on a mission to stop a crocodile and a giraffe from blowing up the Statue of Liberty.

Hey, my surname is Fotachu-I am a 18 years old student from Spain. I am French, and first started using AI around 2022-2023. Since, I couldn't stop generating even one single day. I was lucky enough to get selected by Higgsfield to become a CPP member. I grew my channels to around 10K followers each and made around 200M+ views these past 7 months. I created three-quarters of the scenes on my phone using Cinema Studio V4, and then edited the entire video on my phone. Once the rendering looked good, I re-edited the entire video on my PC and polished all the scenes.


The credit grant offered by the team—because my project was different from the others and they wanted to take a chance on me and see the film completed, I think—was beneficial. In fact, the film cost just over $2,000 in credits, compared to about $30 million for a real production.


The film is a mix of comedy and Hollywod-style scenes. The fact that the main character is a bipedal otter adds a playful touch to the film. What’s more, Mr. Otter is a very endearing character who knows how to crack a joke. The goal of this film is to depict a child’s perspective while playing with toys, through this 22-minute film (22 minutes being the average amount of time a child spends playing with toys). The story builds to a climactic showdown at the Statue of Liberty before closing on a twist that reframes the whole adventure as something far more innocent — because honestly, the best action movies start as games played on a bedroom floor.


The most important thing... is that this whole story was told by a child who was quietly playing with his toys. In fact, as you may have noticed, the beginning is very clear and stems from a dream: it’s the child’s imagination—the idea he clearly had in mind before playing with his toys. As the story unfolds, the ideas blend together and everything becomes increasingly confusing. Finally, the last scenes are clear and precise because the child had thought them through. In conclusion, this story recounts the adventures of an otter, imagined by a dreamy child. 


This one took days of animation, design and post-production work, and I'm really proud of how it turned out. If you enjoy fast-paced co

（全文见 05区 _官方项目brief/MR_OTTER_brief全文.txt）

## 二 提示词写法要点（304 条实测）

- 视频提示词占 68%（208/304）——动作喜剧以运动镜头为主
- 图片提示词 96 条——角色/场景/关键帧设定
- 典型模式：图模型出设定 → 视频模型按设定动画化（官方标准双管线）

## 三 可复用要点

1. 动物拟人喜剧 = 间谍大片语法 × 动物行为学细节（反差感来源）
2. 图先行管线适配长片：317 图设定锁定 22 分钟一致性
3. 完整数据与分类见 GitHub 仓 MR_OTTER/
