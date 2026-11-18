# static-post-studio

A Claude skill that works like a pro art director and graphic designer for **static social posts and carousels**,
for any brand or creator.

Give it a brief ("6-slide launch carousel for our cold brew", "speaker card for our meetup", "RERA explainer for
first-time buyers") and it:

1. **Thinks first**: objective, single message, insight, big idea, three concept routes (and picks one).
2. **Builds a design system**: canvas and safe zones, grid and spacing, palette with roles (60-30-10, one accent,
   contrast-checked), type pairing and scale, layout archetypes, motif, texture and effects.
3. **Writes the copy** slide by slide, plus caption and alt text.
4. **Designs and renders** finished PNGs (Instagram 4:5 / 3:4 / 1:1, stories, LinkedIn document PDFs) from HTML/CSS.
5. **Checks its own work**: text size, safe margins, font/size count, leftover placeholders, a phone-size preview
   and the 3:4 profile-grid crop, then fixes what it finds.

## What's inside

| Path | What it is |
|---|---|
| `SKILL.md` | the workflow and the "premium vs cheap" instincts |
| `references/concept.md` | insight → idea, visual metaphor types, cover hooks, 12 carousel story arcs, single-post formats |
| `references/layout.md` | canvas sizes, safe zones, grid, 8 px spacing, 10 layout archetypes, swipe cues, panoramas |
| `references/typography.md` | pairings by mood (Google Fonts), type scale at 1080 px, tracking, emphasis devices, Indic scripts |
| `references/color.md` | palette roles, 60-30-10, category colour codes, contrast, text-on-image techniques |
| `references/effects.md` | grain, halftone, duotone, glass, frames, stickers, patterns: premium vs cheap, CSS recipes |
| `references/categories.md` | playbooks for real estate, F&B, fashion, events, film, B2B, creators, health, edu, D2C |
| `references/reference-study.md` | slide-by-slide study of 17 real brand posts and the patterns they share |
| `templates/post.html` | the base HTML/CSS template with tokens, layouts and components |
| `scripts/render.py` | renders every slide to exact-size PNG + contact sheet, phone preview, grid preview, QA report |
| `scripts/palette.py` | contrast checker, tint/shade ramps, palette swatches |
| `brands/_template.md` | brand-kit template, so every post for a brand stays consistent |
| `evals/` | test cases (prompts + checks) |

## Install

Copy this folder into your Claude skills folder (for Claude Code: `~/.claude/skills/static-post-studio`).
Rendering needs Python 3 with `playwright` and `pillow`:

```
pip install playwright pillow
playwright install chromium   # or it will fall back to an installed Chrome / Edge
```

Then just ask for a post or carousel.

## Render by hand

```
python scripts/render.py path/to/slides.html path/to/out
python scripts/palette.py contrast "#5E5A52" "#F4F0E8"
```

## Notes

- It never invents logos, prices, testimonials, results or photos of real people; missing assets become clearly
  marked placeholders listed as open items.
- Fonts load from Google Fonts, so rendering needs an internet connection (or locally installed fonts).
