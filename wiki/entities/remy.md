---
title: "Remy"
slug: remy
type: product
last_updated: 2026-05-08
---

# Remy

## What It Is
Remy is a new agentic AI system codenamed "Remy" that Google is developing for its Gemini platform. Unlike competing agents optimized for autonomous execution, Remy emphasizes enhanced user oversight and control mechanisms, allowing users to review and approve each step of multi-step agent workflows. The system represents Google's enterprise-focused, risk-averse approach to agent deployment.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | Google |
| Platform | Gemini |
| Codename | Remy |
| Focus | User control and approval gates for agent workflows |
| Status | In testing (as of May 2026) |

## Significance
Remy reveals a philosophical split in agent UX design. While OpenAI's Operator and Anthropic's Claude Code optimize for autonomous execution (fewer interruptions = faster results), Google is betting users want granular control — approval gates at each step. This reflects Google's risk-averse enterprise DNA: they're building for CIOs who need audit trails and compliance checkpoints, not just end-user efficiency. The timing is strategic — just as enterprises are waking up to agent security concerns, Google is positioning "controllable agents" as the enterprise-safe alternative.

## Connections
- [[topics/agentic_ai]] — Remy introduces a new UX philosophy to the agent market: human-in-the-loop by default rather than autonomy by default; this challenges the "agent-as-employee" model that Symphony and Claude Code promote
- [[sources/google]] — Remy reflects Google's enterprise sales strategy: building for CIO compliance needs rather than individual developer productivity; this is the same risk-averse DNA that produced Gemini's slower but more controlled rollout
- [[sources/openai]] — OpenAI's Operator and Codex optimize for autonomous execution with minimal human interruption; Remy's approval-gate model is a direct philosophical counter-position
- [[sources/anthropic]] — Claude Code similarly minimizes friction by integrating directly into the IDE workflow; Remy's step-by-step approval represents a fundamentally different trust model
- [[ideas/agent-control-interface-wars]] — Remy is the flagship example of the control-vs-autonomy split: Google bets on controllable agents for enterprise safety while competitors bet on autonomous agents for speed
- [[ideas/enterprise-ai-lock-in]] — Remy's approval-gate design pairs naturally with Google's enterprise sales machine; if CIOs mandate controllable agents, Google's existing cloud relationships make it the default choice regardless of model quality
- [[entities/symphony]] — Symphony's "every task gets an agent, agents run continuously" model is the polar opposite of Remy's human-approval-at-each-step approach; these two philosophies will compete for enterprise adoption
- [[ideas/indirect-prompt-injection-threat]] — Remy's granular control model is a response to the IPI threat: if every agent action requires human approval, malicious prompt injection has fewer opportunities to execute autonomously
