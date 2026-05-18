#!/usr/bin/env bash
# wiki_lint.sh — Launch ollama claude agent to lint/self-reflect the wiki.
#
# Checks broken links, removes wrong/duplicate info, improves connections.
# Scheduled to run daily at 1 AM via launchd.
#
# Usage:
#   ./wiki_lint.sh              # uses default model
#   ./wiki_lint.sh glm-5:cloud  # override model
#
set -Eeuo pipefail

REPO="$(cd "$(dirname "$0")" && pwd)"
WIKI_DIR="$REPO/wiki"
LLM_WIKI="$REPO/llm-wiki.md"
PROJECT_SCHEMA="$WIKI_DIR/WIKI.md"
MODEL="${1:-minimax-m2.5:cloud}"
TODAY="$(date '+%Y-%m-%d')"
LINT_MARKER="$REPO/logs/lint_done_${TODAY}.json"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"; }

if [[ ! -d "$WIKI_DIR" ]]; then
    log "wiki/ directory not found — nothing to lint."
    exit 0
fi

if ! command -v ollama >/dev/null 2>&1; then
    echo "ERROR: ollama not found in PATH" >&2
    exit 1
fi

log "Starting wiki lint using model: $MODEL"

cd "$REPO"
git pull --ff-only || true

# Build prompt in a temp file to avoid heredoc quoting issues
PROMPT_FILE="$(mktemp)"
trap 'rm -f "$PROMPT_FILE"' EXIT

cat > "$PROMPT_FILE" <<'STATIC_PART'
You are performing a daily self-reflection and health check on the Daily AI News wiki.

=== YOUR TASK: WIKI LINT ===

Perform a thorough lint of the wiki at wiki/. Go through EVERY check below systematically. Fix problems as you find them — do not just report, actually edit the files.

## Pass 1 — Structural Integrity

1. Read wiki/index.md. For every page listed, verify the .md file exists. Remove entries for missing files.
2. Scan wiki/topics/, wiki/sources/, wiki/timelines/, wiki/entities/, wiki/ideas/ for .md files NOT listed in index.md. Add them.
3. Check all [[wikilinks]] across all pages. For each broken link (target does not exist):
   - If the target is a minor reference, remove the link
   - If the target is an important concept that should have a page, create it
4. Find orphan pages (no inbound links from any other page). Add links from relevant pages or note them for review.
5. Check entity pages: any companies or people in entities/? Companies go in sources/, people should be removed entirely.

## Pass 2 — Wrong & Duplicate Information

1. Look for duplicate pages covering the same concept (e.g., two entity pages for the same model with slight name variations). Merge them — keep the richer one, redirect links.
2. Look for duplicate content within pages (same paragraph or section repeated).
3. Check for factually inconsistent information between pages (e.g., a model release date differs between entity page and timeline page).
4. Check frontmatter: are dates, slugs, and types consistent and correct?
5. Check for stale claims that newer data has superseded — update with current information.
6. Remove any people from entities/ — entities are for technical things only.

## Pass 3 — Connection Quality

1. Find connections that just say "Related:", "See also:", or link without annotation — rewrite with WHY.
2. Find entities mentioned in topics/sources pages but lacking their own entity page — create the page.
3. Check topic pages for missing ## Evolution section — write chronological narrative.
4. Check topic pages for missing ## Patterns & Insights — synthesize from events.
5. Check for ideas that could be extracted from daily insight_analysis but do not have their own page.

## Pass 4 — Index & Log

1. Rebuild wiki/index.md with accurate counts and all pages listed.
2. Append a lint entry to wiki/log.md with counts of what was fixed.

Start now. Be thorough but efficient.
STATIC_PART

LINT_OUTPUT="$(ollama launch claude \
    --model "$MODEL" \
    --yes \
    -- \
    -p "$(cat "$PROMPT_FILE")" \
    --permission-mode dontAsk 2>&1)"

EXIT_CODE=$?
echo "$LINT_OUTPUT" >> "$REPO/logs/lint.log"
log "Wiki lint complete (exit code $EXIT_CODE)."

cd "$REPO"
git add -A

DIFF_STAT="$(git diff --cached --stat 2>/dev/null | tail -1)"
git commit -m "wiki: lint $TODAY" || true
git push || true

# Write lint completion marker with summary for xin-knowledge-bot
python3 -c "
import json, sys
summary = sys.stdin.read().strip()
# Keep last 2000 chars to avoid huge JSON
if len(summary) > 2000:
    summary = summary[-2000:]
marker = {
    'date': '$TODAY',
    'project': 'daily-ai-news',
    'status': 'done',
    'diff_stat': '''$DIFF_STAT''',
    'summary': summary,
}
with open('$LINT_MARKER', 'w') as f:
    json.dump(marker, f, ensure_ascii=False)
" <<< "$LINT_OUTPUT"

exit $EXIT_CODE
