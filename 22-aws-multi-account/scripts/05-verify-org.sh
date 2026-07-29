#!/usr/bin/env bash
set -euo pipefail
aws organizations describe-organization 2>/dev/null && echo "Organizations: enabled" || echo "Organizations: not enabled"
aws organizations list-accounts --output table 2>/dev/null || true
