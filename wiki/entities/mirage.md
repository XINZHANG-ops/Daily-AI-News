---
title: "Mirage"
slug: mirage
type: repo
last_updated: 2026-05-12
---

# Mirage

## What It Is
strukto-ai/mirage is a unified virtual filesystem for AI agents. It mounts services like S3, Google Drive, Slack, Gmail, Redis, GitHub into a single filesystem that agents can navigate with familiar bash commands. Supports OpenAI Agents SDK, Vercel AI SDK, LangChain, Pydantic AI, and OpenHands.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Stars | 2,000+ |
| Forks | 129 |
| Creator | strukto-ai |
| Primary Use | Unified storage abstraction for agents |

## Significance
Mirage addresses a core friction in agent deployment: agents need to interact with dozens of different APIs and storage systems, each with their own auth, protocols, and semantics. By providing a filesystem abstraction, Mirage lets agents use familiar `cd`, `ls`, `cat`, and `cp` commands across cloud services. This is infrastructure that treats agents as first-class users of the cloud rather than applications that call APIs.

The timing is notable: TerminalBench 2.0 showed agents still fail 18-35% of CLI tasks, and tools like Mirage represent where the ecosystem is actually investing energy — in better tooling, not just better models.

## Connections
- [[topics/agentic_ai]] — Mirage's unified filesystem abstraction is exactly the kind of agent infrastructure the ecosystem needs; TerminalBench 2.0 proved models alone won't close the deployment gap
- [[topics/github_trends]] — Trending at 2k stars as developers vote for infrastructure over raw model access
- [[entities/openhands-sdk]] — Supports OpenHands among other agent frameworks; signals convergent evolution on unified abstractions
- [[entities/terminal-bench-2]] — TerminalBench's unsaturated scores prove agents need better tooling; Mirage is the filesystem layer of that tooling
- [[ideas/agent-infrastructure-layer]] — Mirage, OpenSquilla, and HiDream all solve the same problem from different angles: unified abstractions hiding complexity from agents
