"""Import a folder of job photos into the site as case-study projects.

Folder layout (one sub-folder per job):

    photos/
      north-york-condo-elevator-pit/
        before.jpg  after.jpg          (or before-1.jpg / after-1.jpg, before-2.jpg ...)
        other.jpg                      (any extra photos)
        notes.txt                      (optional, see below)

notes.txt (all lines optional):
    title: Condo elevator pit clean-up after winter
    service: elevator-pit-cleaning          # a service slug, e.g. residential-power-washing
    location: North York                    # a city/area name
    date: 2026-10
    description: Two-elevator condo pit with salt sludge and standing water...

Run from the repo root:  python3 tools/add_photos.py /path/to/photos
Then rebuild:            python3 tools/gen.py .
"""
import os, re, sys, json
from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets/img")
PROJ = os.path.join(ROOT, "tools/projects")
MANIFEST = os.path.join(ROOT, "tools/manifest.json")
WIDTHS = [320, 640, 960, 1280, 1600]
EXTS = (".jpg", ".jpeg", ".png", ".webp", ".heic")


def slug(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")[:70]


def export(src, key, alt, manifest):
    try:
        im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    except Exception as e:
        print("  skip", src, e); return None
    w, h = im.size
    sizes = []
    for tw in WIDTHS:
        if tw > w and sizes: break
        tw = min(tw, w)
        im.resize((tw, round(h * tw / w)), Image.LANCZOS).save(f"{IMG}/{key}-{tw}.webp", "WEBP", quality=72, method=6)
        sizes.append(tw)
        if tw == w: break
    manifest[key] = {"alt": alt, "w": w, "h": h, "sizes": sizes}
    return key


def main(folder):
    os.makedirs(PROJ, exist_ok=True)
    manifest = json.load(open(MANIFEST))
    for name in sorted(os.listdir(folder)):
        d = os.path.join(folder, name)
        if not os.path.isdir(d): continue
        notes = {}
        nf = os.path.join(d, "notes.txt")
        if os.path.exists(nf):
            for line in open(nf, encoding="utf-8", errors="ignore"):
                if ":" in line:
                    k, v = line.split(":", 1); notes[k.strip().lower()] = v.strip()
        title = notes.get("title") or name.replace("-", " ").replace("_", " ").strip().capitalize()
        pslug = slug(notes.get("slug") or title)
        loc = notes.get("location", "")
        service = notes.get("service", "")
        base = slug(f"{title} {loc}") if loc and slug(loc) not in slug(title) else slug(title)
        files = sorted(f for f in os.listdir(d) if f.lower().endswith(EXTS))
        pairs, extras = {}, []
        for f in files:
            m = re.match(r"(before|after)[-_ ]?(\d*)", f.lower())
            if m:
                pairs.setdefault(m.group(2) or "1", {})[m.group(1)] = f
            else:
                extras.append(f)
        where = f" in {loc}" if loc else ""
        proj = {"slug": pslug, "title": title, "service": service, "location": loc, "date": notes.get("date", ""),
                "description": notes.get("description", ""), "pairs": [], "photos": []}
        for n, p in sorted(pairs.items()):
            if "before" in p and "after" in p:
                b = export(os.path.join(d, p["before"]), f"{base}-before-{n}", f"{title}{where} — before", manifest)
                a = export(os.path.join(d, p["after"]), f"{base}-after-{n}", f"{title}{where} — after", manifest)
                if b and a: proj["pairs"].append([b, a])
            else:
                extras += list(p.values())
        for i, f in enumerate(extras, 1):
            k = export(os.path.join(d, f), f"{base}-{i}", f"{title}{where} — photo {i}", manifest)
            if k: proj["photos"].append(k)
        json.dump(proj, open(os.path.join(PROJ, pslug + ".json"), "w"), indent=1)
        print(f"project: {pslug}  pairs={len(proj['pairs'])} photos={len(proj['photos'])}")
    json.dump(manifest, open(MANIFEST, "w"), indent=1)


if __name__ == "__main__":
    main(sys.argv[1])
