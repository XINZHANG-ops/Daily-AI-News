#!/usr/bin/env python3
"""
Build SQLite database from JSON data files.
Usage: python3 build_sqlite.py
"""

import json
import sqlite3
from pathlib import Path

REPO_ROOT = Path(__file__).parent
DATA_DIR = REPO_ROOT / "data"
DB_PATH = REPO_ROOT / "ai_news.sqlite"


def create_tables(conn):
    """Create database tables."""
    cur = conn.cursor()

    # Drop existing tables
    cur.execute("DROP TABLE IF EXISTS github_repos")
    cur.execute("DROP TABLE IF EXISTS ai_news")
    cur.execute("DROP TABLE IF EXISTS insights")

    # GitHub Repositories table
    cur.execute("""
    CREATE TABLE github_repos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        url TEXT,
        description_en TEXT,
        description_zh TEXT,
        stars TEXT,
        forks TEXT,
        date_added TEXT NOT NULL
    )
    """)

    # AI News table
    cur.execute("""
    CREATE TABLE ai_news (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title_en TEXT,
        title_zh TEXT,
        url TEXT,
        source TEXT,
        time TEXT,
        description_en TEXT,
        description_zh TEXT,
        date_added TEXT NOT NULL
    )
    """)

    # Daily Insights table
    cur.execute("""
    CREATE TABLE insights (
        date TEXT PRIMARY KEY,
        content_en TEXT,
        content_zh TEXT
    )
    """)

    # Create indexes for faster queries
    cur.execute("CREATE INDEX idx_repos_date ON github_repos(date_added)")
    cur.execute("CREATE INDEX idx_repos_name ON github_repos(name)")
    cur.execute("CREATE INDEX idx_news_date ON ai_news(date_added)")
    cur.execute("CREATE INDEX idx_news_source ON ai_news(source)")

    conn.commit()
    print("✓ Created tables with indexes")


def insert_data(conn):
    """Insert data from JSON files."""
    cur = conn.cursor()

    # Get all JSON files sorted by date
    json_files = sorted(DATA_DIR.glob("*.json"))

    total_repos = 0
    total_news = 0
    total_insights = 0

    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        date = data.get('date')
        if not date:
            print(f"⚠ Skipping {json_file.name}: no date field")
            continue

        # Insert GitHub repos
        for repo in data.get('github_repos', []):
            desc = repo.get('description', {})
            if isinstance(desc, str):
                desc_en = desc_zh = desc
            else:
                desc_en = desc.get('en', '')
                desc_zh = desc.get('zh', '')

            cur.execute("""
                INSERT INTO github_repos
                (name, url, description_en, description_zh, stars, forks, date_added)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                repo.get('name', ''),
                repo.get('url', ''),
                desc_en,
                desc_zh,
                repo.get('stars', ''),
                repo.get('forks', ''),
                date
            ))
            total_repos += 1

        # Insert AI news
        for news in data.get('ai_news', []):
            title = news.get('title', {})
            if isinstance(title, str):
                title_en = title_zh = title
            else:
                title_en = title.get('en', '')
                title_zh = title.get('zh', '')

            desc = news.get('description', {})
            if isinstance(desc, str):
                desc_en = desc_zh = desc
            else:
                desc_en = desc.get('en', '')
                desc_zh = desc.get('zh', '')

            cur.execute("""
                INSERT INTO ai_news
                (title_en, title_zh, url, source, time, description_en, description_zh, date_added)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                title_en,
                title_zh,
                news.get('url', ''),
                news.get('source', ''),
                news.get('time', ''),
                desc_en,
                desc_zh,
                date
            ))
            total_news += 1

        # Insert insight
        insight = data.get('insight_analysis')
        if insight:
            if isinstance(insight, str):
                insight_en = insight_zh = insight
            else:
                insight_en = insight.get('en', '')
                insight_zh = insight.get('zh', '')

            cur.execute("""
                INSERT OR REPLACE INTO insights (date, content_en, content_zh)
                VALUES (?, ?, ?)
            """, (date, insight_en, insight_zh))
            total_insights += 1

    conn.commit()

    print(f"✓ Inserted {total_repos} GitHub repos")
    print(f"✓ Inserted {total_news} AI news items")
    print(f"✓ Inserted {total_insights} daily insights")


def main():
    print("=" * 60)
    print("Daily AI News - Build SQLite Database")
    print("=" * 60)
    print()

    # Create connection
    conn = sqlite3.connect(DB_PATH)

    try:
        # Create tables
        create_tables(conn)

        # Insert data
        insert_data(conn)

        print()
        print("=" * 60)
        print(f"✓ Database created successfully: {DB_PATH}")
        print("=" * 60)

    finally:
        conn.close()

    return 0


if __name__ == "__main__":
    exit(main())
