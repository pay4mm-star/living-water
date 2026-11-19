# City landing pages + guides. Executed inside gen.py's namespace.

def city_links(exclude=None):
    return "".join(f'<li><a href="/pressure-washing-{c["slug"]}/">{c["name"]}</a></li>' for c in CITIES if c["slug"] != exclude)


def city_page(c):
    path = f"/pressure-washing-{c['slug']}/"
    name = c["name"]
    trail = [("Home", "/"), ("Service Areas", "/service-areas/"), (name, path)]
    hoods = "".join(f"<li>{h}</li>" for h in c["hoods"])
    near = [CITY[n] for n in c["nearby"] if n in CITY]
    near_html = "".join(f'<a href="/pressure-washing-{n["slug"]}/">Pressure washing in {n["name"]} →</a>' for n in near)
    keys = []
    for k in [c["hero"]] + [SERVICES[x]["card"] for x in c["services"]]:
        if k not in keys:
            keys.append(k)
    photos = "".join(photo(k) for k in keys[:6])
    faqs = [
        (f"Do you offer pressure washing in {name}?",
         f"Yes. Living Water provides residential, commercial and industrial pressure washing, sandblasting, brick and stone cleaning, efflorescence and graffiti removal, and 24/7 disaster restoration throughout {name}, including {', '.join(c['hoods'][:5])}."),
        (f"How quickly can you book a job in {name}?",
         f"Residential pressure washing in {name} is usually booked within 2–5 days, with same-week service standard. Commercial and emergency clients can call our 24/7 line at {PHONE_EMERG[1]}."),
        (f"Do you charge for quotes in {name}?",
         "No. Assessments are free and you receive a fixed written quote — with our Certificate of Insurance and WSIB clearance — before any work starts."),
        (f"Which services are most requested in {name}?",
         "Most requested here: " + ", ".join(SERVICES[x]["nav"] for x in c["services"][:4]) + "."),
    ]
    intro = "".join(f"<p>{esc(p)}</p>" for p in c["intro"])
    body = f"""
<section class="page-hero"><picture>{hero_img(c["hero"], "100vw", eager=True, alt="")}</picture>
<div class="wrap">{crumbs_html(trail)}<span class="pill">{esc(c["region"])}</span><h1>Pressure Washing &amp; Restoration in {esc(name)}</h1>
<p>Residential, commercial and industrial pressure washing, sandblasting, brick and stone restoration in {esc(name)} — $5M insured, WSIB covered, rated 4.9★ on Google, serving the GTA since 1998.</p>
<div class="cta-row" style="justify-content:flex-start"><a class="btn" href="/contact/#quote">Get a Free Quote</a><a class="btn ghost" href="tel:{PHONE_MAIN[0]}">Call {PHONE_MAIN[1]}</a></div></div></section>
<section><div class="wrap layout">
<article class="prose"><p class="answer">Living Water Pressure Wash Services provides professional pressure washing, soft washing, sandblasting, brick and stone cleaning, efflorescence and graffiti removal, and 24/7 disaster restoration in {esc(name)}, Ontario. Call {PHONE_MAIN[1]} for a free, fixed written quote.</p>
{reviewed_line()}
{intro}
<h2>Local considerations in {esc(name)}</h2><ul class="ticks">{"".join(f"<li>{esc(x)}</li>" for x in LOCAL.get(c["slug"], []))}</ul>
<h2>Neighbourhoods we serve in {esc(name)}</h2><ul class="areas" style="justify-content:flex-start">{hoods}</ul>
<h2>Why {esc(name)} property owners choose Living Water</h2>
<ul class="ticks"><li>28 years of experience and 7,500+ properties cleaned across the GTA</li><li>Surface-specific methods — soft wash, hot-water pressure, steam and media blasting</li><li>$5M liability insurance, WSIB coverage and ISSA-GBAC certification</li><li>Fixed written quotes, before-and-after photos and a free re-clean guarantee</li><li>24/7 emergency line for commercial, industrial and disaster restoration</li></ul>
</article>
<aside class="side">{quote_aside()}<div><h3>Nearby areas</h3><nav class="related" aria-label="Nearby areas">{near_html}<a href="/service-areas/">All service areas →</a></nav></div></aside>
</div></section>
<section class="soft"><div class="wrap"><div class="section-head"><span class="pill light">Services in {esc(name)}</span><h2>Most requested services in {esc(name)}</h2></div>{service_cards(c["services"])}</div></section>
<section><div class="wrap"><div class="section-head"><span class="pill light">Our Work</span><h2>Recent Living Water projects</h2><p>Real photos from Living Water jobs across Toronto and the GTA.</p></div><div class="grid g3">{photos}</div></div></section>
{projects_section(location=name.split(" & ")[0])}
{faq_block(faqs, "Pressure washing in " + esc(name) + ": FAQ")}
{cta_block()}"""
    svc_ld = {"@context": "https://schema.org", "@type": "Service", "@id": SITE + path + "#service",
              "name": f"Pressure washing and restoration in {name}", "serviceType": "Pressure washing",
              "provider": {"@id": ORG_ID},
              "areaServed": {"@type": "City", "name": name, "containedInPlace": {"@type": "AdministrativeArea", "name": c["region"] + ", Ontario"}},
              "hasOfferCatalog": {"@type": "OfferCatalog", "name": f"Services in {name}",
                                  "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": SERVICES[x]["nav"], "url": f"{SITE}/{x}/"}} for x in c["services"]]}}
    title = f"Pressure Washing {name} | Sandblasting & Restoration"
    if len(title) > 60:
        title = f"Pressure Washing {name} | Living Water"
    if len(title) > 60:
        title = f"Pressure Washing {name}"
    desc = f"Pressure washing, sandblasting, brick & stone cleaning in {name}. Since 1998, $5M insured, 4.9★ Google. Free fixed quotes: {PHONE_MAIN[1]}."
    if len(desc) > 158:
        desc = f"Pressure washing, sandblasting and brick & stone cleaning in {name}. Since 1998, $5M insured, 4.9★ on Google. Free quotes."
    page(path, title, desc, body, schema=[svc_ld, crumbs_ld(trail), faq_ld(faqs)], preload=c["hero"], priority="0.8", crumbs=True)


def guide_page(g):
    path = f"/guides/{g['slug']}/"
    short = g["title"].split(":")[0].split("?")[0] + ("?" if "?" in g["title"].split(":")[0] else "")
    trail = [("Home", "/"), ("Guides", "/guides/"), (short, path)]
    rel = "".join(f'<a href="/{x}/">{SERVICES[x]["nav"]} →</a>' for x in g["related"])
    other = "".join(f'<a href="/guides/{o["slug"]}/">{esc(o["title"])}</a>' for o in GUIDES if o["slug"] != g["slug"])
    updated = datetime.date.today().strftime("%B %Y")
    body = f"""
<section class="page-hero"><picture>{hero_img(g["hero"], "100vw", eager=True, alt="")}</picture>
<div class="wrap">{crumbs_html(trail)}<span class="pill">Expert Guide</span><h1>{esc(g["title"])}</h1>
<p>By the Living Water team · 28 years cleaning and restoring GTA properties · Updated {updated}</p></div></section>
<section><div class="wrap layout">
<article class="prose"><p class="answer"><strong>Short answer:</strong> {esc(g["answer"])}</p>{toc(g["body"])}{g["body"]}
<h2>Need help with your property?</h2><p>Living Water has cleaned and restored 7,500+ properties across Toronto and the GTA since 1998. Call <a href="tel:{PHONE_MAIN[0]}">{PHONE_MAIN[1]}</a> or <a href="/contact/#quote">request a free quote</a>.</p></article>
<aside class="side">{quote_aside()}<div><h3>Related services</h3><nav class="related" aria-label="Related services">{rel}</nav></div><div><h3>More guides</h3><nav class="related" aria-label="More guides">{other}</nav></div><div><h3>Resources</h3><nav class="related" aria-label="Resources"><a href="/faq/">All FAQs →</a><a href="/glossary/">Glossary of terms →</a><a href="/gallery/">Before &amp; after gallery →</a><a href="/about-us/">About Living Water →</a></nav></div></aside>
</div></section>
{faq_block(g["faqs"], "Related questions")}
{cta_block()}"""
    art = {"@context": "https://schema.org", "@type": "Article", "@id": SITE + path + "#article", "headline": g["title"][:110],
           "description": g["meta"], "image": SITE + "/assets/img/" + og_for(g["hero"]),
           "datePublished": "2026-11-17", "dateModified": TODAY,
           "author": {"@type": "Organization", "@id": ORG_ID, "name": NAME, "url": SITE + "/about-us/"},
           "publisher": {"@id": ORG_ID}, "mainEntityOfPage": SITE + path, "inLanguage": "en-CA",
           "about": [SERVICES[x]["service_type"] for x in g["related"]]}
    t = g["title"] if len(g["title"]) <= 48 else short
    page(path, (t + " | Living Water") if len(t) <= 47 else (g["title"] if len(g["title"]) <= 60 else t), g["meta"][:160], body, schema=[art, crumbs_ld(trail), faq_ld(g["faqs"])],
         preload=g["hero"], priority="0.7", crumbs=True, og_type="article")


def guides_hub():
    path = "/guides/"
    trail = [("Home", "/"), ("Guides", path)]
    cards = ""
    for g in GUIDES:
        cards += (f'<article class="card">{img(g["hero"], "(max-width: 640px) 100vw, 33vw")}<div class="body"><span class="tag">Guide</span>'
                  f'<h3><a href="/guides/{g["slug"]}/">{esc(g["title"])}</a></h3><p>{esc(g["meta"])}</p><span class="more">Read guide →</span></div></article>')
    body = f"""
<section class="page-hero"><picture>{hero_img("brick-wall-cleaning-technician", "100vw", eager=True, alt="")}</picture>
<div class="wrap">{crumbs_html(trail)}<span class="pill">Expert Guides</span><h1>Pressure Washing &amp; Restoration Guides</h1><p>Straight answers from a GTA contractor with 28 years of experience — methods, schedules, and what to ask before you hire.</p></div></section>
<section><div class="wrap"><h2 class="sr-only">All guides</h2><div class="grid g3">{cards}</div></div></section>
{cta_block()}"""
    lst = {"@context": "https://schema.org", "@type": "ItemList",
           "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{SITE}/guides/{g['slug']}/", "name": g["title"]} for i, g in enumerate(GUIDES)]}
    page(path, "Pressure Washing & Restoration Guides | Living Water",
         "Expert guides on soft washing, efflorescence, sandblasting brick, cleaning schedules, elevator pits and hiring a contractor in the GTA.",
         body, schema=[lst, crumbs_ld(trail)], preload="brick-wall-cleaning-technician", priority="0.7", page_type="CollectionPage", crumbs=True)


def tech_extra():
    import re as _re, secrets as _sec
    # image + page sitemap (overwrites the basic one)
    rows = []
    for p, pr in PAGES:
        meta = PAGE_META.get(p, {})
        imgs = "".join(f"<image:image><image:loc>{SITE}{best(k)}</image:loc><image:title>{esc(M[k]['alt'])}</image:title></image:image>" for k in meta.get("imgs", [])[:20])
        rows.append(f"<url><loc>{SITE}{p}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority>{imgs}</url>")
    open(OUT + "/sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n' + "\n".join(rows) + "\n</urlset>\n")

    # Cloudflare Pages: redirects for old WordPress URLs
    open(OUT + "/_redirects", "w").write("""# Old WordPress URLs -> new pages (301)
/thankyou /thank-you/ 301
/thankyou/ /thank-you/ 301
/power-washing-services-2/ /power-washing-services/ 301
/home-old/ / 301
/testimonials/ /reviews/ 301
/category/* / 301
/feed/ / 301
/feed / 301
/comments/feed/ / 301
/home/ / 301
/services/ /power-washing-services/ 301
/services /power-washing-services/ 301
/fire-damage-restoration/ /disaster-restoration/ 301
/water-damage-restoration/ /disaster-restoration/ 301
/specialised-cleaning-services/ /power-washing-services/ 301
/wp-login.php / 301
/wp-admin/* / 301
/wp-content/uploads/* /gallery/ 301
/index.php / 301
""")
    # Cloudflare Pages: caching + security headers
    open(OUT + "/_headers", "w").write("""/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: SAMEORIGIN
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()
  Strict-Transport-Security: max-age=31536000; includeSubDomains

/assets/*
  Cache-Control: public, max-age=31536000, immutable

/favicon.ico
  Cache-Control: public, max-age=604800

/*.html
  Cache-Control: public, max-age=0, must-revalidate

/llms.txt
  Content-Type: text/plain; charset=utf-8

/llms-full.txt
  Content-Type: text/plain; charset=utf-8

https://:project.pages.dev/*
  X-Robots-Tag: noindex
""")
    # IndexNow key (Bing, Yandex, Seznam, Naver) - stable key
    keyfile = [f for f in os.listdir(OUT) if _re.fullmatch(r"[0-9a-f]{32}\.txt", f)]
    key = keyfile[0][:-4] if keyfile else _sec.token_hex(16)
    open(f"{OUT}/{key}.txt", "w").write(key)
    open(OUT + "/tools/indexnow.sh", "w").write(f"""#!/bin/sh
# Ping IndexNow (Bing etc.) after publishing changes. Run from repo root.
URLS=$(grep -o '<loc>[^<]*</loc>' sitemap.xml | grep -v '/assets/' | sed 's/<[^>]*>//g' | sed 's/.*/"&"/' | paste -sd, -)
curl -s -X POST https://api.indexnow.org/indexnow -H 'Content-Type: application/json' \\
  -d "{{\\"host\\":\\"livingwater-pws.com\\",\\"key\\":\\"{key}\\",\\"keyLocation\\":\\"{SITE}/{key}.txt\\",\\"urlList\\":[$URLS]}}"
echo done
""")
    # llms-full.txt: full plain-text content of every page
    from html.parser import HTMLParser

    class T(HTMLParser):
        def __init__(self):
            super().__init__(); self.out = []; self.skip = 0; self.inmain = False
        def handle_starttag(self, tag, a):
            if tag == "main": self.inmain = True
            if tag in ("script", "style", "aside", "nav", "picture"): self.skip += 1
            if tag in ("h1", "h2", "h3"): self.out.append("\n" + {"h1": "# ", "h2": "## ", "h3": "### "}[tag])
            if tag in ("p", "li", "tr", "summary", "dt"): self.out.append("\n- " if tag == "li" else "\n")
        def handle_endtag(self, tag):
            if tag == "main": self.inmain = False
            if tag in ("script", "style", "aside", "nav", "picture"): self.skip -= 1
        def handle_data(self, d):
            if self.inmain and not self.skip: self.out.append(d)

    parts = [f"# {NAME} — full site content\n\nSource: {SITE}/ · Updated {TODAY}\n"]
    for p, _ in PAGES:
        fn = OUT + p + ("index.html" if p.endswith("/") else "")
        t = T(); t.feed(open(fn).read())
        txt = _re.sub(r"\n\s*\n+", "\n", "".join(t.out)).strip()
        parts.append(f"\n\n---\nURL: {SITE}{p}\n{txt}")
    open(OUT + "/llms-full.txt", "w").write("".join(parts))
    # add guides + cities to llms.txt
    extra = "\n## Service area pages\n" + "\n".join(f"- [Pressure washing in {c['name']}]({SITE}/pressure-washing-{c['slug']}/)" for c in CITIES)
    extra += "\n\n## Expert guides\n" + "\n".join(f"- [{g['title']}]({SITE}/guides/{g['slug']}/): {g['answer']}" for g in GUIDES)
    extra += f"\n\n## Full content\n- [llms-full.txt]({SITE}/llms-full.txt)\n"
    open(OUT + "/llms.txt", "a").write(extra)
