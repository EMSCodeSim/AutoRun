#!/usr/bin/env python3
"""Publish one prebuilt, tested tool monthly; never create untested tools on a schedule."""
import json
import re
from pathlib import Path
from scripts.publish_queue import sitemap
ROOT = Path(__file__).resolve().parents[1]
def main():
    queue = json.loads((ROOT/"content/tool-release-queue.json").read_text())["tools"]
    for item in queue:
        slug = item["slug"]
        if not re.fullmatch(r"[a-z0-9-]{5,70}", slug):
            raise ValueError("Unsafe slug")
        target = ROOT/"tools"/(slug+".html")
        if target.exists():
            continue
        source = (ROOT/item["source"]).resolve()
        if not source.is_relative_to((ROOT/"content/tool-templates").resolve()):
            raise ValueError("Unapproved tool location")
        html = source.read_text(encoding="utf-8")
        if not all(value in html for value in ["<title>", 'name="description"', 'rel="canonical"', 'id="result"', "<script"]):
            raise ValueError("Tool missing required elements")
        target.write_text(html, encoding="utf-8")
        home = ROOT/"index.html"
        previous = home.read_text(encoding="utf-8")
        insertion = '<article class="card"><span class="tag">New interactive tool</span><h3><a href="/tools/'+slug+'.html">'+item["description"]+'</a></h3><p>Free in-browser calculator with transparent assumptions and no account required.</p><a class="more" href="/tools/'+slug+'.html">Open tool →</a></article>'
        marker = '<section class="wrap" id="tools">'
        if previous.count(marker) != 1:
            raise ValueError("Homepage tool section not found")
        next_home = previous.replace(marker, marker + '<div class="cards" style="margin:24px 0">'+ insertion + '</div>',1)
        home.write_text(next_home, encoding="utf-8")
        sitemap()
        print("Published tested tool:", slug)
        return
    print("No prepared tool available; no placeholder release.")

if __name__ == "__main__":
    main()
