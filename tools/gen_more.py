# Pass 3: trust strip, anchors/TOC, facts table, reviews/FAQ/industries pages. Executed in gen.py namespace.
import re as _re

TRUST = """<div class="trust"><div class="wrap"><ul>
<li><span class="ti"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></span><span class="tt"><b>Since 1998</b><small>28 years in business</small></span></li>
<li><span class="ti"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/></svg></span><span class="tt"><b>7,500+</b><small>properties cleaned</small></span></li>
<li><span class="ti"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/></svg></span><span class="tt"><b>$5M</b><small>liability insured</small></span></li>
<li><span class="ti"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="9"/></svg></span><span class="tt"><b>WSIB</b><small>covered &amp; ISSA-GBAC</small></span></li>
<li><span class="ti"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/></svg></span><span class="tt"><b>4.9 / 5</b><small>rated on Google</small></span></li>
</ul></div></div>"""


def _slug(t):
    t = _re.sub(r"<[^>]+>", "", html.unescape(t)).lower()
    return _re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:60]


def add_h2_ids(body):
    seen = set()

    def rep(m):
        attrs, inner = m.group(1), m.group(2)
        if "id=" in attrs:
            return m.group(0)
        sid = _slug(inner) or "section"
        while sid in seen:
            sid += "-2"
        seen.add(sid)
        return f'<h2{attrs} id="{sid}">{inner}</h2>'
    return _re.sub(r"<h2([^>]*)>(.*?)</h2>", rep, body)


def toc(body):
    heads = _re.findall(r"<h2[^>]*>(.*?)</h2>", body)
    if len(heads) < 3:
        return ""
    items = "".join(f'<li><a href="#{_slug(h)}">{_re.sub("<[^>]+>", "", h)}</a></li>' for h in heads)
    return f'<nav class="toc" aria-label="On this page"><strong>On this page</strong><ol>{items}</ol></nav>'


def facts_table(slug):
    if slug not in SERVICE_FACTS:
        return ""
    best_for, methods, clients, avail = SERVICE_FACTS[slug]
    return f"""<div class="glance"><h2 class="sr-only">At a glance</h2><dl>
<div><dt>Best for</dt><dd>{esc(best_for)}</dd></div>
<div><dt>Methods</dt><dd>{esc(methods)}</dd></div>
<div><dt>Who we serve</dt><dd>{esc(clients)}</dd></div>
<div><dt>Availability</dt><dd>{esc(avail)}</dd></div>
<div><dt>Coverage</dt><dd>Toronto &amp; the GTA, Hamilton, Niagara, Barrie</dd></div>
<div><dt>Quote</dt><dd>Free assessment, fixed written price</dd></div>
</dl></div>"""


def reviews_page():
    path = "/reviews/"
    trail = [("Home", "/"), ("Reviews", path)]
    items = "".join(f'<figure class="review"><div class="stars" aria-label="5 out of 5 stars">★★★★★</div><blockquote>“{esc(t)}”</blockquote><figcaption><cite>{esc(n)}</cite><small>Google review</small></figcaption></figure>' for n, t in REVIEWS_FULL)
    body = f"""
<section class="page-hero"><picture>{hero_img("stone-patio-cleaning-after", "100vw", eager=True, alt="")}</picture>
<div class="wrap">{crumbs_html(trail)}<span class="pill">Verified Feedback</span><h1>Living Water Reviews</h1><p>Rated 4.9 out of 5 on Google by homeowners, property managers and businesses across Toronto and the GTA.</p></div></section>
<section><div class="wrap">
<p class="answer">Living Water Pressure Wash Services is rated 4.9 / 5 on Google. Customers most often mention meticulous work, professionalism, fair pricing and results that make old patios, driveways and stone look new again.</p>
<div class="reviews">{items}</div>
<p class="center" style="margin-top:30px"><a class="btn line" href="https://www.google.com/search?q=Living+Water+Pressure+Wash+Services+reviews" rel="noopener" target="_blank">See all reviews on Google</a></p>
</div></section>
<section class="soft"><div class="wrap"><div class="section-head"><h2>See the results for yourself</h2></div><div class="grid g3">{"".join(ba(b, a, t, " — " + c) for b, a, t, c in GALLERY_PAIRS[:3])}</div></div></section>
{cta_block()}"""
    page(path, "Living Water Reviews | 4.9★ Pressure Washing GTA",
         "Read Google reviews of Living Water Pressure Wash Services — rated 4.9/5 by GTA homeowners, property managers and businesses since 1998.",
         body, schema=[crumbs_ld(trail)], preload="stone-patio-cleaning-after", priority="0.7", crumbs=True)


def faq_page():
    path = "/faq/"
    trail = [("Home", "/"), ("FAQ", path)]
    groups = [("General", GENERAL_FAQ)]
    for s in SERVICE_ORDER_CORE + SERVICE_ORDER_SPECIAL:
        groups.append((SERVICES[s]["nav"], SERVICES[s]["faqs"]))
    allq = []
    sections = ""
    for name, faqs in groups:
        allq += faqs
        items = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in faqs)
        sections += f'<h2>{esc(name)}</h2><div class="faq">{items}</div>'
    jump = "".join(f'<li><a href="#{_slug(n)}">{esc(n)}</a></li>' for n, _ in groups)
    body = f"""
<section class="page-hero"><div class="wrap">{crumbs_html(trail)}<span class="pill">Questions</span><h1>Pressure Washing &amp; Restoration FAQ</h1><p>Answers to the questions GTA homeowners, property managers and contractors ask us most.</p></div></section>
<section><div class="wrap layout"><article class="prose faq-page">{sections}</article>
<aside class="side"><nav class="toc" aria-label="FAQ topics"><strong>Topics</strong><ol>{jump}</ol></nav>{quote_aside()}</aside></div></section>
{cta_block()}"""
    page(path, "Pressure Washing FAQ | Living Water Toronto",
         f"{len(allq)} answers about pressure washing, soft washing, sandblasting, brick cleaning, efflorescence, graffiti, elevator pits and restoration in the GTA.",
         body, schema=[crumbs_ld(trail), faq_ld(allq)], priority="0.7", crumbs=True, page_type="FAQPage" if False else "WebPage")


def industries_page():
    path = "/industries/"
    trail = [("Home", "/"), ("Industries", path)]
    cards = ""
    for name, text, svcs, im in INDUSTRIES:
        links = " · ".join(f'<a href="/{x}/">{SERVICES[x]["nav"]}</a>' for x in svcs)
        cards += f'<article class="card ind">{img(im, "(max-width: 640px) 100vw, 33vw")}<div class="body"><h2 style="font-size:1.3rem">{esc(name)}</h2><p>{esc(text)}</p><p class="svc-links">{links}</p></div></article>'
    body = f"""
<section class="page-hero"><picture>{hero_img("boom-lift-brick-facade-cleaning", "100vw", eager=True, alt="")}</picture>
<div class="wrap">{crumbs_html(trail)}<span class="pill">Who we serve</span><h1>Industries We Serve</h1><p>From homeowners to elevator companies, municipalities and heritage conservators — one insured, WSIB-covered team for every surface.</p></div></section>
<section><div class="wrap">
<p class="answer">Living Water works for homeowners, property managers and condominium boards, commercial and retail owners, industrial plants, general contractors and builders, elevator service companies, stone and paver manufacturers, municipalities and heritage conservators across Toronto and the GTA.</p>
<div class="grid g3">{cards}</div></div></section>
<section class="soft"><div class="wrap split"><div><h2>Paperwork handled</h2><ul class="ticks"><li>Certificate of Insurance ($5M CGL) issued before work starts</li><li>WSIB clearance certificate</li><li>Written method statement, scope and fixed price</li><li>Before and after photos for your records</li><li>Certified boom and scissor lift operators</li></ul></div><div>{facts_block()}</div></div></section>
{cta_block()}"""
    page(path, "Industries We Serve | Commercial & Industrial Cleaning GTA",
         "Pressure washing and restoration for property managers, condo boards, industrial plants, contractors, elevator companies, municipalities and homeowners.",
         body, schema=[crumbs_ld(trail)], preload="boom-lift-brick-facade-cleaning", priority="0.7", crumbs=True)
