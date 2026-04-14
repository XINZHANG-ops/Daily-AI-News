# Daily AI News - AI 助手集成设置指南

## 架构说明

```
┌─────────────────────────────────────┐
│  Daily-AI-News (Mac mini)           │
│  - serve_ai_news.py (port 5002)     │  ← AI News 服务（本机）
│  - ai_news.sqlite                   │
│  - supervisor.sh (监控更新)          │
└─────────────────────────────────────┘
                ↓ HTTP
┌─────────────────────────────────────┐
│  AI Server (Windows, port 8080)     │
│  - server.py                        │  ← 主服务器
│  - 调用 AI News 服务获取数据          │
└─────────────────────────────────────┘
                ↓ HTTP
┌─────────────────────────────────────┐
│  用户浏览器                          │
│  - index.html (主页)                │
│  - pages/YYYY-MM-DD.html (分页)    │
│  - AI 助手（右下角紫色按钮）          │
└─────────────────────────────────────┘
```

## 1. Mac Mini 配置（AI News 服务端）

### 1.1 启动 AI News 服务

```bash
cd /Users/xinzhang/Daily-AI-News

# 手动启动（测试用）
python3 serve_ai_news.py --port 5002

# 使用 supervisor 自动管理（推荐）
chmod +x supervisor.sh
nohup ./supervisor.sh > /tmp/ai_news_supervisor.log 2>&1 &
```

### 1.2 Supervisor 功能

- 每 10 分钟检查一次 git 更新
- 自动 git pull
- 自动重建 SQLite 数据库
- 自动重启服务
- 健康检查

### 1.3 验证服务

```bash
# 检查健康
curl http://localhost:5002/health

# 查看统计
curl http://localhost:5002/stats

# 测试 SQL 查询
curl -X POST http://localhost:5002/query \
  -H "Content-Type: application/json" \
  -d '{"sql": "SELECT name, stars FROM github_repos LIMIT 3"}'
```

### 1.4 查看日志

```bash
# 服务日志
tail -f /tmp/ai_news_server.log

# Supervisor 日志
tail -f /tmp/ai_news_supervisor.log
```

## 2. Windows AI Server 配置

### 2.1 更新 .env 文件

在 Windows 的 `/Users/xinzhang/ai-server/.env` 添加：

```bash
# AI News Service (Mac mini)
AI_NEWS_SEARCH_HOST=http://10.0.0.28:5002
```

完整的相关配置：

```bash
# AI Provider
AI_PROVIDER=ollama

# Ollama Settings
OLLAMA_MODEL=ministral-3:8b
OLLAMA_EMBEDDING=embeddinggemma:300m

# Remote Services
MODEL_HOST=http://192.168.1.164:8081  # 如果使用远程模型服务
PAPER_SEARCH_HOST=http://10.0.0.28:5001  # Paper 搜索服务
AI_NEWS_SEARCH_HOST=http://10.0.0.28:5002  # AI News 搜索服务（新增）

# Repository Paths
DAILY_AI_NEWS_REPO=/path/to/Daily-AI-News  # 可选，仅供参考
```

### 2.2 重启 AI Server

```bash
cd /Users/xinzhang/ai-server
python server.py
```

查看启动日志确认：

```
✓ Initialized AI News knowledge from remote host: http://10.0.0.28:5002
```

## 3. 前端页面更新

### 3.1 重新生成所有页面

```bash
cd /Users/xinzhang/Daily-AI-News

# 生成所有页面（会自动包含 AI 助手）
for file in data/*.json; do
  python3 build_from_json.py "$file"
done

# 重建索引
python3 rebuild_index.py
```

### 3.2 AI 助手功能

**主页 (index.html)**:
- 右下角紫色渐变按钮 📰
- 点击打开聊天窗口
- Context 自动设置为 `ai_news`
- 可以询问 GitHub 仓库、AI 新闻、每日洞察

**分页 (pages/YYYY-MM-DD.html)**:
- 同样的 AI 助手
- 自动检测当前日期
- 可以针对当天内容提问

### 3.3 AI 助手样式

**配色方案**（匹配 Daily-AI-News）:
- 主色：紫色渐变 (#e94560 → #7b2cbf)
- 背景：深紫色 (#0f0c29, #302b63, #24243e)
- 强调色：粉红色 (#e94560)

与 daily_paper 的蓝紫色主题完全不同。

## 4. 测试流程

### 4.1 测试 Mac 服务

```bash
# 1. 检查服务运行
curl http://10.0.0.28:5002/health

# 2. 测试查询
curl -X POST http://10.0.0.28:5002/query \
  -H "Content-Type: application/json" \
  -d '{"sql": "SELECT title_en FROM ai_news LIMIT 2"}'
```

### 4.2 测试 AI Server 集成

在浏览器打开页面后：
1. 打开浏览器控制台
2. 检查是否有错误
3. 点击 AI 助手按钮
4. 输入问题："最近有什么 OpenAI 的新闻？"
5. 查看响应

### 4.3 检查 AI Server 日志

应该看到：

```
[CONTEXT CHECK] context_type = 'ai_news'
[AI NEWS SQL] Getting SQL context for: 最近有什么 OpenAI 的新闻？
########################################################################
SELECT title_en, description_en, time FROM ai_news WHERE ...
########################################################################
```

## 5. 常见问题

### Q: AI 助手无法连接？

检查：
1. AI Server 是否运行在 Windows (port 8080)
2. Ngrok tunnel 是否正常
3. `ai-assistant-config.js` 中的 ngrok URL 是否正确

### Q: 查询返回空结果？

检查：
1. Mac mini 的 AI News 服务是否运行 (port 5002)
2. SQLite 数据库是否存在且有数据
3. AI Server 的 `.env` 是否设置了 `AI_NEWS_SEARCH_HOST`

### Q: 样式不对？

确保：
1. `css/ai-assistant.css` 使用了紫色主题
2. 所有 JS 文件都正确引用
3. 浏览器缓存已清除 (Ctrl+Shift+R)

### Q: Context type 不对？

检查：
1. `ai-assistant-constants.js` 中 CONTEXT_TYPES 是否设置为 `ai_news`
2. `ai-assistant.js` 中 `setDefaultContextTag()` 是否查找 `ai_news`

## 6. 文件清单

### Mac Mini (Daily-AI-News)

```
/Users/xinzhang/Daily-AI-News/
├── serve_ai_news.py          # AI News 服务（port 5002）
├── build_sqlite.py           # 构建数据库脚本
├── supervisor.sh             # 自动监控和更新脚本
├── ai_news.sqlite            # SQLite 数据库
├── data/                     # JSON 数据文件
├── js/                       # AI 助手 JavaScript
│   ├── ai-assistant.js
│   ├── ai-assistant-*.js
│   └── ...
└── css/                      # AI 助手样式
    └── ai-assistant.css      # 紫色主题
```

### Windows (AI Server)

```
/Users/xinzhang/ai-server/
├── server.py                 # 主服务器
├── utils/
│   ├── ai_news_util.py      # AI News 知识库（远程调用）
│   └── ...
├── prompts/
│   ├── ai_news_sql_system.yaml  # AI News SQL 提示词
│   └── ...
└── .env                      # 环境配置（添加 AI_NEWS_SEARCH_HOST）
```

## 7. 下一步

1. ✅ 启动 Mac mini 的 AI News 服务
2. ✅ 配置 Windows AI Server 的 .env
3. ✅ 重启 AI Server
4. ✅ 重新生成所有页面
5. ✅ 测试 AI 助手功能
6. 🔄 部署到 GitHub Pages

---

**祝你好运！有问题随时问我。** 🚀
