# Effects, textures, patterns, motifs

The rule: an effect must either **serve legibility**, **carry the concept** or **make the brand ownable**.
If it does none, delete it. One finish per post (e.g. grain + paper), one motif.

## Contents
1. Texture and finish
2. Image treatments
3. Graphic devices and motifs
4. Patterns
5. Premium vs cheap, per effect
6. CSS recipes

---

## 1. Texture and finish
- **Film grain / noise** (template `.grain`): kills the sterile "AI/vector" look, unifies mixed images. 8–18% opacity,
  multiply on light fields, screen on dark. 2026's dominant counter-trend to over-polished AI visuals.
- **Paper**: warm off-white field + faint fibre/noise; riso/zine feel with slight misregistration.
- **Halftone dots**: retro print, pop; good for duotone portraits and big numbers.
- **Grainy blur gradients**: soft blurred colour fields + grain; atmospheric backgrounds for type-led tech/wellness posts.
- **Glass / frosted panel** (R04): backdrop blur + 70–85% white; use only over photos, keep it to one panel.
- **Glow** (R05): on the hero object or one word on dark fields; never on body text.

## 2. Image treatments
- **Grade consistency**: same warmth/contrast across all slides (R06 red motif, R08 teal-amber).
- **Duotone**: two brand colours mapped to shadows/highlights; unifies random photos into one system.
- **B&W + one colour**: portrait in B&W, accent type in colour (R07).
- **Cut-out**: subject with background removed, on a flat field or breaking out of a frame (needs a clean
  mask; a rough edge reads cheap).
- **Inset frame** (R15): photo inside a white/coloured border; feels like a print, premium and calm.
- **Ticket / notched frame** (R11), **arch**, **rounded rectangle**, **circle**: the frame shape can be the motif.
- **Macro detail** (R10): texture close-ups carry appetite/craft with no text.
- **Panorama across slides** (R13/R15): see layout.md.

## 3. Graphic devices and motifs
- **Rules and hairlines**: dividers in icon rows (R14), under labels, frames (R03 inset gold rule).
- **Line icons**: one consistent stroke weight and corner style; never mix icon sets; never emoji as icons in premium work.
- **Highlight box / marker / underline**: emphasis devices (typography.md §4).
- **Pills and tags**: takeaway lines, labels, CTAs.
- **Arrows**: swipe cue and causal links; one style.
- **Dotted outline + pin** (R04): mark a plot, route or area on a photo/map.
- **Stickers/badges** (R11): only in zine/event/youth concepts, with a fixed style (same border, shadow, angle range).
- **Binder rings, tape, torn edges, paper clips**: physical-object metaphors (notebook, scrapbook, dossier);
  pick one metaphor and stay in it.
- **Giant rotated wordmark** bleeding off the edge (R11): instant ownability for events and sub-brands.
- **Recurring character** (R16) or recurring object (sun rays R12, retro TVs R05).
- **Laurels / pull-quotes** (R08): proof styled as honour, not as reviews.

## 4. Patterns
Use as quiet backgrounds (≤ 8% contrast) or as the brand's signature: grid paper, pinstripes (R05), dot grid,
radial sun rays (R12), topographic lines (land/real estate), woven/textile motifs (Indian craft brands),
kolam/rangoli geometry (festive, South India), checkerboard (retro F&B), blueprint lines (architecture).
Never put a loud pattern behind body text.

## 5. Premium vs cheap
| Effect | Premium use | Cheap use |
|---|---|---|
| Gradient | subtle tonal, dissolve into field, grainy blur | rainbow/neon gradients on everything, gradient text |
| Shadow | soft ambient on objects, hard offset as a deliberate retro style | default drop shadow on text and logos |
| Glow | one hero object on dark | outer glow on headlines |
| Stickers | systemised in a zine concept | random badges "NEW!!", "HOT" |
| 3D | one rendered hero object | bevelled/embossed type |
| Texture | grain, paper | stock grunge overlays, lens flares |
| Frames | inset rule, ticket, arch | ornate clip-art borders |
| Icons | one line set, consistent stroke | mixed clip-art, emoji |

## 6. CSS recipes
```css
/* duotone image */
.duo{position:relative} .duo img{filter:grayscale(1) contrast(1.1)}
.duo::after{content:"";position:absolute;inset:0;background:linear-gradient(var(--accent),var(--dark));mix-blend-mode:color}
/* halftone overlay */
.halftone::after{content:"";position:absolute;inset:0;background-image:radial-gradient(rgba(0,0,0,.35) 1.2px,transparent 1.6px);background-size:10px 10px;mix-blend-mode:multiply}
/* frosted panel */
.glass{background:rgba(255,255,255,.78);backdrop-filter:blur(14px) saturate(1.2);border:1px solid rgba(255,255,255,.6);border-radius:28px}
/* grainy blur field */
.blurfield{background:radial-gradient(60% 50% at 25% 30%,var(--accent),transparent 70%),radial-gradient(50% 50% at 80% 75%,var(--field-2),transparent 70%),var(--field);filter:saturate(1.1)}
/* inset print frame */
.inset{position:absolute;inset:36px;overflow:hidden;outline:2px solid rgba(255,255,255,.0)}
/* dotted outline on a photo: use an inline SVG <path stroke-dasharray="2 14" stroke-linecap="round"> */
/* pinstripes */
.pin{background:repeating-linear-gradient(90deg,rgba(255,255,255,.05) 0 1px,transparent 1px 36px),var(--dark)}
/* sun rays */
.rays{background:repeating-conic-gradient(from 0deg at 50% 110%,rgba(255,255,255,.10) 0 4deg,transparent 4deg 12deg),var(--accent)}
/* hard offset retro shadow */
.retro{box-shadow:8px 8px 0 var(--ink);border:4px solid var(--ink)}
```
