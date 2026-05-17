---
title: "AgentClaw"
slug: agentclaw
type: repo
last_updated: 2026-05-16
---

# AgentClaw

## What It Is
AgentClaw is a declarative agent workflow framework that turns one-sentence ideas into reusable capabilities. Features include computer/browser control, code/file operations, MCP integration, knowledge bases, memory, tracing, scheduling, and API/MCP publishing.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | Negai-ai |
| Stars | 92 |
| Forks | 9 |
| Key Feature | Declarative workflow specification |

## Significance
AgentClaw's declarative approach — "one sentence becomes a capability" — represents a philosophical shift from imperative agent programming (telling the agent what to do step by step) to declarative specification (describing the desired outcome and letting the agent figure out the steps). This mirrors the broader industry shift from prompt engineering to specification-driven development.

The built-in knowledge bases, memory, and tracing features address three of the most common failure modes in agent deployments: context loss between sessions, inability to learn from past interactions, and opacity when things go wrong. The API/MCP publishing feature suggests AgentClaw is designed not just for personal use but for building agent services that other agents can call.

## Connections
- [[entities/dulus]] — Dulus provides multi-provider tool execution; AgentClaw provides declarative workflow orchestration — they are complementary layers of the agent stack
- [[entities/evonic]] — evonic handles runtime communication and deployment; AgentClaw handles workflow design — together they cover the full agent lifecycle
- [[topics/github_trends]] — Part of the May 16 agent-framework trio; all three signal the ecosystem's rapid maturation beyond simple chat wrappers
- [[ideas/agentic-is-default]] — Declarative specification is the natural evolution of the agentic shift: users should state goals, not procedures
- [[ideas/spec-driven-development-movement]] — AgentClaw's "one sentence to capability" model directly embodies the spec-driven development philosophy emerging across the ecosystem