#!/usr/bin/env bash
# Tạo repo GitHub và push code — chạy sau khi đã gh auth login
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REPO_NAME="${1:-learn-python-ai}"

cd "$ROOT"

if ! gh auth status &>/dev/null; then
  echo "❌ Chưa đăng nhập GitHub CLI."
  echo ""
  echo "Chạy lệnh sau và làm theo hướng dẫn:"
  echo "  gh auth login"
  echo ""
  echo "Sau đó chạy lại:"
  echo "  bash scripts/publish_github.sh"
  exit 1
fi

echo "=== Tạo repo GitHub: $REPO_NAME ==="

if git remote get-url origin &>/dev/null; then
  echo "Remote origin đã tồn tại. Push trực tiếp..."
  git push -u origin main
else
  gh repo create "$REPO_NAME" \
    --public \
    --source=. \
    --remote=origin \
    --description "Học Python từ cơ bản đến AI/ML, Game Pygame, DevOps/DevSecOps — 12 modules tự học" \
    --push
fi

echo ""
echo "✅ Repo đã publish!"
gh repo view --web 2>/dev/null || echo "URL: https://github.com/$(gh api user -q .login)/$REPO_NAME"
