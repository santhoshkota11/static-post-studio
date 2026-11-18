# Layout: canvas, grid, spacing, archetypes

## Contents
1. Canvas and safe zones
2. Grid and spacing
3. Composition principles
4. Ten layout archetypes (with the template class)
5. Swipe cues, seams and panoramas
6. Furniture (logo, counters, CTAs)

---

## 1. Canvas and safe zones
| Use | Size | Notes |
|---|---|---|
| Instagram feed default | **1080×1350 (4:5)** | most feed space; boostable as an ad; profile grid shows a centred 3:4 crop (≈1012×1350), so keep essentials inside the middle and away from left/right 34 px |
| Instagram grid-native | 1080×1440 (3:4) | fills the 3:4 profile grid with no crop; cannot be boosted as-is (ad tools stop at 4:5) |
| Square | 1080×1080 | older brand grids, LinkedIn single image, X |
| Story / status | 1080×1920 (9:16) | keep text out of the top ~250 px and bottom ~340 px (UI) |
| LinkedIn document | 1080×1350 pages exported to PDF | `render.py --pdf "title"` |
| Landscape carousel | 1080×566 (1.91:1) or 1080×720 | only for documentary/photo stories (R06); feed shows it small |
All slides in one Instagram carousel share the first slide's ratio.
Margins: 64 px minimum safe area, 80–96 px looks premium. Text must sit inside the safe area unless it is a
deliberate bleed (giant wordmark), marked `data-bleed`.

## 2. Grid and spacing
- **Columns**: 6 or 12 columns on 1080 with 88 px margins and 24 px gutters works for almost everything.
  Asymmetric layouts (text on 4 of 6 columns) feel editorial; centred stacks feel calm/institutional.
- **Spacing unit** 8 px. Every gap is a multiple (8, 16, 24, 32, 48, 64, 96, 128). Inside < outside:
  space within a group is smaller than space between groups (Gestalt proximity), so related lines cluster
  and the eye reads them as one unit.
- **Few alignment axes**: Müller-Brockmann's posters use only a few key alignment lines. Pick 2–3 (left margin,
  centre, one internal column) and hang everything on them.
- **Fixed positions across slides**: headline top line, logo, counter and CTA sit at the same coordinates on
  every slide. Nothing kills credibility faster than text that jumps between slides.

## 3. Composition principles
- **One focal point** per frame, decided in advance. Size, contrast, isolation and position create it.
- **Scale contrast**: big differences (display 3–4× body) feel energetic and confident; small differences feel
  quiet/institutional. Choose on purpose.
- **Visual weight & balance**: symmetry = calm, trust (finance, real estate, luxury); asymmetry = energy (youth,
  events, tech). Balance a heavy image with empty space, not with more elements.
- **Negative space is an element**: give the headline a calm area of the image (sky, wall, shadow) or a field.
- **Reading path**: Z (cover: logo → headline → image → CTA) or F (explainers: headline then left-aligned body).
- **Crop with intent**: tight crops = intimacy/detail, wide = context/scale; cut people at joints never.
- **Edges**: an object cut by the edge suggests continuation (great for swipe), an object floating
  centrally suggests a "product shot".

## 4. Ten archetypes (template classes)
1. **Type statement** `L-type`: big serif or grotesk statement, small kicker, short sub-line. Covers, quotes, rules.
2. **Dissolve** `L-dissolve` (R01/R02): image in the lower ~60%, fading upward into a calm field; two-tier
   headline on the field; takeaway pill at the bottom. Premium education for real estate, architecture, travel.
3. **Floor-fade scrim** `L-scrim` (R17): full-bleed photo, dark gradient from the bottom, statement bottom-left.
   Aspirational lifestyle. Check body text contrast on the lightest part behind it.
4. **Four corners** `L-corners` (R07): portrait owns the centre, info pinned to corners (logo/partner,
   role/name, date/venue). Speaker, host, launch, hiring, award.
5. **Split** `L-split` (R15): type panel top, image bottom (or left/right). With `.pano`, one wide image runs
   across consecutive slides.
6. **Hero object** `L-hero` (R10/R12): one product on a flat colour world, name in display type. F&B, D2C.
7. **Macro detail**: full-bleed texture/close-up, no text; alternates with the hero for appetite (R10).
8. **Explainer** `L-explainer` (R14): solid field (alternate light/dark), headline with a boxed keyword,
   line-icon row with hairline dividers, short body. Education, B2B, finance.
9. **Zine / poster** `L-zine` (R11): rotated bleeding wordmark, ticket-frame photos, stickers, mono info lists,
   colour changes per slide on a fixed grid. Events, youth culture, launches with personality.
10. **Frame / one-sheet** (R03/R08): inset border or film-poster grammar: credits row, letter-spaced title,
    billing block, laurels/quotes. Film, culture, premium announcements.
Others worth knowing: collage/cut-out on paper (editorial), photo grid cover (3×2, R14), receipt/document
mock (borrowed format), chat/notification mock, chart-first data slide, map with dotted outline and pin (R04).

## 5. Swipe cues, seams, panoramas
- Cue on the cover: `>>`, `→`, "SWIPE ⟶", a pill with an arrow, a counter "01/07", or an image cut by the right edge.
- **Seam continuity**: an object, line or photo that crosses the slide boundary (R05, R13, R15). Build it as
  one wide image positioned per slide (`.pano` with `--i` and `--n`), so the halves line up exactly.
- Don't put text across a seam (the feed gap and swipe make it unreadable).

## 6. Furniture
- **Logo**: small (≈4–8% of width), a corner, same spot every slide; or only on cover and last slide.
  The idea is the hero.
- **Counter**: optional, mono, low contrast.
- **CTA slide**: one action, phrased as a benefit ("Save this for your next site visit"), or a comment keyword
  ("Comment LOKATIONS for Part 2"). Add handle/website if the brand wants it.
- **Compliance**: regulatory IDs, QR, disclaimers in a quiet, aligned footer (`data-micro`), never fighting the headline.
