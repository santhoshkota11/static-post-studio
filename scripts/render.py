"""Render every <section class="slide"> in an HTML file to PNG, run design QA, and build review sheets.

Usage:
  python render.py <slides.html> <out_dir> [--scale 2] [--safe 64] [--min-px 24] [--pdf "title"] [--no-qa]

What it writes into <out_dir>:
  slide-01.png ...      final exports at the slide's exact CSS size (1080x1350 by default), supersampled
                         at --scale and downsampled with Lanczos so small type stays crisp
  contact-sheet.png     every slide side by side, for judging the carousel as one object (rhythm, seams)
  phone-preview.png     the cover and every slide at real phone width (~390 px) to judge legibility honestly
  grid-preview.png      the cover cropped to the 3:4 profile-grid tile, to check nothing important is cut
  qa.json               machine-readable QA findings (also printed)
  <title>.pdf           only with --pdf (LinkedIn document posts)

Slide size: set CSS variables --W / --H on the slide (or body). The script reads each slide's real box,
so 1080x1350 (4:5), 1080x1440 (3:4), 1080x1080 (1:1), 1080x1920 (9:16 story) all work.

QA checks (warnings, not failures; fix them or justify them):
  - text outside the safe margin (elements may opt out with data-bleed, e.g. a giant wordmark that bleeds on purpose)
  - text smaller than --min-px at 1080 width (opt out with data-micro for legal lines / disclaimers)
  - more than 3 font families on one slide, more than 4 distinct font sizes on one slide
  - images that failed to load, and text that overflows its own box (clipped words)
"""
import argparse
import json
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw
from playwright.sync_api import sync_playwright


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[\s_]+", "-", text)[:80] or "post"


def launch(p):
    """Playwright's bundled Chromium, else any Chromium already in ms-playwright, else system Chrome / Edge."""
    try:
        return p.chromium.launch()
    except Exception as first:
        import glob
        import os
        root = os.path.join(os.environ.get("LOCALAPPDATA", ""), "ms-playwright")
        for exe in sorted(glob.glob(os.path.join(root, "chromium-*", "chrome-win*", "chrome.exe")), reverse=True):
            try:
                return p.chromium.launch(executable_path=exe)
            except Exception:
                pass
        for channel in ("chrome", "msedge"):
            try:
                return p.chromium.launch(channel=channel)
            except Exception:
                pass
        raise first


QA_JS = r"""
({safe, minPx}) => {
  const out = [];
  const slides = [...document.querySelectorAll('section.slide')];
  slides.forEach((s, idx) => {
    const sb = s.getBoundingClientRect();
    const fams = new Set(), sizes = new Set();
    const issues = [];
    const walker = document.createTreeWalker(s, NodeFilter.SHOW_TEXT);
    const seen = new Set();
    while (walker.nextNode()) {
      const t = walker.currentNode;
      if (!t.textContent.trim()) continue;
      const el = t.parentElement;
      if (seen.has(el)) continue; seen.add(el);
      if (el.closest('.ph')) continue;
      const cs = getComputedStyle(el);
      if (cs.visibility === 'hidden' || cs.display === 'none' || +cs.opacity === 0) continue;
      const range = document.createRange(); range.selectNodeContents(t);
      const r = range.getBoundingClientRect();
      if (!r.width || !r.height) continue;
      const fs = parseFloat(cs.fontSize);
      const label = t.textContent.trim().replace(/\s+/g,' ').slice(0, 40);
      fams.add(cs.fontFamily.split(',')[0].replace(/["']/g,'').trim());
      if (!el.closest('.logo,.count,.swipe,.kicker,[data-furniture],[data-micro]')) sizes.add(Math.round(fs));
      const bleed = el.closest('[data-bleed]');
      const micro = el.closest('[data-micro]');
      if (!bleed) {
        const l = r.left - sb.left, tp = r.top - sb.top, rr = sb.right - r.right, bt = sb.bottom - r.bottom;
        if (l < safe - 1 || tp < safe - 1 || rr < safe - 1 || bt < safe - 1)
          issues.push(`text outside ${safe}px safe margin: "${label}" (L${Math.round(l)} T${Math.round(tp)} R${Math.round(rr)} B${Math.round(bt)})`);
      }
      if (!micro && fs < minPx) issues.push(`text ${Math.round(fs)}px < ${minPx}px (unreadable on a phone): "${label}"`);
      if (el.scrollWidth > el.clientWidth + 2 && cs.overflow !== 'visible' && cs.textOverflow !== 'clip')
        issues.push(`text clipped horizontally: "${label}"`);
    }
    const ph = s.querySelectorAll('.ph').length;
    if (ph) issues.push(`${ph} placeholder(s) (.ph) still on this slide: replace with real assets or a designed graphic before delivery`);
    if (fams.size > 3) issues.push(`${fams.size} font families on one slide (${[...fams].join(', ')}); keep to 2, 3 at most`);
    if (sizes.size > 4) issues.push(`${sizes.size} distinct content text sizes (${[...sizes].sort((a,b)=>b-a).join(', ')}); hierarchy reads cleaner with 3 or 4`);
    out.push({slide: idx + 1, w: Math.round(sb.width), h: Math.round(sb.height), fonts: [...fams], sizes: [...sizes].sort((a,b)=>b-a), issues});
  });
  const broken = [...document.images].filter(i => i.getAttribute('src') && !(i.complete && i.naturalWidth)).map(i => i.getAttribute('src'));
  const fontsMissing = [...document.fonts].filter(f => f.status === 'error').map(f => f.family);
  return {slides: out, broken, fontsMissing};
}
"""


def contact_sheet(pngs, path, height=540, gap=0, bg=(118, 118, 118)):
    ims = [Image.open(p).convert("RGB") for p in pngs]
    scaled = [im.resize((round(im.width * height / im.height), height), Image.LANCZOS) for im in ims]
    W = sum(i.width for i in scaled) + gap * (len(scaled) - 1)
    sheet = Image.new("RGB", (W, height), bg)
    x = 0
    for im in scaled:
        sheet.paste(im, (x, 0))
        x += im.width + gap
    sheet.save(path)


def phone_preview(pngs, path, phone_w=390):
    """Each slide at the size it is actually seen in the feed, in a 2-up grid."""
    ims = [Image.open(p).convert("RGB") for p in pngs]
    tiles = [im.resize((phone_w, round(im.height * phone_w / im.width)), Image.LANCZOS) for im in ims]
    cols = min(4, len(tiles))
    rows = (len(tiles) + cols - 1) // cols
    th = max(t.height for t in tiles)
    pad = 24
    sheet = Image.new("RGB", (cols * phone_w + (cols + 1) * pad, rows * th + (rows + 1) * pad), (24, 24, 24))
    for i, t in enumerate(tiles):
        r, c = divmod(i, cols)
        sheet.paste(t, (pad + c * (phone_w + pad), pad + r * (th + pad)))
    sheet.save(path)


def grid_preview(cover_png, path, tile_w=360):
    im = Image.open(cover_png).convert("RGB")
    target_h = round(im.width * 4 / 3)
    if im.height > target_h:  # 4:5 or 9:16 cover: centre-crop to the 3:4 profile tile
        top = (im.height - target_h) // 2
        crop = im.crop((0, top, im.width, top + target_h))
    else:
        crop = im
    tile = crop.resize((tile_w, round(crop.height * tile_w / crop.width)), Image.LANCZOS)
    canvas = Image.new("RGB", (tile_w * 3 + 8, tile.height), (250, 250, 250))
    d = ImageDraw.Draw(canvas)
    for k in range(3):
        if k == 1:
            canvas.paste(tile, (k * (tile_w + 4), 0))
        else:
            d.rectangle([k * (tile_w + 4), 0, k * (tile_w + 4) + tile_w, tile.height], fill=(225, 225, 225))
    canvas.save(path)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("out_dir")
    ap.add_argument("--scale", type=float, default=2.0, help="supersampling factor before downsampling to exact size")
    ap.add_argument("--safe", type=int, default=64, help="safe margin in px at 1080 width")
    ap.add_argument("--min-px", type=int, default=24, help="smallest allowed text size at 1080 width")
    ap.add_argument("--pdf", default=None, help="also write a PDF (LinkedIn document) with this title")
    ap.add_argument("--no-qa", action="store_true")
    a = ap.parse_args()

    html = Path(a.html).resolve()
    out = Path(a.out_dir).resolve()
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("slide-*.png"):
        old.unlink()

    pngs = []
    with sync_playwright() as p:
        browser = launch(p)
        page = browser.new_page(viewport={"width": 1400, "height": 2000}, device_scale_factor=a.scale)
        page.goto(html.as_uri(), wait_until="networkidle")
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(500)
        slides = page.locator("section.slide")
        n = slides.count()
        if n == 0:
            print('No <section class="slide"> found.', file=sys.stderr)
            return 1
        report = page.evaluate(QA_JS, {"safe": a.safe, "minPx": a.min_px}) if not a.no_qa else None
        for i in range(n):
            box = slides.nth(i).bounding_box()
            w, h = round(box["width"]), round(box["height"])
            tmp = out / f"_raw-{i + 1:02d}.png"
            slides.nth(i).screenshot(path=str(tmp))
            im = Image.open(tmp).convert("RGB")
            if im.size != (w, h):
                im = im.resize((w, h), Image.LANCZOS)
            target = out / f"slide-{i + 1:02d}.png"
            im.save(target, optimize=True)
            tmp.unlink()
            pngs.append(target)
        browser.close()

    contact_sheet(pngs, out / "contact-sheet.png")
    phone_preview(pngs, out / "phone-preview.png")
    grid_preview(pngs[0], out / "grid-preview.png")
    print(f"Rendered {len(pngs)} slide(s) to {out}  ({Image.open(pngs[0]).size[0]}x{Image.open(pngs[0]).size[1]})")
    print("Review: contact-sheet.png (rhythm), phone-preview.png (legibility), grid-preview.png (profile crop)")

    if report:
        (out / "qa.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
        total = 0
        for s in report["slides"]:
            for msg in s["issues"]:
                print(f"  QA slide {s['slide']:02d}: {msg}")
                total += 1
        if report["broken"]:
            print("  QA: images that failed to load: " + ", ".join(report["broken"]))
            total += 1
        if report["fontsMissing"]:
            print("  QA: fonts that failed to load (fallback used): " + ", ".join(sorted(set(report["fontsMissing"]))))
            total += 1
        print(f"QA: {total} warning(s)" if total else "QA: clean")

    if a.pdf:
        pages = [Image.open(p).convert("RGB") for p in pngs]
        pdf_path = out / f"{slugify(a.pdf)}.pdf"
        pages[0].save(pdf_path, "PDF", save_all=True, append_images=pages[1:], resolution=72, quality=92, title=a.pdf)
        print(f"PDF: {pdf_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
