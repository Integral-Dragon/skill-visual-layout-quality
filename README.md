# Visual Asset Layout

![Release](https://img.shields.io/badge/release-v1.0.0-0b6e4f)
![Status](https://img.shields.io/badge/status-v1%20ready-14532d)
![License](https://img.shields.io/badge/license-MIT-1f2937)
![Focus](https://img.shields.io/badge/focus-layout%20that%20actually%20ships-7c3aed)

AI models are good at generating visual assets.

They are still weirdly bad at making those assets feel finished.

This repo is a production-oriented skill for fixing that gap.

`visual-asset-layout` is a reusable build-and-review skill for layout-heavy visuals:

- SVG graphics
- PNG/JPG-backed graphics with positioned text
- README hero images
- fixed-layout HTML and infographics
- Excalidraw exports
- slide decks and PDFs

It helps models make better layout decisions during composition, then validate the rendered output before you ship.

## Why This Exists

Most generated visuals fail in familiar ways:

- text technically fits but feels cramped
- padding collapses
- decoration competes with content
- connectors run through labels
- cards feel misaligned even when the math says they are centered
- source files look fine but the exported result is visibly wrong

This repo packages a practical answer:

- stable cross-format layout principles
- implementation guidance split by format
- lightweight preflight tooling
- rendered-output-first QA
- a future-enhancements backlog that keeps the core skill from overfitting every one-off failure

## What You Get

- a reusable skill for Codex or Claude Code
- format-specific guidance for SVG, slides/PDFs, and Excalidraw
- `svg_layout_audit.py` for SVG preflight
- `pptx_pdf_layout_audit.py` for PPTX/PDF preflight
- smoke tests for the audit helpers
- process notes showing how the skill evolved through multi-model critique

## What Makes This Repo Interesting

This is not just a prompt file.

It is a worked example of how to turn repeated AI output failures into a reusable operating layer:

1. notice recurring failure modes
2. generalize them into stable principles
3. keep implementation details format-specific
4. add lightweight helper tooling where it helps
5. collect future ideas without destabilizing the core package

If you care about AI-assisted design, slide generation, README visuals, or diagram tooling, this repo is meant to be stolen from.

## The Brain Trust Angle

This repo was sharpened through a three-way critique loop:

- `Dex` = Codex as canonical integrator
- `Max` = Claude Max as external critic
- `Hopper` = human operator setting direction and deciding when another round was worth it

That process is captured here:

- [meta/brain-trust-collaboration-loop.md](meta/brain-trust-collaboration-loop.md)
- [meta/brain-trust-origin-2026-03-31.md](meta/brain-trust-origin-2026-03-31.md)
- [meta/review-round-2026-03-31.md](meta/review-round-2026-03-31.md)
- [future_enhancements/Max/001-review-2026-04-02.md](future_enhancements/Max/001-review-2026-04-02.md)

The result was useful:

- the skill got materially better
- the scoring of future work got more honest
- the repo now preserves the reasoning behind the changes instead of only the final files

## Quick Start

### Claude Code

Personal:

```bash
git clone https://github.com/Integral-Dragon/skill-visual-layout-quality.git ~/.claude/skills/visual-asset-layout
```

Project-level:

```bash
git clone https://github.com/Integral-Dragon/skill-visual-layout-quality.git .claude/skills/visual-asset-layout
```

### Codex

Local install:

```bash
git clone https://github.com/Integral-Dragon/skill-visual-layout-quality.git ~/.codex/skills/visual-asset-layout
```

### Optional Helper Dependency

For the PPTX helper:

```bash
pip install -r requirements.txt
```

## Core Usage Model

Use the skill in this order:

1. compose the asset using the layout rules prescriptively
2. render the output the user will actually see
3. inspect the rendered artifact, not just the source
4. run a second-pass QA round when the asset is final-quality

The skill is intentionally not “SVG only” and not “QA only.”

It is a build-first, validate-second workflow.

## Repo Layout

```text
visual-asset-layout/
  SKILL.md
  reference.md
  requirements.txt
  references/
    incident-patterns.md
    implementation-excalidraw.md
    implementation-slides-pdf.md
    implementation-svg.md
    research-notes.md
    validation-round.md
  meta/
    brain-trust-collaboration-loop.md
    brain-trust-origin-2026-03-31.md
    review-round-2026-03-31.md
  future_enhancements/
    README.md
    Dex/
      001-current-ideas.md
    Hopper/
      001-current-ideas.md
    Max/
      001-review-2026-04-02.md
  scripts/
    pptx_pdf_layout_audit.py
    svg_layout_audit.py
  tests/
    fixtures/svg/
    run_smoke_tests.py
```

## Helper Scripts

### SVG

```bash
python3 scripts/svg_layout_audit.py path/to/file.svg
```

This is a heuristic preflight only.

It helps catch obvious risks like:

- text wider than its container
- cramped labels
- fragile centered text
- simple container/text mismatches

Final judgment still belongs to the rendered output.

### PPTX / PDF

```bash
python3 scripts/pptx_pdf_layout_audit.py path/to/file.pptx
python3 scripts/pptx_pdf_layout_audit.py path/to/file.pdf
```

Current behavior:

- `.pptx`: checks aspect ratio, scans text frames, flags obvious overflow and font-fragility patterns
- `.pdf`: checks metadata-level page count and page size via `pdfinfo`

This is intentionally honest tooling:

- useful preflight
- not a replacement for rendered thumbnail or page inspection

## Smoke Tests

```bash
python3 tests/run_smoke_tests.py
```

This validates:

- known-good and known-bad SVG fixtures
- generated known-good and known-bad PPTX fixtures
- expected pass/fail behavior of the audit scripts

## Future Enhancements

The repo includes a scored post-v1 backlog in [future_enhancements/README.md](future_enhancements/README.md).

That section exists for a reason:

- keep good ideas
- avoid skill fragility
- compare future work by `Effort / Uncertainty / Impact`
- separate backlog capture from core-skill mutation

Current high-interest ideas include:

- rendered QA helpers for exported assets
- low-fidelity layout mode before full polish
- background sub-agent QA and repair loops
- example-bank capture for periodic refinement

## License

MIT. See [LICENSE](LICENSE).
