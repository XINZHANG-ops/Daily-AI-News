---
title: "DiffusionGemma"
slug: diffusion-gemma
type: model
last_updated: 2026-06-11
---

# DiffusionGemma

## What It Is
DiffusionGemma is a text diffusion model developed by Google that enables ultra-fast text generation. Unlike standard autoregressive Transformers, it utilizes a diffusion-based approach combined with a mixture-of-experts (MoE) architecture to generate text.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Release Date | 2026-06-10 |
| Creator | Google |
| Performance | Up to 1,000 tokens/sec on H100s |
| Architecture | Text Diffusion + MoE |

## Significance
DiffusionGemma represents a significant architectural pivot. By moving away from the autoregressive bottleneck of the KV cache, Google is exploring a path to drastically reduce latency and compute costs for real-time streaming, potentially challenging the dominance of pure Transformer-based MoEs.

## Connections
- [[sources/google]] — Developed by Google as part of its effort to optimize inference speed and reduce the computational overhead of large-scale text generation.
- [[topics/llm_models]] — Introduces a diffusion paradigm to text generation, contrasting with the autoregressive nature of the GPT and Claude families.
- [[ideas/transformer-architecture-evolution]] — Serves as primary evidence that the industry is hitting a wall with KV-cache latency, forcing a move toward non-autoregressive architectures for speed.
