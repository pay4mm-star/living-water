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
<div class="wrap">{crumbs_html(trail)}<span class="pill">Verified Feedback</span><h1>Living Water Reviews</h1><p>Rated 4.9 out of 5 across {GBP_COUNT} Google reviews by homeowners, property managers and businesses across Toronto and the GTA.</p></div></section>
<section><div class="wrap">
<p class="answer">Living Water Pressure Wash Services is rated 4.9 / 5 on Google. Customers most often mention meticulous work, professionalism, fair pricing and results that make old patios, driveways and stone look new again.</p>
<div class="reviews">{items}</div>
<p class="center" style="margin-top:30px"><a class="btn line" href="{GBP_MAPS}" rel="noopener" target="_blank">Read all {GBP_COUNT} reviews on Google</a> <a class="btn" href="{GBP_REVIEW}" rel="noopener" target="_blank">★ Leave us a review</a></p>
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
    for s in SERVICE_ORDER_CORE + SERVICE_ORDER_SPECIAL + SERVICE_ORDER_SUB:
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


def seasonal_bar(path):
    if not SEASONAL.get("on") or path == SEASONAL["link"]:
        return ""
    return f'<a class="season" href="{SEASONAL["link"]}"><span class="s-long">{esc(SEASONAL["text"])}</span><span class="s-short">{esc(SEASONAL.get("short", SEASONAL["text"]))}</span><b>{esc(SEASONAL["cta"])} →</b></a>'


def winter_feature():
    if not SEASONAL.get("on"):
        return ""
    return f"""<section class="winter"><div class="wrap split">
<div><span class="pill">Winter service · Condos &amp; commercial buildings</span>
<h2>Elevator pit cleaning for condo &amp; property managers</h2>
<p>Salt slush, meltwater and debris end up in elevator pits all winter. We pump, clean and sanitize pits after hours, coordinate with your elevator contractor, and send a before-and-after photo report — with COI and WSIB clearance included.</p>
<ul class="ticks"><li>After-hours scheduling, minimal downtime</li><li>Water, oil, sludge and sewage clean-up</li><li>Seasonal programs for multi-building portfolios</li><li>24/7 emergency line: {PHONE_EMERG[1]}</li></ul>
<div class="cta-row" style="justify-content:flex-start"><a class="btn" href="/elevator-pit-cleaning/#pm-quote">Get an elevator pit quote</a><a class="btn line" href="/guides/winter-elevator-pit-checklist/">Winter pit checklist</a></div></div>
<div>{img("elevator-pit-cleaning-toronto", "(max-width:1000px) 100vw, 45vw")}</div>
</div></section>"""


def pm_form_block(slug):
    emergency = slug == "elevator-pit-water-removal"
    return f"""<section class="soft" id="pm-quote"><div class="wrap split" style="align-items:start">
<div><span class="pill light">For condo &amp; property managers</span>
<h2>{"Emergency pump-out request" if emergency else "Request an elevator pit quote"}</h2>
<p>{"For active flooding call <a href='tel:" + PHONE_EMERG[0] + "'>" + PHONE_EMERG[1] + "</a> now — then send details here." if emergency else "Tell us about your building and we'll send a fixed written quote with our COI and WSIB clearance, usually within one business day."}</p>
<ul class="ticks"><li>Fixed price per pit, or a portfolio program</li><li>After-hours scheduling with your elevator contractor</li><li>Before-and-after photo report for the board</li></ul>
{facts_block()}</div>
<div class="contact-card">
<form action="https://api.web3forms.com/submit" method="POST">
<input type="hidden" name="access_key" value="{W3F_KEY}"><input type="hidden" name="from_name" value="Living Water website">
<input type="hidden" name="subject" value="{"EMERGENCY elevator pit" if emergency else "Elevator pit quote"} — livingwater-pws.com">
<input type="hidden" name="redirect" value="{SITE}/thank-you/">
<input type="hidden" name="service" value="{"Elevator Pit Water Removal" if emergency else "Elevator Pit Cleaning"}">
<input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true" style="display:none">
<div class="row"><div class="field"><label for="pm-n">Name *</label><input id="pm-n" name="name" autocomplete="name" required></div>
<div class="field"><label for="pm-r">Role</label><select id="pm-r" name="role"><option>Property manager</option><option>Condo board member</option><option>Building superintendent</option><option>Elevator contractor</option><option>Owner</option><option>Other</option></select></div></div>
<div class="row"><div class="field"><label for="pm-e">Email *</label><input id="pm-e" type="email" name="email" autocomplete="email" required></div>
<div class="field"><label for="pm-p">Phone *</label><input id="pm-p" type="tel" name="phone" autocomplete="tel" required></div></div>
<div class="row"><div class="field"><label for="pm-b">Building / company</label><input id="pm-b" name="building" autocomplete="organization"></div>
<div class="field"><label for="pm-a">Address or postal code *</label><input id="pm-a" name="address" required></div></div>
<div class="row"><div class="field"><label for="pm-c">Number of elevators</label><input id="pm-c" type="number" min="1" name="elevators" inputmode="numeric"></div>
<div class="field"><label for="pm-i">Pit condition</label><select id="pm-i" name="condition"><option>Routine cleaning</option><option>Standing water</option><option>Oil / hydraulic fluid</option><option>Sewage backup</option><option>Debris / garbage</option><option>Not sure</option></select></div></div>
<div class="field"><label for="pm-t">Preferred timing</label><select id="pm-t" name="timing"><option>After hours / overnight</option><option>Weekday daytime</option><option>Weekend</option><option>As soon as possible</option></select></div>
<div class="field"><label for="pm-m">Notes</label><textarea id="pm-m" name="message" rows="3"></textarea></div>
<button class="btn" type="submit">{"Send emergency request" if emergency else "Get my elevator pit quote"}</button>
</form></div></div></section>"""


def glossary_page():
    from content_more import GLOSSARY
    path = "/glossary/"
    trail = [("Home", "/"), ("Glossary", path)]
    items = "".join(f'<div class="term" id="{_slug(t)}"><dt>{esc(t)}</dt><dd>{esc(d)} <a href="{u}">Learn more →</a></dd></div>' for t, d, u in GLOSSARY)
    letters = "".join(f'<a href="#{_slug(t)}">{esc(t)}</a>' for t, _, _ in GLOSSARY)
    body = f"""
<section class="page-hero"><div class="wrap">{crumbs_html(trail)}<span class="pill">Reference</span><h1>Pressure Washing &amp; Restoration Glossary</h1><p>Plain-English definitions of the terms used in pressure washing, blasting, masonry restoration and elevator pit cleaning.</p></div></section>
<section><div class="wrap layout"><article class="prose"><dl class="glossary">{items}</dl></article>
<aside class="side"><nav class="toc glossary-jump" aria-label="Terms"><strong>Terms</strong>{letters}</nav>{quote_aside()}</aside></div></section>
{cta_block()}"""
    terms = {"@context": "https://schema.org", "@type": "DefinedTermSet", "@id": SITE + path + "#terms", "name": "Pressure washing and restoration glossary",
             "hasDefinedTerm": [{"@type": "DefinedTerm", "name": t, "description": d, "url": SITE + path + "#" + _slug(t)} for t, d, _ in GLOSSARY]}
    page(path, "Pressure Washing & Restoration Glossary | Living Water",
         "Definitions of efflorescence, soft washing, hydro jetting, soda and dry ice blasting, poultices, spalling, elevator pits and more.",
         body, schema=[terms, crumbs_ld(trail)], priority="0.6", crumbs=True)


def html_sitemap():
    path = "/sitemap/"
    trail = [("Home", "/"), ("Sitemap", path)]
    groups = [("Services", [(SERVICES[s]["nav"], f"/{s}/") for s in SERVICE_ORDER_CORE + SERVICE_ORDER_SPECIAL] + [("Elevator Pit Water Removal", "/elevator-pit-water-removal/")] + [(SERVICES[s]["nav"], f"/{s}/") for s in SERVICE_ORDER_SUB]),
              ("Service areas", [("All service areas", "/service-areas/")] + [(c["name"], f"/pressure-washing-{c['slug']}/") for c in CITIES]),
              ("Guides", [("All guides", "/guides/")] + [(g["title"], f"/guides/{g['slug']}/") for g in GUIDES]),
              ("Company", [("About", "/about-us/"), ("Reviews", "/reviews/"), ("Industries", "/industries/"), ("Gallery", "/gallery/"), ("Interlock cost calculator", "/interlock-cleaning-sealing-cost-calculator/"), ("Interlock wash, sand & seal $3.50/sq ft", "/interlock-wash-sand-seal-3-50-per-sq-ft/"), ("FAQ", "/faq/"), ("Glossary", "/glossary/"), ("Contact", "/contact/"), ("Safety policy", "/safety-policy/"), ("Privacy policy", "/privacy-policy/")])]
    cols = "".join(f'<div><h2 style="font-size:1.3rem">{n}</h2><ul class="ticks">{"".join(f"<li><a href={chr(34)}{u}{chr(34)}>{esc(t)}</a></li>" for t, u in links)}</ul></div>' for n, links in groups)
    body = f"""<section class="page-hero"><div class="wrap">{crumbs_html(trail)}<h1>Sitemap</h1></div></section>
<section><div class="wrap grid g2">{cols}</div></section>"""
    page(path, "Sitemap | Living Water Pressure Wash Services", "Every page on the Living Water website: pressure washing services, 19 GTA service areas, expert guides, FAQ, glossary and company information.", body, schema=[crumbs_ld(trail)], priority="0.3", crumbs=True)
