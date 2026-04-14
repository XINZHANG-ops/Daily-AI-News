#!/bin/bash
# Daily AI News Service Supervisor
# Monitors git repo for updates and automatically rebuilds + restarts service

REPO_DIR="/Users/xinzhang/Daily-AI-News"
SERVICE_PORT=5002
INTERVAL=600  # Check every 10 minutes
LOG_FILE="/tmp/ai_news_supervisor.log"

cd "$REPO_DIR" || exit 1

# Function to rebuild database and restart service
rebuild_and_restart() {
    echo "[$(date)] Rebuilding database..." | tee -a "$LOG_FILE"

    # Rebuild SQLite from JSON
    python3 build_sqlite.py >> "$LOG_FILE" 2>&1
    if [ $? -eq 0 ]; then
        echo "[$(date)] ✓ Database rebuilt successfully" | tee -a "$LOG_FILE"
    else
        echo "[$(date)] ✗ Database rebuild failed" | tee -a "$LOG_FILE"
        return 1
    fi

    # Kill existing service
    pkill -f "serve_ai_news.py"
    sleep 2

    # Start new service
    nohup python3 serve_ai_news.py --port $SERVICE_PORT >> /tmp/ai_news_server.log 2>&1 &
    SERVICE_PID=$!
    echo "[$(date)] ✓ Service restarted with PID: $SERVICE_PID" | tee -a "$LOG_FILE"

    # Wait a moment and check if service is running
    sleep 2
    if curl -s http://localhost:$SERVICE_PORT/health > /dev/null 2>&1; then
        echo "[$(date)] ✓ Service health check passed" | tee -a "$LOG_FILE"
    else
        echo "[$(date)] ✗ Service health check failed" | tee -a "$LOG_FILE"
        return 1
    fi

    return 0
}

# Initial startup
echo "[$(date)] Starting Daily AI News Service Supervisor" | tee -a "$LOG_FILE"
echo "[$(date)] Repository: $REPO_DIR" | tee -a "$LOG_FILE"
echo "[$(date)] Service Port: $SERVICE_PORT" | tee -a "$LOG_FILE"
echo "[$(date)] Check Interval: ${INTERVAL}s ($(($INTERVAL / 60)) minutes)" | tee -a "$LOG_FILE"
echo "---" | tee -a "$LOG_FILE"

# Start service initially
rebuild_and_restart

# Monitor loop
while true; do
    # Fetch latest from origin
    git fetch origin main >> "$LOG_FILE" 2>&1

    # Check if local is behind remote
    LOCAL=$(git rev-parse HEAD)
    REMOTE=$(git rev-parse origin/main)

    if [ "$LOCAL" != "$REMOTE" ]; then
        echo "[$(date)] Detected update (local: ${LOCAL:0:7}, remote: ${REMOTE:0:7})" | tee -a "$LOG_FILE"

        # Pull changes
        git pull origin main >> "$LOG_FILE" 2>&1
        if [ $? -eq 0 ]; then
            echo "[$(date)] ✓ Git pull successful" | tee -a "$LOG_FILE"

            # Rebuild and restart
            rebuild_and_restart
        else
            echo "[$(date)] ✗ Git pull failed" | tee -a "$LOG_FILE"
        fi
    else
        # Just log heartbeat every 10 checks (100 minutes)
        CHECK_COUNT=$((${CHECK_COUNT:-0} + 1))
        if [ $((CHECK_COUNT % 10)) -eq 0 ]; then
            echo "[$(date)] Heartbeat: No updates (checked $CHECK_COUNT times)" >> "$LOG_FILE"
        fi
    fi

    sleep $INTERVAL
done
