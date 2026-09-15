# Research and architecture decisions

Reviewed September 15, 2026. This is a focused review of primary guidance, not an exhaustive survey or a claim that a framework guarantees quality.

| Source | Finding | Our design choice |
|---|---|---|
| [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | Simple composable workflows can outperform unnecessary architectural complexity. | Start with three skills and explicit checkpoints; add runtime infrastructure only for a demonstrated need. |
| [Anthropic: Context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Focused context and specialist handoffs can limit context overload. | Small task packets, linked evidence and short return reports rather than forwarding entire histories. |
| [Anthropic: Agent evaluations](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | Actual environment outcomes differ from an agent's claimed success; evaluation methods have different strengths. | Check observable artifacts, combine deterministic checks with human review, and keep outcome claims narrow. |
| [OpenAI: Trace grading](https://developers.openai.com/api/docs/guides/trace-grading) | Trace-level evaluation helps locate failures and compare workflow changes. | Record decisions, tool outcomes and evidence links; do not collect hidden reasoning or credentials. |
| [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview) | Graph orchestration supports persistence and deterministic/agentic steps. | Use a documented dependency graph now; consider an executable runtime only for durable unattended execution. |
| [OpenAI: Skills](https://developers.openai.com/codex/skills/) and [Claude Code: Skills](https://code.claude.com/docs/en/skills) | Both support folder-based skills; installation and host behavior differ. | Share core SKILL.md content, with a small host-specific installer. Do not imply local installation enables cloud accounts. |
| [Agent Skills specification](https://agentskills.io/specification) | A common format supports portable skill resources. | Keep core instructions plain Markdown and standard name/description metadata; avoid a vendor-specific runtime dependency. |

These choices are our application of the sources, not benchmark findings. No knowledge graph database is needed to track this small artifact set. A table linking requirements, decisions, tests and captures is enough initially.

## Public landing page recommendation

Lead with the designer's outcome, show the three skill modules, illustrate the workflow, then provide installation, project examples, evidence and contribution links. Label examples as prior work that informed the package. Avoid improvement percentages until a repeatable evaluation supports them.

Before a visual build, choose a name and brand/reference direction. A polished README is the first landing surface; a separate site should add visual examples and explanation rather than duplicate documentation. No site or account-level marketplace installation is included in this release.
