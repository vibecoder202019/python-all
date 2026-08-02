#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
P="$MODULE_DIR/portfolio"
mkdir -p "$P"
[[ -f "$P/README.md" ]] || cat > "$P/README.md" << 'EOF'
# Portfolio — Module 27

Điền artifact theo labs 01–05. Không commit secret thật.
EOF
echo "✓ portfolio/ ready at $P"
echo "  Next: labs/01-adr-and-system-design.md"
