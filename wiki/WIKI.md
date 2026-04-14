# Daily AI News Wiki Schema

## Project Overview

This wiki tracks AI news, trending GitHub repositories, and daily insights from the AI industry.

## Data Sources

- **GitHub Repos**: Trending AI/ML repositories with star counts
- **AI News**: News articles from TechCrunch, Fortune, OpenAI, Anthropic, etc.
- **Daily Insights**: Curated analysis of daily trends

## Database Schema

### Tables

```sql
-- GitHub Repositories
github_repos (
    name TEXT,              -- e.g., "anthropics/claude-code"
    url TEXT,               -- GitHub URL
    description_en TEXT,    -- English description
    description_zh TEXT,    -- Chinese description  
    stars TEXT,             -- e.g., "100k+", "4.2k"
    forks TEXT,             -- e.g., "41.5k+"
    date_added TEXT         -- YYYY-MM-DD
)

-- AI News
ai_news (
    title_en TEXT,          -- English title
    title_zh TEXT,          -- Chinese title
    url TEXT,               -- Article URL
    source TEXT,            -- e.g., "TechCrunch", "Fortune"
    time TEXT,              -- e.g., "April 1, 2026"
    description_en TEXT,    -- English description
    description_zh TEXT,    -- Chinese description
    date_added TEXT         -- YYYY-MM-DD
)

-- Daily Insights
insights (
    date TEXT PRIMARY KEY,  -- YYYY-MM-DD
    content_en TEXT,        -- English analysis
    content_zh TEXT         -- Chinese analysis
)
```

## Wiki Organization

### Recommended Structure

```
wiki/
├── index.md                  # Main index
├── topics/
│   ├── llm_models.md        # LLM releases and updates
│   ├── ai_funding.md        # Funding rounds and valuations
│   ├── github_trends.md     # Trending repos analysis
│   └── ai_companies.md      # Company news and updates
├── sources/
│   ├── openai.md            # OpenAI timeline
│   ├── anthropic.md         # Anthropic timeline
│   ├── google.md            # Google AI news
│   └── meta.md              # Meta AI news
└── timelines/
    ├── 2026-04.md           # April 2026 summary
    └── 2026-03.md           # March 2026 summary
```

## How to Build Wiki

1. **Start with index.md**: Create main navigation
2. **Add topic pages**: As patterns emerge (e.g., multiple LLM releases)
3. **Create source pages**: Track companies/publications over time
4. **Build timelines**: Monthly summaries of key events

## SQL Query Examples

```sql
-- Recent AI news
SELECT title_en, source, time FROM ai_news 
WHERE date_added >= '2026-04-01' 
ORDER BY date_added DESC LIMIT 10;

-- Top GitHub repos
SELECT name, stars, description_en FROM github_repos 
ORDER BY LENGTH(stars) DESC, stars DESC LIMIT 10;

-- News by source
SELECT COUNT(*) as count, source FROM ai_news 
GROUP BY source ORDER BY count DESC;

-- Daily insight
SELECT content_en FROM insights 
WHERE date = '2026-04-13' LIMIT 1;
```

## Wiki Maintenance

- **Daily**: Add new significant events
- **Weekly**: Update source timelines
- **Monthly**: Create timeline summaries
- **As needed**: Create new topic pages when trends emerge

## Cross-Referencing

Use `[[page_name]]` to link:
- Topics to sources
- Sources to topics
- Timelines to both

Example:
```markdown
## Recent LLM Releases

- **2026-04-10**: [[openai]] announced GPT-5
- **2026-04-05**: [[anthropic]] released Claude Opus 4.7
- Related: [[llm_models]], [[ai_funding]]
```
