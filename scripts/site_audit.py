#!/usr/bin/env python3
"""Static-site checks; no API access and no automatic claims of article freshness."""
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit, unquote
from datetime import date

BASE = Path(__file__).resolve().parents[1]
EXCLUDE = {".git", ".github", "drafts", "scripts", "__pycache__"}
class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.has_title = False
        self.description = False
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "title":
            self.has_title = True
        if tag == "meta" and attrs.get("name", "").lower() == "description":
            self.description = bool(attrs.get("content", "").strip())
        if tag in ("a", "link", "script") and ("href" in attrs or "src" in attrs):
            self.links.append(attrs.get("href", attrs.get("src", "")))

errors = []
html_files = []
for f in BASE.rglob("*.html"):
    if any(part in EXCLUDE or part.startswith(".") for part in f.relative_to(BASE).parts):
        continue
    html_files.append(f)
    text = f.read_text(encoding="utf-8")
    p = Page()
    p.feed(text)
    if not p.has_title or not p.description:
        errors.append(f"{f.relative_to(BASE)}: missing title or meta description")
    for link in p.links:
        if not link or link.startswith(("#", "mailto:", "tel:", "data:", "javascript:")):
            continue
        parsed = urlsplit(link)
        if parsed.scheme or parsed.netloc:
            continue
        dest = unquote(parsed.path)
        if dest.startswith("/"):
            target = BASE / dest.lstrip("/")
        else:
            target = f.parent / dest
        if target.is_dir():
            target /= "index.html"
        if not target.exists():
            errors.append(f"{f.relative_to(BASE)}: broken local link {link}")
for name in ("index.html", "robots.txt", "sitemap.xml", "privacy.html", "about.html", "tools/electricity-cost.js"):
    if not (BASE / name).exists():
        errors.append("missing required file " + name)
# Editorial queue: report existing content for periodic review; dates are not automatically changed.
print(f"Audited {len(html_files)} HTML pages on {date.today().isoformat()}.")
print("Review queue (verify claims and outbound sources; no automatic freshness claim):")
for f in sorted(html_files):
    if f.parent.name == "articles":
        print(" -", f.relative_to(BASE))
if errors:
    print("\nERRORS:")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("Static quality checks passed.")
