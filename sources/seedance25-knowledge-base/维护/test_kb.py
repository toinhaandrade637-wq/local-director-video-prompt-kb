"""Standard-library regression tests; fixtures stay inside ignored .local."""
import contextlib
import copy
import hashlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch
import check_kb as lint
import build_skill_refs as refs


class KnowledgeLintTests(unittest.TestCase):
    def setUp(self):
        scratch = Path(__file__).resolve().parents[1] / ".local"
        scratch.mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="kb-regression-", dir=scratch)
        self.root = Path(self.temp.name)
        self.today = datetime.now(timezone(timedelta(hours=8))).date()
        self.catalog = patch.object(lint, "catalog_errors", return_value=[])
        self.catalog.start()
        for name in lint.REQUIRED:
            self.write(name, "# Fixture\n" if name.endswith(".md") else "")
        self.write("README.md", "# Fixture\n\n**0.1.1 试用版**\n\n[目录](现行知识/索引.md)\n")
        self.dump("维护/repository.json", {"version": "0.1.1", "generation_validation": "not-executed"})
        self.dump("资料库/来源登记.json", {"schema_version": 1, "updated": str(self.today), "sources": [
            {"id": "U001", "title": "Fixture source", "kind": "user-convention",
             "storage": "derived-only", "evidence": "Fixture evidence"}]})
        self.write("资料库/来源登记.md", "# 来源\n\nU001\n")
        self.add_page("01", "甲")
        self.add_page("02", "乙")
        for name in lint.NAV:
            self.write(name, "# 方法\n\n[甲](01-甲.md)\n\n[乙](02-乙.md)\n")
        self.write("skills/seedance-prompt/SKILL.md", "---\nname: seedance-prompt\ndescription: Fixture prompt skill.\n---\n# Skill\n\n[甲](references/01-甲.md)\n")
        self.write("skills/seedance-prompt/agents/openai.yaml", 'interface:\n  short_description: "Fixture description with enough length"\n  default_prompt: "Use $seedance-prompt"\n')
        self.events = [{"id": "E001", "occurred_at": f"{self.today}T00:00:00+08:00", "type": "initialize",
                        "version": "0.1.1", "summary": "Fixture initialized", "reason": "Test",
                        "knowledge_ids": ["K01", "K02"], "source_ids": ["U001"],
                        "changes": [{"path": "README.md", "action": "add"}],
                        "validation": {"structural": "passed", "behavior": "passed-scoped", "generation": "not-run"},
                        "evidence": [{"kind": "text-review", "path": "README.md"}]}]
        self.save_events()
        self.refresh_review()
        self.refresh()

    def tearDown(self):
        self.catalog.stop()
        self.temp.cleanup()

    def write(self, path, value):
        p = self.root / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(value, encoding="utf-8")

    def dump(self, path, value):
        self.write(path, json.dumps(value, ensure_ascii=False, indent=2) + "\n")

    def load(self, path):
        return json.loads((self.root / path).read_text(encoding="utf-8"))

    def edit(self, path, old, new):
        text = (self.root / path).read_text(encoding="utf-8")
        self.assertIn(old, text)
        self.write(path, text.replace(old, new))

    def add_page(self, number, title):
        self.write(f"现行知识/{number}-{title}.md", f"---\nid: K{number}\nstatus: trial\nreview: text-reviewed\ngeneration_validation: not-independently-tested\nupdated: {self.today}\nreviewed_on: {self.today}\nreview_after: {self.today + timedelta(days=180)}\ntopics: [结构, 连续性]\nsources: [U001]\n---\n# {title}\n\nA useful fixture method.\n")

    def refresh_review(self):
        pages = []
        for p in refs.canonical_pages(self.root):
            text = p.read_text(encoding="utf-8")
            pages.append({"id": lint.frontmatter(text)["id"], "body_sha256": hashlib.sha256(lint.body_text(text).encode()).hexdigest()})
        self.dump("维护/semantic_review.json", {"schema_version": 1, "reviewed_at": str(self.today),
                  "reviewer": "agent-text-review", "pages": pages, "claims": [
                      {"id": "C001", "key": "fixture-rule", "scope": "global", "page_id": "K01",
                       "source_ids": ["U001"], "value": "conditional", "state": "active"}], "issues": []})

    def refresh(self):
        refs.build(self.root)
        self.dump("维护/publish_files.json", {"schema_version": 1, "files": sorted(lint.discover(self.root))})

    def save_events(self):
        self.write("维护/events.jsonl", "".join(json.dumps(e, ensure_ascii=False) + "\n" for e in self.events))

    def result(self, **kwargs):
        return lint.validate(self.root, today=self.today, **kwargs)

    def assert_error(self, fragment, **kwargs):
        errors, _ = self.result(**kwargs)
        self.assertTrue(any(fragment in e for e in errors), errors)

    def test_valid_fixture_without_git(self):
        errors, counts = self.result()
        self.assertEqual([], errors)
        self.assertEqual([], counts["warnings"])

    def test_duplicate_frontmatter(self):
        self.edit("现行知识/02-乙.md", "status: trial", "status: trial\nstatus: withdrawn")
        self.assert_error("Duplicate frontmatter key")

    def test_bad_metadata_values(self):
        self.edit("现行知识/02-乙.md", "id: K02", "id: banana")
        self.edit("现行知识/02-乙.md", "status: trial", "status: arbitrary")
        self.edit("现行知识/02-乙.md", f"updated: {self.today}", "updated: tomorrow")
        self.assert_error("Knowledge ID must match")
        self.assert_error("Invalid knowledge status")
        self.assert_error("Invalid or missing updated")

    def test_generation_claim_needs_evidence(self):
        self.edit("现行知识/02-乙.md", "generation_validation: not-independently-tested", "generation_validation: independently-tested")
        self.refresh()
        self.assert_error("needs generation_evidence")

    def test_source_fields_and_date(self):
        data = self.load("资料库/来源登记.json")
        data["sources"][0].update(kind=None, evidence=None, current_verified_on="wrong")
        self.dump("资料库/来源登记.json", data)
        self.assert_error("needs nonempty evidence")
        self.assert_error("Invalid source kind/storage")
        self.assert_error("Invalid source date")

    def test_known_source_required(self):
        self.edit("现行知识/02-乙.md", "sources: [U001]", "sources: [U999]")
        self.refresh()
        self.assert_error("Unknown source U999")

    def test_required_publish_file(self):
        data = self.load("维护/publish_files.json")
        data["files"].remove(".github/workflows/validate.yml")
        self.dump("维护/publish_files.json", data)
        self.assert_error("Required publish file absent")

    def test_unlisted_authored_page(self):
        self.add_page("03", "丙")
        self.assert_error("Unlisted authored file")

    def test_orphan_not_hidden_by_generated_index(self):
        self.add_page("03", "丙")
        self.write("index.md", "# Generated\n\n[All](现行知识/03-丙.md)\n")
        self.refresh_review()
        self.refresh()
        self.assert_error("Orphan active knowledge")

    def test_withdrawn_lifecycle(self):
        self.edit("现行知识/02-乙.md", "status: trial", "status: withdrawn")
        self.refresh_review()
        self.refresh()
        self.assertFalse((self.root / "skills/seedance-prompt/references/02-乙.md").exists())
        self.assert_error("Inactive knowledge is still in current navigation")
        for name in lint.NAV:
            self.edit(name, "[乙](02-乙.md)", "")
        self.assertEqual([], self.result()[0])

    def test_overdue_is_warning(self):
        p = "现行知识/02-乙.md"
        self.edit(p, f"reviewed_on: {self.today}", f"reviewed_on: {self.today - timedelta(days=3)}")
        self.edit(p, f"review_after: {self.today + timedelta(days=180)}", f"review_after: {self.today - timedelta(days=1)}")
        self.refresh()
        errors, counts = self.result()
        self.assertEqual([], errors)
        self.assertTrue(any("overdue" in w for w in counts["warnings"]))

    def test_stale_reference(self):
        p = self.root / "skills/seedance-prompt/references/01-甲.md"
        p.write_text(p.read_text(encoding="utf-8") + "changed", encoding="utf-8")
        self.assert_error("stale generated reference")

    def test_generator_protects_unowned_file(self):
        self.write("skills/seedance-prompt/references/manual.md", "user content")
        with self.assertRaisesRegex(ValueError, "unowned"):
            refs.build(self.root)

    def test_broken_file_and_anchors(self):
        self.write("README.md", "**0.1.1 试用版**\n[missing](absent.md)\n[bad](现行知识/01-甲.md#not-found)\n[bad self](#missing)\n")
        errors, _ = self.result()
        self.assertTrue(any("outside publish" in e for e in errors))
        self.assertEqual(2, sum("Missing link anchor" in e for e in errors))

    def test_valid_titles_reference_links_and_duplicate_headings(self):
        self.write("README.md", "# First\n\n**0.1.1 试用版**\n[甲](现行知识/01-甲.md#甲 \"标题\")\n[另一种][method]\n\n[method]: <现行知识/02-乙.md#乙> '提示'\n\n[First again](#first-1)\n\n# First\n")
        self.assertEqual([], self.result()[0])

    def test_undefined_reference_and_local_path(self):
        self.write("README.md", "**0.1.1 试用版**\n[bad][unregistered]\n[local](file:///D:/private.txt)\n")
        self.assert_error("Undefined reference link")
        self.assert_error("local link scheme")

    def test_version_drift(self):
        data = self.load("维护/repository.json")
        data["version"] = "9.9.9"
        self.dump("维护/repository.json", data)
        self.refresh()
        self.assert_error("README current version differs")

    def test_claim_conflict_and_body_change(self):
        data = self.load("维护/semantic_review.json")
        other = copy.deepcopy(data["claims"][0])
        other.update(id="C002", value="always")
        data["claims"].append(other)
        self.dump("维护/semantic_review.json", data)
        self.assert_error("Conflicting active claims")
        self.edit("现行知识/01-甲.md", "A useful fixture method.", "Changed method.")
        self.refresh()
        self.assertTrue(any("Body changed" in w for w in self.result()[1]["warnings"]))

    def test_dispute_and_resolution_evidence(self):
        data = self.load("维护/semantic_review.json")
        data["claims"][0].update(state="disputed", issue_id="Q001")
        self.dump("维护/semantic_review.json", data)
        self.assert_error("Disputed claim needs")
        data["issues"] = [{"id": "Q001", "status": "open", "knowledge_ids": ["K01"], "source_ids": ["U001"],
                           "summary": "Known unresolved question", "next_action": "Compare evidence", "resolution_evidence": []}]
        self.dump("维护/semantic_review.json", data)
        errors, counts = self.result()
        self.assertEqual([], errors)
        self.assertTrue(any("Open semantic issue" in w for w in counts["warnings"]))
        data["claims"] = []
        data["issues"][0]["status"] = "resolved"
        self.dump("维护/semantic_review.json", data)
        self.assert_error("Resolved issue needs evidence")

    def test_event_schema_and_order(self):
        event = copy.deepcopy(self.events[0])
        event.update(id="E001", occurred_at=f"{self.today - timedelta(days=1)}T00:00:00+08:00")
        self.events.append(event)
        self.save_events()
        self.assert_error("duplicate event ID")
        self.assert_error("not chronological")
        self.events[1].update(id="E002", occurred_at=str(self.today))
        self.save_events()
        self.assert_error("Invalid timezone timestamp")

    def test_pending_not_completed(self):
        self.events[0]["validation"]["structural"] = "pending"
        self.save_events()
        self.assert_error("Invalid/incomplete event validation")

    def test_old_event_survives_later_file_removal(self):
        old_path = "维护/旧记录.md"
        self.write(old_path, "# Old record\n")
        self.events[0]["changes"].append({"path": old_path, "action": "add"})
        self.events[0]["evidence"].append({"kind": "report", "path": old_path})
        self.save_events()
        self.refresh()
        self.assertEqual([], self.result()[0])
        (self.root / old_path).unlink()
        event = copy.deepcopy(self.events[0])
        event.update(id="E002", occurred_at=f"{self.today}T01:00:00+08:00",
                     changes=[{"path": old_path, "action": "remove"}], evidence=[])
        self.events.append(event)
        self.save_events()
        self.refresh()
        self.assertEqual([], self.result()[0])
        self.events.pop()
        self.save_events()
        self.assert_error("Latest event path is not published")

    def test_hash_normalization_matches_catalog(self):
        from catalog import body_text
        sample = "\ufeff---\r\nid: K01\r\n---\r\n \t\r\n\r\n# Body\r\n\r\nText.\r\n"
        self.assertEqual(body_text(sample), lint.body_text(sample))
        self.assertEqual("# Body\n\nText.\n", lint.body_text(sample))

    def test_catalog_errors_merged(self):
        with patch.object(lint, "catalog_errors", return_value=["Catalog stale"]):
            self.assert_error("Catalog stale")

    def commit_fixture(self):
        executable = lint.git_executable()
        def command(*args):
            return subprocess.check_output([executable, *args], cwd=self.root, stderr=subprocess.DEVNULL)
        command("init", "-b", "main")
        command("add", "--", *self.load("维护/publish_files.json")["files"])
        command("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "commit", "-m", "fixture")
        return command("rev-parse", "HEAD").decode().strip()

    def test_append_only_and_change_coverage(self):
        base = self.commit_fixture()
        self.edit("README.md", "# Fixture", "# Changed")
        self.assert_error("lacks a new timeline event", base_ref=base)
        event = copy.deepcopy(self.events[0])
        event.update(id="E002", occurred_at=f"{self.today}T01:00:00+08:00", changes=[
            {"path": "README.md", "action": "modify"}, {"path": "维护/events.jsonl", "action": "modify"}])
        self.events.append(event)
        self.save_events()
        self.assertEqual([], self.result(base_ref=base)[0])
        self.events[0]["summary"] = "Rewritten history"
        self.save_events()
        self.assert_error("append-only", base_ref=base)

    def test_invalid_base_ref(self):
        self.assert_error("full 40-character", base_ref="main")

    def test_change_action_matches_existing_path(self):
        base = self.commit_fixture()
        self.edit("README.md", "# Fixture", "# Changed")
        event = copy.deepcopy(self.events[0])
        event.update(id="E002", occurred_at=f"{self.today}T01:00:00+08:00", changes=[
            {"path": "README.md", "action": "add"},
            {"path": "维护/events.jsonl", "action": "modify"}])
        self.events.append(event)
        self.save_events()
        self.assert_error("add targets an existing", base_ref=base)
        self.events[-1]["changes"][0]["action"] = "modify"
        self.save_events()
        self.assertEqual([], self.result(base_ref=base)[0])

    def test_catalog_output_boundary(self):
        from catalog import output_path
        self.assertEqual(self.root / "index.md", output_path(self.root, "index.md"))
        with self.assertRaisesRegex(ValueError, "escapes"):
            output_path(self.root, "../outside.md")
        target = self.root / "outside-target.md"
        self.write("outside-target.md", "Keep user file")
        candidate = self.root / "linked.md"
        try:
            candidate.symlink_to(target)
        except OSError:
            return  # Windows may not grant symlink creation; escape check ran.
        with self.assertRaisesRegex(ValueError, "symlink"):
            output_path(self.root, "linked.md")
        self.assertEqual("Keep user file", target.read_text(encoding="utf-8"))

    def test_strict_warning_cli(self):
        self.edit("现行知识/02-乙.md", "review: text-reviewed", "review: needs-review")
        self.refresh()
        for strict, expected in ((False, False), (True, True)):
            argv = ["check_kb", "--root", str(self.root)] + (["--strict-warnings"] if strict else [])
            with patch.object(sys, "argv", argv), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(expected, lint.main())


if __name__ == "__main__":
    unittest.main()
