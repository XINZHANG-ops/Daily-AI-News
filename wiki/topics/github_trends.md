# GitHub Trends

Analysis of trending AI/ML GitHub repositories from March-April 2026.

## Overview

This period saw explosive growth in AI agent frameworks, coding tools, and infrastructure projects. Key themes:
- **Agent frameworks** dominating GitHub trending
- **Claude Code ecosystem** driving massive clones/improvements
- **Browser automation** for AI agents
- **Memory systems** for long-context agentic workflows
- **Multi-agent orchestration** becoming standard

## Top Repositories by Stars

### Agent Frameworks & Harness

| Repository | Stars | Focus |
|------------|-------|-------|
| ultraworkers/claw-code | 181.9k+ | Clean-room Claude Code rewrite (Rust) |
| microsoft/agent-framework | 8.2k-9.3k | Multi-language (Python/.NET) agent framework |
| agentscope-ai/CoPaw | 14.9k+ | Cross-platform personal AI assistant |
| agentscope-ai/agentscope | Production-ready | Multi-agent, real-time voice |

### Browser & Web Automation

| Repository | Stars | Focus |
|------------|-------|-------|
| browser-use/browser-use | 51.2k | AI agent browser control |
| lightpanda-io/browser | 18.5k | Zig-built headless browser (11x faster, 16x less memory) |
| miemieyong/OpenCat | 3.2k | AI-native browser agent framework |

### Code & Developer Tools

| Repository | Stars | Focus |
|------------|-------|-------|
| obra/superpowers | 40.9k-92.1k | Agentic skills framework for Claude Code/Cursor/Codex |
| pydantic/pydantic-ai | 38.5k | Type-safe GenAI agent framework |
| yizhiyanhua-ai/fireworks-tech-graph | 2.2k | Claude Code skill for production-quality SVG+PNG technical diagrams (8 types, 5 styles, AI/Agent domain knowledge) |
| yechan-Heo/oh-my-codex | 12.9k | OpenAI Codex extensions with hooks, agent teams |
| graphify | 22.7k | Code → queryable knowledge graphs |

### Memory & Knowledge

| Repository | Stars | Focus |
|------------|-------|-------|
| supermemoryai/supermemory | 20.0k | #1 on LongMemEval, LoCoMo, ConvoMem |
| AgriciDaniel/claude-obsidian | 1.1k | Claude + Obsidian knowledge companion (LLM Wiki pattern with /wiki /save /autoresearch commands) |
| vectorize-io/hindsight | 2.8k | Agent memory system (biomimetic) |
| trusgraph-ai/trustgraph | 1.8k | Context development platform |

### LLM Interaction & Prompting

| Repository | Stars | Focus |
|------------|-------|-------|
| hexiecs/talk-normal | 775 | System prompt removing AI slop — makes any LLM respond naturally like a human |

### Communication & Platforms

| Repository | Stars | Focus |
|------------|-------|-------|
| AstrBotDevs/AstrBot | 40.2k | Multi-platform IM bot (QQ, WeChat, Telegram, Feishu) |
| nousresearch/hermes-agent | 19.4k-29.2k | Self-improving agent with learning loop |

### Autonomous Research

| Repository | Stars | Focus |
|------------|-------|-------|
| 666ghj/MiroFish | 28k | Swarm intelligence engine for prediction |
| autorsearch (karpathy) | 4.2k | AI agents running research autonomously |
| dexte | 20.3k | Autonomous financial research agent |
| AI-Scientist-v2 (SakanaAI) | 3k+ | Automated scientific discovery |

### Other Notable

| Repository | Stars | Focus |
|------------|-------|-------|
| microsoft/VibeVoice | 37.1k | Open-source frontier voice AI |
| google-gemini/gemini-cli | 8.7k | Terminal agent (1M context) |
| HKUDS/CLI-Anything | 25.4k | Bridge AI agents with existing CLI apps |
| microsoft/ai-agents-for-beginners | 12.8k | 12 lessons for building AI agents |
| github-mcp-server | 15.3k | GitHub official MCP server |

## Key Trends Analysis

### 1. Claude Code Leak → Ecosystem Explosion
The Claude Code source leak (512K lines TypeScript via npm) spawned rapid ecosystem development:
- **claw-code**: Clean-room Rust rewrite, 181.9k+ stars in days
- **oh-my-claudecode**: Teams-first multi-agent orchestration for Claude Code
- **learn-claude-code**: Learning resources

### 2. Agent Framework Consolidation
MCP (Model Context Protocol) became the dominant standard:
- 97M+ installs by March 2026
- Donated to Linux Foundation
- Adopted by Anthropic, OpenAI, Microsoft, Google

Frameworks now support MCP natively: CrewAI, AgentScope, lastmile-ai/mcp-agent

### 3. Multi-Agent Orchestration
Enterprise-grade frameworks emerged:
- Microsoft Agent Framework v1.0 (Python + .NET)
- Swarms (HeavySwarm with 5-phase workflow)
- AgentScope (production-ready with A2A support)

### 4. Voice-First AI
Growing focus on voice interfaces:
- Microsoft VibeVoice (37.1k stars)
- NVIDIA PersonaPlex-7B (speech-to-speech)
- AgentScope real-time voice

### 5. Physical AI & Robotics
- dimensionalOS/dimos: Agentic OS for physical space
- lightpanda-io/browser: Agent-optimized browser

### 6. Efficiency Innovations
- **PrismML Bonsai**: 1-bit 8B model, 40 tok/s on iPhone
- **flash-moe**: 397B MoE at 4.4 tok/s on MacBook Pro
- **daVinci-LLM**: 3B from scratch, beats OLMo-3-7B on math by 23.2%

## Patterns Observed

### Star Velocity Leaders
1. **claw-code**: 100K+ stars in hours (fastest in history)
2. **obra/superpowers**: 40.9k → 92.1k in days
3. **DeerFlow (ByteDance)**: #1 on GitHub Trending v2.0

### Agent Architectures
- **Harness layer**: Claude Code patterns being replicated
- **Memory layer**: Biomimetic and graph-based approaches
- **Orchestration**: Multi-agent teams, A2A protocols

## Cross-References
- [[topics/llm_models]] - Model releases driving tooling
- [[topics/ai_companies]] - Companies building agent ecosystems

---
*Last updated: 2026-04-14*