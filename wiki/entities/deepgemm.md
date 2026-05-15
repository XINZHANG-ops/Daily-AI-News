---
title: "DeepGEMM"
slug: deepgemm
type: framework
last_updated: 2026-05-04
---

# DeepGEMM

## What It Is
DeepGEMM is DeepSeek's clean and efficient FP8 (8-bit floating point) General Matrix Multiply (GEMM) kernels library with fine-grained scaling for modern LLMs. It provides a unified high-performance tensor core kernel library supporting FP8, FP4, BF16, fused MoE (Mixture of Experts), and Mega MoE with JIT (Just-In-Time) compilation.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | DeepSeek |
| GitHub | deepseek-ai/DeepGEMM |
| Stars | 6.9k |
| License | MIT |
| Technical Focus | FP8 GEMM kernels for LLM inference |

## Significance
DeepGEMM represents DeepSeek's contribution to efficient inference infrastructure. The library's support for FP8 (which reduces memory bandwidth by 50% compared to BF16) combined with MoE optimization makes it particularly relevant for inference workloads. Its JIT compilation approach allows it to adapt to specific hardware at runtime, potentially offering performance advantages over pre-compiled kernels.

The library's focus on FP8 aligns with industry trends toward lower-precision inference to reduce costs and improve throughput. With 6.9k stars, it represents significant community interest in efficient inference tooling.

## Connections
- [[sources/deepseek]] — DeepGEMM is DeepSeek's open-source GPU kernel library that delivers 135 TFLOPS on Hopper architecture, proving that Chinese labs now contribute foundational AI infrastructure software — not just models — to the global ecosystem
- [[topics/ai_funding]] — DeepSeek's ability to produce efficient open-source infrastructure reflects efficiency advantages
- [[entities/ising]] — Both represent efficient approaches to AI hardware/software
- [[topics/github_trends]] — 6.9k stars reflects developer interest in efficient inference tooling