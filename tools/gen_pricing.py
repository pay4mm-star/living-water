# Pressure washing prices page (Toronto & GTA). Only published prices; everything else is quote-based. Executed in gen.py namespace.
PRICE_URL = "/pressure-washing-prices-toronto/"
PRICE_FAQS = [
    ("How much does pressure washing cost in Toronto?",
     "It depends on the surface, area, access and how soiled it is. Living Water gives a free fixed written quote before work starts. Published starting prices: interlock wash, sand and seal at $3.50 per sq ft (before HST), and elevator pit cleaning from $1,500 per single pit."),
    ("Do you charge per square foot?",
     "For interlock wash, sand and seal we price at $3.50 per square foot before HST. Most other work is quoted per job because access, height, surface and soiling vary."),
    ("Are your prices before or after HST?",
     "Prices shown are before 13% HST unless stated, and HST is added to the final invoice."),
    ("Why do quotes for the same size of driveway differ between companies?",
     "Scope differs: some quotes cover only a surface rinse, while others include degreasing, edge detail, polymeric sand and sealing. Ask what is included, what insurance the contractor carries and whether the price is fixed."),
    ("Do you offer free quotes?",
     "Yes. Assessments are free and you get a fixed written price, with our Certificate of Insurance and WSIB clearance, before any work starts."),
    ("What makes a job cost more?",
     "Height or hard access, heavy staining or paint, delicate surfaces that need slower methods, after-hours work, travel distance and added services such as sealing."),
    ("Can I get an instant estimate?",
     "For interlock wash, sand and seal, yes: use our online estimator. For other services, send photos and your address for a quick quote."),
]


def pricing_page():
    path = PRICE_URL
    trail = [("Home", "/"), ("Services", "/power-washing-services/"), ("Pressure Washing Prices", path)]
    hero = "estate-home-driveway-washing"
    answer = ("Pressure washing in Toronto and the GTA is priced by surface, area, access and how soiled the job is. Living Water publishes starting prices where they are fixed: interlock wash, sand and seal at $3.50 per square foot, "
              "and elevator pit cleaning from $1,500 per single pit. Everything else gets a free, fixed written quote before work starts.")
    article = f'''<article class="prose"><p class="answer">{esc(answer)}</p>{reviewed_line()}
<h2>Published prices</h2>
<table class="price-table"><caption class="sr-only">Living Water published starting prices</caption><thead><tr><th scope="col">Service</th><th scope="col">Starting price (before HST)</th><th scope="col">What is included</th></tr></thead><tbody>
<tr><td><a href="{OFFER_URL}">Interlock wash, sand &amp; seal</a></td><td>$3.50 per sq ft</td><td>Wash, polymeric sand and sealer</td></tr>
<tr><td><a href="/elevator-pit-cleaning/">Elevator pit cleaning, single pit</a></td><td>From $1,500</td><td>Up to 4 inches of water, full clean and sanitize, ready for paint</td></tr>
<tr><td>Double pit</td><td>From $2,500</td><td>Full clean and sanitize, ready for paint</td></tr>
<tr><td>Triple pit</td><td>From $3,500</td><td>Full clean and sanitize, ready for paint</td></tr>
<tr><td>Four pits</td><td>From $4,500</td><td>Full clean and sanitize, ready for paint</td></tr></tbody></table>
<p>Estimate interlock jobs instantly with the <a href="{CALC_URL}">interlock cost calculator</a>.</p>
<h2>Services quoted per job</h2>
<p>These vary too much by site to publish one number, so we quote each after a photo review or visit:</p>
<ul class="ticks cols"><li><a href="/residential-power-washing/">Residential power washing</a></li><li><a href="/house-washing/">House washing</a></li><li><a href="/roof-cleaning/">Roof cleaning</a></li><li><a href="/deck-fence-cleaning/">Deck and fence cleaning</a></li><li><a href="/commercial-power-washing/">Commercial power washing</a></li><li><a href="/parking-garage-cleaning/">Parking garage cleaning</a></li><li><a href="/graffiti-removal/">Graffiti removal</a></li><li><a href="/sandblasting-services/">Sandblasting</a></li><li><a href="/efflorescence-removal/">Efflorescence removal</a></li><li><a href="/brick-cleaning-paint-removal/">Brick cleaning and paint removal</a></li></ul>
<h2>What affects the price</h2>
<ul class="ticks"><li>Surface type and condition</li><li>Total area and how many levels or elevations</li><li>Access, height and equipment such as boom lifts</li><li>Staining, paint, graffiti or efflorescence</li><li>Add-ons such as sealing or sanding</li><li>Timing, after-hours work and travel distance</li></ul>
<p>Our guide to <a href="/guides/pressure-washing-cost-factors/">pressure washing cost factors</a> explains these in more detail.</p>
<h2>What you get with every quote</h2>
<ul class="ticks"><li>Free assessment and a fixed written price</li><li>$5M liability insurance certificate and WSIB clearance</li><li>28 years of experience across the GTA</li></ul>
<p>Serving <a href="/pressure-washing-toronto/">Toronto</a> and the wider GTA: see all <a href="/service-areas/">service areas</a>.</p></article>'''
    body = f'''
<section class="page-hero"><picture>{hero_img(hero, "100vw", eager=True, alt="")}</picture>
<div class="wrap">{crumbs_html(trail)}<span class="pill">Pricing</span><h1>Pressure Washing Prices in Toronto &amp; the GTA</h1><p>Published starting prices, what affects cost, and free fixed written quotes.</p>
<div class="cta-row" style="justify-content:flex-start"><a class="btn" href="/contact/#quote">Get a Free Quote</a><a class="btn ghost" href="tel:{PHONE_MAIN[0]}">Call {PHONE_MAIN[1]}</a></div></div></section>
<section><div class="wrap layout">{article}<aside class="side">{quote_aside()}</aside></div></section>
{faq_block(PRICE_FAQS, "Pressure Washing Prices FAQ")}
{areas_block()}
{cta_block()}'''
    page(path, "Pressure Washing Cost & Prices Toronto & GTA | Living Water",
         "Pressure washing prices in Toronto & the GTA: interlock wash, sand and seal $3.50/sq ft, elevator pit cleaning from $1,500. Free fixed quotes.",
         body, schema=[crumbs_ld(trail), faq_ld(PRICE_FAQS)], preload=hero, priority="0.9", crumbs=True)


pricing_page()
