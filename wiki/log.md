# Wiki Log

## [2026-05-02] wiki lint | structural + connection fixes

**Structural fixes:**
- Created missing entity `entities/claude-opus-4-6.md` (index listed it but file was missing)
- Fixed broken [[wikilink]] `[[entities/gemini-3-1-flash-live]]` → `[[entities/gemini-3-1-flash-tts]]` in timelines/2026-03.md
- Fixed broken [[wikilink]] `[[ideas/infrastructure-bottleneck]]` → `[[ideas/efficiency-frontier]]` in topics/ai_funding.md (infrastructure-bottleneck page never existed)
- Removed phantom link `[[sources/crowdstrike]]` from entities/claude-security.md (crowdstrike is not a source page)

**Connection quality improvements:**
- Rewrote entity connections with WHY annotations: llama-4, gemma-4, openclaw
- Fixed link to claude-opus-4-6 from claude-opus-4-7 (predecessor relationship now correct, link now exists)

**Index rebuilt:**
- Topics: 6 (unchanged)
- Sources: 16 (unchanged)
- Timelines: 3 (unchanged)
- Entities: 53 (added claude-opus-4-6)
- Ideas: 17 (unchanged)

## [2026-05-01] ingest | 1 date

Dates processed: 2026-05-01
Topics updated: llm_models (May 1 overview, GB300 Blackwell Ultra mass production, Claude Security launch, Microsoft E7/Agent 365 GA, GUARD Act), ai_companies (Meta 8,000 layoffs May 20, Microsoft E7 lock-in, GUARD Act unanimous passage, Gemini automotive rollout), ai_funding (Meta capex $125-145B, GB300 mass production May delivery), ai_safety (Claude Security defensive pivot, GPT-5.5 Cyber restrictions after mocking Anthropic, GUARD Act criminal penalties), agentic_ai (E7/Agent 365 GA, GB300 35x cost reduction, Gemini automotive), github_trends (harmonist, CoreCoder, open-agent-sdk-go trending)
Sources updated: meta (8,000 layoffs May 20, $125-145B capex, MCI surveillance), microsoft (E7/Agent 365 GA), anthropic (Claude Security launch), openai (GPT-5.5 Cyber restrictions, Musk distillation admission), google (Gemini automotive ~4M vehicles), nvidia (GB300 mass production), xai (Musk distillation admission under oath)
Timelines created: 2026-05 (Week 1 May 1-7)
Entities created: claude-security (Opus 4.7-powered security scanner native to Claude Code), gb300 (Blackwell Ultra mass production, 35x lower cost/token), guard-act (Senate bill criminal penalties for AI chatbot conduct), harmonist (186 specialist agents, zero third-party deps, 949 stars), corecoder (~1,400 lines Python inspired by Claude Code, 652 stars), open-agent-sdk-go (Go SDK for AI agents, 151 stars)
Ideas created: enterprise-ai-lock-in (Microsoft E7 bundle makes AI governance inseparable from Microsoft stack), distillation-hypocrisy (Musk admitted xAI distilled from OpenAI while suing OpenAI for betrayal)
Ideas updated: institutional-gap (added GUARD Act unanimous passage, Musk distillation testimony)

Chat session insights applied: The Apr 23 session noted "wiki freshness" on Claude Mythos — today's Claude Security launch directly addresses the defensive pivot narrative. The Apr 25 session noted "today's insight explicitly calls out the Mythos escalation" — the connection between Mythos restrictions and Claude Security is now explicit in the wiki. Apr 26 session noted "AI coding tools as growth driver" — GB300 35x cost reduction now enables that growth at scale.

Dates processed: 2026-04-29
Topics updated: llm_models (April 29 institutional contradictions pattern: Musk vs Altman Day 3 profit emails, Goldman Sachs/Morgan Stanley threaten IPO withdrawal, EU €800M Meta fine, TSMC 3nm yield collapse to 52%, Mistral Ultra 2 EU positioning), ai_companies (TSMC supply cliff, Mistral Ultra 2 enterprise entry, Ineffable 50 researchers in 72 hours), ai_safety (EU AI Act first fine, TSMC physics reality check), ai_funding (updated with TSMC yield crisis implications), github_trends (Copilot Agent Tier $49/agent/month, TradingAgents 54.6K)
Sources created: mistral (Mistral AI EU positioning), tsmc (3nm yield crisis), github (Copilot Agent Tier monetization)
Sources updated: openai (Day 3 2017 profit emails, Goldman Sachs/Morgan Stanley threaten IPO withdrawal), meta (EU €800M AI Act fine)
Timelines updated: 2026-04 (Week 4, April 29 entry)
Entities created: mistral-ultra-2 (78.4% SWE-bench, €2/M, EU data residency), copilot-agent-tier ($49/agent/month, first platform monetization of agent-scale usage)
Entities updated: ineffable-intelligence (50 researchers hired in 72 hours including AlphaGo/AlphaFold/GPT-4 paper authors)
Ideas updated: institutional-gap (added TSMC yield crisis, EU AI Act fine, 2017 profit email evidence)
Chat session insights applied: Prior sessions noted Claude Code quality issues (resolved Apr 24), Google Cloud Next specifics needed — Mistral Ultra 2 EU positioning and GitHub Copilot Agent Tier directly address the question of what happens when institutional frameworks (legal, regulatory, physical) don't keep pace with capability deployment

**Structural fixes:**
- Removed duplicate entity `gpt-5-5.md` (had 2 files: gpt-5-5.md and gpt-5.5.md) — kept richer gpt-5.5.md with Spud codename, benchmark scores, 49-day release cycle analysis
- Fixed 4 broken [[wikilinks]]: mozilla, cognition, alibaba, efficiency-frontier, ai-job-displacement had no corresponding pages

**New pages created:**
- `sources/cognition.md` — Cognition AI ($25B talks, Devin creator)
- `sources/alibaba.md` — Alibaba (DeepSeek investment talks, Qwen 3.6)
- `sources/mozilla.md` — Mozilla (Thunderbolt enterprise AI client)
- `entities/gemini-3-1-pro.md` — Fixed file that contained wrong slug (was "Claude Opus 4.6" content with gemini-3-1-pro filename)

**New idea pages created:**
- `ideas/efficiency-frontier.md` — Qwen 3.6 efficiency breakthrough; efficient models achieving domain dominance
- `ideas/ai-job-displacement.md` — 92K+ layoffs; Meta 65/75 mandate; governance gap

**Connection quality improvements:**
- `entities/thunderbolt.md` — Rewrote connections with WHY annotations (Mozilla created Thunderbolt as enterprise self-hosted alternative, addresses data privacy concerns)

## [2026-04-30] ingest | 1 date

Dates processed: 2026-04-30
Topics updated: llm_models (April 30 bifurcation: 10GW compute milestone, Anthropic $900B valuation, DeepSeek V4 Flash $0.14/$0.28/M at 78% SWE-bench, Qwen 3.6 73.4% on RTX 4090, Google Pentagon deal, Apple Gemini Siri), ai_companies (Google defense pivot, Apple model outsourcing, Big Tech earnings divergence), ai_funding (OpenAI 10GW energy moat, Anthropic $50B raise trajectory), github_trends (plannotator 4.8K, cc-sdd 3.2K, PraisonAI 7K — workforce-in-a-box pattern)
Sources updated: openai (10GW compute milestone), anthropic ($50B raise at $900B), google (Pentagon classified military AI deal)
Timelines updated: 2026-04 (Week 5, April 30 entry: bifurcation week summary)
Entities updated: deepseek-v4 (added V4-Flash $0.14/$0.28/M variant, 100x price gap revelation, updated significance)
Ideas created: commodity-inference-fragmentation (premium reasoning vs commodity inference 100x cost gap)
Chat session insights applied: Session 28c7d4fb noted [[topics/ai_safety]] may need updating after Bank of England escalation and Qihoo 360 findings — not addressed in this ingest; session 2fe64ce0 confirmed Claude Code performance issues (fixed Apr 24); session d1cce56 asked about Google Cloud Next specifics — TPU 8th gen and Gemini Enterprise Agent Platform were already documented
- `entities/qwen-3-6.md` — Rewrote connections explaining WHY (efficiency breakthrough confirms China 23x efficiency advantage, links to china-efficiency-advantage)

**index.md updated:** Added cognition, alibaba, mozilla sources; added efficiency-frontier and ai-job-displacement ideas

## [2026-04-28] ingest | 1 date

Dates processed: 2026-04-28
Topics updated: llm_models (added enterprise cost war pattern, OpenAI Q1 revenue miss, DeepSeek V4-Pro-Max $1.74/M pricing), ai_companies (Claude eating OpenAI's enterprise lunch, Ineffable $1.1B seed), ai_funding (Big Tech $65B to Anthropic, Ineffable seed), ai_safety (neuromorphic chip physics simulation capability)
Sources updated: openai (Q1 revenue miss, IPO timing critical), google ($40B Anthropic investment validated Claude trajectory), anthropic (updated)
Timelines updated: 2026-04 (Week 4, April 28 entry)
Entities created: ineffable-intelligence (David Silver $1.1B seed), agentswift (iOS builder agent), agent-context (VS Code symlink context extension), future-agi (agent evaluation platform, 482 stars)
Entities updated: deepseek-v4 (added $1.74/M cost-performance leader note)
Chat session insights applied: Previous sessions noted Claude Code quality issues and Google Cloud Next details — today's news confirms Claude winning enterprise workflows validates Anthropic's trajectory; DeepSeek V4 cost data from prior days' context integrated

## [2026-04-27] ingest | 1 date

Dates processed: 2026-04-27
Topics updated: llm_models (added institutional stress test pattern), ai_companies (Meta 65/75 mandate, Musk vs Altman trial), ai_funding (GitHub agent-scale economics crisis), github_trends (275M commits/week, 17M PRs from AI agents), ai_safety (institutional gap widening)
Sources updated: openai (Musk vs Altman court proceedings), anthropic (updated), google (updated), meta (65/75 mandate)
Timelines updated: 2026-04 (Week 4, April 27 entry)
Entities created: gpt-5.5
Entities updated: safety-restricted-releases (new evidence from GPT-5.5 procurement lock-in analysis)
Ideas created: institutional-gap
Chat session insights applied: Session noted AI governance urgency and safety-restricted-releases needed strengthening — reflected in new institutional-gap idea and updated safety-restricted-releases connections

## [2026-04-26] ingest | 1 date

Dates processed: 2026-04-26
Topics updated: llm_models (added capability regression and voice specialization patterns), ai_funding (Google ~25% global compute, regulatory scrutiny), agentic_ai (Project Deal, Claude Code backlash), ai_safety (military-grade AI specialization)
Sources updated: anthropic (Project Deal, Claude Code backlash), openai (GPT-5.5 vs DeepSeek V4 same day), google (Epoch AI compute data), meta (workforce cuts), xai (grok-voice launch)
Timelines updated: 2026-04 (Week 4, April 26 entry)
Entities created: grok-voice-think-fast-1-0, project-deal, ml-intern
Ideas created: agent-e-commerce, voice-agent-battleground
Chat session insights applied: 2026-04-25 session noted Claude Code quality issues — reflected in agentic_ai topic and anthropic source update

## [2026-04-25] ingest | 1 date

Dates processed: 2026-04-25
Topics updated: llm_models, ai_companies, ai_funding, github_trends, ai_safety
Sources updated: openai, anthropic, google, deepseek
Timelines updated: 2026-04 (Week 4)
Entities created: deepseek-v4, nemo-claw, openhands-sdk, scientific-agent-skills
Entities updated: gpt-5.5 (already existed from Apr 23 news)
Ideas updated: (from chat session notes: ai_safety connections strengthened)

## [2026-04-24] ingest | 1 date

Dates processed: 2026-04-24
Topics updated: llm_models, ai_companies, ai_funding, github_trends, ai_safety
Sources updated: openai, meta, microsoft, anthropic
Timelines updated: 2026-04 (Week 4)
Entities created: gpt-5.5, cambridge-neuromorphic-chip
Ideas created: ai-governance-urgency

## [2026-04-23] ingest | 3 dates

Dates processed: 2026-04-21, 2026-04-22, 2026-04-23
Topics updated: llm_models, ai_companies, ai_funding, github_trends, ai_safety, agentic_ai
Sources updated: anthropic, openai, google, spacex, meta
Timelines updated: 2026-04 (Week 4)
Entities created: deepgemm, gemini-enterprise-agent-platform, tpu-8th-gen, vast-data, mercury-agent
Entities updated: claude-mythos, mcp-protocol, gpt-5.4-cyber
Ideas updated: safety-restricted-releases

## [2026-04-20] ingest | 4 dates

Dates processed: 2026-04-17, 2026-04-18, 2026-04-19, 2026-04-20
Topics updated: llm_models, ai_companies, ai_funding, github_trends, ai_safety, agentic_ai
Sources updated: anthropic, openai, google, meta, nvidia
Timelines updated: 2026-04
Entities created: claude-opus-4-7, claude-design, gpt-rosalind, ising, thunderbolt, perplexity-computer, qwen-3-6, a2a-protocol, gemini-3-1-flash-tts
Entities updated: claude-mythos
Ideas created: application-layer-shift, china-efficiency-advantage, quantum-ai-emergence, local-ai-computing

## [2026-04-16] ingest | 31 dates

Dates processed: 2026-03-17 through 2026-04-16
Topics updated: llm_models, ai_companies, ai_funding, github_trends, ai_safety, agentic_ai
Sources updated: anthropic, openai, google, meta, nvidia, deepseek, xai, microsoft
Timelines updated: 2026-03, 2026-04
Entities created: claude-mythos, claude-code, claude-opus-4-6, gpt-5.4, gpt-5.4-cyber, spud-model, gemma-4, llama-4, muse-spark, mimo-v2-pro, project-glasswing, codex, mcp-protocol, openclaw, claw-code, vera-rubin
Ideas created: safety-restricted-releases, peer-preservation, agent-democratization, us-china-ai-fragmentation

## [2026-05-02] wiki lint | comprehensive health check

**Pass 1 — Structural fixes:**
- Renamed `entities/gpt-5-4.md` → `entities/gpt-5.4.md` (filename used hyphens, all 5 wikilinks used dots)
- Renamed `entities/gpt-5-4-cyber.md` → `entities/gpt-5.4-cyber.md` (same issue, 4 broken links)
- Moved `entities/ineffable-intelligence.md` → `sources/ineffable-intelligence.md` (company in entities)
- Fixed broken link `[[entities/blackwell]]` → `[[entities/gb300]]` in sources/nvidia.md
- Fixed broken link `[[entities/vast-data]]` → `[[sources/vast-data]]` in sources/nvidia.md
- Fixed broken link `[[entities/openhands]]` → `[[entities/openhands-sdk]]` in entities/openhands-sdk.md
- Fixed broken link `[[entities/Claude-code]]` → `[[entities/claude-code]]` in entities/mercury-agent.md (case mismatch)
- Fixed wrong link `[[sources/deepseek]]` → `[[sources/alibaba]]` in timelines/2026-04.md (Alibaba Qwen line linked to deepseek)
- Created missing page `sources/perplexity.md` (listed in index but file didn't exist)
- Created missing page `entities/gemini-cli.md` (referenced by google source and gemini-enterprise-agent-platform)
- Created missing page `ideas/agent-economics.md` (referenced by copilot-agent-tier and github source)
- Removed duplicate self-referencing link in entities/openhands-sdk.md

**Pass 2 — Wrong/stale information fixed:**
- Updated `entities/spud-model.md` — Spud was released as GPT-5.5 on April 23; old text implied unreleased
- Updated `entities/gpt-5.4-cyber.md` — Added TAC expansion (April 20) and May 1 OpenAI reversal after mocking Anthropic
- Updated `entities/claude-mythos.md` — last_updated from 2026-04-23 → 2026-05-01
- Updated `entities/claude-opus-4-7.md` — last_updated from 2026-04-20 → 2026-05-01 (now powers Claude Security)
- Fixed `entities/guard-act.md` — type from "product" → "legislation"
- Reformatted `sources/ineffable-intelligence.md` — proper source page format with Timeline and Key Relationships
- Fixed typo "OpenAI'sGPT-5.5" → "OpenAI's GPT-5.5" in topics/llm_models.md

**Pass 3 — Connection quality:**
- Fixed wrong link target in ideas/safety-restricted-releases.md — `[[topics/llm_models]]` → `[[ideas/institutional-gap]]` (connection was about institutional gap, not LLM models)
- All topic pages verified: each has ## Evolution and ## Patterns & Insights sections
- All connections verified: no bare links or "Related:/See also:" patterns found

**Index rebuilt:**
- Sources: 16 → 18 (added perplexity, ineffable-intelligence; fixed count from 16 to match actual 18)
- Entities: 53 (removed ineffable-intelligence, added gemini-cli; net unchanged)
- Ideas: 17 → 18 (added agent-economics)
- Timelines: 3 (unchanged)
- Topics: 6 (unchanged)
- Total files: 98 (6+18+3+53+18 + WIKI.md + index.md + log.md)
