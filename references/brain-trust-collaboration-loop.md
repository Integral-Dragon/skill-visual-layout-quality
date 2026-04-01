# Brain Trust Collaboration Loop

This note captures the first named operating form that emerged across Dex, Max, and Hopper.

It is better understood as a convergence protocol than as a simple review loop.

The point is not merely to get more opinions.

The point is to force a stronger shared model around an important problem while keeping one canonical integration path.

## Name

Primary name:

- `Brain Trust`

Expanded form:

- `Brain Trust collaboration loop`

## Why This Exists

This pattern is useful because three participants collaborating on the same problem force convergence toward a shared model more reliably than one-to-one interactions alone.

The main value is:

- reduced dyadic drift
- better pressure-testing of assumptions
- a clearer sense of progress and diminishing returns
- a stronger ability to separate structure from implementation
- preserved rationale about why a revision happened

## What Brain Trust Actually Is

Brain Trust is a named operating form under the broader multi-model collaboration family.

It is the pattern to use when:

- the problem is important enough that ordinary one-model iteration is not trustworthy enough
- one participant is better at synthesis and integration
- another participant is useful as an external critic or alternate reasoner
- Hopper wants a recoverable trail of why the work changed

Brain Trust is not primarily a "quality-control pass."

It is a structured way to:

- build
- critique
- reconcile
- decide whether another round is worth doing

## Participants

Generic term:

- `participant`

For the human specifically:

- `operator`

In this working example:

- `Dex`: Codex, used for implementation, synthesis, repo edits, and integration
- `Max`: Claude Max, used for independent critique, alternate reasoning, and structural pressure-testing
- `Hopper`: the human operator, used for intent setting, prioritization, and final judgment

## Two Interaction Forms

### 1. Mediated Brain Trust

This is the current primary mode.

The participants are not all talking in one shared room. Instead, Hopper mediates between Dex and Max, while Dex preserves the canonical artifact and synthesis trail.

This mode is valuable because:

- Hopper can buffer and redirect the conversation
- one model can critique another without the whole loop running away
- existing project/session context can be reused in the most relevant open harness

### 2. Shared-Room Brain Trust

This is a later exploration, not the default.

All participants would be able to read the same evolving log and respond directly into a shared collaboration surface.

Potential benefit:

- lower copy/paste friction
- richer direct interplay

Potential risk:

- more coordination noise
- weaker control over canonical state

## High-Level Shape

This pattern should be understood one level above roles-and-loop details.

The shape is:

1. one participant owns the canonical artifact
2. one participant acts as an external critic
3. one participant decides priorities and stopping points
4. the interaction is logged so reasoning and deltas are recoverable
5. ratings or other progress signals help decide when good enough is good enough

## Core Discoveries From This First Use

### Shared-Model Forcing Function

Three-party collaboration forces a better shared model.

With only one model plus Hopper, many sub-assumptions remain implicit.

### Rating Spread Matters

The raw score matters less than the spread and direction.

Useful signals:

- current quality rating
- improvement rating
- agreement/disagreement spread
- whether further effort seems worth it

### Canonical-Integrator Rule

This pattern works best when one participant remains the canonical integrator.

In this working version, that participant is Dex.

Without this rule, the collaboration creates parallel truths instead of convergence.

### Context Preservation Is A First-Class Need

The loop becomes much more useful if each participant can read:

- what was asked
- what changed
- what was criticized
- how the rating shifted

Without a recoverable log, too much value is lost in terminals and copy/paste handoff.

## Working Invocation

Natural invocation phrase:

- `invoke Brain Trust on this`

Meaning:

- bring Dex, Max, and Hopper into a structured collaboration mode around the current problem

Useful shorthand:

- `run Brain Trust on this artifact`
- `use Brain Trust for this workflow problem`
- `switch this into Brain Trust mode`

## What To Capture

Minimum capture set:

- original intent
- first implementation or structural pass
- external critique
- follow-up revision
- before/after ratings
- unresolved gaps
- any discovered failure classes or workflow insights

Minimum useful fields inside that capture:

- artifact or problem being worked
- canonical integrator
- external critic
- current rating or progress signal
- what changed because of critique
- whether another round is justified

## What This Is Not

- not a universal law for all model work
- not a replacement for normal one-model execution
- not yet a fully specified shared-room group chat protocol

## Project-Local Guidance

Use this pattern when:

- the problem is important enough to justify multiple perspectives
- one model is stronger at structure and another at implementation or critique
- progress is otherwise hard to evaluate

Keep the evidence near the artifact being evolved.

If a project does not yet have a local metaprocess layer, it is acceptable to begin with artifact-adjacent reference notes and promote them later.

## Minimal Current Form

The smallest useful mediated Brain Trust pass looks like this:

1. Hopper frames the problem and why it matters.
2. Dex produces or revises the canonical artifact.
3. Max critiques a pinned artifact or commit.
4. Dex classifies the critique and integrates what should change.
5. Hopper decides whether the spread, progress, and remaining gaps justify another round.

## Next Questions

- what is the best minimal logging format for cross-harness collaboration
- how should rating, confidence, and diminishing-returns signals be represented
- when should Brain Trust stay mediated versus move to a shared-room mode
- how much model effort should be spent before invoking outside critique
- when should a thin orchestrator skill be used instead of asking Hopper to manage copy/paste and handoff manually
