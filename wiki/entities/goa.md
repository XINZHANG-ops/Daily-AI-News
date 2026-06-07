---
title: "GoA (Graph-of-Agents)"
slug: goa
type: repo
last_updated: 2026-06-07
---

# GoA (Graph-of-Agents)

## What It Is
GoA (Graph-of-Agents) is a test-time inference framework that dynamically selects and orchestrates specialized language models as a collaborative graph. Published at ICLR 2026, the framework was released by UNITES-Lab with 25 GitHub stars as of June 7, 2026. GoA treats the multi-agent orchestration problem as a graph routing decision at inference time, not a fixed pipeline.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | UNITES-Lab |
| Publication | ICLR 2026 |
| Stars (Jun 7) | 25 |
| Architecture | Dynamic graph of specialized LMs |
| Approach | Test-time inference orchestration |
| Use Case | Collaborative multi-model problem solving |

## Significance
GoA represents the academic cousin of production agent orchestration frameworks like Multica (20.6K stars) and Agent Squad. The key innovation is treating agent selection and routing as a graph problem solved at test time, allowing different specialized models to be selected per query based on the current state. The ICLR 2026 publication gives it academic credibility even as the star count remains modest. The framework's emergence in the same week as Meta's HyperAgents and xAI's Grok Build 0.1 shows the agent infrastructure layer is being approached from three angles: production (Grok Build), research (HyperAgents), and academic (GoA). GoA's "specialized LMs as a collaborative graph" concept aligns with IBM Bob's multi-model routing and Perplexity Computer's "20+ AI models for different tasks" — the multi-model future is being formalized across the stack.

## Connections
- [[topics/agentic_ai]] — Part of the multi-agent orchestration framework wave
- [[entities/agent-squad]] — Amazon-style multi-agent framework with supervisor pattern; GoA formalizes the graph approach
- [[entities/multica]] — Production multi-agent platform; GoA is the academic test-time equivalent
- [[entities/ibm-bob]] — IBM Bob's multi-model orchestration matches GoA's specialized-LM-as-graph concept
- [[entities/perplexity-computer]] — Perplexity's 20+ AI models coordinating different tasks is a production example of GoA's approach
- [[topics/github_trends]] — Trending repo with academic provenance; signals the academic community is engaging with the agent wave
- [[entities/hyperagents]] — Same week release; HyperAgents focuses on self-improvement, GoA on test-time orchestration
- [[ideas/agent-infrastructure-layer]] — GoA's graph-of-agents pattern is a notable contribution to agent infrastructure design
- [[ideas/boring-infrastructure-shift]] — Multi-model orchestration is the "boring infrastructure" that makes agent ecosystems possible
- [[ideas/system-competition-shift]] — GoA formalizes the shift from "best single model" to "best model composition"
