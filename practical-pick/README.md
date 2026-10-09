# Practical Pick — independent site in AutoRun

This subproject is a user-directed editorial pilot using the AutoRun repository for source control. It is **not** a replacement for AutoRun's public AI Business From $0 dashboard, does not revise CONSTITUTION.md, and makes no claim of revenue or AdSense approval.

## Deploy separately

In Netlify, import EMSCodeSim/AutoRun as a **new** site. Set Base directory to `practical-pick` and Publish directory to `.` (or use a production deploy context with the subdirectory as publish root). Do **not** change the existing AutoRun site's build or publish settings. Add a real domain, canonical tags, a verified contact method, legally appropriate privacy/cookie disclosures and sitemap once the final URL is known.

## AI pipeline

The root GitHub Actions workflow `.github/workflows/practical-pick-draft.yml` makes an **unpublished** weekly draft proposal. It runs only when `PRACTICAL_PICK_AI_API_KEY` is explicitly configured, and it will use whichever OpenAI-compatible provider is designated by `PRACTICAL_PICK_AI_BASE_URL`. **No provider is guaranteed free.** Confirm free pricing, quotas, and no-cost access before enabling any keys; the AutoRun constitution disallows paid usage without approval.

Each proposal becomes a pull request containing a draft JSON file in `practical-pick/drafts/`. A person must verify claims and original sources and deliberately add the article to the published HTML pages. Do not automatically merge article PRs. Do not invent testing, customer testimonials, revenue, visits or endorsement.

AdSense is **not active**. Apply only after privacy and publisher requirements are met; preserve the actual seller ID and correct ads.txt and consent obligations. Never click your own ads or buy artificial traffic.

## Scope

The present site includes a responsive landing page and three baseline guides, each explicitly non-hands-on. The AI draft generator and workflow are a safeguarded starting point, not a guarantee of passive income or full autonomy.
