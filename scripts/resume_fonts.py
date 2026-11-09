"""Build the "Resume Serif" web fonts used by the resume page (/resume/).

They are Latin Modern Roman 10, the typeface of the LaTeX PDF resume, cut down to Latin letters and
punctuation, renamed (as the GUST Font License requests for derived works) and saved as WOFF2.

Usage (needs fontTools and brotli):
    python3 -m venv /tmp/fonts && /tmp/fonts/bin/pip install fonttools brotli
    curl -LO https://mirrors.ctan.org/fonts/lm/fonts/opentype/public/lm/lmroman10-{regular,bold,italic}.otf
    /tmp/fonts/bin/python scripts/resume_fonts.py <folder with the three .otf files>

Re-run it if _data/cv.json starts using characters outside Latin and common punctuation
(it prints any the fonts lack). Writes assets/fonts/resume-serif-*.woff2.
"""
import sys
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "fonts"
CV = ROOT / "_data" / "cv.json"

LATIN = list(range(0x20, 0x7F)) + list(range(0xA0, 0x180))           # ASCII, Latin-1, Latin Extended-A
PUNCTUATION = list(range(0x2010, 0x2028)) + list(range(0x2030, 0x203B)) + [0x2192, 0x20AC, 0x2122, 0x2212]


def build(src_dir):
    used = sorted({c for c in CV.read_text(encoding="utf-8") if ord(c) > 0x7E})
    unicodes = LATIN + PUNCTUATION + [ord(c) for c in used]
    for style, weight in (("regular", "Regular"), ("bold", "Bold"), ("italic", "Italic")):
        font = TTFont(Path(src_dir) / f"lmroman10-{style}.otf")
        missing = [c for c in used if ord(c) not in font.getBestCmap()]
        options = subset.Options()
        options.flavor = "woff2"
        options.layout_features = ["kern", "liga"]
        options.name_IDs = ["*"]
        subsetter = subset.Subsetter(options=options)
        subsetter.populate(unicodes=unicodes)
        subsetter.subset(font)

        postscript = f"ResumeSerif-{weight}"
        for record in font["name"].names:
            if record.nameID in (1, 16):
                record.string = "Resume Serif"
            elif record.nameID == 3:
                record.string = f"{postscript}; subset of LMRoman10-{weight}"
            elif record.nameID == 4:
                record.string = f"Resume Serif {weight}"
            elif record.nameID == 6:
                record.string = postscript
        cff = font["CFF "].cff
        cff.fontNames = [postscript]
        cff.topDictIndex[0].FullName = f"Resume Serif {weight}"
        cff.topDictIndex[0].FamilyName = "Resume Serif"

        out = OUT / f"resume-serif-{style}.woff2"
        font.flavor = "woff2"
        font.save(out)
        print(f"wrote {out.relative_to(ROOT)} ({out.stat().st_size / 1024:.1f} KB)"
              + (f"; MISSING characters: {''.join(missing)}" if missing else ""))


if __name__ == "__main__":
    build(sys.argv[1])
