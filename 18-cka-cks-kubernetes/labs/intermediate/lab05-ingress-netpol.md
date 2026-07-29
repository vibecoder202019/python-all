# Lab 05 — Ingress & NetworkPolicy (Intermediate | CKA)

**Namespace:** `cka-lab` | **Thời gian:** 45 phút

## Bài tập 1 — Ingress

```bash
# Cần NGINX Ingress Controller
kubectl apply -f manifests/cka/ingress-web.yaml
# Thêm /etc/hosts: 127.0.0.1 web.cka.local
curl http://web.cka.local
```

## Bài tập 2 — NetworkPolicy allow

Chỉ cho pod `role=backend` nhận traffic từ pod `app=frontend`, port 80.

File: `manifests/cka/netpol-allow-frontend.yaml`

## Bài tập 3 — Test policy

```bash
kubectl run front --image=busybox:1.36 --labels=app=frontend -n cka-lab -- sleep 3600
kubectl run back --image=nginx:1.25 --labels=role=backend -n cka-lab
# Test wget từ front → back
```

## Verify

```bash
bash scripts/03-verify-lab.sh 05
```
