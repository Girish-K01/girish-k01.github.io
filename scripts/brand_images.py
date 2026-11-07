"""Generate the site's social preview card and favicon set.

Usage (needs Pillow; macOS system fonts are used for the lettering):
    python3 -m venv /tmp/brand && /tmp/brand/bin/pip install pillow
    /tmp/brand/bin/python scripts/brand_images.py

Re-run after changing the name, tagline or profile photo. Writes into images/.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / "images"

NAME = "Girish Kulathumani"
TAGLINE = "EEG/EMG decoding · Federated learning"
SEEKING = "Open to research engineer, RA and PhD roles"
URL = "girish-k01.github.io"
PHOTO = IMAGES / "profile_pic.jpg"

BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
REGULAR = "/System/Library/Fonts/Supplemental/Arial.ttf"

BG_LEFT, BG_RIGHT = (11, 15, 25), (17, 26, 46)  # site dark theme background
WHITE, CYAN, SLATE, GREY = (243, 244, 246), (56, 189, 248), (203, 213, 225), (156, 163, 175)
BLUE = (37, 99, 235)  # light theme link colour


def font(path, size):
    return ImageFont.truetype(path, size)


def og_card():
    w, h = 1200, 630
    card = Image.new("RGB", (w, h))
    draw = ImageDraw.Draw(card)
    for x in range(w):  # horizontal gradient
        t = x / (w - 1)
        draw.line([(x, 0), (x, h)], fill=tuple(round(a + (b - a) * t) for a, b in zip(BG_LEFT, BG_RIGHT)))

    left = 80
    draw.rectangle([left, 150, left + 72, 156], fill=CYAN)
    draw.text((left, 180), NAME, font=font(BOLD, 74), fill=WHITE)
    draw.text((left, 290), TAGLINE, font=font(REGULAR, 38), fill=CYAN)
    draw.text((left, 350), SEEKING, font=font(REGULAR, 30), fill=SLATE)
    draw.text((left, 520), URL, font=font(REGULAR, 28), fill=GREY)

    # Circular photo on the right. The source photo is small, so keep it near 1:1.
    size = 230
    photo = Image.open(PHOTO).convert("RGB")
    side = min(photo.size)
    photo = photo.crop(((photo.width - side) // 2, 0, (photo.width + side) // 2, side)).resize((size, size), Image.LANCZOS)
    mask = Image.new("L", (size * 4, size * 4), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, size * 4 - 1, size * 4 - 1], fill=255)
    mask = mask.resize((size, size), Image.LANCZOS)
    cx, cy = 975, 315
    ring = 6
    draw.ellipse([cx - size // 2 - ring, cy - size // 2 - ring, cx + size // 2 + ring, cy + size // 2 + ring], fill=CYAN)
    card.paste(photo, (cx - size // 2, cy - size // 2), mask)

    out = IMAGES / "og-card.png"
    card.save(out, optimize=True)
    print("wrote", out.relative_to(ROOT), card.size)


def monogram(px):
    scale = 4  # draw large, then downsample for smooth edges
    big = px * scale
    img = Image.new("RGBA", (big, big), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([0, 0, big - 1, big - 1], radius=round(big * 0.22), fill=BLUE)
    f = font(BOLD, round(big * 0.5))
    box = draw.textbbox((0, 0), "GK", font=f)
    tw, th = box[2] - box[0], box[3] - box[1]
    draw.text(((big - tw) / 2 - box[0], (big - th) / 2 - box[1]), "GK", font=f, fill=(255, 255, 255))
    return img.resize((px, px), Image.LANCZOS)


def favicons():
    for px, name in [(32, "favicon-32x32.png"), (192, "favicon-192x192.png"), (512, "favicon-512x512.png")]:
        monogram(px).save(IMAGES / name, optimize=True)
    # iOS draws its own rounded corners and dislikes transparency
    touch = Image.new("RGB", (180, 180), BLUE)
    touch.paste(monogram(180), (0, 0), monogram(180))
    touch.save(IMAGES / "apple-touch-icon-180x180.png", optimize=True)
    monogram(48).save(IMAGES / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    (IMAGES / "favicon.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
        '<rect width="64" height="64" rx="14" fill="#2563EB"/>'
        '<text x="32" y="42.5" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" '
        'font-size="29" font-weight="700" fill="#fff">GK</text></svg>\n'
    )
    print("wrote favicon set")


if __name__ == "__main__":
    og_card()
    favicons()
