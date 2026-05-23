---
title: "Symphony"
slug: symphony
type: protocol
last_updated: 2026-05-02
---

# Symphony

## What It Is
OpenAI's open-source specification for orchestrating Codex coding agents at scale. The core model: every open task gets a dedicated agent; agents run continuously; humans review results. Project-management boards become the control plane for coding agent fleets. Language-agnostic with reference implementations in TypeScript, Go, Rust, Java, and Python. 15K+ GitHub stars within days of release.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Release Date | 2026-04-27 |
| Creator | OpenAI |
| Stars | 15K+ |
| Languages | TypeScript, Go, Rust, Java, Python |
| Key Metric | 500% PR increase on internal OpenAI teams |

## Significance
Symphony formalizes the "agent-as-employee" pattern that has been emerging across the industry: treat AI coding agents not as tools but as workers on a team board. The 500% PR increase at OpenAI internal teams suggests the bottleneck in software development has shifted from code generation to task allocation and review — exactly what Symphony addresses. It complements Microsoft E7 (AI agents bundled at $99/user/month) and GitHub Copilot Agent Tier ($49/agent/month) to create a full-stack agent deployment model: Symphony defines the orchestration protocol, Microsoft bundles the governance, and repos like karpathy's CLAUDE.md skills and Context Mode optimize individual agent behavior. However, the model also introduces systemic risk: if every task gets an agent and agents run continuously, the cascading failure modes the Five Eyes guidance warns about become operational reality at scale.

## Connections
- [[entities/codex]] — Symphony is the orchestration layer for Codex; turns individual coding agents into fleets managed like employees on a team board
- [[entities/copilot-agent-tier]] — GitHub's $49/agent/month pricing is the economic counterpart to Symphony's orchestration model; together they form the agent-scale deployment stack
- [[ideas/agent-economics]] — Symphony's "every task gets an agent" model is the demand side of the agent economics equation; Copilot Agent Tier is the supply-side pricing response
- [[topics/agentic_ai]] — Symphony represents the mainstreaming of agent orchestration; the 15K+ stars in days signals the industry is converging on this pattern
- [[sources/openai]] — Symphony is OpenAI's first major open-source infrastructure contribution, positioning Codex as a platform rather than just a product
- karpathy's CLAUDE.md skills (105K stars) — Complements Symphony by optimizing individual agent behavior, while Symphony handles fleet-level orchestration
- [[entities/context-mode]] — Addresses the context efficiency problem that Symphony's continuous agent model exacerbates; more agents means more context pressure
