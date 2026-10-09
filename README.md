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
