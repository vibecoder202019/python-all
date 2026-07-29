#!/usr/bin/env bash
# Module 16 — Test tấn công mô phỏng (SQLi, DDoS, scan)
set -euo pipefail

BASE="${BASE_URL:-http://secure-api.local}"
echo "=== Test Security Defenses ==="
echo "Target: $BASE"
echo ""

pass() { echo "  ✅ $1"; }
fail() { echo "  ❌ $1"; }

# 1. Health check
echo "[1] Health check"
if curl -sf "$BASE/health" > /dev/null 2>&1; then
  pass "API hoạt động"
else
  echo "  ⚠️  API chưa sẵn sàng — thử port-forward:"
  echo "     kubectl port-forward svc/secure-api 8080:80 -n security-lab"
  BASE="http://localhost:8080"
fi

# 2. SQL Injection — phải bị chặn 403
echo ""
echo "[2] SQL Injection"
CODE=$(curl -s -o /dev/null -w "%{http_code}" "$BASE/search?q=%27%20OR%201%3D1--" 2>/dev/null || echo "000")
[ "$CODE" = "403" ] && pass "SQLi bị chặn (403)" || fail "SQLi không bị chặn (code=$CODE)"

# 3. Request bình thường — phải 200
echo ""
echo "[3] Request hợp lệ"
CODE=$(curl -s -o /dev/null -w "%{http_code}" "$BASE/search?q=hello" 2>/dev/null || echo "000")
[ "$CODE" = "200" ] && pass "Request hợp lệ OK (200)" || fail "Request hợp lệ fail (code=$CODE)"

# 4. Rate limit DDoS — gửi nhiều request
echo ""
echo "[4] Rate Limit (DDoS simulation — 15 requests nhanh)"
BLOCKED=0
for i in $(seq 1 15); do
  CODE=$(curl -s -o /dev/null -w "%{http_code}" "$BASE/search?q=test$i" 2>/dev/null || echo "000")
  [ "$CODE" = "429" ] && BLOCKED=1
done
[ "$BLOCKED" = "1" ] && pass "Rate limit kích hoạt (429)" || echo "  ⚠️  Chưa thấy 429 — có thể cần nhiều request hơn"

# 5. Security headers (anti-phishing)
echo ""
echo "[5] Security Headers"
HEADERS=$(curl -sI "$BASE/health" 2>/dev/null || true)
echo "$HEADERS" | grep -qi "x-frame-options" && pass "X-Frame-Options present" || echo "  ⚠️  Thiếu X-Frame-Options (cần Ingress)"
echo "$HEADERS" | grep -qi "x-content-type" && pass "X-Content-Type-Options present" || echo "  ⚠️  Thiếu header"

# 6. Scanner user-agent block
echo ""
echo "[6] Block scanner User-Agent"
CODE=$(curl -s -o /dev/null -w "%{http_code}" -A "sqlmap/1.0" "$BASE/search?q=test" 2>/dev/null || echo "000")
[ "$CODE" = "403" ] && pass "sqlmap UA bị chặn (403)" || echo "  ⚠️  sqlmap UA code=$CODE"

echo ""
echo "=== Test hoàn tất ==="
