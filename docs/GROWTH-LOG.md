# Living Water – Growth Log (running record)

Session routine: 1) check Search Console (queries, pages, indexing) 2) check competitors for core keywords 3) rank backlog by ranking potential > commercial value > probability > speed 4) execute top items, verify live 5) update this log.

## Baseline (2026-11-27, GSC last 28 days; data starts Nov 20)
Clicks 9 · Impressions 1.04K · Avg position 27.9 · Indexed 98 · Not indexed 53 (21 staging noindex, 15 redirects, 5 old 404s, 6 crawled-not-indexed, 6 other) · Pages 112 · Backlinks/reviews: not measured

## Completed
- 2026-11-26: interlock calculator + $3.50 offer page; elevator pit pricing; image audit on 19 service pages + extra FAQs; builders page; client logos; WhatsApp button; pricing page; condo + elevator-company pages; 6 new guides; mobile tap targets, hover/focus polish; Pricing in nav; city-page cost FAQs; case-study rotation.
- 2026-11-27 (later): GBP verified—website link already https+UTM; added services 'Interlock cleaning, sanding and sealing' and 'Paver and stone sealing' (pending Google review); 39 Google reviews seen; new guides: power vs pressure washing, interlock/paver sealing.
- 2026-11-27: honest dateModified/lastmod registry; new titles (industrial, cost guide, home description); full reassessment doc.

## Findings to fix (needs owner)
- NAP inconsistency: BBB listing shows 11 Wedgewood Dr, North York; Toronto Jobs shows 637 Petrolia Rd; Hotfrog/Indeed/ConstructConnect old listings. Claim and correct to 130 Cook's Mill Cres, Vaughan, (416) 663-8000.
- Instagram bio says 'over 20 years'; site says since 1998 (28 years); GBP says 'over 25 years'. Align.

## Backlog (ranked)
(GBP post submitted 2026-11-27)
1. GBP: products added 2026-11-27 (done). Still to do: post about winter elevator pit / spring interlock offer – high value
2. Reviews: Google + HomeStars follow-up process – high value
3. Directory/citation profiles: HomeStars, BBB, Houzz, Yellow Pages – needs user accounts
4. Lock staging.livingwater-pws.com – needs DNS/hosting access
5. Request indexing for 6 crawled-not-indexed pages – GSC (user session)
6. Refresh pages with impressions but no clicks (industrial, roof, deck, cost guide) using GSC query data – next session once data accrues
7. Case-study pages with real job details (2) – needs job facts from user
8. Guides: stone sealing, heritage brick, spring interlock maintenance
9. Backlink outreach list (condo/property-manager groups, builder groups, manufacturers)
10. Monthly AI-answer check (ChatGPT, Perplexity, Google AIO, Copilot)
11. GA4: mark generate_lead + whatsapp_click as key events (needs GA admin)

## Open questions for owner
Confirm: HST extra, "from" pricing, re-clean guarantee, 2–5 day booking, 2–4 yr reseal, elevator-company subcontracting. $3.50/sq ft is at the high end of third-party ranges. Missing client logos.

## 2026-11-27 — Google Business Profile products
- Added 2 GBP products using site photos (submitted; Google shows them within ~30 min):
  1. Elevator Pit Cleaning - Single Pit, $1,500 CAD (from, before HST), category "Elevator Pit Cleaning", links to /elevator-pit-cleaning/.
  2. Interlock Wash, Sand & Seal, $3.50 per sq ft before HST, category "Interlock Cleaning and Sealing", links to the $3.50 page.
- Landing URLs carry UTM (utm_campaign=gbp-products) for GA4 tracking.
- Next: verify products are live; GBP post for winter elevator-pit / spring interlock; possible condo garage cleaning product (quote-based).

## 2026-11-27 (later) — Search Console first query data + anchor fix
- GBP: both products confirmed in the products list; post (winter elevator pit + spring interlock, UTM-tagged button) submitted, pending Google review.
- GSC (6 days of data): top queries "pressure washing toronto" 92 impr pos 23; "power washing toronto" 52 pos 11; "commercial pressure washing" 46 pos 23; homepage is 417 impr, pos 15.9; Industrial page 117 impr pos 27.
- Finding: for "commercial pressure washing" Google served the Industrial page (pos 25) and Commercial page ranked ~62. All internal anchors said "Commercial Power Washing".
- Fix (live, IndexNow pinged): nav/anchor text now "Commercial Pressure Washing" and "Industrial Pressure Washing"; autolink for those exact phrases. Re-check in ~2 weeks whether Commercial page overtakes Industrial for that query.
- Watch: queries with pos 3-5 but 0 clicks ("power washing companies toronto", "pressure washer near toronto") — likely personalized/tiny samples; revisit when volume grows.
- Next: refresh roof/deck/cost-guide pages (pos 50-75), homepage for "pressure washing toronto" pos 23.

## 2026-11-27 (midday)
- Roof and deck pages deepened (identification, timing, process, 3 new FAQs each, internal links); roof title now leads with "Roof Moss Removal" (GSC: pos ~70-75).
- Titles: homepage adds "Power Washing" (query pos 11); pricing page adds "Cost".
- GSC "Request indexing" done for Commercial, Roof and Home pages (works from the Chrome session; ~10/day limit).
- GSC indexing review: the 53 non-indexed are legacy WP/staging URLs (wildcards, feeds, plugins); real redirects (/testimonials/, /power-washing-services-2/, sitemap_index.xml) already 301 correctly. The pricing page is already indexed.
- New guide: cleaning heritage brick and stone in Toronto (supports Historical Remediation page).
- Re-check GSC around Dec 10 for: Commercial vs Industrial page for "commercial pressure washing"; roof/deck positions.

## 2026-11-27 (afternoon)
- New guide: remove oil and rust stains from concrete and pavers (homeowner-intent, links to driveway/sealing/power-vs-pressure).
- Homepage title shortened to 54 chars ("Pressure Washing & Power Washing Toronto | Living Water").
- GBP: uploaded 5 job photos (interlock walkway, condo terrace hot-water wash, roof moss after, rust stain removal after, commercial lobby); 3+ visible as Pending Google review (grid lazy-loads, count unconfirmed).
- Content-depth scan: no thin pages (smallest real pages ~400 words, case studies).
- Note: Cloudflare Pages deploy time varies 1–8 min; check via `gh api .../check-runs` before verifying live.
- Still open for owner: Cloudflare login is signed out in Chrome (not needed unless deploys fail); GBP description says "over 25 years" vs site "since 1998".
- 2026-11-27: Decision (owner delegated): standard wording is "since 1998" (specific, verifiable, never goes stale). GBP description rewritten with "since 1998", $5M insured/WSIB, full service list incl. interlock sealing and roof moss; submitted, pending Google review (opening date already June 1998). Remaining: Instagram bio still says "over 20 years" -> change to "Since 1998" (needs Instagram login).
