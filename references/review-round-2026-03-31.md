# Review Round: 2026-03-31

This note captures the first external critique loop after the major rewrite.

## Participants

- Codex: initial rewrite and self-rating
- Claude: critical review of the rewrite
- user: direction on structure, generality, and follow-up priorities

## Rating Comparison

- Codex initial rating: `8/10`
- Claude review rating: `7/10`
- Codex revised rating after review: `7.5/10`

## Claude's Main Findings

1. The universal-principles vs implementation split is the right architecture.
2. The rendered QA workflow is the strongest part of the redesign.
3. The skill was still stronger for SVG than for slides/PDF.
4. `SKILL.md` had redundancy between principles and non-negotiable rules.
5. `implementation-slides-pdf.md` was too thin.
6. Font substitution should be a first-class failure mode.
7. `svg_layout_audit.py` had significant blind spots.
8. Auto-run conditions for validation were too broad.

## Resulting Follow-Up Changes

- added `font substitution drift` as a failure class
- strengthened slides/PDF implementation guidance
- tightened auto-run language to `final-quality` assets
- added batch timing guidance for validation rounds
- clarified that optical alignment only has teeth during rendered QA
- reduced `SKILL.md` redundancy by replacing the old non-negotiable section with a smaller operational-check section
- improved the SVG audit script with:
  - `style=` parsing
  - basic `translate()` handling
  - inherited transform offsets for nested groups

## Why This Note Exists

The point is not just to preserve praise or criticism. The point is to preserve:

- what changed after outside review
- how ratings shifted after critique
- which weaknesses were judged structural vs tactical

This is intended as a lightweight evolution record for future review rounds.
