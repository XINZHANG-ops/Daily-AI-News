---
title: "RL vs LLM Paradigm"
slug: rl-vs-llm-paradigm
last_updated: 2026-05-03
---

# RL vs LLM Paradigm

## The Insight
David Silver's $1.1B raise for Ineffable Intelligence at a $5.1B valuation is a direct challenge to the LLM scaling orthodoxy that funds the Pentagon deals, Anthropic's $900B round, and OpenAI's $852B valuation. Silver's thesis: LLMs are "fossil fuel" — they remix existing human knowledge but cannot discover genuinely new insights. His alternative is a "superlearner" using reinforcement learning that learns entirely from its own experience, which he positions as "renewable fuel." The $5.1B valuation for a company with no product, no revenue, and no public roadmap is either hubris or a signal that elite investors believe the LLM paradigm has a ceiling that RL can break through. The question Silver's raise poses: if incumbents are already spending $50-145B/year on LLMs, can a $1.1B startup compete — or is this an acqui-hire play dressed as a paradigm shift?

## Evidence
- [[sources/ineffable-intelligence]] — $1.1B seed (largest in AI history) at $5.1B valuation; 50 senior researchers hired in 72 hours from DeepMind, OpenAI, Anthropic; no product disclosed
- [[sources/nvidia]] — Participated in the Ineffable round while also being in the Pentagon deals and supplying chips to every LLM company — hedging across paradigms
- [[topics/llm_models]] — The LLM scaling paradigm shows signs of strain: benchmark saturation (ARC-AGI-3 <1% for all frontier models), capability regression (Claude Code quality issues), and commodity inference achieving frontier scores (DeepSeek V4 Flash at 78% SWE-bench for $0.14/M)
- [[ideas/commodity-inference-fragmentation]] — The bifurcation between premium reasoning and commodity inference strengthens Silver's argument: if commodity models can match frontier models at 1/100th the cost, the LLM scaling curve may be flattening
- [[entities/arc-agi-3]] — ARC-AGI-3 results (GPT-5.5 0.43%, Opus 4.7 0.18%) are the strongest empirical validation of Silver's thesis: the finding that models route unfamiliar situations to memorized templates (mapping grids to "Tetris") reveals LLMs aren't reasoning — they're retrieving; this is the fossil fuel problem made measurable

## Implications
If Silver is right, the tens of billions flowing into LLM compute are building on a depleting resource — human-generated training data — while RL-based systems that learn from experience could scale indefinitely. Nvidia's participation in the round (while supplying every LLM company) shows the chipmaker is hedging: compute demand shifts but doesn't disappear if the paradigm changes. The UK sovereign AI fund's involvement signals the British government is betting the next breakthrough might come from London, not San Francisco. For the military AI divide, Silver's thesis introduces a third possibility: both military deployment and enterprise safety are optimizing for a paradigm (LLMs) that RL will render obsolete, making the entire debate about which track is "responsible" moot.

## Connections
- [[ideas/commodity-inference-fragmentation]] — The premium-vs-commodity split in LLM pricing strengthens Silver's argument that LLM scaling is hitting diminishing returns
- [[ideas/military-ai-divide]] — Silver's RL bet introduces the possibility that both sides of the military divide are optimizing for a paradigm that won't matter
- [[topics/ai_funding]] — $1.1B seed for a no-product company resets expectations for what "early stage" means in AI; the bar for credible AGI-adjacent startups has shifted dramatically
- [[sources/deepseek]] — DeepSeek's V4 Flash achieving 78% SWE-bench at $0.14/M supports Silver's implicit critique: LLM scaling may deliver diminishing capability returns per dollar
- [[entities/ising]] — NVIDIA's quantum AI models represent another orthogonal bet; if Ising and RL both challenge the LLM paradigm from different directions, the compute landscape in 2027-2028 could look nothing like 2026
