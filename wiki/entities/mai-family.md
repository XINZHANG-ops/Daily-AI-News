---
title: "MAI Family"
slug: mai-family
type: model
last_updated: 2026-06-07
---

# MAI Family

## What It Is
MAI (Microsoft AI) is Microsoft's family of in-house AI models announced at Build 2026 and expanded June 6, 2026 with a seven-model drop co-designed with Maia 200 silicon. The family now includes coding models, reasoning models, speech models, transcription models, image generation models, and autonomous agents. The MAI family represents Microsoft's strategic pivot away from exclusive dependence on OpenAI and Anthropic for core AI capabilities.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | Microsoft |
| Announced | June 2, 2026 (Build 2026) |
| June 6 Expansion | Seven-model drop: MAI-Thinking-1, MAI-Code-1-Flash, MAI-Image-2.5, MAI-Transcribe-1.5, MAI-Voice-2, plus 2 more |
| Custom Silicon | Maia 200 (1.4x efficiency boost, co-designed) |
| Key Models | MAI-Thinking-1 (flagship reasoning), MAI-Code-1-Flash (5B coding), MAI-Image-2.5 (surpasses Nano Banana Pro on Arena), MAI-Transcribe-1.5 (5x faster, 43 langs), MAI-Voice-2 (15 langs) |
| Primary Use | Powers GitHub Copilot, enterprise AI agents, Windows Agent Runtime |
| Competition | Anthropic Claude Code, OpenAI Codex, Google Gemini 3.5 Flash, xAI Grok Build |

## Significance
Microsoft's June 6 expansion of the MAI family — seven models in a single day — is the clearest signal yet that the OpenAI partnership is no longer a moat but a hedge. MAI-Image-2.5 beating Nano Banana Pro on Arena is the most market-moving claim: Google's image model was the breakout hit of 2025, and Microsoft just declared it can out-image the image leader on its own silicon. The Maia 200 co-design story is the real tell: Microsoft is the only hyperscaler with paired foundation models + in-house training chips + distribution through M365 Copilot, a three-layer position that lets it price below AWS Bedrock and Google Vertex while gradually weaning the product off GPT-class models. The "seven models, one day" tactic is also a direct shot at the MAI-1/MAI-2 leak from earlier in the week — by pre-announcing breadth instead of one flagship, Microsoft forces the conversation to be about portfolio, not benchmark duels.

The April 2026 contract amendment that removed AGI clauses and Azure exclusivity gave Microsoft the freedom to train frontier models in-house. With Google also announcing Antigravity 2.0 at I/O, the OpenAI-Anthropic duopoly is breaking. The beneficiary is developers who gain negotiating leverage; the loser is any single AI provider that had assumed permanent lock-in.

MAI-Image-2.5 ranks third on the Arena leaderboard, directly attacking Midjourney's last strong differentiator. MAI-Thinking-1 positions Microsoft in the reasoning model race alongside OpenAI o-series and Anthropic's thinking models.

## Connections
- [[sources/microsoft]] — Microsoft developed MAI family to reduce dependence on OpenAI and Anthropic; powers GitHub Copilot
- [[entities/maia-200]] — Custom AI silicon co-designed with the MAI family; the vertical-integration pair that makes the seven-model drop possible
- [[sources/openai]] — Former primary partner for Copilot; now competing with Microsoft's in-house models
- [[sources/anthropic]] — Claude integration in Copilot but Microsoft building competing MAI stack
- [[entities/windows-agent-runtime]] — MAI family powers Windows Agent Runtime; makes Windows first-class runtime for autonomous AI agents
- [[entities/codex]] — OpenAI's coding model that MAI-Code-1-Flash competes with for GitHub Copilot mindshare
- [[entities/claude-code]] — Anthropic's coding assistant that MAI-Code-1-Flash competes with for enterprise developer adoption
- [[entities/gemini-3-5-flash]] — Google's coding model in the same competitive space; Pichai admitted being "a bit behind"
- [[entities/grok-build]] — xAI's $1/$2-per-million-tokens agentic coding model launching the same week — direct margin pressure on MAI-Code-1-Flash
- [[entities/mai-image-2.5]] — Specifically surpasses Nano Banana Pro on Arena; the market-moving claim in the seven-model drop
- [[ideas/agent-control-interface-wars]] — MAI's release adds another contender to the autonomy-vs-control debate in enterprise AI
- [[ideas/pricing-war]] — MAI family's portfolio approach forces the question of whether to compete on flagship or breadth
- [[ideas/vertical-integration]] — MAI + Maia 200 is the canonical case study of chip+model+agent+distribution vertical integration
