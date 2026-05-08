---
title: "GLM-OCR"
slug: glm-ocr
type: repo
last_updated: 2026-05-08
---

# GLM-OCR

## What It Is
GLM-OCR is an accurate, fast, and comprehensive multimodal OCR built on the GLM-V encoder-decoder architecture. At only 0.9B parameters, it achieves 94.62 on OmniDocBench V1.5. It uses a two-stage pipeline: layout detection followed by parallel recognition. Deployable via vLLM, SGLang, and Ollama.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | zai-org |
| Stars | 6.3K |
| Forks | 580 |
| Parameters | 0.9B |
| OmniDocBench V1.5 | 94.62 |
| Architecture | GLM-V encoder-decoder |
| Deployment | vLLM, SGLang, Ollama |

## Significance
GLM-OCR demonstrates that sub-1B parameter models can achieve state-of-the-art results on specialized multimodal tasks. The 0.9B parameter count is two orders of magnitude smaller than frontier LLMs, yet it outperforms them on document understanding benchmarks. The two-stage pipeline (layout detection + parallel recognition) is an architectural insight that could inform how larger models handle document ingestion. Its deployment flexibility via vLLM, SGLang, and Ollama makes it immediately usable across the open-source inference ecosystem.

## Connections
- [[topics/llm_models]] — GLM-OCR validates the efficiency frontier: 0.9B parameters beating frontier models on document OCR proves that task-specific small models can outperform general-purpose giants on narrow domains
- [[topics/github_trends]] — Part of the May 6 repo batch alongside AutoResearch and Hive; signals continued diversification of the agent ecosystem beyond coding into document understanding and multimodal perception
- [[sources/google]] — GLM-V architecture shares lineage with Google's multimodal research; the encoder-decoder approach for OCR mirrors Google's own document-AI work
- [[ideas/efficiency-frontier]] — 0.9B parameters achieving 94.62 on OmniDocBench is another data point that efficient models can dominate narrow domains with dramatically less compute than frontier LLMs