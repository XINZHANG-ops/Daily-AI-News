import os, re
from pathlib import Path
from collections import defaultdict

wiki_dir = Path('wiki')
slugs_by_dir = defaultdict(list)
for d in ['topics', 'sources', 'timelines', 'entities', 'ideas']:
    p = wiki_dir / d
    if p.exists():
        for f in p.glob('*.md'):
            slugs_by_dir[d].append(f.stem)

for d, slugs in slugs_by_dir.items():
    sorted_slugs = sorted(slugs)
    for i, s in enumerate(sorted_slugs[:-1]):
        next_s = sorted_slugs[i+1]
        prefix = 0
        for a, b in zip(s, next_s):
            if a == b:
                prefix += 1
            else:
                break
        if prefix >= 6 and s \!= next_s:
            print(f'{d}/: {s} vs {next_s} (prefix {prefix})')
