# Post-build pass: give each page an honest dateModified/lastmod = the last day its content actually changed.
# Registry lives in tools/lastmod.json. Executed in gen.py namespace (TODAY, OUT, SITE, PAGES available).
import hashlib, json, os, re, subprocess

_REG = os.path.join(HERE, "lastmod.json")
_SEED = "2026-11-26"   # date every page was last stamped before this mechanism existed
_PH = "@@LASTMOD@@"
_reg = json.load(open(_REG)) if os.path.exists(_REG) else None
_first = _reg is None
_reg = _reg or {}
_dates = {}


def _norm(t, stamps):
    for s in stamps:
        t = t.replace(s, _PH)
    return t


def _hash(t):
    return hashlib.sha1(t.encode()).hexdigest()


def _head_norm(rel):
    try:
        return subprocess.run(["git", "show", f"HEAD:{rel}"], cwd=OUT, capture_output=True, text=True, check=True).stdout
    except Exception:
        return None


for p, _pr in PAGES:
    rel = p.strip("/") + "/index.html" if p != "/" else "index.html"
    fp = os.path.join(OUT, rel)
    if not os.path.exists(fp):
        continue
    txt = open(fp).read()
    norm = _norm(txt, [TODAY])
    h = _hash(norm)
    ent = _reg.get(p)
    if ent and ent["h"] == h:
        d = ent["d"]
    elif _first:
        head = _head_norm(rel)
        if head is not None and _hash(_norm(head, [_SEED])) == h:
            d = _SEED
        else:
            d = TODAY
        _reg[p] = {"h": h, "d": d}
    else:
        d = TODAY
        _reg[p] = {"h": h, "d": d}
    _dates[p] = d
    if d != TODAY:
        open(fp, "w").write(norm.replace(_PH, d))

for sm in ("sitemap.xml",):
    fp = os.path.join(OUT, sm)
    if os.path.exists(fp):
        t = open(fp).read()
        t = re.sub(r"<loc>" + re.escape(SITE) + r"([^<]*)</loc><lastmod>[^<]*</lastmod>",
                   lambda m: f"<loc>{SITE}{m.group(1)}</loc><lastmod>{_dates.get(m.group(1), TODAY)}</lastmod>", t)
        open(fp, "w").write(t)
json.dump(_reg, open(_REG, "w"), indent=0, sort_keys=True)
