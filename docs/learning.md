# Evidence-driven improvement

Self-improvement means a versioned learning loop, not automatic rewriting of installed instructions.

1. During authorized project work, capture a concrete failure or user correction in that project's notes. Keep client content, secrets and raw transcripts out of this public repository.
2. Describe the smallest generalizable lesson, its evidence and where it should not apply. A single preference is not a universal rule.
3. Add or select a realistic evaluation scenario with observable outcomes.
4. Compare baseline and candidate on the same task and resources. For nondeterministic results, repeat enough trials to understand variance and report the sample count.
5. Use deterministic tests for behavior, rendered evidence for visual claims, and human judgment for clarity and taste. A model's self-score is insufficient.
6. Propose a small pull request containing the change, results, regressions, cost/time impact and rollback path. A maintainer reviews before merging.
7. Tag a version and explicitly update local installations. Failed candidates stay out of installed skills.

## Candidate record

- Observed problem and evidence
- Proposed change and scope
- Baseline/candidate revision and host/model
- Scenario, observations, artifacts and trial count
- Improvement, regressions and limitations
- Decision: accept, revise or reject

Do not automatically push private traces, broaden permissions, install new dependencies or schedule recurring work. No telemetry is collected by this package. The installer preserves a prior managed version for rollback.

The first release has structural and installer checks only; model behavioral trials remain pending. Use evals/scenarios.json as a starter set and add held-out tasks before claiming general improvement.
