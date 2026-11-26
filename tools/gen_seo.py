# Extra FAQs per service page (answer-engine / long-tail coverage). Executed in gen.py namespace before service pages are generated.
_Q = "Every job is a fixed written quote after a free assessment, so you know the price before work starts."
import re as _re
EXTRA_FAQS = {
"residential-power-washing": [
 ("How much does residential pressure washing cost in Toronto?", f"Price depends on the surfaces, their size and their condition. {_Q} As a reference, our interlock wash, sand and seal package is $3.50 per square foot plus HST."),
 ("Is pressure washing safe for my lawn and plants?", "Yes. We use biodegradable cleaners, pre-wet and rinse nearby plants, and protect landscaping and windows before we start."),
 ("What is the best time of year to pressure wash a house in Ontario?", "From spring thaw through fall, when temperatures stay above freezing and surfaces dry properly. Spring is popular for removing winter salt, and fall for cleaning before sealing and freeze-thaw."),
 ("Which parts of the GTA do you serve for home washing?", "Toronto, North York, Scarborough, Etobicoke, Mississauga, Brampton, Vaughan, Markham, Richmond Hill, Oakville, Burlington, Hamilton, Pickering, Whitby, Oshawa, Newmarket, Aurora and Barrie.")],
"commercial-power-washing": [
 ("How is commercial pressure washing priced?", f"By the area, the surface, how dirty it is, access, and how often we visit. Recurring programs are priced lower per visit than one-off cleans. {_Q}"),
 ("Can you remove gum, grease and stains from storefront sidewalks?", "Yes. Hot-water pressure washing and surface cleaners lift gum, grease and ground-in stains from sidewalks, entrances and plazas, and we work early morning or after hours so customers are not disrupted."),
 ("Can you wash tall building facades?", "Yes. We use boom lifts, ladders and pole systems to wash brick, stone and precast facades and signs safely, with the area coned off and protected."),
 ("Do you clean schools, hospitals and offices?", "Yes. We have washed school buildings, hospital entrances, office campuses and condo podiums, and we work around operating hours and safety rules on site.")],
"industrial-power-washing": [
 ("Do you clean storage tanks and silos?", "Yes. We wash tank and silo exteriors and roofs from boom lifts and, where needed, interiors, with a written site safety plan."),
 ("Can you work during plant shutdowns or overnight?", "Yes. We schedule around shutdowns and run overnight shifts so production is not interrupted."),
 ("Can you degrease heavy equipment such as cranes and machinery?", "Yes. Hot water and industrial degreasers remove oil, mud and build-up from tracks, undercarriages and engine bays on cranes and other heavy equipment."),
 ("How is industrial cleaning priced?", f"By scope, access, hazards and time on site. {_Q}")],
"sandblasting-services": [
 ("What is the difference between sandblasting and media blasting?", "Sandblasting is a general name for abrasive blasting. Media blasting uses a chosen material, such as soda, glass or dry ice, matched to the surface, so softer materials like brick, stone and aluminium can be cleaned with less risk of damage."),
 ("What surfaces can you blast?", "Steel, aluminium, concrete, brick, stone, wood and swimming pool shells, depending on the coating and the finish required."),
 ("How messy is mobile sandblasting?", "We contain the work area, protect landscaping and windows, and collect the debris. Dustless blasting uses water to cut dust dramatically compared with dry blasting."),
 ("How much does sandblasting cost?", f"It depends on the surface, the coating being removed and access. {_Q}")],
"brick-cleaning-paint-removal": [
 ("How much does paint removal from brick cost?", f"It varies with the type of paint, how many layers there are, and the size and height of the wall. {_Q}"),
 ("Will cleaning change the colour of my brick?", "Cleaning reveals the brick's original colour by removing soot, paint and staining. We test a small area first so you can see the result before we continue."),
 ("How long does brick paint removal take?", "A small house wall can take a day or two. Larger buildings take longer, depending on the coating and access. We confirm the schedule in your quote."),
 ("Can you clean tall brick buildings?", "Yes. We clean from boom lifts and lift baskets, mask windows and protect surrounding areas before starting.")],
"historical-remediation": [
 ("How do you protect heritage masonry during cleaning?", "We test methods on a small hidden area, use the gentlest method that works, contain overspray and runoff, and mask windows, trim and landscaping."),
 ("Do you restore churches, monuments and statues?", "Yes. We have cleaned heritage stone walls, limestone entrances and balconies and ornamental details across Toronto and Ontario."),
 ("How much does heritage building restoration cost?", f"Heritage work is priced from the surface, the extent of soiling or coating and access needs. {_Q}")],
"disaster-restoration": [
 ("What types of damage do you handle?", "Fire and smoke, water and flood, wind and storm damage, and mould, for homes and commercial properties across Toronto and the GTA."),
 ("When should I call after a flood or fire?", "As soon as it is safe. Water and smoke damage spread quickly, so calling right away limits the damage. Emergency line: (647) 833-4343, 24/7."),
 ("Will you document the damage for my insurer?", "Yes. We take before-and-after photos and written notes you can send to your insurance adjuster.")],
"elevator-pit-cleaning": [
 ("How do I choose an elevator pit cleaning company?", "Look for a contractor with $5M liability insurance, WSIB clearance, experience coordinating with your elevator company, after-hours availability and a photo report. Living Water provides all of these and a fixed written price."),
 ("Do you clean elevator pits in the middle of winter?", "Yes. Winter is the busiest season because of salt slush and meltwater, and we work overnight and on weekends so elevators are back in service quickly.")],
"elevator-pit-water-removal": [
 ("How much does elevator pit water removal cost?", "Our elevator pit cleaning starts at $1,500 for a single pit with up to 4 inches of water, including full cleaning and sanitizing ready for paint. Deeper water, oil or sewage is quoted separately. See <a href=\"/elevator-pit-cleaning/\">elevator pit cleaning prices</a>."),
 ("Who should I call first if there is water in an elevator pit?", "Take the elevator out of service and call your elevator contractor, then call Living Water at (647) 833-4343 for pump-out and clean-up, 24/7.")],
"efflorescence-removal": [
 ("How do you remove efflorescence from pavers and stone?", "We use cleaners matched to the surface, applied and agitated carefully and rinsed thoroughly, because pressure washing alone only drives moisture back in. We then recommend letting the surface dry before sealing."),
 ("Will efflorescence come back?", "It can return while moisture is still moving through the masonry, especially on new work. Removing it and then fixing moisture sources, and sealing when the surface is dry, reduces repeat blooms."),
 ("How much does efflorescence removal cost?", f"It depends on the material, the area and how severe the blooming is. {_Q}")],
"graffiti-removal": [
 ("How much does graffiti removal cost?", f"It depends on the surface, the paint and the area. {_Q}"),
 ("Can graffiti be removed from brick without damaging it?", "Yes. We choose the gentlest remover and pressure setting that works on the brick, mortar and paint, and test first."),
 ("Do you offer recurring graffiti removal for property managers?", "Yes. We set up one-off or recurring response for properties that are hit repeatedly, often removing graffiti within the same week.")],
"stone-restoration": [
 ("How do you clean natural stone steps and walls?", "We match the cleaner and pressure to the stone, rinse thoroughly and test a small area first, removing grime, algae, mineral deposits and stains without etching or eroding the surface."),
 ("Can rust stains be removed from stone?", "Usually yes. Rust is treated with a specialised remover chosen for the stone, as we have done on stone cladding and rooftop decks."),
 ("How much does stone cleaning cost?", f"It depends on the stone, area, height and staining. {_Q}")],
"metal-restoration": [
 ("How is rust removed from metal?", "Depending on the metal and finish, we use cleaning, abrasive or media blasting to remove rust, scale and old coatings, and can leave the metal ready for primer and paint."),
 ("Can you clean and degrease heavy equipment?", "Yes. We wash and degrease tracks, undercarriages and machinery on cranes and other equipment, on site."),
 ("How much does metal restoration cost?", f"It depends on the metal, the condition and the size. {_Q}")],
"driveway-interlock-cleaning": [
 ("How much does interlock cleaning cost?", "Our full wash, polymeric sand and seal package is $3.50 per square foot plus HST. For example, a 400 sq ft double driveway is $1,400 before HST. Use the <a href=\"/interlock-cleaning-sealing-cost-calculator/\">interlock cost calculator</a> for your own measurements."),
 ("How long does it take to clean and seal an interlock driveway?", "Most residential driveways are cleaned and re-sanded in a day. Sealing needs the interlock to be completely dry, so we schedule around the weather and tell you how long to keep cars off."),
 ("Why are there weeds growing in my interlock joints?", "Joint sand washes out over time, letting seeds and moss take hold. Cleaning removes the old sand, and fresh polymeric sand locks the joints so weeds and ants stay out.")],
"house-washing": [
 ("How much does it cost to pressure wash a house in Toronto?", f"It depends on the size, the siding or masonry and how dirty it is. {_Q}"),
 ("Is house washing safe for windows and plants?", "Yes. We use low pressure and biodegradable cleaners, mask or protect sensitive areas, and rinse nearby plants before and after."),
 ("Do you wash soffits, fascia and trim?", "Yes. Soffits, fascia, trim and gutters' exteriors can be included in a house wash.")],
"roof-cleaning": [
 ("How much does roof cleaning cost?", f"It depends on the roof size, pitch and type. {_Q}"),
 ("How long does it take for moss to disappear after roof cleaning?", "Moss is killed by the treatment and then rinses away, with most visible results appearing in the following days to weeks."),
 ("Is it safe to clean a cedar or asphalt roof?", "Yes, with low-pressure soft washing. High-pressure washing strips granules and splits cedar, so we do not use it on roofs.")],
"deck-fence-cleaning": [
 ("Do you clean boat decks, pool decks and rooftop terraces?", "Yes. We also do mobile power washing of boat decks, plus pool decks, balconies and rooftop terraces."),
 ("How much does deck and fence cleaning cost?", f"It depends on the area, the material and the condition. {_Q}"),
 ("Can you clean pergolas and railings?", "Yes. Pergolas, railings, fences and decks are cleaned with wood-safe methods that avoid raising the grain.")],
"paver-stone-sealing": [
 ("How much does paver sealing cost?", "Our wash, sand and seal package for interlock is $3.50 per square foot plus HST. Try the <a href=\"/interlock-cleaning-sealing-cost-calculator/\">cost calculator</a>."),
 ("When is the best time to seal pavers?", "When the pavers are clean, completely dry, and temperatures are mild, typically late spring through early fall in Ontario."),
 ("Does sealing change the look of pavers?", "A sealer enriches colour and can add sheen depending on the product. We tell you what finish to expect before we start.")],
"parking-garage-cleaning": [
 ("How much does parking garage cleaning cost?", f"It depends on the number of levels, the area and the condition. {_Q}"),
 ("What is the best time of year to wash a parking garage?", "Spring, after a winter of road salt, sand and grime, is the most common time. Many condo boards also schedule a fall clean."),
 ("Do you flush the floor drains?", "Yes. We flush drains and work level by level so the garage stays usable.")],
}
for _s, _l in EXTRA_FAQS.items():
    _have = {q for q, _ in SERVICES[_s]["faqs"]}
    SERVICES[_s]["faqs"] = SERVICES[_s]["faqs"] + [(q, _re.sub(r"<a [^>]*>(.*?)</a>", r"\1", a)) for q, a in _l if q not in _have]
