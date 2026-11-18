"""Colour helper: WCAG contrast checks, tints/shades, and a quick palette swatch image.

Usage:
  python palette.py contrast <fg_hex> <bg_hex> [<fg_hex> <bg_hex> ...]
      prints the contrast ratio and whether it passes for body text (4.5:1) and large display text (3:1)
  python palette.py ramp <hex>
      prints 9 tints/shades of one colour (50..900) for backgrounds, rules and muted text
  python palette.py swatch <out.png> <hex> [<hex> ...] [--weights 60,30,10]
      draws the palette as proportional bands so the 60-30-10 balance can be judged by eye
"""
import sys


def hex_to_rgb(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return "#" + "".join(f"{max(0, min(255, round(c))):02X}" for c in rgb)


def luminance(rgb):
    def ch(c):
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = luminance(hex_to_rgb(a)), luminance(hex_to_rgb(b))
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def mix(a, b, t):
    ra, rb = hex_to_rgb(a), hex_to_rgb(b)
    return rgb_to_hex(tuple(x + (y - x) * t for x, y in zip(ra, rb)))


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    cmd = argv[1]
    if cmd == "contrast":
        pairs = argv[2:]
        for i in range(0, len(pairs) - 1, 2):
            fg, bg = pairs[i], pairs[i + 1]
            r = contrast(fg, bg)
            body = "PASS" if r >= 4.5 else "fail"
            large = "PASS" if r >= 3 else "fail"
            print(f"{fg} on {bg}: {r:.2f}:1  body(4.5) {body}  display(3.0) {large}")
        return 0
    if cmd == "ramp":
        base = argv[2]
        steps = {50: .92, 100: .82, 200: .64, 300: .44, 400: .22, 500: 0, 600: .18, 700: .36, 800: .54, 900: .72}
        for k, t in steps.items():
            print(f"{k:>3}: {mix(base, '#FFFFFF', t) if k < 500 else mix(base, '#000000', t) if k > 500 else rgb_to_hex(hex_to_rgb(base))}")
        return 0
    if cmd == "swatch":
        from PIL import Image, ImageDraw
        out = argv[2]
        cols = [c for c in argv[3:] if c.startswith("#") or len(c) in (3, 6)]
        weights = None
        if "--weights" in argv:
            weights = [float(x) for x in argv[argv.index("--weights") + 1].split(",")]
        weights = weights or [1] * len(cols)
        W, H = 1200, 300
        im = Image.new("RGB", (W, H), "white")
        d = ImageDraw.Draw(im)
        x = 0
        tot = sum(weights[:len(cols)])
        for c, w in zip(cols, weights):
            bw = round(W * w / tot)
            d.rectangle([x, 0, x + bw, H], fill=hex_to_rgb(c))
            d.text((x + 12, H - 28), c.upper(), fill=(255, 255, 255) if luminance(hex_to_rgb(c)) < .4 else (0, 0, 0))
            x += bw
        im.save(out)
        print(f"wrote {out}")
        return 0
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
