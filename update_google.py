import re

with open('wiki/sources/google.md', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'last_updated: 2026-06-09', 'last_updated: 2026-06-11', content)

timeline_entries = """
| 2026-06-10 | DiffusionGemma released | Text diffusion model achieving 1,000 tok/s on H100s using MoE; challenges Transformer latency. |
| 2026-06-11 | Munich court rules on AI Overviews | Court finds Google directly liable for hallucinations, ending the 'platform immunity' defense. |
"""
# Find the end of the Timeline table. It's just before ## Key Relationships
timeline_start = content.find('## Timeline')
relationships_start = content.find('## Key Relationships')
if timeline_start != -1 and relationships_start != -1:
    # The timeline table ends before the relationships section.
    # We should find the end of the actual table (last | line).
    lines = content.splitlines()
    table_end_line = 0
    for i in range(len(lines)-1, -1, -1):
        if lines[i].startswith('|') and i > timeline_start:
            table_end_line = i + 1
            break

    # If we didn't find a table line, just insert before relationships
    if table_end_line == 0:
        table_end_line = relationships_start

    # Reconstruct the content
    content = content[:table_end_line] + timeline_entries + content[table_end_line:]

connections_update = "\n- [[entities/diffusion-gemma.md]] — First major text diffusion model for ultra-fast generation.\n- [[ideas/platform-to-publisher-liability.md]] — Legal precedent set by Munich court regarding AI Overview hallucinations."
connections_start = content.find('## Connections')
if connections_start != -1:
    content = content[:connections_start+16] + connections_update + content[connections_start+16:]

with open('wiki/sources/google.md', 'w', encoding='utf-8') as f:
    f.write(content)
