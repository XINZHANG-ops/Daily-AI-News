---
title: "LongMemEval"
slug: longmemeval
type: benchmark
last_updated: 2026-06-10
---

# LongMemEval

## What It Is
LongMemEval is a benchmark for evaluating long-term memory capabilities of AI agents. Mempalace's June 9, 2026 result of 96.6% R@5 — achieved without an LLM in the retrieval loop — is the highest score in the agent memory category in 2026 and validates the thesis that the agent memory layer does not need LLM-mediated retrieval to achieve frontier-tier performance.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Category | Agent memory evaluation |
| Use Case | Long-term conversation / context retrieval |
| Top Score (June 9, 2026) | 96.6% R@5 (Mempalace) |
| Notable Earlier Leader | SupermemoryAI (LLM-mediated retrieval) |

## Significance
LongMemEval's importance comes from Mempalace's specific result: achieving 96.6% R@5 without an LLM in the retrieval loop means the agent memory category is not LLM-bound. Earlier 2026 leaders (SupermemoryAI at #1 on LongMemEval, LoCoMo, ConvoMem) used LLM-mediated retrieval, which adds both latency and cost to every memory lookup. Mempalace's semantic-search-only approach proves the cost and latency of LLM-mediated retrieval is unnecessary at the frontier.

The benchmark now serves as the test case for "can you solve agent memory without burning LLM tokens on retrieval?" — and the answer is yes, at 96.6% R@5. This is the second 2026 data point (after TileRT's 1000 TPS on commodity 8-GPU) that the agent infrastructure layer is being commoditized below the model.

## Connections
- [[entities/mempalace]] — June 9: 96.6% R@5 on LongMemEval without LLM in retrieval loop; the highest score in 2026
- [[entities/longmemeval]] — Earlier 2026 leader on LongMemEval, LoCoMo, ConvoMem; uses LLM-mediated retrieval
- [[topics/agentic_ai]] — Mempalace's 96.6% R@5 is the canonical data point for "agent infrastructure layer being commoditized below the model"
- [[ideas/commodity-inference-fragmentation]] — Mempalace's no-LLM-in-loop result is the memory-layer data point in the broader inference-cost fragmentation
