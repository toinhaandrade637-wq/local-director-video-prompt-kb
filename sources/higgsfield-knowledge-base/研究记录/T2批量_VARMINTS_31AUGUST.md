# T2 批量收割 #2-#4（VARMINTS + 31_AUGUST + CHARLIE_BOY 缺 JSONL）

> 收割 #6-#8（E162）｜VARMINTS 1,251 行/513 唯一/2.4× + 31_AUGUST 760 行/522 唯一/1.5× + CHARLIE_BOY 无 _all_prompts.jsonl（跳过待查）

## VARMINTS_LAS_BODAS_DEL_RIO（1,251 行 · 2.4× 迭代）

**块头分类学**：POSITIVE LOCKS×408 / PHYSICS×407 / SCENE CONTEXT×397 / LIGHTING×397 / **PERFORMANCE×381**（新块型首见！）

### PERFORMANCE 块 [官方]
ANERNEQ/VENGEANCE 均无此块。PERFORMANCE 独立于 ACTING TASK——ACTING TASK 管角色意图（MOTIVE/OBSTACLE/TACTIC），PERFORMANCE 管**表演执行**（身体如何做、面部如何反应、声音如何表现）。两者是导演（ACTING TASK）与演员（PERFORMANCE）的分工。

### 模型分布
?×776 / default×350 / **video_extension×74**（新模型首见——视频延长专用模型，与 videotape-alpha 同类）

## 31_AUGUST（760 行 · 1.5× 迭代）

**散文体但有内嵌标记**：HARD CUT.×77 / CAMERA HEIGHT×36 / CAMERA MOVEMENT×34 / **JHONNY×34**（角色名独立块）/ CRITICAL:×30（关键规则块）

### CRITICAL: 块 [案例]
类似 ANERNEQ 的 NEGATIVE 栈或 INSIDE_AI 的 THE KEY RULE OF THIS SCENE——每条提示词的关键规则集中声明。

### videotape-alpha 确认 [案例 14×]
31_AUGUST 确认 videotape-alpha 模型的第二次大规模使用（第一次=CAT_STORY×66）。

## CHARLIE_BOY（329 赞）

02区无 _all_prompts.jsonl——可能使用不同 schema 或文件名。待查后补收。

## 结论 → K 页生长

1. **PERFORMANCE 块**（VARMINTS 381×）→ 新块型，ACTING TASK 与 PERFORMANCE 的导演/演员分工→ 视频轨重建时纳入
2. **video_extension 模型**（74×）→ K08 重建时补录
3. **CRITICAL: 块**（31_AUGUST 30×）→ 与 THE KEY RULE OF THIS SCENE 同族，规则立法的另一种形态
4. CHARLIE_BOY 无 JSONL → 02区收录缺口，需补查


## 补充：T2 #5-#7（DOMINIO + LOST + HALVER）

### DOMINIO（746 行 / 522 唯一）
块头：HARD CUT.×376 / REFERENCES×261 / STRUCTURE×249——结构化模板变体，REFERENCES 独立成块（非 ACTIVE REFERENCES），STRUCTURE 独立成块。

### LOST（350 行 / 102 唯一）
散文体（无命名块），1.8× 迭代。

### HALVER（1,040 行 / 580 唯一）
块头：A. ELEMENT REFERENCES×102 / HALVER×100 / LIGHTING×60——**A. 前缀编号式分块**（不同于 VENGEANCE 的无编号标签体），HALVER 作为项目名独立块。

### 新增方法
1. REFERENCES vs ACTIVE REFERENCES：两种引用块命名并存
2. STRUCTURE 独立块：结构描述独立于 SCENE CONTEXT
3. A. 编号式分块：HALVER 用字母编号分节（A/B/C...）


## 补充：CHARLIE_BOY（1,721 行，全库最独特项目）

### **1.0× 迭代率——全部唯一**
1,721 行 1,721 个唯一提示词，**零重生成**。其他项目迭代率 2-8×（同模板反复渲染选优），CHARLIE_BOY 每条提示词都是手写原创。

### **44K 单条提示词——全库最大**
代表 44,469 字符，使用 【】 方括号系统（不同于 VENGEANCE 的 <<<uuid>>> 和 ANERNEQ 的 ALL-CAPS 行首块）。

### 新块型
- **MAINTAIN CONSISTENCY×167**：一致性维护块
- **REFERENCE PRIORITY×158**：引用优先级块
- **FAIL TEST×148**：**自测块**——作者预判可能的失败模式并内置检测（全库首见自引用验证系统）
- **PRODUCTION FRAME×90**：制作框架块
- **CAMERA LAW×75**：相机法则块（不同于运镜提示词，这是相机行为法律）

### 结论
CHARLIE_BOY 代表**手写零迭代路线**的极端案例——与 ANERNEQ（8.8× 迭代选优）形成两极。两种路线的质量差异需要实战验证。
