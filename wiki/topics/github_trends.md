---
title: "GitHub Trends"
slug: github_trends
last_updated: 2026-05-09
---

# GitHub Trends

## Overview
May 2, 2026 brings three notable repos spanning AI video generation and agent infrastructure. MOVA (972 stars) is a foundation model for synchronized video-audio generation in a single pass, breaking the "silent era" of open-source video models. Serena (23.8K stars) is a powerful MCP toolkit providing semantic code retrieval and editing across 40+ languages, operating at the symbol level via LSP servers — "the IDE for your coding agent." AutoMV (104 stars) is a training-free multi-agent system that auto-generates full music videos from songs at $10-20 per MV using Screenwriter, Director, and Verifier agents.

## Evolution

**Agent Frameworks Mature**: The period sees agent frameworks rapidly evolving from experimental prototypes to production-grade infrastructure. Microsoft Agent Framework v1.0 (April 2) provides enterprise-grade Python/.NET support with graph-based workflows, OpenTelemetry integration, and human-in-the-loop capabilities. AgentScope reaches production-ready status with MCP/A2A protocol support.

**Coding Agent Wars**: Claude Code's viral success spawned intense competition. Cursor 3 pivots from IDE to agent orchestration with parallel fleet approach. OpenClaw crosses 302,000 stars as the fastest-growing open-source project in history. Google's Gemini CLI enters the terminal agent race with 1M context and Apache 2.0 licensing.

**Agent Memory and Skills**: The skills ecosystem matures significantly. obra/superpowers reaches 155K stars as the complete software development methodology for coding agents. Hermes Agent crosses 35K stars with multi-platform support and browser integration. EvoSkill enables automatic skill discovery from failed trajectories.

**Efficient Inference**: Multiple projects address the efficiency frontier. Bonsai 8B (PrismML) achieves 40 tokens/sec on iPhone through 1-bit quantization. Ollama 0.19 doubles Apple Silicon performance via MLX integration. flash-moe runs 397B MoE at 4.4 tokens/sec on MacBook Pro.

**Browser and Web Automation**: LightPanda (Zig-built headless browser) achieves 11x faster performance and 16x less memory than Chrome headless. browser-use enables AI agents to control browsers for web automation.

**April 15-20: New Wave of Developer Tools**: A new crop of tools emerges focused on observability, protocol analysis, and design extraction. codeburn (2.6K stars) provides interactive TUI dashboards for Claude Code, Codex, and Cursor cost observability. anything-analyzer (1.3K stars) offers all-in-one protocol analysis with MITM proxy and MCP server integration. design-extract (929 stars) extracts complete design language from any website. microsoft/markitdown reaches 112K stars as the critical document conversion tool for LLM ingestion pipelines.

OpenAI's openai-agents-python (10.1K stars in initial release) enters the multi-agent framework space with a lightweight yet powerful approach. BasedHardware/omi (8.2K stars) offers next-generation AI companion with multimodal perception. EvoMap/evolver (5.8K stars) implements genome evolution protocols for self-improving AI agents.

**April 21-23: Design Skills and Self-Healing Agents**: A new category emerges: AI design skills for agents. huashu-design (4K stars) offers HTML-native design skill for Claude Code with 20 design philosophies. cc-design (603 stars) and web-design-skill (533 stars) follow the Claude Design pattern for high-fidelity prototyping. browser-harness (4.7K stars) enables self-healing browser harnesses for LLMs. OpenMythos (8.1K stars) provides theoretical reconstruction of Claude Mythos architecture from available research literature. worldmonitor reaches 50.7K stars as real-time global intelligence dashboard.

**April 24: Free Claude Code Alternatives and Code Search MCP**: Three notable repos trend on April 24. huggingface/ml-intern (4.5K stars) is an open-source ML engineer that reads papers, trains models, and ships ML models autonomously. zilliztech/claude-context (8.7K stars) is a code search MCP for Claude Code — making entire codebases the context for any coding agent. Alishahryar1/free-claude-code (6.3K stars) provides free Claude Code access via terminal, VSCode extension, or Discord, supporting NVIDIA NIM, OpenRouter, DeepSeek, LM Studio, and llama.cpp. This reflects demand for cost-effective AI coding solutions and improved context for coding agents.

## Notable Repositories

| Repo | Stars | Description |
|------|-------|-------------|
| forrestchang/andrej-karpathy-skills | 105K+ | Single CLAUDE.md file with 4 principles for Claude Code behavior; derived from Karpathy's LLM coding observations |
| mksglu/context-mode | 11.9K+ | MCP server for context window optimization; 98% reduction across 12+ platforms; 116 releases |
| microsoft/markitdown | 112K+ | Document conversion tool for LLM ingestion pipelines |
| virattt/ai-hedge-fund | 56K+ | Multi-agent autonomous hedge fund |
| obra/superpowers | 155K+ | Agentic skills framework for coding agents |
| ultraworkers/claw-code | 181K+ | Clean-room Claude Code rewrite, 100K in hours |
| nousresearch/hermes-agent | 35K+ | Self-improving agent with multi-platform support |
| microsoft/agent-framework | 9K+ | Enterprise multi-language agent framework |
| agentscope-ai/CoPaw | 15K+ | Personal AI assistant with multi-channel support |
| lightpanda-io/browser | 18K+ | Zig-built headless browser, 11x faster |
| HKUDS/nanobot | 39K+ | Ultra-lightweight universal agent harness |
| KeygraphHQ/shannon | 31K+ | White-box AI pentester, 96.15% XBOW success |
| openai/openai-agents-python | 10K+ | OpenAI's multi-agent workflow framework |
| BasedHardware/omi | 8K+ | Next-gen AI companion with multimodal perception |
| EvoMap/evolver | 5.8K+ | GEP-powered self-evolution engine for agents |
| koala73/worldmonitor | 50.7K+ | Global intelligence dashboard, AI news aggregation |
| kyegomez/OpenMythos | 8.1K+ | Theoretical Claude Mythos architecture reconstruction |
| browser-use/browser-harness | 4.7K+ | Self-healing browser harness for LLMs |
| alchaincyf/huashu-design | 4K+ | HTML-native design skill for Claude Code |
| zilliztech/claude-context | 8.7K+ | Code search MCP for Claude Code |
| huggingface/ml-intern | 4.5K+ | Open-source ML engineer that reads papers, trains models |
| Alishahryar1/free-claude-code | 6.3K+ | Free Claude Code via terminal, VSCode, Discord |
| OpenHands/software-agent-sdk | 3.2K+ | Modular SDK for building coding agents |
| NVIDIA/NemoClaw | 1.1K+ | Hardened reference stack for secure OpenClaw deployment |
| K-Dense-AI/scientific-agent-skills | 2.4K+ | 133 scientific skills for AI agents |
| backnotprop/plannotator | 4.8K+ | Visual coding agent plan/review tool with team collaboration and one-click feedback |
| gotalab/cc-sdd | 3.2K+ | Autonomous implementation with native subagent dispatch and adversarial review |
| MervinPraison/PraisonAI | 7K+ | 24/7 AI workforce in 5 lines of code; memory, RAG, 100+ LLMs |
| aaif-goose/goose | new | Open-source extensible AI agent — install, execute, edit, test with any LLM |
| msitarzewski/agency-agents | new | Complete AI agency with specialized expert agents (frontend wizards, Reddit ninjas, etc.) |
| oraios/serena | 23.8K+ | MCP semantic code toolkit for 40+ languages; symbol-level editing via LSP |
| karpathy/autoresearch | 79.2K+ | Autonomous LLM research agent that experiments overnight on a single GPU; self-contained with minimal dependencies |
| aden-hive/hive | 10.2K+ | Multi-agent harness for production AI workloads; graph-based execution DAG, self-healing graph evolution, cost enforcement |
| zai-org/GLM-OCR | 6.3K+ | Multimodal OCR on GLM-V architecture; 0.9B parameters, 94.62 on OmniDocBench V1.5; deployable via vLLM, SGLang, Ollama |
| OpenMOSS/MOVA | 972+ | Foundation model for synchronized video-audio generation in a single pass |
| ruvnet/ruflo | 39.9K+ | Open-source agent orchestration for Claude Code deploying 100+ agent swarms with self-learning memory |
| abhigyanpatwari/GitNexus | 35.4K+ | Zero-server code intelligence engine indexing codebases into MCP-accessible knowledge graphs |
| AIDC-AI/Pixelle-Video | 10.5K+ | AI-powered fully automated short video engine from topic to final video |
| OpenMOSS/MOSS-TTS | 1,765+ | 20+ language TTS with 3-second voice cloning and real-time streaming; edge-to-cloud variants |
| k2-fsa/OmniVoice | 4,359+ | 600+ language voice synthesis with diffusion architecture; 40x faster than real-time |
| Cortiqaai/Cordenex | 247+ | Multi-agent autonomous software engineer for terminal; collaborative coding and project planning |
| cocoindex-io/cocoindex | 9,018+ | Incremental engine for long-horizon agents; persistent stateful AI with automatic state management and recovery |
| Q00/ouroboros | 3,677+ | Agent OS: declarative operating system shifting from prompt engineering to specification-driven behavior |
| hugohe3/ppt-master | 13,205+ | AI generates natively editable PPTX from any document — real PowerPoint shapes with native animations, not images |

## Patterns & Insights

The "harness layer" has emerged as a critical battleground. claw-code's explosive growth demonstrates that closed-source agent architectures can be rapidly replicated — the competitive moat is narrower than assumed. This has implications for business models built on agent frameworks.

The multi-agent orchestration trend is accelerating. frameworks like microsoft/agent-framework, AgentScope, and CoPaw enable complex agent teams with specialized roles, parallel execution, and workflow orchestration.

The open-source agent ecosystem is rapidly converging on standards. MCP (150M+ installs), A2A protocol support, and cross-platform compatibility are becoming baseline expectations.

The efficiency frontier is democratizing access. 1-bit quantization, MLX optimization, and native hardware acceleration mean frontier-class models can now run on consumer devices.

**Design skills emerging**: Following Claude Design's direct challenge to Figma, new tools like huashu-design, cc-design, and web-design-skill enable AI agents to produce high-fidelity HTML designs — suggesting a new category of "design skills" for agents.

**Self-healing browser harnesses**: browser-harness (4.7K stars in days) enables LLMs to complete tasks with self-healing browser automation — a new pattern for agent reliability.

**OpenMythos as knowledge synthesis**: OpenMythos (8.1K stars) demonstrates community interest in understanding frontier models from public information — a form of open-source model archaeology.

**Free alternatives and code context**: The trending repos on April 24 (free-claude-code, claude-context) reflect demand for cost-effective AI coding solutions. The MCP code search tool addresses a key limitation — giving coding agents full codebase context rather than just file snippets.

**April 25: Modular agent frameworks and scientific skills**: New repos trending include OpenHands/software-agent-sdk (3.2K stars) — a clean, modular SDK for building AI agents that work with code, supporting one-off tasks, routine maintenance, and multi-agent operations. NVIDIA/NemoClaw (1.1K stars) provides a hardened reference stack for running OpenClaw securely with NVIDIA OpenShell runtime. K-Dense-AI/scientific-agent-skills (2.4K stars) offers 133 ready-to-use scientific skills for AI agents covering bioinformatics, genomics, drug discovery, and 78+ scientific databases — compatible with Claude Code, Cursor, and Codex.

**April 27: GitHub's agent-scale economics crisis**: GitHub is now processing 275 million commits per week — a 14x explosion from 2025's 1 billion milestone. AI agents opened 17 million PRs in March 2026 vs 4 million in September 2025. GitHub Actions compute hit 2.1 billion minutes in a single week, causing visible outages. The real story is economics: GitHub's free tier was designed for human developers and occasional CI bots, not autonomous agent fleets that generate more code per hour than entire engineering teams. The platform is caught between its open-source heritage (which discourages paywalls) and the reality that agent traffic is destroying economics built for human-scale usage.

**April 29: GitHub Copilot Agent Tier — first platform monetization of agent-scale usage**: GitHub announces Copilot Agent Tier at $49/agent/month with free tier capped at 500 commits/month. This is the direct response to the unsustainable infrastructure economics exposed on April 27. Smaller agent frameworks that relied on GitHub's free tier now face a $49/month per agent tax, favoring well-funded players like Cursor, Claude Code, and Codex. GitHub is essentially becoming a tollbooth on the agent economy it helped create. [[entities/copilot-agent-tier]] — [[sources/github]]

**April 29: TradingAgents and Codex skills trending**: TradingAgents (54.6K stars) is a multi-agent LLM financial trading framework with autonomous research, analysis, risk management, and trading roles. awesome-codex-skills (4.5K stars) is a curated list of practical Codex skills for automating workflows. [[topics/ai_companies]]

**April 30: Workforce-in-a-box pattern emerging**: Three repos trending — plannotator (4.8K stars) for visual code review collaboration, cc-sdd (3.2K) for autonomous implementation with adversarial review, and PraisonAI (7K stars) for "24/7 AI workforce in 5 lines of code" with RAG and 100+ LLM support. The pattern emerging: agent frameworks are no longer just for developers — they're becoming plug-and-play workforce replacements that enterprises can deploy without engineering teams. The democratization is shifting from "anyone can build agents" to "anyone can hire an AI workforce."

**May 1: Agent orchestration frameworks with zero third-party dependencies**: Three new repos trending — harmonist (186 specialist agents across 16 categories, mechanical protocol enforcement, zero third-party deps, 949 stars), CoreCoder (~1,400 lines Python inspired by Claude Code, parallel tool execution, 3-layer context compression, 652 stars), and open-agent-sdk-go (lightweight Go SDK, 32 built-in tools, MCP support, session management, in-process agent loop, 151 stars). The "zero third-party dependencies" philosophy signals teams are seeking to minimize supply chain risk after the MCP vulnerability and npm compromises.

**May 2: Semantic code infrastructure and AI video generation**: Three repos trending. OpenMOSS/MOVA (972 stars) — foundational model for synchronized video-audio generation in a single inference pass, breaking the "silent era" of open-source video models with multilingual lip-sync and ComfyUI integration. oraios/serena (23.8K stars) — MCP toolkit for semantic code retrieval, editing, and refactoring across 40+ languages; operates at the symbol level rather than line numbers via LSP language servers, described as "the IDE for your coding agent." multimodal-art-projection/AutoMV (104 stars) — training-free multi-agent music video generator using Screenwriter, Director, and Verifier agents with character consistency banks and beat-aligned editing at ~$10-20 per MV.

**May 3-4: Agent infrastructure goes enterprise-scale**: Three repos trending. ruvnet/ruflo (39.9K stars) — open-source agent orchestration platform for Claude Code deploying multi-agent swarms with self-learning memory, federated communication, and enterprise security across 100+ specialized agents. abhigyanpatwari/GitNexus (35.4K stars) — zero-server code intelligence engine that indexes any codebase into a knowledge graph (dependencies, call chains, execution flows) and exposes it through MCP tools for AI coding agents. AIDC-AI/Pixelle-Video (10.5K stars) — AI-powered fully automated short video engine handling scriptwriting, AI imagery, voice synthesis, background music, and final assembly from a single topic input. The pattern: coding agent infrastructure (Ruflo, GitNexus) is converging with content creation infrastructure (Pixelle-Video, AutoMV) — agent frameworks are spreading beyond code into every creative domain.

**May 5: The efficiency frontier in agent frameworks**: nanobot's 41.7K stars demonstrate that developers value minimal-code agent harnesses. At ~4,000 lines versus Claude Code's 512,000 lines, nanobot achieves multi-platform chat, MCP support, and WebUI in 99% less code. This validates the "configuration over code" principle (Andrej Karpathy's 105K-star CLAUDE.md) at the framework level. Agent Squad (7.6K stars) adds model-agnostic orchestration, showing demand for frameworks that avoid vendor lock-in at the orchestration layer.

**May 7: Open-source voice AI wave and multi-agent coding**: Three repos trending span voice synthesis and collaborative agent coding. MOSS-TTS (1,765 stars) is an open-source TTS family supporting 20+ languages with voice cloning from 3-second audio and real-time streaming at 180ms TTFB — features that were proprietary differentiators for closed labs just months ago. OmniVoice (4,359 stars) pushes language coverage to 600+ with a diffusion language model architecture and 40x real-time inference speed, dwarfing the 50-100 language support typical of proprietary offerings. Cordenex (247 stars) is a multi-agent autonomous software engineer explicitly targeting team-based development with collaborative coding, project planning, and automated code review — extending the coding agent paradigm from individual assistance to organizational workflows.

**May 8: Specification-driven agents and document-to-presentation AI**: Three repos trending span agent architecture and document automation. cocoindex (9,018 stars) is an incremental engine for long-horizon agents, solving the state-persistence problem that prevents most agents from handling multi-day workflows. ouroboros (3,677 stars) is a declarative "Agent OS" shifting the paradigm from prompt engineering to specification-driven behavior — "Stop prompting. Start specifying." ppt-master (13,205 stars) uses AI to generate natively editable PowerPoint presentations from any document, producing real PowerPoint shapes with native animations rather than static images. The pattern: agent development is maturing from artisanal prompt crafting to structured engineering, while AI output is becoming compatible with existing corporate toolchains rather than requiring new formats.

**May 6: Autonomous research and production harnesses**: Three repos trending signal agent maturity beyond coding. AutoResearch (79.2K stars) is Karpathy's autonomous LLM research agent that experiments overnight on a single GPU — the highest-starred new repo of the day, validating demand for end-to-end scientific automation. Hive (10.2K stars) is a production multi-agent harness with graph-based execution DAGs, self-healing failure recovery, and cost enforcement — addressing the operational reliability gap that most agent frameworks ignore. GLM-OCR (6.3K stars) achieves 94.62 on OmniDocBench with only 0.9B parameters, proving sub-1B models can dominate narrow multimodal tasks. The pattern: agents are fragmenting by vertical (research, production ops, document understanding) just as the broader ecosystem fragments by profession.

## Connections
- [[entities/claude-code]] — Leaked source code spawned claw-code phenomenon; free alternatives emerging; Karpathy principles directly address Claude Code quality issues
- [[entities/claw-code]] — Clean-room rewrite, 181K+ stars
- [[entities/mcp-protocol]] — 150M+ installs, becoming foundational infrastructure; context-mode is an MCP tool optimizing MCP-based workflows
- [[entities/serena]] — MCP toolkit providing semantic code operations at symbol level; 23.8K stars; "IDE for your coding agent"
- [[entities/mova]] — Synchronized video-audio generation foundation model; breaks open-source "silent era"
- [[entities/automv]] — Multi-agent music video generation at $10-20 per MV
- [[entities/openclaw]] — 302K stars, fastest-growing open-source project
- [[entities/claude-design]] — Direct challenge to Figma spawning design skills ecosystem
- [[entities/openhands-sdk]] — Modular SDK for building coding agents; 3.2K stars
- [[entities/nemo-claw]] — NVIDIA's hardened reference stack for secure OpenClaw deployment
- [[entities/scientific-agent-skills]] — 133 scientific skills for agents, 2.4K stars
- [[entities/harmonist]] — Portable agent orchestration with 186 specialist agents; zero third-party deps
- [[entities/corecoder]] — Minimalist Claude Code-inspired coding agent in ~1,400 lines Python
- [[entities/open-agent-sdk-go]] — Lightweight Go SDK for AI agents with MCP support
- [[entities/andrej-karpathy-skills]] — 105K stars; single CLAUDE.md with 4 principles; "configuration over code" for agent behavior; nanobot's minimal-code approach validates this principle at the framework level
- [[entities/context-mode]] — 11.9K stars; 98% context reduction via MCP; critical infrastructure for continuous agent operation
- [[entities/ruflo]] — 39.9K stars; Claude Code agent fleet orchestration with 100+ specialized agents
- [[entities/gitnexus]] — 35.4K stars; MCP knowledge graph for agent codebase navigation; completes agent infrastructure triad with Serena and context-mode
- [[entities/pixelle-video]] — 10.5K stars; fully automated short video engine demonstrating agent frameworks spreading beyond code into creative production
- [[ideas/agent-verticalization]] — Agent infrastructure maturing from individual tools to organizational platforms
- [[entities/autoresearch]] — 79.2K stars; Karpathy's autonomous research agent that experiments overnight on a single GPU; extends "configuration over code" into autonomous experimentation
- [[entities/hive]] — 10.2K stars; production multi-agent harness with self-healing DAG evolution and cost enforcement; fills the operational reliability gap in agent orchestration
- [[entities/glm-ocr]] — 6.3K stars; 0.9B-parameter multimodal OCR beating frontier models on OmniDocBench; validates efficiency frontier for narrow domains
- [[entities/nanobot]] — 41.7K stars; ultra-lightweight personal agent in ~4K lines Python; 99% smaller than alternatives; validates minimal-code agent philosophy
- [[entities/agent-squad]] — 7.6K stars; model-agnostic multi-agent orchestration with SupervisorAgent across Bedrock, Anthropic, OpenAI
- [[entities/web-design-skill]] — 533 stars; transforms AI-generated pages from functional to stunning alongside cc-design in the emerging design-skills category
- [[entities/future-agi]] — 482 stars; end-to-end agent evaluation platform reflecting maturation of agent observability infrastructure
- [[entities/mercury-agent]] — 531 stars; soul-driven personal AI agent with permission-hardened tools and CLI/Telegram multi-channel access
- [[entities/moss-tts]] — 1,765 stars; open-source TTS with 20+ languages, 3-second voice cloning, and 180ms real-time streaming; 0.1B edge variant challenges cloud-dependent proprietary voice models
- [[entities/omnivoice]] — 4,359 stars; 600+ language diffusion voice synthesis at 40x real-time; open-source voice AI is outpacing proprietary language coverage
- [[entities/cordenex]] — 247 stars; multi-agent team coding with collaborative workflows and automated code review; extends coding agents from individual to organizational use
- [[ideas/compute-shortage-forces-cooperation]] — Open-source voice models (MOSS-TTS 0.1B variant, OmniVoice) enable on-device agent voice output without cloud dependency — reducing reliance on the compute partnerships that define the closed-source ecosystem
- [[entities/cocoindex]] — cocoindex's incremental engine for long-horizon agents addresses a critical infrastructure gap: most agents lose state between sessions, making them unsuitable for multi-day workflows
- [[entities/ouroboros]] — ouroboros's declarative specification model represents a philosophical maturation from artisanal prompt engineering to systematic agent architecture; "Stop prompting. Start specifying." captures the industry shift
- [[entities/ppt-master]] — ppt-master's 13.2K stars validate that AI output compatibility with existing corporate tools (native .pptx) is as important as generation quality; the "invisible infrastructure" of format compatibility drives adoption
- [[ideas/agent-control-interface-wars]] — ouroboros's specification-driven model and cocoindex's persistent-state model together represent a shift toward structured, predictable agent behavior — the engineering discipline enterprises need before wide deployment
- [[timelines/2026-05]] — May 2-8 trending repos trace the agent maturity arc: Serena (semantic infrastructure), Ruflo/GitNexus (enterprise orchestration), nanobot (minimalism), cocoindex/ouroboros/ppt-master (infrastructure and document automation)