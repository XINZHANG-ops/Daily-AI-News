---
title: "ProgramBench"
slug: program-bench
type: benchmark
last_updated: 2026-05-23
---

# ProgramBench

## What It Is
ProgramBench is a benchmark from Meta AI Research that tests whether language models can rebuild programs from scratch — specifically, whether AI agents can architect and implement complete codebases from compiled binaries and documentation alone.

## Key Facts

| Attribute | Value |
|-----------|-------|
| Creator | Meta AI Research (facebookresearch) |
| Repository | github.com/facebookresearch/ProgramBench |
| Stars | 637 |
| Forks | 52 |
| Purpose | Test code reconstruction from binaries and docs |

## Significance
 ProgramBench addresses a fundamental question in AI capabilities: can models understand code well enough to reconstruct it from compiled artifacts? This benchmark tests reverse engineering capabilities that have significant implications for security (understanding malware), software archaeology (recovering lost source code), and AI's general understanding of computation. The benchmark was released as part of Meta's broader AI safety and capability evaluation initiative.

## Connections
- [[topics/github_trends]] — ProgramBench is a research benchmark from Meta, one of the major AI labs; 637 stars shows interest in code understanding and reverse engineering
- [[topics/llm_models]] — Tests the limits of LLM code understanding beyond simple code generation
- [[entities/claude-code]] — Claude Code's coding capabilities would be tested by this benchmark
- [[entities/codex]] — OpenAI's coding product would also be evaluated by this benchmark