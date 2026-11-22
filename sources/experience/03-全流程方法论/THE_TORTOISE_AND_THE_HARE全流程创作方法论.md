# THE TORTOISE AND THE HARE 全流程创作方法论

> 社区项目 @benhamin · AI Film Festival 参赛 · 773 赞 / 57,508 播放 · 3 分 54 秒寓言改编剧
> 数据底座：821 job 全量（零丢失，100% 带提示词）/ **381 条唯一去重提示词** / 捕获 2026-10-27

## 〇 项目档案

| 项 | 值 |
|---|---|
| 链接 | https://higgsfield.ai/zh/@benhamin/projects/the-tortoise-and-the-hare |
| 对账 | 官方 829 = 821 job + 8 audio_input；图 430 / 视 391 |
| 结构 | ROOT 197 · IMAGES 253 · SCENE_01 68 / SCENE_02 44 / SCENE_03 142 / SCENE_04 89 · AUDIO 28 |
| 模型 | seedance_2_5 357 · seedream_v5_pro 310 · gpt_image_2 112 · **hf_mult_replace_object 22** · seedance_2_0 9 |
| 工期 | 制作约两周 → 成片 3:54（brief Film Details 原文） |

## 〇.5 创作主题 DNA（官方 brief）

> There are stories of those who have seen it— but none of those who found it and returned.

开场引言式 brief（悬念定调）+ ✨Context + 🎭Narrative + 🎨Visuals + 🎬Production 四段标准面板。"From Characters to Scenes"/"Shaping the Story"章节记录从角色到场景的推进法。

## 一 工作管线（实测）

1. **图视双轨**：图像 430 vs 视频 391 几乎对半——与 THE_KISS（图像 72%）和 DPI（视频 73%）都不同，本项目图定调与视频生成并行推进。
2. **SCENE_01~04 分镜夹**：按场次组织生成（SCENE_03 最多 142 条）， IMAGES 夹 253 条为角色/场景参考库——**结构最清晰的分镜制工作区**。
3. **hf_mult_replace_object 22 条**：库内少见的"物体替换"模型专用法（改物件不重生成整镜），省 credits 的关键技巧。
4. **AUDIO 夹 28 条**：音乐按场景对位（8 audio_input 在计数内为上传件，28 条 job 为生成件——含在 job 内）。
5. 抽卡率 2.2 倍（821→381）。

## 二 可复用清单

1. **场次夹组织法**：SCENE_01~N 每夹一个场景的多次抽卡，成片时按夹取最优——比单夹堆叠好回溯。
2. **物体替换模型**：hf_mult_replace_object 局部改物，避免整镜重跑（22 条实测用法在库）。
3. **引言定调**：brief 开头一句虚构引言（"见过它的故事很多，找到它又回来的没有"）——先给评委一个世界观钩子。
4. **两周工期样本**：单人 4 场景 3.9 分钟的可行产能基线。
