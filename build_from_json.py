#!/usr/bin/env python3
"""
Builds HTML pages from JSON data files.
Usage: python3 build_from_json.py data/2026-03-17.json
"""

import json
import sys
from pathlib import Path
from datetime import datetime

REPO_ROOT = Path(__file__).parent
PAGES_DIR = REPO_ROOT / "pages"
DATA_DIR = REPO_ROOT / "data"

def format_date(date_str):
    """Format YYYY-MM-DD to readable date."""
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return dt.strftime("%B %d, %Y")

def build_repo_card(repo):
    """Build HTML for a GitHub repo card."""
    return f'''                <div class="card">
                    <div class="card-header">
                        <div>
                            <a href="{repo['url']}" class="card-title" target="_blank">{repo['name']}</a>
                            <div class="card-meta">
                                <div class="meta-item"><span>⭐</span> {repo['stars']} stars</div>
                                <div class="meta-item"><span>🍴</span> {repo['forks']} forks</div>
                            </div>
                        </div>
                    </div>
                    <p class="card-description">{repo['description']}</p>
                </div>'''

def build_news_card(news):
    """Build HTML for a news card."""
    return f'''                <div class="card news-card">
                    <span class="news-source">{news['source']}</span>
                    <div class="news-time">{news['time']}</div>
                    <a href="{news['url']}" class="card-title" target="_blank">{news['title']}</a>
                    <p class="card-description">{news['description']}</p>
                </div>'''

def build_html(data):
    """Build full HTML page from JSON data."""
    date = data['date']
    display_date = format_date(date)
    
    repos_html = '\n'.join([build_repo_card(r) for r in data['github_repos']])
    news_html = '\n'.join([build_news_card(n) for n in data['ai_news']])
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI News Digest - {display_date}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
            min-height: 100vh;
            color: #e0e0e0;
            line-height: 1.6;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 20px;
        }}
        
        header {{
            text-align: center;
            margin-bottom: 50px;
            padding: 40px 0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }}
        
        h1 {{
            font-size: 3rem;
            font-weight: 700;
            background: linear-gradient(90deg, #00d4ff, #7b2cbf);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 15px;
            letter-spacing: -1px;
        }}
        
        .date-badge {{
            display: inline-block;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            padding: 10px 25px;
            border-radius: 30px;
            font-size: 1rem;
            color: #00d4ff;
            border: 1px solid rgba(0, 212, 255, 0.3);
        }}
        
        .section {{
            margin-bottom: 60px;
        }}
        
        .section-title {{
            font-size: 1.8rem;
            margin-bottom: 30px;
            display: flex;
            align-items: center;
            gap: 12px;
            color: #fff;
        }}
        
        .section-title span {{
            font-size: 2rem;
        }}
        
        .cards-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 25px;
        }}
        
        .card {{
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            padding: 25px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }}
        
        .card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, #00d4ff, #7b2cbf);
            opacity: 0;
            transition: opacity 0.3s ease;
        }}
        
        .card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
            border-color: rgba(0, 212, 255, 0.3);
        }}
        
        .card:hover::before {{
            opacity: 1;
        }}
        
        .card-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 15px;
        }}
        
        .card-title {{
            font-size: 1.3rem;
            font-weight: 600;
            color: #fff;
            text-decoration: none;
            display: block;
            margin-bottom: 5px;
            transition: color 0.2s ease;
        }}
        
        .card-title:hover {{
            color: #00d4ff;
        }}
        
        .card-meta {{
            display: flex;
            gap: 15px;
            font-size: 0.85rem;
            color: #888;
        }}
        
        .meta-item {{
            display: flex;
            align-items: center;
            gap: 5px;
        }}
        
        .meta-item span {{
            color: #ffd700;
        }}
        
        .card-description {{
            color: #b0b0b0;
            font-size: 0.95rem;
            line-height: 1.6;
        }}
        
        .news-card .card-title {{
            font-size: 1.15rem;
            margin-top: 10px;
        }}
        
        .news-source {{
            display: inline-block;
            background: rgba(0, 212, 255, 0.15);
            color: #00d4ff;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 500;
        }}
        
        .news-time {{
            color: #888;
            font-size: 0.8rem;
            margin-top: 8px;
            margin-bottom: 5px;
        }}
        
        footer {{
            text-align: center;
            padding: 40px 0;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            color: #666;
            font-size: 0.9rem;
        }}
        
        footer a {{
            color: #00d4ff;
            text-decoration: none;
        }}
        
        @media (max-width: 768px) {{
            h1 {{
                font-size: 2rem;
            }}
            
            .cards-grid {{
                grid-template-columns: 1fr;
            }}
            
            .section-title {{
                font-size: 1.4rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🤖 Daily AI News Digest</h1>
            <div class="date-badge">📅 {display_date}</div>
        </header>

        <section class="section">
            <h2 class="section-title"><span>🐙</span> Trending GitHub Repositories</h2>
            <div class="cards-grid">
{repos_html}
            </div>
        </section>

        <section class="section">
            <h2 class="section-title"><span>🤖</span> AI News & Updates</h2>
            <div class="cards-grid">
{news_html}
            </div>
        </section>

        <footer>
            <p>Generated automatically • Daily AI News Digest</p>
        </footer>
    </div>
</body>
</html>'''
    
    return html

def main():
    if len(sys.argv) < 2:
        # Find the most recent JSON file
        json_files = sorted(DATA_DIR.glob("*.json"))
        if not json_files:
            print("No JSON files found in data/ directory")
            return 1
        json_path = json_files[-1]
    else:
        json_path = Path(sys.argv[1])
    
    # Read JSON
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Build HTML
    html = build_html(data)
    
    # Save HTML
    output_path = PAGES_DIR / f"{data['date']}.html"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✓ Built {output_path}")
    return 0

if __name__ == "__main__":
    exit(main())
