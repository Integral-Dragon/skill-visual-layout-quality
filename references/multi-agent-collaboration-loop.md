# Multi-Agent Collaboration Loop

This note captures the working pattern that has been productive across Dex, Max, and Hopper.

## Roles

- `Dex`: Codex, used for implementation, structural edits, and direct repo work
- `Max`: Claude Max, used for independent critique, review, and alternate reasoning
- `Hopper`: the human operator, used for intent setting, prioritization, and final judgment

## Loop

1. Hopper sets intent, constraints, and desired level of rigor.
2. Dex makes the first implementation pass or structural revision.
3. Max reviews the result independently and points out structural issues, missing cases, and risk.
4. Dex applies the follow-up pass.
5. Hopper evaluates the tradeoff and chooses whether to continue or ship.
6. The review round and rating delta are recorded so the collaboration can evolve instead of resetting each session.

## What To Capture

- the original intent
- the first implementation or design pass
- the external critique
- the revision made in response
- the before/after rating
- any failure classes or workflow gaps discovered along the way

## Why It Helps

- It creates a trace of how the three perspectives evolve together.
- It preserves useful critique instead of treating it as disposable chat.
- It makes future review rounds more disciplined because the prior deltas are visible.

## Usage Guidance

Treat this as a project-local collaboration pattern, not a global law.

If the loop starts producing useful precedent, promote the note into the relevant project-local metaprocess area or registry layer rather than keeping it only in chat history.
