---
title: "SWE-bench Verified"
slug: swe-bench-verified
type: benchmark
last_updated: 2026-05-30
---

# SWE-bench Verified

## What It Is
SWE-bench Verified is an upgraded version of SWE-bench, a benchmark designed to evaluate AI models on real-world software engineering problems extracted from GitHub repositories. The "Verified" version addresses data contamination issues present in the original benchmark by using new, unseen problems.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Publisher | Princeton University / Scale AI |
| Release Date | April 2025 (Verified version) |
| Tasks | 500+ real-world GitHub issues with PRs |
| Evaluation | Whether the model can produce a correct patch |

## Benchmark Rankings (May 2026)

| Model | Score | Notes |
|-------|-------|-------|
| Claude Mythos Preview | 93.9% | Current leader |
| Claude Opus 4.8 | 88.6% | Anthropic's previous best |
| GPT-5.4 High | 85.0% | OpenAI's coding model |
| Claude Opus 4.7 Adaptive | 64.3% | On harder Pro variant |

## Significance
SWE-bench Verified has become the primary benchmark for evaluating AI coding agents and LLM software engineering capabilities. The 5.3 percentage point gap between Claude Mythos Preview (93.9%) and Opus 4.8 (88.6%) represents roughly 1 in 20 solved problems — a substantial lead suggesting Mythos has a fundamentally different architecture optimized for agentic code execution.

The benchmark is notable for testing end-to-end capability: given a GitHub issue description, can the model understand the problem, locate relevant code, and generate a correct patch that passes tests?

## Connections
- [[entities/claude-mythos]] — Mythos Preview achieved 93.9% on this benchmark, the highest score ever recorded
- [[entities/claude-opus-4-8]] — Achieved 88.6%, previously the Anthropic best before Mythos
- [[sources/anthropic]] — Developed the models dominating this benchmark
- [[sources/openai]] — GPT-5.4 High scored 85.0%
