# Daily AI News Wiki — Project Schema

This file defines the conventions for building and maintaining the AI news wiki. Read alongside `llm-wiki.md` for the general pattern. When the two conflict, this file takes precedence.

## Context

This wiki tracks AI industry news, trending GitHub repositories, and daily insights. Each day, data is collected into JSON files containing `github_repos`, `ai_news`, and `insight_analysis`. The wiki compiles this into a structured, richly interlinked knowledge base.

**Your job**: Read new data from `data/` JSON files, integrate into the wiki, and maintain rich annotated connections across all pages.

---

## Directory Structure

```
wiki/
  WIKI.md              # This file (project schema)
  index.md             # Catalog of all wiki pages (update on every ingest)
  log.md               # Append-only ingest log
  processed.json       # ["2026-04-01", "2026-04-02", ...]
  topics/              # Broad theme synthesis pages
  sources/             # Company/organization timelines
  timelines/           # Monthly event summaries
  entities/            # Specific named things: models, products, protocols, frameworks, repos
  ideas/               # Cross-cutting insights, patterns, and predictions
```

**IMPORTANT DISTINCTIONS:**
- `topics/` are BROAD THEMES: LLM models, AI funding, GitHub trends, AI companies, AI safety, agentic AI.
- `sources/` are COMPANY/ORG TIMELINES: OpenAI, Anthropic, Google, Meta, xAI — chronological event records.
- `entities/` are SPECIFIC NAMED THINGS: models (Claude Mythos, GPT-5.4, Gemma 4), products (Claude Code, Codex, Cursor), protocols (MCP), frameworks, specific GitHub repos (claw-code), benchmarks (SWE-bench, ARC-AGI-3). NEVER put companies or people in entities — companies go in sources/.
- `ideas/` are CROSS-CUTTING INSIGHTS: "benchmark ceiling crisis", "safety-restricted releases precedent", "the agentic shift", "AI coding as growth driver". Insights that emerge from synthesizing multiple news items.
- `timelines/` are MONTHLY SUMMARIES: week-by-week breakdown of events.

---

## Data Source Format

Each JSON file in `data/` (named `YYYY-MM-DD.json`) contains:

```json
{
  "date": "2026-04-16",
  "github_repos": [{"name": "owner/repo", "url": "...", "description": {"en": "...", "zh": "..."}, "stars": "100k+", "forks": "10k"}],
  "ai_news": [{"title": {"en": "...", "zh": "..."}, "url": "...", "source": "TechCrunch", "time": "2026-04-15", "description": {"en": "...", "zh": "..."}}],
  "insight_analysis": {"en": "...", "zh": "..."}
}
```

---

## Connection Rules — THE MOST IMPORTANT PART

Every `## Connections` section on every page must use **annotated wikilinks**. Every link MUST explain WHY and HOW things connect. This is what makes the wiki valuable.

### BAD — never generate these:

```markdown
## Connections
- Related: [[topics/llm_models]]
- See also: [[sources/anthropic]]
- [[entities/claude-mythos]]
```

### GOOD — always generate these:

```markdown
## Connections
- [[entities/claude-mythos]] — Project Glasswing exists BECAUSE Mythos' cybersecurity capabilities were deemed too dangerous for public release; this is the first time a major lab has withheld a model due to raw capability concerns rather than misuse risk
- [[topics/ai_funding]] — Anthropic's $30B Series G was accelerated partly by Mythos' demonstrated capabilities, which validated the lab's technical lead to investors
- [[ideas/safety-restricted-releases]] — Mythos established the precedent that some models may be too capable for public release, which could reshape how future frontier models are deployed
- [[sources/openai]] — OpenAI responded to the Mythos announcement with an investor memo claiming computing advantage, intensifying the rivalry as both prepare for IPO
```

### Connection annotation checklist:
1. Does the annotation explain a SPECIFIC relationship, not just "related"?
2. Does it say something a reader couldn't guess from the page titles alone?
3. Would removing this annotation lose important context?

If any answer is no, rewrite the annotation.

---

## Topic Page Format

File: `wiki/topics/{topic_slug}.md`

```markdown
---
title: "Topic Name"
slug: topic_slug
last_updated: YYYY-MM-DD
---

# Topic Name

## Overview
<!-- 2-4 paragraph synthesis of the current state of this topic -->

## Evolution
<!-- Chronological NARRATIVE of how this topic has developed.
     NOT a list of events. A story showing progression.

     Example:
     In mid-March, the LLM landscape was dominated by Claude Opus 4.6 and GPT-5.4
     trading benchmark leads. Then the Claude Mythos leak on March 26 fundamentally
     changed the conversation — suddenly the question wasn't "which model is best?"
     but "what happens when a model is too good to release?" This catalyzed...  -->

## Key Developments

| Date | Event | Significance |
|------|-------|-------------|
| 2026-04-10 | Event description | Why this matters |

## Patterns & Insights
<!-- Synthesized observations from looking across all events in this topic -->

## Connections
<!-- ANNOTATED wikilinks — every link must explain WHY -->
```

---

## Source Page Format

File: `wiki/sources/{company_slug}.md`

```markdown
---
title: "Company Name"
slug: company_slug
last_updated: YYYY-MM-DD
---

# Company Name

## Overview
<!-- Current strategic position and trajectory -->

## Timeline

| Date | Event | Details |
|------|-------|---------|
| 2026-04-10 | Event | Details |

## Key Relationships
<!-- Annotated connections to other companies, explaining the dynamics -->

## Connections
<!-- ANNOTATED wikilinks — every link must explain WHY -->
```

---

## Entity Page Format

File: `wiki/entities/{entity_slug}.md`

Entities are SPECIFIC NAMED THINGS: models, products, protocols, frameworks, notable repos, benchmarks. NEVER companies or people.

```markdown
---
title: "Entity Name"
slug: entity_slug
type: model|product|protocol|framework|repo|benchmark
last_updated: YYYY-MM-DD
---

# Entity Name

## What It Is
<!-- 1-2 paragraph description -->

## Key Facts

| Attribute | Value |
|-----------|-------|
| Release Date | 2026-04-XX |
| Creator | Company |
| Key Metric | Value |

## Significance
<!-- Why this entity matters in the broader AI landscape -->

## Connections
<!-- ANNOTATED wikilinks explaining WHY this relates to others -->
```

---

## Idea Page Format

File: `wiki/ideas/{idea_slug}.md`

Ideas are cross-cutting insights, patterns, and predictions that emerge from synthesizing multiple news items.

```markdown
---
title: "Idea Title"
slug: idea_slug
last_updated: YYYY-MM-DD
---

# Idea Title

## The Insight
<!-- What is the core observation? 1-2 paragraphs. -->

## Evidence
<!-- Which events, entities, or trends support this? With annotated links -->
- [[entities/claude-mythos]] — First model withheld due to raw capability
- [[sources/openai]] — OpenAI's Spud model reportedly being evaluated for similar restrictions

## Implications
<!-- What does this mean for the industry? -->

## Connections
<!-- ANNOTATED wikilinks -->
```

---

## Timeline Page Format

File: `wiki/timelines/YYYY-MM.md`

```markdown
---
title: "Month Year Summary"
month: YYYY-MM
last_updated: YYYY-MM-DD
---

# Month Year

## Week 1 (1st–7th)
<!-- Narrative of the week's key events, with wikilinks to relevant pages -->

## Week 2 (8th–14th)
...
```

---

## index.md Format

```markdown
# Daily AI News Wiki

Last updated: YYYY-MM-DD

## Topics
- `topics/{slug}` — one-line description

## Sources
- `sources/{slug}` — one-line description

## Timelines
- `timelines/{YYYY-MM}` — one-line description

## Entities
- `entities/{slug}` — type: one-line description

## Ideas
- `ideas/{slug}` — one-line description
```

---

## log.md Format

Append-only:

```markdown
## [YYYY-MM-DD] ingest | N dates

Dates processed: 2026-04-15, 2026-04-16
Topics updated: llm_models, ai_funding
Sources updated: anthropic, openai
Entities created: gpt-5.4-thinking, mcp-protocol
Ideas created: benchmark-ceiling-crisis
```

---

## Ingest Workflow

For each new date's JSON file in `data/`:

1. **Read** the JSON file (github_repos, ai_news, insight_analysis)
2. **Skip** if date is already in `wiki/processed.json`
3. **Extract** key events, model releases, company news, repo trends
4. **Identify entities** (2-6): specific models, products, protocols, repos, benchmarks mentioned
5. **Identify ideas** (0-3): cross-cutting patterns or insights from the daily analysis
6. **Update** `wiki/topics/{slug}.md` — add events, update Overview, update Evolution narrative, update Patterns & Insights
7. **Update** `wiki/sources/{slug}.md` — add timeline entries for relevant companies
8. **Update** `wiki/timelines/{YYYY-MM}.md` — add to the appropriate week
9. **Create/update** `wiki/entities/{slug}.md` for named models, products, protocols, repos
10. **Create/update** `wiki/ideas/{slug}.md` for cross-cutting insights
11. **Update** `wiki/index.md` with any new pages
12. **Append** to `wiki/log.md`
13. **Update** `wiki/processed.json` — append the date

**CRITICAL**: All `## Connections` sections must have annotated wikilinks. Read the Connection Rules above. Never write "Related:" or "See also:" — always explain WHY.

---

## Lint Checklist

### Structural
- Pages in index.md without corresponding .md file
- Pages not listed in index.md
- Broken wikilinks
- Stale dates or facts superseded by newer data
- Orphan pages with no inbound links

### Connection Quality
- Connections that just say "Related:", "See also:", or link without annotation → rewrite with WHY
- Entities mentioned in topics/sources but lacking their own entity page
- Topic pages missing `## Evolution` section → write chronological narrative
- Topic pages missing `## Patterns & Insights` → synthesize from events
- Companies appearing in `entities/` → move to `sources/`
- People appearing in `entities/` → remove (entities are for technical things only)
- Ideas that could be extracted from daily insights but don't have their own page

## SQL Query Examples

```sql
SELECT title_en, source, time FROM ai_news WHERE date_added >= '2026-04-01' ORDER BY date_added DESC LIMIT 10;
SELECT name, stars, description_en FROM github_repos ORDER BY date_added DESC LIMIT 10;
SELECT content_en FROM insights WHERE date = '2026-04-13' LIMIT 1;
SELECT COUNT(*) as count, source FROM ai_news GROUP BY source ORDER BY count DESC;
```
