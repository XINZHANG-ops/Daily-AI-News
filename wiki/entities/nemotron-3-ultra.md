---
title: "Nemotron 3 Ultra"
slug: nemotron-3-ultra
type: model
last_updated: 2026-06-07
---

# Nemotron 3 Ultra

## What It Is
Nemotron 3 Ultra is NVIDIA's 550B-parameter Mixture-of-Experts model (55B active) released June 4, 2026, using a hybrid Mamba-Transformer architecture and the new NVFP4 quantization format. The model claims 5x throughput gains on Blackwell-generation tensor cores and ships with a license shift from restrictive to OpenMDW-1.1 — a deliberate move to weaponize open weights against closed frontier model competitors.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | NVIDIA |
| Release Date | 2026-06-04 |
| Parameters | 550B total / 55B active (MoE) |
| Architecture | Hybrid Mamba-Transformer |
| Quantization | NVFP4 (4-bit) |
| Throughput | 5x vs prior generation on Blackwell |
| License | OpenMDW-1.1 (shifted from restrictive) |
| Companion Models | Nemotron 3.5 Content Safety (4B), Nemotron 3.5 ASR (40+ languages) |

## Significance
Nemotron 3 Ultra is NVIDIA's quietest but most consequential release of the year — it kicks the 4-bit inference wars into prime time. NVFP4 is not just a quantization scheme; it's a hardware-software lock-in play: tying the model to Blackwell-generation tensor cores ensures that running Nemotron at 5x throughput requires NVIDIA's own silicon, while the weights are given away for free on Hugging Face. The hybrid Mamba-Transformer design is the architectural bet the rest of the field is hedging on — it cuts KV cache cost on long-context agent workloads, which is the exact use case MAI-Thinking-1 and Claude Opus 4.8 (Effort Control) are also chasing. The OpenMDW-1.1 license shift is the most underrated part: NVIDIA is acknowledging that closed-source frontier models are a losing game against open Chinese releases like Qwen3.5 and DeepSeek V4, so it's weaponizing openness as a CUDA moat.

## Connections
- [[sources/nvidia]] — NVIDIA-developed; flagship open-weight model from the chip vendor now competing directly with model companies
- [[entities/maia-200]] — Both custom-silicon co-design stories (Microsoft's Maia 200 vs NVIDIA's Blackwell); represent the new vertical-integration paradigm in AI infrastructure
- [[entities/gb300]] — GB300 Blackwell Ultra is the silicon foundation; Nemotron 3 Ultra is the model that runs natively on it
- [[entities/blackwell-architecture]] — NVFP4 is bound to Blackwell tensor cores; architecture-locked quantization as lock-in
- [[topics/llm_models]] — Part of the May-June 2026 model release surge (Nemotron, MAI family, Grok Build, Opus 4.8)
- [[ideas/open-platform-ai]] — OpenMDW-1.1 license shift confirms the open-weights strategy is becoming mainstream
- [[sources/deepseek]] — Direct competitor at the open-weight frontier; NVIDIA's open-weights play is a direct response to Qwen/DeepSeek dominance
- [[ideas/nvidia-competitive-moat-eroding]] — Nemotron 3 Ultra is NVIDIA's defense: if you can't win on model performance alone, weaponize the model-as-CUDA-distribution play
- [[topics/agentic_ai]] — Hybrid architecture specifically targets long-horizon agent workloads with reduced KV cache cost
