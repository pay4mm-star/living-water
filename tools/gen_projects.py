# Case-study project pages from tools/projects/*.json (created by add_photos.py). Executed in gen.py namespace.
import glob as _glob

PROJECTS = []
for _f in sorted(_glob.glob(os.path.join(HERE, "projects", "*.json"))):
    _p = json.load(open(_f))
    _p["pairs"] = [x for x in _p.get("pairs", []) if x[0] in M and x[1] in M]
    _p["photos"] = [x for x in _p.get("photos", []) if x in M]
    if _p["pairs"] or _p["photos"]:
        PROJECTS.append(_p)
PROJECTS.sort(key=lambda p: p.get("date", ""), reverse=True)


def projects_for(service=None, location=None):
    out = []
    for p in PROJECTS:
        if service and p.get("service") == service: out.append(p)
        elif location and location.lower() in (p.get("location") or "").lower(): out.append(p)
    return out


def project_card(p):
    k = p["pairs"][0][1] if p["pairs"] else p["photos"][0]
    meta = " · ".join(x for x in [SERVICES.get(p.get("service"), {}).get("nav", ""), p.get("location", ""), p.get("date", "")] if x)
    return (f'<article class="card">{img(k, "(max-width: 640px) 100vw, 33vw")}<div class="body"><span class="tag">Case study</span>'
            f'<h3><a href="/projects/{p["slug"]}/">{esc(p["title"])}</a></h3><p>{esc(meta)}</p><span class="more">View project →</span></div></article>')


def projects_section(service=None, location=None):
    ps = projects_for(service, location)[:3]
    if not ps:
        return ""
    return f'<section><div class="wrap"><div class="section-head"><span class="pill light">Case studies</span><h2>Recent projects</h2></div><div class="grid g3">{"".join(project_card(p) for p in ps)}</div></div></section>'


def project_page(p):
    path = f"/projects/{p['slug']}/"
    trail = [("Home", "/"), ("Projects", "/projects/"), (p["title"], path)]
    svc = SERVICES.get(p.get("service"))
    hero = p["pairs"][0][1] if p["pairs"] else p["photos"][0]
    pairs = "".join(ba(b, a, "Before & after", "") for b, a in p["pairs"])
    photos = "".join(photo(k) for k in p["photos"])
    facts = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in [
        ("Service", f'<a href="/{p["service"]}/">{esc(svc["nav"])}</a>' if svc else ""),
        ("Location", esc(p.get("location", ""))), ("Completed", esc(p.get("date", "")))] if v)
    loc = f" in {p['location']}" if p.get("location") else ""
    summary = p.get("description") or f"{svc['nav'] if svc else 'Cleaning and restoration'} project{loc} completed by Living Water Pressure Wash Services."
    body = f"""
<section class="page-hero"><picture>{hero_img(hero)}</picture>
<div class="wrap">{crumbs_html(trail)}<span class="pill">Case study</span><h1>{esc(p["title"])}{esc(loc) if loc and p["location"].lower() not in p["title"].lower() else ""}</h1></div></section>
<section><div class="wrap layout"><article class="prose">
<p class="answer">{esc(summary)}</p>
<div class="facts"><dl>{facts}</dl></div>
{('<h2>Before &amp; after</h2><div class="grid ' + ('g2' if len(p["pairs"]) > 1 else '') + '">' + pairs + '</div>') if pairs else ""}
{('<h2>On the job</h2><div class="grid g2">' + photos + '</div>') if photos else ""}
</article><aside class="side">{quote_aside()}{('<div><h3>This service</h3><nav class="related"><a href="/' + p["service"] + '/">' + esc(svc["nav"]) + ' →</a></nav></div>') if svc else ""}</aside></div></section>
{cta_block()}"""
    ld_ = {"@context": "https://schema.org", "@type": "CreativeWork", "name": p["title"], "about": svc["service_type"] if svc else "Pressure washing",
           "creator": {"@id": ORG_ID}, "locationCreated": {"@type": "Place", "name": p.get("location") or "Greater Toronto Area"},
           "dateCreated": p.get("date") or None, "image": [SITE + best(k) for pr in p["pairs"] for k in pr] + [SITE + best(k) for k in p["photos"]]}
    ld_ = {k: v for k, v in ld_.items() if v}
    title = f"{p['title']}{loc} | Living Water"
    page(path, title[:70], summary[:158], body, schema=[ld_, crumbs_ld(trail)], preload=hero, priority="0.6", crumbs=True)


def projects_hub():
    if not PROJECTS:
        return
    path = "/projects/"
    trail = [("Home", "/"), ("Projects", path)]
    body = f"""
<section class="page-hero"><div class="wrap">{crumbs_html(trail)}<span class="pill">Case studies</span><h1>Recent Projects &amp; Case Studies</h1><p>Real Living Water jobs across Toronto and the GTA — before and after.</p></div></section>
<section><div class="wrap"><div class="grid g3">{"".join(project_card(p) for p in PROJECTS)}</div></div></section>
{cta_block()}"""
    page(path, "Projects & Case Studies | Living Water Pressure Washing",
         "Before-and-after case studies of Living Water pressure washing, elevator pit cleaning, brick, stone and heritage restoration projects across the GTA.",
         body, schema=[crumbs_ld(trail)], priority="0.7", page_type="CollectionPage", crumbs=True)
    for p in PROJECTS:
        project_page(p)
