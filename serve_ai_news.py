#!/usr/bin/env python3
"""
AI News Search Service
======================

Flask service providing SQL query and Wiki Q&A interface for AI News database.
Similar to serve_search.py but simpler (no vector search, only SQL).

Usage:
    python serve_ai_news.py --port 5002
"""

import argparse
import sqlite3
import json
import logging
import subprocess
import threading
import time
import requests as http_requests
from pathlib import Path
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).parent

app = Flask(__name__)
CORS(app)


# =============================================================
# Static file routes
# =============================================================

@app.route('/', methods=['GET'])
def index():
    return send_from_directory(str(REPO_ROOT), 'index.html')


@app.route('/pages/<path:filename>', methods=['GET'])
def pages(filename):
    return send_from_directory(str(REPO_ROOT / 'pages'), filename)


@app.route('/css/<path:filename>', methods=['GET'])
def css(filename):
    return send_from_directory(str(REPO_ROOT / 'css'), filename)


@app.route('/js/<path:filename>', methods=['GET'])
def js(filename):
    return send_from_directory(str(REPO_ROOT / 'js'), filename)


# Global variables
DB_PATH = None
wiki_sessions = {}  # Store conversation history for wiki Q&A


def validate_sql(sql: str) -> tuple[bool, str]:
    """
    Validate SQL query for security.

    Returns:
        (is_valid, error_message)
    """
    sql_upper = sql.upper().strip()

    # Must be a SELECT statement
    if not sql_upper.startswith('SELECT'):
        return False, "Only SELECT queries are allowed"

    # Dangerous keywords
    dangerous = ['DROP', 'DELETE', 'INSERT', 'UPDATE', 'ALTER', 'CREATE', 'EXEC', 'EXECUTE', 'TRUNCATE']
    for keyword in dangerous:
        if keyword in sql_upper:
            return False, f"Dangerous keyword '{keyword}' not allowed"

    return True, ""


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'service': 'ai-news-search',
        'database': str(DB_PATH)
    })


@app.route('/schema', methods=['GET'])
def get_schema():
    """
    Get database schema information.

    Returns:
        JSON with table names and column definitions
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()

            # Get all tables
            cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = [row[0] for row in cur.fetchall()]

            schema = {}
            for table in tables:
                # Get column info for each table
                cur.execute(f"PRAGMA table_info({table})")
                columns = []
                for row in cur.fetchall():
                    columns.append({
                        'name': row[1],
                        'type': row[2],
                        'notnull': bool(row[3]),
                        'pk': bool(row[5])
                    })
                schema[table] = columns

            return jsonify({
                'tables': tables,
                'schema': schema
            })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/query', methods=['POST'])
def query():
    """
    Execute SQL query on AI News database.

    Request JSON:
        {
            "sql": "SELECT title_en, description_en FROM ai_news WHERE ..."
        }

    Returns:
        JSON with query results
    """
    try:
        data = request.get_json()
        if not data or 'sql' not in data:
            return jsonify({'error': 'Missing sql parameter'}), 400

        sql = data['sql']

        # Validate SQL
        is_valid, error = validate_sql(sql)
        if not is_valid:
            return jsonify({'error': f'Invalid SQL: {error}'}), 400

        # Execute query
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row  # Enable column access by name
            cur = conn.cursor()
            cur.execute(sql)

            # Convert rows to dicts
            results = [dict(row) for row in cur.fetchall()]

            return jsonify({
                'sql': sql,
                'count': len(results),
                'results': results
            })

    except sqlite3.Error as e:
        return jsonify({'error': f'Database error: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/stats', methods=['GET'])
def stats():
    """
    Get database statistics.

    Returns:
        JSON with row counts for each table
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()

            # Get table names
            cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = [row[0] for row in cur.fetchall()]

            stats = {}
            for table in tables:
                cur.execute(f"SELECT COUNT(*) FROM {table}")
                count = cur.fetchone()[0]
                stats[table] = count

            # Get date range
            cur.execute("SELECT MIN(date_added), MAX(date_added) FROM github_repos")
            repo_range = cur.fetchone()

            cur.execute("SELECT MIN(date_added), MAX(date_added) FROM ai_news")
            news_range = cur.fetchone()

            cur.execute("SELECT MIN(date), MAX(date) FROM insights")
            insights_range = cur.fetchone()

            return jsonify({
                'counts': stats,
                'date_ranges': {
                    'repos': {'min': repo_range[0], 'max': repo_range[1]},
                    'news': {'min': news_range[0], 'max': news_range[1]},
                    'insights': {'min': insights_range[0], 'max': insights_range[1]}
                }
            })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.before_request
def log_request():
    """Log incoming requests."""
    if request.method == 'POST' and request.path == '/query':
        data = request.get_json() or {}
        sql = data.get('sql', '')[:100]  # First 100 chars
        print(f"[{request.method}] {request.path} - SQL: {sql}...")
    else:
        print(f"[{request.method}] {request.path}")


@app.after_request
def log_response(response):
    """Log responses."""
    print(f"  → {response.status_code} ({response.content_length or 0} bytes)")
    return response


SAFETY_SERVICE_URL = 'http://localhost:5003/filter'


def _filter_pii(text):
    """Filter PII from text via the safety layer service. Returns original on failure."""
    try:
        resp = http_requests.post(
            SAFETY_SERVICE_URL,
            json={'text': text},
            timeout=30
        )
        if resp.ok:
            return resp.json().get('text', text)
    except Exception as e:
        logger.warning(f"Safety filter unavailable: {e}")
    return text


def _ask_wiki_internal(question, model='minimax-m2.7:cloud', session_id=None):
    """
    Internal wiki Q&A logic.

    Returns:
        dict with 'answer' and 'session_id', or 'error' key on failure
    """
    # Get or create session history
    if session_id:
        if session_id not in wiki_sessions:
            wiki_sessions[session_id] = []
        conversation_history = wiki_sessions[session_id]
    else:
        conversation_history = []

    repo_root = Path(__file__).parent
    wiki_dir = repo_root / 'wiki'
    llm_wiki_path = repo_root / 'llm-wiki.md'
    project_schema_path = wiki_dir / 'WIKI.md'

    if not wiki_dir.exists():
        return {'error': 'wiki/ directory not found'}

    try:
        llm_wiki_content = llm_wiki_path.read_text(encoding='utf-8') if llm_wiki_path.exists() else ""
        project_schema_content = project_schema_path.read_text(encoding='utf-8') if project_schema_path.exists() else ""
    except Exception as e:
        logger.error(f"Failed to read schema files: {e}")
        return {'error': f'Failed to read schema: {str(e)}'}

    history_context = ""
    if conversation_history:
        history_context = "\n=== CONVERSATION HISTORY ===\n"
        for msg in conversation_history[-6:]:
            role_label = "User" if msg['role'] == 'user' else "Assistant"
            history_context += f"{role_label}: {msg['content']}\n\n"
        history_context += "=== END HISTORY ===\n\n"

    prompt = f"""You are a research assistant helping answer questions about AI news, GitHub repositories, and daily insights.

=== WIKI PATTERN (llm-wiki.md) ===
{llm_wiki_content}

=== PROJECT SCHEMA (WIKI.md) ===
{project_schema_content}

=== AVAILABLE TOOLS ===

You have access to the following SQL query tool running on localhost:5002:

**SQL Query** (structured queries on AI news database):
   curl -X POST http://localhost:5002/query \\
     -H "Content-Type: application/json" \\
     -d '{{"sql": "SELECT title_en, description_en FROM ai_news WHERE ..."}}'

   Returns: {{"results": [{{"title_en": "...", "description_en": "...", ...}}]}}

   Available tables:
   - github_repos: name, url, description_en, description_zh, stars, forks, date_added
   - ai_news: title_en, title_zh, url, source, time, description_en, description_zh, date_added
   - insights: date, content_en, content_zh

{history_context}=== CURRENT QUESTION ===

Working directory: {repo_root}

The user asks: {question}

Strategy:
1. Consider the conversation history above (if any) for context
2. Read wiki/index.md to see all pages across topics/, sources/, timelines/, entities/, ideas/
3. Read relevant wiki pages — follow [[wikilinks]] across directories, traversing at least 2 levels of connections
4. The wiki contains cross-cutting ideas and entity pages — use these for richer context
5. If wiki coverage is incomplete, use SQL queries to find additional information
6. Synthesize a comprehensive answer combining wiki knowledge and SQL results

Answer:
"""

    try:
        logger.info(f"Calling ollama claude for question: {question[:60]}...")
        result = subprocess.run(
            [
                'ollama', 'launch', 'claude',
                '--model', model,
                '--yes',
                '--',
                '-p', prompt,
                '--permission-mode', 'dontAsk'
            ],
            capture_output=True,
            text=True,
            cwd=str(repo_root),
            timeout=300
        )

        if result.returncode != 0:
            logger.error(f"ollama claude failed: {result.stderr}")
            return {'error': f'Agent failed: {result.stderr}'}

        answer = result.stdout.strip()
        logger.info(f"Answer generated ({len(answer)} chars)")

        answer = _filter_pii(answer)

        if session_id:
            wiki_sessions[session_id].append({'role': 'user', 'content': question})
            wiki_sessions[session_id].append({'role': 'assistant', 'content': answer})
            if len(wiki_sessions[session_id]) > 20:
                wiki_sessions[session_id] = wiki_sessions[session_id][-20:]

        return {'answer': answer, 'model': model, 'session_id': session_id}

    except subprocess.TimeoutExpired:
        logger.error("ollama claude timed out")
        return {'error': 'Request timed out (5 min limit)'}
    except Exception as e:
        logger.error(f"ask_wiki error: {e}")
        return {'error': str(e)}


@app.route('/ask_wiki', methods=['POST'])
def ask_wiki():
    """
    Ask a question based on the wiki knowledge base.

    Request: { "question": "...", "model": "...", "session_id": "..." }
    Response: { "question": "...", "answer": "...", "model": "...", "session_id": "..." }
    """
    data = request.get_json()
    if not data or 'question' not in data:
        return jsonify({'error': 'Missing question parameter'}), 400

    question = data['question']
    model = data.get('model', 'minimax-m2.7:cloud')
    session_id = data.get('session_id')

    result = _ask_wiki_internal(question, model=model, session_id=session_id)
    if 'error' in result:
        return jsonify({'error': result['error']}), 500

    return jsonify({
        'question': question,
        'answer': result['answer'],
        'model': result['model'],
        'session_id': result['session_id']
    })


@app.route('/lint_wiki', methods=['POST'])
def lint_wiki():
    """
    Run wiki health check (lint operation).

    Checks for:
    - Contradictions between pages
    - Stale claims superseded by newer sources
    - Orphan pages with no inbound links
    - Missing cross-references
    - Broken links
    - Metadata consistency

    Request body (optional):
    {
        "model": "minimax-m2.7:cloud"
    }

    Response:
    {
        "status": "completed",
        "report": "...",
        "model": "minimax-m2.7:cloud"
    }
    """
    data = request.get_json() or {}
    model = data.get('model', 'minimax-m2.7:cloud')

    repo_root = Path(__file__).parent
    wiki_dir = repo_root / 'wiki'
    llm_wiki_path = repo_root / 'llm-wiki.md'
    project_schema_path = wiki_dir / 'WIKI.md'

    if not wiki_dir.exists():
        return jsonify({'error': 'wiki/ directory not found'}), 500

    try:
        llm_wiki_content = llm_wiki_path.read_text(encoding='utf-8') if llm_wiki_path.exists() else ""
        project_schema_content = project_schema_path.read_text(encoding='utf-8') if project_schema_path.exists() else ""
    except Exception as e:
        logger.error(f"Failed to read schema files: {e}")
        return jsonify({'error': f'Failed to read schema: {str(e)}'}), 500

    prompt = f"""You are maintaining an AI news wiki. Run a health check (lint operation).

=== WIKI PATTERN (llm-wiki.md) ===
{llm_wiki_content}

=== PROJECT SCHEMA (WIKI.md) ===
{project_schema_content}

=== AVAILABLE TOOLS ===

You have access to the following SQL query tool running on localhost:5002:

**SQL Query** (structured queries on AI news database):
   curl -X POST http://localhost:5002/query \\
     -H "Content-Type: application/json" \\
     -d '{{"sql": "SELECT title_en, description_en FROM ai_news WHERE ..."}}'

   Available tables:
   - github_repos: name, url, description_en, description_zh, stars, forks, date_added
   - ai_news: title_en, title_zh, url, source, time, description_en, description_zh, date_added
   - insights: date, content_en, content_zh

=== YOUR TASK ===

Working directory: {repo_root}

Run a comprehensive health check on wiki/. Check all 5 directories: topics/, sources/, timelines/, entities/, ideas/.

STRUCTURAL CHECKS:
1. **Contradictions**: Do different pages make conflicting claims?
2. **Stale content**: Has newer content superseded old claims?
3. **Orphan pages**: Pages with no inbound links across all directories
4. **Missing cross-references**: Topics/sources/entities that should be linked but aren't
5. **Broken links**: [[references]] that don't have a corresponding page
6. **Index completeness**: Does wiki/index.md list all pages in all 5 directories?

CONNECTION QUALITY CHECKS:
7. **Shallow links**: Connections that just say "Related:", "See also:", or link without annotation → REWRITE with WHY
8. **Missing entities**: Models, products, protocols mentioned in topics/sources but lacking entity pages → create them
9. **Missing ideas**: Recurring themes in daily insights that deserve their own idea page → create them
10. **Topic pages missing ## Evolution**: Write a chronological narrative, not just a list
11. **Topic pages missing ## Patterns & Insights**: Synthesize from events
12. **Companies in entities/**: Company pages belong in sources/, not entities/ → flag
13. **People in entities/**: Entities are for technical things only → flag

Read wiki/index.md, then systematically check all pages in topics/, sources/, timelines/, entities/, ideas/.

After identifying issues:
1. Report all problems found
2. Fix what you can (update pages, add missing links, rewrite shallow connections)
3. Update wiki/log.md with a lint entry

Provide a summary report of what you found and fixed.
"""

    try:
        logger.info("Running wiki lint operation...")
        result = subprocess.run(
            [
                'ollama', 'launch', 'claude',
                '--model', model,
                '--yes',
                '--',
                '-p', prompt,
                '--permission-mode', 'dontAsk'
            ],
            capture_output=True,
            text=True,
            cwd=str(repo_root),
            timeout=600  # 10 minutes timeout for lint
        )

        if result.returncode != 0:
            logger.error(f"ollama claude failed: {result.stderr}")
            return jsonify({'error': f'Lint failed: {result.stderr}'}), 500

        report = result.stdout.strip()
        logger.info(f"Lint completed ({len(report)} chars)")

        return jsonify({
            'status': 'completed',
            'report': report,
            'model': model
        })

    except subprocess.TimeoutExpired:
        logger.error("ollama claude timed out during lint")
        return jsonify({'error': 'Lint timed out (10 min limit)'}), 504
    except Exception as e:
        logger.error(f"lint_wiki error: {e}")
        return jsonify({'error': str(e)}), 500


def run_daily_lint():
    """Background thread that runs wiki lint every day."""
    DAY_SECONDS = 24 * 60 * 60

    while True:
        try:
            time.sleep(DAY_SECONDS)
            logger.info("Running scheduled daily wiki lint...")

            repo_root = Path(__file__).parent
            wiki_dir = repo_root / 'wiki'

            if not wiki_dir.exists():
                logger.warning("wiki/ directory not found, skipping scheduled lint")
                continue

            llm_wiki_path = repo_root / 'llm-wiki.md'
            project_schema_path = wiki_dir / 'WIKI.md'

            llm_wiki_content = llm_wiki_path.read_text(encoding='utf-8') if llm_wiki_path.exists() else ""
            project_schema_content = project_schema_path.read_text(encoding='utf-8') if project_schema_path.exists() else ""

            prompt = f"""You are maintaining an AI news wiki. Run a daily health check (lint operation).

=== WIKI PATTERN (llm-wiki.md) ===
{llm_wiki_content}

=== PROJECT SCHEMA (WIKI.md) ===
{project_schema_content}

=== YOUR TASK ===

Working directory: {repo_root}

This is a scheduled daily health check. Check all 5 directories: topics/, sources/, timelines/, entities/, ideas/.

STRUCTURAL:
1. Contradictions between pages
2. Stale content superseded by newer sources
3. Orphan pages (no inbound links) across all directories
4. Missing cross-references
5. Broken [[wikilinks]]

CONNECTION QUALITY:
6. Shallow connections that just say "Related:" or "See also:" → rewrite with WHY
7. Missing entity pages for models/products/protocols mentioned in topics/sources
8. Missing idea pages for recurring themes
9. Topic pages missing ## Evolution or ## Patterns & Insights → add them
10. Companies in entities/ → move to sources/

Fix what you can, and update wiki/log.md with a lint entry.

Provide a summary report.
"""

            result = subprocess.run(
                [
                    'ollama', 'launch', 'claude',
                    '--model', 'minimax-m2.7:cloud',
                    '--yes',
                    '--',
                    '-p', prompt,
                    '--permission-mode', 'dontAsk'
                ],
                capture_output=True,
                text=True,
                cwd=str(repo_root),
                timeout=600
            )

            if result.returncode == 0:
                logger.info(f"Daily lint completed successfully ({len(result.stdout)} chars)")
            else:
                logger.error(f"Daily lint failed: {result.stderr}")

        except Exception as e:
            logger.error(f"Error in daily lint thread: {e}")


def main():
    parser = argparse.ArgumentParser(description='AI News Search Service')
    parser.add_argument('--db', type=str, default='ai_news.sqlite',
                        help='Path to SQLite database (default: ai_news.sqlite)')
    parser.add_argument('--port', type=int, default=5002,
                        help='Port to run on (default: 5002)')
    parser.add_argument('--host', type=str, default='0.0.0.0',
                        help='Host to bind to (default: 0.0.0.0)')

    args = parser.parse_args()

    # Set global DB path
    global DB_PATH
    DB_PATH = Path(args.db)

    if not DB_PATH.exists():
        print(f"Error: Database not found at {DB_PATH}")
        print("Run 'python build_sqlite.py' first to create the database.")
        return 1

    print("=" * 60)
    print("AI News Search Service")
    print("=" * 60)
    print(f"Database: {DB_PATH}")
    print(f"Server: http://{args.host}:{args.port}")
    print("=" * 60)
    print()
    print("Endpoints:")
    print("  - GET  /health          Health check")
    print("  - GET  /schema          Database schema")
    print("  - GET  /stats           Database statistics")
    print("  - POST /query           SQL queries")
    print("  - POST /ask_wiki        Wiki-based Q&A")
    print("  - POST /lint_wiki       Wiki health check (manual)")
    print("  - Daily automated lint enabled")
    print()

    # Start weekly lint background thread
    logger.info("Starting weekly lint background thread...")
    lint_thread = threading.Thread(target=run_daily_lint, daemon=True)
    lint_thread.start()

    # Run Flask
    app.run(host=args.host, port=args.port, debug=False)

    return 0


if __name__ == '__main__':
    exit(main())
