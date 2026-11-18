# Colour

## Contents
1. Palette roles and proportion
2. Building a palette fast
3. Category and mood codes
4. Contrast and accessibility
5. Text on images
6. Colour systems for carousels and grids

---

## 1. Roles and proportion
Define colours by **role**, not by name: `field` (background), `field-2` (panels), `ink` (headlines/body),
`muted` (secondary text), `accent` (the one colour that points), `on-accent`, plus `dark`/`on-dark` if the
system alternates. **60-30-10**: ~60% field or photo, ~30% ink/support/imagery, ~10% accent. The classic
mistake is inverting it: putting the loud brand colour on 60% of the frame.
**One accent.** It marks the single most important thing on each slide (a word, a number, a CTA, a pin).
If everything is accented, nothing is. Seen everywhere in the study: gold on navy/black (R03, R07, R08),
mustard on green (R10), yellow on plum (R05), red stamp on orange (R12).

## 2. Building a palette fast
1. Start from the brand colour; decide if it's the field (bold brands) or the accent (most brands).
2. Field: a tinted neutral pulled toward the brand hue (warm paper `#F4F0E8`, cool fog `#EEF1F4`, deep ink
   `#14130F`, navy `#0F1B3D`). Pure `#FFFFFF`/`#000000` read cheaper than tinted ones on screen.
3. Ink: near-black or near-white tinted toward the field; muted = ink at ~60–70% (check contrast).
4. Accent: complementary or split-complementary to the field for energy; analogous for calm.
5. **Monochrome world** (R12): field, props and product all in one hue family with a white type layer;
   striking for seasonal/product drops.
6. Ramps: `python scripts/palette.py ramp <hex>` for tints/shades; preview balance with
   `python scripts/palette.py swatch out.png <field> <ink> <accent> --weights 60,30,10`.

## 3. Category and mood codes (use, or break on purpose)
| Category / mood | Typical codes | Ownable twist |
|---|---|---|
| Real estate, advisory | white/sky haze, warm daylight photos, navy + gold for luxury | one signature colour for pills/boxes; inset frames |
| Luxury | near-black, deep navy, bottle green, champagne/gold, ivory | metal as the only accent, thin rules |
| F&B | appetite warms (orange, mustard, tomato), deep green/brown backdrops | colour world per menu or season |
| Health, wellness | sage, clay, cream, soft blue | texture over gradients |
| Finance, B2B, SaaS | black/white with one electric accent, or navy/blue | highlight boxes, chart colour as accent |
| Youth, events, music | saturated flats, clashing pairs (pink/red, navy/mustard), grain | colour changes per slide on a fixed grid (R11) |
| Kids, education | primaries softened, cream fields | consistent character colour |
| Film, culture | graded photo palette (teal/amber), gold type | letter-spaced metallic title |
| Tech, AI | dark with glow, purple/blue, or stark white with one neon | glow only on the hero object |
Colour psychology claims are heuristics, not science; context and contrast with the rest of the feed matter
more. A warm saturated post stands out in a cool, muted feed, and vice versa.

## 4. Contrast
- Body/small text ≥ **4.5:1**; display text (≥ ~48 px at 1080, or bold ≥ 38 px) ≥ **3:1**.
  Check: `python scripts/palette.py contrast <fg> <bg>`.
- Don't de-emphasise with low contrast; de-emphasise with size and weight (low-contrast text is just unreadable).
- Accent text on accent-adjacent fields often fails: check every accent/field pair you actually use.

## 5. Text on images
In order of preference:
1. **Choose/crop the image for it**: put type on sky, wall, shadow, table top, negative space.
2. **Dissolve/gradient into field** (R01): image fades into the background colour where type sits.
3. **Floor-fade scrim**: dark gradient from the bottom (≈80% → 0% over the lower 60%); or top scrim for headers.
4. **Panel**: solid or frosted card (R04), or a half-and-half split (R15).
5. **Pill / strip** behind short lines (R01 takeaway pill, `.pill`).
6. **Darken/duotone the whole image** (40–60%) when the photo is texture, not information.
7. Text shadow: last resort, tight and dark (`0 2px 12px rgba(0,0,0,.55)`), never a soft glow halo.
Measure contrast against the **lightest** pixel area behind the text, not the average.

## 6. Systems across slides and the profile grid
- Keep the field constant and change the accent use, or keep the accent and alternate light/dark fields (R14).
- Changing colour every slide works only with a rigid grid and fixed type/motifs (R11).
- Think about the 3×N profile grid: a series with a consistent field or frame makes the grid read as one brand.
