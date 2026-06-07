---
title: "Grok Build 0.1"
slug: grok-build
type: model
last_updated: 2026-06-07
---

# Grok Build 0.1

## What It Is
Grok Build 0.1 is xAI's first dedicated agentic coding model, released June 5, 2026 by SpaceX/xAI. It generates at 100+ tokens/second with a 256K context window, priced at $1/M input and $2/M output. Day-one integrations span Cursor, Hermes Agent, OpenClaw, Kilo Code, and OpenCode. The "Build" naming signals xAI's pivot from chatbot to build-tool.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Developer | xAI / SpaceX |
| Release Date | 2026-06-05 |
| Type | Dedicated agentic coding model |
| Speed | 100+ tokens/second |
| Context Window | 256K |
| Pricing | $1/M input, $2/M output (40-60% below Claude Code Opus 4.8) |
| Day-One Integrations | Cursor, Hermes Agent, OpenClaw, Kilo Code, OpenCode |

## Significance
Grok Build 0.1 is the most aggressive pricing in the agentic-coding category — and it comes from the company with the most to lose by NOT being in the IDE. At $1/$2 per million tokens, xAI is roughly 40-60% below Claude Code (Opus 4.8: $5/$25) and 80% below GPT-5.4-Codex, while offering comparable or better agentic-coding throughput via the Hermes Agent and OpenClaw ecosystem. The strategic logic: xAI's consumer brand is fractured after the safety controversies, but the developer-tools distribution (Cursor, OpenCode, Kilo Code) is a different funnel with different rules — and IDE seats are the only consumer surface where the company can convert usage into revenue without a subscription app. The "Build" naming is the giveaway: this is xAI's bid to be the build-tool, not the chatbot. SpaceX capital buys them time to take subscale margins for 18-24 months.

## Security Vulnerabilities
Grok Build was identified as vulnerable to three critical security flaws discovered in May 2026:
- **SymJack** — Symlink hijacking allows remote code execution
- **TrustFall** — Folder trust prompt can be weaponized  
- **Mini Shai-Hulud** — Settings injection enables persistence

These vulnerabilities are shared across multiple AI coding agents, indicating systemic architectural flaws in the category rather than vendor-specific issues.

## Connections
- [[entities/grok-4-3]] — The Grok model powering Grok Build
- [[sources/xai]] — xAI's developer tools division; 0.1 release is xAI's bid to be the build-tool, not the chatbot
- [[entities/symjack]] — Vulnerability affecting Grok Build
- [[entities/trustfall]] — Vulnerability affecting Grok Build
- [[entities/mini-shai-hulud]] — Vulnerability affecting Grok Build
- [[topics/ai_security]] — Security vulnerabilities in AI coding agents
- [[entities/claude-code]] — Grok Build 0.1 priced 40-60% below Claude Code Opus 4.8; direct margin pressure on Anthropic
- [[entities/codex]] — xAI's $2/M output is 80% below GPT-5.4-Codex; positions Grok Build as the low-cost agentic coding option
- [[entities/maia-200]] — Microsoft's MAI-Code-1-Flash launched the same week; Grok Build vs MAI-Code-1-Flash is the new price war
- [[entities/nex-n2]] — Same-week open-source Qwen3.5-based agentic model (80.8% SWE-Bench Verified) at zero cost; deepest pressure on premium agentic coding
- [[entities/cursor]] — Day-one integration partner; Cursor multi-agent support now spans xAI alongside OpenAI/Anthropic
- [[ideas/pricing-war]] — Grok Build 0.1 is the agentic-coding battleground: xAI's 40-60% price cut vs Opus 4.8 forces the pricing war to the agent layer
- [[sources/spacex]] — SpaceX capital funds xAI's 18-24 months of subscale margins; the build-tool bet is SpaceX-funded