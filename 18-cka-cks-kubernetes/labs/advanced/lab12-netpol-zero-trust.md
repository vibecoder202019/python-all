# Lab 12 — NetworkPolicy Zero Trust (Advanced | CKS)

**Namespace:** `cks-lab` | **Thời gian:** 45 phút

## Kiến trúc lab

```
[frontend] ──allowed──► [backend] ──allowed──► [database]
     │                      │
     X                      X
  [attacker]            [attacker]
```

## Bài tập 1 — Deploy 3 tier

```bash
kubectl apply -f manifests/cks/three-tier-app.yaml -n cks-lab
```

## Bài tập 2 — Default deny all

```bash
kubectl apply -f manifests/cks/netpol-default-deny.yaml -n cks-lab
# Mọi traffic bị chặn
```

## Bài tập 3 — Allow rules từng bước

1. frontend → backend port 8080
2. backend → database port 5432
3. deny phần còn lại (implicit)

Files: `manifests/cks/netpol-allow-*.yaml`

## Bài tập 4 — Test

```bash
kubectl exec frontend -n cks-lab -- wget -qO- http://backend:8080
kubectl exec attacker -n cks-lab -- wget -qO- http://backend:8080 --timeout=3
# attacker phải fail
```

## Verify

```bash
bash scripts/03-verify-lab.sh 12
```
