# -*- coding: utf-8 -*-
"""重建全部索引与统计：项目表、逐条索引、模型分布、方法表、技能表、MANIFEST、index.json。

源文件只读：
  sources/higgsfield/prompts/<项目>/prompts.jsonl.gz
  sources/higgsfield/_项目元数据.json
  sources/video-prompt-library/AI-全库.jsonl
"""
from __future__ import annotations

import csv
import gzip
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAT = ROOT / "catalog"
CAT.mkdir(parents=True, exist_ok=True)

HF_ROOT = ROOT / "sources" / "higgsfield"
PROMPT_DIR = HF_ROOT / "prompts"
PROJECT_DOCS = HF_ROOT / "projects"


def clean(s: str, n: int = 60) -> str:
    s = re.sub(r"\s+", " ", s or "").strip()
    return s[:n]


def size_mb(p: Path) -> float:
    if p.is_file():
        return p.stat().st_size / 1024 / 1024
    return sum(f.stat().st_size for f in p.rglob("*") if f.is_file()) / 1024 / 1024


# ---------- Higgsfield：从压缩语料重建索引与项目表 ----------
meta = {}
meta_path = HF_ROOT / "_项目元数据.json"
if meta_path.is_file():
    meta = json.loads(meta_path.read_text(encoding="utf-8"))

projects = []
index_path = CAT / "higgsfield-prompts.index.jsonl"
with index_path.open("w", encoding="utf-8", newline="\n") as idx:
    for d in sorted(p for p in PROMPT_DIR.iterdir() if p.is_dir()):
        gz = d / "prompts.jsonl.gz"
        if not gz.is_file():
            continue
        cats = Counter()
        models = Counter()
        types = Counter()
        chars = 0
        n = 0
        with gzip.open(gz, "rt", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                o = json.loads(line)
                n += 1
                prompt = o.get("prompt", "") or ""
                chars += len(prompt)
                cat = o.get("cat", "") or ""
                model = o.get("model", "") or ""
                typ = o.get("type", "") or ""
                cats[cat] += 1
                if model:
                    models[model] += 1
                if typ:
                    types[typ] += 1
                idx.write(json.dumps({
                    "id": o.get("id") or f"HFX-{d.name}-{n:06d}",
                    "project": d.name,
                    "cat": cat,
                    "type": typ,
                    "model": model,
                    "len": len(prompt),
                    "line": n,
                    "head": clean(prompt, 80),
                }, ensure_ascii=False) + "\n")
        if not n:
            continue
        info = meta.get(d.name, {})
        projects.append({
            "project": d.name,
            "theme": info.get("theme", ""),
            "author": info.get("author", ""),
            "url": info.get("url", ""),
            "type": info.get("type", ""),
            "lang": info.get("lang", ""),
            "prompts": n,
            "chars": chars,
            "categories": dict(cats.most_common()),
            "result_types": dict(types),
            "models": dict(models.most_common()),
            "bytes_gz": gz.stat().st_size,
            "prompts_path": f"sources/higgsfield/prompts/{d.name}/prompts.jsonl.gz",
            "docs_path": f"sources/higgsfield/projects/{d.name}/" if (PROJECT_DOCS / d.name).is_dir() else None,
            "has_docs": (PROJECT_DOCS / d.name).is_dir(),
        })

projects.sort(key=lambda x: (-x["prompts"], x["project"]))
(CAT / "higgsfield-projects.json").write_text(
    json.dumps(projects, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
)

model_total = Counter()
cat_total = Counter()
type_total = Counter()
cat_projects = Counter()
for p in projects:
    for k, v in p.get("models", {}).items():
        model_total[k] += v
    for k, v in p.get("categories", {}).items():
        cat_total[k] += v
        cat_projects[k] += 1
    for k, v in p.get("result_types", {}).items():
        type_total[k] += v

docs_projects = sum(
    1 for p in projects
    if (ROOT / "sources" / "higgsfield" / "projects" / p["project"]).is_dir()
)

total_prompts = sum(p["prompts"] for p in projects)
total_chars = sum(p.get("chars", 0) for p in projects)
total_gz = sum(p.get("bytes_gz", 0) for p in projects)

lines = [
    "# Higgsfield 全量项目索引",
    "",
    "> 611 个项目的去重提示词全集。每个项目一份 `prompts.jsonl.gz`（每行一条，字段 `id/cat/type/model/prompt`），"
    "项目文档在 `sources/higgsfield/projects/<项目>/`。",
    "> 检索单条提示词请用 `catalog/higgsfield-prompts.index.jsonl`，不要逐个解压项目文件。",
    "",
    f"共 **{len(projects)}** 个项目、**{total_prompts:,}** 条去重提示词，"
    f"原文 **{total_chars / 1024 / 1024:.0f} MB**，压缩后 **{total_gz / 1024 / 1024:.0f} MB**。",
    "",
    "## 怎么读",
    "",
    "1. 按下表找项目，或用 `docs/02-任务路由.md` 先定任务。",
    "2. 单条检索：`python tools/kb.py search --source higgsfield --project <项目> --limit 10`。",
    "3. 取全文：`python tools/kb.py get --id HFX-<项目>-000001`。",
    "4. 整项目通读：`zcat sources/higgsfield/prompts/<项目>/prompts.jsonl.gz`（Windows 用 Python 解压）。",
    "",
    "## 项目总表",
    "",
    "| 项目 | 主题 | 提示词 | 视频/图片 | 主要模型 | 文档 |",
    "|---|---|---:|---|---|---|",
]
for p in projects:
    theme = clean(p.get("theme", ""), 42).replace("|", "/") or "—"
    v = p.get("result_types", {}).get("video", 0)
    i = p.get("result_types", {}).get("image", 0)
    top = "、".join(f"{k}×{n}" for k, n in list(p.get("models", {}).items())[:3]) or "未标注"
    docs_dir = ROOT / "sources" / "higgsfield" / "projects" / p["project"]
    docs_cell = f"[docs](../sources/higgsfield/projects/{p['project']}/)" if docs_dir.is_dir() else "—"
    lines.append(
        f"| [{p['project']}](../sources/higgsfield/prompts/{p['project']}/) | {theme} | "
        f"{p['prompts']:,} | {v}/{i} | {top} | {docs_cell} |"
    )

lines += [
    "",
    "## 分类口径",
    "",
    "| cat | 含义 | 条数 |",
    "|---|---|---:|",
]
cat_desc = {
    "scenes": "分镜 / 镜头 / 场面调度",
    "characters": "角色设定",
    "locations": "场景设定",
    "props": "道具设定",
    "assets": "图生视频素材与重跑记录",
    "cover": "封面 / 海报",
    "all": "仅见于全量文件、未归入上述类别",
    "other": "其它",
}
for k, v in cat_total.most_common():
    lines.append(f"| `{k}` | {cat_desc.get(k, '')} | {v:,} |")

lines += [
    "",
    "## 分类覆盖",
    "",
    "**注意：不是每个项目都有分类文件。** 很多项目上游只给了一份 `_all_prompts.jsonl`，"
    "因此这些项目的全部提示词都落在 `all`。检索前先看本表，确认项目有没有 `scenes` / `characters` 等细分。",
    "",
    "| cat | 有该类目的项目数 |",
    "|---|---:|",
]
for k, v in cat_projects.most_common():
    lines.append(f"| `{k}` | {v} |")
lines += [
    "",
    f"- 只有 `all` 一个类目的项目：**{sum(1 for p in projects if set(p.get('categories', {})) == {'all'})}** 个。",
    f"- 带项目文档（brief / README / 官方 Skill）的项目：**{docs_projects}** 个。",
    "",
    "## 说明",
    "",
    "- 同一项目内按提示词原文 MD5 去重；跨项目不去重（不同项目复用同一句是有效信息）。",
    "- `cat` 取该提示词在分类文件中的最高优先归类：scenes > characters > locations > props > assets > cover > all。",
    "- `type` 由模型名推断，空值表示模型未标注。",
    "- 611 个项目来自本地全量数据包；原 78 项目 GitHub 仓是其子集，已并入，不再单独保留。",
    "- 需要按列筛选时用同目录的 `higgsfield-projects.csv`。",
    "",
]
(CAT / "higgsfield-projects.md").write_text("\n".join(lines), encoding="utf-8")

(CAT / "higgsfield-models.json").write_text(
    json.dumps({
        "projects": len(projects),
        "prompts": total_prompts,
        "chars": total_chars,
        "bytes_gzip": total_gz,
        "by_model": dict(model_total.most_common()),
        "by_category": dict(cat_total.most_common()),
        "by_result_type": dict(type_total.most_common()),
        "projects_by_category": dict(cat_projects.most_common()),
        "all_only_projects": sum(1 for p in projects if set(p.get("categories", {})) == {"all"}),
        "projects_with_docs": docs_projects,
    }, ensure_ascii=False, indent=1) + "\n",
    encoding="utf-8",
)

# 表格视图：方便在 Excel / Numbers 里筛选排序
with (CAT / "higgsfield-projects.csv").open("w", encoding="utf-8-sig", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["project", "theme", "prompts", "chars", "video", "image",
                "seedance_2_5", "seedance_2_0", "default", "top_model", "has_docs", "prompts_path"])
    for p in projects:
        w.writerow([
            p["project"], p.get("theme", ""), p["prompts"], p.get("chars", 0),
            p.get("result_types", {}).get("video", 0),
            p.get("result_types", {}).get("image", 0),
            p.get("models", {}).get("seedance_2_5", 0),
            p.get("models", {}).get("seedance_2_0", 0),
            p.get("models", {}).get("default", 0),
            next(iter(p.get("models", {})), ""),
            1 if (ROOT / "sources" / "higgsfield" / "projects" / p["project"]).is_dir() else 0,
            p["prompts_path"],
        ])

# ---------- VPL：从全库 JSONL 重建索引 ----------
VPL_SRC = ROOT / "sources" / "video-prompt-library" / "AI-全库.jsonl"
vpl_index = CAT / "video-prompt-library.index.jsonl"
vpl_rows = 0
vpl_zone = Counter()
vpl_cat = Counter()
vpl_model = Counter()
if VPL_SRC.is_file():
    with vpl_index.open("w", encoding="utf-8", newline="\n") as out:
        with VPL_SRC.open(encoding="utf-8") as fh:
            for lineno, line in enumerate(fh, 1):
                line = line.strip()
                if not line:
                    continue
                o = json.loads(line)
                vpl_rows += 1
                zone = o.get("区", "") or ""
                cat = o.get("cat", "") or ""
                sub = o.get("sub", "") or ""
                model = o.get("model", "") or ""
                original = o.get("original", "") or ""
                vpl_zone[zone] += 1
                vpl_cat[cat] += 1
                vpl_model[model or "未标注"] += 1
                out.write(json.dumps({
                    "id": f"VPL-{o.get('id', lineno)}",
                    "zone": zone,
                    "model": model,
                    "cat": cat,
                    "sub": sub,
                    "name": o.get("name") or o.get("title") or o.get("desc") or "",
                    "desc": clean(o.get("desc", "") or "", 140),
                    "tags": o.get("tags", []) or [],
                    "lang": o.get("lang", "") or "",
                    "length": len(original),
                    "line": lineno,
                    "head": clean(original, 80),
                }, ensure_ascii=False) + "\n")

# ---------- 方法表 ----------
method_rows = []
hf_methods = ROOT / "sources" / "higgsfield-knowledge-base" / "现行知识"
for sub in ["视频", "生图", "通用"]:
    d = hf_methods / sub
    if not d.is_dir():
        continue
    for f in sorted(d.glob("*.md")):
        method_rows.append({
            "id": f"H-{sub}-{f.stem.split('-')[0]}",
            "library": "higgsfield",
            "track": sub,
            "title": f.stem,
            "path": f"sources/higgsfield-knowledge-base/现行知识/{sub}/{f.name}",
            "bytes": f.stat().st_size,
        })
for f in sorted(hf_methods.glob("*.md")):
    method_rows.append({
        "id": f"H-NAV-{f.stem}",
        "library": "higgsfield",
        "track": "导航",
        "title": f.stem,
        "path": f"sources/higgsfield-knowledge-base/现行知识/{f.name}",
        "bytes": f.stat().st_size,
    })

sd_methods = ROOT / "sources" / "seedance25-knowledge-base" / "现行知识"
for f in sorted(sd_methods.glob("*.md")):
    method_rows.append({
        "id": f"SD25-{f.stem.split('-')[0]}",
        "library": "seedance-2.5",
        "track": "现行知识",
        "title": f.stem,
        "path": f"sources/seedance25-knowledge-base/现行知识/{f.name}",
        "bytes": f.stat().st_size,
    })

(CAT / "methods.json").write_text(
    json.dumps(method_rows, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
)

# ---------- 技能表 ----------
skill_rows = []
SK = ROOT / "skills"
if SK.is_dir():
    for d in sorted(SK.iterdir()):
        if not d.is_dir():
            continue
        sk = d / "SKILL.md"
        if sk.is_file():
            head = ""
            for line in sk.read_text(encoding="utf-8", errors="ignore").splitlines()[:12]:
                if line.startswith("description:"):
                    head = line.split(":", 1)[1].strip().strip('"')
                    break
            skill_rows.append({
                "name": d.name,
                "path": f"skills/{d.name}/SKILL.md",
                "description": clean(head, 160),
                "files": sum(1 for f in d.rglob("*") if f.is_file()),
            })
(CAT / "skills.json").write_text(
    json.dumps(skill_rows, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
)

# ---------- 总表 ----------
stats = {
    "schema_version": "2.0",
    "name": "本地导演助手 · 视频提示词知识库",
    "updated": date.today().isoformat(),
    "counts": {
        "higgsfield_projects": len(projects),
        "higgsfield_prompts": total_prompts,
        "higgsfield_chars": total_chars,
        "higgsfield_gzip_bytes": total_gz,
        "higgsfield_projects_with_docs": docs_projects,
        "higgsfield_all_only_projects": sum(1 for p in projects if set(p.get("categories", {})) == {"all"}),
        "video_prompt_library_entries": vpl_rows,
        "method_pages": len(method_rows),
        "skills": len(skill_rows),
        "catalog_index_rows": total_prompts + vpl_rows,
    },
    "entrypoints": {
        "start_here": "START-HERE.md",
        "human": "README.md",
        "ai": "AGENTS.md",
        "map": "INDEX.md",
        "machine": "index.json",
        "llms": "llms.txt",
        "manifest": "MANIFEST.json",
        "catalog": "catalog/README.md",
        "taxonomy": "catalog/taxonomy.md",
        "docs_map": "docs/00-文档地图.md",
        "quick_start": "docs/01-快速开始.md",
        "task_routing": "docs/02-任务路由.md",
        "retrieval": "docs/03-检索手册.md",
        "fields": "docs/04-字段与格式.md",
        "rights": "docs/05-来源版本与版权.md",
        "maintenance": "docs/06-维护与更新.md",
        "examples": "docs/07-检索案例.md",
        "report": "docs/08-构建与校验报告.md",
        "changelog": "CHANGELOG.md",
    },
    "sources": [
        {
            "id": "higgsfield-full",
            "title": "Higgsfield 611 个项目全量提示词",
            "kind": "prompt-corpus",
            "path": "sources/higgsfield/prompts/",
            "docs": "sources/higgsfield/projects/",
            "entry": "sources/higgsfield/_ENTRY.md",
            "projects": len(projects),
            "prompts": total_prompts,
            "catalog": "catalog/higgsfield-prompts.index.jsonl",
            "project_index": "catalog/higgsfield-projects.md",
        },
        {
            "id": "higgsfield-knowledge-base",
            "title": "Higgsfield 三轨方法库（视频 8 / 生图 2 / 通用 4）",
            "kind": "method",
            "path": "sources/higgsfield-knowledge-base/",
            "entry": "sources/higgsfield-knowledge-base/_ENTRY.md",
            "reading_copy": "methods/README.md#higgsfield-三轨",
        },
        {
            "id": "experience",
            "title": "官方教程、创作者博客、项目 brief、官方技能包",
            "kind": "method+reference",
            "path": "sources/experience/",
            "entry": "sources/experience/_ENTRY.md",
            "folders": ["03-全流程方法论", "05-官方教程", "05-创作者博客", "05-官方项目brief", "05-官方技能包"],
        },
        {
            "id": "video-prompt-library",
            "title": "多模型视频提示词库（主库 / 通用区 / 教程区）",
            "kind": "prompt-corpus+lexicon",
            "path": "sources/video-prompt-library/",
            "entries": vpl_rows,
            "entry": "sources/video-prompt-library/_ENTRY.md",
            "catalog": "catalog/video-prompt-library.index.jsonl",
            "guide": "catalog/video-prompt-library.md",
        },
        {
            "id": "seedance25-knowledge-base",
            "title": "Seedance 2.5 提示词方法与 Skill",
            "kind": "method+skill",
            "path": "sources/seedance25-knowledge-base/",
            "method_pages": sum(1 for m in method_rows if m["library"] == "seedance-2.5"),
            "entry": "sources/seedance25-knowledge-base/_ENTRY.md",
            "reading_copy": "methods/README.md#seedance-25",
        },
        {
            "id": "skills-repo",
            "title": "通用技能仓库（角色/道具资产表、剧本格式、Suno 音乐、图片解析）",
            "kind": "skill",
            "path": "sources/skills-repo/",
            "entry": "sources/skills-repo/_ENTRY.md",
            "reading_copy": "skills/",
        },
    ],
    "stats": {
        "higgsfield": {
            "projects": len(projects),
            "prompts": total_prompts,
            "by_model": dict(model_total.most_common()),
            "by_category": dict(cat_total.most_common()),
            "by_result_type": dict(type_total.most_common()),
        },
        "video_prompt_library": {
            "entries": vpl_rows,
            "zones": dict(vpl_zone),
            "categories": dict(vpl_cat.most_common(30)),
            "models": dict(vpl_model),
        },
    },
}
(ROOT / "index.json").write_text(
    json.dumps(stats, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
)

# ---------- MANIFEST ----------
PURPOSE = {
    "START-HERE.md": ("human", "5 分钟上手：三条路线与五个高频动作", None),
    "README.md": ("human", "总览：来源、规模、用法、目录地图", None),
    "AGENTS.md": ("ai", "AI 作业卡：读取顺序、任务路由、硬规则、引用格式", None),
    "INDEX.md": ("map", "全局地图：入口、层、任务、来源、统计", None),
    "llms.txt": ("machine", "给 AI 的最小入口（llms.txt 规范）", None),
    "index.json": ("machine", "机器总表：统计、来源、入口", None),
    "MANIFEST.json": ("machine", "本文件：每个顶层条目的用途与规模", None),
    "CHANGELOG.md": ("meta", "变更记录", None),
    "NOTICE.md": ("meta", "来源、权利与下架流程", None),
    "LICENSE": ("meta", "说明文字与工具的许可", None),
    "docs": ("docs", "使用说明：上手、路由、检索、字段、来源、维护、案例、报告", "docs/00-文档地图.md"),
    "catalog": ("index", "统一索引：项目表、分类树、逐条索引、口径", "catalog/README.md"),
    "methods": ("nav", "方法导航（正文在 sources/）", "methods/README.md"),
    "skills": ("skill", "8 个可加载技能 + 官方技能文本", "skills/README.md"),
    "sources": ("corpus", "六个来源的快照与原文", "sources/README.md"),
    "tools": ("tool", "检索、取全文、重建索引、校验", "tools/kb.py"),
    ".github": ("ci", "推送时跑快速校验", ".github/workflows/validate.yml"),
}

manifest = {
    "schema_version": "1.0",
    "name": stats["name"],
    "updated": stats["updated"],
    "entrypoints": stats["entrypoints"],
    "counts": stats["counts"],
    "items": [],
}
for name, (kind, purpose, entry) in PURPOSE.items():
    p = ROOT / name
    if not p.exists():
        continue
    if p.is_dir():
        files = [f for f in p.rglob("*") if f.is_file()]
        n, b = len(files), sum(f.stat().st_size for f in files)
    else:
        n, b = 1, p.stat().st_size
    manifest["items"].append({
        "name": name,
        "kind": kind,
        "purpose": purpose,
        "entry": entry,
        "files": n,
        "bytes": b,
    })
(ROOT / "MANIFEST.json").write_text(
    json.dumps(manifest, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
)

print(f"projects {len(projects)} prompts {total_prompts} vpl {vpl_rows} methods {len(method_rows)} skills {len(skill_rows)}")
