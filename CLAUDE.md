# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Overview

Daily AI News is an automated system that tracks AI industry news, trending GitHub repositories, and daily insights. Data is collected into JSON files, rendered as bilingual (EN/ZH) HTML pages, and published to GitHub Pages. An LLM-maintained wiki synthesizes knowledge across days.

## Commands

```bash
# Build HTML pages from JSON data
python3 build_from_json.py data/2026-04-16.json

# Rebuild all pages
for file in data/*.json; do python3 build_from_json.py "$file"; done

# Rebuild index.html
python3 rebuild_index.py

# Rebuild SQLite database
python3 build_sqlite.py

# Stage new papers for wiki + build wiki
python3 -u wiki_sync.py       # (daily_paper only, not used here)
bash wiki_build.sh             # Launch ollama claude agent to update wiki

# Full wiki rebuild from all data
bash wiki_rebuild.sh

# Start search/wiki API server (port 5002)
python3 serve_ai_news.py --port 5002

# Start supervisor daemon (monitors git, auto-rebuilds)
nohup /Users/xinzhang/Downloads/ai_news_server > /tmp/ai_news_supervisor.log 2>&1 &
```

## Architecture

### Data Pipeline

```
JSON data files (data/YYYY-MM-DD.json)
  ├─ github_repos: [{name, url, description{en,zh}, stars, forks}]
  ├─ ai_news: [{title{en,zh}, url, source, time, description{en,zh}}]
  └─ insight_analysis: {en, zh}
       ↓
  ├→ build_from_json.py → HTML pages (pages/*.html, bilingual UI)
  ├→ build_sqlite.py → ai_news.sqlite (3 tables: github_repos, ai_news, insights)
  └→ wiki_build.sh → Wiki pages (topics, sources, timelines, entities, ideas)
       ↓
  serve_ai_news.py → Flask REST API (port 5002)
       ↓
  rebuild_index.py → index.html (date archive list)
```

### Flask API (serve_ai_news.py, port 5002)

- `GET /health` — liveness check
- `GET /schema` — SQLite schema
- `GET /stats` — row counts and date ranges
- `POST /query` — SQL queries (SELECT only)
- `POST /ask_wiki` — Wiki Q&A via ollama claude agent (with session memory)
- `POST /lint_wiki` — Wiki health check
- Background: daily automated lint

### Supervisor (`/Users/xinzhang/Downloads/ai_news_server`)

Polls git every 10min. On remote change: `git pull` → `build_sqlite.py` → `wiki_build.sh` → restart `serve_ai_news.py`.

## Cross-Repo Architecture

This project is part of a 3-repo system that work together:

```
┌─────────────────────────────────────────────────────────────────┐
│  User's Browser (GitHub Pages)                                   │
│  ├─ daily_paper pages (context_type="paper")                    │
│  └─ Daily-AI-News pages (context_type="ai_news")                │
│       ↓ POST /chat via ngrok tunnel                             │
├──────────────────── Internet / ngrok ───────────────────────────┤
│  Windows — ai-server, port 8080 + ngrok tunnel                   │
│  ├─ "paper"   → POST /ask_wiki to Mac LAN IP:5001              │
│  ├─ "ai_news" → POST /ask_wiki to Mac LAN IP:5002              │
│  └─ other     → local Ollama LLM                                │
│       ↓ HTTP over WiFi LAN (e.g. http://10.0.0.28)             │
├──────────────────── Same WiFi LAN ──────────────────────────────┤
│  Mac (daily_paper + this repo)                                   │
│  ├─ serve_search.py (port 5001) — /ask_wiki, /search, /query   │
│  ├─ serve_ai_news.py (port 5002) — /ask_wiki, /query           │
│  └─ Ollama (local LLM for wiki building + wiki Q&A)            │
└─────────────────────────────────────────────────────────────────┘
```

**Network:** Mac and Windows on same WiFi LAN. Windows runs ngrok to expose port 8080 to the internet for GitHub Pages. Windows→Mac communication uses LAN IP directly (no ngrok).

**Repos:**
- **daily_paper** (`/Users/xinzhang/daily_paper`): Paper fetching, wiki, search API on Mac port 5001
- **Daily-AI-News** (this repo): AI news, wiki, search API on Mac port 5002
- **ai-server** (`/Users/xinzhang/ai-server`): Windows chat router on port 8080 + ngrok

**Session flow:** Frontend generates `client-XXXXX` session_id → ai-server accepts it → forwards same session_id to Mac `/ask_wiki` → Mac `wiki_sessions` tracks history → injected into LLM prompt on subsequent messages.

**Frontend config:** `js/ai-assistant-config.js` — `LOCAL` points to `localhost:8080` (browsing on Windows), `NGROK` points to public ngrok URL (GitHub Pages). Context type auto-set to `ai_news` via `ai-assistant-constants.js`.

## Wiki — Persistent Knowledge Base

The wiki at `wiki/` is an LLM-maintained knowledge base that grows with every day's data.

**Directories:**
- `topics/` — broad themes: LLM models, AI funding, GitHub trends, AI companies
- `sources/` — company timelines: OpenAI, Anthropic, Google, Meta
- `timelines/` — monthly event summaries
- `entities/` — specific things: models (Claude Mythos, GPT-5.4), products (Claude Code), protocols (MCP), repos, benchmarks. Never companies or people.
- `ideas/` — cross-cutting insights: "benchmark ceiling crisis", "safety-restricted releases precedent"

**Pipeline:** Data arrives in `data/` → `wiki_build.sh` launches ollama claude agent → agent reads JSON files, creates/updates pages with annotated `[[wikilinks]]` → `serve_ai_news.py` `/ask_wiki` queries the wiki with session memory.

**Key files:**
- `wiki/WIKI.md` — schema defining page templates, connection rules, ingest workflow
- `wiki/index.md` — catalog of all pages (5 sections)
- `wiki_build.sh` — launches ollama claude agent to update wiki
- `wiki_rebuild.sh` — full rebuild from all data (deletes wiki, rebuilds from scratch)

**Connection rules:** Every `[[wikilink]]` must be annotated with WHY things connect. Never "Related:" or "See also:" — always a specific explanation.

## Key Details

- **Bilingual**: All data and UI support EN/ZH toggle
- **Model**: Wiki building uses `minimax-m2.7:cloud` via ollama by default
- **SQLite tables**: `github_repos`, `ai_news`, `insights` — all have `date_added` column
- **Frontend**: Purple gradient theme (#e94560 → #7b2cbf), distinct from daily_paper's blue-purple
- **Git workflow**: `rebuild_index.py` auto-commits and pushes to GitHub Pages
