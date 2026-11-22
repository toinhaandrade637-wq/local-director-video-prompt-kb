# -*- coding: utf-8 -*-
"""重建统一索引：项目表、模型分布、方法表、技能表、总入口 index.json。"""
from __future__ import annotations

import json
import re
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAT = ROOT / "catalog"
CAT.mkdir(parents=True, exist_ok=True)


def clean(s: str, n: int = 60) -> str:
    s = re.sub(r"\s+", " ", s or "").strip()
    return s[:n]


def size_mb(p: Path) -> float:
    if p.is_file():
        return p.stat().st_size / 1024 / 1024
    return sum(f.stat().st_size for f in p.rglob("*") if f.is_file()) / 1024 / 1024


# ---------- Higgsfield 项目 ----------
projects = json.loads((CAT / "higgsfield-projects.json").read_text(encoding="utf-8"))

model_total = Counter()
cat_total = Counter()
type_total = Counter()
for p in projects:
    for k, v in p.get("models", {}).items():
        model_total[k] += v
    for k, v in p.get("categories", {}).items():
        cat_total[k] += v
    for k, v in p.get("result_types", {}).items():
        type_total[k] += v

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
    "## 说明",
    "",
    "- 同一项目内按提示词原文 MD5 去重；跨项目不去重（不同项目复用同一句是有效信息）。",
    "- `cat` 取该提示词在分类文件中的最高优先归类：scenes > characters > locations > props > assets > cover > all。",
    "- `type` 由模型名推断，空值表示模型未标注。",
    "- 611 个项目来自本地全量数据包；原 78 项目 GitHub 仓是其子集，已并入，不再单独保留。",
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
    }, ensure_ascii=False, indent=1) + "\n",
    encoding="utf-8",
)

# ---------- VPL ----------
vpl_index = CAT / "video-prompt-library.index.jsonl"
vpl_rows = 0
vpl_zone = Counter()
vpl_cat = Counter()
vpl_model = Counter()
if vpl_index.is_file():
    with vpl_index.open(encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            o = json.loads(line)
            vpl_rows += 1
            vpl_zone[o.get("zone", "")] += 1
            vpl_cat[o.get("cat", "")] += 1
            vpl_model[o.get("model", "") or "未标注"] += 1

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
        "video_prompt_library_entries": vpl_rows,
        "method_pages": len(method_rows),
        "skills": len(skill_rows),
        "catalog_index_rows": total_prompts + vpl_rows,
    },
    "entrypoints": {
        "human": "README.md",
        "ai": "AGENTS.md",
        "map": "INDEX.md",
        "machine": "index.json",
        "catalog": "catalog/README.md",
        "task_routing": "docs/02-任务路由.md",
        "retrieval": "docs/03-检索手册.md",
        "fields": "docs/04-字段与格式.md",
        "rights": "docs/05-来源版本与版权.md",
        "maintenance": "docs/06-维护与更新.md",
    },
    "sources": [
        {
            "id": "higgsfield-full",
            "title": "Higgsfield 611 个项目全量提示词",
            "kind": "prompt-corpus",
            "path": "sources/higgsfield/prompts/",
            "docs": "sources/higgsfield/projects/",
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
            "reading_copy": "methods/higgsfield/",
        },
        {
            "id": "experience",
            "title": "官方教程、创作者博客、项目 brief、官方技能包",
            "kind": "method+reference",
            "path": "sources/experience/",
            "folders": ["03-全流程方法论", "05-官方教程", "05-创作者博客", "05-官方项目brief", "05-官方技能包"],
        },
        {
            "id": "video-prompt-library",
            "title": "多模型视频提示词库（主库 / 通用区 / 教程区）",
            "kind": "prompt-corpus+lexicon",
            "path": "sources/video-prompt-library/",
            "entries": vpl_rows,
            "catalog": "catalog/video-prompt-library.index.jsonl",
            "guide": "catalog/video-prompt-library.md",
        },
        {
            "id": "seedance25-knowledge-base",
            "title": "Seedance 2.5 提示词方法与 Skill",
            "kind": "method+skill",
            "path": "sources/seedance25-knowledge-base/",
            "method_pages": sum(1 for m in method_rows if m["library"] == "seedance-2.5"),
            "reading_copy": "methods/seedance-2.5/",
        },
        {
            "id": "skills-repo",
            "title": "通用技能仓库（角色/道具资产表、剧本格式、Suno 音乐、图片解析）",
            "kind": "skill",
            "path": "sources/skills-repo/",
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

print(f"projects {len(projects)} prompts {total_prompts} vpl {vpl_rows} methods {len(method_rows)} skills {len(skill_rows)}")
