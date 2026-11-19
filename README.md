# Living Water Pressure Wash Services — livingwater-pws.com

Static, fast, SEO + GEO optimized rebuild of livingwater-pws.com. No WordPress, no plugins, no database — plain HTML/CSS/JS that can be hosted anywhere (GitHub Pages, Netlify, Cloudflare Pages, or any web host).

## What's included
- 20 indexable pages, same URL slugs as the old WordPress site (no ranking loss from changed URLs)
- New `/service-areas/` page covering 31 GTA / Ontario communities
- Only original Living Water job photos, renamed with descriptive filenames, descriptive alt text, responsive WebP (480/960/1600px)
- Before/after drag sliders + lightbox gallery
- Self-hosted fonts (Josefin Sans + Public Sans), same teal/navy theme as the original

## SEO
- Unique title, meta description, canonical, Open Graph and Twitter tags on every page
- JSON-LD: LocalBusiness/HomeAndConstructionBusiness (NAP, 3 phone lines, 24/7 emergency, areaServed, credentials, service catalog), WebSite, Service (per service page), BreadcrumbList, FAQPage, ImageGallery, AboutPage, ContactPage
- `sitemap.xml`, `robots.txt`, 404 page, internal linking (related services, breadcrumbs, footer)
- Core Web Vitals: preloaded hero image + fonts, lazy-loaded images with width/height, ~4 KB of JS

## GEO (AI search: ChatGPT, Perplexity, Google AI Overviews, Claude)
- `llms.txt` with company facts, services and FAQ
- `robots.txt` explicitly allows AI crawlers (GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, Google-Extended…)
- "Answer-first" summary paragraph at the top of every page, a facts table (founded, insurance, rating, area, phones) and FAQs written as quotable answers

## SEO/GEO pass 2 (added)
- 19 city landing pages (`/pressure-washing-<city>/`) with local neighbourhoods, services, FAQs and City-scoped Service schema
- 6 expert guides (`/guides/`) written answer-first for AI search, with Article + FAQPage schema
- WebPage schema with `speakable`, `dateModified` and breadcrumbs on every page; per-page 1200×630 social images
- Image sitemap (every photo + alt text), `_redirects` (old WordPress URLs → new pages, 301), `_headers` (1-year asset caching, security headers, `noindex` on the *.pages.dev preview)
- `llms-full.txt` (full site text for AI crawlers) and an IndexNow key + `tools/indexnow.sh` to ping Bing after updates

## Pass 3 (added)
- New pages: `/reviews/`, `/faq/` (all FAQs, FAQPage schema), `/industries/`, plus 5 more guides (11 total)
- Trust bar under every hero, "At a glance" facts on service pages, "On this page" jump links on long pages
- Mobile sticky Call / 24/7 / Free Quote bar; quote form now accepts a photo
- Anchor ids on every H2 (deep links for Google and AI citations), Article `og:type` on guides

## Adding new job photos (case studies)
1. Put each job in its own folder: `before.jpg` + `after.jpg` (or `before-1`/`after-1`, `before-2`/`after-2`…), any extra photos, and an optional `notes.txt`:
   ```
   title: Condo elevator pit clean-up after winter
   service: elevator-pit-cleaning
   location: North York
   date: 2026-11
   description: Two-elevator condo pit with salt sludge and standing water.
   ```
2. `python3 tools/add_photos.py /path/to/photos` then `python3 tools/gen.py .`
3. Each job becomes a `/projects/<name>/` case study, appears on its service page and matching city page, and is added to the sitemap.

## Before going live — to do
1. **Quote form**: uses formsubmit.co (free). Submit the form once after launch, then click the activation link sent to info@livingwater-pws.com.
2. **Business address**: if you have a public address, add `streetAddress` + `postalCode` in `tools/gen.py` (BUSINESS → address). Make sure name/phone match your Google Business Profile exactly.
3. **Google Business Profile URL** (most important local-SEO signal): add it to `sameAs` in the schema, plus Facebook/Instagram/etc.
4. Submit `https://livingwater-pws.com/sitemap.xml` in Google Search Console and Bing Webmaster Tools.
5. Safety Policy PDF: drop the PDF in `/assets/` and link it from `/safety-policy/` if you want it downloadable.

## Hosting on GitHub Pages
Settings → Pages → Deploy from branch → `main` / root. Then set custom domain `livingwater-pws.com` and point DNS (A records to GitHub Pages IPs, or CNAME `www` to `pay4mm-star.github.io`).

## Editing
Content lives in `tools/content.py`; layout in `tools/gen.py`. Rebuild with `python3 tools/gen.py .` (requires `tools/manifest.json`; images are already in `assets/img`). Or edit the HTML directly.
