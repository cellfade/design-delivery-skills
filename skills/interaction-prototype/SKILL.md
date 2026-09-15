---
name: interaction-prototype
description: Build or refine a demo-ready interactive product prototype with coherent state, visible outcomes and recoverable errors. Use for selected multi-step or multi-role workflows; does not imply production infrastructure or a complete application.
---

# Interaction prototype

Demonstrate consequential choices at selected touchpoints. Use the project's brief, contract, references and existing implementation. Choose the simplest medium that supports the required interactions and review.

## Model what people must understand

Map actor, entry point, evidence/input, action, prerequisite, resulting state and next step. Separate independent dimensions when they have different meanings, such as assessment versus authorization, or saving versus delivery. Do not impose these particular dimensions on products that do not need them.

Write a small set of invariants for the domain. For asynchronous workflows, consider stale decisions, new evidence, duplicate actions and delayed receipt. For multiple records or roles, decide which state belongs to each record and which is shared.

Show simulation boundaries. A scenario selector may jump between examples, but it does not demonstrate that the transitions between those examples work. Distinguish seeded scenes from complete interactive paths.

## Build the visible path

Use references to identify the host product's visual and interaction patterns. If the user requests a screenshot backdrop, add the proposed interaction layer without rebuilding unrelated product areas. Clearly delimit interactive and illustrative controls.

Make prerequisites discoverable at the point of action. If a decision needs fields or a reason, let the user supply them in that context or provide a direct recovery route that preserves their draft. Associate errors with the actual missing prerequisite. A valid message must not hide a missing assessment, and a completed assessment must not remain blocked by stale form state.

Show the result beyond the submit button: parent list or map badge, record history, destination role and next action where relevant. Avoid contradictory badges derived independently from the underlying state.

## Verify transitions, not only scenes

Use [the risk-based acceptance matrix](references/acceptance-matrix.md) before declaring readiness. Choose cases by consequence rather than generating an exhaustive Cartesian product.

- Unit tests exercise consequential transition rules, stale data and sequence-dependent behavior where code exists.
- Browser or prototype walkthroughs start from the same visible entries a user would choose. Try action-first paths as well as the expected sequence.
- Capture before, error and recovered states for high-risk paths, with enough context to identify the record and role.
- Use actual viewport dimensions and screenshots for responsive claims. A failed viewport override is a coverage limitation, not a pass.

Any discovered blocker gets a regression case that would have caught it. Re-run impacted journeys after the fix; do not repeatedly broaden testing without a new risk or change.

Record the tested revision, environment, case, expected result, observation and evidence path. Keep unit, rendered, interaction and representative-user evidence distinct. A screenshot count is not a coverage measure.

## Handoff

Provide the demo route, alternate paths, reset behavior, seeded/simulated behavior and known limits. Capture product imagery only from a stable checked state. Publishing or external synchronization follows the user's existing authorization and the project release workflow.
