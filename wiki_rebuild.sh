#!/usr/bin/env bash
# wiki_rebuild.sh — Delete current wiki and rebuild from ALL data with new schema.
#
# Usage:
#   bash wiki_rebuild.sh              # uses default model
#   bash wiki_rebuild.sh glm-5:cloud  # override model
#
set -Eeuo pipefail

REPO="$(cd "$(dirname "$0")" && pwd)"
WIKI_DIR="$REPO/wiki"
MODEL="${1:-minimax-m2.7:cloud}"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"; }

# ── Step 1: Delete current wiki content ───────────────────────────────────
log "Step 1: Cleaning wiki content..."
rm -rf "$WIKI_DIR/topics" "$WIKI_DIR/sources" "$WIKI_DIR/timelines" "$WIKI_DIR/entities" "$WIKI_DIR/ideas"
rm -f "$WIKI_DIR/index.md" "$WIKI_DIR/log.md" "$WIKI_DIR/processed.json"

mkdir -p "$WIKI_DIR/topics" "$WIKI_DIR/sources" "$WIKI_DIR/timelines" "$WIKI_DIR/entities" "$WIKI_DIR/ideas"

# Seed index.md
cat > "$WIKI_DIR/index.md" <<'EOF'
# Daily AI News Wiki

Last updated: —

## Topics

## Sources

## Timelines

## Entities

## Ideas
EOF

# Seed log.md
echo "# Wiki Log" > "$WIKI_DIR/log.md"

# Seed processed.json (empty — rebuild everything)
echo '[]' > "$WIKI_DIR/processed.json"

log "  Wiki cleaned."

# ── Step 2: Rebuild wiki from all data ────────────────────────────────────
DATA_COUNT=$(find "$REPO/data" -name "*.json" -type f | wc -l | tr -d ' ')
log "Step 2: Rebuilding wiki from $DATA_COUNT data files with model: $MODEL..."
bash "$REPO/wiki_build.sh" "$MODEL"

# ── Step 3: Verify structure ──────────────────────────────────────────────
log "Step 3: Verifying wiki structure..."
echo "--- topics ---"
ls "$WIKI_DIR/topics/" 2>/dev/null || echo "(empty)"
echo "--- sources ---"
ls "$WIKI_DIR/sources/" 2>/dev/null || echo "(empty)"
echo "--- timelines ---"
ls "$WIKI_DIR/timelines/" 2>/dev/null || echo "(empty)"
echo "--- entities ---"
ls "$WIKI_DIR/entities/" 2>/dev/null || echo "(empty)"
echo "--- ideas ---"
ls "$WIKI_DIR/ideas/" 2>/dev/null || echo "(empty)"
echo "--- index.md header ---"
head -5 "$WIKI_DIR/index.md"

log "Wiki rebuild complete!"
