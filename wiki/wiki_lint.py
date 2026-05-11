import os, re

wiki_dir = '/Users/xinzhang/Daily-AI-News/wiki'
all_pages = {}
all_links = {}

for root, dirs, files in os.walk(wiki_dir):
    for f in files:
        if f.endswith('.md'):
            path = os.path.join(root, f)
            rel = os.path.relpath(path, wiki_dir)
            slug = rel.replace('.md', '')
            with open(path) as fh:
                content = fh.read()
            all_pages[slug] = content
            all_links[slug] = set(re.findall(r'\[\[([^\]]+)\]\]', content))

print("=== ORPHAN PAGES ===")
for slug in sorted(all_pages):
    if slug in ('WIKI.md', 'index.md', 'log.md'):
        continue
    inbound = 0
    for other, links in all_links.items():
        if not (other == slug) and slug in links:
            inbound += 1
    if inbound == 0:
        print('ORPHAN:', slug)

print("\n=== BROKEN LINKS ===")
pages = set(all_pages.keys())
all_unique_links = set()
for links in all_links.values():
    all_unique_links.update(links)

for link in sorted(all_unique_links):
    if link not in pages:
        print('BROKEN:', link)

print("\n=== ENTITY PAGES THAT MIGHT BE PEOPLE ===")
people_patterns = ['karpathy', 'eliezer', 'andrej', 'dr-venus']
for slug in sorted(all_pages):
    if slug.startswith('entities/'):
        name = os.path.basename(slug)
        if any(p in name.lower() for p in people_patterns):
            print('PERSON?', slug)
