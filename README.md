# Practical Pick — free home technology help

Public website: https://autoruntest.netlify.app

This is a focused, advertiser-free site with free troubleshooting checklists, one working energy-cost calculator, and practical buying advice. The repository replaces the old AutoRun experiment by the owner's request.

## SEO and reader value

- Core topic: everyday home technology, electrical energy cost estimates, Wi-Fi troubleshooting, USB-C compatibility.
- Primary reader benefit: solve a problem without purchasing anything.
- Supporting articles link to interactive tools rather than thin keyword variants.
- Site includes an XML sitemap, page-specific titles/descriptions, About and Privacy pages.
- No claim is made about actual search volume or traffic until Search Console data confirms it.
- Domain is currently the existing Netlify subdomain; only change canonical/sitemap host when a custom domain is attached.

## Automation

1. **Weekly QA:** `.github/workflows/site-qa.yml` runs a local-link, metadata and site-file audit on commits and Mondays, and produces a review queue. It does not fabricate article update dates or claim that outbound sources were checked.
2. **AI drafts:** `.github/workflows/practical-pick-draft.yml` can propose one draft per week **only after** a free/approved OpenAI-compatible model and API key are configured. AI drafts are not published automatically. Every factual claim and primary source should be confirmed before publishing.
3. **Publishing:** merge genuinely reviewed pages into main. Static Netlify deployment then updates the site through its existing Git integration.

## Organic growth plan

- Publish detailed answers to long-tail troubleshooting questions and add helpful tools for the same audience.
- Add relevant official manufacturer/agency sources and fix gaps before seeking rankings.
- Connect Google Search Console, inspect actual impressions/queries monthly and improve pages based on user intent.
- Do not post dozens of low-value AI pages or fabricated hands-on reviews.
- Gradually expand one adjacent cluster at a time after measuring real results.

## Advertising later

Google AdSense is not active. Before applying, confirm original content depth, working publisher contact channel, privacy disclosures, any applicable cookie consent solution, site ownership, and Google publisher policies. Add ads.txt and ad code **only** from a real approved AdSense account. No secrets or paid APIs in this repository.

## Energy math

`kWh = watts / 1000 * hours_per_day * days`
`estimated_cost = kWh * dollars_per_kWh`

Checks and reader disclosures distinguish a simple energy-only estimate from full utility bills and fluctuating actual loads.


## Free Google Search Console setup (owner verification required)

Search Console is free. A paid third-party Search Console connector is **not needed** and is currently unavailable for this project. The site now advertises its sitemap in `robots.txt`, and every public page has a self-referencing canonical link.

1. Visit https://search.google.com/search-console and sign in to the Google account that will own this site.
2. Add a **URL prefix** property with the exact URL `https://autoruntest.netlify.app/`. This is easier than DNS verification while using a Netlify subdomain.
3. Choose the **HTML file verification** method and download Google's generated verification file. Add that exact file to the repository root through a GitHub PR (or send its filename and contents to a maintainer to publish). Click **Verify** in Search Console only after it is live. Do not invent verification tokens.
4. In Search Console → Sitemaps, submit `https://autoruntest.netlify.app/sitemap.xml`.
5. In the Performance → Search results report, monitor clicks, impressions, pages and queries. Newly added sites may have little or no data initially. Avoid judging topic demand until sufficient real impressions arrive.

**Monthly SEO decision rule:** prioritize pages receiving genuine impressions but low click-through rates, queries where existing guides can answer a clearer question, and useful companion tools. Do not mass-generate dozens of thin pages. Record the measurement period and actual observed numbers when changing strategy.

When a verified custom domain is introduced, update the canonical URLs, sitemap and robots file to the new host together and submit the new property/sitemap.


## Automatic illustrated long-form publishing (October 2026)

The site publishes one **pre-written, structured, source-linked guide** per Wednesday using `.github/workflows/publish-weekly.yml`. The queue is in `content/publishing-queue.json` and the stdlib-only generator is `scripts/publish_queue.py`. A new article includes original inline SVG explanatory artwork, clear subsections, linked primary sources, no false hands-on claims, and a machine-readable Article schema. The publisher also refreshes `latest.html` and the XML sitemap, runs `scripts/site_audit.py`, and commits only actual changes. Netlify deploys from GitHub main.

The first article was published with this release. Five additional substantive guides are ready for release, one each week. **This is a finite queue**: when exhausted, the publisher explicitly does not fabricate articles or fake updated dates. To keep publication going indefinitely, a contributor or connected AI drafting service must add additional credible article entries to the queue after checking source quality. The optional AI draft workflow already in this repository prepares unpublished suggestions, but requires an explicitly approved API provider; it cannot automatically guarantee accuracy.

### Editing workflow

1. Add one new complete article object to `content/publishing-queue.json` with unique slug, verified primary-source references, at least five sections and 325 words in body sections.
2. Confirm no invented personal experience, testing, pricing or manufacturer claims.
3. On Wednesday, the free GitHub Actions job publishes at most one unpublished queue entry. The workflow can also be started manually in GitHub Actions.
4. Monitor the weekly QA workflow. If sources materially change, update existing articles and note the real changes rather than silently changing the publication date.

### Operating limits

- The system **does not** automatically research external changes, verify every source, or renew an exhausted queue.
- A Google Search Console account remains unverified until site ownership is completed.
- Advertising is not active, and there is no guarantee of search traffic or AdSense approval.
- GitHub Actions scheduled workflows can be delayed and may be disabled after 60 days of repository inactivity on public repositories. Confirm the workflow actually runs in Actions.

## Editorial release cadence — three publishing slots, one refresh, one tool

Schedules are GitHub Actions cron times in UTC and can run later than scheduled:

| Schedule | Workflow | What actually happens |
| --- | --- | --- |
| Monday, Wednesday, Friday at 13:37 UTC | `.github/workflows/publish-weekly.yml` | Publish **at most one** previously prepared, source-linked illustrated guide per slot; run static QA first |
| Sunday at 15:15 UTC | `.github/workflows/refresh-weekly.yml` | Apply **at most one** specific substantive revision from `content/refresh-queue.json`, with a real textual change; otherwise skip |
| First Tuesday each month at 15:42 UTC | `.github/workflows/tools-monthly.yml` | Publish **at most one** previously built and reviewed tool from `content/tool-release-queue.json` and update links/sitemap |

A prepared illustrated guide uses the queue schema in `content/publishing-queue.json`. Adding a new entry requires factual review, at least five meaningful sections, credible source references and no fabricated test results. All release tasks are gated by `scripts/site_audit.py` before committing. The generator never invents an article when the queue is empty.

**Capacity and limitations:** Five further illustrated guides, one substantive page revision and one runtime calculator are initially available for these schedules. This is NOT enough to sustain three new articles each week or a new tool each month indefinitely. The editor or an approved free AI research service must continue adding high-quality, source-checked queue items. The existing optional AI draft action needs provider credentials and does not automatically supply verified queue entries.

GitHub Actions may disable scheduled workflows for inactivity in public repos, and scheduled runs are not guaranteed to fire at an exact minute. Verify workflow runs, QA results and production deployment after each release. Revisions do not claim source verification unless someone has actually performed it. No AdSense or paid APIs are enabled.
