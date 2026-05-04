---
title: "ARC-AGI-3"
slug: arc-agi-3
type: benchmark
last_updated: 2026-05-03
---

# ARC-AGI-3

## What It Is
ARC-AGI-3 is an interactive reasoning benchmark from the ARC Prize Foundation designed to test genuine reasoning capabilities rather than pattern matching. Unlike static benchmarks, it requires models to interactively explore and understand novel environments, form coherent world models, and solve problems humans find intuitive.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Release Date | 2026-05-02 |
| Creator | ARC Prize Foundation |
| GPT-5.5 Score | 0.43% |
| Claude Opus 4.7 Score | 0.18% |
| Human Performance | Near 100% |
| Evaluations | 160 replays |

## Significance
ARC-AGI-3 exposes the fundamental gap between benchmark saturation and genuine reasoning. Claude Opus 4.7 scored 87.6% on SWE-bench — a benchmark measuring real-world coding — yet scored 0.18% on puzzles children can solve. The ARC Prize Foundation identified three systematic failure modes: models fail to form coherent world models, incorrectly map unfamiliar environments to known games (hallucinating Tetris/Breakout from 2D grids), and carry false theories forward even after "successful" solutions. This reveals that frontier models route unfamiliar situations to the nearest memorized template rather than constructing situation-specific models — a finding with profound implications for the LLM scaling paradigm.

## Connections
- [[entities/claude-opus-4-7]] — Scored 0.18% on ARC-AGI-3 despite 87.6% on SWE-bench; the stark contrast exposes the gap between code pattern-matching and genuine reasoning
- [[entities/gpt-5.5]] — Scored 0.43% on ARC-AGI-3; marginally better than Opus 4.7 but still below 1% — no frontier model demonstrates reasoning on this benchmark
- [[ideas/rl-vs-llm-paradigm]] — ARC-AGI-3 results are the strongest empirical evidence for David Silver's thesis that LLMs are "fossil fuel" — pattern-matching existing knowledge rather than discovering new insights; his RL-native startup raised $1.1B the same week
- [[topics/llm_models]] — The benchmark saturation problem ARC-AGI-3 reveals is becoming the central challenge for the LLM scaling paradigm
- [[entities/terminal-bench-2]] — GPT-5.5 scored 82.7% on Terminal-Bench 2.0 vs 0.43% on ARC-AGI-3; the benchmarks measuring different capabilities yield results differing by 190x
