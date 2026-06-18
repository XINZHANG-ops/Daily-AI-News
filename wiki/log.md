## [2026-06-10] lint

Pre-scan found 4 broken links. Repairs:

**Broken links fixed (4):**
- `entities/tilert` → `[[entities/cerebras]]` rewritten to `[[sources/cerebras]]`
- `entities/tilert` → `[[entities/groq]]` rewritten to `[[sources/groq]]`
- `topics/ai_infrastructure` → `[[entities/cerebras]]` rewritten to `[[sources/cerebras]]`
- `topics/ai_infrastructure` → `[[entities/groq]]` rewritten to `[[sources/groq]]`

**New sources created (2):**
- `sources/cerebras` — AI hardware company behind Wafer-Scale Engine (WSE-3); ~969 TPS peak was the bar Xiaomi + TileRT cleared on commodity 8-GPU on June 8, 2026
- `sources/groq` — AI hardware company founded by Jonathan Ross (ex-Google TPU architect); Groq LPU peaked at ~750 TPS, undercut by Xiaomi + TileRT achieving ~1200 TPS on commodity hardware

**Index updates:**
- `wiki/index.md` Sources count incremented from 51 → 53 with descriptive entries for both new sources

**Full wiki audit results (357 files, 3,383 links):**
- Broken links: 0
- Orphan pages: 0
- Empty/stub pages: 0
- All topic pages have ## Evolution and ## Patterns & Insights sections
- No bare "Related:" or "See also:" annotations
- No company/people misclassified in entities/

## [2026-06-07] ingest | 1 date

Dates processed: 2026-06-07
Topics updated: llm_models, agentic_ai, ai_companies, ai_safety, github_trends
Sources updated: anthropic, microsoft, nvidia, xai, openai, google
Entities created: nemotron-3-ultra, maia-200, openai-lockdown-mode, nex-n2, hyperagents, goa
Entities updated: mai-family, grok-build, claude-mythos, project-glasswing
Ideas created: foundation-model-portfolio-war, agentic-developer-as-primary-end-user
Timelines updated: 2026-06 (June 4-7 portfolio war + agentic developer shift)

Key insights extracted:
- Microsoft dropped seven MAI models in a single day (June 6) co-designed with Maia 200 silicon — clearest signal yet that OpenAI partnership is hedge, not moat
- xAI's Grok Build 0.1 at $1/$2 per million tokens is 40-60% below Claude Code Opus 4.8, 80% below GPT-5.4-Codex
- NVIDIA Nemotron 3 Ultra (550B MoE, NVFP4 quantization) shifts to OpenMDW-1.1 license, weaponizing openness as CUDA moat
- Anthropic Glasswing expands to 150 orgs (NATO + Samsung), Mythos-class models promised "in the coming weeks"
- OpenAI Lockdown Mode is defensive posture after Meta Instagram breach; vs Anthropic's offensive Glasswing expansion
- Three GitHub repos same day (Nex-N2, HyperAgents, GoA) confirm agentic developer is primary end-user
- Idea created: "Foundation Model Portfolio War" — competition shifted from "best flagship" to "best portfolio"
- Idea created: "Agentic Developer as Primary End-User" — every product designed for an agent or a developer building agents
- MAI-Image-2.5 surpassing Nano Banana Pro on Arena is first major breach of Google's image generation lead

## [2026-06-03] lint | wiki health check

Fixed broken links: entities/gbase.md: [[entities/openhands]] → [[entities/openhands-sdk]]; ideas/multi-turn-structural.md: removed invalid [[sources/cisco]] link
Fixed orphan pages: Added [[ideas/ai-accountability-precedent]] link from topics/ai_safety.md; Added [[entities/enisa]] link from topics/ai_security.md; Added [[ideas/multi-turn-structural]] link from topics/ai_security.md; Added [[entities/devin]] link from entities/windsurf-2.md
Updated index.md: Added missing pages - timelines/2026-06, ideas/multi-turn-structural, entities (gbase, mai-family, windows-agent-runtime); Counts: Timelines 3→4, Ideas 66→67, Entities 192→195

## [2026-06-02] ingest | 1 date

Dates processed: 2026-06-02
Topics updated: llm_models, ai_funding, ai_safety, agentic_ai
Sources updated: anthropic, openai, microsoft, google
Entities created: enisa, mai-family, windows-agent-runtime, gbase
Entities updated: gamma-world (stars), claude-mythos (ENISA access)
Ideas created: ai-accountability-precedent, multi-turn-structural
Timelines updated: 2026-06 (June 2 events)

## [2026-06-02] lint | wiki health check

Fixed broken links: [[entities/mcp]] → [[entities/mcp-protocol]] in synapse-ai.md, nano-brain.md; [[entities/nemoclaw]] → [[entities/nemo-claw]] in cosmos-3.md, physical_ai.md
Updated nemo-claw.md: Added May 2026 Agent Toolkit content (physical AI) while preserving March 2026 OpenClaw reference stack info
Verified all wikilinks: No broken links found
## [2026-06-01] lint | wiki health check

Fixed empty source pages (deleted stubs <10 lines): cepi, lawrence-livermore-national-laboratory, notion, rakuten, asana, johns-hopkins-apl
Fixed structure: moved entities/cognition (company type) to sources/, removed duplicate entities/cognition.md
Fixed broken wikilinks: updated timelines/2026-05.md, entities/devin.md, entities/claude-managed-agents.md, entities/gpt-rosalind.md
Fixed index.md: Sources 54→45, Ideas 68→66; added missing entries (geely, waymo, claude-managed-agents, claude-opus-4-8, devin, waymo-ojai); removed duplicates (eidolon-os, micron, samsung, sk-hynix)
Verified all counts match: Topics 8, Sources 45, Timelines 3, Entities 187, Ideas 66

## [2026-05-31] lint | wiki health check

Fixed orphan pages: Added [[entities/swe-bench]] link from topics/llm_models.md; Added [[entities/eidolon-os]] link from ideas/local-ai-computing.md
Added missing pages to index.md: entities (eidolon-os, qwen-3-7-max), sources (micron, samsung, sk-hynix), ideas (pricing-war, vertical-integration)
Updated index.md counts: Sources 43→46, Entities 182→184, Ideas 66→68
Added Patterns & Insights sections to topics missing them: ai_infrastructure, ai_security
Updated last_updated dates

## [2026-05-28] ingest | 1 date

Dates processed: 2026-05-28
Topics updated: llm_models, ai_companies, ai_funding, ai_infrastructure
Sources updated: anthropic, openai, spacex, microsoft, google, coinbase
Entities created: mai-image-2-5, base-mcp
Entities updated: mirage (stars/forks), natural-language-autoencoders (updated), gemini-3-5-flash (new May 28 data), claude-code (security plugin)
Ideas updated: two-track-ai-future (Pentagon dropping Claude evidence)

## [2026-05-29] ingest | 1 date

Dates processed: 2026-05-29
Topics updated: llm_models, ai_companies
Sources updated: anthropic, openai, meta, google, nvidia, mistral
Entities created: claude-opus-4-8, gamma-world, gemini-embedding-2
Entities updated: claude-mythos (93.9% SWE-bench), heretic (updated with new stats)
Ideas created: 
Ideas updated:

## [2026-05-30] ingest | 1 date

Dates processed: 2026-05-30
Topics updated: llm_models, ai_funding, ai_infrastructure, ai_security, agentic_ai
Sources updated: anthropic, google, mistral, cognition, samsung, sk-hynix, micron
Entities created: qwen-3-7-max, eidolon-os
Entities updated: mirage (stars updated to 2.8k)
Ideas created: pricing-war, vertical-integration
Ideas updated:
## [2026-05-31] ingest | 1 date

Dates processed: 2026-05-31
Topics updated: llm_models, ai_funding, ai_infrastructure, agentic_ai
Sources updated: anthropic, openai, waymo, meta, google
Entities created: waymo-ojai, claude-managed-agents, geely
Entities updated: gpt-rosalind (added biodefense program), claude-code (added May 2026 leak details)
Ideas created: 
Ideas updated: platform-consolidation (updated with May 31 events)

## [2026-06-01] ingest | 1 date

Dates processed: 2026-06-01
Topics updated: llm_models, agentic_ai, ai_funding
Topics created: physical_ai
Sources updated: anthropic, openai, google, nvidia, perplexity, cognition
Entities created: cosmos-3, antigravity-platform, gemini-spark (updated), synapse-ai, genclaw, nano-brain
Entities updated: claude-opus-4-8 (42-day cadence, Effort Controls)
Timelines created: 2026-06
Ideas updated: agent-infrastructure-layer (reinforced by convergence)

## [2026-06-03] ingest | 1 date

Dates processed: 2026-06-03
Topics updated: agentic_ai, ai_safety, github_trends, ai_companies
Sources updated: microsoft, openai, google, anthropic
Entities created: project-solara, ai-overviews
Entities updated: codex (5M users, Sites, role-specific plugins)
Timelines updated: 2026-06 (June 3: Trump AI order, Solara, Codex enterprise, Google opt-out)
Ideas created: 
Ideas updated: 

## [2026-06-04] lint | wiki health check

Fixed broken links: created entities/100cc, entities/minta, entities/showhn (June 3 GitHub trending repos); created topics/ai_search, sources/qualcomm, sources/salesforce (entities referenced without pages); created sources/cisco (replaced bare "Cisco security research" reference in ideas/multi-turn-structural)
Fixed wikilinks: entities/perplexity → entities/perplexity-computer + sources/perplexity in topics/ai_search and entities/ai-overviews; ideas/regulatory-fragmentation bare link annotated in topics/ai_safety
Fixed orphan pages: Added [[entities/enisa]] + [[ideas/multi-turn-structural]] from topics/ai_security (with new June 2026 Evolution entries); Added [[timelines/2026-06]] from topics/agentic_ai
Updated index.md: Added new pages - topics/ai_search, sources/qualcomm, sources/salesforce, sources/cisco, entities/100cc, entities/mai-family, entities/minta, entities/showhn, entities/windows-agent-runtime, ideas/multi-turn-structural; Counts: Topics 9→10, Sources 45→48, Entities 199→201, Ideas 67→68
Verified all wikilinks: No broken links

## [2026-06-08] lint | wiki health check

Fixed broken links: entities/hyperagents.md — [[entities/ineffable-intelligence]] → [[sources/ineffable-intelligence]] (Ineffable is a company, not an entity), [[entities/karpathy-autoresearch]] → [[entities/autoresearch]] (the actual slug is autoresearch, not karpathy-autoresearch)
Updated last_updated: entities/hyperagents.md 2026-06-07→2026-06-08, index.md 2026-06-07→2026-06-08
Verified all wikilinks: No broken links
Verified counts: Topics 10, Sources 48, Timelines 4, Entities 207, Ideas 70 (all match index claims)

## [2026-06-08] ingest | 1 date

Dates processed: 2026-06-08
Topics updated: llm_models, ai_companies, agentic_ai, ai_infrastructure, physical_ai, github_trends, ai_funding
Sources updated: anthropic, openai, google, nvidia, github
Sources created: unisound, jetbrains
Entities created: unisound-u2, mellum-2, snowey, gitpup-agent, agent-ghost
Timelines updated: 2026-06 (June 8: hybrid reasoning consensus + bifurcated industry)
Ideas updated: agent-infrastructure-layer (reinforced), foundation-model-portfolio-war (profitability-or-near), agent-verticalization (6-stage skill tree literalization), efficiency-frontier (Hybrid Thinking), safety-restricted-releases (verifiable pause advocacy)

Chat session learning: Reviewed 3 Q&A sessions (Apr 23-26). Confirmed recurring themes: agent infrastructure layer consolidation, frontier model portfolio war, Claude 1,858% growth context, Google $40B Anthropic investment, Claude Mythos Bank of England escalation, multi-turn vulnerability as structural. No new corrections needed; existing topic/source/entity pages already cover these patterns.

## [2026-06-10] ingest | 1 date

Dates processed: 2026-06-10
Topics updated: llm_models, ai_funding, ai_safety, ai_infrastructure, agentic_ai, github_trends, ai_companies, physical_ai
Sources updated: anthropic, tencent, nvidia
Sources created: allen-control-systems, eu-ai-office
Entities created: claude-fable-5, tencent-hy3, nvidia-dsx-os, allen-control-systems, command-center, mempalace, agent-reach, headroom, bullfrog, eu-gpai-code-of-practice, longmemeval, swe-bench-pro
Timelines updated: 2026-06 (June 9-10: 55× single-day pricing split, safety-productized frontier, DSX OS, Bullfrog $200M, EU NCA designation, Command Center, agent cost stack)
Ideas created: harness-layer-no-moat, ai-factory-software-stack, agent-cost-stack-fragmentation

Chat session learning: Reviewed 3 Q&A sessions (Apr 23-26). The patterns confirmed (Mythos geopolitical escalation, Google $40B Anthropic investment, multi-turn vulnerability as structural, frontier profitability-or-near) all extend the existing wiki narrative. The new June 9-10 patterns (Fable 5 productizes the safety-routing layer, 55× Hy3 vs Fable 5 same-day pricing split, Bullfrog $200M physical-AI defense validation, EU NCA active monitoring, agent cost stack open-sourcing in a single day) are net-new themes that create new ideas pages and several new entity pages.

## [2026-06-09] ingest | 1 date

Dates processed: 2026-06-09
Topics updated: llm_models, agentic_ai, ai_infrastructure, ai_safety, ai_companies, github_trends, ai_funding
Sources updated: anthropic, openai, google, apple, spacex, meta
Sources created: xiaomi
Entities created: afm-3, afm-3-cloud-pro, tilert, mimo-v2-5-pro-ultraspeed, google-skills, last30days-skill, turbovec
Entities updated: hatch (June 8: $200/mo Hatch Plus tier), muse-spark (June 8: Hatch transition target)
Timelines updated: 2026-06 (June 8-9: compute-IPO-pause convergence — AFM 3, OpenAI $852B IPO, Xiaomi 1000 TPS, Google-SpaceX $920M/month, Jack Clark brake pedal)
Ideas updated: two-track-ai-future (four-track bifurcation), openai-ipo-validates-agent-economy ($852B filing), safety-restricted-releases (brake pedal as filing-deadline play), three-tier-safety-playbook (brake pedal = third tier formalized)

Chat session learning: Reviewed 3 Q&A sessions (Apr 23-26). Confirmed recurring themes: agent infrastructure layer consolidation, Claude 1,858% growth, Google $40B Anthropic investment, multi-turn vulnerability. No new corrections needed; existing topic/source/entity pages already cover these patterns. New June 8-9 patterns (compute-IPO-pause convergence) extend rather than contradict existing narratives.
- 2026-06-11: Wiki Lint performed. Fixed orphan/duplicate company page (allen-control-systems), verified index integrity (0 missing/extra), checked topic sections and connection quality.
- 2026-06-11: Wiki Lint performed. Fixed orphan/duplicate company page (allen-control-systems), verified index integrity (0 missing/extra), checked topic sections and connection quality.

## [2026-06-12] wiki lint
- Fixed 23 dead links (removed .md extension from wikilinks)
- Resolved 9 orphan pages by fixing links and adding link from topics/physical_ai to ideas/de-novo-generative-biology
- Synced wiki/index.md with filesystem: removed entities/allen-control-systems (moved to sources), added 16 missing pages (diffusion-gemma, dreaming-v3, gbrain, etc.)
- Updated index counts and verified all topic pages have Evolution/Patterns sections
## [2026-06-11] ingest | 1 date

Dates processed: 2026-06-11
Topics updated: llm_models, ai_safety, ai_companies, github_trends, biotech
Sources updated: google, openai, anthropic, meta, xai
Entities created: diffusion-gemma, dreaming-v3, gbrain, joyai-echo, sensenova-u1
Entities updated: claude-fable-5
Ideas created: model-moat-fragility, chatbot-to-os-pivot
Ideas updated: platform-to-publisher-liability, human-out-of-the-loop-combat, transformer-architecture-evolution, de-novo-generative-biology

## [2026-06-12] ingest | 1 date

Dates processed: 2026-06-12
Topics updated: agentic_ai, ai_companies, ai_funding, github_trends, physical_ai
Sources updated: prometheus, anthropic, openai, google
Entities created: humanoid-gpt, mue-x, meadow-mind, chatgpt
Entities updated: claude-fable-5
Ideas created: agentic-economic-actor, physical-ai-pivot, agentic-anarchy, invisible-containment-tension
Ideas updated: openai-ipo-validates-agent-economy
2026-06-13: WIKI LINT completed.
- Fixed broken links: [[sources/google_deepmind]] -> [[sources/google]], [[entities/sense-nova-u1]] -> [[entities/sensenova-u1]].
- Created missing page: [[ideas/titan-era-of-ai]].
- Fixed orphan pages: Linked [[ideas/chatbot-to-os-pivot]] from Agentic AI and [[topics/biotech]] from De Novo Generative Biology.
- Structural integrity: Deleted non-entity page [[entities/eliezer]], rebuilt index.md.
- Connection quality: Verified all topic pages have Evolution and Patterns sections.
- Result: Wiki structural health restored.
2026-06-14: Fixed broken links to [[entities/eliezer]] in timelines and topics; removed non-existent entity from index; rebuilt index.md.

## [2026-06-14] ingest | 1 date

Dates processed: 2026-06-14
Topics updated: llm_models, ai_companies, github_trends, ai_safety, ai_governance
Sources updated: anthropic, openai, google
Entities updated: fable-5, mythos-5, c2pa-protocol, synthid, neuralbridge-sdk, dataroom, showui-pi
Ideas updated: digital-kill-switch, ai-iron-curtain, regulatory-capture-bio-threats, frontier-club-consolidation, sovereign-ai
Timelines updated: 2026-06
2026-06-15: WIKI LINT - Fixed orphan page swe-bench; merged fable-5 into claude-fable-5; fixed 2 broken links; updated index.md

## [2026-06-15] ingest | 1 date

Dates processed: 2026-06-15
Topics updated: llm_models, ai_companies, ai_funding, ai_governance, ai_safety, github_trends
Sources updated: anthropic, eu-ai-office
Entities updated: claude-fable-5, mythos-5, spatial-claw, open-notebook, copilot-kit
Ideas updated: sovereign-ai-surge, nationalized-ai, generative-ui-shift, digital-kill-switch

## [2026-06-16] lint | wiki health check

- Fixed broken link: [[sources/us_government]] created to resolve link from ideas/nationalized-ai
- Structural integrity: Added 8 missing entities (copilot-kit, open-notebook, spatial-claw, etc.) and 3 missing ideas (generative-ui-shift, nationalized-ai, sovereign-ai-surge) to index.md
- Sync: Updated wiki/index.md counts (Sources 56→57, Entities 244→247, Ideas 91→94)
- Connection quality: Verified all topic pages contain ## Evolution and ## Patterns & Insights sections
- Audit: No company/people misclassifications in entities/ found; no unannotated links detected

## [2026-06-17] ingest | 2 dates

Dates processed: 2026-06-16, 2026-06-17
Topics updated: llm_models, ai_companies, ai_safety, github_trends, physical_ai
Sources updated: anthropic, xai, alibaba, genesis-ai
Entities created/updated: eno, grok-gov, legion-intelligence, prometheus, lathe, neuralbridge-sdk, peek, rynnbrain, qwen-3-7-max, ouroboros-kernelsmith, internal-safety-collapse, social-stockfish
Ideas created/updated: ai-as-strategic-munition, ai-as-tactical-executioner, sovereign-ai-acceleration, embodied-agency-shift, internal-safety-collapse

## [2026-06-18] ingest | 1 date

Dates processed: 2026-06-18
Topics updated: llm_models, ai_companies, ai_funding, github_trends
Sources updated: openai, anthropic, midjourney, spacex, pinterest, prometheus
Entities updated: gpt-5.4, maria-agent, midjourney-medical, mythos-5, claude-fable-5, cursor, prometheus-ai, ghost-layer, joyai-vl-interaction, scrapling
Ideas updated: agentic-science, conceptual-leaps, reconstructing-reality, ai-iron-curtain, software-defined-engineering, agentic-commerce
