#!/usr/bin/env bash
# Verify lab completion
set -euo pipefail
NUM="${1:?Usage: $0 LAB_NUM (01-14)}"
NS="${NS:-cka-lab}"

pass() { echo "  ✅ $1"; }
fail() { echo "  ❌ $1"; }

echo "=== Verify Lab $NUM ==="

case "$NUM" in
  01)
    kubectl get ns cka-lab &>/dev/null && pass "namespace cka-lab" || fail "namespace cka-lab"
    kubectl get pod -n cka-lab -l app=web &>/dev/null && pass "pod web" || fail "pod web (optional)"
    ;;
  02)
    replicas=$(kubectl get deploy web -n cka-lab -o jsonpath='{.status.readyReplicas}' 2>/dev/null || echo 0)
    [ "${replicas:-0}" -ge 1 ] && pass "deployment web ready ($replicas)" || fail "deployment web"
    ;;
  03)
    kubectl get svc -n cka-lab &>/dev/null && pass "service exists" || fail "service"
    ;;
  04)
    kubectl get configmap -n cka-lab &>/dev/null && pass "configmap" || fail "configmap"
    kubectl get secret -n cka-lab &>/dev/null && pass "secret" || fail "secret"
    ;;
  09)
    kubectl get ns cka-trouble &>/dev/null && pass "namespace cka-trouble" || fail "apply troubleshoot yaml first"
    not_running=$(kubectl get pods -n cka-trouble --field-selector=status.phase!=Running 2>/dev/null | tail -n +2 | wc -l | tr -d ' ')
    [ "$not_running" = "0" ] && pass "all pods Running" || fail "$not_running pods not Running — keep troubleshooting"
    ;;
  11|12)
    kubectl get ns cks-lab &>/dev/null && pass "namespace cks-lab" || fail "namespace cks-lab"
    ;;
  *)
    echo "  ℹ️  Verify thủ công — xem lab doc và kubectl get all -n $NS"
    ;;
esac
echo "Done."
