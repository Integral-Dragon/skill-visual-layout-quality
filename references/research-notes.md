# Research Notes

External guidance that materially informed this skill.

## Carbon Design System

Source:

- https://v10.carbondesignsystem.com/guidelines/2x-grid/overview/

Relevant guidance:

- The 8px mini-unit is the geometric foundation for layout rhythm.
- Margins and padding should use fixed multiples of the mini-unit.
- Type should align to the edge of box padding, not sit on the padding itself.

Why it matters here:

- This supports using a spacing system instead of ad hoc nudges.
- It also reinforces that padding is a content boundary, not spare area for text to drift into.

## WCAG Visual Presentation

Source:

- https://www.w3.org/WAI/WCAG20/versions/guidelines/wcag20-guidelines-20081211-letter.pdf

Relevant guidance:

- Line width should be no more than 80 characters or glyphs for readable visual presentation.

Why it matters here:

- Even when an asset is not "accessible content" in the strict sense, overlong lines in fixed-layout visuals are a readability smell and usually a hierarchy problem.

## MDN SVG Text Anchor

Source:

- https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/text-anchor

Relevant guidance:

- `text-anchor` changes where rendered text sits relative to the current text position.
- For multi-line text, alignment happens per line.

Why it matters here:

- Centering and right alignment in SVG cannot be judged from the `x` coordinate alone.
- Multi-line alignment must be treated line-by-line.

## Local Inference From Incident Review

This is an inference from local Codex and Claude histories, not a cited web source:

- Width math alone is not enough.
- Many failures occurred even when text remained inside the nominal container.
- The dominant failure mode is not just overflow; it is the combination of weak padding, visual crowding, decorative intrusion, and missing rendered-output QA.
