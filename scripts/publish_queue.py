#!/usr/bin/env python3
"""Publish at most one prepared, source-linked guide. No paid services or AI key needed."""
from __future__ import annotations
from datetime import datetime, timezone
from html import escape
from pathlib import Path
import json
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://autoruntest.netlify.app/"
QUEUE = ROOT / "content" / "publishing-queue.json"
VALID_CATEGORIES = {"Wi-Fi", "Energy", "Charging"}

def diagram(kind: str) -> str:
    """Original accessible SVG explanatory artwork with no external assets."""
    begin = '<svg class="article-art" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 360" '
    if kind == "energy":
        return begin + 'aria-label="Energy use illustration: power multiplied by time equals energy"><rect width="960" height="360" rx="28" fill="#e9f3ef"/><circle cx="170" cy="180" r="96" fill="#b9e1cc"/><path d="M174 96 121 191h46l-18 78 84-116h-52l26-57" fill="#247b59"/><g font-family="Arial,sans-serif" text-anchor="middle" fill="#1a4335"><text x="425" y="150" font-size="49" font-weight="bold">Power</text><text x="425" y="206" font-size="31">kW</text><text x="575" y="190" font-size="55">×</text><text x="733" y="150" font-size="49" font-weight="bold">Time</text><text x="733" y="206" font-size="31">hours</text></g><text x="480" y="304" text-anchor="middle" fill="#1a4335" font-family="Arial,sans-serif" font-size="29">Power × time = energy (kWh)</text></svg>'
    if kind == "wifi":
        return begin + 'aria-label="Router signal spreading through rooms and becoming weaker behind walls"><rect width="960" height="360" rx="28" fill="#e7f1fa"/><rect x="510" y="45" width="365" height="270" rx="16" fill="#f7fafc" stroke="#91b4d3" stroke-width="5"/><line x1="694" y1="45" x2="694" y2="315" stroke="#91b4d3" stroke-width="8"/><path d="M170 177Q340 28 510 177M210 177Q350 67 490 177M260 177Q360 112 455 177" fill="none" stroke="#4e8bb9" stroke-width="12" opacity=".6"/><rect x="140" y="179" width="130" height="82" rx="18" fill="#214d73"/><path d="M170 178v-42m70 42v-42" stroke="#214d73" stroke-width="9"/><circle cx="180" cy="228" r="7" fill="#89e4b3"/><circle cx="206" cy="228" r="7" fill="#89e4b3"/><g fill="#214d73" font-family="Arial,sans-serif" font-size="28"><text x="550" y="190">Room A</text><text x="726" y="190">Room B</text></g><circle cx="794" cy="126" r="15" fill="#ed9a5d"/><path d="M783 107Q795 93 808 107" fill="none" stroke="#ed9a5d" stroke-width="5"/></svg>'
    if kind == "battery":
        return begin + 'aria-label="Battery pack drawing contrasting stored energy and usable output"><rect width="960" height="360" rx="28" fill="#eef0fb"/><rect x="173" y="85" width="350" height="196" rx="28" fill="#263b67"/><rect x="523" y="151" width="22" height="63" rx="5" fill="#263b67"/><rect x="199" y="111" width="280" height="145" rx="16" fill="#cbd5f2"/><rect x="199" y="111" width="215" height="145" rx="16" fill="#92c9ae"/><path d="M605 179h96m-21-20 22 20-22 20" stroke="#326686" fill="none" stroke-width="12" stroke-linecap="round"/><g font-family="Arial,sans-serif" font-weight="bold" fill="#263b67" text-anchor="middle"><text x="340" y="65" font-size="29">Stored energy (Wh)</text><text x="805" y="156" font-size="30">Output</text><text x="805" y="198" font-size="30">power (W)</text><text x="805" y="238" font-size="19" font-weight="normal">Check both ratings</text></g></svg>'
    return begin + 'aria-label="Charging cable, power adapter and device linked together"><rect width="960" height="360" rx="28" fill="#f9eee5"/><rect x="120" y="112" width="150" height="150" rx="22" fill="#db9666"/><rect x="157" y="144" width="76" height="81" rx="10" fill="#fff6eb"/><path d="M270 180C390 180 390 275 500 180S640 92 685 180" fill="none" stroke="#5b6884" stroke-width="16" stroke-linecap="round"/><rect x="680" y="78" width="152" height="220" rx="28" fill="#273b58"/><rect x="698" y="101" width="116" height="166" rx="10" fill="#c6e5da"/><path d="M752 139l-27 49h26l-11 38 48-63h-29l18-24" fill="#267b58"/><text x="190" y="80" text-anchor="middle" font-family="Arial,sans-serif" font-size="25" fill="#273b58">Adapter</text><text x="755" y="53" text-anchor="middle" font-family="Arial,sans-serif" font-size="25" fill="#273b58">Device</text></svg>'

def page_html(article: dict, date: str) -> str:
    title, slug = article["title"], article["slug"]
    blocks = []
    for heading, paragraphs in article["sections"]:
        blocks.append("<section><h2>" + escape(heading) + "</h2>")
        for paragraph in paragraphs:
            blocks.append("<p>" + escape(paragraph) + "</p>")
        blocks.append("</section>")
    sources = "".join('<li><a rel="noopener" href="' + escape(url, quote=True) + '">' + escape(label) + "</a></li>" for label, url in article["sources"])
    schema = json.dumps({"@context": "https://schema.org", "@type": "Article", "headline": title, "description":article["dek"],"datePublished": date,"author":{"@type":"Organization","name":"Practical Pick"}}, separators=(",", ":")).replace("<","\\u003c")
    url = BASE_URL + "articles/" + slug + ".html"
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)} | Practical Pick</title><meta name="description" content="{escape(article['dek'], quote=True)}"><meta name="robots" content="index,follow"><link rel="canonical" href="{url}"><link rel="stylesheet" href="/styles.css"><link rel="stylesheet" href="/editorial.css"><script type="application/ld+json">{schema}</script></head><body><header class="top"><div class="wrap nav"><a class="brand" href="/">Practical<span>Pick</span></a><nav aria-label="Main navigation"><a href="/#tools">Free tools</a><a href="/latest.html">Latest guides</a><a href="/about.html">About</a></nav></div></header><main class="wrap longform"><p class="eyebrow">{escape(article['category'])} · Explainer</p><h1>{escape(title)}</h1><p class="story-dek">{escape(article['dek'])}</p>{diagram(article['diagram'])}<p class="editorial-note">Published {date} · Prepared with automated editorial assistance · Illustration is an original explanatory diagram, not a product photo or test result.</p><div class="article-body">{''.join(blocks)}<section><h2>Sources and further reading</h2><p>Consult original manufacturer documentation for device-specific guidance. These background sources support the concepts discussed; they do not represent independent testing of any product.</p><ul>{sources}</ul></section><aside class="next-actions"><h2>Put it into practice</h2><p><a href="/tools/electricity-cost.html">Calculate electricity cost</a> · <a href="/tools/wifi-checklist.html">Troubleshoot Wi-Fi</a> · <a href="/tools/usb-c-checklist.html">Check USB-C compatibility</a></p></aside><p><a href="/latest.html">← More in-depth guides</a></p></div></main><footer><div class="wrap"><a href="/">Practical Pick</a> · <a href="/about.html">Editorial standards</a> · <a href="/privacy.html">Privacy</a></div></footer></body></html>"""

def validate(data: dict) -> None:
    if data.get("schema_version") != 1:
        raise ValueError("Unknown queue schema")
    for a in data["articles"]:
        if not re.fullmatch(r"[a-z0-9-]{5,70}", a["slug"]):
            raise ValueError("Invalid slug")
        if a["category"] not in VALID_CATEGORIES or a["diagram"] not in {"energy", "wifi", "battery", "charging"}:
            raise ValueError("Invalid category or illustration")
        if len(a["sections"]) < 5 or len(a["sources"]) < 1:
            raise ValueError("Article is insufficiently developed")
        if len(" ".join(p for _, paragraphs in a["sections"] for p in paragraphs).split()) < 325:
            raise ValueError("Article below minimum depth")
        for title, link in a["sources"]:
            if not link.startswith("https://") or not title:
                raise ValueError("Invalid source")
    if len({x["slug"] for x in data["articles"]}) != len(data["articles"]):
        raise ValueError("Duplicate article slug")

def catalog() -> None:
    cards = []
    for a in json.loads(QUEUE.read_text())["articles"]:
        if not (ROOT / "articles" / (a["slug"] + ".html")).exists():
            continue
        href = "/articles/" + a["slug"] + ".html"
        cards.append('<article class="card"><span class="tag">' + escape(a["category"]) + '</span><h3><a href="' + href + '">' + escape(a["title"]) + '</a></h3><p>' + escape(a["dek"]) + '</p><a class="more" href="' + href + '">Read guide →</a></article>')
    header = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Latest in-depth guides | Practical Pick</title><meta name="description" content="In-depth explainers on Wi-Fi, home energy costs and everyday charging technology."><link rel="canonical" href="' + BASE_URL + 'latest.html"><link rel="stylesheet" href="/styles.css"></head><body><header class="top"><div class="wrap nav"><a class="brand" href="/">Practical<span>Pick</span></a><nav><a href="/#tools">Free tools</a><a href="/#guides">Guides</a></nav></div></header><main class="wrap tool-page"><p class="eyebrow">In-depth guides</p><h1>Useful answers, explained.</h1><p class="tool-intro">Real questions, practical advice, and source-linked explanations. New prepared guides are released on the editorial schedule.</p><div class="cards">'
    footer = '</div></main><footer><div class="wrap"><a href="/">← Home</a> · <a href="/about.html">Editorial standards</a></div></footer></body></html>'
    (ROOT / "latest.html").write_text(header + "".join(cards) + footer, encoding="utf-8")

def sitemap() -> None:
    pages = sorted(p for p in ROOT.rglob("*.html") if not any(c in {".git", ".github", "drafts"} for c in p.relative_to(ROOT).parts))
    root = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for page in pages:
        local = page.relative_to(ROOT).as_posix()
        url = ET.SubElement(root, "url")
        ET.SubElement(url, "loc").text = BASE_URL + ("" if local == "index.html" else local)
    ET.indent(root, space="  ")
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(root, encoding="unicode") + "\n", encoding="utf-8")

def main() -> None:
    data = json.loads(QUEUE.read_text(encoding="utf-8"))
    validate(data)
    pending = [a for a in data["articles"] if not (ROOT / "articles" / (a["slug"] + ".html")).exists()]
    today = datetime.now(timezone.utc).date().isoformat()
    if pending:
        a = pending[0]
        target = ROOT / "articles" / (a["slug"] + ".html")
        target.write_text(page_html(a, today), encoding="utf-8")
        print("Published one prepared article:", target.relative_to(ROOT))
    else:
        print("Queue exhausted; not fabricating a new article or fake content update.")
    catalog()
    sitemap()
    print("Regenerated latest.html and sitemap.xml")

if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print("ERROR: publication blocked:", ex, file=sys.stderr)
        raise
