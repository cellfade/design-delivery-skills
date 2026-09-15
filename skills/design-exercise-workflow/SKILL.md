---
name: design-exercise-workflow
description: Coordinate a product design brief into a scoped interactive prototype and evidence-based case study, with shared decisions, review checkpoints and presentation handoff. Use for paired deliverables or design exercises, rather than an isolated UI edit.
---

# Design exercise workflow

Produce two connected deliverables: an interactive demonstration of selected decisions and a case study that explains their rationale. Scale the workflow to the assignment's actual timebox. A working frontend is optional if another prototyping medium better fits the brief.

## Establish the contract

Read the actual brief before relying on summaries or third-party reviews. Extract evaluation criteria, minimum deliverables, time expectations, submission deadlines, supplied facts and restrictions. Distinguish the timebox from submission lead time. Preserve previously submitted documents unless the user requests a change.

Create or update a short project contract using [the template](references/project-contract.md). Separate supplied facts, hypotheses, observed results and open questions. Identify which audience needs the immediate outcome and why secondary audiences are deferred. Mark each promised behavior as working, simulated, illustrated or outside scope.

Choose a scope that can demonstrate a meaningful user outcome within the time available. Keep a list of optional ideas. Do not automatically turn suggestions or interesting extensions into implementation work. For a late addition, assess its effect on the existing narrative, testing and deadline; offer a bounded substitution when appropriate.

## Coordinate the two deliverables

Use `interaction-prototype` and `product-case-study` if installed. Otherwise follow these outcomes directly; missing companion skills are not a reason to stop.

- Prototype: one complete consequential journey, plus relevant failure and recovery paths. Define shared state and terminology before splitting implementation.
- Case study: start an outline alongside the prototype. Explain the problem and choices early; insert verified captures as the design stabilizes.
- Maintain one project decision log and artifact index. Record the source of each fact and whether a design change affects screenshots, copy, diagrams or design files.

Use existing design, writing, imagery, testing and deployment skills only when relevant and available. Do not duplicate their tool procedures here. Respect the user's references and writing preferences without generalizing them to unrelated projects.

If delegation is authorized and useful, assign bounded ownership: interactions/state, case-study narrative/layout, independent acceptance review. One integrator owns shared terminology and merge decisions. Do not let multiple contributors edit shared state or publish concurrently without coordination.

## Checkpoints

Use checkpoints as observable completion criteria, not automatic permission requests:

1. **Framing:** a reader can identify the problem, users, constraints and scope; each material claim has a source or assumption label.
2. **Interaction:** a user can complete the selected journey and recover from tested errors through the visible UI. State tests and screenshots support different claims.
3. **Presentation:** the page explains the choices, distinguishes design process from product workflow, and keeps optional depth out of the main route.
4. **Release:** required checks pass for the intended revision; deployment, links, metadata and default demo state are verified. Explicitly list unsynchronized artifacts and coverage limits.

Before release, agree a freeze boundary proportional to time remaining. After that boundary, prioritize broken interactions, inaccurate claims and presentation blockers. Do not add optional imagery or workflows merely to increase polish.

## Close the loop

Deliver the usable links, a short rehearsal route, tested coverage and limitations. Never equate agent walkthroughs with research involving representative users. Avoid claims that all states are tested.

After the presentation, capture observed feedback separately from predictions. Extract recurring lessons and make narrow skill improvements. Leave the live submission unchanged during retrospective analysis unless requested.

## Shared-host execution and learning

Use a compact handoff record with objective, inputs, authorized scope, owner, completion evidence and stop condition. Keep iteration budgets explicit. Parallel tasks need independent ownership; shared mutable state has one integrator. Resume from the project contract and evidence index, checking revision drift.

After a demonstrated failure, record a candidate lesson in project notes and propose the smallest skill change with a regression scenario. Compare baseline and candidate behavior before promoting it. Do not automatically rewrite installed skills, publish private traces, merge changes or create scheduled work. Host-specific installation does not imply cloud-account availability.
