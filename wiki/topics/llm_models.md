# LLM Models

A comprehensive overview of large language model releases, updates, and capabilities from major AI labs.

## Overview

The period from March to April 2026 marks a significant inflection point in the LLM landscape. Key themes include:
- **Frontier models crossing capability thresholds** that raise security concerns (Claude Mythos)
- **Multi-modal and agentic capabilities** becoming standard
- **Cost efficiency improvements** enabling broader access
- **Active model launches** across US and Chinese labs

## Major Model Releases

### Claude Family (Anthropic)

| Model | Release Date | Key Features |
|-------|-------------|--------------|
| Claude Opus 4.6 | March 2026 | 1M token context window GA, agentic coding |
| Claude Sonnet 4.6 | March 2026 | 1M token context window GA, standard pricing |
| Claude Mythos | March 2026 (leaked) | 10T parameters, cybersecurity focus, NOT publicly released |
| Claude Mythos Preview | April 2026 | Restricted release via Project Glasswing |

**Key Development**: Claude Mythos was described internally as posing "unprecedented cybersecurity risks" due to its ability to discover unknown vulnerabilities in production codebases. This led to the unprecedented decision to withhold the model from public release and instead launch [[sources/anthropic#project-glasswing|Project Glasswing]].

### GPT Family (OpenAI)

| Model | Release Date | Key Features |
|-------|-------------|--------------|
| GPT-5.4 | April 2026 | 75.0% on OSWorld-Verified (human-level OS tasks), 27.7pp gain over GPT-5.2 |
| GPT-5.4 "Thinking" | March 2026 | GPT-6-level reasoning in smaller, faster architecture |
| GPT-5.4 Mini/Nano | March 17, 2026 | Affordable high-performance, near-top-tier at accessible cost |
| "Spud" | April 2026 (completed) | Next flagship model, expected to "accelerate the economy" |

**Key Development**: OpenAI completed pretraining of "Spud" which will support the productivity super-app strategy combining ChatGPT, Codex, and Atlas browser.

### Gemini Family (Google)

| Model | Release Date | Key Features |
|-------|-------------|--------------|
| Gemini 3.1 Flash Live | March 26, 2026 | Real-time multimodal voice, sub-300ms latency, 200+ countries |
| Gemini 3.1 Pro | Ongoing | $2/M tokens, frontier-level performance |
| Gemini 3 Deep Think | March 28, 2026 | For Ultra subscribers, harder technical use cases |
| Gemma 4 | April 2, 2026 | Apache 2.0, four sizes (2B-31B), #3 on Arena AI open leaderboard |

**Key Development**: Gemma 4's 31B model ranks #3 globally on Arena AI, while the 26B MoE ranks #6, outperforming models 20x their size.

### Other Notable Models

| Model | Organization | Release Date | Key Features |
|-------|-------------|--------------|--------------|
| Muse Spark | Meta | April 8, 2026 | Closed source, #4 on benchmarks (52 score), figure understanding 86.4% |
| MiMo-V2-Pro | Xiaomi | March 21, 2026 | 1T parameters, 42B active, #3 on agent benchmarks globally |
| Qwen3.6-Plus | Alibaba | April 2, 2026 | 1M context, agentic coding competitive with Claude Opus 4.5 |
| Llama 4 Scout/Maverick | Meta | April 5, 2026 | 10M token context (Scout), 400B+ parameters (Maverick), open-weight |
| Grok 4.20 | xAI | Ongoing | 78% non-hallucination rate |

## Capability Benchmarks

### OSWorld-Verified (Computer Use)
- **GPT-5.4 Thinking**: 75.0% (27.7pp gain over GPT-5.2)
- Claude Opus 4.6 remains strong in coding benchmarks

### SWE-bench Verified
- **Claude Mythos Preview**: 93.9%
- **Qwen3.6-Plus**: Competitive with Claude Opus 4.5
- **Cursor + Kimi K2.5**: 73.7% at $0.50/1M tokens

### ARC-AGI-3
- All frontier models scored under 1%
- Best score: Gemini 3.1 Pro at 0.37%
- Grok 4.2: 0%

### Arena AI Open Leaderboard
1. Gemini 3.1 Pro Preview
2. GPT-5.4
3. **Gemma 4 31B** (new)
4. Claude Opus 4.6
5. Claude Sonnet 4.6
6. **Gemma 4 26B MoE** (new)

## Key Trends

### 1. Safety-Restricted Releases
The Claude Mythos situation represents the first time a major AI lab has deliberately withheld a frontier model due to capability concerns rather than misuse risk. This sets a precedent for future extremely capable models.

### 2. Agentic Focus
Models are increasingly designed for autonomous task execution:
- GPT-5.4 achieves human-level OS navigation
- Qwen3.6-Plus built specifically for agentic coding
- Claude Mythos designed for cybersecurity operations

### 3. Cost Competition
Price wars are enabling accessibility:
- Gemini 3.1 Pro: $2/M tokens
- MiMo-V2-Pro: 67% cheaper than Claude Sonnet 4.6 for agentic tasks
- GPT-5.4 Mini/Nano: Affordable entry points

### 4. Context Window Race
- Claude: 1M tokens (GA)
- Qwen3.6-Plus: 1M tokens
- Llama 4 Scout: **10M tokens**
- Gemini CLI: 1M tokens

## Model Intelligence Index (Artificial Analysis v4.0)
1. GPT-5.4: 57
2. Claude Opus 4.6: 53
3. Muse Spark: 52
4. Gemini 3.1 Pro Preview: ~52

## Related Pages
- [[topics/ai_companies]] - Company strategies around model development
- [[topics/ai_funding]] - Investment in frontier model development
- [[sources/anthropic]] - Anthropic timeline
- [[sources/openai]] - OpenAI timeline
- [[sources/google]] - Google AI developments

---
*Last updated: 2026-04-14*