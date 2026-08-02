#!/usr/bin/env bash
# Local DevSecOps pipeline — mirror GitHub Actions stages
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"
APP="$MODULE_DIR/sample-app"
REPORTS="$MODULE_DIR/reports"
IMAGE="devsecops-lab-app:local"
FAIL=0

mkdir -p "$REPORTS"
cd "$ROOT_DIR"
# shellcheck disable=SC1091
[ -f .venv/bin/activate ] && source .venv/bin/activate

echo "╔══════════════════════════════════════════╗"
echo "║  Module 26 — Local DevSecOps Pipeline    ║"
echo "╚══════════════════════════════════════════╝"

# ── 1. Secrets ──
echo ""
echo "==> [1/8] Secret scan (Gitleaks)"
if command -v gitleaks >/dev/null 2>&1; then
  if gitleaks detect --source "$MODULE_DIR" --report-path "$REPORTS/gitleaks.json" --report-format json -v; then
    echo "    OK — no secrets"
  else
    echo "    FAIL — secrets detected (xem $REPORTS/gitleaks.json)"
    FAIL=1
  fi
else
  echo "    SKIP — cài: brew install gitleaks"
  # Fallback: detect-private-key style
  if grep -RInE '(BEGIN (RSA |OPENSSH )?PRIVATE KEY|AKIA[0-9A-Z]{16})' "$APP" 2>/dev/null; then
    echo "    FAIL — pattern khóa riêng / AWS key trong sample-app"
    FAIL=1
  else
    echo "    OK (heuristic fallback)"
  fi
fi

# ── 2. SCA ──
echo ""
echo "==> [2/8] SCA (pip-audit)"
if command -v pip-audit >/dev/null 2>&1; then
  # JSON report (không fail pipeline)
  pip-audit -r "$APP/requirements.txt" -f json -o "$REPORTS/pip-audit.json" || true
  # Human report — lab: warn only (đổi exit 1 khi fail-closed)
  if pip-audit -r "$APP/requirements.txt"; then
    echo "    OK — no known vulnerable deps"
  else
    echo "    WARN — vulnerable deps (xem reports/pip-audit.json); lab không fail CRITICAL gate"
  fi
else
  echo "    SKIP — pip install pip-audit"
fi

# ── 3. SAST Bandit ──
echo ""
echo "==> [3/8] SAST (Bandit)"
if command -v bandit >/dev/null 2>&1 || python -c "import bandit" 2>/dev/null; then
  bandit -r "$APP" -f json -o "$REPORTS/bandit.json" 2>/dev/null || true
  if bandit -r "$APP" -ll; then
    echo "    OK — no HIGH/CRITICAL"
  else
    echo "    WARN/FAIL — Bandit HIGH+ (lab app có MD5 cố ý — kỳ vọng thấy finding)"
    echo "    Lab note: findings là bình thường; production phải fix hoặc # nosec + ticket"
    # Lab: không fail cả pipeline vì intentional MD5 — chỉ warn
  fi
else
  echo "    SKIP — pip install bandit"
fi

# ── 4. Unit tests ──
echo ""
echo "==> [4/8] Unit tests"
if (cd "$APP" && pip install -q -r requirements.txt pytest httpx >/dev/null && PYTHONPATH=. pytest -q); then
  echo "    OK"
else
  echo "    FAIL — tests"
  FAIL=1
fi

# ── 5–7. Docker + Trivy ──
echo ""
echo "==> [5/8] Build image"
if command -v docker >/dev/null 2>&1 && docker info >/dev/null 2>&1; then
  docker build -t "$IMAGE" "$APP"
  echo "    OK — $IMAGE"

  echo ""
  echo "==> [6/8] Container scan (Trivy CRITICAL)"
  if command -v trivy >/dev/null 2>&1; then
    trivy image --severity CRITICAL --exit-code 1 --ignore-unfixed "$IMAGE" \
      --format json --output "$REPORTS/trivy.json" || {
        echo "    FAIL — CRITICAL CVEs in image"
        FAIL=1
      }
    trivy image --severity HIGH,CRITICAL --ignore-unfixed "$IMAGE" || true
  else
    echo "    SKIP — brew install trivy"
  fi

  echo ""
  echo "==> [7/8] SBOM (Syft)"
  if command -v syft >/dev/null 2>&1; then
    syft "$IMAGE" -o cyclonedx-json > "$REPORTS/sbom.cyclonedx.json"
    echo "    OK — $REPORTS/sbom.cyclonedx.json"
  else
    echo "    SKIP — brew install syft"
  fi
else
  echo "    SKIP Docker/Trivy/SBOM — Docker daemon không chạy hoặc chưa cài"
fi

# ── 8. Policy summary ──
echo ""
echo "==> [8/8] Policy gate summary"
echo "    Policy: $MODULE_DIR/policy/severity-gate.yaml"
echo "    Reports: $REPORTS/"
ls -la "$REPORTS" 2>/dev/null || true

echo ""
if [[ "$FAIL" -eq 0 ]]; then
  echo "✓ Local pipeline finished (gates CRITICAL secrets/deps/tests)"
  echo "  Xem Bandit findings trong reports/bandit.json để học SAST."
  exit 0
else
  echo "✗ Pipeline FAILED — xem stages FAIL ở trên"
  exit 1
fi
