---
title: "SWE-bench Pro"
slug: swe-bench-pro
type: benchmark
last_updated: 2026-06-10
---

# SWE-bench Pro

## What It Is
SWE-bench Pro is a harder variant of SWE-bench Verified designed to evaluate AI models on more complex, multi-file, multi-repo software engineering tasks. On June 9, 2026, Anthropic's Claude Fable 5 became the first public model to cross 80% on SWE-bench Pro with a score of 80.3% — a 16+ point gap over Claude Opus 4.8's ~64% (estimated). The result is the highest public SWE-bench Pro score disclosed in 2026 and re-establishes Anthropic as the clear capability leader at the moment OpenAI is filing for IPO.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Type | Harder variant of SWE-bench Verified |
| Top Score (June 9, 2026) | 80.3% (Claude Fable 5, first public model above 80%) |
| Previous Public Leader | Claude Opus 4.8 at ~64% (estimated) |
| Reference: Mythos Preview | 77.8% (restricted model) |

## Significance
SWE-bench Pro was designed to be the harder agentic-coding benchmark — the one where single-file PR resolution is no longer sufficient, and the model has to navigate complex dependency graphs across multiple repos. Fable 5's 80.3% is the first public score above 80% and represents the operational definition of "agentic coding at frontier tier": the model can autonomously resolve multi-file, multi-repo tasks that previously required human coordination across teams.

The 16+ point gap between Fable 5 and Opus 4.8 is also a pricing signal: the $10/M input price (2× Opus 4.8) is the rate-card translation of the capability gap. For workloads where multi-file multi-repo resolution is the bottleneck, the 2× premium is the cost of crossing the 80% threshold.

The Mythos Preview's 77.8% (restricted model) being below Fable 5's 80.3% (public model) is notable: Fable 5 is the first public model to outscore the restricted Mythos Preview on a harder agentic-coding benchmark. The safety-routing layer that makes Fable 5 deployable has not hurt SWE-bench Pro performance compared to the unrestricted restricted model.

## Connections
- [[entities/claude-fable-5]] — June 9: 80.3% on SWE-bench Pro, first public model above 80%; the 16+ point gap over Opus 4.8 is the operational definition of frontier agentic coding
- [[entities/swe-bench-verified]] — SWE-bench Pro is the harder variant; Fable 5's 80.3% on Pro mirrors its ~92% on Verified (between Opus 4.8 at 88.6% and Mythos at 93.9%)
- [[entities/claude-mythos]] — Mythos Preview scored 77.8% on SWE-bench Pro vs Fable 5's 80.3% — the first public model to outscore the restricted Mythos Preview on a harder agentic-coding benchmark
- [[entities/claude-opus-4-8]] — Estimated ~64% on SWE-bench Pro (vs Fable 5's 80.3%); the 16+ point gap is the rate-card translation
- [[sources/anthropic]] — Fable 5's 80.3% is the first public score above 80% on SWE-bench Pro; re-establishes Anthropic as the capability leader 3 weeks before OpenAI's IPO filing
- [[sources/openai]] — OpenAI's $852B IPO filing will need to disclose a "competitive position" section; Fable 5's 80.3% on SWE-bench Pro is the specific number OpenAI's GPT-5.5-Codex will be measured against
