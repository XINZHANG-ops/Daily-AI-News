---
title: "SWE-bench"
slug: swe-bench
type: benchmark
last_updated: 2026-05-30
---

# SWE-bench

## What It Is
SWE-bench is a benchmark designed to evaluate AI models on real-world software engineering problems. It contains problems extracted from GitHub repositories, requiring models to understand issue descriptions, locate relevant code, and generate correct patches.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Publisher | Princeton University, Scale AI |
| Release Date | November 2023 |
| Tasks | ~500 real-world GitHub issues with accepted PRs |
| Evaluation | Whether the model produces a correct patch |

## Variants
- **SWE-bench Original**: The original benchmark with potential data contamination
- **SWE-bench Verified**: Updated version with new, unseen problems to prevent contamination
- **SWE-bench Pro**: Harder variant with more complex problems

## Connections
- [[entities/swe-bench-verified]] — The contamination-free version now used for evaluations
- [[topics/llm_models]] — Models are evaluated on this benchmark for coding capability
