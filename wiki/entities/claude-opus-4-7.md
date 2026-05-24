---
title: "Claude Opus 4.7"
slug: claude-opus-4-7
type: model
last_updated: 2026-05-23
---

# Claude Opus 4.7

## What It Is
Claude Opus 4.7 is Anthropic's flagship model released April 16-17, 2026. It represents a significant leap in coding capability with 87.6% on SWE-bench Verified (+6.8pts over Opus 4.6), 64.3% on SWE-bench Pro, tripled vision resolution to 3.75 megapixels, and new cyber safeguards developed from the Claude Mythos safety work. The May 2026 update added self-verification capability — the model can reread code and mentally run tests before output, solving 4 tasks neither 4.6 nor Sonnet 4.6 could crack.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Release Date | 2026-04-16/17 |
| Creator | Anthropic |
| SWE-bench Verified | 87.6% (+6.8pts over 4.6) |
| SWE-bench Pro | 64.3% |
| Internal Coding Benchmarks | +13% over 4.6 |
| Vision Resolution | 3.75 megapixels (3x previous) |
| Cyber Safeguards | Developed from Claude Mythos safety research |
| Self-Verification | New capability: rereads code, mentally runs tests before output |
| CursorBench | 70% (vs 58% for Opus 4.6) |
| Rakuten-SWE-Bench | 3x more tasks resolved |
| Visual Acuity | 98.5% (vs 54.5% for 4.6) |
| Pricing | $5/$25 per million tokens (unchanged) |
| Tokenizer | New — causes 1.0-1.35x token drift for same inputs |

## Significance
Claude Opus 4.7 raises the bar for coding benchmarks, surpassing Opus 4.6 by nearly 7 percentage points on SWE-bench Verified. The cyber safeguards developed from Claude Mythos research represent a new approach to model safety — embedding security awareness directly into the model rather than external filtering.

The self-verification capability is the real differentiator — it solves 4 tasks that neither Opus 4.6 nor Sonnet 4.6 could crack. However, the new tokenizer causes 1.0-1.35x token drift for the same inputs, a hidden cost not mentioned in the announcement. Meanwhile, Claude Mythos Preview (93.9% SWE-bench) remains locked to just 50 organizations — Anthropic is deliberately rationing its best model to extract maximum enterprise value.

The model is available in Amazon Bedrock and Anthropic's API, with a major UK expansion announced including a new London office. By May 23, 2026, Claude Opus 4.7 became generally available on Amazon Bedrock with improved coding, visual understanding, and multi-step reasoning, plus zero operator data access — expanding Anthropic's distribution through AWS渠道.

## Connections
- [[sources/anthropic]] — Released by Anthropic, builds on Mythos safety research
- [[entities/claude-mythos]] — Opus 4.7's cyber safeguards directly inherit from Mythos safety research, showing that Anthropic channels its most restricted model's learnings into its most accessible flagship — a knowledge-transfer pipeline from classified research to consumer deployment
- [[entities/claude-security]] — Powers Claude Security; the same model that finds zero-days also drives the defensive scanner
- [[topics/llm_models]] — Latest in the Claude Opus family
- [[ideas/safety-restricted-releases]] — Continues the safety-aware release pattern