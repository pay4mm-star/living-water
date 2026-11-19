"""Pass 3 content: full reviews, industries, service at-a-glance facts, more guides."""

REVIEWS_FULL = [
    ("Mark Sampson", "We had an AMAZING experience with Navid and his team. They expertly pressure washed our backyard stones and applied a sealer to the pool coping. Navid really cares about doing an exceptional, professional job. They stand by their work. I'd highly recommend using them!"),
    ("Des Hunter", "After 11 years, we decided it was time to pressure wash our patio and the deck around the pool. We checked various companies and selected Living Water based on discussions with Navid and cost. Navid was personable and very professional in his work habits. All patio furniture was removed and then replaced. He was meticulous in ensuring every patio stone was completely clean. The end result was a patio and pool deck that looked like the original 11 years ago."),
    ("Brian Flaherty", "I was looking at the state my patio and driveway pavers and bricks were in and thought they should be replaced. Instead I called Living Water to try and clean them. Excellent job — when they finished, my walkways and drive looked better than new! Great work Navid!"),
    ("Mason Carter", "The company I work for hired Living Water Pressure Wash Services to clean up a product we had sent to a job site. Naveed and his team were great to work with and made sure everything went smoothly. Our contact on site said the stone looks great and the cleaners did a fantastic job. Would recommend Living Water to anyone in need of this type of service."),
    ("Domenic Sorbara", "Navid and team were incredible. They took the time required and the patience to do the job for a very fair price. Would highly recommend."),
    ("Raaz Alakoozi", "Pleasure to have had Navid and his colleague power wash our driveway and backyard. Excellent job, excellent service and very professional. Would definitely recommend to friends and neighbours."),
    ("Shawn Vanderyagt", "Professional, personable and a service that performs beyond your expectations. Truly a pleasure to deal with. I would highly recommend their services and especially their abilities to every one of my customers."),
    ("Ali Reyhany", "Great job cleaning and sealing stone work at my house. Definitely recommend them."),
    ("Sachin Kharbanda", "Very good service, reliable and friendly."),
    ("Steven H", "Incredible service and over-achieved in every way."),
]

INDUSTRIES = [
    ("Property managers & condominium boards", "Scheduled washing of entrances, garages, walkways and facades, plus elevator pit cleaning — with COI and WSIB clearance for your files.",
     ["commercial-power-washing", "elevator-pit-cleaning", "graffiti-removal"], "condo-column-pressure-washing"),
    ("Commercial & retail properties", "Plazas, storefronts, restaurants and office buildings kept clean on overnight or weekend schedules.",
     ["commercial-power-washing", "graffiti-removal", "brick-cleaning-paint-removal"], "commercial-building-exterior-washing"),
    ("Industrial & manufacturing", "Silo and tank cleaning, hydro jetting, degreasing and sanitation for plants, food facilities and heavy equipment.",
     ["industrial-power-washing", "sandblasting-services", "metal-restoration"], "silo-tank-exterior-cleaning-boom-lift"),
    ("General contractors & builders", "Post-construction clean-up, mortar and efflorescence removal, and surface preparation for coatings.",
     ["efflorescence-removal", "brick-cleaning-paint-removal", "sandblasting-services"], "new-build-construction-cleanup"),
    ("Elevator service companies", "The trusted referral of large GTA elevator companies for pit cleaning, oil spills and flood clean-up.",
     ["elevator-pit-cleaning"], "elevator-pit-pressure-washing"),
    ("Stone & paver manufacturers", "Warranty service for efflorescence and staining on stone and paver products across Ontario.",
     ["efflorescence-removal", "stone-restoration"], "precast-stone-coping-cleaning"),
    ("Heritage conservators, architects & municipalities", "Test panels and gentle, documented methods for historic buildings, monuments and public landmarks.",
     ["historical-remediation", "stone-restoration", "metal-restoration"], "heritage-facade-restoration-after"),
    ("Homeowners", "Driveways, interlock, siding, roofs, decks and pool areas cleaned with the right method for each surface.",
     ["residential-power-washing", "efflorescence-removal", "stone-restoration"], "estate-home-driveway-washing"),
]

# per service: (best for, methods, clients, availability)
SERVICE_FACTS = {
    "driveway-interlock-cleaning": ("Concrete and interlock driveways, walkways, patios, stone paths", "Hot-water surface cleaning, stain pre-treatment, polymeric re-sanding, sealing", "Homeowners, HOAs", "Spring and fall most popular; booked within 2–5 days"),
    "house-washing": ("Vinyl and aluminium siding, brick, stone, stucco, soffits and trim", "Low-pressure soft washing with biodegradable cleaners", "Homeowners", "Spring to fall"),
    "roof-cleaning": ("Asphalt shingle, cedar, ceramic tile, metal and flat roofs", "Soft washing — never high pressure on shingles", "Homeowners, property managers", "Spring and fall"),
    "deck-fence-cleaning": ("Wood, composite and PVC decks, fences, railings and pergolas", "Wood-safe cleaners, low-pressure rinse along the grain", "Homeowners", "Spring and summer, before staining"),
    "paver-stone-sealing": ("Interlock, pavers, natural stone, pool decks and coping", "Deep clean, efflorescence check, re-sand, breathable sealer", "Homeowners, builders", "Dry weather, late spring to early fall"),
    "parking-garage-cleaning": ("Underground and above-ground garages, ramps, drains", "Hot-water washing, salt and oil removal, drain flushing", "Condo boards, property managers, commercial owners", "Overnight and weekend, level by level"),
    "residential-power-washing": ("Driveways, interlock, patios, siding, roofs, decks, brick and stone", "Soft washing, hot-water pressure washing, surface cleaners, sealing", "Homeowners, HOAs", "Usually booked within 2–5 days"),
    "commercial-power-washing": ("Plazas, storefronts, sidewalks, parking lots and garages, schools, restaurants", "Hot-water pressure washing, degreasing, gum and graffiti removal", "Property managers, condo boards, businesses", "Overnight and weekend scheduling; 24/7 emergency line"),
    "industrial-power-washing": ("Plants, silos and tanks, food facilities, bridges, heavy equipment", "High-pressure washing, hydro jetting, degreasing, sanitation", "Manufacturers, plants, municipalities", "24/7 emergency response"),
    "sandblasting-services": ("Steel, aluminium, concrete, pools, durable masonry, coatings", "Dustless wet blasting, dry blasting, micro, soda and dry ice blasting", "Contractors, pool companies, restoration firms, owners", "Mobile service across the GTA"),
    "brick-cleaning-paint-removal": ("Interior and exterior brick, painted masonry, mortar smears", "Chemical cleaning, neutralised acid washing, controlled rinsing, micro blasting", "Homeowners, builders, commercial owners", "Test patch before full work"),
    "historical-remediation": ("Heritage brick, stone, statues, monuments, copper and aluminium", "Steam, soda and micro blasting, poultices, lead paint removal", "Conservators, architects, municipalities, owners", "Test panels for approval"),
    "disaster-restoration": ("Fire, smoke, water, wind and mould damage", "Securing, extraction, drying, soot remediation, antimicrobial treatment, rebuild", "Homeowners, businesses, property managers", "24/7 emergency line (647) 833-4343"),
    "elevator-pit-cleaning": ("Condo, rental, office, retail and institutional elevator pits", "Debris and water removal, oil and sludge clean-up, pressure washing, sanitizing", "Condo boards, property managers, elevator contractors", "After-hours scheduling; 24/7 emergency line"),
    "elevator-pit-water-removal": ("Flooded pits, sewage backups, oil and hydraulic spills", "Pump-out, sludge and oil removal, sanitizing, photo documentation", "Condo boards, property managers, elevator contractors", "24/7 emergency: (647) 833-4343"),
    "efflorescence-removal": ("Brick, stone, precast, concrete and interlock", "Material-specific masonry cleaners, pre-wetting, controlled rinsing", "Homeowners, builders, stone manufacturers", "Warranty service for Ontario manufacturers"),
    "graffiti-removal": ("Brick, concrete, stone, metal, glass and painted surfaces", "Bio-friendly removers, controlled pressure, poultices, anti-graffiti coating", "Businesses, municipalities, property managers", "Same-week removal"),
    "stone-restoration": ("Marble, granite, limestone, sandstone, natural stone, precast", "pH-appropriate cleaners, low pressure, stain removal, sealing", "Homeowners, commercial and heritage owners", "Assessment before cleaning"),
    "metal-restoration": ("Steel, stainless steel, aluminium and copper", "Rust and oxidation removal, coating stripping, media blasting", "Industrial, commercial and heritage owners", "Surface preparation for coating"),
}

GUIDES_MORE = [
    dict(slug="winter-elevator-pit-checklist",
         title="Winter Elevator Pit Checklist for Condo & Property Managers",
         meta="A winter elevator pit checklist for condo boards and property managers: salt, meltwater and thaws, monthly checks, and when to book.",
         hero="elevator-pit-cleaning-toronto", related=["elevator-pit-cleaning", "elevator-pit-water-removal"],
         answer="In winter, condo and property managers should ask their elevator contractor to report pit conditions at every maintenance visit, watch for water, salt residue, odours and debris, keep entrance matting and sill areas clean to limit meltwater, test sump pumps before the thaw, and book a professional pit cleaning after winter — or immediately after any flood, leak or sewage backup.",
         body="""
<h2>Why winter is hard on elevator pits</h2>
<p>Snow and slush tracked into lobbies melts at the elevator sill and runs into the hoistway, carrying road salt and grit. Freeze-thaw cycles and spring melt raise groundwater, and frozen pipes and sprinklers can flood lower levels. The result is corrosive, salty sludge around buffers and rail brackets.</p>
<h2>Monthly winter checklist</h2>
<ol class="ticks">
<li>Ask your elevator contractor to note pit condition (water, debris, oil) on every service report.</li>
<li>Check lobby and garage entrances: matting in place, sill areas swept and dry.</li>
<li>Watch for odours, damp marks or salt staining at landing doors.</li>
<li>Confirm the pit sump pump (if present) runs and its cover is secure.</li>
<li>Check for leaks from garage ceilings, sprinkler lines and drains near the hoistway.</li>
<li>Keep a log with photos — useful for reserve-fund planning and warranty or insurance claims.</li>
</ol>
<h2>When to book a pit cleaning</h2>
<ul class="ticks"><li>After winter, to remove salt, grit and meltwater residue</li><li>Immediately after any flood, leak, sewage backup or oil spill</li><li>When your elevator contractor reports debris, water or oil</li><li>Before first-year Tarion warranty inspections in new condominiums</li></ul>
<h2>What the rules say</h2>
<p>Ontario elevators are regulated by TSSA under the CSA B44 code. TSSA's pre-inspection checklist calls for permanent means to prevent groundwater accumulating in pits and for sumps to be covered, and TSSA warns never to use elevators in a flooded building. Tarion's guidelines for new condominiums state pits should be clear of standing water and cleaned of construction debris.</p>
<h2>Budgeting tip</h2>
<p>Ask for a fixed written quote per pit and a seasonal program across all your buildings. A post-winter clean and an annual clean are a common pattern; emergency pump-outs are billed separately.</p>
""",
         faqs=[("Should elevator pits be cleaned in winter or spring?", "Both have a place: emergency pump-outs happen whenever water appears, and a scheduled clean after winter removes the season's salt and meltwater residue."),
               ("Can our cleaning staff clean the elevator pit?", "Entering a pit requires the elevator to be taken out of service and secured by the elevator contractor, so pit cleaning should be coordinated with them and done by trained contractors.")]),
    dict(slug="interlock-cleaning-and-resanding",
         title="How to Clean and Re-Sand Interlock Pavers",
         meta="How pros clean interlock driveways and patios, remove moss and stains, re-sand joints with polymeric sand and decide whether to seal.",
         hero="garden-stone-pathway-cleaned", related=["residential-power-washing", "efflorescence-removal"],
         answer="Interlock is cleaned by pre-treating stains and organic growth, washing with a rotary surface cleaner (not a bare wand) to avoid stripes, flushing out old joint sand and debris, letting the pavers dry completely, then sweeping new polymeric sand into the joints and activating it with a light mist. Sealing is optional and protects colour and helps resist stains.",
         body="""
<h2>Why interlock gets dirty and weedy</h2>
<p>Joint sand washes out over time, leaving gaps where soil, seeds and moss settle. Oil drips, tire marks, rust from patio furniture and winter salt add stains, and new pavers can bloom with efflorescence.</p>
<h2>Step-by-step professional process</h2>
<ol class="ticks"><li><strong>Inspect</strong> for sunken or broken pavers and drainage problems.</li><li><strong>Pre-treat</strong> oil, rust and organic stains with suitable cleaners.</li><li><strong>Surface-clean</strong> with a rotary cleaner for an even, stripe-free finish.</li><li><strong>Flush the joints</strong> to remove old sand, weeds and moss.</li><li><strong>Rinse and dry</strong> — polymeric sand needs dry pavers and dry joints.</li><li><strong>Re-sand</strong> with polymeric sand, compact, and sweep off the surface.</li><li><strong>Activate</strong> with a fine mist so the sand hardens without hazing.</li><li><strong>Seal (optional)</strong> once fully cured, if the surface benefits.</li></ol>
<h2>Common mistakes</h2>
<ul class="ticks"><li>Using a narrow wand tip — leaves stripes and erodes the paver face.</li><li>Applying polymeric sand to damp pavers — causes haze that is hard to remove.</li><li>Sealing over efflorescence or damp pavers — traps moisture and whitens the sealer.</li></ul>
""",
         faqs=[("How often should interlock be re-sanded?", "Typically every few years, or whenever joints look empty or weeds start appearing. Polymeric sand lasts longer than regular sand."),
               ("Should I seal my interlock?", "Sealing is optional. It can enrich colour and make stains easier to clean, but it must be applied to clean, dry pavers with no efflorescence.")]),
    dict(slug="remove-paint-from-brick",
         title="How to Remove Paint from Brick Without Damaging It",
         meta="Safe ways to strip paint from interior and exterior brick — chemical strippers, low-pressure rinsing and micro blasting — and what to avoid.",
         hero="painted-building-paint-removal-after", related=["brick-cleaning-paint-removal", "historical-remediation", "sandblasting-services"],
         answer="The safest way to remove paint from brick is a chemical paint stripper matched to the coating, left to dwell (often under a cover), then removed with low-pressure rinsing or scraping — with gentle micro or soda blasting only for stubborn residue. Avoid high-pressure washing and coarse sandblasting, which strip the brick's fired face and lead to water damage.",
         body="""
<h2>Start with a test patch</h2>
<p>Paint type, the number of layers and the brick itself all affect results. A small test area shows which stripper works, how long it needs, and whether any ghosting will remain — before the whole wall is committed.</p>
<h2>Methods compared</h2>
<table><thead><tr><th>Method</th><th>Risk to brick</th><th>Notes</th></tr></thead><tbody>
<tr><td>Chemical stripper + low-pressure rinse</td><td>Low</td><td>The standard approach for most painted brick.</td></tr>
<tr><td>Micro / soda blasting</td><td>Low–medium</td><td>For residue in pores and textured brick, at controlled pressure.</td></tr>
<tr><td>Steam</td><td>Low</td><td>Helps soften some coatings on heritage masonry.</td></tr>
<tr><td>High-pressure washing alone</td><td>High</td><td>Rarely removes paint and erodes brick and mortar.</td></tr>
<tr><td>Coarse sandblasting</td><td>Very high</td><td>Destroys the brick face; avoid on clay brick.</td></tr>
</tbody></table>
<h2>Lead paint</h2>
<p>Older buildings may have lead-based paint. It must be removed with containment and proper waste handling — not dry-scraped or blasted into the open air.</p>
<h2>After paint removal</h2>
<p>Once stripped and rinsed, brick should be left breathable. Repointing failed mortar joints and fixing water sources helps the restored brick last.</p>
""",
         faqs=[("Can all paint be removed from brick?", "Most coatings can be removed. Very porous brick may keep faint ghosting of the old paint, which a test patch will reveal."),
               ("Is it better to repaint brick instead?", "Painted brick needs repainting every several years and can trap moisture. Stripping restores a low-maintenance, breathable surface.")]),
    dict(slug="graffiti-removal-guide",
         title="Graffiti Removal Guide: Brick, Concrete, Stone & Metal",
         meta="How graffiti is removed from brick, concrete, stone, metal and glass without ghosting or damage, and how anti-graffiti coatings work.",
         hero="graffiti-removal-house-wall", related=["graffiti-removal", "brick-cleaning-paint-removal"],
         answer="Graffiti is best removed quickly with a remover matched to the paint and the surface — solvent-based removers for spray paint and markers, followed by controlled low-to-medium pressure rinsing — rather than high pressure alone, which drives paint deeper into porous brick and concrete. Anti-graffiti coatings make future tags much easier to remove.",
         body="""
<h2>Why fast removal matters</h2>
<p>Fresh paint sits closer to the surface and comes off more cleanly. The longer it cures, the deeper it penetrates porous materials, and quickly removed tags are less likely to attract more.</p>
<h2>Approach by surface</h2>
<table><thead><tr><th>Surface</th><th>Typical approach</th></tr></thead><tbody>
<tr><td>Brick</td><td>Remover dwell, then low-pressure hot rinse; poultice for ghosting</td></tr>
<tr><td>Concrete</td><td>Remover plus hot-water pressure rinse</td></tr>
<tr><td>Natural stone</td><td>pH-appropriate remover, gentle rinse, poultice if needed</td></tr>
<tr><td>Metal & painted surfaces</td><td>Mild solvent that lifts tag but not factory finish</td></tr>
<tr><td>Glass</td><td>Solvent and blade; etched graffiti needs polishing or film</td></tr>
</tbody></table>
<h2>Anti-graffiti coatings</h2>
<p><strong>Sacrificial</strong> coatings come off with the graffiti and are re-applied; <strong>permanent</strong> coatings let tags be wiped or washed off repeatedly. Both should be breathable on masonry.</p>
""",
         faqs=[("Will graffiti removal leave a shadow?", "Fresh graffiti usually leaves no trace. Old tags on porous brick may leave light ghosting, reduced with poultices or gentle blasting."),
               ("Who removes graffiti on private property in Toronto?", "Property owners are generally responsible for removing graffiti from their buildings; check your municipality's current graffiti bylaw for timelines.")]),
    dict(slug="pressure-washing-cost-factors",
         title="What Affects the Cost of Pressure Washing in Toronto?",
         meta="What sets the price of pressure washing, sandblasting and restoration in the GTA: size, surface, staining, access, method and timing.",
         hero="living-water-van-residential-pressure-washing", related=["residential-power-washing", "commercial-power-washing", "sandblasting-services"],
         answer="Pressure washing prices in the GTA depend mainly on the area and type of surface, how heavy the staining or growth is, the cleaning method required (soft wash, hot water, chemical or blasting), access and height (ladders, lifts, containment), extras like re-sanding or sealing, and scheduling such as after-hours or emergency work. A site-specific, fixed written quote is the only reliable number.",
         body="""
<h2>The main cost factors</h2>
<table><thead><tr><th>Factor</th><th>Why it matters</th></tr></thead><tbody>
<tr><td>Size of the area</td><td>More square footage means more time, water and product.</td></tr>
<tr><td>Surface type</td><td>Delicate surfaces (heritage brick, limestone, cedar) need slower, gentler methods.</td></tr>
<tr><td>Level of staining</td><td>Oil, rust, paint, efflorescence and deep moss need pre-treatment or multiple passes.</td></tr>
<tr><td>Method</td><td>Soft washing, hot-water washing, chemical cleaning and media blasting use different equipment and materials.</td></tr>
<tr><td>Access & height</td><td>Ladders, boom or scissor lifts, scaffolding and containment add set-up time.</td></tr>
<tr><td>Protection & runoff</td><td>Covering plants, windows and vehicles, and managing wash water.</td></tr>
<tr><td>Extras</td><td>Polymeric sand, sealing, anti-graffiti coatings, repairs.</td></tr>
<tr><td>Scheduling</td><td>Overnight, weekend or 24/7 emergency work.</td></tr>
</tbody></table>
<h2>How to get an accurate quote</h2>
<ul class="ticks"><li>Send photos of each surface and any problem areas.</li><li>Give approximate dimensions and your postal code.</li><li>Mention access limits — tight side yards, heights, parking.</li><li>Ask for a fixed written quote with method and scope, not an hourly estimate.</li></ul>
<h2>Why the cheapest quote can cost more</h2>
<p>Damage from the wrong method — etched concrete, washed-out mortar, stripped shingles, burned brick — is expensive or impossible to reverse. Compare insurance, WSIB coverage and method, not just price.</p>
""",
         faqs=[("Do you charge for quotes?", "No. Living Water provides free assessments and fixed written quotes."),
               ("Can I get a quote from photos?", "Yes — for most straightforward residential work we can quote from photos and dimensions. Commercial, industrial and restoration projects usually need a site visit.")]),
    dict(slug="fire-smoke-damage-first-steps",
         title="After a Fire: First Steps for Property Owners",
         meta="What to do in the first hours and days after a home or commercial fire: safety, insurance, securing the property, smoke and soot clean-up.",
         hero="heritage-building-scaffolding-restoration", related=["disaster-restoration"],
         answer="After a fire, wait until the fire department confirms the building is safe to enter, contact your insurance company right away, document the damage with photos before anything is moved, secure the property against weather and entry, and start professional smoke, soot and water clean-up quickly — soot and firefighting water keep causing damage the longer they sit.",
         body="""
<h2>First 24 hours</h2>
<ol class="ticks"><li><strong>Safety first</strong> — only re-enter when officials say it is safe; utilities may need inspection before reconnection.</li><li><strong>Call your insurer</strong> and ask how they want the claim documented.</li><li><strong>Photograph everything</strong> before cleaning or removing items.</li><li><strong>Secure the property</strong> — board windows and doors, tarp the roof.</li><li><strong>Remove standing water</strong> from firefighting to limit mould.</li></ol>
<h2>Why soot and smoke need fast action</h2>
<p>Soot is acidic and can discolour and etch surfaces, and smoke odour penetrates porous materials. Early cleaning limits permanent damage and keeps restoration costs down.</p>
<h2>What professional restoration includes</h2>
<ul class="ticks"><li>Damage assessment and a written scope</li><li>Board-up and weather protection</li><li>Water extraction and drying</li><li>Smoke and soot remediation on structure and surfaces</li><li>Exterior soot cleaning on brick, stone and siding</li><li>Repairs and rebuilding</li></ul>
""",
         faqs=[("Can smoke-damaged brick be cleaned?", "Yes. Exterior soot on brick and stone is cleaned with suitable cleaners and controlled washing, or gentle media blasting for heavy deposits."),
               ("How quickly should restoration start?", "As soon as the property is declared safe and your insurer is notified. Delays let soot, odour and water damage spread.")]),
]

GLOSSARY = [
    ("Abrasive blasting", "Driving a stream of abrasive media (sand, glass, garnet, soda, walnut shell and others) at a surface under pressure to strip rust, paint, scale or coatings.", "/sandblasting-services/"),
    ("Acid wash", "Cleaning masonry with a diluted acid-based cleaner to dissolve mortar smears and mineral stains. It must be tested, correctly diluted and neutralised.", "/brick-cleaning-paint-removal/"),
    ("Anti-graffiti coating", "A clear protective coating that makes graffiti easier to remove. Sacrificial coatings come off with the graffiti; permanent coatings stay in place.", "/graffiti-removal/"),
    ("Buffer (elevator)", "The spring or oil device at the bottom of an elevator pit that stops a car or counterweight travelling past its normal limit. Pit debris and corrosion around buffers is a common clean-up item.", "/elevator-pit-cleaning/"),
    ("Dry ice blasting", "Blasting with frozen carbon dioxide pellets that turn to gas on impact, removing coatings and residue without leaving abrasive media behind.", "/sandblasting-services/"),
    ("Dustless blasting", "Wet abrasive blasting where water is mixed with the media to suppress airborne dust.", "/sandblasting-services/"),
    ("Efflorescence", "A white, powdery salt deposit left on brick, concrete, stone or pavers when water moves through the material and evaporates at the surface.", "/efflorescence-removal/"),
    ("Elevator pit", "The space at the bottom of an elevator hoistway, below the lowest landing, housing buffers and other equipment. It collects debris, water and oil.", "/elevator-pit-cleaning/"),
    ("Hot-water pressure washing", "Pressure washing with heated water, often called power washing, which cuts through oil, grease and gum faster than cold water.", "/commercial-power-washing/"),
    ("Hydro jetting", "Using very high-pressure water streams to scour build-up from inside pipes, condensers and lines.", "/industrial-power-washing/"),
    ("Lime run", "Hard white calcium carbonate deposits that streak from mortar joints, harder to remove than ordinary efflorescence.", "/efflorescence-removal/"),
    ("Micro blasting", "Precision blasting with very fine media at low pressure, used on detailed or delicate masonry and stubborn coatings.", "/historical-remediation/"),
    ("Poultice", "A paste applied to stone or brick that draws stains or paint ghosting out of the pores as it dries.", "/stone-restoration/"),
    ("Polymeric sand", "Joint sand for interlock pavers mixed with binders that harden when misted with water, resisting washout and weeds.", "/guides/interlock-cleaning-and-resanding/"),
    ("Pressure washing", "Cleaning with high-pressure water to remove dirt, grime and stains from durable surfaces like concrete and interlock.", "/residential-power-washing/"),
    ("Soda blasting", "Blasting with sodium bicarbonate, a soft media suited to delicate surfaces, soot and light coatings.", "/guides/is-sandblasting-safe-for-brick/"),
    ("Soft washing", "Low-pressure cleaning that uses biodegradable cleaners to kill and remove algae, mould and mildew from siding, stucco and roofs.", "/guides/soft-washing-vs-pressure-washing/"),
    ("Spalling", "Flaking or popping of the surface of brick, stone or concrete, often caused by trapped moisture freezing and thawing.", "/brick-cleaning-paint-removal/"),
    ("Sump pump", "A pump in a pit or basin that removes collected water. In elevator pits, sumps must be covered and working to prevent flooding.", "/elevator-pit-water-removal/"),
    ("Surface cleaner", "A rotary attachment for pressure washers that cleans flat surfaces evenly without the stripes a bare wand leaves.", "/guides/interlock-cleaning-and-resanding/"),
    ("WSIB clearance certificate", "A document from Ontario's Workplace Safety and Insurance Board confirming a contractor's account is in good standing.", "/guides/hiring-a-pressure-washing-contractor/"),
]
