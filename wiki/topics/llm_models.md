---
title: "LLM Models"
slug: llm_models
last_updated: 2026-05-04
---

# LLM Models

## Overview
May 2, 2026 delivers the most damning empirical critique of the LLM paradigm to date: ARC-AGI-3 results show GPT-5.5 (0.43%) and Claude Opus 4.7 (0.18%) performing below 1% on interactive reasoning puzzles humans solve effortlessly — while these same models ace SWE-bench at 80%+. The finding that models "hallucinate" mapping unfamiliar 2D grids to Tetris/Breakout reveals they're not reasoning about novel situations at all — they're routing to the nearest memorized template. Mistral Medium 3.5 enters the fray with a reasoning-effort toggle (one model switching modes per-request instead of separate chat/reasoning variants), and the Pentagon's "AI-first" declaration scales military AI deployment to 1M+ defense personnel. The industry is simultaneously discovering the ceiling of current architectures and building the infrastructure for what comes next. Claude Mythos established the precedent of capability-based restrictions, and by May 2026 both Anthropic (Claude Security) and OpenAI (GPT-5.5 Cyber) are racing to build defensive moats around their most dangerous capabilities. NVIDIA's GB300 Blackwell Ultra entering mass production addresses the economics problem that GitHub's 275M weekly commits revealed — 35x lower cost-per-token for agentic AI. Meanwhile, the Senate GUARD Act advancing unanimously signals Washington has found its bipartisan AI issue: child safety with criminal penalties for model conduct.

## Evolution

The period opens with NVIDIA's GTC 2026 announcement of the Vera Rubin platform, signaling the next generation of AI hardware. Within days, Xiaomi's MiMo-V2-Pro appeared anonymously on OpenRouter as "Hunter Alpha," achieving 1426 Elo on GDPval-AA benchmark before being revealed as Xiaomi's trillion-parameter model built by former DeepSeek researcher Luo Fuli.

The Claude Mythos leak on March 26 fundamentally changed the conversation. Nearly 3,000 internal documents exposed a model described internally as "the most capable we've built" with "dramatically higher" scores than Opus 4.6 on coding and cybersecurity benchmarks. The model was found capable of discovering unknown vulnerabilities in production codebases — capabilities described as "unprecedented cybersecurity risks."

OpenAI's GPT-5.4 family launched mid-March with Mini and Nano variants offering near-top-tier performance at accessible price points. The GPT-5.4 "Thinking" variant achieved 75.0% on OSWorld-Verified, a 27.7 percentage point increase over GPT-5.2, enabling native operating system-level computer use.

Google's Gemma 4 release on April 2 marked a strategic shift to Apache 2.0 licensing — fully permissive for the first time. Four variants (2B to 31B) with the 31B dense model ranking #3 on Arena AI's open leaderboard, while the 26B MoE model ranked #6, outperforming models 20x their size.

Alibaba's Qwen3.6-Plus launched April 2 with 1M-token context and agentic coding performance competitive with Claude Opus 4.5, debuting at the top of global usage charts.

Meta surprised the community with Muse Spark (April 8) — their first proprietary model, breaking with the open-source tradition since 2023. The model scores 52 on the Artificial Analysis Intelligence Index v4.0, ranking 4th, excelling at figure understanding (86.4% on CharXiv Reasoning) but struggling with abstract reasoning.

**April 15-20: The Application Layer Takes Over**

The week of April 15-20 marks a clear inflection point: the model race is giving way to application competition. Anthropic releases Claude Opus 4.7 with 87.6% on SWE-bench (up from 80.8% on Opus 4.6) and Claude Design — a direct challenge to Figma's design workflow moat. OpenAI counters with GPT-Rosalind for life sciences, targeting Amgen, Moderna, Novo Nordisk. The NSA confirms partnership with Anthropic on Claude Mythos through Project Glasswing, identifying thousands of zero-day vulnerabilities.

Stanford HAI's 2026 report confirms China's AI capabilities have fundamentally closed the gap with the US. ByteDance's best model trails Anthropic's Claude by only 39 Arena points — a 2.7% difference compared to 300+ points in May 2023. Notably, China achieved this with $12.4B in private investment versus America's $285.9B, suggesting structural efficiency advantages.

NVIDIA's Ising emerges as a genuinely new category — open quantum AI models for quantum error correction, delivering 2.5x faster and 3x more accurate decoding. If delivered, this could reshape the AI hardware roadmap entirely.

**April 21-23: Security Concerns and Reasoning Advances**

The final days of the period see security concerns intensify. A critical MCP vulnerability (affecting 150M+ installations) enables arbitrary command execution across 7,000+ servers — Anthropic calls it "expected behavior." Meanwhile, Claude Mythos 5 is confirmed at 10 trillion parameters, with the Bank of England warning it could "crack the whole cyber-risk world open." Google reveals Gemini 3 Deep Think can identify logical flaws in peer-reviewed math papers that cleared human review. China's Qihoo 360 finds 1,000 software vulnerabilities using AI-powered agents.

**April 24: DeepSeek V4 and the China Challenge**

DeepSeek releases V4-Pro (1.6T total/49B active params) and V4-Flash (284B total/13B active params) on April 24, featuring enhanced agentic coding, world-class reasoning, and 1M context as default. Open weights available on Hugging Face. Tencent and Alibaba are reportedly in talks to invest in DeepSeek's first funding round, with Tencent proposing up to a 20% stake — a significant shift as major Chinese tech giants seek to partner with the AI startup that rattled Silicon Valley.

**April 26: Flagship Model Collision and Capability Regression**

Two flagship models shipping within one week of each other (Claude Opus 4.7 on April 17, GPT-5.5 on April 23) both positioned as top agentic coding platforms with 1M-token contexts. OpenAI appears to have accelerated GPT-5.5 specifically to counter Claude Opus 4.7's SWE-bench lead. Meanwhile DeepSeek V4-Pro-Max scores 80.6% on SWE-bench Verified at $1.74/M tokens vs Opus 4.7's ~$10/M — the cost-performance frontier is suddenly crowded. Concurrently, Anthropic acknowledges engineering missteps causing Claude Code's recent performance decline, risking power user defection to OpenAI's Codex. Meanwhile both Anthropic (Claude Mythos 5) and OpenAI (GPT-5.4 Cyber) release models explicitly positioned for cyber offense/defense — the specialization trend accelerating as general performance benchmarks saturate.

## Key Developments

| Date | Event | Significance |
|------|-------|-------------|
| 2026-03-17 | GPT-5.4 Mini/Nano release | Near-top-tier performance at accessible costs |
| 2026-05-02 | ARC-AGI-3 results: GPT-5.5 0.43%, Opus 4.7 0.18% | Models route unfamiliar situations to memorized templates (hallucinating Tetris from grids); strongest evidence yet that LLMs don't reason — they retrieve |
| 2026-05-02 | Mistral Medium 3.5 released | 128B dense model with reasoning-effort toggle per request; SWE-Bench 77.6%, AIME25 86.3%; one model for chat+reasoning+code instead of separate variants |
| 2026-05-02 | OpenAI open-sources Symphony for Codex orchestration | "Every task gets an agent" model formalized; 15K+ stars in days; 500% PR increase at OpenAI internal teams |
| 2026-05-02 | context-mode MCP server trends (11.9K stars) | 98% context reduction across 12+ platforms; context optimization becomes critical agent infrastructure |
| 2026-05-02 | andrej-karpathy-skills hits 105K stars | Single CLAUDE.md file with 4 principles for agent behavior; "configuration over code" approach to agent quality |
| 2026-03-19 | Xiaomi MiMo-V2-Pro revealed as "Hunter Alpha" | Chinese AI "stealth launch" strategy demonstrated |
| 2026-03-26 | Claude Mythos documents leaked | 3,000 internal docs exposed unprecedented cybersecurity risks |
| 2026-04-02 | Google Gemma 4 (Apache 2.0) | First fully permissive Gemma release, 31B ranks #3 on Arena |
| 2026-04-02 | Qwen3.6-Plus launches | 1M context, tops global usage charts on debut |
| 2026-04-05 | Claude Mythos 5 (10T params) confirmed | First widely recognized 10-trillion-parameter model |
| 2026-04-08 | Meta Muse Spark (proprietary) | Breaks Meta's open-source tradition, ranks 4th |
| 2026-04-10 | Claude Opus 4.6: 80.8% on SWE-bench | Near-tie with Gemini 3.1 Pro (80.6%) on production-relevant coding |
| 2026-04-14 | GPT-5.4-Cyber released | OpenAI's defensive cybersecurity model variant |
| 2026-04-16 | Stanford HAI: US-China gap effectively closed | Top models within 2.7 points on Arena benchmark |
| 2026-04-17 | Claude Opus 4.7: 87.6% SWE-bench, Claude Design | Major coding gains and direct Figma challenge |
| 2026-04-17 | GPT-Rosalind: life sciences model | OpenAI targets Amgen, Moderna, Novo Nordisk |
| 2026-04-18 | NVIDIA Ising: open quantum AI models | First quantum AI model family; 2.5x faster error correction |
| 2026-04-19 | Mozilla Thunderbolt: enterprise AI client | Self-hostable, cross-platform, OpenAI-compatible |
| 2026-04-20 | NSA uses Claude Mythos via Project Glasswing | Identified thousands of zero-day vulnerabilities |
| 2026-04-21 | Critical MCP vulnerability disclosed | 150M+ installations exposed to remote code execution |
| 2026-04-22 | Claude Mythos 5: 10T params, cybersecurity focus | 10-trillion-parameter model for vulnerability discovery |
| 2026-04-22 | Qihoo 360 finds 1,000 vulnerabilities | AI-powered Vulnerability Discovery Agent |
| 2026-04-23 | Bank of England on Mythos | "Could crack the whole cyber-risk world open" |
| 2026-04-23 | Google Cloud Next: TPU 8th gen, Gemini Enterprise Agent Platform | 3x Ironwood performance, managing thousands of agents |
| 2026-04-23 | OpenAI releases GPT-5.5 | "Smartest and most intuitive" model; super app vision |
| 2026-04-24 | GitHub Copilot training opt-out deadline | Users must opt out by April 24 to prevent code usage for training |
| 2026-04-24 | DeepSeek V4 released | V4-Pro (1.6T/49B) and V4-Flash (284B/13B), 1M context, open weights |
| 2026-04-24 | Tencent/Alibaba in talks to invest in DeepSeek | Tencent proposing up to 20% stake; major Chinese tech backing DeepSeek |
| 2026-04-25 | Google releases new AI agents suite | Challenge to OpenAI and Anthropic in agentic AI market |
| 2026-04-26 | Claude Mythos 5 goes military-grade | Forces global cybersecurity rethink; OpenAI counters with GPT-5.4 Cyber same day |
| 2026-04-26 | Claude Code faces user backlash | Anthropic acknowledges engineering missteps; power users may defect to Codex |
| 2026-04-26 | xAI grok-voice-think-fast-1.0 launches | 67.3% on τ-voice Bench; voice agent market heating up |
| 2026-04-27 | GPT-5.5 49-day release cycle revealed as procurement lock-in | Vellum analysis shows enterprise deal-closing strategy, not benchmarking |
| 2026-04-27 | GitHub 275M commits/week; AI agents opened 17M PRs in March | Platform strain signals coming paywalls for agent-scale usage |
| 2026-04-28 | OpenAI Q1 revenue miss confirmed | First concrete sign Claude is winning enterprise coding contracts |
| 2026-04-28 | DeepSeek V4-Pro-Max: $1.74/M tokens | Cost-performance leader; 2.6x cheaper than Claude Opus 4.7 |
| 2026-04-30 | OpenAI secures 10GW of US compute | 3GW added in 90 days; surpasses original Stargate target years early |
| 2026-04-30 | Anthropic eyes $50B raise at $900B valuation | Revenue run rate nearing $40B; 2.4x valuation increase in under 3 months |
| 2026-04-30 | DeepSeek V4 Flash: $0.14/$0.28 per million tokens | 100x cheaper than GPT-5.5/Claude Opus 4.7; 78% SWE-bench |
| 2026-04-30 | Google signs Pentagon deal for classified military AI | Crosses "Don't Be Evil" rubicon; carves out defense niche |
| 2026-04-30 | Qwen 3.6-35B-A3B: 73.4% SWE-bench on RTX 4090 | 3B active params; frontier-grade coding on consumer hardware |
| 2026-04-30 | Apple confirms Gemini-powered Siri for iOS 27 | Knowledge distillation from large Gemini models to on-device Apple Foundation Models |
| 2026-05-01 | NVIDIA GB300 Blackwell Ultra enters mass production | 288GB HBM3e, 10 TB/s, NVLink 6; 50x throughput/megawatt, 35x lower cost/token for agentic AI |
| 2026-05-01 | Anthropic launches Claude Security (public beta) | Powered by Opus 4.7; integrated with CrowdStrike, Palo Alto, SentinelOne, Wiz, Microsoft Security |
| 2026-05-01 | Microsoft M365 E7 and Agent 365 GA at $99/$15 per user/month | First new enterprise license in a decade; bundles E5, Copilot, Agent 365, Entra Suite |
| 2026-05-01 | Microsoft Copilot adds multi-model support | Claude joins OpenAI models in Copilot; 20M paid enterprise seats; Accenture 740K seats; Legal Agent launched as first profession-specific vertical |
| 2026-04-28 | IBM Bob: multi-model orchestration for SDLC | Routes tasks to Claude, Mistral, IBM Granite based on fit; represents shift from "best single model" to "best model per task" architecture |

## Patterns & Insights

**The reasoning-revelation gap**: ARC-AGI-3 results expose a fundamental truth: models that score 80%+ on SWE-bench score <1% on puzzles children can solve. The finding that models hallucinate Tetris/Breakout from unfamiliar grids reveals the architecture limitation — these systems pattern-match to known templates rather than constructing situation-specific models. Every new benchmark designed to test genuine reasoning (not memorization) exposes the same ceiling.

**The reasoning toggle design pattern**: Mistral Medium 3.5's per-request reasoning-effort toggle is an architectural alternative to shipping separate models for chat vs reasoning. If this pattern proves effective at scale, it could obsolete the multi-model strategy OpenAI (o-series vs GPT) and Anthropic (Opus vs Claude Security) are pursuing.

The "stealth launch" pattern has emerged as a major trend — Xiaomi's MiMo-V2-Pro tested anonymously as "Hunter Alpha" on OpenRouter before formal reveal, allowing unbiased benchmark data collection before brand expectations distorted assessment. This approach is being adopted more widely.

The capability-safety tension has reached unprecedented levels. Claude Mythos represents a new category: models restricted not because humans might misuse them, but because the model itself could discover vulnerabilities that outpace defender response. This has triggered government-level concern, with VP Vance and Treasury Secretary convening emergency calls with tech CEOs.

Benchmark saturation is becoming evident. ARC-AGI-3 saw every frontier model score under 1% on tasks 100% of humans solved on first try. Traditional benchmarks are failing to keep pace with capability gains.

**The super app convergence**: OpenAI's GPT-5.5 release with "super app" framing — combining ChatGPT, Codex, and AI browser — signals that the major AI labs are pivoting from model competition to platform competition. This mirrors the evolution of mobile apps where the battle shifted from operating systems to app ecosystems.

**The US-China AI competition intensifies on multiple fronts**: DeepSeek V4's release with open weights and 1M context default, combined with Tencent and Alibaba investment talks, signals a new phase in the geopolitical AI rivalry. Google's new AI agents suite on April 22 adds another dimension — now both US and Chinese labs are competing across models, agents, and platforms simultaneously.

**The cybersecurity-AI convergence**: Both OpenAI (GPT-5.4-Cyber) and Anthropic (Claude Mythos) are releasing models with intentionally lowered safeguards for defensive purposes — a trend that blurs the line between safety research and weaponization.

**AI auditing human expertise**: Gemini 3 Deep Think identifying errors in peer-reviewed math papers signals a new era of AI-assisted academic research where AI can audit human expertise in specialized domains.

**MCP as supply chain risk**: The MCP vulnerability affecting 150M+ installations demonstrates that "expected behaviors" in architectural decisions can propagate silently across languages and libraries — a supply chain event, not just a CVE.

**Capability regression as retention risk**: Claude Code's engineering missteps causing performance decline, with Anthropic staying silent for months, shows that shipped capability regression is a real competitive risk. Power users have options, and brand loyalty erodes fast when the coding agent doesn't code reliably.

**Voice as a distinct battleground**: xAI's grok-voice-think-fast-1.0 scoring 67.3% on τ-voice Bench, specifically outperforming in retail, airline, and telecom workflows, demonstrates that voice models are becoming a separate competitive dimension from text. The specialization trend is accelerating — every major model release this week targets a vertical capability (cyber, voice, coding) rather than general performance.

**The enterprise cost war begins**: OpenAI's Q1 revenue miss is the first concrete signal that Claude is winning deterministic developer workflows. GPT-5.5's benchmark lead is real, but Anthropic's $25/M output tokens vs OpenAI's $30/M gives enterprise buyers a 17% cost advantage on the most expensive axis. DeepSeek V4-Pro-Max at $1.74/M tokens changes the math entirely — suddenly the cost-performance frontier belongs to Chinese labs, not Western ones.

**April 27: The Institutional Stress Test**: The day's most significant news is the Musk vs. Altman court case beginning — the trial that could force OpenAI to revert to a non-profit structure, invalidating every Microsoft investment instrument and enterprise contract built on the assumption of a commercial entity. Meanwhile, GPT-5.5's 49-day release cycle is revealed as an enterprise procurement lock-in strategy (not benchmarking), and GitHub's infrastructure strain from 275M commits/week signals that free-tier economics built for human developers cannot survive fleets of autonomous agents. The connective tissue: the gap between AI capability growth and institutional frameworks (legal, economic, governance) meant to contain it is widening faster than any previous technology transition. Companies are building facts on the ground and hoping legal/regulatory systems will accommodate rather than reverse what they've built.

**April 28: Claude Eating OpenAI's Lunch in Enterprise**: OpenAI missed multiple Q1 monthly revenue targets after losing ground to Anthropic in coding and enterprise markets — the first concrete sign that Claude is winning deterministic developer workflows. GPT-5.5's Terminal-Bench lead (82.7% vs 58.6% Opus 4.7) is real, but OpenAI charges $30/M output tokens vs Anthropic's $25/M, and enterprise buyers care about total cost of ownership. Meanwhile, DeepSeek V4-Pro-Max at $1.74/M tokens is now the cost-performance leader — 2.6x cheaper than Claude Opus 4.7 and 17x cheaper than GPT-5.5's output pricing. DeepSeek's 1.6T parameter model with open weights continues the China challenge at a fraction of Western cost structures.

**April 29: Institutional Contradictions Surface**: The Musk vs Altman trial reveals 2017 emails showing Altman and Brockman discussed for-profit conversion before the 2019 "capped profit" announcement — threatening to invalidate Microsoft's $10B+ investment and every enterprise contract since 2019. Goldman Sachs and Morgan Stanley threaten to withdraw from OpenAI's IPO. The EU issues its first AI Act fine — €800M on Meta for unauthorized data training, citing the MCI employee tracking program. TSMC's 3nm yield collapses to 52%, creating a Q3 supply cliff for H200 and AMD MI350 wafers. Meanwhile, Mistral Ultra 2 (78.4% SWE-bench at €2/M) positions itself as the EU-compliant alternative to US labs. Ineffable Intelligence hires 50 senior researchers from DeepMind, OpenAI, and Anthropic in 72 hours — assembling the most credentialed AI research team in history. The pattern: legal, regulatory, physical, and economic frameworks are not keeping pace with capability deployment.

**April 30: The Bifurcation Week Concludes**: OpenAI secures 10GW of US compute (3GW added in 90 days), surpassing Stargate targets years early — a physical energy infrastructure moat. Anthropic eyes $50B raise at $900B valuation, revenue run rate nearing $40B, doubling from $380B valuation in under three months. DeepSeek V4 Flash launches at $0.14/$0.28 per million tokens — 100x cheaper than frontier models while scoring 78% on SWE-bench. Qwen 3.6-35B-A3B scores 73.4% SWE-bench with just 3B active parameters on an RTX 4090 — frontier-grade coding on consumer hardware. The week ends with a clear bifurcation: premium reasoning (Opus, GPT-5.5) vs commodity inference (DeepSeek, Qwen, Kimi) — and commodity inference getting frontier-level scores.

**May 1: The Defensive Pivot and Governance Reality**: Anthropic launches Claude Security (powered by Opus 4.7) as a native security scanning capability inside Claude Code — if you build AI that finds vulnerabilities, you must build one that fixes them. Partnering with CrowdStrike, Palo Alto, and Wiz shows Anthropic is becoming the intelligence layer inside existing security stacks rather than replacing them. OpenAI's GPT-5.5 Cyber restrictions (after mocking Anthropic for the same with Mythos) reveal that liability now overrides competitive posturing — once the White House opposed Mythos expansion and NSA probed Microsoft with it, every frontier lab realized unrestricted cyber-AI is a legal grenade. NVIDIA's GB300 Blackwell Ultra (35x lower cost/token) directly addresses the economics exposed by GitHub's 275M commits/week — if agent-scale coding is 1/35th the cost, the $49/agent/month GitHub Copilot pricing starts looking expensive.

**May 2: The Reasoning Ceiling Exposed and Design Patterns Evolve**: ARC-AGI-3 results deliver the most damning empirical critique of the LLM paradigm to date. GPT-5.5 (0.43%) and Claude Opus 4.7 (0.18%) — models that dominate SWE-bench — score below 1% on interactive reasoning puzzles humans solve effortlessly. The three systematic errors identified (failure to form world models, incorrect environment mapping to known games, carrying false theories forward) reveal LLMs don't reason about novel situations — they pattern-match to the nearest memorized template. This lands the same week David Silver's RL-native startup raised $1.1B, and the market is already pricing in a post-LLM paradigm. Meanwhile, Mistral Medium 3.5 introduces a design pattern worth watching: one 128B dense model with a reasoning-effort toggle per request, eliminating the need for separate chat/reasoning model variants. The 77.6% SWE-bench score is solid but not category-defining; the real bet is on the vertically integrated Vibe cloud coding agents bundled with the release.

## Connections
- [[entities/arc-agi-3]] — The benchmark that exposed the LLM reasoning ceiling: GPT-5.5 0.43%, Opus 4.7 0.18% vs near-100% human performance
- [[entities/mistral-medium-3-5]] — 128B dense model with reasoning-effort toggle; one-model-for-all design pattern challenges the multi-model approach
- [[entities/symphony]] — OpenAI's Codex orchestration spec formalizes "agent-as-employee" model; 15K+ stars signals industry convergence
- [[entities/context-mode]] — 98% context reduction MCP server; solves the noise problem that continuous agent execution creates
- [[sources/anthropic]] — Claude Mythos developed and leaked by Anthropic; Opus 4.7 release; Project Glasswing
- [[sources/openai]] — GPT-5.4 family, GPT-5.5 release, Spud completion, GPT-5.4-Cyber, GPT-Rosalind
- [[sources/google]] — Gemma 4 Apache 2.0 release, Gemini 3.1 Pro near-tie with Claude Opus 4.6, TPU 8th gen
- [[entities/claude-mythos]] — Central to this period; too dangerous to release publicly
- [[entities/claude-opus-4-7]] — Anthropic's latest flagship with 87.6% SWE-bench; powers Claude Security
- [[entities/claude-design]] — Anthropic's direct challenge to Figma's design workflow
- [[entities/gpt-5.4]] — OpenAI's flagship model family with Thinking, Mini, Nano, Cyber variants
- [[entities/gpt-5.5]] — OpenAI's latest model with "super app" integration vision
- [[entities/gpt-rosalind]] — OpenAI's life sciences domain model
- [[entities/gemma-4]] — Google's first fully permissive open model, ranked #3 on Arena
- [[entities/deepseek-v4]] — DeepSeek's latest with 1M context and open weights, Tencent/Alibaba investment talks
- [[entities/claude-security]] — Anthropic's defensive security scanner built on Opus 4.7; native to Claude Code workflow
- [[entities/gb300]] — NVIDIA Blackwell Ultra mass production; 35x lower cost/token for agentic AI workloads
- [[entities/guard-act]] — Senate bill with criminal penalties for AI chatbot conduct; creates liability precedent
- [[ideas/safety-restricted-releases]] — Claude Mythos established the precedent; GPT-5.5 Cyber follows same pattern
- [[ideas/us-china-ai-fragmentation]] — Stanford HAI confirms gap has collapsed
- [[ideas/institutional-gap]] — May 1 exemplifies GUARD Act criminal penalties and liability exceeding Section 230 frameworks
- [[entities/ibm-bob]] — Multi-model orchestration routing tasks to best-fit model challenges the "one best model" assumption; Claude, Mistral, and Granite each win different task categories
- [[entities/microsoft-legal-agent]] — Claude integration in Copilot proves no single model provider wins enterprise AI alone; multi-model support is becoming table stakes