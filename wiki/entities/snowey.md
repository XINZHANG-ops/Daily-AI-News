---
title: "Snowey"
slug: snowey
type: repo
last_updated: 2026-06-08
---

# Snowey

## What It Is
Snowey (BlusceLabs/Snowey, 4.2k stars, 186 forks) is a self-improving autonomous AI agent with a closed learning loop: skill auto-creation, persistent memory (FTS5 session search), and model-agnostic support for 200+ models via OpenRouter. Ships with Telegram/Discord/Slack/WhatsApp/Signal gateways and one-click migration from OpenClaw.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Repository | BlusceLabs/Snowey |
| Stars | 4.2k |
| Forks | 186 |
| Architecture | Self-improving autonomous agent with closed learning loop |
| Memory | Persistent FTS5 session search |
| Model Support | 200+ models via OpenRouter (model-agnostic) |
| Distribution | Telegram, Discord, Slack, WhatsApp, Signal gateways |
| Migration | One-click from OpenClaw |

## Significance
Snowey is the week's flag-bearer for the "closed learning loop" pattern in open-source agents — skill auto-creation, FTS5-backed persistent memory, and model-agnostic execution via OpenRouter combine to create an agent that improves itself within a session without weight updates. The one-click OpenClaw migration is the strategic insight: the existing-agent ecosystem has reached a switch-cost inflection point, and Snowey bets that the integration story (Telegram/Discord/Slack/WhatsApp/Signal) plus closed-loop learning is enough to win share. The 4.2k stars in a short window signals that "self-improving agent" is now a recognized category in the GitHub trending, not just a research curiosity.

## Connections
- [[entities/openclaw]] — Snowey offers one-click migration from OpenClaw, positioning itself as the natural successor; the integration of the same channel gateways (Telegram/Discord/Slack/Signal) preserves OpenClaw's user value
- [[topics/github_trends]] — 4.2k stars in a short window confirms the "self-improving agent" category is recognized at the trending level
- [[topics/agentic_ai]] — Closed learning loop with skill auto-creation is the practical implementation of the "agent improves itself within session" pattern
- [[entities/agent-ghost]] — Companion trend on the same day: AgentGhost takes the 6-tier memory + DSPy/GEPA prompt optimization approach; Snowey takes the closed-loop skill auto-creation approach — two different bets on what "self-improving" means
- [[entities/gitpup-agent]] — Companion trend on the same day: Gitpup's 6-stage skill tree is the gamified version of what Snowey's skill auto-creation builds dynamically
- [[entities/mcp-protocol]] — Snowey's persistent FTS5 session search is the kind of memory layer that MCP servers typically externalize; Snowey internalizes the search to make the agent self-contained
- [[ideas/agent-verticalization]] — Snowey verticalizes to "agent + multi-channel gateway + self-improvement" — three features no single competitor combines at the same level of integration
- [[ideas/agent-infrastructure-layer]] — Snowey is one of three open-source agent repos (with AgentGhost and Gitpup-agent) trending on the same day — the agent infrastructure layer is being commoditized from below
- [[timelines/2026-06]] — June 8: the "self-improving agent" pattern crystallizes at the GitHub trending level
