#!/usr/bin/env python3
"""Release one specifically prepared factual improvement, never a date-only update."""
import json
from pathlib import Path
from datetime import datetime, timezone
from html import escape
import re

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "content" / "refresh-queue.json"

def main():
    items = json.loads(QUEUE.read_text(encoding="utf-8"))["revisions"]
    for entry in items:
        slug = entry["slug"]
        if not re.fullmatch(r"[a-z0-9-]+", slug):
            raise ValueError("Invalid article slug")
        article = ROOT / "articles" / (slug + ".html")
        if not article.is_file():
            continue
        html = article.read_text(encoding="utf-8")
        token = '<!-- PRACTICAL_PICK_REFRESH:' + entry["revision"] + ' -->'
        if token in html:
            continue
        anchor = entry["before"]
        if html.count(anchor) != 1:
            raise RuntimeError("Cannot safely find exact single insertion point for " + slug)
        sections = entry["sections"]
        if not sections or not all(len(s["paragraphs"]) > 0 for s in sections):
            raise ValueError("Revision missing substantive changes")
        addition = "".join("<section><h2>" + escape(s["heading"]) + "</h2>" + "".join("<p>" + escape(p) + "</p>" for p in s["paragraphs"]) + "</section>" for s in sections)
        if len(re.sub(r"<[^>]+>", " ", addition).split()) < 125:
            raise ValueError("Refresh requires substantive written improvement")
        html = html.replace(anchor, token + addition + anchor, 1)
        now = datetime.now(timezone.utc).date().isoformat()
        html = html.replace("</head>", '<meta name="date-modified" content="' + now + '"></head>', 1)
        article.write_text(html, encoding="utf-8")
        print("Published material improvement to", article.relative_to(ROOT), "on", now)
        return
    print("No verified revisions remain; do not change published dates.")

if __name__ == "__main__":
    main()
