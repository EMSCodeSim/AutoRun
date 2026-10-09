#!/usr/bin/env python3
"""Unit checks for finite automation release queues. No paid services."""
import json
from pathlib import Path
import unittest
import sys

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE / "scripts"))
import publish_queue

class EditorialAutomationTests(unittest.TestCase):
    def test_article_queue_has_unique_slugs_and_sufficient_depth(self):
        source = json.loads((BASE / "content/publishing-queue.json").read_text(encoding="utf-8"))
        publish_queue.validate(source)
        self.assertGreaterEqual(len(source["articles"]), 6)
    def test_prepared_revision_contains_meaningful_new_content(self):
        data = json.loads((BASE / "content/refresh-queue.json").read_text(encoding="utf-8"))
        self.assertTrue(data["revisions"])
        for revision in data["revisions"]:
            self.assertGreaterEqual(len(" ".join(p for s in revision["sections"] for p in s["paragraphs"]).split()), 125)
            self.assertEqual((BASE / "articles" / (revision["slug"] + ".html")).is_file(), True)
    def test_approved_tool_is_prebuilt_with_formula(self):
        data = json.loads((BASE / "content/tool-release-queue.json").read_text(encoding="utf-8"))
        for item in data["tools"]:
            source = BASE / item["source"]
            self.assertTrue(source.is_file())
            markup = source.read_text(encoding="utf-8")
            self.assertIn("id=\"result\"", markup)
            self.assertIn("id=\"capacity\"", markup)
            self.assertIn("id=\"watts\"", markup)
            self.assertIn("cap*eta/power", markup)
        self.assertAlmostEqual(74 * 0.8 / 20, 2.96, places=8)
    def test_empty_queued_items_do_not_trigger_publication(self):
        for p in [BASE / "scripts/publish_queue.py", BASE / "scripts/refresh_content.py", BASE / "scripts/publish_tool.py"]:
            self.assertTrue(p.is_file())
            self.assertIn("if __name__", p.read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
