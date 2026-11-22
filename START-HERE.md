# 从这里开始

> 5 分钟搞清楚：这个库装了什么、你该先读哪一页、AI 该怎么用。
> 只想知道怎么查一条提示词，直接跳到 [第 3 节](#3-五个高频动作)。

## 1. 先确认你要做什么

| 你的目标 | 走这条路线 | 大概用时 |
|---|---|---|
| 找一条能参考的提示词，马上用 | [docs/01-快速开始](docs/01-快速开始.md) → 搜索引 → 取全文 | 5 分钟 |
| 学一部片子从头到尾怎么组织提示词 | [catalog/higgsfield-projects.md](catalog/higgsfield-projects.md) → 项目文档 → 抽读 5–10 条 | 15 分钟 |
| 系统学怎么写，再动笔 | [methods/README.md](methods/README.md) → [docs/02-任务路由](docs/02-任务路由.md) | 30–60 分钟 |
| 让 AI 直接接手 | [AGENTS.md](AGENTS.md) → 把任务交给它 | 1 分钟 |
| 修库、加料、发版 | [docs/06-维护与更新](docs/06-维护与更新.md) → [docs/08-构建与校验报告](docs/08-构建与校验报告.md) | 视改动 |

## 2. 库的三层结构

```text
方法层   sources/*/现行知识/     教怎么写：结构、参考分工、表演、打戏、运镜、光影、声音、平台限制
语料层   sources/higgsfield/     611 个项目的原样提示词，一项目一份压缩 JSONL
索引层   catalog/               轻量索引：ID、项目、类别、模型、长度、行号、80 字摘要
```

三条使用原则：

1. **先索引，后回读。** 不要一上来解压整个项目，816 MB 原文不是给人读的。
2. **方法看结构，语料看案例。** 方法页告诉你为什么这样写，语料告诉你在真实项目里长什么样。
3. **参考不是模板。** 换掉人物、场景、台词、动作结果，只迁移结构。

## 3. 五个高频动作

```bash
# ① 看库里有什么
python tools/kb.py stats

# ② 关键词找
python tools/kb.py search --keyword "霓虹" --limit 10

# ③ 按项目 + 类别找
python tools/kb.py search --project DETOUR --cat scenes --type video --limit 10

# ④ 按模型 + 长度找
python tools/kb.py search --model seedance_2_5 --min-length 3000 --limit 10

# ⑤ 拿到 ID 后读全文
python tools/kb.py get --id HFX-DETOUR-000166
python tools/kb.py get --id VPL-sd2-259
```

没有 Python 时：直接搜 `catalog/higgsfield-prompts.index.jsonl`，拿到 `project` + `line`，再按 [docs/03-检索手册](docs/03-检索手册.md) 第 4 节回读。

## 4. 三个真实例子

| 我想要 | 命令 | 结果 |
|---|---|---|
| 一段雪地近身格斗的完整提示词 | `get --id VPL-sd2-259` | 《雪地女特工·近身搏斗》173 字，Seedance 2.0 |
| DETOUR 里 8 秒霓虹街景的镜头 | `search --keyword "霓虹"` | `HFX-DETOUR-000166`，3,722 字，21:9 三镜连续 |
| 一个 8000 字级的 Seedance 2.5 长提示词 | `search --model seedance_2_5 --min-length 6000` | `HFX-ANERNEQ-000001`，8,156 字，极夜生火 |

更多案例见 [docs/07-检索案例](docs/07-检索案例.md)。

## 5. 必须先知道的三个数据事实

1. **分类覆盖有限。** 611 个项目里，537 个上游只给了 `_all_prompts.jsonl`，所以它们的提示词全在 `cat=all`。只有 6 个项目有 `scenes` 细分。检索时 `--cat scenes` 返回 0 条是正常的，去掉 `--cat` 再试。
2. **跨项目不去重。** 同一句提示词出现在两个项目里，是两条记录。这正是“谁在复用、谁在迭代”的线索。
3. **`model=default` 不是模型名。** 它表示平台自动选择，共 45,467 条，不要当成某个具体模型。

## 6. 三条红线

| 不要 | 因为 |
|---|---|
| 把参考提示词整段复制后只改名字 | 结构可以学，事实必须换成当前项目的 |
| 用索引里的 80 字摘要当原文 | 摘要只够判断相关性，写作前必须回读 |
| 在没有依据时说“某模型支持/不支持” | 语料不是官方文档，平台能力去查方法页与官方资料 |

## 7. 接下来读什么

| 你是 | 下一步 |
|---|---|
| 人，第一次用 | [README.md](README.md) → [INDEX.md](INDEX.md) |
| AI | [AGENTS.md](AGENTS.md) → [docs/02-任务路由](docs/02-任务路由.md) |
| 想直接查 | [docs/03-检索手册](docs/03-检索手册.md) → [docs/07-检索案例](docs/07-检索案例.md) |
| 想理解数据 | [catalog/taxonomy.md](catalog/taxonomy.md) → [docs/04-字段与格式](docs/04-字段与格式.md) |
| 要维护它 | [docs/06-维护与更新](docs/06-维护与更新.md) → [docs/08-构建与校验报告](docs/08-构建与校验报告.md) |
