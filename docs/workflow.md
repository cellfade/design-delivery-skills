# Workflow and orchestration

The coordinator owns a project contract, not the entire implementation. Each node has inputs, an owner, output evidence and a completion condition. Prototype and narrative can proceed independently once the framing is agreed; final screenshots depend on verified interactions.

## Shared state

Maintain only what the project needs: brief/rubric, supplied facts, assumptions, scope, decisions, artifact revisions, acceptance cases, blockers, budget and next step. Persist this in project files so either host can resume. A compact requirement-to-decision-to-test-to-capture table provides traceability without a graph database.

## Handoff packet

Include objective, permitted files/actions, relevant evidence, dependencies, definition of done, time budget and stop condition. Return artifacts, checks performed, limitations and decisions needed. A handoff is not authority to publish or change unrelated resources.

Use parallel workers only when authorized and their tasks are independent enough to justify coordination cost. Assign one owner per mutable artifact and one integrator for shared state. A reviewer should try unexpected user routes, not merely replay the implementer's demonstration.

## Bounded loops

Set the iteration/time budget for the task. A failed check routes back to its responsible node with a reproducible observation. Stop and surface a blocker if repeated iterations do not improve the result or require unavailable input. A critical unresolved defect cannot become a pass because the budget ended. Quality checks are completion evidence, not a reason to ask permission for routine authorized edits.

## Resume

Read the latest contract, revision and open evidence items; verify drift before resuming. Store outcome summaries and tool evidence, not hidden reasoning. Mark stale screenshots or design files explicitly.

## Optional executable graph

Only add a graph runtime when actual requirements include durable scheduled execution, recovery across processes or programmatic branching. Skills alone do not execute a background workflow. The current graph is instructional and manually coordinated by the active host.
