#!/usr/bin/env python3
"""
Rebuilds the index.html with links to all pages in the pages/ directory.
Also commits and pushes changes to git.
"""

import os
import re
import subprocess
from datetime import datetime
from pathlib import Path

# Configuration
PAGES_DIR = Path("pages")
INDEX_FILE = Path("index.html")
REPO_ROOT = Path(__file__).parent

def get_page_files():
    """Get all HTML files in pages directory, sorted by date (newest first)."""
    pages_path = REPO_ROOT / PAGES_DIR
    if not pages_path.exists():
        return []
    
    files = []
    for f in pages_path.glob("*.html"):
        # Extract date from filename (YYYY-MM-DD.html)
        match = re.match(r'(\d{4}-\d{2}-\d{2})\.html$', f.name)
        if match:
            date_str = match.group(1)
            try:
                date_obj = datetime.strptime(date_str, "%Y-%m-%d")
                files.append((date_obj, date_str, f.name))
            except ValueError:
                continue
    
    # Sort by date descending (newest first)
    files.sort(reverse=True)
    return files

def format_date_display(date_str):
    """Format YYYY-MM-DD to a nice readable date."""
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    return date_obj.strftime("%B %d, %Y")

def build_archive_html(files):
    """Build the archive list HTML."""
    if not files:
        return '''<div class="empty-state">
            <div class="empty-state-icon">📭</div>
            <p>No news archives yet. Check back tomorrow!</p>
        </div>'''
    
    items_html = ['<div class="archive-list">']
    
    for date_obj, date_str, filename in files:
        display_date = format_date_display(date_str)
        items_html.append(f'''        <div class="archive-item">
            <a href="pages/{filename}" class="date-link">
                {display_date}
            </a>
            <span class="arrow">→</span>
        </div>''')
    
    items_html.append('    </div>')
    items_html.append(f'    <p style="text-align: center; margin-top: 30px; color: #888;">Total archives: <span class="total-count">{len(files)}</span></p>')
    
    return '\n'.join(items_html)

def rebuild_index():
    """Rebuild the index.html file."""
    files = get_page_files()
    
    if not INDEX_FILE.exists():
        print(f"Error: {INDEX_FILE} not found!")
        return False
    
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the marker comments and replace content between them
    pattern = r'(<!-- ARCHIVE_ITEMS_START -->).*?(<!-- ARCHIVE_ITEMS_END -->)'
    replacement = f'<!-- ARCHIVE_ITEMS_START -->\n{build_archive_html(files)}\n            <!-- ARCHIVE_ITEMS_END -->'
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✓ Rebuilt index.html with {len(files)} archive(s)")
    return True

def run_git_commands():
    """Run git add, commit, and push."""
    os.chdir(REPO_ROOT)
    
    # Check if this is a git repo
    result = subprocess.run(['git', 'rev-parse', '--git-dir'], 
                          capture_output=True, text=True)
    if result.returncode != 0:
        print("Error: Not a git repository!")
        return False
    
    # Git add -A
    result = subprocess.run(['git', 'add', '-A'], 
                          capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error during git add: {result.stderr}")
        return False
    print("✓ git add -A")
    
    # Check if there are changes to commit
    result = subprocess.run(['git', 'diff', '--cached', '--quiet'])
    if result.returncode == 0:
        print("No changes to commit.")
        return True
    
    # Git commit
    today = datetime.now().strftime("%Y-%m-%d")
    commit_msg = f"Update: Add AI news for {today}"
    result = subprocess.run(['git', 'commit', '-m', commit_msg], 
                          capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error during git commit: {result.stderr}")
        return False
    print(f"✓ git commit -m \"{commit_msg}\"")
    
    # Git push
    result = subprocess.run(['git', 'push'], 
                          capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error during git push: {result.stderr}")
        return False
    print("✓ git push")
    
    return True

def main():
    print("=" * 50)
    print("Daily AI News - Rebuild Index & Deploy")
    print("=" * 50)
    print()
    
    # Step 1: Rebuild index
    if not rebuild_index():
        print("Failed to rebuild index.")
        return 1
    print()
    
    # Step 2: Git operations
    if not run_git_commands():
        print("Git operations failed.")
        return 1
    print()
    
    print("=" * 50)
    print("✓ Done! Site updated and deployed.")
    print("=" * 50)
    return 0

if __name__ == "__main__":
    exit(main())
