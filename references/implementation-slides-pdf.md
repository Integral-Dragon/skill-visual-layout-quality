# Implementation: Slides And PDFs

Use these tactics when applying the universal principles to slide decks and PDFs.

## Why Slides/PDFs Need Their Own Layer

Decks and PDFs fail differently from SVGs:

- z-order issues show up only in slide renderers
- footer and page-number safe zones matter
- dense page layouts can pass source inspection but fail at presentation size
- font substitution can change text metrics across machines or export paths
- aspect ratio mismatches can silently destroy an otherwise sound layout

## Practical Rules

- Validate slide/page thumbnails or rendered images.
- Check title-to-content spacing, footer safety, card padding, and z-order collisions.
- Decorative shapes belong in margins or background layers only.
- For decks, do not trust one clean slide; inspect the rendered set.
- Confirm the intended aspect ratio before building or exporting. `16:9` vs `4:3` mistakes are layout bugs, not formatting trivia.
- Check whether the render environment actually has the fonts the layout depends on.
- Assume speaker notes are not a safe place for visible-content overflow hacks. Keep visible content stable without relying on notes.
- Check image assets at rendered scale; a low-resolution embedded image can look fine in source but fail badly in export.
- If animations are used, confirm the PDF export still communicates the slide without them.

## Validation Workflow

1. Render thumbnails or export to PDF.
2. Inspect rendered slides/pages.
3. Look for:
   - title-to-body crowding
   - content too close to footer
   - decorative shapes crossing content
   - weak padding inside cards or callouts
   - low-contrast labels
   - text reflow caused by font substitution
   - master/template artifacts colliding with slide-specific content
   - wrong aspect ratio or letterboxing/cropping symptoms
   - blurry or under-scaled embedded images
4. Fix the source deck.
5. Re-render.

## Specific Failure Modes

### Slide Master / Template Collisions

Master elements can create invisible overlap debt:

- repeated headers or accent bars may intrude on content zones
- template footers can fight slide-specific footer text
- placeholder remnants can survive into client-facing output

Check rendered slides for template residue, not just authored content.

### Aspect Ratio Mismatch

If content was composed for `16:9` and exported or re-opened as `4:3`, spacing and collision failures will cascade quickly.

Confirm:

- source slide size
- export slide size
- target presentation surface

### Font Availability / Substitution

This is a first-class failure mode.

If the intended font is unavailable:

- labels may widen
- line breaks may change
- optical centering may drift
- container padding may collapse

When in doubt:

- use a safer fallback stack
- re-check rendered output on the actual export machine
- avoid designs that depend on one fragile custom font metric

### Visible Content Safe Zones

Keep high-value content away from:

- footer and page-number areas
- title/master overlays
- screen-share crop zones
- projector overscan edges when the deck is presentation-facing

## Typical Fixes

- demote decorative shapes to thin edge accents
- increase card or section height
- normalize internal padding across a slide family
- move footer metadata farther from content
- shorten or split dense headings instead of just shrinking them
- replace fragile fonts or widen containers after font fallback
- fix slide master residue instead of compensating on every slide
- rebuild for the correct aspect ratio instead of stretching the layout
