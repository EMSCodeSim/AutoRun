# Practical Pick

**Practical Pick** is an independent practical-buying-guide website. This repository formerly hosted **AutoRun — AI Business From $0**, which the owner explicitly chose to replace. The previous content may remain in Git history; the deployed root site now serves Practical Pick.

## Current state

- Responsive standalone HTML/CSS website at repository root.
- Three original introductory guides in `articles/`.
- AI drafting tool in `scripts/generate_draft.py` (never directly publishes).
- Weekly GitHub Actions workflow at `.github/workflows/practical-pick-draft.yml`.
- No active AdSense application, ad unit, revenue claim, or affiliate account.
- No AI API credentials committed to source control.

## Deployment

The existing Netlify project may already deploy the repository root. Keep its publish directory as the repository root (or `.`) and build command blank, because this is static HTML. Confirm the existing Netlify site's Git branch and deploy configuration before assuming the new version is publicly live.

## Optional AI drafting

The draft workflow runs Tuesdays at 14:15 UTC or manually. Without credentials, it does nothing and costs nothing. To enable it, only after independently verifying that the provider has a genuinely free option without charges or auto-converting billing, configure GitHub Actions:

- Repository secret `PRACTICAL_PICK_AI_API_KEY`
- Repository variable `PRACTICAL_PICK_AI_BASE_URL` (HTTPS OpenAI-compatible API base)
- Repository variable `PRACTICAL_PICK_AI_MODEL`

The generator cannot browse live sources, so its output is unverified. It creates a draft proposal pull request, **not** a public article. Verify the draft against current authoritative sources, edit, and intentionally publish once ready. The weekly job can be disabled in the Actions interface.

## AdSense launch requirements

Before applying for ads, provide a real contact method, publisher information, privacy/cookie policy appropriate for the jurisdictions served, any legally required consent management, stable domain and canonical/sitemap configuration, original valuable articles, and accurate ad/affiliate disclosure. Add AdSense code and ads.txt only from an approved publisher account. Never invent publisher IDs.

## Editorial standards

- No fake testing, ratings, reviews or endorsements.
- Clear separation of documented specifications and experience.
- Link relevant primary sources where claims warrant verification.
- No scaled publication of thin AI-generated pages.
- Never fabricate traffic, earnings, costs or affiliate commissions.
- Do not activate paid APIs or usage-based billing without explicit approval.
