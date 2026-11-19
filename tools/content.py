"""All copy for livingwater-pws.com. Facts come from the existing site."""

SITE = "https://livingwater-pws.com"
NAME = "Living Water Pressure Wash Services"
LEGAL = "Living Water Pressure Wash Services Ltd."
EMAIL = "info@livingwater-pws.com"
PHONE_MAIN = ("+1-416-663-8000", "(416) 663-8000")
PHONE_TOLL = ("+1-833-456-2978", "1-833-456-2978")
PHONE_EMERG = ("+1-647-833-4343", "(647) 833-4343")

AREAS = ["Toronto", "North York", "Scarborough", "Etobicoke", "East York", "Mississauga", "Brampton",
         "Vaughan", "Woodbridge", "Maple", "Kleinburg", "Richmond Hill", "Markham", "King City", "Aurora",
         "Newmarket", "Georgina", "Pickering", "Ajax", "Whitby", "Oshawa", "Oakville", "Burlington", "Milton",
         "Hamilton", "Guelph", "Cambridge", "St. Catharines", "Niagara Falls", "Barrie", "Simcoe County"]

REGIONS = {
    "City of Toronto": ["Toronto", "North York", "Scarborough", "Etobicoke", "East York"],
    "Peel & Halton": ["Mississauga", "Brampton", "Oakville", "Burlington", "Milton"],
    "York Region": ["Vaughan", "Woodbridge", "Maple", "Kleinburg", "Richmond Hill", "Markham", "King City", "Aurora", "Newmarket", "Georgina"],
    "Durham Region": ["Pickering", "Ajax", "Whitby", "Oshawa"],
    "Hamilton, Niagara & Waterloo-Wellington": ["Hamilton", "St. Catharines", "Niagara Falls", "Guelph", "Cambridge"],
    "Simcoe County": ["Barrie", "Simcoe County"],
}

REVIEWS = [
    ("Mark Sampson", "We had an amazing experience with Navid and his team. They expertly pressure washed our backyard stones and applied a sealer to the pool coping. They stand by their work."),
    ("Des Hunter", "After 11 years we decided it was time to pressure wash our patio and pool deck. He was meticulous in ensuring every patio stone was completely clean. The end result looked like the original 11 years ago."),
    ("Brian Flaherty", "I thought my patio and driveway pavers needed replacing. Instead I called Living Water — when they finished, my walkways and drive looked better than new!"),
    ("Mason Carter", "Our company hired Living Water to clean up product sent to a job site. Naveed and his team were great to work with and made sure everything went smoothly."),
    ("Raaz Alakoozi", "Navid and his colleague power washed our driveway and backyard. Excellent job, excellent service and very professional. Would definitely recommend."),
    ("Shawn Vanderyagt", "Professional, personable and a service that performs beyond your expectations. I would highly recommend their services to every one of my customers."),
]

PROCESS = [
    ("Tell us the surface", "Two minutes on the form or one call: property type, service and postal code."),
    ("Free assessment", "Phone quote for straightforward residential work. Site visit for commercial, industrial and restoration projects."),
    ("Fixed written quote", "Method, scope, timing and price in writing — with our Certificate of Insurance and WSIB clearance."),
    ("We clean, you inspect", "Before and after photos on every job. Not happy? We come back and re-clean it for free."),
]

GENERAL_FAQ = [
    ("How quickly can Living Water start?", "Residential jobs are usually booked within 2–5 days, and same-week service is standard. Commercial and industrial clients get 24/7 emergency response on (647) 833-4343."),
    ("Are you licensed and insured?", "Yes. Living Water is fully licensed in Ontario, carries $5 million in commercial general liability insurance, is WSIB covered and ISSA-GBAC certified. We send a Certificate of Insurance to your property manager, condo board or HOA on request."),
    ("Will pressure washing damage my driveway, brick or siding?", "Not when it is done right. We match the pressure, nozzle, water temperature and chemistry to each surface — interlock, brick, vinyl, stucco, stone and wood all need different approaches. Where high pressure is wrong we soft wash, steam or use media blasting instead."),
    ("Do you do commercial and industrial work?", "Yes — refineries, plants, silos and tanks, heritage restoration, graffiti removal, sandblasting and elevator pit cleaning. Many of our clients are property managers, general contractors and municipalities. Our crews are certified boom and scissor lift operators."),
    ("What areas do you serve?", "Toronto and the entire Greater Toronto Area, including Mississauga, Brampton, Vaughan, Markham, Richmond Hill, Oakville, Burlington, Pickering, Ajax, Whitby and Oshawa, plus Hamilton, Niagara, Guelph, Cambridge, Barrie and Simcoe County."),
    ("Is the quote free?", "Yes. Assessments are free and no-obligation, and you receive a fixed written quote before any work starts."),
]

# ---------------------------------------------------------------- services
# Each service: slug -> dict
SERVICES = {}

def svc(slug, **kw):
    kw["slug"] = slug
    SERVICES[slug] = kw

svc("residential-power-washing",
    group="core", nav="Residential Power Washing", short="Residential",
    title="Residential Power Washing Toronto & GTA | Living Water",
    desc="Driveway, interlock, siding, deck, roof and brick cleaning for GTA homes — soft wash or pressure wash matched to each surface. Free quotes: (416) 663-8000.",
    h1="Residential Power Washing in Toronto & the GTA",
    sub="Your home's exterior, gently restored. Driveways, interlock, siding, decks and walkways washed back to the colour you bought.",
    hero="estate-home-driveway-washing", card="stone-patio-cleaning-after",
    card_text="Driveways, interlock, siding, decks and walkways washed back to the colour you bought.",
    answer="Living Water cleans the outside of homes across Toronto and the GTA — driveways, interlock, patios, brick, stone, stucco, siding, roofs, decks and fences — using low-pressure soft washing with biodegradable cleaners where high pressure would damage siding, mortar or window seals.",
    body="""
<p>Ontario weather is hard on a house. Road salt, spring pollen, summer algae and autumn leaves leave driveways stained, interlock green and brick dull. Residential power washing removes that build-up safely, restoring curb appeal and protecting the materials you paid for.</p>
<p>High pressure is not always the answer. It can strip sand from interlock joints, etch soft stone, blow out mortar and force water behind siding. Our technicians choose between soft washing, hot-water pressure washing and gentle media cleaning for each surface — the judgement that comes from washing 7,500+ properties since 1998.</p>
<h2>What we clean at your home</h2>
<ul class="ticks cols">
<li>Driveways, interlock and pavers</li><li>Patios, pool decks and coping</li><li>Exterior and interior brick</li><li>Stone, cement, limestone and precast</li><li>Stucco cleaning and soft wash treatments</li><li>Roofs: cedar, ceramic and metal</li><li>Gutters, siding and windows</li><li>Decks and fences</li><li>Efflorescence on walls, steps and stone</li><li>Sealant removal from pavers</li><li>Professional paint removal</li><li>Sandblasting for concrete and pools</li>
</ul>
<h2>Soft washing vs. pressure washing</h2>
<p><strong>Soft washing</strong> uses low pressure and biodegradable cleaners to dissolve algae, mildew and grime on siding, stucco and roofs. <strong>Pressure washing</strong> — often with hot water — lifts oil, tire marks and deep dirt from concrete and interlock. Most homes need both, and we tell you which surface gets which.</p>
<h2>Sealing after cleaning</h2>
<p>Once interlock, natural stone or pool coping is clean and dry, sealing can help it resist stains and fading. We will tell you honestly whether your surface benefits from a sealer.</p>
""",
    photos=["stone-patio-cleaning-before|stone-patio-cleaning-after", "estate-home-driveway-washing", "roof-moss-washing-ladder", "century-home-pressure-washing", "garden-stone-pathway-cleaned", "modern-stone-home-exterior-clean"],
    faqs=[("How often should I pressure wash my driveway?", "Most GTA homeowners wash driveways and interlock every one to two years, ideally in spring to remove winter salt and again if moss or oil stains appear."),
          ("Can you clean my roof without damaging shingles?", "Yes. Roofs are soft washed at low pressure with cleaners that kill moss and algae, so granules and shingles are not damaged. We clean cedar, ceramic and metal roofs."),
          ("Do I need to be home during the cleaning?", "Not usually. We need access to an outdoor water tap and the areas being cleaned. We send before and after photos when the job is complete."),
          ("Do you move patio furniture?", "Yes. Our crews move and replace patio furniture and protect plants, windows and nearby surfaces as part of the job.")],
    service_type="Residential pressure washing")

svc("commercial-power-washing",
    group="core", nav="Commercial Power Washing", short="Commercial",
    title="Commercial Pressure Washing Toronto & GTA | Living Water",
    desc="Commercial pressure washing for plazas, storefronts, parking garages, schools, restaurants and warehouses across the GTA. $5M insured, WSIB covered.",
    h1="Commercial Pressure Washing for GTA Properties",
    sub="Storefronts, plazas, parking garages, schools and warehouses cleaned on a schedule that works around your business.",
    hero="commercial-lobby-entrance-pressure-washing", card="commercial-building-exterior-washing",
    card_text="Plazas, storefronts, parking lots and garages cleaned on a schedule that suits your business.",
    answer="Living Water provides commercial pressure washing across Toronto and the GTA for retail plazas, office buildings, parking lots and garages, schools, restaurants, warehouses and construction sites — removing gum, grease, graffiti and stains while keeping the property open and safe.",
    body="""
<p>A clean property builds trust before a customer walks in. Living Water serves small businesses and large commercial organizations across Ontario, and many of our clients are property managers, condominium boards and facility managers who need dependable, insured contractors.</p>
<p>We specialise in removing stains, gum, graffiti and hazardous grease build-up, and in restoring brick and concrete. Work can be scheduled overnight or on weekends to avoid disrupting tenants and customers.</p>
<h2>Benefits of commercial power washing</h2>
<ul class="ticks">
<li><strong>Improved appearance</strong> — clean facades, walkways and entrances help attract customers and protect your reputation.</li>
<li><strong>Enhanced safety</strong> — removing grime, algae and grease helps prevent slips and falls.</li>
<li><strong>Longer surface life</strong> — regular cleaning slows deterioration and avoids costly repairs and replacement.</li>
</ul>
<h2>Commercial properties we clean</h2>
<div class="grid g2">
<div><h3>Construction sites & equipment</h3><p>Mud, dirt and debris removed from sites, hoarding and heavy machinery.</p></div>
<div><h3>Warehouses & factories</h3><p>Indoor and outdoor washing of floors, walls and loading areas.</p></div>
<div><h3>Parking lots & garages</h3><p>Oil, salt and grime lifted from stalls, ramps, curbs and walls.</p></div>
<div><h3>Schools</h3><p>Exterior surfaces, entrances and playgrounds cleaned safely.</p></div>
<div><h3>Restaurants</h3><p>Patios, sidewalks, dumpster pads and grease-stained areas.</p></div>
<div><h3>Plazas & shared buildings</h3><p>Sidewalks, walls, storefronts and common areas.</p></div>
</div>
""",
    photos=["commercial-building-exterior-washing", "parking-lot-pressure-washing-crew", "brick-storefront-boom-lift-washing", "condo-column-pressure-washing", "rooftop-terrace-pressure-washing-crew", "commercial-column-restoration"],
    faqs=[("Can you work after hours?", "Yes. We regularly schedule commercial work overnight and on weekends so tenants, shoppers and staff are not disrupted."),
          ("Do you provide a Certificate of Insurance?", "Yes. We carry $5 million commercial general liability and full WSIB coverage, and send a COI and WSIB clearance with every quote."),
          ("Can you set up a maintenance schedule?", "Yes. Many property managers book seasonal or monthly cleaning for entrances, garages and walkways.")],
    service_type="Commercial pressure washing")

svc("industrial-power-washing",
    group="core", nav="Industrial Power Washing", short="Industrial",
    title="Industrial Pressure Washing & Hydro Jetting | Living Water",
    desc="Industrial pressure washing and hydro jetting for plants, silos, tanks, food facilities and heavy equipment across Ontario. 24/7 emergency response.",
    h1="Industrial Pressure Washing & Hydro Jetting",
    sub="Plants, silos, tanks, food facilities and heavy equipment cleaned safely — from blasting condenser pipes to restoring a whole facility.",
    hero="industrial-pressure-washing-crew-gta", card="silo-tank-exterior-cleaning-boom-lift",
    card_text="Hydro jetting, tank and silo cleaning, and degreasing for plants and heavy equipment.",
    answer="Living Water provides industrial pressure washing and hydro jetting across Ontario — cleaning silos and tanks inside and out, manufacturing and food plants, bridges and dams, condenser pipes and heavy equipment — with safety-first planning and 24/7 emergency response.",
    body="""
<p>Industrial cleaning demands more than horsepower. It needs a plan that protects your people, your equipment and your production schedule. The Living Water team has extensive experience with the unique requirements of industrial cleaning and remediation, and health and safety come first on every site.</p>
<p>Keeping equipment and machinery clean keeps it running smoothly and extends its working life. We work with you to build a cleaning schedule that is safe for your business, your employees and your workplace.</p>
<h2>Our industrial services</h2>
<ul class="ticks cols">
<li>Silo and tank cleaning, exterior and interior</li><li>Industrial plant pressure washing and sanitation</li><li>Food plant sanitation and disinfection</li><li>Manufacturing facility cleaning</li><li>Hydro jetting of condenser pipes and lines</li><li>Heavy equipment and crane degreasing</li><li>Bridges and dams — sandblasting or pressure washing</li><li>Mould remediation on equipment and facilities</li><li>Professional paint and coating removal</li>
</ul>
<h2>Certified for work at height</h2>
<p>Our technicians are certified boom and scissor lift operators, so tall tanks, silos and facades can be cleaned without scaffolding delays.</p>
""",
    photos=["silo-tank-exterior-cleaning-boom-lift", "silo-tank-wash-progress", "industrial-tank-pressure-washing", "crane-heavy-equipment-washing", "crane-track-degreasing", "industrial-pressure-washing-crew-gta"],
    faqs=[("What is hydro jetting?", "Hydro jetting uses very high-pressure water streams to scour build-up from the inside of pipes, condensers and lines without abrasive media."),
          ("Do you offer emergency industrial cleaning?", "Yes. Industrial and commercial clients can reach our 24/7 emergency line at (647) 833-4343."),
          ("Can you clean food processing plants?", "Yes. We provide pressure washing, sanitation and disinfection for food plants, scheduled around production.")],
    service_type="Industrial pressure washing")

svc("sandblasting-services",
    group="core", nav="Sandblasting & Media Blasting", short="Sandblasting",
    title="Sandblasting & Media Blasting Toronto | Living Water",
    desc="Mobile dustless sandblasting, micro, soda and dry ice blasting for rust, paint, epoxy and pool prep across Toronto and the GTA. Free quotes.",
    h1="Sandblasting & Dustless Media Blasting in Toronto",
    sub="The efficient way to strip rust, scale, stains and old coatings and prepare surfaces for painting.",
    hero="dustless-sandblasting-concrete", card="media-blasting-stone-technician",
    card_text="High-CFM to micro blasting for rust, paint and coating removal and surface preparation.",
    answer="Living Water offers mobile dustless sandblasting, wet and dry abrasive blasting, micro blasting, soda blasting and dry ice blasting across Toronto and the GTA to remove rust, scale, paint and epoxy from steel, aluminium, brick, concrete and pools.",
    body="""
<p>Sandblasting — also called abrasive blasting — drives a high-pressure stream of media against a surface to remove rust, scale, stains and old paint. It is the fastest way to prepare metal, masonry and concrete for painting, coating or other treatments.</p>
<p>We work for general contractors, pool painting companies, fire restoration firms, renovation and maintenance companies, and residential, commercial and industrial property owners. Our team can explain why a particular blasting method will — or will not — suit your project.</p>
<h2>Why choose dustless blasting</h2>
<ul class="ticks">
<li><strong>Efficient and effective</strong> — removes rust, scale, stains and old coatings quickly, leaving a clean profile ready for treatment.</li>
<li><strong>Versatile</strong> — steel and aluminium, brick facades, concrete pool shells, machinery, bridges, tanks, and water and sewage plants.</li>
<li><strong>Environmentally responsible</strong> — dustless technology keeps airborne dust down and uses environmentally friendly media.</li>
</ul>
<h2>Blasting services</h2>
<div class="grid g2">
<div><h3>Abrasive blasting</h3><p>Removes rust, scale, stains and old paint from a wide range of surfaces.</p></div>
<div><h3>Aluminium & steel blasting</h3><p>Media and pressure matched to metal so the substrate is not damaged.</p></div>
<div><h3>Wet & dry sandblasting</h3><p>Chosen per surface — wet blasting controls dust on sensitive sites.</p></div>
<div><h3>Dry ice blasting</h3><p>Lifts coatings and residue without abrasive media or secondary waste.</p></div>
<div><h3>Pool repainting prep</h3><p>Concrete pool shells blasted clean and ready to repaint.</p></div>
<div><h3>Epoxy coating removal</h3><p>Old epoxy floors and coatings stripped back to sound concrete.</p></div>
</div>
""",
    photos=["dustless-sandblasting-concrete", "media-blasting-stone-technician", "heritage-building-contained-blasting", "paint-stripping-wall-surface"],
    faqs=[("Is sandblasting safe for brick?", "It can be, with the right media and pressure. Soft or heritage brick often needs micro blasting or soda blasting instead of sand. We assess first and test a small area."),
          ("What is dustless sandblasting?", "Dustless blasting mixes water with the abrasive media so dust is captured at the surface, making it cleaner and safer for occupied or urban sites."),
          ("Do you blast swimming pools?", "Yes. We blast concrete pool shells to remove failing paint so they can be repainted.")],
    service_type="Sandblasting")

svc("brick-cleaning-paint-removal",
    group="core", nav="Brick Cleaning & Paint Removal", short="Brick & Paint",
    title="Brick Cleaning & Paint Removal Toronto | Living Water",
    desc="Brick cleaning, acid washing and paint removal for homes and commercial buildings in Toronto & the GTA — without damaging brick, mortar or windows.",
    h1="Brick Cleaning & Paint Removal in Toronto",
    sub="Professional brick cleaning and paint stripping without unnecessary damage to brick, mortar, windows or landscaping.",
    hero="brick-wall-paint-removal-pressure-washing", card="brick-masonry-house-cleaning-after",
    card_text="Patient, technology-led brick cleaning and paint removal — because masonry damage can't be undone.",
    answer="Living Water cleans brick and removes paint from interior and exterior masonry across Toronto and the GTA, choosing between chemical cleaning, controlled pressure washing and abrasive blasting after assessing the brick and the coating — so mortar, windows and plants are protected.",
    body="""
<p>Brick collects years of dirt, staining, paint, efflorescence and other build-up. Removing it is not simply a matter of more pressure — the wrong method can scar brick faces, wash out mortar, etch glass and kill landscaping. Once that damage is done, there is no going back.</p>
<p>That is why we assess the brick and the material to be removed before selecting a cleaning, chemical or blasting method — and always neutralise acid washes properly.</p>
<h2>Brick cleaning & paint removal services</h2>
<ul class="ticks cols">
<li>Exterior brick cleaning</li><li>Interior brick cleaning</li><li>Brick paint removal</li><li>Old coating removal</li><li>Dirt and grime removal</li><li>Efflorescence removal</li><li>Brick stain removal</li><li>Chemical brick cleaning and acid washing</li><li>Sandblasting and abrasive blasting where appropriate</li><li>Brick restoration and surface preparation</li>
</ul>
""",
    photos=["commercial-brick-paint-removal-before|commercial-brick-paint-removal-after", "painted-building-paint-removal-before|painted-building-paint-removal-after", "brick-masonry-house-cleaning-before|brick-masonry-house-cleaning-after", "brick-arch-window-cleaning", "yellow-brick-wall-cleaning", "brick-wall-cleaning-technician"],
    faqs=[("Can paint be removed from brick without damaging it?", "In most cases, yes. We use chemical strippers and controlled low-pressure rinsing, or gentle media blasting for stubborn coatings, after testing a small area."),
          ("What is a brick acid wash?", "An acid wash dissolves mortar smears and mineral stains from new or old brick. It must be correctly diluted, tested and neutralised to avoid burning the brick."),
          ("Do you clean interior brick?", "Yes — interior brick walls and fireplaces can be cleaned with low-moisture methods and full protection of the room.")],
    service_type="Brick cleaning and paint removal")

svc("historical-remediation",
    group="core", nav="Historical Remediation", short="Heritage",
    title="Heritage Building Restoration Toronto | Living Water",
    desc="Heritage masonry cleaning, lead paint removal, soda blasting and steam cleaning for historic buildings, statues and landmarks in Toronto since 1998.",
    h1="Historical Remediation & Heritage Facade Restoration",
    sub="Respectful cleaning and restoration for historic buildings, statues and landmarks across Toronto and Ontario.",
    hero="heritage-stone-wall-pressure-washing-toronto", card="heritage-facade-restoration-after",
    card_text="Soda blasting, steam cleaning and lead paint removal for century-old buildings and landmarks.",
    answer="Living Water restores historic buildings, statues and landmarks in Toronto and Ontario using heritage-appropriate methods — steam cleaning, soda and micro blasting, wet and dry sandblasting, and lead paint removal — with a working knowledge of the brick, stone and metals used in Canadian construction over the past century.",
    body="""
<p>Historic buildings and landmarks are part of our shared heritage. Over time they suffer from pollution, failed coatings, efflorescence and deterioration, and restoring them is far more involved than a repaint. It requires a firm grasp of the construction and artistic materials used in Canada over the last hundred years.</p>
<p>Our technicians approach every heritage project with respect and care, choosing the gentlest method that will work and testing before scaling up.</p>
<h2>Historical remediation services</h2>
<ul class="ticks cols">
<li>Restoration of historical buildings</li><li>Cleaning statues and landmarks</li><li>Lead paint removal</li><li>Exterior paint removal from all surfaces</li><li>Brick cleaning and brick restoration</li><li>Natural stone restoration and cleaning</li><li>Efflorescence removal</li><li>Steam cleaning</li><li>Wet and dry sandblasting</li><li>Aluminium and copper restoration</li>
</ul>
<h2>Notable project: the U.S. Consulate in Toronto</h2>
<p>One of our notable heritage projects was the U.S. diplomatic building in Toronto. Its exterior combined brick, limestone, concrete, precast, granite, aluminium and glass — each needing its own cleaning approach while protecting the building's historical integrity.</p>
""",
    photos=["heritage-facade-restoration-before|heritage-facade-restoration-after", "heritage-stone-wall-pressure-washing-toronto", "historical-building-remediation-ontario", "heritage-building-scaffolding-restoration", "yellow-brick-heritage-building-cleaning", "heritage-red-brick-building-cleaning", "ornamental-balcony-stone-restoration"],
    faqs=[("Which cleaning methods are safe for heritage masonry?", "Usually the gentlest effective method: low-pressure steam, poultices, soda or micro blasting at low pressure, and carefully tested chemical cleaners. High-pressure water and coarse sand are avoided on soft historic brick and stone."),
          ("Can you remove lead paint?", "Yes. We remove lead-based paint from historic surfaces with containment and safe handling and disposal of waste."),
          ("Do you work with heritage consultants?", "Yes. We regularly work alongside architects, heritage conservators and general contractors and can complete test panels for approval.")],
    service_type="Historic building restoration")

svc("disaster-restoration",
    group="core", nav="Disaster Restoration", short="Disaster",
    title="Fire, Water & Wind Damage Restoration Toronto | Living Water",
    desc="24/7 fire, smoke, water, wind and mould damage restoration across Toronto and the GTA. Emergency securing, extraction, drying and rebuild. Call (647) 833-4343.",
    h1="Fire, Water & Wind Damage Restoration",
    sub="24/7 emergency response to secure, clean and restore your home or business after fire, flood, storm or mould.",
    hero="wind-damage-deck-tree", card="wind-damage-deck-tree",
    card_text="24/7 fire, smoke, water, wind and mould damage response and restoration.",
    answer="Living Water provides 24/7 disaster restoration across Toronto and the GTA — fire and smoke damage cleaning, water extraction and drying, wind and storm damage securing and repair, and mould remediation — restoring homes and businesses to their pre-loss condition. Emergency line: (647) 833-4343.",
    body="""
<p>When disaster strikes, every hour counts. Our team moves quickly to assess the damage, secure the property and start recovery — from a small kitchen fire to major storm damage.</p>
<h2>Fire damage restoration</h2>
<ol class="ticks">
<li><strong>Inspection and evaluation</strong> — a full walkthrough to assess structure, electrical and smoke- or soot-affected zones.</li>
<li><strong>Securing the property</strong> — boarding windows and entryways to stop weather exposure and unauthorized access.</li>
<li><strong>Smoke and soot remediation</strong> — removing particles that degrade air quality and keep damaging surfaces.</li>
<li><strong>Rebuilding and restoration</strong> — structural repairs, drywall and finishing once the property is safe.</li>
</ol>
<h2>Water damage restoration</h2>
<p>Floods, leaks, burst pipes and failed appliances escalate quickly into mould and structural damage. We find and stop the source, extract standing water with industrial pumps and vacuums, dry walls, floors and ceilings with commercial dehumidifiers, then repair drywall, flooring and structural elements.</p>
<h2>Wind & storm damage restoration</h2>
<p>We inspect for torn roofing, broken windows, stripped siding and hidden structural damage; tarp roofs and board openings to stop water getting in; complete permanent repairs; and recommend upgrades that make the property more resilient to the next storm.</p>
<h2>Mould removal & remediation</h2>
<p>Our technicians locate visible and hidden mould and the moisture behind it, contain the area with negative air pressure and barriers, remove affected materials, treat surfaces with EPA-approved antimicrobials, and restore the space.</p>
""",
    photos=["wind-damage-deck-tree", "paint-stripping-wall-surface", "heritage-building-scaffolding-restoration"],
    faqs=[("Do you respond to emergencies at night or on weekends?", "Yes. Our emergency line, (647) 833-4343, is answered 24/7 for fire, water, wind and commercial emergencies."),
          ("Do you work with insurance claims?", "We document damage with photos and written scopes that you can provide to your insurer. Contact your insurance company as soon as possible after a loss."),
          ("How fast must water damage be dried?", "As soon as possible. Mould can begin growing within 24–48 hours, which is why extraction and drying start immediately.")],
    service_type="Disaster restoration")

svc("elevator-pit-cleaning",
    group="special", nav="Elevator Pit Cleaning", short="Elevator Pits",
    title="Elevator Pit Cleaning Toronto & GTA | Condos & Buildings",
    desc="Elevator pit cleaning for condos and commercial buildings in Toronto & the GTA: water, oil, sludge and debris removal, after hours, COI + WSIB, 24/7.",
    h1="Elevator Pit Cleaning for Condos & Commercial Buildings",
    sub="Winter is pit season. Salt slush, meltwater and debris end up in your elevator pits — we clean, pump and sanitize them after hours, with the paperwork property managers need.",
    hero="elevator-pit-cleaning-toronto", card="elevator-pit-pressure-washing",
    card_text="Water, oil, sludge and debris removed — the trusted referral of large GTA elevator companies.",
    answer="Living Water cleans elevator pits for condominium corporations, property managers and commercial buildings across Toronto and the GTA — removing debris, standing water, oil, sludge and sewage, then pressure washing, sanitizing and deodorizing the pit. Work is coordinated with your elevator contractor, scheduled after hours, and documented with before-and-after photos. Emergency line: (647) 833-4343, 24/7.",
    body="""
<h2>Why winter is elevator pit season</h2>
<p>From December to April, GTA buildings track in snow, slush and road salt every day. Meltwater runs through door sills and into the hoistway, salt and grit settle in the pit, and freeze-thaw cycles and spring melt push groundwater through cracks and failing sumps. Left alone, that mix becomes corrosive sludge around buffers, rails and pit equipment — and a slip hazard for the mechanics who have to work there.</p>
<ul class="ticks"><li>Salt-laden meltwater corrodes pit steel, buffers and rail brackets</li><li>Wet debris and garbage become a fire and odour problem</li><li>Groundwater seepage and sump failures peak during thaws</li><li>Frozen and burst pipes flood lower levels and pits</li></ul>
<h2>Built for condo boards and property managers</h2>
<div class="grid g2">
<div><h3>Paperwork ready</h3><p>Certificate of Insurance ($5M CGL) and WSIB clearance sent with every quote — ready for your contractor files.</p></div>
<div><h3>Coordinated with your elevator contractor</h3><p>We schedule with your elevator company so the car is taken out of service and locked out safely before anyone enters the pit.</p></div>
<div><h3>After-hours & minimal downtime</h3><p>Overnight, early-morning and weekend scheduling keeps residents and tenants moving. Most routine pits are done in a single visit.</p></div>
<div><h3>Photo report for your records</h3><p>Before-and-after photos of every pit for board reports, reserve-fund studies, warranty claims and insurance.</p></div>
<div><h3>Multi-building portfolios</h3><p>One contractor for every building in your portfolio, with seasonal or recurring programs.</p></div>
<div><h3>Trusted by elevator companies</h3><p>Some of Ontario's leading elevator service providers refer their most difficult pits to us — oil spills, floods and sewage backups.</p></div>
</div>
<h2>What's included</h2>
<ul class="ticks cols"><li>Debris, garbage and dust removal</li><li>Standing water pump-out</li><li>Sludge and salt residue removal</li><li>Oil and hydraulic fluid spill clean-up</li><li>Proper disposal of oily and hazardous waste</li><li>Pressure washing and degreasing</li><li>Sanitizing and deodorizing</li><li>Sewage backup clean-up</li><li>Crack repair</li><li>Elevator pit painting</li></ul>
<h2>How a pit cleaning works</h2>
<ol class="ticks"><li><strong>Quote</strong> — send the number of elevators, pit photos if you have them, and the building address. Fixed written price.</li><li><strong>Schedule</strong> — we book a time with you and your elevator contractor, often after hours.</li><li><strong>Lock-out</strong> — the elevator contractor takes the car out of service and secures it.</li><li><strong>Clean</strong> — debris and water removed, oil and sludge cleaned up, pit washed, degreased and sanitized.</li><li><strong>Report</strong> — before-and-after photos and notes on anything we see, such as leaks, cracks or sump issues.</li></ol>
<h2>Standards and warranty context in Ontario</h2>
<p>Elevating devices in Ontario are regulated by the Technical Standards and Safety Authority (TSSA) under the CSA B44 safety code. TSSA's elevator pre-inspection checklist calls for permanent means to prevent groundwater accumulating in the pit, and for sumps in pits to be covered. For newer condominiums, Tarion's construction performance guidelines state that elevator pits should be clear of standing water or fluids and cleaned of construction debris after construction — useful to document during first-year warranty inspections.</p>
<p>Your elevator contractor remains responsible for the equipment itself; Living Water handles the cleaning, pumping and sanitizing so the pit stays clean, dry and safe to work in.</p>
<h2>Buildings we serve</h2>
<ul class="ticks cols"><li>Condominium towers and townhouse complexes</li><li>Rental apartment buildings</li><li>Office towers and commercial buildings</li><li>Retail plazas and shopping centres</li><li>Hospitals, schools and institutions</li><li>Industrial and warehouse facilities</li></ul>
<h2>Elevator pit cleaning across the GTA</h2>
<p>We clean elevator pits in condominium towers and commercial buildings across <a href="/pressure-washing-toronto/">downtown Toronto</a>, <a href="/pressure-washing-north-york/">North York</a> along the Yonge corridor, <a href="/pressure-washing-etobicoke/">Etobicoke</a>'s Humber Bay Shores, <a href="/pressure-washing-scarborough/">Scarborough</a>, <a href="/pressure-washing-mississauga/">Mississauga</a> City Centre, <a href="/pressure-washing-vaughan/">Vaughan</a> Metropolitan Centre, <a href="/pressure-washing-markham/">Markham</a>, <a href="/pressure-washing-richmond-hill/">Richmond Hill</a>, <a href="/pressure-washing-oakville/">Oakville</a>, <a href="/pressure-washing-burlington/">Burlington</a> and <a href="/pressure-washing-hamilton/">Hamilton</a>.</p>
<p><strong>Water in a pit right now?</strong> See <a href="/elevator-pit-water-removal/">emergency elevator pit water removal</a> or call <a href="tel:+1-647-833-4343">(647) 833-4343</a>, 24/7.</p>
""",
    photos=["elevator-pit-cleaning-toronto", "elevator-pit-pressure-washing", "elevator-pit-buffer-cleaning", "elevator-pit-springs-cleaned", "condo-column-pressure-washing", "commercial-building-exterior-washing"],
    faqs=[("How often should a condo clean its elevator pits?", "At least once a year, and more often in high-traffic buildings. Many property managers book a cleaning after winter to remove salt and meltwater residue, and immediately after any flood, leak or sewage backup."),
          ("Who is responsible for cleaning the elevator pit?", "The building owner or property manager usually arranges pit cleaning. The elevator contractor maintains the equipment and controls access, so the cleaning is coordinated with them."),
          ("Do you work after hours?", "Yes. We regularly schedule overnight, early-morning and weekend pit cleaning so residents and tenants are not inconvenienced."),
          ("How long is the elevator out of service?", "Routine pit cleaning is usually completed in a few hours per elevator. Flood, oil or sewage clean-ups take longer depending on volume and disposal."),
          ("Do you provide insurance and WSIB documents?", "Yes. We send our Certificate of Insurance ($5M commercial general liability) and WSIB clearance with every quote."),
          ("Can you clean pits in multiple buildings?", "Yes. We set up one-time, seasonal or recurring programs across property management portfolios in Toronto and the GTA."),
          ("What causes water in an elevator pit?", "Common causes are groundwater seepage, failed sump pumps, meltwater and salt slush tracked in during winter, sprinkler discharge, burst pipes and floor-washing water entering the hoistway.")],
    service_type="Elevator pit cleaning")

svc("elevator-pit-water-removal",
    group="special", nav="Elevator Pit Water Removal", short="Emergency",
    title="Water in Elevator Pit? 24/7 Pump-Out & Clean-Up | GTA",
    desc="Emergency elevator pit water removal in Toronto & the GTA: 24/7 pump-out, sludge, oil and sewage clean-up with photo documentation. Call (647) 833-4343.",
    h1="Emergency Elevator Pit Water Removal — 24/7",
    sub="Flooded pit, sewage backup or oil spill? We pump it out, clean it up and document it so your elevator contractor can get the car back in service.",
    hero="elevator-pit-pressure-washing", card="elevator-pit-buffer-cleaning",
    card_text="24/7 pump-out, sludge, oil and sewage clean-up for flooded elevator pits.",
    answer="If an elevator pit has standing water, take the elevator out of service, call your elevator contractor, and call Living Water's 24/7 line at (647) 833-4343. We pump out the water, remove sludge, oil and debris, sanitize after sewage backups, and provide before-and-after photos for your records and insurance.",
    body="""
<h2>What to do right now</h2>
<ol class="ticks"><li><strong>Stop using the elevator.</strong> TSSA warns never to use elevators in a flooded building or where water has leaked onto elevator components.</li><li><strong>Call your elevator contractor</strong> to take the car out of service and assess the equipment.</li><li><strong>Find and stop the source</strong> if it is safe to do so — a burst pipe, sprinkler, sump or roof drain.</li><li><strong>Call Living Water 24/7</strong> on (647) 833-4343 for pump-out and clean-up.</li><li><strong>Take photos</strong> and notify your insurer if damage is significant.</li></ol>
<h2>What we do</h2>
<ul class="ticks cols"><li>Pump out standing water</li><li>Remove sludge, silt and debris</li><li>Contain and clean up oil and hydraulic fluid</li><li>Dispose of contaminated water and waste properly</li><li>Clean and sanitize after sewage backups</li><li>Pressure wash and deodorize the pit</li><li>Photo documentation for insurance and the board</li><li>Notes on leaks, cracks or sump problems we find</li></ul>
<h2>Common causes of a flooded pit</h2>
<ul class="ticks"><li>Groundwater seepage during thaws and heavy rain</li><li>Failed or undersized sump pumps</li><li>Burst or frozen pipes and sprinkler discharge</li><li>Salt slush and meltwater tracked in during winter</li><li>Floor-washing water running into the hoistway</li><li>Sewer backups into lower levels</li></ul>
<h2>Preventing the next one</h2>
<p>TSSA's pre-inspection checklist calls for permanent means to prevent groundwater accumulating in pits. Talk to your elevator contractor and building engineer about sump capacity, drains and sealing cracks — and book a routine pit cleaning after winter so problems are spotted early.</p>
""",
    photos=["elevator-pit-pressure-washing", "elevator-pit-cleaning-toronto", "elevator-pit-springs-cleaned"],
    faqs=[("Is it safe to use an elevator with water in the pit?", "No. Take it out of service and have your elevator contractor inspect it. TSSA advises never using elevators in a flooded building or where water has reached elevator components."),
          ("How fast can you respond?", "Our emergency line, (647) 833-4343, is answered 24/7 for commercial and condominium clients across the GTA."),
          ("Do you handle sewage in elevator pits?", "Yes. We remove sewage-contaminated water and debris, then clean, sanitize and deodorize the pit.")],
    service_type="Elevator pit water removal")

svc("efflorescence-removal",
    group="special", nav="Efflorescence Removal", short="Efflorescence",
    title="Efflorescence Removal Toronto & GTA | Living Water",
    desc="White efflorescence and mineral deposits removed from brick, stone, concrete and interlock in the GTA. Warranty provider for Ontario stone makers.",
    h1="Efflorescence Removal for Brick, Stone & Masonry",
    sub="White, powdery mineral deposits removed safely from brick, stone, concrete and interlock.",
    hero="efflorescence-removal-front-steps-after", card="efflorescence-removal-front-steps-after",
    card_text="Trusted as the exclusive warranty service provider for many Ontario stone manufacturers.",
    answer="Efflorescence is the white, powdery salt deposit left when moisture moves through masonry and evaporates. Living Water removes it from brick, natural stone, concrete and interlock across Toronto and the GTA, and is trusted as the warranty service provider for many Ontario stone manufacturers.",
    body="""
<p>Living Water has an extensive track record fixing new and old efflorescence problems. We assess the material first and choose the right cleaning method rather than treating every surface the same — especially important for older brick, stone and heritage masonry, where aggressive cleaning causes damage.</p>
<h2>Efflorescence services</h2>
<ul class="ticks cols">
<li>Brick efflorescence removal</li><li>Stone efflorescence removal</li><li>Concrete and interlock mineral deposit removal</li><li>Exterior wall and facade cleaning</li><li>Chemical cleaning where appropriate</li><li>Controlled pressure washing</li><li>Final rinsing and surface clean-up</li>
</ul>
<h2>Will efflorescence come back?</h2>
<p>It can return if moisture keeps moving through the material. New masonry often blooms for a season while it cures. We explain the cause on your property and the right approach — including when sealing helps.</p>
""",
    photos=["efflorescence-removal-front-steps-before|efflorescence-removal-front-steps-after", "precast-stone-coping-cleaning", "concrete-surface-cleaning-residue-removal"],
    faqs=[("What causes efflorescence?", "Water dissolves salts inside brick, mortar, concrete or stone, carries them to the surface and evaporates, leaving a white crystalline deposit."),
          ("Can pressure washing alone remove efflorescence?", "Light, fresh efflorescence sometimes brushes or rinses off, but established deposits usually need a suitable masonry cleaner followed by controlled rinsing."),
          ("Is efflorescence covered by my stone warranty?", "Many Ontario stone and paver manufacturers use Living Water as their warranty service provider. Check with your supplier or contact us.")],
    service_type="Efflorescence removal")

svc("graffiti-removal",
    group="special", nav="Graffiti Removal", short="Graffiti",
    title="Graffiti Removal Toronto & GTA | Living Water",
    desc="Same-week graffiti removal from brick, stone, concrete, metal and glass across Toronto and the GTA, plus anti-graffiti coatings. Call (416) 663-8000.",
    h1="Graffiti Removal Without Damaging the Surface",
    sub="Same-week tag removal from brick, concrete, stone, metal, glass and painted surfaces — plus anti-graffiti coatings.",
    hero="graffiti-removal-house-wall", card="graffiti-removal-house-wall",
    card_text="Same-week removal from brick, concrete, glass and painted surfaces, plus anti-graffiti coating.",
    answer="Living Water removes graffiti from brick, concrete, stone, metal and glass across Toronto and the GTA — usually within the same week — using bio-friendly chemical removers and controlled pressure washing selected for the surface, and can apply anti-graffiti coatings afterwards.",
    body="""
<p>Graffiti changes how people see your building — and removing it is not just a matter of pressure. The wrong method leaves ghosting or damages brick, stone and concrete. We look at the surface, the type of paint or marker and the condition of the material before choosing a method.</p>
<h2>Graffiti removal services</h2>
<ul class="ticks cols">
<li>Brick graffiti removal</li><li>Concrete graffiti removal</li><li>Stone graffiti removal</li><li>Metal surface graffiti removal</li><li>Paint and marker removal</li><li>Chemical graffiti removal</li><li>Controlled pressure washing</li><li>Anti-graffiti coatings</li>
</ul>
<p>We serve commercial, residential, institutional and industrial properties, including municipalities and property managers who need fast turnaround.</p>
""",
    photos=["graffiti-removal-house-wall", "brick-wall-cleaning-technician", "brick-wall-low-pressure-wash"],
    faqs=[("How fast can graffiti be removed?", "We typically remove graffiti within the same week, and sooner for offensive tags or commercial clients."),
          ("Will the wall show a shadow afterwards?", "Fresh graffiti removed with the right chemistry usually leaves no trace. Older tags on porous brick can leave light ghosting, which we minimise with poultices or gentle blasting."),
          ("What is an anti-graffiti coating?", "A clear protective coating that makes future graffiti easier to remove without damaging the surface underneath.")],
    service_type="Graffiti removal")

svc("stone-restoration",
    group="special", nav="Stone Restoration", short="Stone",
    title="Stone Cleaning & Restoration Toronto | Living Water",
    desc="Natural stone cleaning and restoration — marble, granite, limestone, sandstone and precast — for homes, commercial and heritage properties in the GTA.",
    h1="Stone Cleaning & Restoration",
    sub="Marble, granite, limestone, sandstone, natural stone and precast brought back to life without damage.",
    hero="ornamental-balcony-stone-restoration", card="stone-house-exterior-cleaning",
    card_text="Marble, granite, limestone, sandstone and precast restored without damaging the surface.",
    answer="Living Water cleans and restores natural stone — marble, granite, limestone, sandstone and precast — on homes, commercial buildings and heritage properties across Toronto and the GTA, removing stains, mineral deposits and organic growth with methods matched to the stone.",
    body="""
<p>Stone collects dirt, stains, mineral deposits and organic growth over time, and heavy-handed cleaning can permanently damage it — especially older or softer stone. Living Water has built a reputation for bringing old, discoloured stone back to life.</p>
<h2>Stone restoration services</h2>
<ul class="ticks cols">
<li>Natural stone cleaning</li><li>Stone stain removal</li><li>Dirt and surface build-up removal</li><li>Stone facade cleaning</li><li>Walkway and patio stone cleaning</li><li>Mineral deposit removal</li><li>Surface restoration</li><li>Stone sealing where appropriate</li><li>Monument cleaning</li>
</ul>
<p>Every stone is different, so we assess the material before starting. From a small residential patio to a large commercial or heritage facade, we recommend the right approach.</p>
""",
    photos=["ornamental-balcony-stone-restoration", "limestone-wall-hand-cleaning", "stone-house-exterior-cleaning", "precast-stone-coping-cleaning", "modern-stone-home-exterior-cleaning"],
    faqs=[("Can you clean limestone and marble safely?", "Yes. Soft, acid-sensitive stones like limestone and marble are cleaned with pH-appropriate products and low pressure — never harsh acids."),
          ("Should natural stone be sealed?", "Often, yes — especially patios and pool coping. Sealing helps resist staining. We advise based on the stone type and use."),
          ("Do you clean monuments and statues?", "Yes. Monuments, memorials and statues are cleaned with gentle, conservation-appropriate methods.")],
    service_type="Stone restoration")

svc("metal-restoration",
    group="special", nav="Metal Restoration", short="Metal",
    title="Metal Restoration & Rust Removal Toronto | Living Water",
    desc="Rust and oxidation removal, coating stripping and surface preparation for steel, stainless, aluminium and copper across Toronto and the GTA.",
    h1="Metal Restoration, Rust Removal & Surface Preparation",
    sub="Stainless steel, copper and aluminium cleaned, de-rusted and prepared so they look new again.",
    hero="industrial-tank-pressure-washing", card="crane-track-degreasing",
    card_text="Stainless steel, copper and aluminium cleaned, de-rusted and prepared for coating.",
    answer="Living Water restores metal surfaces across Toronto and the GTA — removing rust, oxidation, old paint and coatings from steel, stainless steel, aluminium and copper — using cleaning, sandblasting or media blasting chosen for the metal and the finish required.",
    body="""
<p>Stainless steel, copper and aluminium are durable, but all need maintenance to keep looking new. Rust, oxidation, old paint and grime affect both appearance and condition.</p>
<p>For some projects, blasting or another specialised method is better than standard pressure washing. With sandblasting and media blasting in-house, we select the approach based on the surface and the result you want.</p>
<h2>Metal restoration services</h2>
<ul class="ticks cols">
<li>Rust removal</li><li>Oxidation removal</li><li>Metal surface cleaning</li><li>Old coating removal</li><li>Paint removal</li><li>Surface preparation for coating</li><li>Copper and aluminium restoration</li><li>Sandblasting where appropriate</li>
</ul>
""",
    photos=["industrial-tank-pressure-washing", "crane-track-degreasing", "crane-heavy-equipment-washing"],
    faqs=[("Can you remove rust without damaging the metal?", "Yes. We select the blasting media and pressure to suit the metal so the substrate is cleaned without unnecessary profile or thinning."),
          ("Do you restore architectural copper and aluminium?", "Yes — including heritage copper and aluminium elements on historic buildings.")],
    service_type="Metal restoration")

SERVICE_ORDER_CORE = ["residential-power-washing", "commercial-power-washing", "industrial-power-washing", "sandblasting-services", "brick-cleaning-paint-removal", "historical-remediation", "disaster-restoration"]
SERVICE_ORDER_SPECIAL = ["elevator-pit-cleaning", "efflorescence-removal", "graffiti-removal", "stone-restoration", "metal-restoration"]

GALLERY_PAIRS = [
    ("heritage-facade-restoration-before", "heritage-facade-restoration-after", "Heritage facade, soda blast", "Gentle media cleaning on a century-old Toronto building entrance."),
    ("efflorescence-removal-front-steps-before", "efflorescence-removal-front-steps-after", "Efflorescence removal", "Mineral deposits removed from precast front steps."),
    ("brick-masonry-house-cleaning-before", "brick-masonry-house-cleaning-after", "Brick masonry cleaning", "Mortar smears and grime cleaned from a new brick home."),
    ("commercial-brick-paint-removal-before", "commercial-brick-paint-removal-after", "Commercial paint removal", "Patchy paint stripped from a commercial brick facade."),
    ("stone-patio-cleaning-before", "stone-patio-cleaning-after", "Stone patio & loggia", "Residential stone patio cleaned back to its original colour."),
    ("boat-deck-mobile-power-wash-before", "boat-deck-mobile-power-wash-after", "Mobile power wash, boat deck", "Our mobile unit cleaning a sailboat deck."),
    ("painted-building-paint-removal-before", "painted-building-paint-removal-after", "Paint stripping, downtown Toronto", "Painted masonry stripped to reveal the original brick."),
]

# Spring campaign (switch on in March): SEASONAL = dict(on=True, text="🌱 Spring cleaning season: driveways, interlock & salt damage clean-up", link="/residential-power-washing/", cta="Get a quote")
SEASONAL = dict(on=True, text="❄ Winter booking now open: elevator pit cleaning for condos & commercial buildings", link="/elevator-pit-cleaning/", cta="Book now")
