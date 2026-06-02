---
title: "Claude Opus 4.8"
slug: claude-opus-4-8
type: model
last_updated: 2026-06-01
---

# Claude Opus 4.8

## What It Is
Claude Opus 4.8 is Anthropic's flagship model released May 29, 2026, just 42 days after Opus 4.7 — the shortest model release cadence in Anthropic's history. It achieves 88.6% on SWE-bench Verified, representing a modest improvement over Opus 4.7's 87.6%, while Claude Mythos Preview (restricted) reaches 93.9% on the same benchmark. The model introduces new Effort Controls (Low/Medium/High/Max) and Dynamic Workflows feature, competing on UX differentiation rather than raw capability gains.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Release Date | 2026-05-29 |
| Days After Opus 4.7 | 42 days (shortest in Anthropic history) |
| Creator | Anthropic |
| SWE-bench Verified | 88.6% |
| SWE-bench Pro | ~64% (estimated) |
| SWE-bench vs Mythos Preview | -5.3 points behind Mythos (93.9%) |
| Vision Resolution | 3.75 megapixels (inherited from 4.7) |
| Self-Verification | Inherited and enhanced from 4.7 |
| Context Window | 200K tokens |
| Effort Controls | Low/Medium/High/Max |
| Dynamic Workflows | New feature for customizable task execution |

## Significance
The 42-day cadence between Opus 4.7 and 4.8 signals Anthropic has entered an aggressive release cycle, possibly responding to OpenAI's o3 retirement and Google's Gemini Spark launch. The new Effort Controls and Dynamic Workflows feature suggest they're competing not just on benchmarks but on UX differentiation — trying to capture the professional developer market that values controllable output over raw capability.

The modest jump from 87.6% to 88.6% suggests diminishing returns on the current architecture. Meanwhile, Mythos Preview at 77.8% on SWE-bench Pro (vs ~64% for Opus 4.7 Adaptive) indicates Mythos has fundamentally different architecture optimization for agentic code execution.

With Anthropic's $900B valuation now surpassing OpenAI's, Opus 4.8 serves as the "accessible" flagship while Mythos remains the "aspirational" product locked behind Project Glasswing. The aggressive release cadence positions Anthropic to maintain relevance against accelerated competition.

## Connections
- [[sources/anthropic]] — Released by Anthropic on May 29, 2026; part of the valuation surge to $900B; 42-day cadence is the shortest in company history
- [[entities/claude-mythos]] — Opus 4.8 trails Mythos Preview by 5.3 percentage points on SWE-bench Verified (88.6% vs 93.9%), highlighting the capability gap between released and restricted models
- [[entities/claude-opus-4-7]] — Direct predecessor with 87.6% SWE-bench released April 16-17; 42 days between releases is the new company record
- [[entities/claude-code]] — Powers Claude Code; the model developers use for coding assistance; Effort Controls target professional developers who want controllable output
- [[topics/llm_models]] — Latest in the Claude Opus family; aggressive cadence signals competitive response to OpenAI o3 retirement and Google Gemini Spark
- [[sources/openai]] — OpenAI's o3 retirement (August 2026) and GPT-4.5 retirement (June 2026) may be creating market space Anthropic is exploiting with accelerated releases
- [[ideas/safety-restricted-releases]] — The Opus 4.8 vs Mythos gap validates the strategy of releasing "good enough" while reserving "best" for enterprise
- [[ideas/agent-control-interface-wars]] — Effort Controls (Low/Medium/High/Max) represent Anthropic's answer to the control-vs-autonomy debate that Remy's approval-gate and OpenAI's autonomous Operator embody
