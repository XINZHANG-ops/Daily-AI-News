---
title: "multica"
slug: multica
type: repo
last_updated: 2026-05-10
---

# multica

## What It Is
multica is an open-source managed agents platform that turns coding agents into real teammates. It supports Claude Code, Codex, OpenClaw, OpenCode, Hermes, Gemini, Pi, and Cursor Agent within a unified local/cloud runtime. With 20.6K stars and 2.5K forks, it represents the emerging "agent orchestration as infrastructure" category.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Repo | multica-ai/multica |
| Stars | 20.6K |
| Forks | 2.5K |
| Supported Agents | Claude Code, Codex, OpenClaw, OpenCode, Hermes, Gemini, Pi, Cursor Agent |
| Runtime | Unified local/cloud |

## Significance
multica's value proposition is not building a better agent but managing the agents that already exist. By supporting eight major coding agents in one platform — with task assignment, progress tracking, and skill compounding — it addresses the fragmentation problem enterprises face when different teams adopt different agents. The "managed agents" framing signals a maturation from "which agent is best?" to "how do we coordinate the agents we've already adopted?" This mirrors the evolution of cloud infrastructure from raw VMs to orchestration platforms like Kubernetes.

## Connections
- [[entities/claude-code]] — multica treats Claude Code as one agent among many rather than the default; this multi-agent-neutrality is its core architectural bet
- [[entities/codex]] — Codex integration means OpenAI's coding agent can be assigned tasks and tracked alongside Anthropic's within the same organizational dashboard
- [[entities/openclaw]] — OpenClaw support validates multica's bet that enterprises will run multiple open-source agent stacks simultaneously
- [[topics/agentic_ai]] — multica is the orchestration layer above individual agents, reflecting the ecosystem's maturation from raw capabilities to fleet management
- [[ideas/agent-verticalization]] — By assigning tasks and tracking progress across specialized agents, multica enables the verticalization trend: one platform coordinates finance agents, coding agents, and research agents without forcing standardization on a single model
- [[sources/anthropic]] — Anthropic's Claude Code is the most popular enterprise coding agent; multica's support for it is table stakes for any orchestration platform
- [[sources/openai]] — Codex's 3M weekly users make it a mandatory integration for any agent management platform aiming at enterprise scale
