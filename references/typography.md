# Typography

## Contents
1. Rules that never change
2. Type scale at 1080 px
3. Pairings by mood (Google Fonts, free to use)
4. Emphasis devices (pick one per post)
5. Tracking, leading, case
6. Indian scripts and bilingual posts
7. Common failures

---

## 1. Rules
- **Two families max** (display + text), plus an optional utility mono for labels. Different classifications
  pair best (serif + grotesk, slab + humanist); two similar sans fight.
- **Three or four content sizes per slide.** More sizes = no hierarchy.
- **One emphasis device per post** (see §4). Bold *and* italic *and* colour on the same words is shouting.
- **Contrast of weight/style beats contrast of colour** for emphasis: small regular line + heavy italic line (R01)
  reads instantly even in greyscale.
- Body lines 20–40 characters on a slide (a phone shows the post ~390 px wide); headlines break by meaning,
  not by box width (no orphans, no "the" ending a line).
- Professional, well-drawn faces; avoid system defaults (Arial, Times), novelty and "Canva default" faces
  (Montserrat everywhere, Bebas for everything, Great Vibes script) unless the brand already owns them.

## 2. Type scale at 1080 px wide (phone shows it at ~36%)
| Role | Size | Leading | Notes |
|---|---|---|---|
| Display / cover | 96–160 px | 0.9–1.05 | serif can go bigger than sans for the same weight |
| H2 (slide headline) | 64–96 px | 1.0–1.1 | |
| H3 / sub | 44–56 px | 1.1–1.2 | |
| Body | 32–40 px | 1.25–1.4 | never below 28 px for real reading |
| Small / caption / labels | 24–28 px | 1.3 | 24 px is the floor (render.py warns below) |
| Micro (legal, credits) | 16–20 px | 1.3 | only for disclaimers, mark `data-micro` |
Headline ≈ 2.5–4× body. Check `phone-preview.png`: if you squint and can't read the body, it's too small.

## 3. Pairings by mood
| Mood / category | Display | Text | Seen in |
|---|---|---|---|
| Editorial luxury, real estate, hospitality | Fraunces, Playfair Display, Cormorant Garamond, Bodoni Moda | Inter, Inter Tight, Manrope | R03, R15 |
| Modern premium serif (fashion, beauty, food) | Instrument Serif, DM Serif Display, Gloock, Young Serif | DM Sans, Instrument Sans | R10, R12 |
| Calm corporate / advisory | Plus Jakarta Sans, Manrope, Sora (heavy italic for line 2) | same family regular | R01 |
| Explainer / B2B / finance | Inter Tight, Geist, Space Grotesk, Montserrat (if brand) | same family | R14 |
| Film / culture one-sheet | Cormorant SC, Cinzel (letter-spaced), Bodoni Moda | Oswald / Barlow Condensed for billing | R08 |
| Events, youth, zine | Bricolage Grotesque, Archivo Black, Anton, Syne, Climate Crisis, Cooper-style (Fraunces 800 soft) | Space Mono, IBM Plex Mono, JetBrains Mono | R11 |
| Tech / AI / product | Geist, Space Grotesk, Satoshi-like (General Sans if licensed) | Geist Mono / JetBrains Mono labels | R05 |
| Handmade / friendly / kids | Caveat, Kalam, Patrick Hand (accents only) | Nunito, Quicksand | R16 cover |
| Bold sport / streetwear | Anton, Big Shoulders Display, Druk-like condensed | Archivo, Barlow | |
Load from Google Fonts in the `<link>`; if the brand has licensed fonts, install/link them instead.

## 4. Emphasis devices (choose one per post, repeat it everywhere)
1. **Italic switch**: one or two words in italic of the same serif ("Most posts are *decorated*").
2. **Weight jump**: light line + heavy line, or one heavy word in a light sentence.
3. **Two-tier headline**: small caps line + big heavy line (R01).
4. **Boxed keyword** `.hl`: inverted box behind 1–3 words (R14). Superb for explainers.
5. **Accent word**: one word in the accent colour.
6. **Marker / underline / circle**: hand-drawn mark, only if the brand is personal/creator-led.
7. **Size jump inside a line**: "How **BILLIONAIRES** choose real estate" (R17).

## 5. Tracking, leading, case
- ALL CAPS: only for short lines (< 1 line), always +5–12% letter-spacing (`letter-spacing:.06–.12em`);
  small labels in caps can go to +14%.
- Large display lowercase/sentence case: tighten slightly (−1% to −3%).
- Display leading tight (0.9–1.05); body 1.25–1.4.
- Sentence case reads friendlier and faster than Title Case; Title Case looks like an ad.
- Numbers as heroes: use lining/tabular figures, consider a different weight for units ("15 lakh **sq. ft.**").
- Centred text: fine for 1–3 line stacks; left-align anything longer.

## 6. Indian scripts, bilingual posts
- Pair a Latin face with an Indic face of matching weight/colour: Devanagari (Tiro Devanagari Hindi, Noto Serif
  Devanagari, Mukta, Hind, Yatra One for display), Telugu (Noto Sans/Serif Telugu, Ramabhadra, Mandali, NTR,
  Gurajada for display), Tamil (Noto Sans Tamil, Catamaran, Mukta Malar), Kannada (Noto Sans Kannada, Baloo Tamma 2).
- Indic scripts need ~1.15–1.3× the Latin size and more leading (matras above/below); test rendering of
  conjuncts, never use fake bold.
- A script word can be the motif (R12 "PROJECT गर्मी", R08 Devanagari title under the Latin title).

## 7. Failures to catch
Text on busy image areas; tracking caps not opened up; widows/orphans; justified text with rivers on a slide;
faux bold/italic; more than one emphasis device; 3+ families; body under 28 px; headline that breaks mid-phrase.
