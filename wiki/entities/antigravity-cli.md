---
title: "Antigravity CLI"
slug: antigravity-cli
type: product
last_updated: 2026-05-27
---

# Antigravity CLI

## What It Is
Antigravity CLI is Google's closed-source successor to the open-source Gemini CLI, serving as the foundation for Google's managed AI agents in the Gemini API. Announced in late May 2026, it marked Google's second major open-source retreat in months, following the Gemma 3 licensing changes. Antigravity is powered by Gemini 3.5 Flash and enables tighter agentic workflow integration than its open-source predecessor.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | Google |
| Release Date | 2026-05-26 |
| Underlying Model | Gemini 3.5 Flash |
| Status | Closed-source |
| Predecessor | Gemini CLI (open-source) |

## Significance
The shift from Gemini CLI to Antigravity CLI represents a strategic pivot in Google's developer tooling. While open-source Gemini CLI was embraced by the community for its transparency and extensibility, Google chose to close-source to protect proprietary prompt engineering and enable tighter agentic workflow integration. However, this move alienates the developer community that initially adopted Gemini CLI precisely because it was open.

This pattern mirrors Microsoft's .NET and HashiCorp Terraform transitions to business licenses, where community forks emerged but eventually faded as the company out-invested open alternatives. The strategic logic is clear: control the deployment layer to capture value and protect proprietary advances.

## Connections
- [[entities/gemini-cli]] — Antigravity replaces the open-source Gemini CLI; Google argues closed-source enables tighter integration but this alienates the community that embraced it
- [[sources/google]] — Google is pushing Pro, Ultra, and free users from Gemini CLI to Antigravity; this is part of Google's broader agentic AI strategy
- [[topics/agentic_ai]] — Antigravity powers managed agents in Gemini API; Google aims to own the deployment layer where margins are higher and switching costs create lock-in
- [[ideas/agent-infrastructure-layer]] — The closed-sourcing of Antigravity follows the industry trend of controlling the deployment layer to capture value