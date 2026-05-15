---
title: "Terminal-Bench 2.0"
slug: terminal-bench-2
type: benchmark
last_updated: 2026-05-15
---

# Terminal-Bench 2.0

## What It Is
A benchmark for evaluating AI model performance on terminal/command-line tasks, measuring practical system administration and DevOps capabilities. GPT-5.5 scored 82.7% vs Claude Opus 4.7's 58.6%, making it a key differentiator in the enterprise coding race. Along with SWE-bench, it has become one of the primary benchmarks for comparing frontier coding models.

## Key Facts

| Attribute | Value |
|-----------|-------|
| GPT-5.5 Score | 82.7% |
| Claude Opus 4.6 Score | ~69% (raw, May 12 unsaturated benchmark) |
| Claude Opus 4.7 Score | 58.6% |
| With-Agent Score | ~82% (May 12) |
| Failure Rate | 18-35% of CLI tasks still fail even with frontier models |
| Gap | 24.1 percentage points |
| Domain | Terminal/CLI tasks, system administration |

## Significance
The 24-point gap between GPT-5.5 and Claude Opus 4.7 on Terminal-Bench 2.0 reveals a hidden dimension of model competition: while SWE-bench focuses on code generation, Terminal-Bench measures practical system interaction. GPT-5.5's dominance here suggests OpenAI has prioritized operational AI capabilities — models that can actually administer systems, not just write code for them.

On May 12, 2026, unsaturated benchmark scores revealed that even frontier models leave an 18-35% CLI task failure rate. GPT-5.5 scored ~73% raw and ~82% with agents; Claude Opus 4.6 scored ~69% raw. This ~37% gap between lab benchmarks and deployment reality (the difference between ~82% with agents and ~73% raw, plus the remaining failure rate) is the empirical driver behind the agent infrastructure investment wave. Models alone won't close the deployment gap — agents need better tooling, not just better models.

## Connections
- [[topics/llm_models]] — Terminal Bench 2 and SWE-bench now jointly define the coding-model competition frontier: SWE-bench measures software engineering depth while Terminal Bench 2 measures command-line automation breadth — together they capture the full spectrum of developer-facing model capability
- [[sources/openai]] — Terminal-Bench gap supports OpenAI's "super app" positioning of GPT-5.5; May 12 unsaturated scores show even GPT-5.5 leaves ~18% of CLI tasks unsolved without agent tooling
- [[ideas/agent-infrastructure-layer]] — The 18-35% CLI failure rate is the empirical evidence that drives infrastructure investment; Mirage, OpenSquilla, and HiDream represent convergent evolution to solve this deployment gap
- [[entities/gpt-5.5]] — Scored ~73% raw and ~82% with agents on May 12 unsaturated Terminal-Bench 2.0, confirming the ~37% deployment-reality gap
- [[entities/claude-opus-4-7]] — Scored 58.6% on Terminal-Bench 2.0; Claude Opus 4.6 raw score ~69% on May 12 unsaturated benchmark shows the gap is not static
