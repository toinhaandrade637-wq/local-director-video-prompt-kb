#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""发布前校验：链接、计数、索引可回读、敏感信息、绝对路径。"""
from __future__ import annotations

import gzip
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []
warnings = []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def rel_targets(md: Path, text: str):
    for m in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", text):
        t = m.group(1).strip()
        if t.startswith(("http://", "https://", "#", "mailto:")):
            continue
        t = t.split("#", 1)[0]
        if not t:
            continue
        # Windows 绝对路径不是仓库内链接；在 Linux 上会被误当成相对路径
        if re.match(r"^[A-Za-z]:[\\/]", t):
            warn(f"指向本机路径（未入库）：{md.relative_to(ROOT)} -> {t[:48]}")
            continue
        yield (md.parent / t).resolve()


def check_links():
    n = 0
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts:
            continue
        try:
            text = md.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for tgt in rel_targets(md, text):
            n += 1
            if ROOT not in tgt.parents and tgt != ROOT:
                # 指向仓库外
                warn(f"指向仓外链接：{md.relative_to(ROOT)} -> {tgt}")
                continue
            if not tgt.exists():
                suffix = tgt.suffix.lower()
                if suffix in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".mp4", ".mov", ".pdf"}:
                    warn(f"缺失素材（原图/附件未入库）：{md.relative_to(ROOT)} -> {tgt.name}")
                elif re.match(r"^image_\d+$", tgt.name):
                    warn(f"输入图占位引用（非文件）：{md.relative_to(ROOT)} -> {tgt.name}")
                else:
                    err(f"失效链接：{md.relative_to(ROOT)} -> {tgt.relative_to(ROOT) if ROOT in tgt.parents else tgt}")
    print(f"links checked: {n}")


def check_index(fast: bool = False):
    idx = ROOT / "catalog" / "higgsfield-prompts.index.jsonl"
    if not idx.is_file():
        err("缺少 higgsfield-prompts.index.jsonl")
        return
    rows = 0
    per_project = Counter()
    with idx.open(encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            rows += 1
            o = json.loads(line)
            per_project[o["project"]] += 1
            if not o.get("id", "").startswith("HFX-"):
                err(f"索引 ID 异常：{o.get('id')}")
    data = json.loads((ROOT / "index.json").read_text(encoding="utf-8"))
    expect = data["counts"]["higgsfield_prompts"]
    if rows != expect:
        err(f"索引行数 {rows} 与 index.json {expect} 不一致")
    else:
        print(f"higgsfield index rows: {rows}")

    if fast:
        print(f"projects in index: {len(per_project)} (fast mode: 未逐项目核对压缩文件)")
    else:
        for project, count in per_project.items():
            p = ROOT / "sources" / "higgsfield" / "prompts" / project / "prompts.jsonl.gz"
            if not p.is_file():
                err(f"缺少项目语料：{project}")
                continue
            with gzip.open(p, "rt", encoding="utf-8") as fh:
                n = sum(1 for line in fh if line.strip())
            if n != count:
                err(f"{project} 行数不一致：索引 {count} / 文件 {n}")
        print(f"projects verified: {len(per_project)}")

    vpl = ROOT / "catalog" / "video-prompt-library.index.jsonl"
    if not vpl.is_file():
        err("缺少 video-prompt-library.index.jsonl")
    else:
        n = sum(1 for line in vpl.open(encoding="utf-8") if line.strip())
        if n != data["counts"]["video_prompt_library_entries"]:
            err(f"VPL 索引 {n} 与 index.json 不一致")
        else:
            print(f"vpl index rows: {n}")


SECRET_PATTERNS = [
    (re.compile(r"gh[pousr]_[A-Za-z0-9]{30,}"), "GitHub token"),
    (re.compile(r"github_pat_[A-Za-z0-9_]{30,}"), "GitHub PAT"),
    (re.compile(r"sk-[A-Za-z0-9]{24,}"), "OpenAI key"),
    (re.compile(r"AKIA[0-9A-Z]{16}"), "AWS key"),
    (re.compile(r"xox[baprs]-[A-Za-z0-9-]{20,}"), "Slack token"),
    (re.compile(r"-----BEGIN (RSA |OPENSSH )?PRIVATE KEY-----"), "private key"),
]
ABS_PATTERNS = [
    re.compile(r"[A-Za-z]:\\Users\\"),
    re.compile(r"D:\\本地导演助手"),
    re.compile(r"D:\\higgsfield"),
]


def check_secrets():
    hits = 0
    for f in ROOT.rglob("*"):
        if not f.is_file() or ".git" in f.parts:
            continue
        if f.suffix.lower() not in {".md", ".txt", ".json", ".jsonl", ".py", ".js", ".html", ".csv"}:
            continue
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for pat, label in SECRET_PATTERNS:
            for m in pat.finditer(text):
                hits += 1
                err(f"疑似 {label}：{f.relative_to(ROOT)} -> {m.group(0)[:12]}…")
        if f.parts[-2:-1] and f.parts[-2] in {"docs", "catalog", "methods", "skills", "tools"}:
            for pat in ABS_PATTERNS:
                if pat.search(text):
                    warn(f"文档含本机绝对路径：{f.relative_to(ROOT)}")
                    break
    print(f"secret scan hits: {hits}")


def check_required():
    for name in ["README.md", "AGENTS.md", "INDEX.md", "index.json", "NOTICE.md", "START-HERE.md", "MANIFEST.json"]:
        if not (ROOT / name).is_file():
            err(f"缺少 {name}")
    for name in ["00-文档地图.md", "01-快速开始.md", "02-任务路由.md", "03-检索手册.md",
                 "04-字段与格式.md", "05-来源版本与版权.md", "06-维护与更新.md",
                 "07-检索案例.md", "08-构建与校验报告.md"]:
        if not (ROOT / "docs" / name).is_file():
            err(f"缺少 docs/{name}")
    for name in ["higgsfield-projects.md", "higgsfield-projects.csv", "taxonomy.md",
                 "video-prompt-library.md", "README.md"]:
        if not (ROOT / "catalog" / name).is_file():
            err(f"缺少 catalog/{name}")


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--fast", action="store_true", help="跳过逐项目压缩文件核对（CI 用）")
    args = ap.parse_args()
    check_required()
    check_index(fast=args.fast)
    check_links()
    check_secrets()
    print()
    if warnings:
        print(f"警告 {len(warnings)}")
        for w in warnings[:30]:
            print("  !", w)
    if errors:
        print(f"错误 {len(errors)}")
        for e in errors[:50]:
            print("  x", e)
        sys.exit(1)
    print("OK")


if __name__ == "__main__":
    main()
