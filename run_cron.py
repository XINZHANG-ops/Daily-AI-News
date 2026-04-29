#!/usr/bin/env python3
"""Cron launcher for Daily AI News Digest — invokes ollama claude with the full prompt."""
import subprocess, sys, os
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo

BASE_DIR = "/Users/xinzhang/Daily-AI-News"
os.environ["PATH"] = "/usr/local/bin:/Users/xinzhang/.local/bin:/opt/homebrew/bin:" + os.environ.get("PATH", "")
CLAUDE_CMD = ["/usr/local/bin/ollama", "launch", "claude", "--model", "minimax-m2.7:cloud", "--"]

toronto = ZoneInfo("America/Toronto")
now_toronto = datetime.now(toronto)
now_utc = datetime.now(timezone.utc)

# Match the format from the original OpenClaw job
weekday_names = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
month_names = ["January","February","March","April","May","June","July","August","September","October","November","December"]
day = now_toronto.day
suffix = "th" if 11 <= day <= 13 else {1:"st",2:"nd",3:"rd"}.get(day%10,"th")
weekday_str = weekday_names[now_toronto.weekday()]
month_str = month_names[now_toronto.month - 1]
hour_12 = now_toronto.strftime("%-I:%M %p")
current_time_str = f"{weekday_str}, {month_str} {day}{suffix}, {now_toronto.year} - {hour_12} (America/Toronto) / {now_utc.strftime('%Y-%m-%d %H:%M')} UTC"
today_str = now_toronto.strftime("%Y-%m-%d")

prompt = f"""Generate a daily AI news digest with JSON data first, then build HTML.

## STEP 1: Collect Data and Save as JSON

### Deduplication - Load Existing History
BEFORE searching, read all JSON files in /Users/xinzhang/Daily-AI-News/data/ from the last 30 days.
Extract ALL repo names from each file's "github_repos" array (the "name" field like "owner/repo").
Create a blacklist of these repos to avoid duplicates across days.

### Collect New Data (BILINGUAL - EN/ZH)
1. NEW trending GitHub repos (AI/ML related, created in last 7 days)
   - Check Hacker News "Show HN", Reddit r/MachineLearning, GitHub search, Twitter/X, tech blogs
   - **CRITICAL: MUST extract the EXACT GitHub URL from search results**
   - Filter OUT repos that exist in the blacklist (appeared in last 30 days)
   - Pick top 3 fresh repos with stars/forks that are NOT duplicates
   - **CRITICAL VALIDATION (MANDATORY):** After selecting repos, run this command for EACH repo URL to verify it exists:
     curl -sI "https://github.com/owner/repo" | head -1
     If the result is NOT "HTTP/2 200", discard that repo immediately and find a replacement. Do NOT include any 404 or unreachable repos in the final JSON.

2. AI News from the past day (5-8 stories)

Then create a JSON file at /Users/xinzhang/Daily-AI-News/data/{today_str}.json with this BILINGUAL structure:
```json
{{
  "date": "{today_str}",
  "github_repos": [
    {{
      "name": "owner/repo",
      "url": "https://github.com/owner/repo",
      "description": {{"en": "Original English description", "zh": "中文翻译的描述"}},
      "stars": "2.8k",
      "forks": "312"
    }}
  ],
  "ai_news": [
    {{
      "title": {{"en": "Original English title", "zh": "中文翻译的标题"}},
      "url": "...",
      "source": "...",
      "time": "...",
      "description": {{"en": "Original English description", "zh": "中文翻译的描述"}},
      "insight": {{"en": "Why this matters - connects dots, gives context, tells the reader what's the significance or how it connects to broader trends or other items you encountered during your research today", "zh": "为什么重要 - 打通红绿灯上下文、点出意义、串联你搜索过程中看到的相关信息、揭示这一天真正的故事线"}}
    }}
  ],
  "insight_analysis": {{
    "en": "Deep dive paragraph in English - synthesize the day's events into a coherent narrative. What is the real story? What patterns emerge? What matters beyond the obvious? Write like an analyst, not a newscaster.",
    "zh": "深度中文分析段落 - 将当天的事件综合成一个连贯的叙事。真正的主题是什么？出现什么模式？什么是显而易见之外的重要事项？像分析师而非新闻播报员那样写作。"
  }}
}}
```

**IMPORTANT:** All text fields must be objects with "en" and "zh" keys. Keep original English in "en", provide Chinese translations in "zh".

## STEP 2: Writing Style - "打通" Each News Item

The key difference: every news item should have an "insight" that does NOT just restate the news, but ADDS value:

**横向打通 (Cross-reference):**
- During your research, you read many news across many sources. As you write each item's insight, draw connections to things you saw during your search—even if they didn't make it into the final digest.
- If two companies made moves on the same day, connect them. If a new product echoes a trend you saw elsewhere, say so. If something seems small but connects to something bigger, surface that.
- Example: "This launch came three days after [X company]'s announcement of [Y], positioning them in direct competition for [use case]. Meanwhile, [Z company] announced something related from the other side of the market."

**纵向深挖 (So what?):**
- Don't just describe what happened — tell me why I should care
- If there's a number, explain what it means relative to alternatives or historical context
- If a company made a move, connect it to their broader strategy or the competitive landscape

**Contextual comparison:**
- Use "vs", "compared to", "surpassing", "trailing" to frame data against competitors
- When a model scores 87.6%, say "X points above the previous best" and if relevant note the trade-off (e.g., token consumption increased)

**The day's real story:**
- Try to identify what the real narrative of this particular day is—not just a list of events, but what they collectively reveal
- Sometimes several seemingly unrelated items all point to the same underlying shift; surface that pattern

**Writing voice:**
- Like an analyst writing for a sophisticated reader, not a news wire service
- Each item should feel like it was written by someone who sees the whole picture
- No filler phrases like "In recent days" or "With the development of AI"
- Every sentence should carry information weight

**Format: Use numbered list style similar to the example:**
Each item: `NN *Title* : context, comparison, connection, so-what.`

Example of good insight writing:
- ❌ "Anthropic released Claude Opus 4.7 with 87.6% on SWE-bench, maintaining $5/M token pricing."
- ✅ "Anthropic releases Claude Opus 4.7 (SWE-bench 87.6%, +6.8pts over 4.6) at unchanged $5/M pricing—but new tokenizer makes same inputs 1.0-1.35x costlier, a trade-off the memo didn't mention."

## STEP 3: Build HTML from JSON

Run: cd /Users/xinzhang/Daily-AI-News && python3 build_from_json.py data/{today_str}.json

## STEP 4: Git Operations

Run: cd /Users/xinzhang/Daily-AI-News && git pull && python3 rebuild_index.py
Current time: {current_time_str}"""

os.makedirs(os.path.join(BASE_DIR, "logs"), exist_ok=True)

print(f"[{datetime.now().isoformat()}] Starting Daily AI News Digest")
sys.stdout.flush()

result = subprocess.run(
    CLAUDE_CMD + [
        "--print", "-p", prompt,
        "--max-turns", "50",
        "--dangerously-skip-permissions",
    ],
    cwd=BASE_DIR,
    timeout=1800,
)

print(f"[{datetime.now().isoformat()}] Done (exit code {result.returncode})")
sys.exit(result.returncode)
