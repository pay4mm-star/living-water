# Audience landing pages: condo/property managers and elevator service companies. Executed in gen.py namespace.
COND_URL = "/condo-property-manager-pressure-washing-toronto/"
ELEV_URL = "/elevator-company-pit-cleaning-subcontractor-gta/"

COND_FAQS = [
    ("What services do you provide to condo corporations and property managers?",
     "Garage and podium washing, entrance and walkway cleaning, facade and brick washing, graffiti removal, elevator pit cleaning and emergency water cleanup, scheduled to suit your building and your residents."),
    ("Do you provide insurance and WSIB documents?",
     "Yes. We provide a $5M liability Certificate of Insurance and WSIB clearance for your files before work starts, and follow your contractor sign-in and safety rules."),
    ("Can work be done after hours or on weekends?",
     "Yes. We schedule around residents and building operations, including evenings and weekends where the property allows."),
    ("Can you set up a regular maintenance schedule?",
     "Yes. Many buildings book a spring wash after the salt season and a fall clean before winter, with extra visits for entrances and high-traffic areas. We can quote a recurring program."),
    ("How much does elevator pit cleaning cost?",
     "Published starting prices are $1,500 for a single pit (up to 4 inches of water), $2,500 for a double, $3,500 for a triple and $4,500 for four pits, each including full cleaning and sanitizing ready for paint, before HST."),
    ("Do you handle emergency water or flooding in garages and pits?",
     "Yes. Our 24/7 emergency line is (647) 833-4343 for water removal and cleanup in garages, mechanical areas and elevator pits."),
    ("How do you quote for a board or property manager?",
     "A free assessment or photo review, then a fixed written price you can take to the board for approval."),
]
ELEV_FAQS = [
    ("Do you work as a subcontractor for elevator companies?",
     "Yes. We clean elevator pits for elevator service and maintenance companies, coordinated with your mechanics so the unit is locked out and secured by you before we enter."),
    ("What does your elevator pit cleaning include?",
     "Removal of water and debris, full cleaning and sanitizing of the pit, ready for paint. Published starting prices begin at $1,500 for a single pit with up to 4 inches of water, before HST."),
    ("Do you provide insurance and WSIB?",
     "Yes. We provide a $5M liability Certificate of Insurance and WSIB clearance, and follow your safety and lock-out procedures."),
    ("Can you handle emergency pump-outs?",
     "Yes. Call our 24/7 line at (647) 833-4343."),
    ("Do you offer pricing for multiple pits?",
     "Yes. Published starting prices cover single, double, triple and four-pit jobs, and we can quote multi-building or recurring programs."),
    ("Which areas do you cover?",
     "Toronto and the GTA, including Mississauga, Vaughan, Markham, Brampton, Oakville, Burlington, Hamilton and Barrie."),
]


def _aud_page(path, trail, pill, h1, lead, hero, answer, sections, figs, faqs, title, desc, related):
    photos = "".join(photo(k) for k in figs)
    rel = "".join(f'<a href="{u}">{t} →</a>' for u, t in related)
    body = f'''
<section class="page-hero"><picture>{hero_img(hero, "100vw", eager=True, alt="")}</picture>
<div class="wrap">{crumbs_html(trail)}<span class="pill">{esc(pill)}</span><h1>{h1}</h1><p>{esc(lead)}</p>
<div class="cta-row" style="justify-content:flex-start"><a class="btn" href="/contact/#quote">Get a Free Quote</a><a class="btn ghost" href="tel:{PHONE_MAIN[0]}">Call {PHONE_MAIN[1]}</a></div></div></section>
<section><div class="wrap layout"><article class="prose"><p class="answer">{esc(answer)}</p>{reviewed_line()}{sections}
<h2>Recent work</h2><div class="grid g3">{photos}</div></article>
<aside class="side">{quote_aside()}<div><h2 class="h3">Related</h2><nav class="related" aria-label="Related pages">{rel}</nav></div></aside></div></section>
{faq_block(faqs, "FAQ")}
{areas_block()}
{cta_block()}'''
    svc = {"@context": "https://schema.org", "@type": "Service", "@id": SITE + path + "#service", "name": h1.replace("&amp;", "&"),
           "description": answer, "url": SITE + path, "provider": {"@id": ORG_ID}, "image": SITE + best(hero),
           "areaServed": [{"@type": "City", "name": a} for a in AREAS]}
    page(path, title, desc, body, schema=[svc, crumbs_ld(trail), faq_ld(faqs)], preload=hero, priority="0.8", crumbs=True)


def audience_pages():
    cond_sections = '''<h2>One contractor for the whole property</h2>
<div class="grid g2"><div><h3>Garages and podiums</h3><p>Hot-water washing of parking levels, ramps, drive lanes and podium decks to remove salt, grit and oil. See <a href="/parking-garage-cleaning/">parking garage cleaning</a> and our <a href="/guides/condo-parking-garage-cleaning-guide/">condo garage guide</a>.</p></div>
<div><h3>Entrances, walkways and facades</h3><p>Safe, material-matched cleaning of brick, stone, precast and metal, with <a href="/graffiti-removal/">graffiti removal</a> when needed. See <a href="/commercial-power-washing/">commercial power washing</a>.</p></div>
<div><h3>Elevator pits</h3><p>Full cleaning and sanitizing, ready for paint, from $1,500 per pit. See <a href="/elevator-pit-cleaning/">elevator pit cleaning</a> and the <a href="/guides/winter-elevator-pit-checklist/">winter checklist</a>.</p></div>
<div><h3>Emergency cleanup</h3><p>24/7 response for water in garages, mechanical rooms and pits via <a href="/elevator-pit-water-removal/">elevator pit water removal</a> and <a href="/disaster-restoration/">disaster restoration</a>.</p></div></div>
<h2>Built for boards and managers</h2>
<ul class="ticks"><li>$5M liability Certificate of Insurance and WSIB clearance for your files</li><li>Fixed written quotes you can take to the board</li><li>Scheduling around residents, including evenings and weekends</li><li>Written scope so you can compare contractors fairly</li><li>Recurring spring and fall programs available</li></ul>
<h2>How it works</h2>
<ol class="steps-list"><li><strong>Tell us about the building.</strong> Address, what needs cleaning and any access limits.</li><li><strong>Assessment and quote.</strong> Free visit or photo review, then a fixed written price.</li><li><strong>Schedule and notice.</strong> We agree dates and help with resident notices.</li><li><strong>Clean and report.</strong> Work completed, site left tidy, documents on file.</li></ol>'''
    _aud_page(COND_URL, [("Home", "/"), ("Industries", "/industries/"), ("Condo & Property Managers", COND_URL)], "For Condo Boards & Property Managers",
              "Pressure Washing for Condos &amp; Property Managers in Toronto",
              "Garages, podiums, entrances, facades and elevator pits for condo corporations and property managers across the GTA.",
              "condo-column-pressure-washing",
              "Living Water cleans condo garages, podiums, entrances, facades and elevator pits for condo corporations and property managers across Toronto and the GTA, with a $5M liability certificate, WSIB clearance, fixed written quotes and scheduling around residents.",
              cond_sections, ["condo-podium-column-cleaning-1", "pressure-washer-set-up-in-a-parking-garage", "condo-elevator-pit-clean-out-after-1", "hot-water-washing-a-condo-terrace-and-planter-wall", "commercial-lobby-entrance-pressure-washing", "condo-elevator-pit-clean-out-1"],
              COND_FAQS, "Condo & Property Manager Pressure Washing | Toronto GTA",
              "Pressure washing for condo boards and property managers in Toronto & the GTA: garages, podiums, entrances, facades, elevator pits. COI + WSIB, fixed quotes.",
              [("/parking-garage-cleaning/", "Parking garage cleaning"), ("/elevator-pit-cleaning/", "Elevator pit cleaning"), ("/commercial-power-washing/", "Commercial power washing"), ("/pressure-washing-prices-toronto/", "Pricing")])
    elev_sections = '''<h2>Elevator pit cleaning for elevator companies</h2>
<p>When a pit needs cleaning, your mechanics need it done properly and out of the way. Living Water cleans and sanitizes elevator pits so they are ready for paint, working to your lock-out and safety procedures.</p>
<table class="price-table"><caption class="sr-only">Elevator pit cleaning starting prices</caption><thead><tr><th scope="col">Pits</th><th scope="col">Starting price (before HST)</th></tr></thead><tbody><tr><td>Single pit (up to 4 inches of water)</td><td>From $1,500</td></tr><tr><td>Double pit</td><td>From $2,500</td></tr><tr><td>Triple pit</td><td>From $3,500</td></tr><tr><td>Four pits</td><td>From $4,500</td></tr></tbody></table>
<h2>Why elevator companies use a specialist</h2>
<ul class="ticks"><li>Coordinated with your mechanics and lock-out procedures</li><li>Water removal, cleaning and sanitizing in one visit</li><li>$5M liability insurance and WSIB clearance</li><li>24/7 emergency line for urgent pump-outs</li><li>Multi-pit and multi-building programs quoted on request</li></ul>
<p>See the full <a href="/elevator-pit-cleaning/">elevator pit cleaning service</a>, our <a href="/elevator-pit-water-removal/">water removal</a> service and the <a href="/guides/elevator-pit-cleaning-guide/">elevator pit cleaning guide</a>.</p>'''
    _aud_page(ELEV_URL, [("Home", "/"), ("Industries", "/industries/"), ("Elevator Companies", ELEV_URL)], "For Elevator Service Companies",
              "Elevator Pit Cleaning for Elevator Companies in the GTA",
              "A specialist pit-cleaning partner for elevator service and maintenance companies in Toronto and the GTA.",
              "elevator-pit-pressure-washing",
              "Living Water cleans and sanitizes elevator pits as a partner to elevator service companies across Toronto and the GTA, from $1,500 per single pit, coordinated with your mechanics and lock-out procedures, with $5M liability insurance, WSIB clearance and 24/7 emergency response.",
              elev_sections, ["elevator-pit-cleaning-toronto", "elevator-pit-buffer-cleaning", "elevator-pit-springs-cleaned", "condo-elevator-pit-clean-out-before-1", "condo-elevator-pit-clean-out-after-1", "condo-elevator-pit-clean-out-3"],
              ELEV_FAQS, "Elevator Pit Cleaning for Elevator Companies | GTA",
              "Elevator pit cleaning partner for elevator service companies in the GTA. From $1,500 per pit, COI + WSIB, 24/7 emergency response.",
              [("/elevator-pit-cleaning/", "Elevator pit cleaning"), ("/elevator-pit-water-removal/", "Elevator pit water removal"), ("/guides/elevator-pit-cleaning-guide/", "Elevator pit guide"), ("/pressure-washing-prices-toronto/", "Pricing")])


audience_pages()
