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
