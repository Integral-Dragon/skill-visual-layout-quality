# Implementation: Slides And PDFs

Use these tactics when applying the universal principles to slide decks and PDFs.

## Why Slides/PDFs Need Their Own Layer

Decks and PDFs fail differently from SVGs:

- z-order issues show up only in slide renderers
- footer and page-number safe zones matter
- dense page layouts can pass source inspection but fail at presentation size

## Practical Rules

- Validate slide/page thumbnails or rendered images.
- Check title-to-content spacing, footer safety, card padding, and z-order collisions.
- Decorative shapes belong in margins or background layers only.
- For decks, do not trust one clean slide; inspect the rendered set.

## Validation Workflow

1. Render thumbnails or export to PDF.
2. Inspect rendered slides/pages.
3. Look for:
   - title-to-body crowding
   - content too close to footer
   - decorative shapes crossing content
   - weak padding inside cards or callouts
   - low-contrast labels
4. Fix the source deck.
5. Re-render.

## Typical Fixes

- demote decorative shapes to thin edge accents
- increase card or section height
- normalize internal padding across a slide family
- move footer metadata farther from content
- shorten or split dense headings instead of just shrinking them
