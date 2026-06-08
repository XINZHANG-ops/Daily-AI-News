---
title: "Gitpup Agent (Goldie)"
slug: gitpup-agent
type: repo
last_updated: 2026-06-08
---

# Gitpup Agent (Goldie)

## What It Is
Gitpup Agent (Cheesecaster/gitpup-agent, 1.8k stars, 92 forks) is a self-evolving "Golden Retriever" coding agent ("Goldie") that runs on the decentralized GitLawb network. It climbs a 6-stage skill tree (Puppy → Master), uses LLM reasoning to scan GitHub trending repos, generate PRs, and self-modify its own behavior. The defining feature is that the agent is the user: the skill tree, network positioning, and self-modification capability make the agent literally operate on its own development.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Repository | Cheesecaster/gitpup-agent |
| Stars | 1.8k |
| Forks | 92 |
| Network | Decentralized GitLawb network |
| Skill Tree | 6 stages (Puppy → Master) |
| Core Function | LLM reasoning to scan GitHub trending, generate PRs, self-modify behavior |
| Codename | "Goldie" (Golden Retriever metaphor) |

## Significance
Gitpup's 6-stage skill tree is the first literal packaging of agent verticalization as a gamified learning path. The agent's "level" determines what tasks it can handle, what network peers it can collaborate with, and what self-modification capabilities are unlocked. The "Puppy → Master" framing turns agent capability progression into a discoverable onboarding story — a developer (or another agent) can start with a constrained agent and watch it improve over time. The decentralized GitLawb network is the second novel element: the agent doesn't run on a centralized platform, it operates as a peer in a network where reputation/coordination is network-level, not platform-level.

The self-modification capability is the most architecturally distinctive element: the agent uses LLM reasoning to scan GitHub trending repos, generate PRs to itself, and modify its own behavior. This is "agent is the user" taken to the extreme — the agent's own development workflow is the use case.

## Connections
- [[topics/github_trends]] — 1.8k stars in a short window for a "self-evolving coding agent" is a strong signal that the category is moving from research to deployable patterns
- [[topics/agentic_ai]] — Gitpup's 6-stage skill tree is the first literal packaging of agent capability progression as a deployable pattern
- [[entities/snowey]] — Companion trend: Snowey takes the closed-loop skill auto-creation approach; Gitpup takes the gamified skill tree + self-modification approach — two different bets on "self-improving"
- [[entities/agent-ghost]] — Companion trend: AgentGhost's 6-tier memory is a static architecture; Gitpup's 6-stage skill tree is a dynamic progression — the 6-step pattern appears in two architecturally different implementations on the same day
- [[entities/openclaw]] — Gitpup's decentralized GitLawb network is positioned as an alternative to centralized agent platforms; OpenClaw's channel integration is the centralized model
- [[entities/claude-code]] — Claude Code is the "brain" model; Gitpup is the "self-modifying wrapper" that scans GitHub and uses Claude-class LLMs to generate PRs
- [[ideas/agent-verticalization]] — Gitpup's "Golden Retriever" 6-stage skill tree literalizes the agent verticalization as gamified progression
- [[ideas/agent-infrastructure-layer]] — Gitpup is the third open-source agent repo (with Snowey and AgentGhost) trending on the same day — the agent infrastructure layer is being commoditized from below
- [[timelines/2026-06]] — June 8: the "self-modifying agent" pattern crystallizes at the GitHub trending level
