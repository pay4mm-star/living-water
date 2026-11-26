# Interlock wash / sand / seal pricing pages + estimator. Executed in gen.py namespace (after gen_more, gen_links, gen_projects).
PSF = 3.50
HST_RATE = 0.13
CALC_URL = "/interlock-cleaning-sealing-cost-calculator/"
OFFER_URL = "/interlock-wash-sand-seal-3-50-per-sq-ft/"
EST_JS_V = _ver("/assets/js/estimator.js")


def _m(n):
    return f"${n:,.2f}" if n != int(n) else f"${int(n):,}"


SAMPLES = [("Front walkway and steps", 150), ("Single-car driveway (12 × 20 ft)", 240), ("Backyard patio (14 × 16 ft)", 224),
           ("Double driveway (20 × 20 ft)", 400), ("Driveway plus front walkway", 600), ("Large driveway, walkway and patio", 1000)]


def price_table():
    rows = "".join(f"<tr><td>{esc(n)}</td><td>{sf:,} sq ft</td><td>{_m(sf * PSF)}</td><td>{_m(round(sf * PSF * (1 + HST_RATE), 2))}</td></tr>" for n, sf in SAMPLES)
    return (f'<table class="price-table"><caption class="sr-only">Sample interlock wash, sand and seal prices at $3.50 per square foot</caption>'
            f'<thead><tr><th scope="col">Typical area</th><th scope="col">Size</th><th scope="col">Price before HST</th><th scope="col">Total with 13% HST</th></tr></thead><tbody>{rows}</tbody></table>')


def estimator_html(compact=False):
    presets = "".join(f'<button type="button" data-preset="{p}">{l}</button>' for p, l in [
        ("Driveway|12|20", "Single driveway 12×20 ft"), ("Driveway|20|20", "Double driveway 20×20 ft"),
        ("Front walkway|4|30", "Walkway 4×30 ft"), ("Backyard patio|14|16", "Patio 14×16 ft")])
    return f'''<section class="est-wrap" id="estimator" data-rate="{PSF}" data-hst="{HST_RATE}"><div class="wrap">
<div class="est">
<div class="est-main">
<h2>Interlock wash, sand &amp; seal estimator</h2>
<p class="est-lead">Add each area you want done and the price updates instantly — {_m(PSF)} per square foot for the full wash, polymeric sand and seal.</p>
<div class="est-unit" role="group" aria-label="Measurement unit"><button type="button" data-unit="ft" aria-pressed="true">Feet</button><button type="button" data-unit="m" aria-pressed="false">Metres</button></div>
<div class="est-presets"><span>Quick add:</span>{presets}</div>
<div id="est-rows" role="group" aria-label="Areas to clean and seal"></div>
<noscript><p><strong>Turn on JavaScript to use the calculator, or work it out yourself:</strong> length × width in feet = square feet, then multiply by {_m(PSF)}. HST is added.</p></noscript>
<p style="margin:14px 0 0"><button type="button" class="btn line sm" id="est-add">+ Add another area</button></p>
</div>
<aside class="est-result" aria-live="polite" aria-label="Your estimate">
<h2>Your estimate</h2>
<dl><div><dt>Total area</dt><dd id="est-area">0 sq ft</dd></div>
<div><dt>Wash, sand &amp; seal at {_m(PSF)}/sq ft</dt><dd id="est-sub">$0.00</dd></div>
<div><dt>HST (13%)</dt><dd id="est-hst">$0.00</dd></div>
<div class="big"><dt>Estimated total</dt><dd id="est-total">$0.00</dd></div></dl>
<p class="est-note">This is an estimate. We confirm a fixed written price after a free assessment. Surfaces needing old sealer stripped, heavy staining or efflorescence treatment can change the price — we tell you before any work starts.</p>
<a class="btn" href="#est-quote">Get this quote</a>
<a class="btn ghost" href="tel:{PHONE_MAIN[0]}">Call {PHONE_MAIN[1]}</a>
</aside>
</div>
<div class="est-quote" id="est-quote">
<h2>Send me this quote</h2>
<p>Tell us where to send it. We reply within one business day with a fixed written price — no obligation.</p>
<form id="est-quote-form" action="https://api.web3forms.com/submit" method="POST">
<input type="hidden" name="access_key" value="{W3F_KEY}">
<input type="hidden" name="subject" value="Interlock quote request — livingwater-pws.com">
<input type="hidden" name="from_name" value="Living Water website">
<input type="hidden" name="redirect" value="{SITE}/thank-you/">
<input type="hidden" name="service" value="Interlock Wash, Sand &amp; Seal ($3.50/sq ft)">
<input type="hidden" name="estimate_sqft" value=""><input type="hidden" name="estimate_before_hst" value=""><input type="hidden" name="estimate_details" value="">
<input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true" style="display:none">
<div class="row"><div class="field"><label for="eq-n">Name *</label><input id="eq-n" name="name" autocomplete="name" required></div>
<div class="field"><label for="eq-p">Phone *</label><input id="eq-p" type="tel" name="phone" autocomplete="tel" required></div></div>
<div class="row"><div class="field"><label for="eq-e">Email *</label><input id="eq-e" type="email" name="email" autocomplete="email" required></div>
<div class="field"><label for="eq-pc">Postal code / city *</label><input id="eq-pc" name="location" autocomplete="postal-code" required></div></div>
<div class="field"><label for="eq-m">Anything we should know? (optional)</label><textarea id="eq-m" name="message" rows="3" placeholder="e.g. sealed before, weeds in the joints, oil stains near the garage"></textarea></div>
<button class="btn" type="submit">Send my quote request</button>
<p style="font-size:.85rem;margin-top:12px">We never share or sell your information. See our <a href="/privacy-policy/">privacy policy</a>.</p>
</form></div>
</div></section>
<script src="/assets/js/estimator.js?v={EST_JS_V}" defer></script>'''


def _faq_pair(q, a):
    return (q, a)


CALC_FAQS = [
    ("How much does interlock cleaning and sealing cost in Toronto?",
     f"Living Water's full interlock wash, polymeric sand and seal package is {_m(PSF)} per square foot plus HST across Toronto and the GTA. A 400 sq ft double driveway is {_m(400 * PSF)} before HST, and a 150 sq ft front walkway is {_m(150 * PSF)} before HST."),
    ("How do I calculate the square footage of my interlock driveway or patio?",
     "Multiply the length by the width in feet for each rectangular area, then add the areas together. Split L-shaped or curved areas into rectangles and estimate. If you measure in metres, multiply square metres by 10.76 to get square feet — the calculator above does this when you switch to metres."),
    ("What is included in the $3.50 per square foot price?",
     "A hot-water surface-cleaner wash that removes dirt, moss and algae, flushing out the old joint sand, re-sanding with polymeric sand, and application of a protective sealer once the interlock is fully dry. We also bring and remove our own equipment and clean up."),
    ("Is HST included in the estimate?",
     "No. The $3.50 per square foot price is before HST. The calculator shows the 13% HST separately so you can see the total you would pay."),
    ("Is the online estimate my final price?",
     "It is a close guide for a standard job, and we confirm a fixed written price after a free assessment, before any work starts. Heavy staining, efflorescence, old failing sealer that must be stripped, or very difficult access can change the price — we tell you first."),
    ("How much does it cost to clean interlock without sealing?",
     "We price wash-only jobs from your measurements and the condition of the surface, so ask for a fixed written quote. The $3.50 per square foot rate is for the complete wash, sand and seal package."),
    ("How often does interlock need to be resealed?",
     "Most sealed interlock is re-sealed every two to four years, depending on the sealer used, sun exposure and traffic. We check the surface at your assessment and tell you honestly whether it needs sealing again."),
    ("When can interlock be washed and sealed in Ontario?",
     "Sealer needs clean, completely dry pavers and mild, dry weather, so the main season runs from spring thaw through fall. Residential jobs are typically booked within two to five days of your quote."),
    ("Do I need to be home during the work?",
     "Not usually. We need access to the area and an outdoor tap if available, and we keep you updated. We will tell you how long to keep cars and foot traffic off the sealed surface for the sealer being used."),
    ("Which areas do you serve?",
     "Toronto, Vaughan, Markham, Richmond Hill, Mississauga, Oakville, Burlington, Brampton, Etobicoke, North York, Scarborough, Pickering, Whitby, Oshawa, Newmarket, Aurora, Hamilton, Barrie and the wider GTA."),
]

OFFER_FAQS = [
    ("What does wash, sand and seal mean?",
     "Wash is a hot-water surface-cleaner clean that removes dirt, moss, algae and weeds. Sand is re-filling the joints with polymeric sand so the pavers lock together and weeds stay out. Seal is a protective sealer applied once the interlock is clean and dry."),
    ("Is it really $3.50 per square foot?",
     f"Yes. Living Water charges {_m(PSF)} per square foot plus HST for the complete wash, sand and seal package on standard residential interlock. We confirm the exact figure in a fixed written quote after a free assessment."),
    ("What would my driveway cost?",
     f"Multiply the square footage by {_m(PSF)}. A 240 sq ft single-car driveway is {_m(240 * PSF)} before HST; a 400 sq ft double driveway is {_m(400 * PSF)} before HST. Use the estimator on this page for your exact measurements."),
    ("Does the price include HST?",
     "No — HST (13%) is added to the $3.50 per square foot price. The estimator shows both figures."),
    ("Can I just have my interlock washed and not sealed?",
     "Yes. Sealing is optional, and we price wash-only or wash and re-sand jobs from your measurements. Ask for a fixed written quote."),
    ("Why does interlock need re-sanding after washing?",
     "Cleaning flushes the old, weedy joint sand out along with the dirt. Fresh polymeric sand locks the pavers in place and resists weeds, ants and washout."),
    ("Is sealing worth it?",
     "A sealer enriches colour and makes stains easier to clean, and it helps joint sand stay put. It must go on clean, dry pavers with no efflorescence, and it needs re-applying every few years. We will tell you honestly if your surface does not need it."),
    ("Do you offer free quotes?",
     "Yes. Estimates and assessments are free, and every price is a fixed written quote before any work starts. We also send a certificate of insurance and WSIB clearance on request."),
]


def _quote_btns():
    return f'<div class="cta-row" style="justify-content:flex-start"><a class="btn" href="#estimator">Calculate my price</a><a class="btn ghost" href="tel:{PHONE_MAIN[0]}">Call {PHONE_MAIN[1]}</a></div>'


def _howto_ld():
    steps = [("Measure each area", "Use a tape measure to find the length and width of each interlock area in feet and multiply them to get square feet."),
             ("Split irregular shapes", "Break L-shaped or curved areas into rectangles, measure each one, and add the results together."),
             ("Add up the total square footage", "Add the square footage of the driveway, walkway, patio and steps. If you measured in metres, multiply square metres by 10.76."),
             ("Multiply by the price per square foot", f"Multiply the total by {_m(PSF)} for the wash, sand and seal package, then add 13% HST — or enter the measurements in the calculator.")]
    return {"@context": "https://schema.org", "@type": "HowTo", "name": "How to estimate interlock cleaning and sealing cost", "totalTime": "PT10M",
            "supply": [{"@type": "HowToSupply", "name": "Tape measure"}], "step": [{"@type": "HowToStep", "position": i + 1, "name": n, "text": t, "url": SITE + CALC_URL + "#how-to-measure"} for i, (n, t) in enumerate(steps)]}


def _service_ld(url, name, desc, img_key):
    return {"@context": "https://schema.org", "@type": "Service", "@id": SITE + url + "#service", "name": name, "serviceType": "Interlock cleaning, polymeric sanding and sealing",
            "description": desc, "url": SITE + url, "provider": {"@id": ORG_ID}, "image": SITE + best(img_key),
            "areaServed": [{"@type": "City", "name": a} for a in AREAS],
            "offers": {"@type": "Offer", "url": SITE + url, "priceCurrency": "CAD", "availability": "https://schema.org/InStock",
                       "description": "Wash, polymeric sand and seal for interlock and pavers. Price is before HST; fixed written quote after free assessment.",
                       "priceSpecification": {"@type": "UnitPriceSpecification", "price": f"{PSF:.2f}", "priceCurrency": "CAD", "unitCode": "FTK", "unitText": "square foot", "valueAddedTaxIncluded": False}}}


def calc_page():
    path = CALC_URL
    trail = [("Home", "/"), ("Services", "/power-washing-services/"), ("Driveway & Interlock Cleaning", "/driveway-interlock-cleaning/"), ("Interlock Cost Calculator", path)]
    hero = "stone-and-cedar-modern-home-with-a-charcoal-paver-driveway-after-clean"
    gallery_figs = "".join(photo(k) for k in ["interlock-walkway-pattern-after-cleaning", "interlock-steps-and-garden-beds", "clean-interlock-walkway-with-landscaping",
                                              "pale-paver-walkway-through-a-landscaped-garden-after-cleaning", "large-patterned-paver-patio-with-raised-steps-after-cleaning", "interlock-side-path-after-washing"])
    ba_fig = photo("stone-patio-cleaning-before|stone-patio-cleaning-after")
    eff = (f'<figure>{img("charcoal-paver-driveway-with-white-efflorescence-blotches-before-clean", "(max-width: 640px) 100vw, 380px")}<figcaption>Charcoal paver driveway with white efflorescence blotches — before</figcaption></figure>'
           f'<figure>{img("charcoal-paver-driveway-after-efflorescence-cleaning", "(max-width: 640px) 100vw, 380px")}<figcaption>The same driveway after cleaning</figcaption></figure>')
    answer = (f"Living Water's interlock cleaning and resealing price is {_m(PSF)} per square foot plus HST for the complete wash, polymeric sand and seal package across Toronto and the GTA. "
              f"A 400 sq ft double driveway costs about {_m(400 * PSF)} before HST. Use the calculator to price your own driveway, walkway and patio in seconds.")
    article = f'''<article class="prose">
<p class="answer">{esc(answer)}</p>{reviewed_line()}
<h2>How much does interlock cleaning and resealing cost?</h2>
<p>Most Ontario homeowners want one number: what will it cost to bring my interlock back and protect it? Our wash, sand and seal package is a flat <strong>{_m(PSF)} per square foot</strong> (plus 13% HST). That covers the hot-water surface-cleaner wash, fresh polymeric sand in the joints and a protective sealer applied once the pavers are dry.</p>
<p>Here is what that looks like on typical GTA properties:</p>
{price_table()}
<p>Prices are before any extras that a specific surface may need (see below). For a fixed written quote, <a href="/contact/#quote">request a free assessment</a>.</p>
<h2 id="how-to-measure">How to measure your interlock in 4 steps</h2>
<ol class="steps-list"><li><strong>Measure each area.</strong> Use a tape measure for the length and width in feet and multiply to get square feet.</li>
<li><strong>Split irregular shapes.</strong> Break L-shaped or curved areas into rectangles and add them up.</li>
<li><strong>Add the totals.</strong> Driveway, walkway, patio, steps and pool deck all count. Working in metres? Multiply square metres by 10.76.</li>
<li><strong>Multiply by {_m(PSF)}.</strong> Add 13% HST, or just type the measurements into the calculator above.</li></ol>
<h2>What is included in the price</h2>
<ul class="ticks cols"><li>Hot-water rotary surface-cleaner wash — no stripes or paver damage</li><li>Removal of moss, algae, dirt and weeds from the surface and joints</li><li>Fresh polymeric sand in the joints, so pavers lock and weeds stay out</li><li>Protective sealer applied to clean, dry interlock</li><li>Our own equipment, water supply and clean-up</li><li>Free assessment and a fixed written quote</li><li>Certificate of insurance and WSIB clearance on request</li><li>Re-clean guarantee</li></ul>
<h2>What can change the price</h2>
<ul class="ticks"><li><strong>Surface condition.</strong> Heavy oil, rust or efflorescence needs extra treatment.</li><li><strong>Old or failing sealer.</strong> It has to be stripped before new sealer will bond.</li><li><strong>Access.</strong> Steep grades, no water access or long hose runs add time.</li><li><strong>Joint condition.</strong> Deep weed growth or badly settled pavers may need repair first.</li></ul>
<p>We always tell you about any of these <em>before</em> work starts — never on the invoice. Read more in our <a href="/guides/pressure-washing-cost-factors/">pressure washing cost factors guide</a>.</p>
<h2>The wash, sand and seal process</h2>
<p>We wash first because sealer over dirt traps it. After the interlock is clean and fully dry, polymeric sand is swept into the joints and activated, and the sealer goes on last. Rushing the order — or sealing damp pavers — is what causes white haze and peeling, so we schedule around the weather. See our full <a href="/guides/interlock-cleaning-and-resanding/">interlock cleaning and re-sanding guide</a>.</p>
<h2>Interlock cleaning results from real Living Water jobs</h2>
<p>Photos from GTA driveways, walkways and patios.</p>
<div class="grid g3">{gallery_figs}</div>
<div class="grid g2" style="margin-top:24px">{ba_fig}{eff}</div>
<h2>How often should interlock be resealed?</h2>
<p>Most sealed interlock needs re-sealing every two to four years. Sun-baked driveways and high-traffic areas wear sooner; sheltered walkways last longer. If water no longer beads on the surface or joint sand keeps washing out, it is time for a check. We will tell you honestly whether it needs sealing again.</p>
<h2>Why homeowners choose Living Water</h2>
<p>Living Water has washed more than 7,500 properties across the GTA since 1998, carries $5M liability insurance and WSIB coverage, and holds a 4.9 / 5 rating on Google. See the <a href="/driveway-interlock-cleaning/">driveway and interlock cleaning service</a>, the <a href="/paver-stone-sealing/">paver and stone sealing service</a>, or our <a href="{OFFER_URL}">$3.50 per sq ft wash, sand and seal offer</a>.</p>
</article>'''
    body = f'''
<section class="page-hero"><picture>{hero_img(hero, "100vw", eager=True, alt="")}</picture>
<div class="wrap">{crumbs_html(trail)}<span class="pill">Free Online Estimator</span><h1>Interlock Cleaning &amp; Resealing Cost Calculator</h1><p>Wash, sand and seal your interlock for {_m(PSF)} per square foot. Enter your measurements and see your price instantly.</p>{_quote_btns()}</div></section>
{estimator_html()}
<section><div class="wrap layout">{article}
<aside class="side">{quote_aside()}<div><h2 class="h3">Related</h2><nav class="related" aria-label="Related pages"><a href="{OFFER_URL}">$3.50/sq ft wash, sand &amp; seal →</a><a href="/driveway-interlock-cleaning/">Driveway &amp; interlock cleaning →</a><a href="/paver-stone-sealing/">Paver &amp; stone sealing →</a><a href="/guides/interlock-cleaning-and-resanding/">Re-sanding guide →</a><a href="/guides/pressure-washing-cost-factors/">Cost factors guide →</a></nav></div></aside>
</div></section>
{faq_block(CALC_FAQS, "Interlock Cleaning &amp; Sealing Cost FAQ")}
{reviews_block()}
{areas_block()}
{cta_block()}'''
    app = {"@context": "https://schema.org", "@type": "WebApplication", "@id": SITE + path + "#calculator", "name": "Interlock Cleaning & Sealing Cost Calculator",
           "url": SITE + path, "applicationCategory": "BusinessApplication", "operatingSystem": "Any (web browser)", "browserRequirements": "Requires JavaScript",
           "description": f"Free calculator that estimates the cost of washing, re-sanding and sealing interlock pavers at {_m(PSF)} per square foot plus HST.",
           "provider": {"@id": ORG_ID}, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "CAD"}, "inLanguage": "en-CA"}
    page(path, "Interlock Cleaning & Sealing Cost Calculator | Toronto & GTA",
         f"Free interlock cleaning and resealing cost calculator. Wash, sand and seal for {_m(PSF)} per sq ft in Toronto & the GTA — enter your measurements, get a price.",
         body, schema=[app, _service_ld(path, "Interlock Wash, Sand and Seal", answer, hero), _howto_ld(), crumbs_ld(trail), faq_ld(CALC_FAQS)], preload=hero, priority="0.9", crumbs=True)


def offer_page():
    path = OFFER_URL
    trail = [("Home", "/"), ("Services", "/power-washing-services/"), ("Driveway & Interlock Cleaning", "/driveway-interlock-cleaning/"), ("Wash, Sand & Seal $3.50/sq ft", path)]
    hero = "large-patterned-paver-patio-with-raised-steps-after-cleaning"
    answer = (f"Living Water washes, re-sands and seals interlock for {_m(PSF)} per square foot plus HST across Toronto and the GTA. The price covers a hot-water surface-cleaner wash, fresh polymeric sand in the joints and a protective sealer — "
              f"for example, {_m(400 * PSF)} before HST for a 400 sq ft double driveway.")
    steps = [("Wash", "interlock-and-asphalt-edge-washed", "A hot-water rotary surface cleaner lifts dirt, moss, algae and weeds from the pavers and flushes out the tired joint sand. No stripes, no paver damage."),
             ("Sand", "interlock-walkway-pattern-after-cleaning", "Once the surface is clean and dry, polymeric sand is swept into the joints and activated so the pavers lock together and weeds and ants stay out."),
             ("Seal", "stone-patio-cleaning-after", "A protective sealer enriches colour and makes stains easier to clean. It goes on only after the interlock is clean, dry and free of efflorescence.")]
    step_html = "".join(f'<figure>{img(k, "(max-width: 640px) 100vw, 380px")}<h3><span class="n">{i}</span>{t}</h3><p>{esc(d)}</p></figure>' for i, (t, k, d) in enumerate(steps, 1))
    gal = "".join(photo(k) for k in ["interlock-steps-and-garden-beds", "clean-interlock-walkway-with-landscaping", "interlock-side-path-after-washing"])
    ba_fig = photo("stone-patio-cleaning-before|stone-patio-cleaning-after")
    article = f'''<article class="prose">
<p class="answer">{esc(answer)}</p>{reviewed_line()}
<div class="offer-box"><div><div class="amt">{_m(PSF)}<small> / sq ft</small></div><p>Wash + polymeric sand + seal · plus HST · fixed written quote</p></div><a class="btn" href="#estimator">Calculate my price</a></div>
<h2>What you get for {_m(PSF)} per square foot</h2>
<p>One price, three steps, one crew. Instead of piecing together a cleaner, a sand supplier and a sealing contractor, Living Water handles the whole interlock restoration:</p>
<div class="steps3">{step_html}</div>
<h2>Sample prices</h2>
<p>Multiply your area by {_m(PSF)}. Here are typical GTA jobs:</p>
{price_table()}
<p>Need a number for your own property? Use the <a href="{CALC_URL}">interlock cleaning and resealing cost calculator</a> or the estimator on this page.</p>
<h2>Who this price is for</h2>
<ul class="ticks cols"><li>Interlock and concrete paver driveways</li><li>Front walkways and steps</li><li>Backyard patios and pool decks</li><li>Side paths and garden borders</li><li>Condo and townhouse driveways</li><li>Homes across Toronto and the GTA</li></ul>
<p>Heavy efflorescence, old failing sealer that needs stripping and unusual access can change the price. We spot those at your free assessment and tell you before the work starts, so the written quote is the price you pay.</p>
<h2>Before and after</h2>
<div class="grid g3">{gal}</div>
<div class="grid g2" style="margin-top:24px">{ba_fig}</div>
<h2>Why get it all done at once</h2>
<p>Washing, re-sanding and sealing are a sequence: clean pavers take sand better, and sand-locked joints take sealer better. Doing all three together means the interlock stays tight, the colour is richer and the surface is easier to keep clean. The result typically lasts two to four years before it needs re-sealing, depending on the sealer, sun and traffic.</p>
<h2>How to book</h2>
<ol class="steps-list"><li><strong>Get your estimate</strong> with the calculator above, or call {PHONE_MAIN[1]}.</li><li><strong>Free assessment.</strong> We check the surface and confirm a fixed written quote.</li><li><strong>Booking.</strong> Residential jobs are typically scheduled within 2–5 days.</li><li><strong>Done and guaranteed.</strong> Clean-up included, with our re-clean guarantee.</li></ol>
<p>Read how interlock cleaning works in our <a href="/guides/interlock-cleaning-and-resanding/">expert guide</a>, or see our <a href="/driveway-interlock-cleaning/">driveway and interlock cleaning</a> and <a href="/paver-stone-sealing/">paver sealing</a> services.</p>
</article>'''
    body = f'''
<section class="page-hero"><picture>{hero_img(hero, "100vw", eager=True, alt="")}</picture>
<div class="wrap">{crumbs_html(trail)}<span class="pill">Interlock Offer</span><h1>Interlock Wash, Sand &amp; Seal — {_m(PSF)} per Sq Ft</h1><p>Hot-water wash, polymeric sand and protective sealer in one price, across Toronto and the GTA.</p>{_quote_btns()}</div></section>
<section><div class="wrap layout">{article}
<aside class="side">{quote_aside()}<div><h2 class="h3">Related</h2><nav class="related" aria-label="Related pages"><a href="{CALC_URL}">Interlock cost calculator →</a><a href="/driveway-interlock-cleaning/">Driveway &amp; interlock cleaning →</a><a href="/paver-stone-sealing/">Paver &amp; stone sealing →</a><a href="/guides/interlock-cleaning-and-resanding/">Re-sanding guide →</a><a href="/service-areas/">Service areas →</a></nav></div></aside>
</div></section>
{estimator_html()}
{faq_block(OFFER_FAQS, "Wash, Sand &amp; Seal FAQ")}
{reviews_block()}
{areas_block()}
{cta_block()}'''
    page(path, f"Interlock Wash, Sand & Seal – {_m(PSF)} per Sq Ft | Living Water",
         f"Interlock wash, polymeric sand and seal for {_m(PSF)} per square foot across Toronto & the GTA. See what's included, sample prices and get a free quote.",
         body, schema=[_service_ld(path, f"Interlock Wash, Sand and Seal — {_m(PSF)} per sq ft", answer, hero), crumbs_ld(trail), faq_ld(OFFER_FAQS)], preload=hero, priority="0.9", crumbs=True)


def interlock_promo():
    return (f'<div class="promo-inline"><h2>Interlock wash, sand &amp; seal: {_m(PSF)} per sq ft</h2>'
            f'<p>One price for the hot-water wash, polymeric sand and protective sealer. Price your own driveway, walkway or patio in seconds.</p>'
            f'<a class="btn sm" href="{CALC_URL}">Open the cost calculator</a> <a class="btn line sm" href="{OFFER_URL}">See what is included</a></div>')


# promo boxes on related service pages (before they are generated)
for _s in ("driveway-interlock-cleaning", "paver-stone-sealing"):
    if interlock_promo() not in SERVICES[_s]["body"]:
        SERVICES[_s]["body"] = SERVICES[_s]["body"].replace("<h2>What", interlock_promo() + "<h2>What", 1) if "<h2>What" in SERVICES[_s]["body"] else SERVICES[_s]["body"] + interlock_promo()

# calculator + offer pages are generated here (gen.py's page() list is ready at this point)
calc_page(); offer_page()
