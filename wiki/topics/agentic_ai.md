---
title: "Agentic AI"
slug: agentic_ai
last_updated: 2026-05-01
---

# Agentic AI

## Overview
May 1, 2026 reveals the economics of agentic AI are approaching inflection point. NVIDIA GB300 Blackwell Ultra (35x lower cost/token) combined with Microsoft's E7 bundle at $99/user/month and Agent 365 at $15/user/month signal that the agentic era is no longer theoretical — it's priced and packaged for enterprise deployment. The question is shifting from "can agents code?" to "who controls the agent governance stack?"

## Evolution

**Coding Agent Wars**: Anthropic's Claude Code went viral in late 2025, driving Anthropic's ARR from $9B to $30B. OpenAI's Codex reached 3 million weekly active users (70% month-over-month growth), launching a $100 ChatGPT Pro tier with 5x Codex access. Google pushed Antigravity for AI Studio and Gemini CLI as terminal agent. Cursor 3 pivoted from IDE to agent orchestration. The competition for developer mindshare has become the primary battleground ahead of both companies' IPOs.

**April 24-25: Valuation Explosion and Ecosystem Maturation**: Cognition AI (creator of Devin AI software engineer) is in talks to raise at a $25 billion valuation — more than doubling its prior valuation — reflecting the intense interest in AI coding tools. On April 25, three major GitHub repos demonstrate the ecosystem maturing: OpenHands/software-agent-sdk (3.2K stars) provides a clean, modular SDK for building coding agents with support for one-off tasks, routine maintenance, and multi-agent operations. NVIDIA/NemoClaw (1.1K stars) offers a hardened reference stack for running OpenClaw securely with NVIDIA OpenShell runtime. K-Dense-AI/scientific-agent-skills (2.4K stars) provides 133 ready-to-use scientific skills for AI agents covering bioinformatics, genomics, drug discovery, and 78+ scientific databases — compatible with Claude Code, Cursor, and Codex.

The modular SDK pattern (OpenHands) and specialized skills repositories (scientific-agent-skills) signal that the ecosystem is maturing beyond raw model capabilities toward practical, composable tools. This suggests a shift from "which model is best?" to "which agent stack is most reliable and extensible?"

**Claude Code Leak and claw-code**: On March 31, Anthropic accidentally exposed Claude Code's 512,000-line TypeScript source via misconfigured .map files. Within hours, a Python clean-room rewrite using OpenAI's oh-my-codex hit 50K stars in 2 hours and 100K stars total — creating a DMCA-proof derived work and demonstrating that the harness layer is as vulnerable to replication as model weights.

**Multi-Agent Orchestration**: Microsoft Agent Framework v1.0 provides enterprise-grade Python/.NET support with graph-based workflows, streaming, checkpointing, and human-in-the-loop. AgentScope reached production-ready status with MCP/A2A protocol support and real-time voice. oh-my-claudecode enables 32+ specialized agents with automatic parallelization.

**Physical AI Emergence**: At HumanX 2026, Samsanga demonstrated autonomous trucks and robots working alongside human operators. NVIDIA GTC showcased physical AI for healthcare robotics with Open-H, Cosmos-H, and GR00T-H datasets. South Korea deployed thousands of ChatGPT-enabled social care robots for elderly population.

**Self-Improving Agents**: Hermes Agent crossed 35K stars with periodic nudges and agent-curated memory. EvoSkill automatically discovers and synthesizes reusable skills from failed trajectories. lsdefine/GenericAgent crystallizes task execution paths into reusable skills, forming a personal skill tree.

**Agent Memory Systems**: SupermemoryAI reached #1 on LongMemEval, LoCoMo, and ConvoMem benchmarks. TrustGraph provides graph-native context infrastructure. The skills ecosystem (obra/superpowers at 155K+ stars) enables structured agent development workflows.

## Key Developments

| Date | Event | Significance |
|------|-------|-------------|
| 2026-03-22 | Claude Code Channels for Telegram/Discord | MCP-based two-way chat from messaging apps |
| 2026-03-28 | Claude Computer Use goes viral | Anthropic's Super Bowl ad strategy paying off |
| 2026-03-29 | Claude subscriptions more than doubled | Consumer adoption accelerating |
| 2026-04-01 | Claude Code source leaked | 512K lines TypeScript; claw-code 100K stars in hours |
| 2026-04-02 | Cursor 3 pivots to orchestration | Agent-first interface with parallel fleets |
| 2026-04-02 | Microsoft Agent Framework v1.0 | Enterprise multi-language agent infrastructure |
| 2026-04-07 | OpenAI Codex 3M weekly users | 70% month-over-month growth |
| 2026-04-08 | AgentScope production-ready | MCP/A2A, real-time voice, production evaluation |
| 2026-04-08 | HumanX: Physical AI demo | Autonomous trucks in real-world deployment |
| 2026-04-14 | Oracle banking AI agents | Agentic AI entering enterprise workflows |
| 2026-04-15 | Composio agent orchestrator | Parallel coding agents with CI/merge conflict handling |
| 2026-04-24 | Cognition AI in talks at $25B valuation | Devin's creator more than doubling prior valuation |
| 2026-04-25 | OpenHands SDK (3.2K stars) | Modular SDK for coding agents with multi-agent support |
| 2026-04-25 | NemoClaw (1.1K stars) | Hardened reference stack for secure OpenClaw deployment |
| 2026-04-25 | Scientific-agent-skills (2.4K stars) | 133 scientific skills for agents, 78+ databases |
| 2026-04-26 | Claude Code faces user backlash | Anthropic acknowledges missteps; OpenAI's GPT-5.5 launched same day with Codex roots |
| 2026-04-26 | Project Deal: agent-on-agent marketplace | Anthropic runs experiment where Claude models negotiate and transact autonomously |
| 2026-05-01 | Microsoft M365 E7 and Agent 365 GA | $99/user/month bundle; Agent 365 at $15/user/month; first new enterprise license in a decade |
| 2026-05-01 | NVIDIA GB300 Blackwell Ultra enters mass production | Ships May to hyperscalers; 35x lower cost/token; 50x throughput/megawatt for agentic workloads |
| 2026-05-01 | Gemini rolls out to ~4M GM vehicles | Replacing Google Assistant with vehicle-specific AI concierge; largest automotive AI deployment |

## Patterns & Insights

The coding agent market has become the primary driver of AI company revenue. Anthropic's ARR growth from $9B to $30B in under a year was primarily driven by Claude Code. This has made developer adoption critical ahead of IPO timelines.

The harness layer is increasingly contested. The Claude Code leak and rapid replication by claw-code demonstrates that closed-source architectures provide limited moat. Competitive differentiation is shifting to reliability, ecosystem integration, and enterprise support.

Agent-to-agent protocols (MCP with 150M+ installs, A2A) are becoming standard infrastructure. The protocol wars are settling as major companies (Anthropic, OpenAI, Microsoft, Google) adopt compatible standards.

Physical AI is emerging as the next frontier. Autonomous vehicles, robots, and AI-powered infrastructure represent the expansion of agentic AI beyond software into physical environments.

**Ecosystem maturation beyond raw capabilities**: The emergence of modular SDKs (OpenHands), hardened security stacks (NemoClaw), and specialized skills repositories (scientific-agent-skills) signals a shift from model-centric to tooling-centric competition. The April 25 news cycle demonstrates this: OpenHands SDK provides clean separation between one-off tasks, routine maintenance, and multi-agent operations; NemoClaw addresses enterprise security concerns for OpenClaw deployments; scientific-agent-skills brings 133 domain-specific capabilities to agents. This composability means competitive advantage increasingly comes from ecosystem breadth rather than raw model performance.

**AI coding tools as critical infrastructure**: Cognition AI's $25B valuation (more than doubling from prior round) validates AI coding as a strategic investment category. SpaceX's $60B Cursor investment, Anthropic's Claude Code-driven ARR growth, and OpenAI's Codex 3M users all point to the same conclusion: coding agents have crossed the chasm from demo to enterprise necessity.

**Agent-to-agent commerce emerging**: Anthropic's Project Deal — where Claude models represented both buyers and sellers in a classified marketplace, striking real deals for real goods and real money — is a proof-of-concept for AI-to-AI economic activity. The endgame is autonomous commercial agents that can buy, sell, and broker on behalf of humans. This timing, right after GPT-5.5 and Claude Opus 4.7 launches, suggests frontier labs are racing to demonstrate practical agentic utility beyond benchmark superiority.

**Capability regression as competitive vulnerability**: Claude Code's engineering missteps and months of silence before acknowledgment created a window for OpenAI to land GPT-5.5 (with Codex roots) the same day the backlash story broke. Power users have options, and brand loyalty erodes fast when the coding agent doesn't code reliably — this is a real retention risk, not just a PR problem.

## Connections
- [[entities/claude-code]] — Primary driver of Anthropic's ARR growth
- [[entities/claw-code]] — Clean-room rewrite, 100K stars in hours
- [[entities/openclaw]] — 302K stars, fastest-growing open-source project
- [[entities/mcp-protocol]] — 150M+ installs, dominant agent protocol
- [[entities/openhands-sdk]] — Modular SDK for coding agents, 3.2K stars
- [[entities/nemo-claw]] — NVIDIA's hardened stack for secure OpenClaw deployment
- [[entities/scientific-agent-skills]] — 133 scientific skills for agents, 2.4K stars
- [[ideas/agent-democratization]] — Open-source frameworks democratizing agentic AI
- [[sources/anthropic]] — Claude Code success driving $30B ARR
- [[sources/cognition]] — Devin creator, $25B valuation talks, AI coding competition with Claude Code
