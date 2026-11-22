"""Generate self-contained Skill references from active canonical knowledge only."""
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = Path("skills/seedance-prompt/references")
MARKER = "<!-- Generated from canonical knowledge. Edit the source, then run build_skill_refs.py. -->"
ACTIVE = {"trial", "validated"}
STATUSES = ACTIVE | {"deprecated", "withdrawn"}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def normalized(path):
    return path.read_text(encoding="utf-8-sig").replace("\r\n", "\n")


def canonical_pages(root):
    return sorted(p for p in (root / "现行知识").glob("*.md")
                  if re.fullmatch(r"\d+-.+\.md", p.name))


def page_status(text, name):
    match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
    if not match:
        raise ValueError(f"Missing frontmatter: {name}")
    values = re.findall(r"^status:\s*([^\n]+)$", match.group(1), re.M)
    if len(values) != 1 or values[0].strip().strip("\"'") not in STATUSES:
        raise ValueError(f"Missing, duplicate or invalid status: {name}")
    return values[0].strip().strip("\"'")


def expected(root):
    root = root.resolve()
    config = json.loads((root / "维护/repository.json").read_text(encoding="utf-8"))
    pages = canonical_pages(root)
    if not pages:
        raise ValueError("No canonical knowledge pages found")
    selected = []
    for p in pages:
        if not p.resolve().is_relative_to(root) or p.is_symlink():
            raise ValueError(f"Unsafe canonical source: {p.name}")
        if page_status(normalized(p), p.name) in ACTIVE:
            selected.append(p)
    outputs, entries = {}, []
    for src in selected + [root / "资料库/来源登记.md"]:
        if not src.resolve().is_relative_to(root) or src.is_symlink():
            raise ValueError(f"Unsafe reference source: {src.name}")
        original = normalized(src)
        name = src.name if src.parent.name == "现行知识" else "source-registry.md"
        body = original.replace("../资料库/来源登记.md", "source-registry.md")
        body = body.replace("机器可读记录见[来源登记.json](来源登记.json)。", "本页为随 Skill 发布的来源元信息；快照版本见[manifest](manifest.json)。")
        if src.parent.name == "现行知识":
            body = re.sub(r"\A---\n.*?\n---\n?", "", body, count=1, flags=re.S).lstrip("\n")
        else:
            sources = json.loads((root / "资料库/来源登记.json").read_text(encoding="utf-8"))["sources"]
            body = "# 方法与示例出处\n\n" + "\n".join(
                f"- {s['id']}：{s['title']}" + (f" — {s['url']}" if s.get('url') else "") for s in sources) + "\n"
        body = MARKER + "\n\n" + body
        outputs[name] = body.encode("utf-8")
        entries.append({"source": src.relative_to(root).as_posix(), "reference": name,
                        "source_sha256": digest(original.encode("utf-8")),
                        "reference_sha256": digest(outputs[name])})
    manifest = {"schema_version": 1, "knowledge_version": config["version"],
                "skill_version": config["version"],
                "generation_validation": config.get("generation_validation", "not-executed"),
                "normalization": "UTF-8 without BOM, LF line endings", "files": entries}
    outputs["manifest.json"] = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    return outputs


def check(root):
    outputs = expected(root)
    target = root / TARGET
    errors = []
    actual = {p.name for p in target.iterdir() if p.is_file()} if target.exists() else set()
    for name, data in outputs.items():
        p = target / name
        if p.is_symlink() or not p.resolve().is_relative_to(root.resolve()):
            errors.append(f"Unsafe generated reference: {name}")
        elif not p.exists() or normalized(p).encode("utf-8") != data:
            errors.append(f"Missing or stale generated reference: {name}")
    for name in actual - set(outputs):
        errors.append(f"Unexpected generated reference: {name}")
    return errors


def build(root):
    root = root.resolve()
    target = root / TARGET
    target.mkdir(parents=True, exist_ok=True)
    if target.is_symlink() or not target.resolve().is_relative_to(root):
        raise ValueError("Unsafe reference directory")
    outputs = expected(root)
    extras = [p for p in target.iterdir() if p.is_file() and p.name not in outputs]
    for p in extras:
        if p.is_symlink() or not p.resolve().is_relative_to(target.resolve()) or MARKER not in normalized(p):
            raise ValueError(f"Review unexpected unowned reference before rebuilding: {p.name}")
    # Only obsolete files carrying this generator's ownership marker are removed.
    for p in extras:
        p.unlink()
    for name, data in outputs.items():
        p = target / name
        if p.is_symlink():
            raise ValueError(f"Refuse to overwrite a symlink: {name}")
        p.write_bytes(data)
    return len(outputs) - 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        if args.check:
            errors = check(args.root.resolve())
            print("\n".join(errors) if errors else "Skill references are current.")
            return bool(errors)
        print(f"Built {build(args.root)} references and version manifest.")
        return 0
    except (ValueError, OSError, KeyError) as exc:
        print(f"Reference build failed: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
