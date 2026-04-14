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
MODEL="${1:-minimax-m2.7:cloud}"

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

For each JSON file in data/:
1. Read the JSON file (contains github_repos, ai_news, insight_analysis)
2. Follow the ingest workflow defined in WIKI.md:
   - Update or create topic pages (wiki/topics/)
   - Update or create source pages (wiki/sources/)
   - Update or create timeline pages (wiki/timelines/)
   - Update wiki/index.md with new pages
   - Append entry to wiki/log.md
3. After all dates are processed, update wiki/processed.json with the processed dates

Be thorough with topic synthesis — the goal is a wiki where each topic page synthesizes trends across multiple days, not just lists of news items.

Key topics to track:
- LLM releases and updates (GPT, Claude, Gemini, etc.)
- AI company news (OpenAI, Anthropic, Google, Meta, etc.)
- Funding rounds and valuations
- GitHub trending repositories and patterns
- Industry trends and insights

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
