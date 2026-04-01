# Brain Trust Origin Note: 2026-03-31

This note captures the first emergence of the Brain Trust pattern in this repo context.

## Origin Situation

The immediate trigger was recurring frustration with visual layout quality across generated assets.

Initial problem shape:

- Dex was struggling with layout quality in the course-website work
- Max was brought in because Hopper expected stronger visual implementation
- Max also showed recurring failures
- the work was burning too much time as one-off fixes

That shifted the problem from:

- `fix this visual`

to:

- `improve the general capability behind these visual failures`

This was the first important turn.

The time sink was no longer just a bad asset.

The time sink was the repeated pattern of fixing the same class of problem one artifact at a time.

## Why The Interaction Became Different

This was not just "ask another model for help."

Several conditions made the collaboration unusually productive:

- Dex had direct project context from the active repo session
- Max had recent context from parallel work on the same class of issue
- Hopper used Dex to synthesize and rewrite prompts for Max
- Dex and Max both produced ratings, which made progress easier to judge
- critique was being turned into checked-in deltas instead of remaining disposable chat

Another important condition was that Dex was already active inside the relevant repo context, while Max had parallel context from working the same problem class in another harness.

That meant the collaboration started with live context instead of from a cold prompt.

## Key Insights Hopper Surfaced

### 1. The real issue was deeper than the immediate skill

The visual-layout-quality effort started as a skill problem, but Hopper recognized it was also:

- a workflow problem
- a context-capture problem
- a multi-model coordination problem

### 2. Ratings are useful as a control signal

The number itself matters less than:

- whether the scores are converging
- the spread between participants
- whether additional effort seems worth it

This matters because Hopper often needs to decide whether to keep spending time on a workflow improvement or accept that it is good enough for now.

Brain Trust made that decision less arbitrary.

### 3. Copy/paste handoff is lossy

Having Dex generate prompts for Max was useful, but Max did not automatically receive the surrounding context and rationale.

That exposed the need for:

- persistent logs
- explicit review notes
- artifact-linked evolution records

It also exposed a practical need for a better logging substrate.

Without that, a participant can see the prompt being forwarded but not the surrounding rationale, objections, or interpretation that led to it.

### 4. There are two distinct interaction models

The first model is the mediated model:

- Hopper speaks separately with Dex and Max
- Dex remains the canonical integrator

The second is a future shared-room model:

- all participants can read the same collaboration log directly

This note is about the first model.

### 5. Role separation can be psychologically useful

Hopper described Dex as stronger at high-level structure and Max as stronger at certain implementation tasks.

Whether or not that remains universally true, the perceived role split was useful because it made critique feel less redundant and made the collaboration easier to steer.

### 6. This raised broader questions than the immediate skill

The collaboration surfaced several questions that are still open:

- how much model effort should be spent before outside critique is invoked
- how should diminishing returns be represented
- how much should skill layering be preferred over monolithic "uber skills"
- whether future participants such as Gemini should be able to join by reading the same captured trail
- whether some capability profiles should be grounded in model cards or research instead of intuition alone

## Why The Name Matters

`Brain Trust` is a better invocation name than a literal tool-name phrase like `Dex-Max-Hopper collaboration loop`.

It is:

- easier to remember
- easier to invoke in live work
- high-level enough to cover future variants

It also avoids making the pattern sound like a rigid fixed trio.

`Brain Trust` can survive changes in the exact participants while preserving the operating idea.

## What This Note Should Preserve

The point is not to preserve every utterance.

The point is to preserve:

- why the pattern emerged
- why it felt more productive than ordinary one-model iteration
- what interaction mechanics mattered
- what future tooling or metaprocess work it suggests

## Relationship To Review Notes

This note is upstream of the tactical review notes.

- `review-round-2026-03-31.md` captures critique and deltas for the skill artifact
- this note captures why the collaboration mode itself became interesting enough to name and formalize

## Backlog Surfaced By The First Use

The first use surfaced several follow-on items that should not be lost:

- rename or tighten the name of the visual-layout-quality skill
- decide whether a thin orchestrator skill should load layered skills instead of merging them
- improve persistent cross-harness logging so participants can recover the actual interaction trail
- revisit high-effort versus multi-pass execution as a reusable decision rule
