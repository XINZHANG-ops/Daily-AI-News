# Wiki Build Log

This file tracks wiki maintenance operations over time.

## Format

Each entry should follow this pattern:

```
## [YYYY-MM-DD HH:MM] operation | Description
Brief summary of what was done
```

---

## [2026-04-14 00:00] init | Wiki initialized

Initial wiki structure created with:
- index.md - Main navigation
- WIKI.md - Project schema
- processed.json - Empty tracking file

Ready for first ingest.

## [2026-04-14 01:00] ingest | 28 dates processed (2026-03-17 to 2026-04-13)

### Topics Created
- [[topics/llm_models]] - Comprehensive LLM model tracking with benchmark comparisons
- [[topics/ai_companies]] - Company strategies, valuations, and competitive dynamics
- [[topics/ai_funding]] - Record Q1 2026 funding ($267B total, $242B into AI)
- [[topics/github_trends]] - Analysis of trending repositories

### Sources Created
- [[sources/openai]] - OpenAI timeline (GPT-5.4, $122B funding, Codex, IPO prep)
- [[sources/anthropic]] - Anthropic timeline (Claude Mythos, Project Glasswing, $30B ARR)
- [[sources/google]] - Google AI (Gemma 4, Gemini 3.1 Flash Live, Texas data center)
- [[sources/meta]] - Meta AI (Muse Spark closed-source, Llama 4 Scout/Maverick)

### Timelines Created
- [[timelines/2026-03]] - March 2026 events (GTC, Claude Mythos leak, Sora shutdown)
- [[timelines/2026-04]] - April 2026 events (Project Glasswing, funding records)

### Key Insights Synthesized
1. **Claude Mythos**: First frontier model withheld from public release due to capability concerns
2. **Agentic AI mainstream**: Claude Code drove Anthropic's ARR from $9B to $30B
3. **Coding agent wars**: OpenAI Codex 3M users, Google Gemini CLI released
4. **Infrastructure race**: Anthropic-Google-Broadcom multi-gigawatt TPU deal
5. **China-US tensions**: Frontier Model Forum coalition against model distillation

### Files Updated
- wiki/index.md - Updated with new structure and statistics
- wiki/log.md - Added ingest entry
- wiki/processed.json - Tracking all 28 dates

### Data Volume
- 28 JSON files processed
- 84+ GitHub repositories analyzed
- 200+ AI news articles synthesized
- 28 insight analyses documented

---
_End of log_

## [2026-04-14 03:00] ingest | 2026-04-14 processed

### Key News Events
- **Claude Mythos controversy**: The Guardian reports Anthropic withheld model citing danger; US Treasury Secretary Scott Bessent summoned bank heads; critics (Gary Marcus) accused Anthropic of exaggeration; UK AI Security Institute confirmed Mythos outperformed other systems in cybersecurity
- **AI passes peer review**: AI system successfully passed scientific peer review (Forbes); UC Berkeley's Carl Boettiger criticized AI Scientist project for focusing on replication vs meaningful research
- **DeepSeek V4 anticipation**: Growing anticipation for upcoming release from Chinese lab known for competitive open-weight models
- **Stanford benchmark crisis**: Benchmarks failing to keep pace with model capabilities — popular math benchmark has 42% error rate
- **Human scientists still outperform AI**: Nature report confirms humans still outperform best AI agents on complex research tasks
- **Anthropic infrastructure strain**: Expanded Google/Broadcom compute partnership; introduced usage caps on Claude subscriptions

### GitHub Trending (April 14)
- **yizhiyanhua-ai/fireworks-tech-graph** (2.2k stars): Claude Code skill for production-quality SVG+PNG technical diagrams (8 types, 5 styles)
- **AgriciDaniel/claude-obsidian** (1.1k stars): Claude + Obsidian knowledge companion using LLM Wiki pattern
- **hexiecs/talk-normal** (775 stars): System prompt removing AI slop for natural LLM responses

### Wiki Updates
- [[sources/anthropic]] - Added infrastructure strain note, source code leak entry
- [[topics/llm_models]] - Added DeepSeek V4, MiniMax MMX-CLI; added Benchmark Ceiling Crisis section
- [[topics/ai_companies]] - Updated Anthropic section with infrastructure strain
- [[topics/github_trends]] - Added fireworks-tech-graph, claude-obsidian, talk-normal
- [[timelines/2026-04]] - Added April 14 entries (8 events)
- [[index]] - Updated stats (29 days, 87+ repos, 214+ articles, 29 insights)
- Key Events in index.md - Added benchmark crisis and human vs AI scientists events

### Synthesized Insight
The week reveals an AI industry at an inflection point: Anthropic's dramatic reveal of Claude Mythos — claiming it's too dangerous to release while fighting for Pentagon contracts — shows the growing tension between "safety" as genuine principle versus marketing strategy. Meanwhile, the open-source ecosystem continues to democratize AI capabilities: fireworks-tech-graph brings professional diagram generation to Claude Code, while tools like claude-obsidian and talk-normal show the community's focus on making AI interactions more natural and personal. The benchmark crisis highlights that traditional metrics are losing relevance as model capabilities accelerate beyond measurement. For practitioners: the skills ecosystem (agents, tools, memory) is maturing rapidly, making AI agents increasingly autonomous — the question is no longer capability but trustworthiness and cost efficiency.

## [2026-04-14 02:00] lint | Health check

### Issues Found & Fixed
1. **Broken link** (`sources/anthropic.md`): Removed dangling `[[topics/ai_security]]` reference (page doesn't exist)
2. **Missing cross-ref** (`sources/meta.md`): Added `[[topics/ai_funding]]` link for $14B+ investment context
3. **Naming clarification** (`sources/anthropic.md`): Clarified "Claude Mythos" (leaked) vs "Claude Mythos Preview" (restricted release)

### Wiki Health Summary
- All 12 wiki pages verified
- No orphan pages detected (all pages have inbound links from index.md or other pages)
- No broken `[[reference]]` links (after fixes above)
- Cross-reference coverage: Good
- Metadata consistency: Statistics in index.md align with source content
- No stale content detected (all pages marked 2026-04-14)