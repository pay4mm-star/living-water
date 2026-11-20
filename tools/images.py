"""Map original Living Water photos to SEO filenames + alt text, export responsive WebP."""
import os, sys, json
from PIL import Image, ImageOps

SRC = "/home/claude/src/img/"
OUT = sys.argv[1] + "/assets/img/"
os.makedirs(OUT, exist_ok=True)

# key: (source, alt text)
IMAGES = {
    # hero / banners
    "heritage-stone-wall-pressure-washing-toronto": ("2026/08/pws2.png", "Living Water technician pressure washing a heritage stone church wall in Toronto"),
    "living-water-van-residential-pressure-washing": ("2026/08/11.png", "Living Water Pressure Wash Services van at a residential job in the GTA"),
    "industrial-pressure-washing-crew-gta": ("2026/08/industry.png", "Living Water industrial pressure washing van and equipment on site"),
    "roof-moss-removal-soft-wash": ("2026/08/resdensial.png", "Technician removing moss from a shingle roof with low-pressure soft washing"),
    "commercial-lobby-entrance-pressure-washing": ("2026/09/banner.webp", "Pressure washing the entrance and walkway of a commercial building"),
    "brick-wall-paint-removal-pressure-washing": ("2026/09/brick-paint.webp", "Controlled pressure washing removing paint from a commercial brick wall"),
    # before / after pairs
    "efflorescence-removal-front-steps-before": ("2026/06/Efflorescence-Cleaning-3-Before.webp", "Front porch steps covered in white efflorescence before cleaning"),
    "efflorescence-removal-front-steps-after": ("2026/06/Efflorescence-Cleaning-3-After.webp", "Front porch steps after professional efflorescence removal"),
    "brick-masonry-house-cleaning-before": ("2026/06/Masonry-Cleaning-1-Before.webp", "Brick house rear facade stained with mortar and grime before masonry cleaning"),
    "brick-masonry-house-cleaning-after": ("2026/06/Masonry-Cleaning-1-After.webp", "Brick house rear facade after professional masonry cleaning"),
    "boat-deck-mobile-power-wash-before": ("2026/06/Mobile-Power-Wash-1-Before.webp", "Sailboat deck with dirt and staining before mobile power washing"),
    "boat-deck-mobile-power-wash-after": ("2026/06/Mobile-Power-Wash-2-After.webp", "Sailboat deck bright and clean after mobile power washing"),
    "commercial-brick-paint-removal-before": ("2026/06/Paint-Removal-1-Before.webp", "Commercial brick building with patchy paint before paint removal"),
    "commercial-brick-paint-removal-after": ("2026/06/Paint-Removal-1-After.webp", "Commercial brick building after paint removal, uniform clean brick"),
    "stone-patio-cleaning-before": ("2026/06/Residential-Cleaning-2-Before.webp", "Stone patio and loggia with grime before residential pressure washing"),
    "stone-patio-cleaning-after": ("2026/06/Residential-Cleaning-2-After.webp", "Stone patio and loggia after residential pressure washing"),
    "heritage-facade-restoration-before": ("2026/08/12-old.jpg", "Ornate heritage building entrance darkened by decades of soot before restoration"),
    "heritage-facade-restoration-after": ("2026/08/12-edit.jpg", "Heritage building entrance after gentle facade cleaning and restoration"),
    "painted-building-paint-removal-before": ("2026/10/Paint-Removal-4-After.jpeg", "Downtown Toronto masonry building with patchy, weathered paint before restoration"),
    "painted-building-paint-removal-after": ("2026/10/Paint-Removal-4-Before.jpeg", "Downtown Toronto masonry building with a clean, uniform facade after restoration"),
    # project photos
    "heritage-red-brick-building-cleaning": ("2026/08/60787623430__C824A0E2-0610-4BA5-9C61-18E4BF7E14BF-scaled.jpg", "Red brick heritage building partly cleaned, showing the difference professional brick cleaning makes"),
    "concrete-surface-cleaning-residue-removal": ("2026/08/63933091846__CD9F03B4-6AE4-48F6-985D-C7B2BB54C31E.jpeg", "Concrete surface with residue being cleaned by a Living Water crew"),
    "ornamental-balcony-stone-restoration": ("2026/08/6ea2eea6-309d-4b9f-9866-45e5d8c08c19.jpg", "Contained stone balcony and wrought iron railing during restoration"),
    "media-blasting-stone-technician": ("2026/08/9292ba75-b02c-4d74-851d-701230c73efc.jpg", "Technician in protective suit media blasting a stone surface"),
    "elevator-pit-cleaning-toronto": ("2026/08/Elevator.webp", "Elevator pit cleaning and sludge removal in a Toronto building"),
    "historical-building-remediation-ontario": ("2026/08/Historical.webp", "Historic red brick building with clock tower after exterior remediation"),
    "rooftop-concrete-deck-pressure-washing": ("2026/08/IMG_0296.jpeg", "Rooftop concrete deck being pressure washed"),
    "commercial-column-cleaning-ladder": ("2026/08/IMG_0576.jpeg", "Cleaning a commercial building column from a ladder"),
    "modern-stone-home-exterior-cleaning": ("2026/08/IMG_0736.jpeg", "Modern stone and wood home exterior during cleaning"),
    "modern-stone-home-exterior-clean": ("2026/08/IMG_0753.jpeg", "Modern stone home exterior after professional cleaning"),
    "limestone-wall-hand-cleaning": ("2026/08/IMG_0982.jpeg", "Technician hand cleaning a limestone wall with drop sheets protecting the ground"),
    "boom-lift-brick-facade-cleaning": ("2026/08/IMG_1144.jpeg", "Crew on a boom lift cleaning a multi-storey brick facade"),
    "new-build-construction-cleanup": ("2026/08/IMG_1229.jpeg", "Post-construction exterior cleanup at a new modern home"),
    "brick-arch-window-cleaning": ("2026/08/IMG_6332-scaled.jpg", "Brick arch and window surround partly cleaned showing original colour"),
    "precast-stone-coping-cleaning": ("2026/08/IMG_7066.jpeg", "Precast stone copings side by side showing cleaned versus uncleaned"),
    "dustless-sandblasting-concrete": ("2026/08/Sandblasting.webp", "Technician performing dustless sandblasting on concrete"),
    "estate-home-exterior-restoration": ("2026/08/about-image-1.png", "Estate home with contained work area during exterior restoration"),
    "rooftop-terrace-pressure-washing-crew": ("2026/08/about-image-2.png", "Living Water crew pressure washing a rooftop terrace"),
    "custom-home-exterior-washing": ("2026/08/serv-1.png", "Custom home exterior with Living Water vans on site"),
    "industrial-tank-pressure-washing": ("2026/08/serv-3.png", "Industrial storage tanks being pressure washed from a boom lift"),
    "commercial-column-restoration": ("2026/08/serv-4.png", "Commercial column and storefront cleaning in Toronto"),
    "stone-house-exterior-cleaning": ("2026/08/serv-5.png", "Stone house exterior after professional washing"),
    "elevator-pit-pressure-washing": ("2026/08/service-image-2-1.png", "Technician pressure washing inside an elevator pit"),
    "elevator-pit-buffer-cleaning": ("2026/08/service-image-4.png", "Elevator pit buffer springs and floor after cleaning"),
    "silo-tank-exterior-cleaning-boom-lift": ("2026/09/11.webp", "Silo tank exterior being cleaned from a boom lift"),
    "silo-tank-wash-progress": ("2026/09/IMG_0603.jpeg", "Tall silo tank with cleaned and uncleaned sections visible"),
    "condo-column-pressure-washing": ("2026/09/IMG_0609.jpeg", "Condo building column being pressure washed from a ladder"),
    "graffiti-removal-house-wall": ("2026/09/IMG_0759.jpeg", "Living Water technician removing graffiti from a house wall"),
    "brick-wall-cleaning-technician": ("2026/09/IMG_0806-1.jpeg", "Living Water technician cleaning a light brick wall"),
    "crane-heavy-equipment-washing": ("2026/09/IMG_0863.jpeg", "Crawler crane being pressure washed on a construction site"),
    "slate-pathway-cleaning-before": ("2026/09/IMG_2972.jpeg", "Slate garden pathway covered in grime and organic growth"),
    "garden-stone-pathway-cleaned": ("2026/09/IMG_2979.jpeg", "Garden stone pathway after pressure washing"),
    "yellow-brick-wall-cleaning": ("2026/09/brick.png", "Yellow brick wall cleaning on a commercial building"),
    "commercial-building-exterior-washing": ("2026/09/commercial.webp", "Commercial building exterior and entrance washing in Toronto"),
    "elevator-pit-springs-cleaned": ("2026/09/gallery-item.png", "Elevator pit springs and equipment after decontamination"),
    "paint-stripping-wall-surface": ("2026/09/image0.jpeg", "Wall surface with peeling paint during paint stripping"),
    "century-home-pressure-washing": ("2026/09/residential-2.webp", "Century brick home with Living Water van parked out front"),
    "estate-home-driveway-washing": ("2026/09/residential.webp", "Estate home driveway and front steps being pressure washed"),
    "heritage-building-scaffolding-restoration": ("2026/10/IMG_1558-scaled.jpeg", "Heritage building wrapped and contained for restoration with a boom lift"),
    "heritage-building-contained-blasting": ("2026/10/IMG_1583-scaled.jpeg", "Heritage building facade under containment for blasting"),
    "yellow-brick-heritage-building-cleaning": ("2026/10/IMG_4906.jpeg", "Yellow brick heritage building being cleaned with boom lifts"),
    "wind-damage-deck-tree": ("2026/06/Wind-damage.webp", "Fallen tree on a backyard deck after a wind storm"),
    "parking-lot-pressure-washing-crew": ("slider/cache/9bc7773465a9c6815fb3d50efb8c8292/slide-1.webp", "Two technicians pressure washing a parking lot"),
    "brick-storefront-boom-lift-washing": ("slider/cache/12b3f4c3339e95fe6dba032c0dff2cf2/slide-2.webp", "Brick storefront being washed from a boom lift"),
    "crane-track-degreasing": ("slider/cache/4f9df2b81154b61b6dd242f23b70f24c/slide-3.webp", "Technician degreasing crane tracks"),
    "brick-wall-low-pressure-wash": ("slider/cache/f5412d4fd698f44a2b3ef07c7240cfe3/slide-4.webp", "Technician washing a brick wall in high-visibility gear"),
    "roof-moss-washing-ladder": ("slider/cache/f209caf2aa3a9be969e9f011eaabfa73/slide-5.webp", "Technician on a ladder washing moss off a roof"),
}

WIDTHS = [320, 640, 960, 1280, 1600]
manifest = {}
for key, (src, alt) in IMAGES.items():
    im = ImageOps.exif_transpose(Image.open(SRC + src)).convert("RGB")
    w, h = im.size
    sizes = []
    for tw in WIDTHS:
        if tw > w and sizes:
            break
        tw = min(tw, w)
        th = round(h * tw / w)
        im.resize((tw, th), Image.LANCZOS).save(f"{OUT}{key}-{tw}.webp", "WEBP", quality=72, method=6)
        sizes.append(tw)
        if tw == w:
            break
    manifest[key] = {"alt": alt, "w": w, "h": h, "sizes": sizes}

# Open Graph image 1200x630 JPEG
og = ImageOps.fit(Image.open(SRC + "2026/08/pws2.png").convert("RGB"), (1200, 630), Image.LANCZOS)
og.save(OUT + "og-living-water-pressure-washing.jpg", quality=82)

# logos / icons (copied as-is, they are brand assets)
Image.open(SRC + "2026/08/logo-1.png").save(OUT + "living-water-logo.png", optimize=True)
Image.open(SRC + "2026/08/logo-1.png").save(OUT + "living-water-logo.webp", "WEBP", quality=90)
Image.open(SRC + "2026/08/logo-1.png").resize((440, 70), Image.LANCZOS).save(OUT + "living-water-logo-440.webp", "WEBP", quality=90)
Image.open(SRC + "2026/07/Living-Water-logo_28-2.webp").save(OUT + "living-water-28-years-logo.webp", "WEBP", quality=90)
Image.open(SRC + "2026/08/80b5b04f8328fb7d00e570e90fa968922541d53d.png").save(OUT + "living-water-logo-footer.png", optimize=True)
for s in (180, 192, 270):
    Image.open(SRC + f"2026/05/logo{s}.png").save(sys.argv[1] + f"/assets/icons/icon-{s}.png", optimize=True) if os.makedirs(sys.argv[1] + "/assets/icons", exist_ok=True) is None else None
Image.open(SRC + "2026/05/logo270.png").resize((512, 512), Image.LANCZOS).save(sys.argv[1] + "/assets/icons/icon-512.png", optimize=True)
Image.open(SRC + "2026/05/logo192.png").resize((32, 32), Image.LANCZOS).save(sys.argv[1] + "/favicon.ico", sizes=[(32, 32)])

json.dump(manifest, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "manifest.json"), "w"), indent=1)
print(len(manifest), "images")
