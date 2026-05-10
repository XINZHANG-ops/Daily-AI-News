---
title: "DR-Venus"
slug: dr-venus
type: model
last_updated: 2026-05-09
---

# DR-Venus

## What It Is
DR-Venus is a 4-billion-parameter deep research agent trained entirely on open data (10,000 samples). It establishes a new small-model frontier on deep research benchmarks like BrowseComp and GAIA, demonstrating that compact models can achieve research-grade performance when trained specifically for autonomous research workflows. Self-contained with minimal dependencies.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Parameters | 4B |
| Training Data | 10K open-data samples |
| Benchmarks | BrowseComp, GAIA |
| Stars | 1.8k |
| Forks | 247 |

## Significance
DR-Venus challenges the assumption that research agents require frontier-scale parameters. At 4B parameters — smaller than many smartphone models — it achieves competitive scores on research benchmarks through specialized training rather than scale. This is part of a broader pattern: GLM-OCR (0.9B parameters, 94.62 on OmniDocBench) and Qwen 3.6-35B-A3B (3B active params, 73.4% SWE-bench on RTX 4090) all demonstrate that narrow tasks can be dominated by small, efficient models.

The "deep research" category is particularly significant because it is the workflow that companies like Perplexity and Anthropic are vertically targeting. DR-Venus proves this doesn't require GPT-5.5-scale compute — a 4B model on open data can compete. The implication for democratization: research-grade AI becomes runnable on consumer hardware without API costs or cloud dependency.

## Connections
- [[ideas/efficiency-frontier]] — DR-Venus joins GLM-OCR and Qwen 3.6-35B-A3B as evidence that efficient models achieve domain dominance with dramatically less compute; the efficiency frontier is advancing faster than the scale frontier
- [[entities/autoresearch]] — Karpathy's 79.2K-star autonomous research agent and DR-Venus both target the same autonomous research workflow, but DR-Venus does it at 1/1000th the parameter count; together they define the spectrum from maximalist to minimalist research agents
- [[topics/llm_models]] — The small-model research trend (DR-Venus 4B, GLM-OCR 0.9B) is a direct response to the cost economics exposed by DeepSeek V4 and Anthropic's $200B cloud commitment; if 4B models can do research, the trillion-parameter arms race looks increasingly wasteful
- [[sources/perplexity]] — Perplexity Finance and DR-Venus both target research workflows, but Perplexity orchestrates existing data subscriptions while DR-Venus is a self-contained model; the convergence validates research as the highest-value agent vertical
- [[entities/dexter]] — Dexter (finance research) and DR-Venus (general deep research) are the open-source layer of the research-agent vertical; both prove that specialized models outperform general models on specific research tasks
- [[ideas/agent-verticalization]] — DR-Venus is the model-layer evidence for verticalization: a 4B research specialist outperforms general frontier models on research benchmarks because it was designed for one job, not all jobs
