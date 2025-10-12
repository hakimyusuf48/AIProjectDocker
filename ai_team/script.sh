#!/usr/bin/env bash
set -euo pipefail
PORT="${PORT:-5000}"
# simple placeholder content
cat > /app/index.html <<'HTML'
<!doctype html>
<html><body><h1>AI Team placeholder</h1></body></html>
HTML
exec python3 -m http.server "$PORT"
