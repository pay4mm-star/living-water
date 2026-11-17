"""City landing pages + expert guides (GEO content hub)."""

# slug, name, region, neighbourhoods, intro paragraphs, priority services, hero, nearby
CITIES = [
    dict(slug="toronto", name="Toronto", region="City of Toronto",
         hoods=["The Annex", "Cabbagetown", "Leslieville", "The Beaches", "Rosedale", "Forest Hill", "Yorkville", "Liberty Village", "Downtown core"],
         intro=["Toronto's older neighbourhoods are built from soft Victorian and Edwardian red brick, sandstone and limestone — materials that are easily scarred by a rental pressure washer. Downtown, storefronts, condo podiums and heritage facades collect soot, gum and graffiti that need the right chemistry, not more pressure.",
                "Living Water has worked across the city since 1998 — on homes, heritage facades, commercial plazas and condo garages. We bring hot-water units, soda and micro blasting, and boom-lift-certified crews for multi-storey work."],
         services=["historical-remediation", "brick-cleaning-paint-removal", "graffiti-removal", "commercial-power-washing", "residential-power-washing", "elevator-pit-cleaning"],
         hero="heritage-red-brick-building-cleaning", nearby=["north-york", "scarborough", "etobicoke", "vaughan"]),
    dict(slug="north-york", name="North York", region="City of Toronto",
         hoods=["Willowdale", "York Mills", "Bayview Village", "Don Mills", "Hoggs Hollow", "Bathurst Manor", "Downsview", "Newtonbrook", "Armour Heights"],
         intro=["North York mixes 1950s bungalows in Don Mills and Bathurst Manor with large custom homes in York Mills, Bayview Village and Hoggs Hollow — many finished in natural stone, precast and wide interlock driveways that stain, green over and bloom with efflorescence.",
                "Along Yonge Street, condo towers, parking garages and retail podiums need regular commercial washing and elevator pit maintenance. Living Water serves North York homes, condominium corporations and commercial properties every week."],
         services=["residential-power-washing", "efflorescence-removal", "stone-restoration", "elevator-pit-cleaning", "commercial-power-washing", "brick-cleaning-paint-removal"],
         hero="estate-home-driveway-washing", nearby=["toronto", "vaughan", "richmond-hill", "markham"]),
    dict(slug="scarborough", name="Scarborough", region="City of Toronto",
         hoods=["Agincourt", "Guildwood", "Highland Creek", "Malvern", "Scarborough Village", "Birch Cliff", "Cliffside", "Wexford", "L'Amoreaux"],
         intro=["Scarborough's post-war bungalows and split-levels, interlock driveways and backyard patios take a beating from road salt, shade and moss — especially near the Bluffs and the Rouge Valley's mature tree canopy.",
                "Its plazas, industrial parks and institutional buildings also need commercial pressure washing, graffiti removal and degreasing. Living Water serves Scarborough homeowners, property managers and industrial clients with fixed written quotes."],
         services=["residential-power-washing", "commercial-power-washing", "graffiti-removal", "industrial-power-washing", "brick-cleaning-paint-removal", "efflorescence-removal"],
         hero="parking-lot-pressure-washing-crew", nearby=["toronto", "markham", "pickering", "north-york"]),
    dict(slug="etobicoke", name="Etobicoke", region="City of Toronto",
         hoods=["The Kingsway", "Islington Village", "Mimico", "Long Branch", "Humber Bay Shores", "Alderwood", "Markland Wood", "Rexdale", "Humber Valley"],
         intro=["Etobicoke ranges from Tudor-revival stone and brick homes in the Kingsway and Humber Valley to lakeside condos at Humber Bay Shores and industrial land along Highway 427.",
                "Natural stone, flagstone walkways and heritage brick need gentle, surface-specific cleaning, while warehouses and plants need degreasing and hydro jetting. Living Water handles both — residential, commercial and industrial — across Etobicoke."],
         services=["stone-restoration", "residential-power-washing", "industrial-power-washing", "commercial-power-washing", "brick-cleaning-paint-removal", "sandblasting-services"],
         hero="stone-house-exterior-cleaning", nearby=["toronto", "mississauga", "vaughan", "north-york"]),
    dict(slug="mississauga", name="Mississauga", region="Peel Region",
         hoods=["Port Credit", "Lorne Park", "Streetsville", "Meadowvale", "Erin Mills", "Clarkson", "Malton", "City Centre", "Churchill Meadows"],
         intro=["Mississauga has lakefront homes in Port Credit and Lorne Park, newer subdivisions across Churchill Meadows and Meadowvale, and one of Canada's largest concentrations of warehouses and logistics facilities around Pearson Airport.",
                "Living Water provides residential pressure washing and interlock cleaning for Mississauga homeowners, and industrial pressure washing, sandblasting and commercial maintenance for plants, distribution centres and retail properties."],
         services=["industrial-power-washing", "commercial-power-washing", "residential-power-washing", "sandblasting-services", "efflorescence-removal", "graffiti-removal"],
         hero="industrial-pressure-washing-crew-gta", nearby=["etobicoke", "brampton", "oakville", "toronto"]),
    dict(slug="brampton", name="Brampton", region="Peel Region",
         hoods=["Downtown Brampton", "Bramalea", "Springdale", "Mount Pleasant", "Heart Lake", "Castlemore", "Credit Valley", "Fletcher's Meadow", "Sandringham-Wellington"],
         intro=["Much of Brampton's housing is newer construction, and new brick, precast and stone commonly develop white efflorescence and mortar staining in the first few years. Interlock driveways and steps in subdivisions like Castlemore and Credit Valley also need regular cleaning and resanding.",
                "Brampton is also a major logistics and manufacturing hub. Living Water serves homeowners and builders with efflorescence removal and post-construction cleaning, and industrial clients with pressure washing and degreasing."],
         services=["efflorescence-removal", "residential-power-washing", "industrial-power-washing", "commercial-power-washing", "brick-cleaning-paint-removal", "sandblasting-services"],
         hero="new-build-construction-cleanup", nearby=["mississauga", "vaughan", "etobicoke", "oakville"]),
    dict(slug="vaughan", name="Vaughan", region="York Region",
         hoods=["Woodbridge", "Maple", "Kleinburg", "Thornhill", "Concord", "Vaughan Metropolitan Centre", "Vellore Village", "Patterson", "Sonoma Heights"],
         intro=["Vaughan's large custom homes in Woodbridge, Kleinburg and Maple often feature natural stone facades, precast details, wide interlock driveways and pool decks — surfaces that need careful cleaning and sealing to keep their colour.",
                "Concord and the Highway 400/407 corridor are home to manufacturing and distribution facilities. Living Water serves Vaughan homeowners, builders and industrial clients, including post-construction clean-up and efflorescence removal on new builds."],
         services=["residential-power-washing", "stone-restoration", "efflorescence-removal", "industrial-power-washing", "sandblasting-services", "commercial-power-washing"],
         hero="modern-stone-home-exterior-clean", nearby=["north-york", "richmond-hill", "brampton", "toronto"]),
    dict(slug="markham", name="Markham", region="York Region",
         hoods=["Unionville", "Markham Village", "Cornell", "Cathedraltown", "Berczy Village", "Angus Glen", "Thornhill", "Milliken", "Wismer"],
         intro=["Markham combines heritage main streets in Unionville and Markham Village with newer communities like Cornell and Cathedraltown, and a large base of office and technology campuses.",
                "Living Water offers gentle heritage-appropriate cleaning for older brick and stone, efflorescence removal and interlock cleaning for newer homes, and scheduled commercial washing for offices, plazas and condominiums across Markham."],
         services=["residential-power-washing", "commercial-power-washing", "historical-remediation", "efflorescence-removal", "elevator-pit-cleaning", "graffiti-removal"],
         hero="custom-home-exterior-washing", nearby=["richmond-hill", "scarborough", "north-york", "pickering"]),
    dict(slug="richmond-hill", name="Richmond Hill", region="York Region",
         hoods=["Oak Ridges", "Bayview Hill", "Mill Pond", "Richmond Hill Village", "Jefferson", "Westbrook", "Elgin Mills", "Langstaff", "South Richvale"],
         intro=["Richmond Hill's estate homes in Bayview Hill, South Richvale and Oak Ridges feature natural stone, limestone trim, large interlock driveways and pool surrounds — high-value surfaces where the wrong pressure or acid can cause permanent damage.",
                "Living Water cleans and seals stone, removes efflorescence and moss, and maintains condos, plazas and commercial buildings along Yonge Street and Highway 7."],
         services=["residential-power-washing", "stone-restoration", "efflorescence-removal", "commercial-power-washing", "brick-cleaning-paint-removal", "elevator-pit-cleaning"],
         hero="estate-home-exterior-restoration", nearby=["markham", "vaughan", "north-york", "toronto"]),
    dict(slug="oakville", name="Oakville", region="Halton Region",
         hoods=["Old Oakville", "Bronte", "Glen Abbey", "Joshua Creek", "Kerr Village", "Clearview", "Eastlake", "River Oaks", "Morrison"],
         intro=["Oakville's lakefront estates in Eastlake, Morrison and Old Oakville are finished in natural stone, limestone and premium brick, with large stone patios and pool decks exposed to lake-effect moisture and algae.",
                "Living Water brings gentle stone restoration, soft washing and sealing to Oakville homes, and commercial washing to plazas and businesses in Kerr Village, Bronte and Glen Abbey."],
         services=["stone-restoration", "residential-power-washing", "efflorescence-removal", "brick-cleaning-paint-removal", "commercial-power-washing", "metal-restoration"],
         hero="stone-patio-cleaning-after", nearby=["burlington", "mississauga", "brampton", "etobicoke"]),
    dict(slug="burlington", name="Burlington", region="Halton Region",
         hoods=["Downtown Burlington", "Aldershot", "Roseland", "Tyandaga", "Alton Village", "Millcroft", "Orchard", "Headon Forest", "Shoreacres"],
         intro=["Burlington's lakeside neighbourhoods like Roseland and Shoreacres, and newer communities like Alton Village and the Orchard, share the same problems: algae on shaded siding, moss on roofs and staining on interlock and stone.",
                "Living Water provides residential soft washing and pressure washing, stone cleaning and commercial maintenance across Burlington, and serves industrial clients along the QEW and Highway 403."],
         services=["residential-power-washing", "stone-restoration", "commercial-power-washing", "industrial-power-washing", "efflorescence-removal", "graffiti-removal"],
         hero="roof-moss-removal-soft-wash", nearby=["oakville", "hamilton", "mississauga", "brampton"]),
    dict(slug="oshawa", name="Oshawa", region="Durham Region",
         hoods=["Downtown Oshawa", "Northglen", "Kedron", "Windfields", "Lakeview", "Samac", "Eastdale", "Taunton", "O'Neill"],
         intro=["Oshawa has a historic downtown of century-old brick commercial buildings, established neighbourhoods near Lakeview and O'Neill, and fast-growing north-end communities like Windfields and Kedron.",
                "Its industrial base also needs heavy-duty cleaning. Living Water provides heritage brick cleaning and paint removal downtown, residential washing across Oshawa, and industrial pressure washing, hydro jetting and sandblasting for plants and equipment."],
         services=["industrial-power-washing", "brick-cleaning-paint-removal", "historical-remediation", "residential-power-washing", "sandblasting-services", "commercial-power-washing"],
         hero="yellow-brick-heritage-building-cleaning", nearby=["pickering", "scarborough", "markham", "toronto"]),
    dict(slug="pickering", name="Pickering & Ajax", region="Durham Region",
         hoods=["Bay Ridges", "Liverpool", "Amberlea", "Rouge Park", "Duffin Heights", "Seaton", "Ajax Pickering Village", "South Ajax", "Northeast Ajax"],
         intro=["Pickering and Ajax have lakeside neighbourhoods like Bay Ridges and South Ajax alongside new communities in Duffin Heights and Seaton, where new brick and precast often show efflorescence and construction staining.",
                "Living Water serves Pickering and Ajax homeowners with driveway, interlock, siding and roof cleaning, and commercial and industrial clients with pressure washing, graffiti removal and degreasing."],
         services=["residential-power-washing", "efflorescence-removal", "commercial-power-washing", "industrial-power-washing", "graffiti-removal", "brick-cleaning-paint-removal"],
         hero="garden-stone-pathway-cleaned", nearby=["scarborough", "oshawa", "markham", "toronto"]),
    dict(slug="hamilton", name="Hamilton", region="Hamilton",
         hoods=["Downtown Hamilton", "Westdale", "Durand", "Kirkendall", "Dundas", "Ancaster", "Stoney Creek", "Waterdown", "Hamilton Mountain"],
         intro=["Hamilton's Durand, Kirkendall and Westdale neighbourhoods are full of century brick and stone homes, and its downtown has many heritage commercial buildings — classic candidates for careful masonry cleaning and paint removal.",
                "Hamilton's steel and manufacturing heritage also means heavy industrial cleaning needs. Living Water travels to Hamilton for heritage, commercial and industrial projects, including sandblasting, hydro jetting and metal restoration."],
         services=["historical-remediation", "brick-cleaning-paint-removal", "industrial-power-washing", "sandblasting-services", "metal-restoration", "residential-power-washing"],
         hero="historical-building-remediation-ontario", nearby=["burlington", "oakville", "mississauga", "brampton"]),
]

GUIDES = [
    dict(slug="soft-washing-vs-pressure-washing",
         title="Soft Washing vs Pressure Washing: Which Does Your Property Need?",
         meta="Soft washing vs pressure washing explained by a Toronto contractor with 28 years' experience — which surfaces need which method, and what goes wrong when you choose badly.",
         hero="roof-moss-washing-ladder", related=["residential-power-washing", "commercial-power-washing"],
         answer="Soft washing uses low pressure (similar to a garden hose) plus biodegradable cleaners to kill and dissolve algae, mould and mildew; pressure washing uses high-pressure water — often heated — to physically blast off dirt, oil and stains. Use soft washing on siding, stucco, roofs, painted wood and soft or heritage masonry; use pressure washing on concrete, interlock and other hard, durable surfaces.",
         body="""
<h2>What is soft washing?</h2>
<p>Soft washing applies a cleaning solution at low pressure, lets it dwell so it can break down organic growth, then rinses gently. Because the chemistry does the work, it reaches algae and mould spores that pressure alone only knocks off the surface — so results last longer.</p>
<h2>What is pressure washing?</h2>
<p>Pressure washing relies on mechanical force. Professional units deliver high pressure and high flow, and hot-water machines (often called "power washing") cut through oil, grease, gum and tire marks far faster than cold water.</p>
<h2>Which method for which surface?</h2>
<table>
<thead><tr><th>Surface</th><th>Recommended method</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Vinyl and aluminium siding</td><td>Soft wash</td><td>High pressure forces water behind panels and can crack or dent them.</td></tr>
<tr><td>Stucco and EIFS</td><td>Soft wash</td><td>Pressure can gouge the finish and drive water into the wall.</td></tr>
<tr><td>Asphalt shingle, cedar or ceramic roofs</td><td>Soft wash</td><td>Pressure strips granules, splits shakes and can void warranties.</td></tr>
<tr><td>Wood decks and fences</td><td>Low pressure / soft wash</td><td>High pressure raises and furrows the grain.</td></tr>
<tr><td>Heritage or soft brick and stone</td><td>Soft wash, steam or gentle media blasting</td><td>Pressure erodes the brick face and washes out mortar.</td></tr>
<tr><td>Concrete driveways and garage floors</td><td>Hot-water pressure wash</td><td>Durable surface; heat lifts oil and grease.</td></tr>
<tr><td>Interlock and pavers</td><td>Pressure wash with surface cleaner, then re-sand</td><td>Removes moss and staining; joints are re-filled afterwards.</td></tr>
<tr><td>Commercial sidewalks and plazas</td><td>Hot-water pressure wash</td><td>Removes gum, grease and heavy foot-traffic grime.</td></tr>
</tbody></table>
<h2>What happens when the wrong method is used?</h2>
<ul class="ticks"><li>Etched "wand marks" and stripes in concrete</li><li>Sand blown out of interlock joints, leading to weeds and shifting</li><li>Mortar washed out of brick joints, letting water in</li><li>Water forced behind siding and into window seals</li><li>Shingle granules stripped, shortening roof life</li></ul>
<h2>Most homes need both</h2>
<p>A typical GTA home combines a soft-washed house, roof and deck with a pressure-washed driveway and walkway. A professional crew will tell you which surface gets which method before work starts.</p>
""",
         faqs=[("Is soft washing as effective as pressure washing?", "For organic growth like algae, mould and mildew it is usually more effective, because the cleaner kills the growth instead of just knocking off the surface layer."),
               ("Is soft washing safe for plants?", "Professional crews pre-wet and rinse plants and use biodegradable cleaners to protect landscaping."),
               ("What is the difference between power washing and pressure washing?", "The terms are often used interchangeably; 'power washing' usually refers to pressure washing with heated water.")]),
    dict(slug="how-to-remove-efflorescence",
         title="How to Remove Efflorescence from Brick, Stone & Interlock",
         meta="What causes efflorescence on brick, stone and interlock, how professionals remove it safely, and how to stop it coming back — from a GTA efflorescence specialist.",
         hero="efflorescence-removal-front-steps-before", related=["efflorescence-removal", "brick-cleaning-paint-removal"],
         answer="Efflorescence is a white, powdery salt deposit left when water moves through brick, concrete, stone or mortar and evaporates at the surface. Light, fresh efflorescence can be dry-brushed off; established deposits need a masonry cleaner suited to the material, applied to a pre-wetted surface and thoroughly rinsed. It stops returning only when the moisture source is controlled or the material finishes curing.",
         body="""
<h2>What causes efflorescence?</h2>
<p>Three things must be present: soluble salts in or behind the masonry, water to dissolve them, and a path for that water to reach the surface and evaporate. New brick, mortar, precast and concrete pavers contain more free salts, which is why new homes and new interlock often "bloom" in their first year or two.</p>
<h2>Efflorescence vs other white stains</h2>
<ul class="ticks"><li><strong>Efflorescence</strong> — powdery or crystalline, often brushes off when dry, reappears after rain.</li><li><strong>Lime run / calcium carbonate</strong> — hard white crust, often streaking from mortar joints; needs stronger treatment.</li><li><strong>Mortar smears</strong> — left from construction; removed with a properly neutralised masonry cleaner.</li></ul>
<h2>How professionals remove efflorescence</h2>
<ol class="ticks"><li><strong>Identify the material and the deposit</strong> — limestone, marble and some precast are acid-sensitive.</li><li><strong>Test a small area</strong> to confirm the cleaner will not discolour the surface.</li><li><strong>Pre-wet the surface</strong> so the cleaner stays on the face and is not drawn deep into the material.</li><li><strong>Apply the correct cleaner</strong> and agitate where needed.</li><li><strong>Rinse thoroughly</strong> with controlled pressure, and neutralise if an acid-based product was used.</li><li><strong>Address the moisture</strong> — downspouts, grading, failed caulking or missing caps.</li></ol>
<h2>Mistakes to avoid</h2>
<ul class="ticks"><li>Using undiluted muriatic acid — it can burn brick, etch stone and leave new stains.</li><li>Blasting with high pressure — it drives more water in and can damage the face.</li><li>Sealing over efflorescence — it traps the salts and can cause spalling.</li></ul>
<h2>Will it come back?</h2>
<p>On new construction, efflorescence often returns a few times as the material cures, then stops. On older buildings, recurring efflorescence points to a moisture problem that should be fixed. Once the surface is clean and dry, a breathable sealer can help on pavers and some stone.</p>
""",
         faqs=[("Does vinegar remove efflorescence?", "Diluted vinegar can lift light efflorescence on durable brick, but it is acidic and can etch limestone, marble and some precast. Test first or use a product made for the specific material."),
               ("Is efflorescence harmful?", "Efflorescence itself is cosmetic, but it shows water is moving through the masonry, which can lead to freeze-thaw damage over time."),
               ("Is efflorescence covered under paver or stone warranties?", "Many manufacturers treat it as a natural occurrence; some use specialist contractors such as Living Water for warranty service. Check with your supplier.")]),
    dict(slug="is-sandblasting-safe-for-brick",
         title="Is Sandblasting Safe for Brick? Media Blasting Options Explained",
         meta="When sandblasting damages brick, safer alternatives like soda, micro and dry ice blasting, and how to choose the right method for paint and coating removal.",
         hero="media-blasting-stone-technician", related=["sandblasting-services", "historical-remediation", "brick-cleaning-paint-removal"],
         answer="Traditional sandblasting with coarse abrasive at high pressure is not safe for most brick — it strips the hard outer face, exposes the soft core to water and freeze-thaw damage, and erodes mortar. Brick can be cleaned or stripped safely with gentler methods: chemical paint strippers, low-pressure micro blasting with fine media, soda blasting, steam, or dry ice blasting, chosen after a test patch.",
         body="""
<h2>Why aggressive sandblasting damages brick</h2>
<p>Clay brick is fired to create a hard, dense outer skin. Coarse abrasive at high pressure removes that skin along with the dirt or paint, leaving a rough, porous surface that absorbs water. In Ontario's freeze-thaw cycles, absorbed water expands and causes spalling — faces popping off — within a few winters.</p>
<h2>Safer blasting and cleaning options</h2>
<table>
<thead><tr><th>Method</th><th>How it works</th><th>Best for</th></tr></thead>
<tbody>
<tr><td>Chemical stripping</td><td>Stripper softens paint, removed with low-pressure rinsing</td><td>Painted brick, heritage facades</td></tr>
<tr><td>Micro blasting</td><td>Fine media at low pressure, tightly controlled</td><td>Detailed masonry, stubborn coatings</td></tr>
<tr><td>Soda blasting</td><td>Sodium bicarbonate media, softer than sand</td><td>Delicate surfaces, soot, light coatings</td></tr>
<tr><td>Dry ice blasting</td><td>Frozen CO₂ pellets that sublimate on impact</td><td>Coatings and residue with no media clean-up</td></tr>
<tr><td>Steam cleaning</td><td>Low-pressure, high-temperature water</td><td>Heritage stone and brick, organic staining</td></tr>
<tr><td>Dustless (wet) abrasive blasting</td><td>Abrasive mixed with water to control dust</td><td>Concrete, steel, pools, durable masonry</td></tr>
</tbody></table>
<h2>When is sandblasting the right choice?</h2>
<p>Abrasive blasting is excellent for steel, aluminium, concrete, pool shells, bridges, tanks and heavy coatings like epoxy. On masonry it should be limited to durable brick or concrete, at low pressure, with fine media — and always after a test panel.</p>
<h2>Questions to ask a blasting contractor</h2>
<ul class="ticks"><li>Will you do a test patch and let me approve it?</li><li>What media and pressure will you use, and why?</li><li>How will dust, runoff and neighbouring property be protected?</li><li>Are you WSIB covered and insured, and can you provide a certificate?</li></ul>
""",
         faqs=[("Can painted brick be restored to original?", "Usually, yes, with chemical stripping and gentle rinsing or micro blasting. Some paint ghosting may remain on very porous brick."),
               ("Is soda blasting safe for brick?", "Soda is much softer than sand and is often suitable for brick and stone, but pressure and nozzle distance still matter, and sodium residue must be rinsed well."),
               ("Does dustless blasting create dust?", "It greatly reduces airborne dust by wetting the media, making it better suited to occupied or urban sites.")]),
    dict(slug="how-often-to-pressure-wash-ontario",
         title="How Often Should You Pressure Wash in Ontario? A Seasonal Schedule",
         meta="A practical pressure washing and exterior cleaning schedule for GTA homes and commercial properties — what to clean in spring, summer and fall, and how often.",
         hero="living-water-van-residential-pressure-washing", related=["residential-power-washing", "commercial-power-washing"],
         answer="Most GTA homes should have driveways, walkways and interlock pressure washed once a year — ideally in spring after road salt season — with house siding and roofs soft washed every one to three years as algae appears, and decks cleaned annually before sealing. Commercial entrances, sidewalks and parking areas typically need cleaning monthly to quarterly depending on foot traffic.",
         body="""
<h2>Recommended frequency by surface</h2>
<table>
<thead><tr><th>Surface</th><th>How often</th><th>Best time</th></tr></thead>
<tbody>
<tr><td>Driveway and walkways</td><td>Every year</td><td>Spring, after salt season</td></tr>
<tr><td>Interlock and pavers</td><td>Every 1–2 years, re-sand as needed</td><td>Late spring</td></tr>
<tr><td>House siding / brick</td><td>Every 1–3 years</td><td>Spring to early fall</td></tr>
<tr><td>Roof (moss / algae)</td><td>When growth appears, typically every 2–4 years</td><td>Spring or fall</td></tr>
<tr><td>Deck and fence</td><td>Every year</td><td>Spring, before staining or sealing</td></tr>
<tr><td>Pool deck and coping</td><td>Every year</td><td>Pool opening</td></tr>
<tr><td>Commercial entrances & sidewalks</td><td>Monthly to quarterly</td><td>Year-round, off-hours</td></tr>
<tr><td>Parking garages</td><td>1–2 times per year</td><td>Spring, after salt season</td></tr>
</tbody></table>
<h2>Spring: the most important clean</h2>
<p>Road salt, sand and winter grime are corrosive to concrete and interlock and stain brick. A spring wash removes them before summer heat bakes stains in, and it is the right moment to check for frost damage, efflorescence and loose pavers.</p>
<h2>Summer: decks, patios and sealing</h2>
<p>Warm, dry weather is ideal for cleaning and sealing decks, pool coping and stone patios, which need dry surfaces to cure.</p>
<h2>Fall: before freeze-up</h2>
<p>Removing moss, leaves and organic growth in fall keeps surfaces from staying wet through winter, reducing freeze-thaw damage and slip hazards.</p>
<h2>Winter</h2>
<p>Exterior washing stops once temperatures stay below freezing, but emergency work, interior cleaning, elevator pits and industrial jobs continue year-round.</p>
""",
         faqs=[("Can you pressure wash in winter in Toronto?", "Exterior residential washing is generally avoided below freezing because water freezes on surfaces. Interior, industrial and emergency work continues year-round."),
               ("Does regular pressure washing damage concrete?", "Not when done correctly with surface cleaners at appropriate pressure. Annual cleaning helps concrete last longer by removing salt and organic growth.")]),
    dict(slug="elevator-pit-cleaning-guide",
         title="Elevator Pit Cleaning: What Building Managers Need to Know",
         meta="Why elevator pits must be kept clean, warning signs of a problem, what professional elevator pit cleaning includes, and how to handle oil spills and sewage backups.",
         hero="elevator-pit-pressure-washing", related=["elevator-pit-cleaning", "industrial-power-washing"],
         answer="Elevator pits collect garbage, dust, oil and water over time, creating fire, slip and environmental hazards for riders and maintenance crews. Building managers should have pits inspected during routine elevator maintenance and professionally cleaned whenever debris, oil, standing water or odours are present — and immediately after flooding or a sewage backup.",
         body="""
<h2>Why elevator pits get dirty</h2>
<p>The pit sits at the lowest point of the hoistway. Debris falls through door gaps, hydraulic and lubricating oil can leak, and groundwater, sprinkler discharge or sewage backups collect there. Because nobody sees it, contamination builds up unnoticed.</p>
<h2>Warning signs</h2>
<ul class="ticks"><li>Garbage or dust accumulation</li><li>Standing water, mud or sludge</li><li>Oil sheen or hydraulic fluid on the floor</li><li>Foul odours from the hoistway</li><li>Visible cracks or water entry</li></ul>
<h2>What professional elevator pit cleaning includes</h2>
<ol class="ticks"><li>Coordination with your elevator service provider so the elevator is locked out safely</li><li>Removal of debris, sludge and standing water</li><li>Oil spill clean-up and proper disposal of hazardous waste</li><li>Pressure washing and degreasing of the pit floor, walls and equipment</li><li>Sanitizing and deodorizing, especially after sewage backups</li><li>Crack repair and pit painting where required</li></ol>
<h2>Why use a specialist?</h2>
<p>Pit work involves confined spaces, moving equipment and contaminated waste. Elevator companies across Ontario refer pit cleaning to specialists like Living Water so their mechanics can focus on the equipment.</p>
""",
         faqs=[("Who is responsible for cleaning the elevator pit?", "Usually the building owner or property manager arranges cleaning, coordinated with the elevator maintenance contractor who controls access to the equipment."),
               ("How long does elevator pit cleaning take?", "Routine cleaning is often completed in a few hours; flood or oil spill clean-up can take longer depending on volume and disposal.")]),
    dict(slug="hiring-a-pressure-washing-contractor",
         title="How to Hire a Pressure Washing Contractor in the GTA: 10 Questions to Ask",
         meta="The questions to ask before hiring a pressure washing or sandblasting contractor in Toronto — insurance, WSIB, methods, written quotes and guarantees.",
         hero="rooftop-terrace-pressure-washing-crew", related=["commercial-power-washing", "residential-power-washing"],
         answer="Before hiring a pressure washing contractor in Ontario, confirm they carry commercial general liability insurance and WSIB coverage (and can send certificates), ask how they will clean each surface and protect plants, windows and runoff, get a fixed written quote with scope and timing, and look for verifiable reviews and before-and-after photos of similar work.",
         body="""
<h2>10 questions to ask</h2>
<ol class="ticks">
<li><strong>Are you insured?</strong> Ask for a Certificate of Insurance showing commercial general liability. Living Water carries $5M.</li>
<li><strong>Are your workers covered by WSIB?</strong> In Ontario, hiring a contractor without WSIB coverage can expose the property owner to liability. Ask for a clearance certificate.</li>
<li><strong>How will you clean each surface?</strong> A professional distinguishes soft washing, hot-water pressure washing and blasting.</li>
<li><strong>Will you test first?</strong> Essential for brick, stone, heritage and paint removal.</li>
<li><strong>How will you protect plants, windows, vehicles and neighbours?</strong></li>
<li><strong>How do you manage wash water and runoff?</strong> Municipal sewer bylaws restrict what can enter storm drains.</li>
<li><strong>Is the quote fixed and in writing?</strong> It should state method, scope, timing and price.</li>
<li><strong>Do you have photos of similar jobs?</strong></li>
<li><strong>What happens if I'm not satisfied?</strong> Look for a re-clean guarantee.</li>
<li><strong>Are your crews certified for lifts and work at height?</strong> Needed for multi-storey facades.</li>
</ol>
<h2>Red flags</h2>
<ul class="ticks"><li>Cash-only, no written quote</li><li>No insurance certificate or WSIB clearance</li><li>"One pressure for everything"</li><li>Pressure to decide on the spot</li></ul>
""",
         faqs=[("Why does WSIB matter when hiring a contractor?", "If an uncovered worker is injured on your property, you may face liability. A WSIB clearance certificate confirms the contractor's account is in good standing."),
               ("Should a pressure washing quote be free?", "Most reputable contractors provide free assessments and fixed written quotes; Living Water does.")]),
]
