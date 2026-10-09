#!/usr/bin/env python3
"""Generate one unpublished article proposal. Never changes the public site."""
import datetime
import json
import os
import pathlib
import re
import urllib.request

BASE = pathlib.Path(__file__).resolve().parents[1]
KEY = os.getenv("PRACTICAL_PICK_AI_API_KEY")
URL = os.getenv("PRACTICAL_PICK_AI_BASE_URL", "").rstrip("/")
MODEL = os.getenv("PRACTICAL_PICK_AI_MODEL", "")
if not (KEY and URL and MODEL):
    print("No configured free/approved AI provider; skipping safely.")
    raise SystemExit(0)
if not URL.startswith("https://"):
    raise SystemExit("Only HTTPS AI endpoints are allowed")

TOPICS = [
    "USB-C cable compatibility buying questions",
    "Practical power bank buying considerations",
    "Desk chair adjustability checklist",
    "Home toolkit essentials for beginners",
    "Home office task lighting buying checklist",
    "Choosing a portable storage drive",
    "Evaluating a home air purifier specification sheet",
]
today = datetime.date.today()
topic = TOPICS[(today.toordinal() // 7) % len(TOPICS)]
system_prompt = (
    "Write an original unpublished consumer educational draft. "
    "You do not have verified live web access. Never invent source URLs, "
    "prices, certifications, tests, first-hand experiences, ratings, "
    "reviews, endorsements, statistics, or claims of independent verification. "
    "Suggest primary-source verification tasks. "
    "Return only JSON keys: title, introduction, sections (list with heading and "
    "body strings), verification_tasks (list of strings). Provide at least four "
    "substantive sections. Avoid safety-critical advice. The output is a DRAFT."
)
payload = {
    "model": MODEL,
    "messages": [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Prepare a useful plain-English checklist about {topic}."},
    ],
    "temperature": 0.3,
}
request = urllib.request.Request(
    URL + "/chat/completions",
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json", "Authorization": "Bearer " + KEY},
    method="POST",
)
with urllib.request.urlopen(request, timeout=60) as response:
    result = json.load(response)
raw = result["choices"][0]["message"]["content"].strip()
if raw.startswith("```"):
    raw = re.sub(r"^\x60{3}(?:json)?\s*|\s*\x60{3}$", "", raw)
draft = json.loads(raw)
if not isinstance(draft, dict) or not isinstance(draft.get("sections"), list):
    raise ValueError("Unexpected model response structure")
if len(draft["sections"]) < 4 or not draft.get("verification_tasks"):
    raise ValueError("Draft requires four sections and verification tasks")
name = re.sub("[^a-z0-9]+", "-", str(draft.get("title", topic)).lower()).strip("-")[:64]
draft["status"] = "UNPUBLISHED_REQUIRES_HUMAN_FACT_CHECK"
draft["date"] = str(today)
draft["topic"] = topic
outdir = BASE / "drafts"
outdir.mkdir(parents=True, exist_ok=True)
out = outdir / (today.isoformat() + "-" + name + ".json")
out.write_text(json.dumps(draft, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("Created private-to-repository draft (not published):", out)
