#!/usr/bin/env bash
# wiki_build.sh — Launch ollama claude agent to build/update the AI News wiki.
#
# Usage:
#   ./wiki_build.sh              # uses default model
#   ./wiki_build.sh glm-5:cloud  # override model
#
set -Eeuo pipefail

REPO="$(cd "$(dirname "$0")" && pwd)"
WIKI_DIR="$REPO/wiki"
DATA_DIR="$REPO/data"
LLM_WIKI="$REPO/llm-wiki.md"
PROJECT_SCHEMA="$WIKI_DIR/WIKI.md"
MODEL="${1:-minimax-m2.5:cloud}"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"; }

# ── Sanity checks ──────────────────────────────────────────────────────────
if [[ ! -d "$DATA_DIR" ]] || [[ -z "$(ls -A "$DATA_DIR"/*.json 2>/dev/null)" ]]; then
    log "data/ is empty — nothing to build. Skipping."
    exit 0
fi

# ── Check for new data ─────────────────────────────────────────────────────
# Get list of dates from JSON files
DATA_DATES=$(find "$DATA_DIR" -name "*.json" -exec basename {} .json \; | sort)

PROCESSED_FILE="$WIKI_DIR/processed.json"
NEW_COUNT=0

if [[ -f "$PROCESSED_FILE" ]]; then
    # Count how many dates are new
    for date in $DATA_DATES; do
        if ! grep -q "\"$date\"" "$PROCESSED_FILE"; then
            ((NEW_COUNT++))
        fi
    done

    if [[ "$NEW_COUNT" -eq 0 ]]; then
        log "All data in data/ already processed — skipping build."
        exit 0
    fi
else
    # No processed.json yet, all data is new
    NEW_COUNT=$(echo "$DATA_DATES" | wc -w | tr -d ' ')
fi

if ! command -v ollama >/dev/null 2>&1; then
    echo "ERROR: ollama not found in PATH" >&2
    exit 1
fi

log "Building wiki for $NEW_COUNT new date(s) using model: $MODEL"

# ── Check for chat sessions ───────────────────────────────────────────────
SESSIONS_DIR="$REPO/wiki_sessions"
SESSION_COUNT=0
if [[ -d "$SESSIONS_DIR" ]] && [[ -n "$(ls -A "$SESSIONS_DIR"/*.json 2>/dev/null)" ]]; then
    SESSION_COUNT=$(find "$SESSIONS_DIR" -name "*.json" -type f | wc -l | tr -d ' ')
fi
log "Found $SESSION_COUNT chat sessions in wiki_sessions/"

# ── Build the task prompt ──────────────────────────────────────────────────
TASK_PROMPT="$(cat <<PROMPT
You are maintaining an AI news wiki for the Daily-AI-News project.

Below are two documents that define your task:

=== GENERAL WIKI PATTERN (llm-wiki.md) ===
$(cat "$LLM_WIKI")

=== PROJECT-SPECIFIC SCHEMA (WIKI.md) ===
$(cat "$PROJECT_SCHEMA")

=== YOUR TASK ===

Working directory: $REPO

There are $NEW_COUNT new date(s) in data/ that have not yet been added to the wiki.
There are $SESSION_COUNT chat sessions in wiki_sessions/ with past Q&A conversations.

Follow the ingest workflow defined in WIKI.md exactly. Key steps:

STEP 1 — For each new JSON file in data/ (check wiki/processed.json to find unprocessed dates):
1. Read the JSON file (github_repos, ai_news, insight_analysis)
2. Identify specific entities: models (e.g., "Claude Mythos", "GPT-5.4"), products (e.g., "Claude Code", "Codex"), protocols (e.g., "MCP"), notable repos (e.g., "claw-code"), benchmarks
3. Identify ideas: cross-cutting insights or patterns in the daily analysis
4. Update wiki/topics/ (llm_models, ai_companies, ai_funding, github_trends — create new topics if needed)
5. Update wiki/sources/ for relevant companies (openai, anthropic, google, meta — create new sources if needed)
6. Update wiki/timelines/ for the appropriate month
7. Create/update wiki/entities/ pages for each entity identified
8. Create/update wiki/ideas/ pages for each cross-cutting insight

STEP 2 — Learn from chat history:
If wiki_sessions/ has JSON files, read them. Each file is a JSON array of {role, content} messages.
Look for:
- Questions the user asked that reveal knowledge gaps in the wiki → fill those gaps
- Insights or connections mentioned in Q&A that should be added to idea/topic/entity pages
- Repeated questions about the same topic → that topic page needs more depth
- Corrections or clarifications from conversations → update affected pages
Do NOT copy raw Q&A into the wiki. Extract the useful knowledge and integrate it naturally.

STEP 3 — After all processing:
1. Update wiki/index.md with all 5 sections (Topics, Sources, Timelines, Entities, Ideas)
2. Update wiki/processed.json
3. Append to wiki/log.md

CRITICAL REQUIREMENT — Connections:
Every ## Connections section on every page must have ANNOTATED [[wikilinks]]. Read the Connection Rules in WIKI.md carefully. NEVER write "Related:" or "See also:" — always explain WHY with a specific annotation.

Be thorough with:
- Topic synthesis: ## Evolution tells a chronological story (not a list), ## Patterns & Insights synthesizes across events
- Entity identification: extract specific named models, products, protocols, repos from each date
- Idea extraction: look for insights in insight_analysis and recurring patterns across multiple days

Start now.
PROMPT
)"

# ── Launch the agent ───────────────────────────────────────────────────────
log "Launching ollama claude agent..."
cd "$REPO"

ollama launch claude \
    --model "$MODEL" \
    --yes \
    -- \
    -p "$TASK_PROMPT" \
    --permission-mode dontAsk 2>&1 | tee -a "$REPO/wiki_build.log"

log "Wiki build complete."
