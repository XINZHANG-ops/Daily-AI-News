---
title: "AgentGhost"
slug: agent-ghost
type: repo
last_updated: 2026-06-08
---

# AgentGhost

## What It Is
AgentGhost (vventirozos/AgentGhost, 612 stars, 47 forks) is an autonomous FastAPI service wrapping an OpenAI-compatible LLM with 6-tier memory (vector, graph, profile, skill, journal, episodic), Docker-isolated tool execution, MCTS planning, swarm inference, and local DSPy/GEPA prompt optimization with no weight updates. It is the most architecturally ambitious agent to trend on GitHub the week of June 8, 2026.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Repository | vventirozos/AgentGhost |
| Stars | 612 |
| Forks | 47 |
| Architecture | FastAPI service wrapping OpenAI-compatible LLM |
| Memory Tiers | 6 (vector, graph, profile, skill, journal, episodic) |
| Tool Execution | Docker-isolated |
| Planning | MCTS (Monte Carlo Tree Search) |
| Inference | Swarm inference |
| Prompt Optimization | Local DSPy/GEPA (no weight updates) |

## Significance
AgentGhost represents the convergence of multiple research threads into a single open-source agent: 6-tier memory (each tier serves a different retrieval/recall pattern), MCTS planning (search-based reasoning at the action level), swarm inference (multiple model candidates for each decision), and local DSPy/GEPA prompt optimization (no fine-tuning required — the agent improves by re-prompting). The combination is the most architecturally ambitious of the week — most open-source agents pick one or two of these techniques; AgentGhost integrates all of them.

The "no weight updates" approach to self-improvement is the strategic insight: while Snowey uses closed-loop skill auto-creation and Gitpup uses gamified skill tree progression, AgentGhost treats prompt optimization as a first-class capability that can be run locally with DSPy/GEPA. This makes AgentGhost the most "research-flavored" of the three but also the one with the clearest path to production use cases where fine-tuning is restricted (e.g., regulated industries).

## Connections
- [[topics/github_trends]] — 612 stars in a short window for an architecturally ambitious agent (6-tier memory + MCTS + DSPy/GEPA) signals that "research-grade" agent architectures are reaching the GitHub trending level
- [[topics/agentic_ai]] — AgentGhost's 6-tier memory is the most architecturally detailed memory architecture to reach the trending level; pairs with MCTS planning and local prompt optimization for full-stack agent capability
- [[entities/snowey]] — Companion trend: Snowey takes the closed-loop skill auto-creation approach; AgentGhost takes the static 6-tier memory + DSPy/GEPA approach — two different bets on "self-improving"
- [[entities/gitpup-agent]] — Companion trend: AgentGhost's 6-tier memory is a static architecture; Gitpup's 6-stage skill tree is a dynamic progression — the 6-step pattern appears in two architecturally different implementations on the same day
- [[entities/mcp-protocol]] — AgentGhost's Docker-isolated tool execution is the kind of MCP server pattern that MCP-compliant agents typically externalize; AgentGhost internalizes tool isolation to make the agent self-contained
- [[entities/symphony]] — Symphony's research-validated multi-agent pattern is one architectural influence on AgentGhost's swarm inference design
- [[ideas/agent-infrastructure-layer]] — AgentGhost is the third open-source agent repo (with Snowey and Gitpup-agent) trending on the same day — the agent infrastructure layer is being commoditized from below
- [[ideas/agent-verticalization]] — AgentGhost verticalizes to "memory architecture + MCTS + DSPy/GEPA" — the most architecturally ambitious verticalization in the week's GitHub trending
- [[timelines/2026-06]] — June 8: the "architecturally ambitious open-source agent" pattern crystallizes at the GitHub trending level
