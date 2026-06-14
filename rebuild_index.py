#!/usr/bin/env python3
import os
import re
from pathlib import Path
from datetime import datetime

REPO_ROOT = Path(__file__).parent
PAGES_DIR = REPO_ROOT / "pages"
INDEX_FILE = REPO_ROOT / "index.html"

def format_date(date_str):
    """Convert 2026-06-14 to June 14, 2026."""
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return dt.strftime("%B %d, %Y")
    except ValueError:
        return date_str

def rebuild_index():
    # Get all html files in pages/
    pages = list(PAGES_DIR.glob("*.html"))

    # Extract dates and sort descending
    dates = []
    for p in pages:
        date_part = p.stem # 2026-06-14
        if re.match(r"^\d{4}-\d{2}-\d{2}$", date_part):
            dates.append(date_part)

    dates.sort(reverse=True)

    # Build HTML for the list
    items_html = '<div class="archive-list">\n'
    for d in dates:
        display_date = format_date(d)
        items_html += f'''        <div class="archive-item">
            <a href="pages/{d}.html" class="date-link">
                {display_date}
            </a>
            <span class="arrow">→</</span>
        </div>
'''
    items_html += '    </div>'

    # Total count
    total_count = len(dates)

    # Read index.html
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace content between markers
    start_marker = "<!-- ARCHIVE_ITEMS_START -->"
    end_marker = "<!-- ARCHIVE_ITEMS_END -->"

    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)

    if start_idx == -1 or end_idx == -1:
        print("Markers not found in index.html")
        return 1

    # Replace the inner content
    new_content = content[:start_idx + len(start_marker)] + "\n" + items_html + "\n" + content[end_idx:]

    # Update total count in the footer
    # Look for <span class="total-count">...</span>
    new_content = re.sub(
        r'(<span class="total-count">).*?(</span>)',
        lambda m: f"{m.group(1)}{total_count}{m.group(2)}",
        new_content
    )

    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✓ Rebuilt index.html with {total_count} entries")
    return 0

if __name__ == "__main__":
    exit(rebuild_index())
