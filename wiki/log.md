# Wiki Log

## [2026-05-05] wiki lint | comprehensive health check

**Pass 1 — Structural fixes:**
- Fixed broken `wikilink` references in historical log entries (converted `[[...]]` to code spans for non-existent targets in log.md)
- Merged duplicate entity `entities/spud-model.md` into `entities/gpt-5.5.md` (same model, codename vs released name); removed spud-model.md
- Redirected inbound links: `timelines/2026-03.md` and `sources/openai.md` now link to `entities/gpt-5.5` instead of `entities/spud-model`
- Updated `index.md`: removed spud-model entry, merged gpt-5.5 description to include codename "Spud", entity count corrected 72 → 71 → 72
- Verified all 123 content pages have corresponding .md files (6 topics, 20 sources, 3 timelines, 72 entities, 22 ideas)
- Verified no unlisted .md files exist in any section
- Verified zero broken wikilinks across all content pages (WIKI.md template examples excluded)
- Verified no orphan pages: all 122 content pages have at least one inbound link
- Verified no companies or people in entities/: all 72 entity types are valid (model, product, protocol, framework, repo, benchmark, legislation)

**Pass 2 — Wrong & duplicate information fixed:**
- Removed duplicate entity `spud-model` — kept richer `gpt-5.5.md` with ARC-AGI-3, Pentagon deployment, and Symphony connections
- Created missing entity `entities/pixelle-video.md` — AI-powered fully automated short video engine (10.5K stars); mentioned in `topics/github_trends` Patterns section but lacked a page
- Updated `topics/github_trends.md`: added `pixelle-video` to Connections; last_updated 2026-05-04 → 2026-05-05
- Updated `timelines/2026-03.md`: fixed grammar ("pressure" → "pressured") and replaced spud-model link with gpt-5.5; last_updated 2026-05-04 → 2026-05-05
- Updated `timelines/2026-05.md`: linked Pixelle-Video as wikilink instead of plain text; last_updated 2026-05-04 → 2026-05-05
- Updated `sources/openai.md`: removed redundant spud-model connection, enhanced gpt-5.5 connection with codename note; last_updated 2026-05-04 → 2026-05-05

**Pass 3 — Connection quality:**
- All 6 topic pages verified: each has ## Evolution and ## Patterns & Insights sections
- No bare "Related:", "See also:", or unannotated links found in any content page
- All connections verified: every link explains WHY and HOW things connect
- Created `entities/pixelle-video.md` with annotated connections to github_trends, agentic_ai, ruflo, automv, and mova

**Index rebuilt:**
- Topics: 6 (unchanged)
- Sources: 20 (unchanged)
- Timelines: 3 (unchanged)
- Entities: 72 (removed spud-model, added pixelle-video; net unchanged)
- Ideas: 22 (unchanged)
- Total content pages: 123 (6+20+3+72+22)

## [2026-05-04] ingest | 1 date

Dates processed: 2026-05-04
Topics updated: agentic_ai (agent verticalization: IBM Bob SDLC automation, Microsoft Legal Agent, Ruflo 100+ agent swarms, GitNexus knowledge graphs; new key developments and Patterns & Insights from May 3-4), ai_companies (Anthropic $1.5B Wall Street JV, Musk trial 2015-2018 emails, IBM Bob enterprise entry, AI music platform proliferation), ai_funding ($1.5B JV with Blackstone/Goldman Sachs/H&F as pre-IPO enterprise distribution strategy), ai_safety (Pentagon exclusion cost quantified: ~$200M vs $1.5B JV; market bifurcation with price tags on both sides), llm_models (multi-model support: Claude in Copilot, IBM Bob multi-model orchestration), github_trends (Ruflo 39.9K, GitNexus 35.4K, Pixelle-Video 10.5K; agent infrastructure goes enterprise-scale)
Sources updated: anthropic ($1.5B JV finalized, Pentagon exclusion cost quantified at ~$200M, Hegseth "ideological lunatic" quote, IPO rumored October 2026 at $60B+), openai (Musk trial 2015-2018 emails exposed, xAI confirmed using OpenAI models to train Grok, Musk advocated for-profit pivot in 2017), meta (ARI talent details: Xiaolong Wang ex-Nvidia/UCSD, Lerrel Pinto ex-NYU with Fauna→Amazon→Meta trajectory; "Android for robots" licensing strategy), microsoft (20M Copilot paid enterprise seats, Accenture 740K, agent mode default across Office, multi-model support with Claude, Legal Agent launched May 1 as first profession-specific vertical)
Sources created: ibm (IBM Bob: AI-first development partner, 80K+ internal users, multi-model orchestration, neutral alternative to Microsoft Copilot)
Timelines updated: 2026-05 (May 3-4: Anthropic $1.5B JV, Pentagon split quantified, agent verticalization evidence, Musk trial origin story autopsy, Microsoft Copilot 20M seats, AI music platform proliferation, IBM Bob, GitHub trending repos)
Entities created: ruflo (agent orchestration platform for Claude Code, 39.9K stars), gitnexus (MCP knowledge graph for codebases, 35.4K stars), ibm-bob (enterprise AI dev partner for full SDLC, 80K+ users), microsoft-legal-agent (profession-specific Copilot for contract review in Word)
Ideas created: agent-verticalization (agent layer consolidating into profession-specific platforms; moat shifts from model quality to workflow understanding)
Ideas updated: military-ai-divide (strengthened with $200M exclusion cost and $1.5B JV contrast — both sides of military-safety split now have quantified economics)

Chat session insights applied: All three prior chat sessions (28c7d4fb, 2fe64ce0, d1cce567) were already applied in previous ingests (Apr 23-26 news, Google Cloud Next details, AI layoff patterns). Today's news provides the latest chapter in the structural narratives those sessions identified: the military-safety bifurcation (session 28c7d4fb noted ai_safety needed updates), agent-layer maturation (session 2fe64ce0 discussed Claude Code quality issues and AI employment shifts), and Google's defense pivot (session d1cce567 asked about Google Cloud Next — today's Pentagon expansion completes the defense arc from Project Maven protests to full integration).

## [2026-05-04] wiki lint | comprehensive health check

**Pass 1 — Structural fixes:**
- Verified all 117 pages listed in index.md have corresponding .md files (6 topics, 19 sources, 3 timelines, 68 entities, 21 ideas)
- Verified no unlisted .md files exist in any section
- Verified all 803 wikilinks across content pages resolve correctly (broken links only in WIKI.md templates and log.md historical fix records)
- Verified no orphan pages: all 117 content pages have at least one inbound link
- Verified no companies or people in entities/: all 68 entity types are valid (model, product, protocol, framework, repo, benchmark, legislation)

**Pass 2 — Wrong & duplicate information fixed:**
- Fixed `timelines/2026-03.md`: Removed bare wikilinks at paragraph ends (now annotated in narrative); corrected "Gemini 3.1 Flash Live" → "Gemini 3.1 Flash TTS" in Connections; updated last_updated from 2026-04-16 → 2026-05-04
- Updated `entities/gpt-5.5.md`: Added ARC-AGI-3 0.43% score, Pentagon IL6/IL7 deployment, GPT-5.5 Cyber May 1 restrictions, and Symphony orchestration connections; last_updated 2026-04-27 → 2026-05-04
- Updated `entities/mimo-v2-pro.md`: Noted Opus 4.6 superseded by Opus 4.7; last_updated 2026-04-16 → 2026-05-04
- Updated `entities/muse-spark.md`: Enhanced significance with workforce restructuring context; last_updated 2026-04-16 → 2026-05-04
- Updated `entities/spud-model.md`: last_updated 2026-04-27 → 2026-05-04
- Updated `sources/spacex.md`: last_updated 2026-04-23 → 2026-05-04
- Updated `sources/alibaba.md`: Added Qwen 3.6 SWE-Bench benchmark context; last_updated 2026-04-25 → 2026-05-04
- Updated `sources/deepseek.md`: Added V4 Flash 100x pricing context and commodity inference fragmentation; last_updated 2026-04-25 → 2026-05-04
- Bumped last_updated dates for entities with no content changes but verified as current: deepgemm (2026-04-23→2026-05-04), mercury-agent (2026-04-23→2026-05-04), cc-design (2026-04-23→2026-05-04), web-design-skill (2026-04-23→2026-05-04)

**Pass 3 — Connection quality:**
- Rewrote bare wikilinks in `timelines/2026-03.md` as annotated narrative connections (Vera Rubin, MiMo-V2-Pro, DeepSeek, Gemini 3.1 Flash TTS)
- Enhanced connections in `entities/mimo-v2-pro.md`: Added china-efficiency-advantage link and "stealth launch" pattern annotation
- Enhanced connections in `entities/muse-spark.md`: Added ai-job-displacement link and proprietary pivot context
- Added connections to `sources/xai.md`: Now links to spacex (parent company), grok-voice-think-fast-1-0 (product), openai (distillation source)
- Updated `ideas/safety-restricted-releases.md`: Added ARC-AGI-3 context, May 1 OpenAI Cyber restriction convergence; last_updated 2026-04-27 → 2026-05-04
- Updated `ideas/ai-governance-urgency.md`: Added GUARD Act passage, Five Eyes guidance, Pentagon deployment contrast; last_updated 2026-04-27 → 2026-05-04
- Updated `ideas/agent-economics.md`: Added Netomi $110M, agent infrastructure funding wave, and Symphony orchestration; last_updated 2026-04-29 → 2026-05-04
- All 6 topic pages verified: each has ## Evolution and ## Patterns & Insights sections
- No bare "Related:" or "See also:" connections found in any content page
- All entity pages verified: each has annotated connections explaining WHY

**Index rebuilt:**
- Topics: 6 (unchanged)
- Sources: 19 (unchanged)
- Timelines: 3 (unchanged)
- Entities: 68 (unchanged)
- Ideas: 21 (unchanged)
- Total content pages: 117 (6+19+3+68+21)

## [2026-05-03] ingest | 1 date

Dates processed: 2026-05-03
Topics updated: llm_models (ARC-AGI-3 <1% exposes reasoning ceiling, Mistral Medium 3.5 reasoning toggle design pattern, May 2 reasoning ceiling evolution section), ai_companies (May 2 fault lines: Pentagon expanded contracts with "any lawful operational use," Sam Altman's three pillars/"personal AGI," Meta "Android for robots" strategy, Mistral Vibe vertical integration, Oscars AI ban), ai_funding (Netomi $110M agentic CX, agent infrastructure funding wave: Standard Intelligence $75M + Actively $45M + Parallel $100M at $2B), github_trends (Serena 23.8K semantic code MCP, MOVA 972 video+audio, AutoMV 104 multi-agent music videos), ai_safety (dual crisis: dangerously capable Mythos + incapable of reasoning per ARC-AGI-3; "any lawful use" at scale with 1M+ personnel; EU tightening vs Pentagon expansion), agentic_ai (Serena semantic infrastructure, Netomi 40K req/s enterprise CX, Mistral Vibe integration, agent stack funded layer by layer)
Sources updated: openai (three pillars strategy, ARC-AGI-3 0.43%, Pentagon expanded contracts), anthropic (Pentagon conspicuous absence, ARC-AGI-3 0.18%, "any lawful use" lawsuit continues), google (Pentagon expansion — complete Project Maven reversal, 1M+ defense personnel), meta (ARI "Android for robots" licensing strategy, $25B bonds), mistral (Medium 3.5 + Vibe launch, reasoning toggle, vertical integration strategy)
Sources created: netomi (agentic CX platform, $110M Series C led by Accenture Ventures, 40K req/s)
Timelines updated: 2026-05 (Week 1 — May 2: ARC-AGI-3 bombshell, Pentagon "AI-first" formalized, Mistral Medium 3.5 + Vibe, Meta robotics platform strategy, Sam Altman's three pillars, Oscars AI ban, agent infrastructure funding wave, GitHub trending repos)
Entities created: arc-agi-3 (benchmark: GPT-5.5 0.43%, Opus 4.7 0.18%; exposed LLMs don't reason — they retrieve), mistral-medium-3-5 (128B dense model with reasoning-effort toggle; SWE-Bench 77.6%, AIME25 86.3%), vibe (Mistral's vertically integrated cloud coding agents), serena (MCP semantic code toolkit across 40+ languages; 23.8K stars; symbol-level editing via LSP), mova (synchronized video-audio generation foundation model; 972 stars), automv (multi-agent music video generator; $10-20 per MV; 104 stars)
Ideas created: ai-creative-regulation (Oscars ban codifies "regulate creative core, leave tool layer alone" as global regulatory template)
Ideas updated: military-ai-divide (added Google Project Maven reversal evidence, Meta absence from coalition, "any lawful use" at 1M+ personnel scale), rl-vs-llm-paradigm (added ARC-AGI-3 results as strongest empirical evidence for Silver's thesis)

Chat session insights applied: Session 28c7d4fb (Apr 23) noted ai_safety topic needed Qihoo 360 and Bank of England updates — both already present from prior ingests. Session 2fe64ce0 (Apr 25-26) discussed AI employment structural changes — ARI "Android for robots" extends displacement to physical labor, now reflected in ai_job_displacement idea. Session d1cce567 asked about Google Cloud Next — Google's inclusion in Pentagon coalition with "any lawful use" clause and the 2018 Project Maven reversal provides the defense context that complements the Cloud Next product announcements. All three sessions confirm the military-safety divide as the defining structural tension of this period.

## [2026-05-03] wiki lint | comprehensive health check

**Pass 1 — Structural fixes:**
- Fixed broken `wikilink` `entities/gpt-5-4-cyber` → `entities/gpt-5.4-cyber` in timelines/2026-04.md (hyphens vs dots)
- Fixed broken `wikilink` `entities/five-eyes-agent-security-guidance` → `topics/ai_safety` in ideas/military-ai-divide.md (entity never existed; Five Eyes guidance is discussed in ai_safety topic)
- Verified no orphan pages: all 103 pages have at least one inbound link
- Verified no companies or people in entities/: all 56 original entity types are valid (model, product, protocol, framework, repo, legislation)

**Pass 2 — Wrong/stale information fixed:**
- Updated `entities/gpt-5.4.md` — last_updated from 2026-04-16 → 2026-04-20 (content referenced April 20 TAC expansion)
- Updated `entities/claude-code.md` — last_updated from 2026-04-16 → 2026-05-01; added Claude Security integration, Karpathy skills phenomenon, quality regression context
- Updated `entities/claude-opus-4-7.md` — Added Claude Security connection (powers the defensive scanner)
- Updated `entities/mcp-protocol.md` — last_updated from 2026-04-23 → 2026-05-02; Key Facts now shows 150M+ total installs (was only showing 97M+ monthly)

**Pass 3 — Connection quality:**
- All 6 topic pages verified: each has ## Evolution and ## Patterns & Insights sections
- No bare "Related:" or "See also:" connections found in any content page (only in WIKI.md as counter-examples)
- Created 6 new entity pages for significant named things referenced across multiple pages but lacking their own page:
  - `entities/agent-365.md` — Microsoft's $15/user/month AI agent product
  - `entities/m365-e7.md` — Microsoft's $99/user/month enterprise AI bundle
  - `entities/cursor.md` — AI coding IDE with $60B SpaceX investment
  - `entities/terminal-bench-2.md` — Benchmark: GPT-5.5 82.7% vs Claude Opus 4.7 58.6%
  - `entities/ari.md` — Meta's humanoid robotics acquisition
  - `entities/gemini-3-deep-think.md` — Google's advanced reasoning mode
- Added inbound links to new entities from sources/microsoft.md, sources/spacex.md, sources/meta.md

**Index rebuilt:**
- Topics: 6 (unchanged)
- Sources: 18 (unchanged)
- Timelines: 3 (unchanged)
- Entities: 56 → 62 (added agent-365, ari, cursor, gemini-3-deep-think, m365-e7, terminal-bench-2)
- Ideas: 20 (unchanged)
- Total files: 109 (6+18+3+62+20 + WIKI.md + index.md + log.md)

## [2026-05-02] ingest | 1 date

Dates processed: 2026-05-02
Topics updated: llm_models (Symphony orchestration spec, context-mode optimization, andrej-karpathy-skills 105K stars), ai_companies (Pentagon 8-company AI coalition — Anthropic excluded as "supply chain risk"; Anthropic ~$900B valuation; Meta ARI robotics acquisition; Five Eyes joint AI agent security guidance; Ineffable $5.1B valuation; Symphony open-sourcing), ai_funding (Anthropic $50B at $900B+, Ineffable $1.1B at $5.1B, Pentagon contracts worth billions), ai_safety (Pentagon exclusion of Anthropic, Five Eyes first joint agent security guidance, Musk distillation admission under oath), agentic_ai (Symphony orchestration at fleet scale, Five Eyes agent governance framework, context-mode 98% context reduction), github_trends (andrej-karpathy-skills 105K, context-mode 11.9K, ds2api 3.1K)
Sources updated: anthropic (Pentagon exclusion as "supply chain risk," $50B at $900B+ valuation), openai (Pentagon classified network inclusion, Symphony orchestration spec), google (Pentagon classified network inclusion), meta (ARI humanoid robotics acquisition), microsoft (Pentagon classified network inclusion, Agent Governance Toolkit open-source), nvidia (Pentagon classified network inclusion, Ineffable investment participation), xai (Pentagon classified network inclusion), ineffable-intelligence ($5.1B valuation confirmed, Silver's "LLMs are fossil fuel" thesis)
Timelines updated: 2026-05 (Week 1 — May 1 extended: Pentagon coalition, Anthropic exclusion, ARI acquisition, Five Eyes guidance, Musk courtroom admission, Ineffable RL bet, Symphony spec; May 2 GitHub trends)
Entities created: symphony (OpenAI Codex orchestration spec; 15K+ stars; agent-as-employee model), andrej-karpathy-skills (105K stars; single CLAUDE.md with 4 principles; "configuration over code"), context-mode (11.9K stars; MCP server for 98% context reduction; 12+ platforms)
Ideas created: military-ai-divide (May 1, 2026: commercial AI formally splits into Pentagon's 8-company coalition vs Anthropic's safety-first exclusion), rl-vs-llm-paradigm (David Silver's $5.1B bet that RL superlearning will make LLM scaling obsolete)
Ideas updated: institutional-gap (added Five Eyes guidance vs Pentagon deployment same-day contrast — governance frameworks published for technology deployed yesterday)

Chat session insights applied: The Apr 23 session requested more Google Cloud Next details — today's Five Eyes guidance (May 1) is the governance counterpart to the Cloud Next agent announcements, and Symphony (April 27, open-sourced) extends the agent orchestration narrative. The Apr 25 session highlighted "92K+ tech layoffs" as a recurring pattern — Meta's ARI acquisition extends the displacement thesis from digital to physical labor. The Apr 25 session asked specifically about Google news — Google's inclusion in the Pentagon 8-company coalition extends the defense pivot beyond the previously documented April 30 Pentagon deal. Session d1cce567 specifically asked about Google Cloud Next — the Five Eyes framework and Symphony orchestration spec both connect to the Cloud Next announcements (Gemini Enterprise Agent Platform, TPU 8th gen) as the operational infrastructure catching up to the product announcements.

## [2026-05-02] wiki lint | structural + connection fixes

**Structural fixes:**
- Created missing entity `entities/claude-opus-4-6.md` (index listed it but file was missing)
- Fixed broken `wikilink` `entities/gemini-3-1-flash-live` → `entities/gemini-3-1-flash-tts` in timelines/2026-03.md
- Fixed broken `wikilink` `ideas/infrastructure-bottleneck` → `ideas/efficiency-frontier` in topics/ai_funding.md (infrastructure-bottleneck page never existed)
- Removed phantom link `sources/crowdstrike` from entities/claude-security.md (crowdstrike is not a source page)

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
- Fixed 4 broken `wikilinks`: mozilla, cognition, alibaba, efficiency-frontier, ai-job-displacement had no corresponding pages

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
- Fixed broken link `entities/blackwell` → `entities/gb300` in sources/nvidia.md
- Fixed broken link `entities/vast-data` → `sources/vast-data` in sources/nvidia.md
- Fixed broken link `entities/openhands` → `entities/openhands-sdk` in entities/openhands-sdk.md
- Fixed broken link `entities/Claude-code` → `entities/claude-code` in entities/mercury-agent.md (case mismatch)
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
