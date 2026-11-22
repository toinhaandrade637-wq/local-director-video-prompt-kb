"""Lint structure and recorded claims; this is not an automatic semantic proof."""
import argparse
import ast
import hashlib
import html
import json
import os
import re
import shlex
import shutil
import subprocess
import unicodedata
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import unquote, urlsplit
from build_skill_refs import ROOT, ACTIVE, STATUSES, check as check_refs, normalized

ALLOWED = re.compile(
    r"(?:README\.md|AGENTS\.md|index\.(?:md|json)|\.gitignore|\.gitattributes|"
    r"资料库/.+\.(?:md|json|txt|ps1|jpg)|研究记录/.+\.(?:md|json|txt|ps1)|现行知识/[^/]+\.md|"
    r"(?:项目入口|知识库搭建方案_讨论稿_v0\.1|Seedance2\.5_提示词结构_讨论稿_v0\.1|Seedance2\.5知识库_建设蓝图)\.md|"
    r"实践记录/(?:任务索引|任务模板|反馈模板)\.md|"
    r"维护/[^/]+\.(?:md|py)|维护/(?:publish_files|repository|semantic_review)\.json|"
    r"维护/events\.jsonl|维护/固定验证任务/[^/]+\.md|"
    r"skills/seedance-prompt/SKILL\.md|skills/seedance-prompt/agents/openai\.yaml|"
    r"skills/seedance-prompt/references/(?:[^/]+\.md|manifest\.json)|"
    r"\.github/workflows/validate\.yml)\Z")
NAV = {"现行知识/索引.md", "现行知识/按任务查.md", "现行知识/按问题查.md"}
REQUIRED = {"README.md", "AGENTS.md", "index.md", "index.json", ".gitignore", ".gitattributes",
            "资料库/来源登记.md", "资料库/来源登记.json", "维护/publish_files.json",
            "维护/repository.json", "维护/events.jsonl", "维护/semantic_review.json",
            "维护/catalog.py", "维护/check_kb.py", "维护/build_skill_refs.py", "维护/test_kb.py",
            "维护/工作流程.md", "维护/更新记录.md", "维护/待验证问题.md",
            "skills/seedance-prompt/SKILL.md", "skills/seedance-prompt/agents/openai.yaml",
            "skills/seedance-prompt/references/manifest.json", ".github/workflows/validate.yml"} | NAV
KINDS = {"authorized-experience", "official-document", "official-link", "official-skill-reference",
         "structure-reference", "user-convention", "user-image", "user-prompt"}
STORAGE = {"derived-only", "link-only", "local-only", "private-repo"}
PAGE_FIELDS = {"id", "status", "review", "generation_validation", "updated", "sources",
               "reviewed_on", "review_after", "topics", "generation_evidence"}
SECRETS = [re.compile(r"gh[pousr]_[A-Za-z0-9]{30,}"),
           re.compile(r"github_pat_[A-Za-z0-9_]{40,}"),
           re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----")]


def string(value):
    return isinstance(value, str) and bool(value.strip())


def archive(name):
    return (name.startswith(("资料库/", "研究记录/")) and name not in {"资料库/来源登记.md", "资料库/来源登记.json"}) or name in {
        "项目入口.md", "知识库搭建方案_讨论稿_v0.1.md", "Seedance2.5_提示词结构_讨论稿_v0.1.md", "Seedance2.5知识库_建设蓝图.md"}


def scalar(value):
    value = value.strip()
    if value.startswith("["):
        if not value.endswith("]"):
            raise ValueError("Unclosed inline list")
        lexer = shlex.shlex(value[1:-1], posix=True)
        lexer.whitespace = ","
        lexer.whitespace_split = True
        lexer.commenters = ""
        return [item.strip() for item in lexer if item.strip()]
    if value.startswith(("'", '"')):
        result = ast.literal_eval(value)
        if not isinstance(result, str):
            raise ValueError("Expected quoted string")
        return result
    if value.startswith(("{", "|", ">", "&", "*")):
        raise ValueError("Unsupported frontmatter syntax; use flat scalars and inline lists")
    return value


def frontmatter(text):
    """Strict project subset, deliberately not a full YAML parser."""
    match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
    if not match:
        raise ValueError("Missing or unclosed frontmatter")
    result = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        item = re.fullmatch(r"([A-Za-z_][\w-]*):\s*(.*)", line)
        if not item:
            raise ValueError("Unsupported frontmatter line; use a flat key/value mapping")
        key, value = item.groups()
        if key in result:
            raise ValueError(f"Duplicate frontmatter key: {key}")
        result[key] = scalar(value)
    return result


def body_text(text):
    from catalog import body_text as canonical_body_text
    return canonical_body_text(text)


def iso_date(value):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ValueError("Expected ISO date YYYY-MM-DD")
    return date.fromisoformat(value)


def timestamp(value):
    if not string(value):
        raise ValueError("Missing timestamp")
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("Timestamp must have timezone")
    return parsed


def git_executable():
    found = shutil.which("git")
    if not found and os.name == "nt":
        p = Path(os.environ.get("ProgramFiles", "C:/Program Files")) / "Git/cmd/git.exe"
        if p.is_file():
            found = str(p)
    if not found:
        raise OSError("git unavailable")
    return found


def git(root, *args, required=True):
    result = subprocess.run([git_executable(), *args], cwd=root, capture_output=True)
    if required and result.returncode:
        raise ValueError("Git command failed: " + " ".join(args[:2]))
    return result


def discover(root):
    found = {name for name in REQUIRED if (root / name).is_file()}
    dirs = ["现行知识", "实践记录", "维护", "维护/固定验证任务",
            "skills/seedance-prompt", "skills/seedance-prompt/agents",
            "skills/seedance-prompt/references", ".github/workflows"]
    for directory in dirs:
        for p in (root / directory).glob("*"):
            if p.is_file() and ALLOWED.fullmatch(p.relative_to(root).as_posix()):
                found.add(p.relative_to(root).as_posix())
    return found


def without_fences(text):
    lines, marker = [], None
    for line in text.splitlines():
        m = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if m:
            if marker is None:
                marker = m.group(1)[0]
            elif marker == m.group(1)[0]:
                marker = None
            continue
        if marker is None:
            lines.append(line)
    return "\n".join(lines)


def heading_anchors(text):
    text = without_fences(body_text(text))
    anchors, counts = set(), defaultdict(int)
    headings = re.findall(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", text, re.M)
    headings += re.findall(r"^([^\n]+)\n(?:={3,}|-{3,})\s*$", text, re.M)
    for heading in headings:
        heading = re.sub(r"<[^>]*>", "", html.unescape(heading))
        heading = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", heading)
        slug = "".join(c for c in heading.lower()
                       if c in "-_ " or c.isalnum() or unicodedata.category(c).startswith("M"))
        slug = slug.replace(" ", "-")
        suffix = "" if counts[slug] == 0 else "-" + str(counts[slug])
        anchors.add(slug + suffix)
        counts[slug] += 1
    anchors.update(re.findall(r'<a\s+[^>]*(?:id|name)=["\']([^"\']+)["\']', text, re.I))
    return anchors


def destination(raw):
    raw = raw.strip()
    if raw.startswith("<"):
        end = raw.find(">")
        if end < 0:
            raise ValueError("Unclosed angle-bracket link")
        dest, rest = raw[1:end], raw[end + 1:].strip()
    else:
        match = re.match(r"(\S+)(?:\s+(.*))?$", raw, re.S)
        if not match:
            raise ValueError("Empty link destination")
        dest, rest = match.group(1), (match.group(2) or "").strip()
    if rest and not re.fullmatch(r'''(?:"[^"]*"|'[^']*'|\([^)]*\))''', rest, re.S):
        raise ValueError("Unsupported link title syntax")
    return re.sub(r"\\([() ])", r"\1", dest)


def markdown_links(text):
    """Inline, angle destinations and common full/collapsed/shortcut references."""
    text = without_fences(text)
    text = re.sub(r"`+[^`\n]*`+", "", text)
    problems, targets, definitions = [], [], {}
    if re.search(r"\[\[[^\n]+\]\]", text):
        problems.append("Unsupported wiki link; use Markdown links")
    if re.search(r"<a\s+[^>]*href\s*=", text, re.I):
        problems.append("Unsupported HTML href; use Markdown links")
    definition_pattern = r"^\s{0,3}\[([^\]\n]+)\]:\s*(.+)$"
    for m in re.finditer(definition_pattern, text, re.M):
        key = " ".join(m.group(1).lower().split())
        try:
            if key in definitions:
                raise ValueError("Duplicate reference-link definition")
            definitions[key] = destination(m.group(2))
        except ValueError as exc:
            problems.append(str(exc))
    text = re.sub(definition_pattern, "", text, flags=re.M)
    position = 0
    while True:
        m = re.search(r"!?\[([^\]\n]+)\]", text[position:])
        if not m:
            break
        label = m.group(1)
        end = position + m.end()
        position = end
        if end < len(text) and text[end] == "(":
            depth, quote, angle, j = 1, None, False, end + 1
            while j < len(text) and depth:
                c = text[j]
                if c == "\\":
                    j += 2
                    continue
                if quote:
                    if c == quote:
                        quote = None
                elif c in "\"'" and (j == end + 1 or text[j - 1].isspace()):
                    quote = c
                elif c == "<":
                    angle = True
                elif c == ">":
                    angle = False
                elif not angle and c == "(":
                    depth += 1
                elif not angle and c == ")":
                    depth -= 1
                j += 1
            if depth:
                problems.append("Unclosed Markdown link")
                continue
            try:
                targets.append(destination(text[end + 1:j - 1]))
            except ValueError as exc:
                problems.append(str(exc))
            position = j
        else:
            ref = re.match(r"\[([^\]\n]*)\]", text[end:])
            key = " ".join((ref.group(1) or label).lower().split()) if ref else " ".join(label.lower().split())
            if ref:
                position += ref.end()
                if key not in definitions:
                    problems.append(f"Undefined reference link: {key}")
            if key in definitions:
                targets.append(definitions[key])
    return targets, problems


def catalog_errors(root):
    from catalog import check
    return check(root)


def validate(root, base_ref=None, today=None):
    root = root.resolve()
    today = today or datetime.now(timezone(timedelta(hours=8))).date()
    errors, warnings = [], []
    listing = json.loads((root / "维护/publish_files.json").read_text(encoding="utf-8"))
    files = listing.get("files")
    if not isinstance(files, list) or not all(string(n) for n in files):
        raise ValueError("Publish files must be a list of nonempty strings")
    if len(files) != len(set(files)):
        errors.append("Duplicate entries in publish manifest")
    file_set = set(files)
    for name in sorted(REQUIRED - file_set):
        errors.append(f"Required publish file absent from manifest: {name}")
    for name in sorted(discover(root) - file_set):
        errors.append(f"Unlisted authored file: {name}")
    texts = {}
    for name in files:
        if not ALLOWED.fullmatch(name):
            errors.append(f"Disallowed publish path: {name}")
            continue
        p = root / name
        if p.is_symlink() or not p.resolve().is_relative_to(root) or not p.is_file():
            errors.append(f"Missing or unsafe publish file: {name}")
            continue
        try:
            if p.suffix.lower() == ".jpg":
                continue
            texts[name] = normalized(p)
        except UnicodeError:
            errors.append(f"Non-UTF-8 publish file: {name}")
            continue
        if any(pattern.search(texts[name]) for pattern in SECRETS):
            errors.append(f"Credential-like content: {name} (value withheld)")
    config = json.loads(texts.get("维护/repository.json", "{}"))
    version = config.get("version", "")
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:-[\w.-]+)?", version):
        errors.append("Invalid repository version")
    if not any(f"**{version} {label}**" in texts.get("README.md", "") for label in ("试用版", "现行版")):
        errors.append("README current version differs from repository.json")
    registry = json.loads(texts.get("资料库/来源登记.json", '{"sources":[]}'))
    records = registry.get("sources")
    if not isinstance(records, list):
        raise ValueError("Source registry requires a sources list")
    ids = set()
    for source in records:
        if not isinstance(source, dict):
            errors.append("Source entry must be an object")
            continue
        sid = source.get("id")
        if not isinstance(sid, str) or not re.fullmatch(r"[A-Z]\d{3}", sid):
            errors.append("Invalid source ID")
            continue
        if sid in ids:
            errors.append(f"Duplicate source ID: {sid}")
        ids.add(sid)
        for key in ("title", "evidence"):
            if not string(source.get(key)):
                errors.append(f"Source {sid} needs nonempty {key}")
        if source.get("kind") not in KINDS or source.get("storage") not in STORAGE:
            errors.append(f"Invalid source kind/storage: {sid}")
        for key in ("snapshot_date", "text_reviewed_on", "current_verified_on"):
            if source.get(key) is not None:
                try:
                    if iso_date(source[key]) > today:
                        raise ValueError("future date")
                except ValueError:
                    errors.append(f"Invalid source date {key}: {sid}")
        if "media_reviewed" in source and not isinstance(source["media_reviewed"], bool):
            errors.append(f"Source media_reviewed must be boolean: {sid}")
    pages = {n: t for n, t in texts.items() if re.match(r"现行知识/\d+-", n)}
    metadata, id_to_path = {}, {}
    for name, text in pages.items():
        try:
            meta = frontmatter(text)
        except (ValueError, SyntaxError) as exc:
            errors.append(f"{name}: {exc}")
            continue
        metadata[name] = meta
        if set(meta) - PAGE_FIELDS:
            errors.append(f"Unknown page metadata: {name}: {sorted(set(meta) - PAGE_FIELDS)}")
        prefix = re.match(r"现行知识/(\d+)-", name).group(1)
        kid = meta.get("id")
        if kid != "K" + prefix:
            errors.append(f"Knowledge ID must match filename: {name}")
        if isinstance(kid, str):
            if kid in id_to_path:
                errors.append(f"Duplicate knowledge ID: {kid}")
            id_to_path[kid] = name
        if meta.get("status") not in STATUSES:
            errors.append(f"Invalid knowledge status: {name}")
        if meta.get("review") not in {"text-reviewed", "needs-review"}:
            errors.append(f"Invalid review state: {name}")
        if meta.get("generation_validation") not in {"not-independently-tested", "user-reported", "independently-tested"}:
            errors.append(f"Invalid generation-validation state: {name}")
        if meta.get("generation_validation") == "independently-tested" and not meta.get("generation_evidence"):
            errors.append(f"Independent validation needs generation_evidence: {name}")
        dates = {}
        for key in ("updated", "reviewed_on", "review_after"):
            try:
                dates[key] = iso_date(meta.get(key))
            except (TypeError, ValueError):
                errors.append(f"Invalid or missing {key}: {name}")
        if dates.get("reviewed_on", today) > today or dates.get("updated", today) > today:
            errors.append(f"Knowledge date is in the future: {name}")
        if dates.get("review_after", today) < dates.get("reviewed_on", today):
            errors.append(f"review_after precedes reviewed_on: {name}")
        if meta.get("status") in ACTIVE:
            if dates.get("review_after", today) < today:
                warnings.append(f"Review overdue (not automatically invalid): {name}")
            if meta.get("review") == "needs-review":
                warnings.append(f"Needs text review: {name}")
        for field in ("sources", "topics"):
            values = meta.get(field)
            if not isinstance(values, list) or not values or not all(string(v) for v in values):
                errors.append(f"Nonempty inline list required for {field}: {name}")
            elif field == "sources":
                for sid in values:
                    if sid not in ids:
                        errors.append(f"Unknown source {sid}: {name}")
    if not pages:
        errors.append("No canonical knowledge pages")
    graph = defaultdict(set)
    anchors = {n: heading_anchors(t) for n, t in texts.items() if n.endswith(".md")}
    for name, text in texts.items():
        if not name.endswith(".md") or archive(name):
            continue
        targets, problems = markdown_links(text)
        errors.extend(f"{name}: {problem}" for problem in problems)
        for raw in targets:
            if re.match(r"^[A-Za-z]:", raw) or raw.startswith(("/", "\\")):
                errors.append(f"Absolute local link prohibited: {name}")
                continue
            parts = urlsplit(raw)
            if parts.scheme:
                if parts.scheme.lower() not in {"http", "https", "mailto"}:
                    errors.append(f"Unsupported or local link scheme: {name}")
                continue
            p = (root / name).parent / unquote(parts.path) if parts.path else root / name
            p = p.resolve()
            if not p.is_relative_to(root):
                errors.append(f"Out-of-repository link: {name}")
                continue
            dest = p.relative_to(root).as_posix()
            if dest not in file_set:
                errors.append(f"Link points outside publish manifest: {name} -> {parts.path}")
                continue
            graph[name].add(dest)
            fragment = unquote(parts.fragment)
            if fragment and fragment not in anchors.get(dest, set()):
                errors.append(f"Missing link anchor: {name} -> {dest}#{fragment}")
    active_pages = {n for n, m in metadata.items() if m.get("status") in ACTIVE}
    inactive_pages = set(metadata) - active_pages
    reached, queue = set(NAV), list(NAV)
    while queue:
        source = queue.pop()
        for dest in graph[source]:
            # Generated indexes must not make every orphan appear navigable.
            if dest not in NAV | set(pages):
                continue
            if dest in inactive_pages:
                errors.append(f"Inactive knowledge is still in current navigation: {source} -> {dest}")
                continue
            if dest not in reached:
                reached.add(dest)
                queue.append(dest)
    for name in sorted(active_pages - reached):
        errors.append(f"Orphan active knowledge: {name}")
    for name in sorted(inactive_pages):
        reference = "skills/seedance-prompt/references/" + Path(name).name
        if reference in file_set:
            errors.append(f"Inactive knowledge still published in Skill: {name}")
    skill = texts.get("skills/seedance-prompt/SKILL.md", "")
    try:
        smeta = frontmatter(skill)
        if smeta.get("name") != "seedance-prompt" or not string(smeta.get("description")):
            errors.append("Skill name/description missing")
    except (ValueError, SyntaxError) as exc:
        errors.append(f"Invalid Skill frontmatter: {exc}")
    ui = texts.get("skills/seedance-prompt/agents/openai.yaml", "")
    short = re.search(r'short_description: "([^"]+)"', ui)
    if not short or not 25 <= len(short.group(1)) <= 64 or "$seedance-prompt" not in ui:
        errors.append("Invalid Skill UI metadata")
    validate_semantics(texts, metadata, id_to_path, ids, errors, warnings)
    events = validate_events(texts, file_set, id_to_path, ids, errors)
    try:
        errors.extend(check_refs(root))
        errors.extend(catalog_errors(root))
    except (ImportError, ValueError, OSError, KeyError, TypeError) as exc:
        errors.append(f"Generated content check cannot complete: {type(exc).__name__}: {exc}")
    if (root / ".git").exists():
        try:
            tracked = git(root, "ls-files", "-z").stdout.decode("utf-8").split("\0")
            for name in filter(None, tracked):
                if name not in file_set and (root / name).exists():
                    errors.append(f"Tracked outside publish manifest: {name}")
        except (ValueError, OSError) as exc:
            errors.append(f"Cannot inspect git index: {exc}")
    if base_ref is not None:
        validate_changes(root, base_ref, texts, file_set, events, errors)
    return list(dict.fromkeys(errors)), {"warnings": list(dict.fromkeys(warnings)),
            "publish_files": len(files), "knowledge_pages": len(pages),
            "active_knowledge_pages": len(active_pages), "source_records": len(ids),
            "events": len(events), "generation_validation": config.get("generation_validation", "unknown")}


def validate_semantics(texts, metadata, id_to_path, source_ids, errors, warnings):
    data = json.loads(texts.get("维护/semantic_review.json", "{}"))
    if data.get("schema_version") != 1 or data.get("reviewer") != "agent-text-review":
        errors.append("Invalid semantic-review schema/reviewer")
    try:
        value = data.get("reviewed_at")
        iso_date(value) if isinstance(value, str) and len(value) == 10 else timestamp(value)
    except (ValueError, TypeError):
        errors.append("Invalid semantic reviewed_at")
    reviewed = {}
    for item in data.get("pages", []):
        if not isinstance(item, dict) or item.get("id") not in id_to_path:
            errors.append("Unknown page in semantic review")
            continue
        kid, checksum = item["id"], item.get("body_sha256")
        if kid in reviewed or not isinstance(checksum, str) or not re.fullmatch(r"[a-f0-9]{64}", checksum):
            errors.append(f"Duplicate page or invalid semantic hash: {kid}")
            continue
        reviewed[kid] = checksum
        actual = hashlib.sha256(body_text(texts[id_to_path[kid]]).encode("utf-8")).hexdigest()
        if actual != checksum:
            warnings.append(f"Body changed since semantic review: {kid}")
    for kid in set(id_to_path) - set(reviewed):
        warnings.append(f"No recorded semantic review: {kid}")
    issues = {}
    for issue in data.get("issues", []):
        if not isinstance(issue, dict) or not string(issue.get("id")):
            errors.append("Invalid issue object")
            continue
        iid = issue["id"]
        if iid in issues or issue.get("status") not in {"open", "resolved", "withdrawn"}:
            errors.append(f"Duplicate/invalid semantic issue: {iid}")
        issues[iid] = issue
        for field in ("summary", "next_action"):
            if not string(issue.get(field)):
                errors.append(f"Issue {iid} needs {field}")
        check_ids(issue.get("knowledge_ids"), id_to_path, f"issue {iid} knowledge", errors)
        check_ids(issue.get("source_ids"), source_ids, f"issue {iid} sources", errors)
        evidence = issue.get("resolution_evidence")
        if not isinstance(evidence, list) or (issue.get("status") == "resolved" and not evidence):
            errors.append(f"Resolved issue needs evidence list: {iid}")
        if issue.get("status") == "open":
            warnings.append(f"Open semantic issue {iid}: {issue.get('summary', '')}")
    seen, active = set(), defaultdict(set)
    for claim in data.get("claims", []):
        if not isinstance(claim, dict):
            errors.append("Invalid claim object")
            continue
        cid = claim.get("id")
        if not string(cid) or cid in seen:
            errors.append("Missing or duplicate claim ID")
        seen.add(cid)
        for key in ("key", "scope", "page_id"):
            if not string(claim.get(key)):
                errors.append(f"Claim {cid} requires {key}")
        if claim.get("page_id") not in id_to_path or "value" not in claim:
            errors.append(f"Unknown claim page or missing value: {cid}")
        check_ids(claim.get("source_ids"), source_ids, f"claim {cid} sources", errors)
        state = claim.get("state")
        if state == "active":
            active[(claim.get("key"), claim.get("scope"))].add(json.dumps(claim.get("value"), sort_keys=True, ensure_ascii=False))
            p = id_to_path.get(claim.get("page_id"))
            if p and metadata[p].get("status") not in ACTIVE:
                errors.append(f"Active claim belongs to inactive page: {cid}")
        elif state == "disputed":
            if issues.get(claim.get("issue_id"), {}).get("status") != "open":
                errors.append(f"Disputed claim needs linked open issue: {cid}")
        else:
            errors.append(f"Invalid claim state: {cid}")
    for (key, scope), values in active.items():
        if len(values) > 1:
            errors.append(f"Conflicting active claims in same scope: {key} / {scope}")


def check_ids(values, valid, context, errors):
    if not isinstance(values, list) or not all(string(v) for v in values):
        errors.append(f"ID list required: {context}")
        return
    for value in values:
        if value not in valid:
            errors.append(f"Unknown ID {value}: {context}")


def safe_relative(value):
    return string(value) and not value.startswith(("/", "\\")) and "\\" not in value and not re.match(r"^[A-Za-z]:", value) and ".." not in Path(value).parts


def validate_events(texts, files, knowledge_ids, source_ids, errors):
    events, ids, previous = [], set(), None
    path_history, evidence_paths = defaultdict(list), []
    for line_no, line in enumerate(texts.get("维护/events.jsonl", "").splitlines(), 1):
        if not line.strip():
            errors.append(f"Blank event line: {line_no}")
            continue
        try:
            event = json.loads(line)
        except ValueError:
            errors.append(f"Invalid JSON event line: {line_no}")
            continue
        if not isinstance(event, dict):
            errors.append(f"Event must be object: {line_no}")
            continue
        events.append(event)
        eid = event.get("id")
        if not string(eid) or eid in ids:
            errors.append(f"Missing or duplicate event ID: line {line_no}")
        ids.add(eid)
        for key in ("type", "version", "summary", "reason"):
            if not string(event.get(key)):
                errors.append(f"Event {eid} needs {key}")
        try:
            current = timestamp(event.get("occurred_at"))
            if previous and current < previous:
                errors.append(f"Events are not chronological: {eid}")
            previous = current
        except (ValueError, TypeError):
            errors.append(f"Invalid timezone timestamp: {eid}")
        check_ids(event.get("knowledge_ids"), knowledge_ids, f"event {eid} knowledge", errors)
        check_ids(event.get("source_ids"), source_ids, f"event {eid} sources", errors)
        changes = event.get("changes")
        if not isinstance(changes, list):
            errors.append(f"Event changes list required: {eid}")
            changes = []
        for item in changes:
            if not isinstance(item, dict) or not safe_relative(item.get("path")) or item.get("action") not in {"add", "modify", "remove"}:
                errors.append(f"Invalid event change: {eid}")
            else:
                path_history[item["path"]].append((line_no, item["action"], eid))
        checks = event.get("validation")
        if not isinstance(checks, dict):
            errors.append(f"Event validation object required: {eid}")
        else:
            for key in ("structural", "behavior", "generation"):
                if checks.get(key) not in {"passed", "passed-scoped", "failed", "not-run", "partial"}:
                    errors.append(f"Invalid/incomplete event validation {key}: {eid}")
        evidence = event.get("evidence")
        if not isinstance(evidence, list):
            errors.append(f"Event evidence list required: {eid}")
            evidence = []
        for item in evidence:
            if not isinstance(item, dict) or not string(item.get("kind")):
                errors.append(f"Invalid event evidence: {eid}")
                continue
            if "path" in item:
                if not safe_relative(item["path"]):
                    errors.append(f"Invalid event evidence path: {eid}")
                else:
                    evidence_paths.append((line_no, item["path"], eid))
            if "url" in item and (not string(item["url"]) or urlsplit(item["url"]).scheme not in {"http", "https"}):
                errors.append(f"Invalid event evidence URL: {eid}")
    if not events:
        errors.append("Machine event timeline is empty")
    # Old add/modify entries remain true history after a later recorded removal.
    # Only the final recorded state must agree with today's publication set.
    for path, history in path_history.items():
        _, action, eid = history[-1]
        if action == "remove" and path in files:
            errors.append(f"Removed event path is still published: {eid}: {path}")
        elif action != "remove" and path not in files:
            errors.append(f"Latest event path is not published: {eid}: {path}")
    for line_no, path, eid in evidence_paths:
        if path in files:
            continue
        history = path_history.get(path, [])
        existed_then = any(n <= line_no and action in {"add", "modify"} for n, action, _ in history)
        removed_later = any(n > line_no and action == "remove" for n, action, _ in history)
        if not (existed_then and removed_later):
            errors.append(f"Invalid event evidence path: {eid}: {path}")
    return events


def coverage_exempt(path):
    return path in {"index.md", "index.json", "资料库/来源登记.md", "维护/更新记录.md", "维护/待验证问题.md"} or path.startswith("skills/seedance-prompt/references/")


def validate_changes(root, base_ref, texts, files, events, errors):
    if not re.fullmatch(r"[0-9a-fA-F]{40}", base_ref):
        errors.append("--base-ref must be a full 40-character commit SHA")
        return
    try:
        git(root, "cat-file", "-e", base_ref + "^{commit}")
        previous = git(root, "show", base_ref + ":维护/events.jsonl", required=False)
        old = previous.stdout.decode("utf-8") if previous.returncode == 0 else ""
        now = texts.get("维护/events.jsonl", "")
        if not now.startswith(old):
            errors.append("Event history must be append-only relative to base commit")
            return
        old_count = len([line for line in old.splitlines() if line.strip()])
        fresh = events[old_count:]
        if not old:
            # A first timeline may backfill old commits; those are history, not
            # evidence that the present working-tree changes were recorded.
            base_time = timestamp(git(root, "show", "-s", "--format=%cI", base_ref).stdout.decode("utf-8").strip())
            fresh = [event for event in fresh if timestamp(event["occurred_at"]) > base_time]
        base_files = set(git(root, "ls-tree", "-r", "--name-only", "-z", base_ref).stdout.decode("utf-8").split("\0")) - {""}
        changed = set(git(root, "diff", "--name-only", "-z", base_ref, "--").stdout.decode("utf-8").split("\0")) - {""}
        changed.update(files - base_files)
        changed = {p for p in changed if (p in files or p in base_files and ALLOWED.fullmatch(p)) and not coverage_exempt(p)}
        covered = {c.get("path") for e in fresh for c in e.get("changes", []) if isinstance(c, dict)}
        for path in sorted(changed - covered):
            errors.append(f"Changed publish file lacks a new timeline event: {path}")
        for path in sorted(changed & covered):
            exists = path in base_files
            for event in fresh:
                for change in event.get("changes", []):
                    if change.get("path") != path:
                        continue
                    action = change.get("action")
                    if action == "add":
                        if exists:
                            errors.append(f"Timeline add targets an existing base path: {path}")
                        exists = True
                    elif action in {"modify", "remove"}:
                        if not exists:
                            errors.append(f"Timeline {action} targets an absent path: {path}")
                        if action == "remove":
                            exists = False
            if exists != (path in files):
                errors.append(f"Timeline final path state differs from publication: {path}")
    except (ValueError, OSError, UnicodeError) as exc:
        errors.append(f"Cannot check base-ref history: {type(exc).__name__}: {exc}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--base-ref")
    parser.add_argument("--strict-warnings", action="store_true")
    args = parser.parse_args()
    try:
        errors, counts = validate(args.root, base_ref=args.base_ref)
    except (ValueError, OSError, KeyError, TypeError, SyntaxError) as exc:
        print(json.dumps({"ok": False, "errors": [f"Validation cannot complete: {type(exc).__name__}: {exc}"], "warnings": []}, ensure_ascii=False))
        return 1
    print(json.dumps({"ok": not errors, "errors": errors, **counts}, ensure_ascii=False, indent=2))
    return bool(errors or args.strict_warnings and counts["warnings"])


if __name__ == "__main__":
    raise SystemExit(main())
