---
title: "evonic"
slug: evonic
type: repo
last_updated: 2026-05-16
---

# evonic

## What It Is
evonic is an open agentic AI platform for designing, deploying, and orchestrating intelligent agents. Features include multi-agent swarms, workplace execution (local/remote/cloud), agent-to-agent communication, heuristic safety detection, and channel support for Telegram, WhatsApp, Discord, and Slack.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | anvie |
| Stars | 97 |
| Forks | 12 |
| Key Feature | Multi-agent swarms with cross-platform channel integration |

## Significance
evonic is notable for treating agents as a communication layer rather than just a task-execution layer. By integrating with Telegram, WhatsApp, Discord, and Slack, evonic positions agents as participants in existing human communication channels — not standalone interfaces users must learn.

The "workplace execution" model (local/remote/cloud) reflects the infrastructure reality that agents need deployment flexibility: some tasks require on-device privacy, others need cloud-scale compute. The heuristic safety detection layer addresses a gap in most open-source frameworks — most provide tools but not guardrails.

## Connections
- [[entities/dulus]] — Both are multi-provider agent frameworks from May 16, but evonic targets enterprise orchestration while Dulus targets individual developers
- [[entities/agentclaw]] — AgentClaw focuses on declarative workflow specification; evonic focuses on runtime orchestration and communication — they address different layers of the agent stack
- [[topics/agentic_ai]] — evonic's channel integration strategy (meeting users where they communicate) is a distribution insight that proprietary labs may copy
- [[ideas/agentic-is-default]] — Cross-platform agent deployment treats AI as ambient infrastructure rather than a destination app
- [[ideas/agent-control-interface-wars]] — evonic's safety detection layer is a runtime governance approach, distinct from Google's approval-gate model or Anthropic's native security scanning