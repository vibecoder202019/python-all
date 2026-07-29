#!/usr/bin/env bash
# Gợi ý đáp án Mock Exam Lab 14 — chỉ xem sau khi làm xong
set -euo pipefail
NS=exam-mock
kubectl create namespace $NS --dry-run=client -o yaml | kubectl apply -f -
kubectl config set-context --current --namespace=$NS

kubectl create deployment web --image=nginx:1.25 --replicas=3 -n $NS
kubectl label deployment web app=web -n $NS --overwrite
kubectl expose deployment web --port=80 -n $NS --name=web-svc
# ... tiếp tục các task theo lab14-mock-exam.md
echo "Xem đầy đủ trong labs/advanced/lab14-mock-exam.md"

# --- JSONPath (bài tập 11–15) ---
# 11. kubectl get pod web-pod -n cka-lab -o jsonpath='{.status.podIP}'
# 12. kubectl get pods -n cka-lab -o jsonpath='{range .items[*]}{.metadata.name}{" "}{.status.podIP}{"\n"}{end}'
# 13. kubectl get pods -n cka-lab -o custom-columns=NAME:.metadata.name,PHASE:.status.phase,NODE:.spec.nodeName
# 14. kubectl get secret db-secret -n cka-lab -o jsonpath='{.data.password}' | base64 -d && echo
# 15. kubectl get pod POD -n NS -o jsonpath='{.spec.containers[0].securityContext.readOnlyRootFilesystem}'
