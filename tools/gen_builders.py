# Masonry cleaning for home builders (Ontario). Executed in gen.py namespace.
BLD_URL = "/masonry-cleaning-for-home-builders/"
_CITIES = ["Toronto", "Vaughan", "Markham", "Richmond Hill", "Mississauga", "Brampton", "Oakville", "Burlington", "Milton", "Whitby", "Oshawa", "Pickering", "Newmarket", "Aurora", "Barrie", "Hamilton", "St. Catharines and Niagara"]

BLD_FAQS = [
    ("What is post-construction masonry cleaning?",
     "It is the final clean of new brick, stone, precast and concrete after the masons and other trades finish. It removes mortar smears and splatter, construction dust, stains, rust marks and efflorescence so the building looks right at inspection and closing."),
    ("Why does new brick and stone get white efflorescence?",
     "New masonry holds moisture from mortar and construction. As it dries, water carries natural salts to the surface and leaves a white powdery bloom. It is common on new buildings, and we remove it so the colour shows true before handover."),
    ("When should masonry be cleaned on a new build?",
     "Usually after the masonry is complete and cured and before final landscaping, final inspection and occupancy or closing. Cleaning too early lets later trades re-soil the walls, and we can coordinate timing with your site super."),
    ("Do you clean townhome blocks and condo towers?",
     "Yes. We clean multi-unit townhome blocks, condo podiums, limestone bases and tall brick elevations using boom lifts, ladders and pole systems, working floor by floor or block by block."),
    ("How do you price masonry cleaning for builders?",
     "Per project, from the wall area, height and access, the masonry type and how soiled it is. We give a fixed written quote after reviewing drawings or photos or a site visit, and can price per unit, per block or as a program across subdivisions."),
    ("Can you clean without damaging new brick, stone or mortar?",
     "Yes. We match the cleaner and pressure to the masonry, test a small area first, and avoid aggressive methods that can etch limestone or open mortar joints."),
    ("Do you provide insurance and WSIB documents for site access?",
     "Yes. We provide a Certificate of Insurance ($5M liability) and WSIB clearance, and follow your site safety rules and sign-in procedures."),
    ("Can you work around other trades and tight schedules?",
     "Yes. We schedule early mornings, evenings and weekends, coordinate with the site super, and move quickly to keep final cleans off your critical path."),
    ("Which parts of Ontario do you serve?",
     "Toronto and the GTA, plus Hamilton, Niagara, Barrie and surrounding communities. Contact us for projects further afield."),
    ("Can you remove efflorescence on stone covered by a manufacturer warranty?",
     "Yes. Living Water is relied on by several Ontario stone and paver manufacturers as a warranty service provider for efflorescence removal. Ask us to coordinate with your supplier."),
]


def builders_page():
    path = BLD_URL
    trail = [("Home", "/"), ("Services", "/power-washing-services/"), ("Brick Cleaning & Paint Removal", "/brick-cleaning-paint-removal/"), ("Masonry Cleaning for Home Builders", path)]
    hero = "new-condo-townhome-blocks-in-dark-brick-and-glass-during-construction-"
    answer = ("Living Water provides post-construction masonry cleaning for home builders across Ontario: removing mortar smears, construction dust, rust marks and white efflorescence from new brick, stone and precast "
              "on single homes, townhome blocks and condo towers, scheduled around your trades and ready for final inspection and closing. We carry $5M liability insurance and WSIB clearance, and quote each project at a fixed price.")
    figs = "".join(photo(k) for k in ["white-efflorescence-on-a-new-dark-brick-corner-before-cleaning", "technician-washing-the-limestone-base-of-a-new-dark-brick-condo",
                                      "boom-lift-set-up-in-front-of-new-condo-townhomes-for-facade-washing", "grey-brick-condo-building-on-a-corner-lot-after-exterior-cleaning",
                                      "limestone-look-cladding-on-a-new-custom-home-before-cleaning", "new-luxury-home-exterior-cleaning"])
    ba_pair = photo("efflorescence-removal-on-precast-steps-before-1|efflorescence-removal-on-precast-steps-after-1")
    more = "".join(photo(k) for k in ["dark-brick-condo-tower-corner-with-a-crew-washing-the-podium", "living-water-vans-on-site-at-a-new-condo-development-in-the-gta", "new-home-exterior-after-cleaning"])
    cities = ", ".join(f'<a href="/pressure-washing-{c["slug"]}/">{esc(c["name"])}</a>' for c in CITIES)
    article = f'''<article class="prose">
<p class="answer">{esc(answer)}</p>{reviewed_line()}
<h2>Masonry cleaning built for home builders</h2>
<p>The last thing between a finished build and a happy buyer is a clean exterior. Mortar smears, dust from cutting, rust runs, grout haze and white efflorescence are all normal on new masonry, but they show up at the pre-delivery inspection and in the buyer's first photos. Living Water cleans them off so your brick, stone and precast look the way they were specified.</p>
<div class="grid g2">
<div><h3>Single homes and custom builds</h3><p>Stone cladding, brick and limestone-look facades, porches, steps and driveways cleaned and ready for handover.</p></div>
<div><h3>Townhome blocks and subdivisions</h3><p>Block-by-block programs priced per unit or per block, so you can plan costs across a phase.</p></div>
<div><h3>Condo towers and podiums</h3><p>Dark brick, limestone bases and precast cleaned from boom lifts and lift baskets after construction.</p></div>
<div><h3>Models, sales centres and show homes</h3><p>A quick, careful clean so the property looks its best for buyers and photography.</p></div>
</div>
<h2>What we remove from new masonry</h2>
<ul class="ticks cols"><li>Mortar smears and splatter</li><li>Construction dust and dirt</li><li>White efflorescence on brick, stone and precast</li><li>Rust and metal run-off stains</li><li>Grout haze and cement residue</li><li>Efflorescence on pavers, steps and copings</li><li>Algae and organic growth on exposed walls</li><li>General soiling before final photos</li></ul>
<h2>Before and after on new builds</h2>
<div class="grid g3">{figs}</div>
<div class="grid g2" style="margin-top:24px">{ba_pair}</div>
<h2>Why builders choose Living Water</h2>
<ul class="ticks"><li><strong>28 years on the job.</strong> We have cleaned 7,500+ properties across the GTA, including new condo and townhome developments.</li><li><strong>Safe on new masonry.</strong> Methods are matched to the brick, stone or precast, and tested first, so mortar and finishes are protected.</li><li><strong>Equipment for height.</strong> Boom lifts, lift baskets and pole systems for tall elevations.</li><li><strong>Site-ready paperwork.</strong> $5M liability insurance and WSIB clearance on request, and we follow your site safety rules.</li><li><strong>Fits your schedule.</strong> Early, late and weekend work around other trades.</li><li><strong>Warranty know-how.</strong> We remove efflorescence as a service provider for several Ontario stone manufacturers.</li><li><strong>Photo reports.</strong> Before-and-after photos for your files and your customers.</li></ul>
<h2>How a builder project works</h2>
<ol class="steps-list"><li><strong>Send the details.</strong> Address, number of units or elevations, masonry type and photos or drawings.</li><li><strong>Quote.</strong> A fixed written price per unit, block or phase.</li><li><strong>Schedule.</strong> We coordinate with your site super around trades, inspections and closings.</li><li><strong>Clean.</strong> Test area first, then the full clean, with protection for windows, landscaping and finishes.</li><li><strong>Report.</strong> Before-and-after photos and notes on anything we see, such as ongoing efflorescence or sealed joints.</li></ol>
<h2>Efflorescence on new builds</h2>
<p>Efflorescence is the white, powdery salt deposit left when moisture moves through masonry and evaporates. It is cosmetic, common on new brick, stone and pavers, and can reappear until the masonry dries out. Read our guide on <a href="/guides/how-to-remove-efflorescence/">how to remove efflorescence</a> or see our <a href="/efflorescence-removal/">efflorescence removal service</a>. For brick, see <a href="/brick-cleaning-paint-removal/">brick cleaning</a> and <a href="/stone-restoration/">stone restoration</a>.</p>
<h2>Serving builders across Ontario</h2>
<p>We work with home builders, townhome developers and general contractors in {cities}, as well as Hamilton, Niagara and Barrie. See all <a href="/service-areas/">service areas</a>.</p>
<h2>More new-build projects</h2>
<div class="grid g3">{more}</div>
</article>'''
    form = f'''<section class="soft" id="builder-quote"><div class="wrap"><div class="contact-card">
<h2>Request a builder quote</h2><p>Tell us about your project. We reply within one business day with a fixed written price.</p>
<form action="https://api.web3forms.com/submit" method="POST">
<input type="hidden" name="access_key" value="{W3F_KEY}"><input type="hidden" name="subject" value="Builder masonry cleaning quote — livingwater-pws.com">
<input type="hidden" name="from_name" value="Living Water website"><input type="hidden" name="redirect" value="{SITE}/thank-you/">
<input type="hidden" name="service" value="Masonry cleaning for home builders">
<input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true" style="display:none">
<div class="row"><div class="field"><label for="bq-c">Company *</label><input id="bq-c" name="company" autocomplete="organization" required></div><div class="field"><label for="bq-n">Your name *</label><input id="bq-n" name="name" autocomplete="name" required></div></div>
<div class="row"><div class="field"><label for="bq-p">Phone *</label><input id="bq-p" type="tel" name="phone" autocomplete="tel" required></div><div class="field"><label for="bq-e">Email *</label><input id="bq-e" type="email" name="email" autocomplete="email" required></div></div>
<div class="row"><div class="field"><label for="bq-l">Project location *</label><input id="bq-l" name="location" required></div><div class="field"><label for="bq-u">Number of homes / units / elevations</label><input id="bq-u" name="units"></div></div>
<div class="row"><div class="field"><label for="bq-t">Project type</label><select id="bq-t" name="project_type"><option>Single / custom home</option><option>Townhome blocks</option><option>Condo or apartment building</option><option>Subdivision program</option><option>Other</option></select></div><div class="field"><label for="bq-d">Target date</label><input id="bq-d" name="target_date" placeholder="e.g. before closing in March"></div></div>
<div class="field"><label for="bq-m">Masonry and issues (optional)</label><textarea id="bq-m" name="message" rows="3" placeholder="e.g. dark brick with efflorescence, limestone base, mortar smears"></textarea></div>
<button class="btn" type="submit">Send my builder quote request</button>
<p style="font-size:.85rem;margin-top:12px">Photos or drawings help: reply to our email with them. We never share your information.</p>
</form></div></div></section>'''
    body = f'''
<section class="page-hero"><picture>{hero_img(hero, "100vw", eager=True, alt="")}</picture>
<div class="wrap">{crumbs_html(trail)}<span class="pill">For Home Builders</span><h1>Masonry Cleaning for Home Builders in Ontario</h1><p>Post-construction brick, stone and precast cleaning for new homes, townhomes and condos, ready for inspection and closing.</p>
<div class="cta-row" style="justify-content:flex-start"><a class="btn" href="#builder-quote">Get a Builder Quote</a><a class="btn ghost" href="tel:{PHONE_MAIN[0]}">Call {PHONE_MAIN[1]}</a></div></div></section>
<section><div class="wrap layout">{article}
<aside class="side">{quote_aside()}<div><h2 class="h3">Related</h2><nav class="related" aria-label="Related pages"><a href="/brick-cleaning-paint-removal/">Brick cleaning &amp; paint removal →</a><a href="/efflorescence-removal/">Efflorescence removal →</a><a href="/stone-restoration/">Stone restoration →</a><a href="/commercial-power-washing/">Commercial power washing →</a><a href="/industries/">Industries we serve →</a></nav></div></aside>
</div></section>
{form}
{faq_block(BLD_FAQS, "Builder Masonry Cleaning FAQ")}
{reviews_block()}
{areas_block()}
{cta_block()}'''
    svc_ld = {"@context": "https://schema.org", "@type": "Service", "@id": SITE + path + "#service", "name": "Masonry Cleaning for Home Builders",
              "serviceType": "Post-construction masonry cleaning", "description": answer, "url": SITE + path, "provider": {"@id": ORG_ID}, "image": SITE + best(hero),
              "areaServed": [{"@type": "AdministrativeArea", "name": "Ontario"}] + [{"@type": "City", "name": a} for a in AREAS],
              "audience": {"@type": "BusinessAudience", "audienceType": "Home builders, townhome and condo developers, general contractors"},
              "offers": {"@type": "Offer", "url": SITE + path + "#builder-quote", "priceCurrency": "CAD", "description": "Fixed written quote per project, unit or block"}}
    page(path, "Masonry Cleaning for Home Builders | Ontario New Builds",
         "Post-construction masonry cleaning for Ontario home builders: remove mortar, dust and efflorescence from new brick and stone. Townhomes, condos, custom homes.",
         body, schema=[svc_ld, crumbs_ld(trail), faq_ld(BLD_FAQS)], preload=hero, priority="0.9", crumbs=True)


builders_page()
