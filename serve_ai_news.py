#!/usr/bin/env python3
"""
AI News Search Service
======================

Flask service providing SQL query interface for AI News database.

Usage:
    python serve_ai_news.py --port 5002
"""

import argparse
import sqlite3
import json
import logging
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
    print()

    # Run Flask
    app.run(host=args.host, port=args.port, debug=False)

    return 0


if __name__ == '__main__':
    exit(main())
