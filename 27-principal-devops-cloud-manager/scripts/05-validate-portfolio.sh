#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
P="$MODULE_DIR/portfolio"
echo "=== Validate portfolio Module 27 ==="
missing=0
for f in \
  README.md \
  ADR-001-compute-platform.md \
  ADR-002-secret-strategy.md \
  platform-catalog.md \
  slo-payments-api.md \
  runbook-payments-api.md \
  postmortem-2026-lab.md \
  governance-scorecard.json \
  finops-30-day-plan.md \
  one-pager.md \
  architecture-ascii.md \
  pitch.md
 do
  if [[ -f "$P/$f" ]]; then echo "  ✓ $f"; else echo "  ✗ missing $f"; missing=1; fi
done
if [[ "$missing" -eq 0 ]]; then
  echo "✓ Portfolio files present — review quality manually before interviews"
  exit 0
else
  echo "→ Hoàn thành labs 01–05 rồi chạy lại"
  exit 1
fi
