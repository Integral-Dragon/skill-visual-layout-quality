# Hopper Ideas

## 1. Rust helper utilities for higher-speed layout tooling

Explore building Rust helper utilities that start as supplements to the Python tools and only replace them if profiling shows a real speed win.

Possible targets:

- SVG preflight helpers
- rendered-asset QA helpers
- PDF/image processing utilities
- batch-oriented inspection pipelines

Why it matters:

- asset generation and validation time will matter more as quality expectations rise
- if the skill grows into more rendering, rasterization, or batch-inspection work, execution speed could become a practical bottleneck
- starting as supplements is safer than rewriting the current Python scripts on faith

Current Dex read:

- this is more compelling for future rendered-QA helpers than for the current lightweight preflight scripts
- the present Python scripts are small enough that a full rewrite would probably not pay off yet
- the right trigger is profiling evidence, not language preference

Scores:

- Effort: `4`
- Uncertainty: `4`
- Impact: `3`

## 2. Background sub-agent QA and repair loop

Allow the main asset-generation thread to apply the skill prescriptively during composition, then spin up background sub-agents to:

- render the output
- inspect it against the layout rules
- report findings back quickly
- fix issues in parallel when the failures are straightforward

Desired behavior:

- Hopper does not wait idly for a full serial QA pass
- sub-agents can validate or remediate while the main thread moves on
- only meaningful problems or final reconciliations need to come back to the main thread

Why it matters:

- elapsed wall-clock time matters more than token efficiency here
- this fits the actual usage pattern of the skill:
  - build first
  - inspect rendered output
  - repair if needed
- it could turn the optional validation round into something that feels much less expensive to Hopper

Current Dex read:

- conceptually strong
- most useful once the rendered-QA path is more tool-backed and standardized
- best version is probably:
  - main thread generates asset
  - background worker renders/inspects
  - worker auto-fixes only bounded issues
  - main thread reconciles the final state
- biggest uncertainty is not model behavior; it is workflow design and write-scope safety

Scores:

- Effort: `4`
- Uncertainty: `3`
- Impact: `5`

## 3. Shared example bank for periodic skill refinement

When background QA finds a real layout defect and fixes it, store the case in a shared example bank instead of immediately mutating the skill.

The bank would capture things like:

- original asset or reduced repro
- what failed in the rendered output
- what fix resolved it
- whether the failure was format-specific or general
- whether it looks like a recurring class or a one-off edge case

Desired behavior:

- do not rewrite the skill every time a single failure occurs
- accumulate evidence over time
- periodically review the bank and only generalize where the pattern is real

Why it matters:

- direct per-failure updates can make the skill brittle or overfit weird cases
- a bank of real examples creates a better basis for:
  - new failure classes
  - improved test fixtures
  - better heuristics
  - better implementation guidance

Current Dex read:

- this is a very good governance mechanism for the skill
- especially valuable if background QA/remediation becomes common
- best implemented as a triage layer:
  - capture
  - cluster
  - periodically review
  - promote only stable patterns into the core skill

Scores:

- Effort: `3`
- Uncertainty: `2`
- Impact: `5`

## 4. Low-fidelity layout mode before full polish

Add a low-fidelity mode for early layout work:

- rough wireframe or paper-prototype style composition
- minimal styling
- fast spacing and hierarchy checks
- quick approval of structure before expensive polish/export work

Then, once the low-fidelity layout looks right:

- the main thread or a background worker can apply the full visual treatment
- background QA can inspect the polished version
- only the final pass pays the full rendering and validation cost

Why it matters:

- layout failures are often visible before visual polish matters
- this could shorten the feedback loop for:
  - card sizing
  - spacing rhythm
  - hierarchy
  - overflow risk
- it also has standalone value as a design workflow, even if time savings are only moderate

Current Dex read:

- strong idea
- probably best expressed as an operating mode of the skill rather than a separate skill
- especially useful for slides, infographics, README heroes, and diagram-like assets
- combines well with background QA:
  - low-fi first
  - approve structure quickly
  - polish in parallel
  - validate rendered output after

Scores:

- Effort: `3`
- Uncertainty: `2`
- Impact: `4`
