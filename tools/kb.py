#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""知识库检索工具：只读索引，按需回读原文。

用法：
  python tools/kb.py stats
  python tools/kb.py search --keyword 雨夜 --limit 10
  python tools/kb.py search --source higgsfield --project DETOUR --cat scenes --type video --limit 10
  python tools/kb.py search --source vpl --zone 主库 --cat 动作·打斗 --limit 10
  python tools/kb.py get --id HFX-DETOUR-000123
  python tools/kb.py get --id VPL-sd2-240 --json
"""
from __future__ import annotations

import argparse
import gzip
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAT = ROOT / "catalog"
HF_INDEX = CAT / "higgsfield-prompts.index.jsonl"
VPL_INDEX = CAT / "video-prompt-library.index.jsonl"
HF_PROMPTS = ROOT / "sources" / "higgsfield" / "prompts"
VPL_SOURCE = ROOT / "sources" / "video-prompt-library" / "AI-全库.jsonl"


def iter_jsonl(path: Path):
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue


def cmd_stats(_args):
    data = json.loads((ROOT / "index.json").read_text(encoding="utf-8"))
    counts = data.get("counts", {})
    print("知识库统计")
    print(f"  更新日期        {data.get('updated')}")
    print(f"  Higgsfield 项目  {counts.get('higgsfield_projects', 0):,}")
    print(f"  Higgsfield 提示词 {counts.get('higgsfield_prompts', 0):,}")
    print(f"  多模型库条目     {counts.get('video_prompt_library_entries', 0):,}")
    print(f"  方法页          {counts.get('method_pages', 0):,}")
    print(f"  技能            {counts.get('skills', 0):,}")
    hf = data.get("stats", {}).get("higgsfield", {})
    if hf.get("by_model"):
        print("\nHiggsfield 模型 Top 10")
        for k, v in list(hf["by_model"].items())[:10]:
            print(f"  {k or '未标注':<28} {v:>8,}")
    vpl = data.get("stats", {}).get("video_prompt_library", {})
    if vpl.get("zones"):
        print("\n多模型库分区")
        for k, v in vpl["zones"].items():
            print(f"  {k:<10} {v:>6,}")


def match_hf(o, a):
    if a.project and o.get("project") != a.project:
        return False
    if a.cat and o.get("cat") != a.cat:
        return False
    if a.model and a.model.lower() not in (o.get("model", "").lower()):
        return False
    if a.type and o.get("type") != a.type:
        return False
    n = o.get("len", 0)
    if a.min_length and n < a.min_length:
        return False
    if a.max_length and n > a.max_length:
        return False
    if a.keyword:
        hay = " ".join([
            o.get("head", ""),
            o.get("project", ""),
            o.get("cat", ""),
            o.get("model", ""),
        ]).lower()
        if a.keyword.lower() not in hay:
            return False
    return True


def match_vpl(o, a):
    if a.zone and o.get("zone") != a.zone:
        return False
    if a.cat and a.cat not in (o.get("cat", "") or ""):
        return False
    if a.sub and a.sub not in (o.get("sub", "") or ""):
        return False
    if a.model and a.model.lower() not in (o.get("model", "") or "").lower():
        return False
    n = o.get("length", 0)
    if a.min_length and n < a.min_length:
        return False
    if a.max_length and n > a.max_length:
        return False
    if a.tags:
        tags = o.get("tags", []) or []
        for t in a.tags:
            if t not in tags:
                return False
    if a.keyword:
        hay = " ".join([
            o.get("head", ""),
            o.get("name", ""),
            o.get("desc", ""),
            o.get("cat", ""),
            o.get("sub", ""),
            " ".join(o.get("tags", []) or []),
        ]).lower()
        if a.keyword.lower() not in hay:
            return False
    return True


def cmd_search(a):
    out = sys.stdout
    total = 0
    if a.source in ("all", "higgsfield") and HF_INDEX.is_file():
        for o in iter_jsonl(HF_INDEX):
            if not match_hf(o, a):
                continue
            out.write(
                f"{o['id']}\tHiggsfield\t{o['project']}\t{o.get('cat','')}\t"
                f"{o.get('type','')}\t{o.get('model','') or '未标注'}\t{o.get('len',0)}\t"
                f"{o.get('head','')[:90]}\n"
            )
            total += 1
            if total >= a.limit:
                break
    if total < a.limit and a.source in ("all", "vpl") and VPL_INDEX.is_file():
        for o in iter_jsonl(VPL_INDEX):
            if not match_vpl(o, a):
                continue
            out.write(
                f"{o['id']}\tVPL\t{o.get('zone','')}/{o.get('cat','')}/{o.get('sub','')}\t"
                f"{o.get('model','') or '未标注'}\t{o.get('length',0)}\t"
                f"{o.get('name','') or o.get('head','')[:60]}\n"
            )
            total += 1
            if total >= a.limit:
                break
    if total == 0:
        print("没有匹配。放宽条件，或换 --keyword。", file=sys.stderr)
        return 1
    print(f"\n# {total} 条。用 python tools/kb.py get --id <ID> 取全文", file=sys.stderr)
    return 0


def cmd_get(a):
    ident = a.id.strip()
    if ident.startswith("HFX-"):
        # HFX-<PROJECT>-<6位>
        body = ident[4:]
        project, _, seq = body.rpartition("-")
        if not project or not seq.isdigit():
            print(f"ID 格式不对：{ident}", file=sys.stderr)
            return 1
        path = HF_PROMPTS / project / "prompts.jsonl.gz"
        if not path.is_file():
            print(f"找不到项目文件：{path}", file=sys.stderr)
            return 1
        target = int(seq)
        with gzip.open(path, "rt", encoding="utf-8") as fh:
            for n, line in enumerate(fh, 1):
                if n == target:
                    o = json.loads(line)
                    if a.json:
                        print(json.dumps(o, ensure_ascii=False, indent=2))
                    else:
                        print(o.get("prompt", ""))
                    return 0
        print(f"第 {target} 行不存在", file=sys.stderr)
        return 1

    if ident.startswith("VPL-"):
        raw = ident[4:]
        for o in iter_jsonl(VPL_SOURCE):
            if o.get("id") == raw:
                if a.json:
                    print(json.dumps(o, ensure_ascii=False, indent=2))
                else:
                    print(f"# {o.get('name','')}\n# {o.get('zone','')}/{o.get('cat','')}/{o.get('sub','')} | {o.get('model','') or '未标注'}\n")
                    print(o.get("original", ""))
                    if o.get("zh"):
                        print("\n--- 中文译文 ---\n")
                        print(o["zh"])
                return 0
        print(f"找不到 VPL 条目：{raw}", file=sys.stderr)
        return 1

    print("只支持 HFX-<项目>-<六位行号> 与 VPL-<原id>。", file=sys.stderr)
    return 1


def main():
    p = argparse.ArgumentParser(description="视频提示词知识库检索")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("stats", help="看统计").set_defaults(func=cmd_stats)

    s = sub.add_parser("search", help="检索轻量索引")
    s.add_argument("--source", choices=["all", "higgsfield", "vpl"], default="all")
    s.add_argument("--keyword")
    s.add_argument("--project")
    s.add_argument("--cat")
    s.add_argument("--sub")
    s.add_argument("--model")
    s.add_argument("--type", choices=["video", "image", ""])
    s.add_argument("--zone")
    s.add_argument("--tags", help="逗号分隔，全部命中")
    s.add_argument("--min-length", type=int, dest="min_length")
    s.add_argument("--max-length", type=int, dest="max_length")
    s.add_argument("--limit", type=int, default=20)
    s.set_defaults(func=cmd_search)

    g = sub.add_parser("get", help="按 ID 取全文")
    g.add_argument("--id", required=True)
    g.add_argument("--json", action="store_true")
    g.set_defaults(func=cmd_get)

    a = p.parse_args()
    if getattr(a, "tags", None):
        a.tags = [x.strip() for x in a.tags.split(",") if x.strip()]
    sys.exit(a.func(a))


if __name__ == "__main__":
    main()
