import json, os, html, sys, datetime
from content import *

OUT = sys.argv[1]
M = json.load(open("/home/claude/build/manifest.json"))
TODAY = datetime.date.today().isoformat()
PAGES = []  # (path, priority)
esc = html.escape

# ------------------------------------------------------------ helpers
def srcset(k):
    return ", ".join(f"/assets/img/{k}-{w}.webp {w}w" for w in M[k]["sizes"])

def best(k, maxw=1600):
    s = [w for w in M[k]["sizes"] if w <= maxw]
    return f"/assets/img/{k}-{s[-1]}.webp"

def img(k, sizes="(max-width: 700px) 100vw, 50vw", cls="", eager=False, alt=None):
    m = M[k]
    w = m["sizes"][-1]; h = round(m["h"] * w / m["w"])
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ""
    return (f'<img src="{best(k, 960)}" srcset="{srcset(k)}" sizes="{sizes}" width="{w}" height="{h}" '
            f'alt="{esc(alt or m["alt"])}" {load}{c}>')

def ba(before, after, title="", caption=""):
    cap = f"<figcaption><strong>{esc(title)}</strong>{esc(caption)}</figcaption>" if title else ""
    return f'''<figure><div class="ba">
{img(before)}
<div class="after">{img(after)}</div>
<span class="lbl b">Before</span><span class="lbl a">After</span><div class="bar"></div>
<input type="range" min="0" max="100" value="50" aria-label="Drag to compare before and after: {esc(title or M[after]["alt"])}">
</div>{cap}</figure>'''

def photo(spec):
    if "|" in spec:
        b, a = spec.split("|"); return ba(b, a, "Before & after", " — " + M[a]["alt"])
    return f'<figure>{img(spec, "(max-width: 700px) 100vw, 33vw")}<figcaption>{esc(M[spec]["alt"])}</figcaption></figure>'

def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + "</script>"

ORG_ID = SITE + "/#business"
BUSINESS = {
    "@context": "https://schema.org",
    "@type": ["LocalBusiness", "HomeAndConstructionBusiness"],
    "@id": ORG_ID,
    "name": NAME,
    "legalName": LEGAL,
    "alternateName": ["Living Water", "Living Water PWS", "Living Water Pressure Washing"],
    "url": SITE + "/",
    "logo": SITE + "/assets/img/living-water-logo.png",
    "image": [SITE + "/assets/img/og-living-water-pressure-washing.jpg"],
    "description": "Pressure washing, sandblasting, brick cleaning, heritage restoration and disaster restoration for residential, commercial and industrial properties across Toronto and the Greater Toronto Area since 1998.",
    "foundingDate": "1998",
    "email": EMAIL,
    "telephone": PHONE_MAIN[0],
    "contactPoint": [
        {"@type": "ContactPoint", "telephone": PHONE_MAIN[0], "contactType": "customer service", "areaServed": "CA-ON", "availableLanguage": "English"},
        {"@type": "ContactPoint", "telephone": PHONE_TOLL[0], "contactType": "sales", "contactOption": "TollFree", "areaServed": "CA"},
        {"@type": "ContactPoint", "telephone": PHONE_EMERG[0], "contactType": "emergency", "hoursAvailable": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "00:00", "closes": "23:59"}},
    ],
    "address": {"@type": "PostalAddress", "addressLocality": "Toronto", "addressRegion": "ON", "addressCountry": "CA"},
    "areaServed": [{"@type": "City", "name": a} for a in AREAS] + [{"@type": "AdministrativeArea", "name": "Greater Toronto Area"}],
    "knowsAbout": ["Pressure washing", "Soft washing", "Sandblasting", "Dustless blasting", "Soda blasting", "Hydro jetting", "Brick cleaning", "Paint removal", "Efflorescence removal", "Graffiti removal", "Heritage masonry restoration", "Elevator pit cleaning", "Fire damage restoration", "Water damage restoration", "Mould remediation"],
    "hasCredential": [{"@type": "EducationalOccupationalCredential", "name": "ISSA GBAC certification"}, {"@type": "EducationalOccupationalCredential", "name": "WSIB coverage (Ontario)"}],
    "slogan": "Trusted surface restoration, done with integrity.",
    "priceRange": "$$",
    "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Pressure washing and restoration services",
                        "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": SERVICES[s]["nav"], "url": f"{SITE}/{s}/"}} for s in SERVICE_ORDER_CORE + SERVICE_ORDER_SPECIAL]},
}
WEBSITE = {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": NAME, "publisher": {"@id": ORG_ID}, "inLanguage": "en-CA"}

def crumbs_ld(trail):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + p} for i, (n, p) in enumerate(trail)]}

def faq_ld(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

def crumbs_html(trail):
    parts = []
    for i, (n, p) in enumerate(trail):
        parts.append(f'<a href="{p}">{esc(n)}</a>' if i < len(trail) - 1 else f'<span aria-current="page">{esc(n)}</span>')
    return '<nav class="crumbs" aria-label="Breadcrumb">' + ' <span>/</span> '.join(parts) + "</nav>"

# ------------------------------------------------------------ layout
def nav_html(current):
    def a(href, label):
        cur = ' aria-current="page"' if href == current else ""
        return f'<a href="{href}"{cur}>{label}</a>'
    core = "".join(f"<li>{a('/'+s+'/', SERVICES[s]['nav'])}</li>" for s in SERVICE_ORDER_CORE)
    spec = "".join(f"<li>{a('/'+s+'/', SERVICES[s]['nav'])}</li>" for s in SERVICE_ORDER_SPECIAL)
    return f'''<nav class="nav" id="nav" aria-label="Main">
<ul>
<li>{a("/", "Home")}</li>
<li class="has-sub"><button type="button" aria-expanded="false" aria-controls="sub-services">Services ▾</button>
<ul class="sub" id="sub-services"><li>{a("/power-washing-services/", "<strong>All Services</strong>")}</li>{core}<li class="sub-label">Specialised Cleaning</li>{spec}</ul></li>
<li>{a("/service-areas/", "Service Areas")}</li>
<li>{a("/about-us/", "About Us")}</li>
<li>{a("/gallery/", "Gallery")}</li>
<li>{a("/contact/", "Contact")}</li>
</ul></nav>'''

def footer_html():
    core = "".join(f'<li><a href="/{s}/">{SERVICES[s]["nav"]}</a></li>' for s in SERVICE_ORDER_CORE)
    spec = "".join(f'<li><a href="/{s}/">{SERVICES[s]["nav"]}</a></li>' for s in SERVICE_ORDER_SPECIAL)
    return f'''<footer class="site-footer">
<div class="wrap fgrid">
<div>
<img src="/assets/img/living-water-logo-footer.png" width="300" height="70" alt="Living Water Pressure Wash Services logo" loading="lazy">
<p style="margin-top:16px">Trusted surface restoration, done with integrity. Pressure washing, sandblasting and restoration across the Greater Toronto Area since 1998.</p>
<div class="badges"><span>Since 1998</span><span>$5M Insured</span><span>WSIB</span><span>ISSA-GBAC</span><span>4.9★ Google</span></div>
</div>
<div><h3>Services</h3><ul>{core}</ul></div>
<div><h3>Specialised</h3><ul>{spec}<li><a href="/service-areas/">Service Areas</a></li><li><a href="/gallery/">Project Gallery</a></li></ul></div>
<div><h3>Get in Touch</h3><ul class="nap">
<li>Main Office<br><a href="tel:{PHONE_MAIN[0]}">{PHONE_MAIN[1]}</a></li>
<li>Toll Free<br><a href="tel:{PHONE_TOLL[0]}">{PHONE_TOLL[1]}</a></li>
<li>24/7 Emergency Line<br><a href="tel:{PHONE_EMERG[0]}">{PHONE_EMERG[1]}</a></li>
<li>Email<br><a href="mailto:{EMAIL}">{EMAIL}</a></li>
</ul></div>
</div>
<div class="wrap copy"><span>© <span id="year">2026</span> {LEGAL} All rights reserved.</span>
<span><a href="/safety-policy/">Safety Policy</a> · <a href="/privacy-policy/">Privacy Policy</a> · <a href="/sitemap.xml">Sitemap</a></span></div>
</footer>
<a class="btn float-cta" href="/contact/#quote">✉ Get a Free Quote</a>'''

def page(path, title, desc, body, schema=(), og_img="og-living-water-pressure-washing.jpg", preload=None, priority="0.7", noindex=False):
    canonical = SITE + path
    pre = f'<link rel="preload" as="image" href="{best(preload, 960)}" imagesrcset="{srcset(preload)}" imagesizes="100vw" fetchpriority="high">' if preload else ""
    og_url = og_img if og_img.startswith("http") else f"{SITE}/assets/img/{og_img}"
    robots = "noindex, follow" if noindex else "index, follow, max-image-preview:large, max-snippet:-1"
    doc = f'''<!doctype html>
<html lang="en-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="{robots}">
<meta name="geo.region" content="CA-ON"><meta name="geo.placename" content="Toronto">
<meta property="og:type" content="website"><meta property="og:locale" content="en_CA"><meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}"><meta property="og:image" content="{og_url}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(title)}"><meta name="twitter:description" content="{esc(desc)}"><meta name="twitter:image" content="{og_url}">
<meta name="theme-color" content="#0e7b87">
<link rel="icon" href="/favicon.ico" sizes="32x32"><link rel="icon" type="image/png" href="/assets/icons/icon-192.png"><link rel="apple-touch-icon" href="/assets/icons/icon-180.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/assets/fonts/josefin-sans-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/public-sans-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
{pre}
<link rel="stylesheet" href="/assets/css/styles.css">
<link rel="alternate" type="text/plain" title="LLM summary" href="/llms.txt">
{ld(BUSINESS) if path == "/" else ""}{ld(WEBSITE) if path == "/" else ""}{"".join(ld(s) for s in schema)}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="wrap"><span><a href="mailto:{EMAIL}">{EMAIL}</a><span class="hide-sm"> | Serving Toronto &amp; the GTA since 1998</span></span><span>24/7 Emergency: <a href="tel:{PHONE_EMERG[0]}">{PHONE_EMERG[1]}</a></span></div></div>
<header class="site-header"><div class="wrap">
<a class="logo" href="/" aria-label="Living Water Pressure Wash Services home"><img src="/assets/img/living-water-logo.webp" width="880" height="140" alt="Living Water Pressure Wash Services"></a>
<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="nav">Menu ☰</button>
{nav_html(path)}
<a class="btn sm header-cta" href="/contact/#quote">Get a Free Quote</a>
</div></header>
<main id="main">
{body}
</main>
{footer_html()}
<div class="lightbox" role="dialog" aria-modal="true" aria-label="Photo viewer"><button type="button" aria-label="Close">×</button><img alt=""><p></p></div>
<script src="/assets/js/site.js" defer></script>
</body>
</html>'''
    fn = OUT + path + ("index.html" if path.endswith("/") else "")
    os.makedirs(os.path.dirname(fn), exist_ok=True)
    open(fn, "w").write(doc)
    if not noindex:
        PAGES.append((path, priority))

# ------------------------------------------------------------ shared blocks
def service_cards(slugs, tag_attr="short"):
    out = []
    for s in slugs:
        d = SERVICES[s]
        out.append(f'''<article class="card">{img(d["card"], "(max-width: 640px) 100vw, (max-width: 1000px) 50vw, 33vw")}
<div class="body"><span class="tag">{esc(d[tag_attr])}</span><h3><a href="/{s}/">{esc(d["nav"])}</a></h3><p>{esc(d["card_text"])}</p><span class="more">Learn more →</span></div></article>''')
    return '<div class="grid g3">' + "".join(out) + "</div>"

def reviews_block():
    items = "".join(f'<figure class="review"><div class="stars" aria-label="5 out of 5 stars">★★★★★</div><blockquote>“{esc(t)}”</blockquote><figcaption><cite>{esc(n)}</cite><small>Google review</small></figcaption></figure>' for n, t in REVIEWS)
    return f'''<section class="soft"><div class="wrap">
<div class="section-head"><span class="pill light">Verified Feedback</span><h2>What Our Clients Say</h2><p>Rated 4.9 / 5 on Google by homeowners, property management firms, condominium boards and facility managers across the GTA.</p></div>
<div class="reviews">{items}</div>
<p class="center" style="margin-top:30px"><a class="btn line" href="https://www.google.com/search?q=Living+Water+Pressure+Wash+Services+reviews" rel="noopener" target="_blank">Read more reviews on Google</a></p>
</div></section>'''

def areas_block(dark=True):
    lis = "".join(f"<li>{a}</li>" for a in AREAS)
    return f'''<section class="{'dark' if dark else 'soft'}"><div class="wrap center">
<span class="pill">GTA Coverage</span><h2>Serving Toronto &amp; the Greater Toronto Area</h2>
<p style="max-width:720px;margin:0 auto 26px">Our pressure washing fleet is dispatched daily across GTA municipalities, fully equipped with high-volume hot-water systems.</p>
<ul class="areas">{lis}</ul>
<p style="margin-top:24px"><a class="btn ghost" href="/service-areas/">See all service areas</a></p>
</div></section>'''

def faq_block(faqs, title="Frequently Asked Questions"):
    items = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in faqs)
    return f'<section><div class="wrap"><div class="section-head"><span class="pill light">Questions</span><h2>{title}</h2><p>Anything not covered here? Call <a href="tel:{PHONE_MAIN[0]}">{PHONE_MAIN[1]}</a> and ask.</p></div><div class="faq">{items}</div></div></section>'

def cta_block():
    return f'''<section><div class="wrap"><div class="cta-band">
<div><h2>Is your property looking tired?</h2><p>Toronto &amp; GTA · typically booked within 2–5 days. Emergency and disaster restoration answered 24/7 on <a style="color:#fff" href="tel:{PHONE_EMERG[0]}">{PHONE_EMERG[1]}</a>.</p>
<div class="cta-row" style="justify-content:flex-start"><a class="btn" href="/contact/#quote">Request a quote online</a><a class="btn ghost" href="tel:{PHONE_MAIN[0]}">Call {PHONE_MAIN[1]}</a></div></div>
<ul class="ticks"><li>Free no-obligation assessment</li><li>Fixed written quote before any work starts</li><li>Certificate of insurance and WSIB clearance supplied</li><li>Re-clean guarantee</li></ul>
</div></div></section>'''

def process_block():
    steps = "".join(f'<div class="step"><h3>{t}</h3><p>{d}</p></div>' for t, d in PROCESS)
    return f'<section class="soft"><div class="wrap"><div class="section-head"><span class="pill light">How it works</span><h2>Four steps, no surprises on the invoice.</h2></div><div class="steps">{steps}</div></div></section>'

def facts_block():
    return f'''<div class="facts"><h3>Living Water at a glance</h3><dl>
<dt>Business</dt><dd>{LEGAL}</dd>
<dt>Founded</dt><dd>1998 — 28 years in business</dd>
<dt>Projects</dt><dd>7,500+ residential, commercial, industrial and heritage properties</dd>
<dt>Insurance</dt><dd>$5M commercial general liability · WSIB covered · ISSA-GBAC certified</dd>
<dt>Rating</dt><dd>4.9 / 5 on Google</dd>
<dt>Service area</dt><dd>Toronto, the GTA, Hamilton, Niagara, Guelph, Cambridge, Barrie &amp; Simcoe County</dd>
<dt>Phone</dt><dd><a href="tel:{PHONE_MAIN[0]}">{PHONE_MAIN[1]}</a> · 24/7 emergency <a href="tel:{PHONE_EMERG[0]}">{PHONE_EMERG[1]}</a></dd>
</dl></div>'''

def quote_aside():
    return f'''<div class="contact-card"><h3>Get a free quote</h3><p>Fixed written price before any work starts.</p>
<p><a class="btn" style="width:100%;justify-content:center" href="/contact/#quote">Request a quote</a></p>
<ul class="contact-list"><li><b>Main office</b><a href="tel:{PHONE_MAIN[0]}">{PHONE_MAIN[1]}</a></li><li><b>24/7 emergency</b><a href="tel:{PHONE_EMERG[0]}">{PHONE_EMERG[1]}</a></li></ul></div>'''

# ------------------------------------------------------------ HOME
def home():
    stats = f'''<div class="stats">
<div class="stat"><b>28</b><span>years in business</span><p>Washing, blasting and restoring across the GTA since 1998.</p></div>
<div class="stat"><b>7,500+</b><span>properties cleaned</span><p>Residential, commercial, industrial and heritage.</p></div>
<div class="stat"><b>$5M</b><span>liability insured</span><p>Plus full WSIB coverage. COI issued before we start.</p></div>
<div class="stat"><b>4.9★</b><span>rating on Google</span><p>From homeowners and property managers across the GTA.</p></div></div>'''
    work = "".join(ba(b, a, t, " — " + c) for b, a, t, c in GALLERY_PAIRS[:3])
    capabilities = ["Residential, commercial & industrial power washing", "Brick acid wash & paint removal", "Efflorescence removal", "Industrial hydro jetting", "Concrete blasting & rust removal", "Swimming pool prep", "Micro & soda blasting", "Fire damage restoration", "Historical, stone & metal restoration", "Monument cleaning"]
    body = f'''
<section class="hero" aria-labelledby="h1">
<picture>{img("heritage-stone-wall-pressure-washing-toronto", "100vw", eager=True, alt="")}</picture>
<div class="wrap">
<span class="pill">Professional Pressure Washing · Since 1998</span>
<h1 id="h1">Pressure Washing, Restoration &amp; Sandblasting <em>across Toronto &amp; the GTA</em></h1>
<p class="lead">Living Water has cleaned and restored more than 7,500 homes, commercial buildings, industrial sites and heritage landmarks across the Greater Toronto Area since 1998 — $5M insured, WSIB covered and rated 4.9★ on Google.</p>
<div class="cta-row"><a class="btn" href="/contact/#quote">Get Your Free Quote</a><a class="btn ghost" href="tel:{PHONE_MAIN[0]}">Call {PHONE_MAIN[1]}</a></div>
</div></section>

<section><div class="wrap">
<div class="section-head"><span class="pill light">Comprehensive Capabilities</span><h2>Professional Pressure Washing, Restoration &amp; Sandblasting Services</h2>
<p>From residential driveways to heritage facades and industrial hydro jetting — every service has its own method, its own specialists and its own quote.</p></div>
{service_cards(SERVICE_ORDER_CORE[:6])}
<h3 class="center" style="margin:50px 0 24px">Specialised Cleaning Services</h3>
{service_cards(SERVICE_ORDER_SPECIAL[:3])}
<p class="center" style="margin-top:34px"><a class="btn line" href="/power-washing-services/">View all services</a></p>
</div></section>

<section class="soft"><div class="wrap split">
<div><span class="pill light">Why Living Water</span><h2>Twenty-eight years of not ruining anyone's brick.</h2>
<p>Anyone can rent a pressure washer. The difference is knowing when <em>not</em> to use one — soft washing siding, soda blasting heritage masonry, neutralising an acid wash properly. That judgement is what 7,500+ property owners have trusted us with.</p>
<ul class="ticks"><li>28+ years serving commercial, industrial and residential GTA sites</li><li>Fully licensed, with $5M comprehensive general liability</li><li>WSIB covered — protecting building owners from liability</li><li>Certified boom and scissor lift operators</li><li>Satisfaction guaranteed: not thrilled? We re-clean for free</li></ul>
<a class="btn" href="/about-us/">About our team</a></div>
<div>{img("living-water-van-residential-pressure-washing", "(max-width:1000px) 100vw, 45vw")}</div>
</div>
<div class="wrap" style="margin-top:50px">{stats}</div></section>

<section><div class="wrap">
<div class="section-head"><span class="pill light">The Work</span><h2>Quality Work. Proven Results.</h2><p>Drag the slider to compare real Living Water projects, before and after.</p></div>
<div class="grid g3">{work}</div>
<p class="center" style="margin-top:34px"><a class="btn line" href="/gallery/">See the full gallery</a></p>
</div></section>

{process_block()}

<section><div class="wrap split rev">
<div>{img("boom-lift-brick-facade-cleaning", "(max-width:1000px) 100vw, 40vw")}</div>
<div><span class="pill light">Industry Leaders</span><h2>Trusted surface restoration, done with integrity.</h2>
<p>Since 1998 we have been a structural restoration partner to property managers, general contractors, municipalities and heritage conservators. We don't just wash surfaces — we protect the investment behind them.</p>
<ul class="ticks cols">{"".join(f"<li>{c}</li>" for c in capabilities)}</ul>
{facts_block()}</div>
</div></section>

{reviews_block()}
{areas_block()}
{faq_block(GENERAL_FAQ)}
{cta_block()}'''
    page("/", "Pressure Washing & Sandblasting Toronto & GTA | Living Water",
         "Living Water: pressure washing, sandblasting, brick cleaning, heritage and disaster restoration across Toronto & the GTA since 1998. $5M insured, 4.9★ Google. Free quotes.",
         body, schema=[faq_ld(GENERAL_FAQ)], preload="heritage-stone-wall-pressure-washing-toronto", priority="1.0")

# ------------------------------------------------------------ SERVICE PAGES
def service_page(s):
    d = SERVICES[s]
    group = "Specialised Cleaning" if d["group"] == "special" else "Services"
    trail = [("Home", "/"), ("Services", "/power-washing-services/"), (d["nav"], f"/{s}/")]
    photos = "".join(photo(p) for p in d["photos"])
    pool = SERVICE_ORDER_CORE + SERVICE_ORDER_SPECIAL
    related = [x for x in pool if x != s][:]
    # prefer same group first
    related = sorted(related, key=lambda x: SERVICES[x]["group"] != d["group"])[:5]
    rel_html = "".join(f'<a href="/{x}/">{SERVICES[x]["nav"]} →</a>' for x in related)
    body = f'''
<section class="page-hero"><picture>{img(d["hero"], "100vw", eager=True, alt="")}</picture>
<div class="wrap">{crumbs_html(trail)}<span class="pill">{esc(group)}</span><h1>{esc(d["h1"])}</h1><p>{esc(d["sub"])}</p>
<div class="cta-row" style="justify-content:flex-start"><a class="btn" href="/contact/#quote">Get a Free Quote</a><a class="btn ghost" href="tel:{PHONE_MAIN[0]}">Call {PHONE_MAIN[1]}</a></div></div></section>
<section><div class="wrap layout">
<article class="prose"><p class="answer">{esc(d["answer"])}</p>{d["body"]}</article>
<aside class="side">{quote_aside()}<div><h3>Related services</h3><nav class="related" aria-label="Related services">{rel_html}</nav></div></aside>
</div></section>
<section class="soft"><div class="wrap"><div class="section-head"><span class="pill light">Our Work</span><h2>{esc(d["nav"])} Projects</h2><p>Real photos from Living Water jobs across Toronto and the GTA.</p></div>
<div class="grid g3">{photos}</div></div></section>
{process_block() if d["group"]=="core" else ""}
{faq_block(d["faqs"], esc(d["nav"]) + " FAQ")}
{reviews_block()}
{areas_block()}
{cta_block()}'''
    service_ld = {"@context": "https://schema.org", "@type": "Service", "@id": f"{SITE}/{s}/#service",
                  "name": d["nav"], "serviceType": d["service_type"], "description": d["answer"],
                  "url": f"{SITE}/{s}/", "provider": {"@id": ORG_ID}, "image": f"{SITE}{best(d['hero'])}",
                  "areaServed": [{"@type": "City", "name": a} for a in AREAS],
                  "offers": {"@type": "Offer", "priceCurrency": "CAD", "description": "Free assessment and fixed written quote"}}
    page(f"/{s}/", d["title"], d["desc"], body,
         schema=[service_ld, crumbs_ld(trail), faq_ld(d["faqs"])],
         og_img=best(d["hero"]).replace("/assets/img/", "") if False else "og-living-water-pressure-washing.jpg",
         preload=d["hero"], priority="0.9")

# ------------------------------------------------------------ SERVICES HUB
def services_hub():
    trail = [("Home", "/"), ("Services", "/power-washing-services/")]
    deep = [("Dirt & grime removal", "Built-up dirt, dust and weather-related grime."), ("Stain treatment", "Stubborn stains, discolouration and surface marks."),
            ("Algae & mildew cleaning", "Organic growth removed from exterior surfaces."), ("Oil & grease removal", "Heavy grease and oil in high-traffic areas."),
            ("Graffiti & paint removal", "Affected surfaces restored without damage."), ("Seasonal deep cleaning", "A refresh after harsh weather, ready for the season ahead.")]
    deep_html = "".join(f'<div class="step" style="padding-top:22px"><h3>{t}</h3><p>{x}</p></div>' for t, x in deep)
    body = f'''
<section class="page-hero"><picture>{img("rooftop-terrace-pressure-washing-crew", "100vw", eager=True, alt="")}</picture>
<div class="wrap">{crumbs_html(trail)}<span class="pill">Our Professional Services</span><h1>Power Washing Services in Toronto &amp; the GTA</h1>
<p>Where professional cleaning meets proven expertise — power washing, sandblasting and restoration for residential, commercial and industrial properties.</p>
<div class="cta-row" style="justify-content:flex-start"><a class="btn" href="/contact/#quote">Get a Free Quote</a><a class="btn ghost" href="tel:{PHONE_MAIN[0]}">Call {PHONE_MAIN[1]}</a></div></div></section>
<section><div class="wrap split">
<div><span class="pill light">Professional Power</span><h2>Why professional power washing?</h2>
<p class="answer">Professional power washing removes dirt, algae, grease and stains while protecting the surface underneath — because the right equipment, pressure, water temperature and cleaning chemistry differ for every material.</p>
<ul class="ticks"><li>Restores curb appeal and a fresh, clean appearance</li><li>Removes dirt, grime, algae, grease, stains and stubborn build-up</li><li>Helps protect exterior surfaces from premature wear</li><li>Improves safety by removing slippery contaminants</li><li>Uses professional equipment and surface-specific techniques</li><li>Saves time with efficient, consistent, reliable results</li></ul></div>
<div>{img("parking-lot-pressure-washing-crew", "(max-width:1000px) 100vw, 45vw")}</div></div></section>
<section class="soft"><div class="wrap"><div class="section-head"><span class="pill light">Comprehensive Capabilities</span><h2>Pressure Washing, Restoration &amp; Sandblasting</h2></div>{service_cards(SERVICE_ORDER_CORE)}</div></section>
<section><div class="wrap"><div class="section-head"><span class="pill light">Specialised Cleaning</span><h2>Specialised Cleaning Services</h2><p>The right technique for each surface — elevator pits, efflorescence, graffiti, stone and metal.</p></div>{service_cards(SERVICE_ORDER_SPECIAL)}</div></section>
<section class="soft"><div class="wrap"><div class="section-head"><span class="pill light">Deep Surface Cleaning</span><h2>From routine cleaning to tough restoration</h2></div><div class="grid g3">{deep_html}</div></div></section>
{areas_block()}
{faq_block(GENERAL_FAQ)}
{cta_block()}'''
    items = {"@context": "https://schema.org", "@type": "ItemList", "name": "Living Water services",
             "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{SITE}/{s}/", "name": SERVICES[s]["nav"]} for i, s in enumerate(SERVICE_ORDER_CORE + SERVICE_ORDER_SPECIAL)]}
    page("/power-washing-services/", "Power Washing Services Toronto & GTA | Living Water",
         "Residential, commercial and industrial power washing, sandblasting, brick cleaning, graffiti, efflorescence, elevator pit and restoration services across Toronto & the GTA.",
         body, schema=[items, crumbs_ld(trail), faq_ld(GENERAL_FAQ)], preload="rooftop-terrace-pressure-washing-crew", priority="0.9")

# ------------------------------------------------------------ ABOUT
def about():
    trail = [("Home", "/"), ("About Us", "/about-us/")]
    body = f'''
<section class="page-hero"><picture>{img("century-home-pressure-washing", "100vw", eager=True, alt="")}</picture>
<div class="wrap">{crumbs_html(trail)}<span class="pill">Who we are</span><h1>About Living Water Pressure Wash Services</h1><p>Meticulous care for every surface — professional pressure washing and sandblasting in Toronto and the GTA since 1998.</p></div></section>
<section><div class="wrap split">
<div><p class="answer">{LEGAL} is a Toronto-area pressure washing, sandblasting and surface restoration company founded in 1998. It has cleaned 7,500+ residential, commercial, industrial and heritage properties, and is $5M insured, WSIB covered and ISSA-GBAC certified.</p>
<p>When your property needs expert care, you want a team that shows up prepared and delivers results that last. That is what Living Water has done for more than 28 years. From residential driveways to heritage building facades, we bring the same precision and professionalism to every job.</p>
<p>Our clients — homeowners, business owners, property managers and heritage conservators — trust us with their most valuable assets, and we take that responsibility seriously.</p>
<h2>What sets us apart</h2>
<ul class="ticks"><li><strong>Honesty</strong> in everything we say and quote</li><li><strong>Expert technique</strong> with top-quality equipment matched to each surface</li><li><strong>Environmentally responsible</strong> methods that protect the spaces around your property</li><li><strong>Long-term relationships</strong> — many clients have been with us for decades</li></ul></div>
<div>{img("estate-home-exterior-restoration", "(max-width:1000px) 100vw, 45vw")}<div style="margin-top:24px">{facts_block()}</div></div>
</div></section>
<section class="soft"><div class="wrap split rev">
<div>{img("rooftop-terrace-pressure-washing-crew", "(max-width:1000px) 100vw, 45vw")}</div>
<div><span class="pill light">Services we provide</span><h2>Premium exterior restoration for Greater Toronto's properties</h2><p>We don't just clean surfaces — we reveal the beauty beneath the weathering.</p>
<ul class="ticks cols"><li>Residential, commercial &amp; industrial pressure washing</li><li>Sandblasting</li><li>Driveway &amp; concrete cleaning</li><li>House &amp; exterior washing</li><li>Brick restoration</li><li>Stain, rust, graffiti, paint &amp; gum removal</li><li>Elevator pit cleaning</li><li>Historical building remediation</li><li>Deck and fence cleaning</li><li>Fire, water &amp; wind damage recovery</li></ul>
<div class="stats" style="grid-template-columns:1fr 1fr;margin-top:20px"><div class="stat"><b>24/7</b><span>emergency service</span></div><div class="stat"><b>2–5</b><span>days to book residential</span></div></div></div>
</div></section>
{reviews_block()}
{faq_block(GENERAL_FAQ, "Questions before you book")}
{cta_block()}'''
    about_ld = {"@context": "https://schema.org", "@type": "AboutPage", "url": SITE + "/about-us/", "name": "About Living Water Pressure Wash Services", "mainEntity": {"@id": ORG_ID}}
    page("/about-us/", "About Living Water | GTA Pressure Washing Since 1998",
         "Living Water Pressure Wash Services Ltd. has cleaned and restored 7,500+ GTA properties since 1998. $5M insured, WSIB covered, ISSA-GBAC certified, 4.9★ on Google.",
         body, schema=[about_ld, crumbs_ld(trail), faq_ld(GENERAL_FAQ)], preload="century-home-pressure-washing", priority="0.8")

# ------------------------------------------------------------ GALLERY
def gallery():
    trail = [("Home", "/"), ("Gallery", "/gallery/")]
    pairs = "".join(ba(b, a, t, " — " + c) for b, a, t, c in GALLERY_PAIRS)
    used_pairs = {x for p in GALLERY_PAIRS for x in p[:2]}
    singles = [k for k in M if k not in used_pairs]
    grid = "".join(f'<figure>{img(k, "(max-width:640px) 100vw, 33vw").replace("<img ", f"<img data-full={chr(34)}{best(k)}{chr(34)} ", 1)}<figcaption>{esc(M[k]["alt"])}</figcaption></figure>' for k in singles)
    body = f'''
<section class="page-hero"><picture>{img("yellow-brick-heritage-building-cleaning", "100vw", eager=True, alt="")}</picture>
<div class="wrap">{crumbs_html(trail)}<span class="pill">Project Gallery</span><h1>Pressure Washing &amp; Restoration Gallery</h1><p>Real before-and-after photos from Living Water projects across Toronto and the GTA — homes, commercial buildings, industrial sites and heritage landmarks.</p></div></section>
<section><div class="wrap"><div class="section-head"><span class="pill light">Before &amp; After</span><h2>Drag to compare</h2></div><div class="grid g3">{pairs}</div></div></section>
<section class="soft"><div class="wrap"><div class="section-head"><span class="pill light">On the job</span><h2>Our crews at work</h2><p>Click any photo to enlarge.</p></div><div class="masonry">{grid}</div></div></section>
{cta_block()}'''
    gal_ld = {"@context": "https://schema.org", "@type": "ImageGallery", "name": "Living Water project gallery", "url": SITE + "/gallery/",
              "associatedMedia": [{"@type": "ImageObject", "contentUrl": SITE + best(k), "caption": M[k]["alt"]} for k in M]}
    page("/gallery/", "Before & After Gallery | Pressure Washing Toronto | Living Water",
         "Before and after photos of Living Water pressure washing, brick cleaning, paint removal, efflorescence and heritage restoration projects across Toronto and the GTA.",
         body, schema=[gal_ld, crumbs_ld(trail)], preload="yellow-brick-heritage-building-cleaning", priority="0.7")

# ------------------------------------------------------------ SERVICE AREAS
def service_areas():
    trail = [("Home", "/"), ("Service Areas", "/service-areas/")]
    blocks = ""
    for region, towns in REGIONS.items():
        rid = region.lower().replace(" & ", "-").replace(", ", "-").replace(" ", "-")
        lis = "".join(f'<li id="{t.lower().replace(" ", "-").replace(".", "")}">{t}</li>' for t in towns)
        blocks += f'<div class="card" style="padding:26px"><h2 style="font-size:1.4rem" id="{rid}">{region}</h2><p>Pressure washing, sandblasting, brick cleaning and restoration in {", ".join(towns[:-1]) + " and " + towns[-1] if len(towns) > 1 else towns[0]}.</p><ul class="areas" style="justify-content:flex-start">{lis}</ul></div>'
    links = "".join(f'<li><a href="/{s}/">{SERVICES[s]["nav"]}</a></li>' for s in SERVICE_ORDER_CORE + SERVICE_ORDER_SPECIAL)
    faqs = [("Do you serve my city?", "Living Water serves the City of Toronto (including North York, Scarborough, Etobicoke and East York), Peel and Halton (Mississauga, Brampton, Oakville, Burlington, Milton), York Region (Vaughan, Woodbridge, Maple, Kleinburg, Richmond Hill, Markham, King City, Aurora, Newmarket, Georgina), Durham Region (Pickering, Ajax, Whitby, Oshawa), Hamilton, Niagara, Guelph, Cambridge, Barrie and Simcoe County."),
            ("Do you charge extra for travel outside Toronto?", "Your quote is a fixed written price that already accounts for location. Call us for projects outside the listed areas — larger commercial and heritage projects across Ontario are considered."),
            ("How quickly can you get to my property?", "Residential work is usually booked within 2–5 days across the GTA. Emergency and disaster restoration is answered 24/7 on (647) 833-4343.")]
    body = f'''
<section class="page-hero"><picture>{img("brick-storefront-boom-lift-washing", "100vw", eager=True, alt="")}</picture>
<div class="wrap">{crumbs_html(trail)}<span class="pill">GTA Coverage</span><h1>Pressure Washing Service Areas — Toronto &amp; the GTA</h1><p>Our crews and hot-water pressure washing units are dispatched daily across Toronto, Peel, Halton, York and Durham regions, plus Hamilton, Niagara, Waterloo-Wellington and Simcoe County.</p></div></section>
<section><div class="wrap">
<p class="answer">Living Water Pressure Wash Services serves 30+ communities across the Greater Toronto Area and southern Ontario, from Oshawa to Hamilton and north to Barrie, offering every service — residential, commercial and industrial pressure washing, sandblasting, brick and heritage restoration and 24/7 disaster restoration — in each one.</p>
<div class="grid g2">{blocks}</div></div></section>
<section class="soft"><div class="wrap split"><div><h2>Every service, in every community</h2><ul class="ticks cols">{links}</ul></div><div>{facts_block()}</div></div></section>
{faq_block(faqs, "Service area FAQ")}
{cta_block()}'''
    page("/service-areas/", "Service Areas | Pressure Washing Toronto, Mississauga, Vaughan & GTA",
         "Living Water provides pressure washing, sandblasting and restoration in Toronto, Mississauga, Brampton, Vaughan, Markham, Richmond Hill, Oakville, Oshawa, Hamilton, Barrie and more.",
         body, schema=[crumbs_ld(trail), faq_ld(faqs)], preload="brick-storefront-boom-lift-washing", priority="0.8")

# ------------------------------------------------------------ CONTACT
def contact():
    trail = [("Home", "/"), ("Contact", "/contact/")]
    opts = ["Residential Power Wash", "Commercial Power Wash", "Industrial Power Wash", "Sandblasting", "Brick Cleaning & Paint Removal", "Historical Remediation", "Disaster Restoration", "Elevator Pit Cleaning", "Efflorescence Removal", "Graffiti Removal", "Stone Restoration", "Metal Restoration", "Other"]
    opt_html = "".join(f"<option>{esc(o)}</option>" for o in opts)
    body = f'''
<section class="page-hero"><picture>{img("custom-home-exterior-washing", "100vw", eager=True, alt="")}</picture>
<div class="wrap">{crumbs_html(trail)}<span class="pill">Contact Us</span><h1>Get a Free Pressure Washing Quote</h1><p>Tell us about your project and we'll come back with a fixed written quote. We'd love to hear from you.</p></div></section>
<section><div class="wrap split" style="align-items:start">
<div class="contact-card" id="quote">
<h2>Request a free quote</h2><p>Takes two minutes. We reply within one business day.</p>
<form action="https://formsubmit.co/{EMAIL}" method="POST">
<input type="hidden" name="_subject" value="New quote request — livingwater-pws.com">
<input type="hidden" name="_next" value="{SITE}/thank-you/">
<input type="hidden" name="_template" value="table">
<input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
<div class="row"><div class="field"><label for="fn">First name *</label><input id="fn" name="first_name" autocomplete="given-name" required></div>
<div class="field"><label for="ln">Last name *</label><input id="ln" name="last_name" autocomplete="family-name" required></div></div>
<div class="row"><div class="field"><label for="em">Email *</label><input id="em" type="email" name="email" autocomplete="email" required></div>
<div class="field"><label for="ph">Phone *</label><input id="ph" type="tel" name="phone" autocomplete="tel" required></div></div>
<div class="row"><div class="field"><label for="sv">Service *</label><select id="sv" name="service" required><option value="">Choose a service…</option>{opt_html}</select></div>
<div class="field"><label for="pc">Postal code / city</label><input id="pc" name="location" autocomplete="postal-code"></div></div>
<div class="field"><label for="msg">Tell us about the surface and project</label><textarea id="msg" name="message" rows="5"></textarea></div>
<button class="btn" type="submit">Send my quote request</button>
<p style="font-size:.85rem;margin-top:12px">We never share or sell your information. See our <a href="/privacy-policy/">privacy policy</a>.</p>
</form></div>
<div><h2>Call or email</h2>
<ul class="contact-list">
<li><b>Main office</b><a href="tel:{PHONE_MAIN[0]}">{PHONE_MAIN[1]}</a></li>
<li><b>Toll free</b><a href="tel:{PHONE_TOLL[0]}">{PHONE_TOLL[1]}</a></li>
<li><b>24/7 emergency line</b><a href="tel:{PHONE_EMERG[0]}">{PHONE_EMERG[1]}</a></li>
<li><b>Email</b><a href="mailto:{EMAIL}">{EMAIL}</a></li>
<li><b>Service area</b>Toronto &amp; the Greater Toronto Area — <a href="/service-areas/">see all areas</a></li>
</ul>
<div style="margin-top:26px">{img("living-water-van-residential-pressure-washing", "(max-width:1000px) 100vw, 45vw")}</div>
</div></div></section>
{reviews_block()}
{areas_block()}'''
    cp = {"@context": "https://schema.org", "@type": "ContactPage", "url": SITE + "/contact/", "name": "Contact Living Water", "mainEntity": {"@id": ORG_ID}}
    page("/contact/", "Contact Living Water | Free Pressure Washing Quote Toronto",
         "Request a free pressure washing, sandblasting or restoration quote. Call (416) 663-8000, toll free 1-833-456-2978, or 24/7 emergency (647) 833-4343.",
         body, schema=[cp, crumbs_ld(trail)], preload="custom-home-exterior-washing", priority="0.8")

# ------------------------------------------------------------ simple pages
def simple(path, title, desc, h1, html_body, trail_name, noindex=False, priority="0.3"):
    trail = [("Home", "/"), (trail_name, path)]
    body = f'''<section class="page-hero"><div class="wrap">{crumbs_html(trail)}<h1>{h1}</h1></div></section>
<section><div class="wrap prose" style="max-width:860px">{html_body}</div></section>{cta_block()}'''
    page(path, title, desc, body, schema=[crumbs_ld(trail)], noindex=noindex, priority=priority)

def legal():
    simple("/safety-policy/", "Health & Safety Policy | Living Water Pressure Wash Services",
           "Living Water's health and safety commitment to employees, clients and the public on every job.",
           "Health &amp; Safety Policy", f'''
<p class="answer">Living Water is committed to protecting our employees, clients and the public on every job we undertake. Safety is planned into every quote, not added afterwards.</p>
<ul class="ticks"><li>Full WSIB coverage and $5M commercial general liability insurance</li><li>Certificate of Insurance and WSIB clearance supplied before work starts</li><li>Certified boom and scissor lift operators</li><li>Site-specific hazard assessment, containment and protection of people, plants and property</li><li>Proper handling and disposal of chemicals, oil and hazardous waste</li><li>ISSA-GBAC certified cleaning and disinfection practices</li></ul>
<p>The policy applies to all employees, subcontractors and on-site personnel across all service divisions. To request the full Health &amp; Safety Policy document, email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>''', "Safety Policy")
    simple("/privacy-policy/", "Privacy Policy | Living Water Pressure Wash Services",
           "How Living Water Pressure Wash Services collects, uses and protects your personal information.",
           "Privacy Policy", f'''
<h2>Who we are</h2><p>This website, {SITE}/, is operated by {LEGAL}</p>
<h2>Information we collect</h2><p>When you request a quote we collect the details you provide — name, email, phone number, location and project information — so we can respond. Our web host may log standard technical data such as IP address and browser type for security.</p>
<h2>Confidentiality and use</h2><p>We keep your personal information confidential. We do not send unsolicited emails or sell your contact information. Information is used only to respond to you and provide our services.</p>
<h2>Form processing</h2><p>Quote requests are delivered to our inbox by a third-party form service, which processes the data only to deliver it to us.</p>
<h2>Cookies</h2><p>This site does not use advertising or tracking cookies.</p>
<h2>Your rights</h2><p>You may ask for a copy of the personal information we hold about you, or ask us to delete it, subject to legal record-keeping obligations.</p>
<h2>Contact us</h2><p>Questions about this policy: <a href="mailto:{EMAIL}">{EMAIL}</a> or <a href="tel:{PHONE_MAIN[0]}">{PHONE_MAIN[1]}</a>.</p>''', "Privacy Policy")
    simple("/thank-you/", "Thank You | Living Water", "Thanks for your quote request.", "Thank you — we've got your request",
           f'<p class="answer">We will reply within one business day with next steps or a quote. For anything urgent call <a href="tel:{PHONE_MAIN[0]}">{PHONE_MAIN[1]}</a>, or our 24/7 emergency line <a href="tel:{PHONE_EMERG[0]}">{PHONE_EMERG[1]}</a>.</p><p><a class="btn" href="/">Back to home</a></p>',
           "Thank You", noindex=True)
    # 404
    trail = [("Home", "/"), ("Page not found", "/404.html")]
    body = f'''<section class="page-hero"><div class="wrap"><h1>Page not found</h1><p>The page you were looking for has moved. Try one of these:</p></div></section>
<section><div class="wrap">{service_cards(SERVICE_ORDER_CORE[:3])}</div></section>'''
    page("/404.html", "Page Not Found | Living Water", "Page not found.", body, noindex=True)

# ------------------------------------------------------------ technical SEO / GEO files
def tech():
    urls = "".join(f"<url><loc>{SITE}{p}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>\n" for p, pr in PAGES)
    open(OUT + "/sitemap.xml", "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    open(OUT + "/robots.txt", "w").write(f"""# Living Water Pressure Wash Services
User-agent: *
Allow: /
Disallow: /thank-you/

# AI / answer-engine crawlers are welcome (GEO)
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: Applebot-Extended
Allow: /
User-agent: Bingbot
Allow: /

Sitemap: {SITE}/sitemap.xml
""")
    svc_lines = "\n".join(f"- [{SERVICES[s]['nav']}]({SITE}/{s}/): {SERVICES[s]['answer']}" for s in SERVICE_ORDER_CORE + SERVICE_ORDER_SPECIAL)
    faq_lines = "\n".join(f"**{q}**\n{a}\n" for q, a in GENERAL_FAQ)
    open(OUT + "/llms.txt", "w").write(f"""# {NAME}

> {LEGAL} is a pressure washing, sandblasting and surface restoration company serving Toronto and the Greater Toronto Area (Ontario, Canada) since 1998. It cleans and restores residential, commercial, industrial and heritage properties, has completed 7,500+ projects, carries $5M commercial general liability insurance, is WSIB covered and ISSA-GBAC certified, and is rated 4.9/5 on Google.

## Key facts
- Founded: 1998 (28 years in business)
- Headquarters / service base: Toronto, Ontario, Canada
- Phone (main office): {PHONE_MAIN[1]}
- Toll free: {PHONE_TOLL[1]}
- 24/7 emergency line: {PHONE_EMERG[1]}
- Email: {EMAIL}
- Website: {SITE}/
- Booking: residential jobs typically within 2–5 days; free assessment and fixed written quote; re-clean guarantee
- Service area: {", ".join(AREAS)}

## Services
{svc_lines}

## Key pages
- [Home]({SITE}/)
- [All services]({SITE}/power-washing-services/)
- [Service areas]({SITE}/service-areas/)
- [About]({SITE}/about-us/)
- [Gallery of before & after projects]({SITE}/gallery/)
- [Contact / free quote]({SITE}/contact/)

## FAQ
{faq_lines}""")
    open(OUT + "/site.webmanifest", "w").write(json.dumps({"name": NAME, "short_name": "Living Water", "start_url": "/", "display": "standalone", "background_color": "#ffffff", "theme_color": "#0e7b87",
        "icons": [{"src": "/assets/icons/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/assets/icons/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=1))
    open(OUT + "/humans.txt", "w").write(f"/* TEAM */\nCompany: {LEGAL}\nContact: {EMAIL}\nLocation: Toronto, Ontario, Canada\n")

home(); services_hub()
for s in SERVICES: service_page(s)
about(); gallery(); service_areas(); contact(); legal(); tech()
print(len(PAGES), "indexable pages")
