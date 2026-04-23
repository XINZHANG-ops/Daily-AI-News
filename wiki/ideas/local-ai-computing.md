---
title: "Local AI Computing"
slug: local-ai-computing
last_updated: 2026-04-20
---

# Local AI Computing

## The Insight
The week of April 15-20, 2026 sees the emergence of device-resident, always-on AI assistants as a distinct category. Perplexity's "Computer" runs locally on Mac mini, managing files, controlling native apps, and browsing autonomously. This represents a shift from cloud-based AI to local AI computing — with implications for privacy, latency, and the AI business model.

## Evidence
- [[entities/perplexity-computer]] — Always-on local AI on Mac mini, $200/month, controls iMessage/Calendar
- [[topics/llm_models]] — Qwen 3.6-35B-A3B with 3B active params runs on consumer hardware
- [[entities/thunderbolt]] — Mozilla's enterprise self-hosted AI client enables local deployment

## Implications
Local AI computing has several advantages:
1. Privacy: Data never leaves the device
2. Latency: No network round-trips
3. Offline capability: Works without internet
4. Cost: No per-token API charges

This trend could challenge the cloud AI business model if enough computation can run locally. The combination of efficient models (Qwen 3.6 with 3B params) and local inference frameworks (MLX, llama.cpp) makes local AI increasingly viable.

## Connections
- [[entities/perplexity-computer]] — Pioneering always-on local AI
- [[entities/thunderbolt]] — Enterprise self-hosted alternative
- [[entities/qwen-3-6]] — Enables local deployment with 3B active params
- [[ideas/efficiency-frontier]] — Efficiency improvements enabling local AI