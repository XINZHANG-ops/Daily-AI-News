import glob

for f in glob.glob('/Users/xinzhang/Daily-AI-News/wiki/**/*.md', recursive=True):
    if 'index.md' in f or 'log.md' in f or 'WIKI.md' in f:
        continue
    with open(f) as fh:
        lines = fh.readlines()
    in_table = False
    cols = 0
    for i, line in enumerate(lines, 1):
        if line.strip().startswith('|'):
            parts = [p.strip() for p in line.strip().split('|')]
            parts = [p for p in parts if p]
            if not in_table:
                in_table = True
                cols = len(parts)
            else:
                if len(parts) \!= cols and '---' not in line and not all(set(p) <= set(' -|') for p in parts):
                    print(f'BAD TABLE {f}:{i} ({len(parts)} cols, expected {cols}): {line.strip()[:80]}')
        else:
            in_table = False
            cols = 0
