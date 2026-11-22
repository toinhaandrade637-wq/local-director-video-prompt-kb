# Academy L4-L6 教材蒸馏（官方教学 · 平台操作教学）

> 收割 #5b（E155）｜来源：Academy新课字幕 VTT 原文（shot-sizes 21.8K / direct-your-own-scene 19.4K / create-and-edit-assets 38.9K）

## 核心发现：L4-L6 是平台操作教学而非提示词工艺

Academy 新课 AI Creation: First Steps 的 L4-L6 内容主要是**平台工作流教学**（怎么用 Elements / 怎么用视频参考 / 怎么用多镜头），而非提示词写作方法论。提示词工艺在 K09（cineimage-soul）与 K13（PromptBank 运镜）中已覆盖。

## L5 Shot Sizes and Prompting（14K 字幕）

### 要点
- **Elements 系统**：@mention 引用已保存参考（Character 前缀/Prop 前缀/Location 前缀），不用每次手动附加图片
- **Seedance 2.5 多模态**：text + images + video + audio 一起输入
- **多镜头 vs 单镜头**：Seedance 根据 prompt 结构自动选择——单镜头描述一镜到底，多镜头逐镜描述+切割点
- **画面参考分工**：每个角色图给面部和服装，场地图给空间布局
- **Seedance 2.5 可生成 4-30 秒带声音视频**

### 值得保留的方法
- Elements 命名规范：Character 类加 Character 前缀，@ 引用时自动识别
- 多镜头描述方法：逐镜描述每个 shot 的内容+切割点位置
- 画面参考分工：每个参考件在 prompt 中显式声明它负责什么（face vs location vs prop）

## L6 Direct Your Own Scene（12K 字幕）

### 要点
- **双重锁（Double Lock）**：视频参考控制相机运动 + 提示词控制最终画面外观
- **iPhone 参考拍摄**：不用完美——要的是相机路径/构图/速度/动作时序
- **参考分工显式声明**：图像参考管角色/箱子/场地，视频参考管相机运动/构图/速度/动作时序
- **单镜修改**：改变已完成镜头的一个细节而不重新生成全部

### 值得保留的方法
- Double Lock 模式：video reference 定义 movement + prompt 定义 look = 两个锁同时生效
- 参考分工声明模板：Keep the image instructions for [characters/location]. Use this video for [camera movement, framing, speed, and action timing].
- 单镜修改方法：Change one detail. Keep the rest.

## 结论

Academy L4-L6 教材价值在**平台工作流**（Elements/多镜头/视频参考），而非提示词工艺。提示词工艺已在 K09（cineimage-soul）/K13（PromptBank）/K14（fight-scene）中覆盖。L4-L6 内容**不产出新 K 页**——平台操作知识已由 K09-K16 的方法层覆盖，且平台 UI 教学非本知识库范围（随版本更新过时）。
