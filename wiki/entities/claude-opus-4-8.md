---
title: "Claude Opus 4.8"
slug: claude-opus-4-8
type: model
last_updated: 2026-05-29
---

# Claude Opus 4.8

## What It Is
Claude Opus 4.8 is Anthropic's latest flagship model released May 29, 2026. It achieves 88.6% on SWE-bench Verified, representing a modest improvement over Opus 4.7's 87.6%, while Claude Mythos Preview (restricted) reaches 93.9% on the same benchmark. The model builds on Opus 4.7's self-verification capability and cyber safeguards derived from Claude Mythos research.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Release Date | 2026-05-29 |
| Creator | Anthropic |
| SWE-bench Verified | 88.6% |
| SWE-bench Pro | ~64% (estimated) |
| SWE-bench vs Mythos Preview | -5.3 points behind Mythos (93.9%) |
| Vision Resolution | 3.75 megapixels (inherited from 4.7) |
| Self-Verification | Inherited and enhanced from 4.7 |
| Context Window | 200K tokens |

## Significance
Claude Opus 4.8 represents a minor incremental update over Opus 4.7, gaining only 1 percentage point on SWE-bench Verified. Meanwhile, the restricted Claude Mythos Preview achieves 93.9% — a 5.3 point gap that represents roughly 1 in 20 additional problems solved. This widening gap between the released flagship and the restricted preview highlights Anthropic's deliberate rationing strategy: maintaining a clear capability hierarchy that justifies enterprise premium pricing.

The modest jump from 87.6% to 88.6% suggests diminishing returns on the current architecture. Meanwhile, Mythos Preview at 77.8% on SWE-bench Pro (vs ~64% for Opus 4.7 Adaptive) indicates Mythos has fundamentally different architecture optimization for agentic code execution, not just incremental improvements.

With Anthropic's $965B valuation now surpassing OpenAI's $730B and $47B annualized revenue, Opus 4.8 serves as the "accessible" flagship while Mythos remains the "aspirational" product locked behind Project Glasswing.

## Connections
- [[sources/anthropic]] — Released by Anthropic on May 29, 2026; part of the valuation surge to $965B
- [[entities/claude-mythos]] — Opus 4.8 trails Mythos Preview by 5.3 percentage points on SWE-bench Verified (88.6% vs 93.9%), highlighting the capability gap between Anthropic's released and restricted models
- [[entities/claude-opus-4-7]] — Direct predecessor with 87.6% SWE-bench; Opus 4.8 is a modest incremental improvement
- [[entities/claude-code]] — Powers Claude Code; the model developers use for coding assistance
- [[topics/llm_models]] — Latest in the Claude Opus family
- [[sources/openai]] — OpenAI's GPT-5.4 High scores 85% on SWE-bench, putting Opus 4.8 ahead by 3.6 points
- [[ideas/safety-restricted-releases]] — The Opus 4.8 vs Mythos gap validates the strategy of releasing "good enough" while reserving "best" for enterprise