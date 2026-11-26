# Contextual internal linking + freshness. Executed in gen.py namespace.
import re as _re2

# phrase (case-insensitive) -> url. First match per page is linked, longest phrases first.
LINK_MAP = {
    "post-construction masonry cleaning": "/masonry-cleaning-for-home-builders/",
    "masonry cleaning for home builders": "/masonry-cleaning-for-home-builders/",
    "interlock cleaning cost": "/interlock-cleaning-sealing-cost-calculator/",
    "interlock cost calculator": "/interlock-cleaning-sealing-cost-calculator/",
    "wash, sand and seal": "/interlock-wash-sand-seal-3-50-per-sq-ft/",
    "soft washing": "/guides/soft-washing-vs-pressure-washing/",
    "soft wash": "/guides/soft-washing-vs-pressure-washing/",
    "efflorescence": "/efflorescence-removal/",
    "elevator pit": "/elevator-pit-cleaning/",
    "elevator pits": "/elevator-pit-cleaning/",
    "graffiti": "/graffiti-removal/",
    "sandblasting": "/sandblasting-services/",
    "media blasting": "/guides/is-sandblasting-safe-for-brick/",
    "soda blasting": "/guides/is-sandblasting-safe-for-brick/",
    "micro blasting": "/guides/is-sandblasting-safe-for-brick/",
    "paint removal": "/brick-cleaning-paint-removal/",
    "brick cleaning": "/brick-cleaning-paint-removal/",
    "interlock": "/driveway-interlock-cleaning/",
    "driveway": "/driveway-interlock-cleaning/",
    "driveways": "/driveway-interlock-cleaning/",
    "roofs": "/roof-cleaning/",
    "moss": "/roof-cleaning/",
    "siding": "/house-washing/",
    "decks": "/deck-fence-cleaning/",
    "sealing": "/paver-stone-sealing/",
    "sealer": "/paver-stone-sealing/",
    "parking garages": "/parking-garage-cleaning/",
    "garages": "/parking-garage-cleaning/",
    "polymeric sand": "/guides/interlock-cleaning-and-resanding/",
    "heritage": "/historical-remediation/",
    "natural stone": "/stone-restoration/",
    "rust removal": "/metal-restoration/",
    "hydro jetting": "/industrial-power-washing/",
    "fire damage": "/disaster-restoration/",
    "water damage": "/disaster-restoration/",
    "mould remediation": "/disaster-restoration/",
    "sewage backup": "/elevator-pit-water-removal/",
    "property managers": "/industries/",
    "condominium boards": "/industries/",
    "fixed written quote": "/guides/pressure-washing-cost-factors/",
    "WSIB": "/guides/hiring-a-pressure-washing-contractor/",
    "Toronto": "/pressure-washing-toronto/",
    "Mississauga": "/pressure-washing-mississauga/",
    "Vaughan": "/pressure-washing-vaughan/",
    "Markham": "/pressure-washing-markham/",
    "Richmond Hill": "/pressure-washing-richmond-hill/",
    "North York": "/pressure-washing-north-york/",
    "Oakville": "/pressure-washing-oakville/",
    "Hamilton": "/pressure-washing-hamilton/",
}
MAX_LINKS = 6


def autolink(body, path):
    m = _re2.search(r'(<article class="prose[^"]*">)(.*?)(</article>)', body, _re2.S)
    if not m:
        return body
    art = m.group(2)
    used, count = set(), 0
    phrases = sorted(LINK_MAP, key=len, reverse=True)
    parts = _re2.split(r"(<[^>]+>)", art)
    stack = []  # open tags that block linking
    out = []
    for part in parts:
        if part.startswith("<"):
            t = _re2.match(r"</?\s*([a-z0-9]+)", part, _re2.I)
            name = t.group(1).lower() if t else ""
            if name in ("a", "h1", "h2", "h3", "summary", "strong", "th", "button", "label", "nav"):
                if part.startswith("</"):
                    if stack and stack[-1] == name: stack.pop()
                elif not part.endswith("/>"):
                    stack.append(name)
            out.append(part)
            continue
        if stack or count >= MAX_LINKS or not part.strip():
            out.append(part); continue
        for ph in phrases:
            url = LINK_MAP[ph]
            if url in used or url == path or count >= MAX_LINKS:
                continue
            flags = 0 if ph[0].isupper() else _re2.I
            mm = _re2.search(r"(?<![\w/-])" + _re2.escape(ph) + r"(?![\w-])", part, flags)
            if mm:
                part = part[:mm.start()] + f'<a href="{url}">{mm.group(0)}</a>' + part[mm.end():]
                used.add(url); count += 1
                # only one link per text node to keep it readable
                break
        out.append(part)
    return body[:m.start(2)] + "".join(out) + body[m.end(2):]


def reviewed_line():
    return f'<p class="reviewed">Reviewed by the Living Water team · {datetime.date.today().strftime("%B %Y")} · 28 years of field experience</p>'
