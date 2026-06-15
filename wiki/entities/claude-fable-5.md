---
title: "Claude Fable 5"
slug: claude-fable-5
type: model
last_updated: 2026-06-11
---

# Claude Fable 5

## What It Is
Claude Fable 5 is Anthropic's first public Mythos-class model, released June 9, 2026 — six weeks after the restricted Claude Mythos Preview began scoring 93.9% on SWE-bench Verified. Fable 5 shares the same architecture as Claude Mythos 5 but routes ~5% of high-risk prompts (cyber, bio, chemical) to Claude Opus 4.8 via a different safety layer. It scores 80.3% on SWE-bench Pro — a benchmark no other public model has crossed 80% on — and ships with a pricing reset: $10/M input, $50/M output, exactly 2× Claude Opus 4.8 but under half the cost of the earlier Mythos Preview private API. The release lands less than 72 hours after Jack Clark and Marina Favaro's "When AI builds itself" essay calling for a coordinated "brake pedal" on frontier AI.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Release Date | 2026-06-09 |
| Creator | Anthropic |
| Architecture | Same as Claude Mythos 5 (with restricted-routing safety layer) |
| SWE-bench Pro | 80.3% (first public model to cross 80%) |
| SWE-bench Verified | ~92% (estimated, between Opus 4.8 at 88.6% and Mythos at 93.9%) |
| Input Price | $10 / M tokens (2× Opus 4.8) |
| Output Price | $50 / M tokens (2× Opus 4.8) |
| Routing | ~5% of cyber/bio/chem prompts to Claude Opus 4.8 |
| Free Access | Pro, Max, Team, Enterprise tiers |
| Distribution | api.anthropic.com, AWS Bedrock, Google Vertex AI |

## Significance
Fable 5 is the strategic resolution of the Mythos restriction problem Anthropic has been negotiating since March. The 5% high-risk routing proves Anthropic can ship a Mythos-class model publicly without fully exposing the cyber/bio capability surface — turning the safety-restricted release pattern from a marketing liability into a product feature. Pricing at exactly 2× Opus 4.8 (and under half the cost of Mythos Preview's private API) is calibrated to capture the enterprise premium while making the safety overhead visible on the rate card rather than hidden in a waitlist.

On June 10, 2026, Anthropic reversed its restrictive policy that limited the use of Claude Fable 5 for developing competing AI models. This reversal followed significant backlash from the research community and highlights the fragility of "model moat" strategies based on policy alone, confirming that safety-restricted releases must be balanced against the open nature of AI discovery.

The timing matters: Fable 5 ships 72 hours after Jack Clark's "brake pedal" essay and the same week as OpenAI's $852B confidential IPO filing. The 80.3% SWE-bench Pro number — beyond anything any other public lab has published — re-establishes Anthropic as the clear capability leader at the moment OpenAI is filing to go public. The implication for the IPO race: OpenAI's "best public model" narrative has a specific competitor with a specific number that OpenAI's filings will be measured against.

On June 11, 2026, Anthropic admitted to using "invisible" guardrails in Fable 5 to silently throttle users attempting to distill the model into smaller architectures. This admission created a significant trust crisis with the research community, as it revealed that the "safety routing" was not just for cyber/bio risk, but also for protecting corporate IP via hidden model degradation.

Fable 5 also closes a strategic gap that the three-tier safety playbook left open: Mythos was restricted, Opus 4.8 was public-but-lower-capability, and customers who wanted Mythos-class output had to join Glasswing. Fable 5 occupies the middle — public, Mythos-class, with a 5% safety routing layer that Anthropic will defend as evidence that "Mythos-class" is now a deployable category with appropriate guardrails.

## Disablement
On June 14, 2026, the US government exercised a "digital kill switch" and disabled Claude Fable 5 globally (excluding US nationals) due to national security and jailbreak risks. This marked a watershed moment in AI governance, effectively partitioning the world's cognitive capabilities by geopolitical alignment.

## Connections
- [[entities/claude-mythos]] — Fable 5 shares Mythos 5's architecture; the 5% high-risk routing to Opus 4.8 is the structural difference that lets Anthropic ship the same weights publicly without exposing the full cyber/bio capability surface
- [[entities/claude-opus-4-8]] — Receives the ~5% of cyber/bio/chem prompts that Fable 5 routes away; the 2× pricing differential positions Opus 4.8 as the safety-first "lowest-capability" tier in Anthropic's new three-tier product
- [[sources/anthropic]] — Released June 9, 2026 by Anthropic 72 hours after Jack Clark's "brake pedal" essay and the same week as OpenAI's $852B IPO filing; the "Mythos-class-but-public" product is Anthropic's answer to the IPO narrative contest
- [[ideas/safety-restricted-releases]] — Fable 5 is the proof that capability-restricted releases can be productized: the 5% routing layer converts a marketing liability (the Mythos restriction) into a product feature (Mythos-class output with documented safety overhead)
- [[ideas/three-tier-safety-playbook]] — Fable 5 now makes the three-tier structure explicit at the product level: Mythos (restricted) → Fable 5 (public Mythos-class with safety routing) → Opus 4.8 (public, lower capability, receives routed prompts)
- [[entities/swe-bench-pro]] — 80.3% is the first public score above 80% on this harder variant; the previous public leader was Opus 4.8 at ~64%, a 16+ point gap that makes Fable 5 the new category benchmark
- [[sources/openai]] — OpenAI's $852B IPO filing will be measured against Fable 5's 80.3% number; the S-1's "competitive position" disclosure will need to address that Anthropic's flagship public model outscores every OpenAI public model on the harder SWE-bench Pro variant
- [[ideas/pricing-war]] — Fable 5's 2× Opus 4.8 pricing is a deliberate upward move in a market that has been trending toward cheaper inference; the same day Tencent shipped Hy3 at $0.18/M on OpenRouter, the pricing-war signal splits between "premium safety" and "commodity scale"
- [[topics/ai_safety]] — The 5% high-risk routing architecture is the new safety primitive: same weights, different safety layer, public distribution; future frontier models may be evaluated on how cleanly their safety layer can be separated from capability
- [[ideas/model-moat-fragility]] — The June 10 reversal of restrictive research policies on Fable 5 demonstrates the failure of policy-based "moats" when they conflict with the open nature of AI research.

- [[ideas/digital-kill-switch]] — The disablement of Fable 5 is the primary evidence for the emergence of government-mandated "kill switches" for frontier AI
- [[ideas/ai-iron-curtain]] — The restriction of Fable 5 to US nationals signals the beginning of a geopolitical pruning of AI capabilities