#!/usr/bin/env python3
import os
import re
from pathlib import Path
from datetime import datetime

REPO_ROOT = Path(__file__).parent
PAGES_DIR = REPO_ROOT / "pages"
INDEX_FILE = REPO_ROOT / "index.html"

def format_date(date_str):
    # Expects YYYY-MM-DD
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return dt.strftime("%B %d, %Y")
    except:
        return date_str

def main():
    if not INDEX_FILE.exists():
        print(f"Error: {INDEX_FILE} not found")
        return 1

    # Get all .html files in pages/
    pages = sorted(list(PAGES_DIR.glob("*.html")), reverse=True)

    items_html = '<div class="archive-list">\n'
    for page in pages:
        date_str = page.stem # YYYY-MM-DD
        display_date = format_date(date_str)
        items_html += f'''        <div class=archive-item>
            <a href="pages/{page.name}" class=date-link>
                {display_date}
            </a>
            <span class=arrow>→</span>
        </div>\n'''
    items_html += '</div>'

    # Read index.html and replace the block
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'(<!-- ARCHIVE_ITEMS_START -->)(.*)(<!-- ARCHIVE_ITEMS_END -->)'
    replacement = rf'\1\n{items_html}\n\3'

    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✓ Rebuilt index.html with {len(pages)} pages")
    return 0

if __name__ == "__main__":
    main()
