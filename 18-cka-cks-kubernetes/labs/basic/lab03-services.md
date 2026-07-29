# Lab 03 — Service & DNS (Basic | CKA)

**Namespace:** `cka-lab` | **Thời gian:** 45 phút

## Bài tập 1 — ClusterIP Service

Expose deployment `web` (lab 02) — port 80 → target 80:

```bash
kubectl expose deployment web --port=80 --target-port=80 --name=web-svc -n cka-lab
kubectl get svc,endpoints -n cka-lab
```

## Bài tập 2 — Test DNS nội bộ

```bash
kubectl run curl --image=curlimages/curl:8.5.0 -it --rm -n cka-lab -- \
  curl -s http://web-svc.cka-lab.svc.cluster.local
```

## Bài tập 3 — NodePort

Tạo deployment `api` (httpd) + Service type NodePort port 80:

```bash
kubectl create deployment api --image=httpd:2.4-alpine -n cka-lab
kubectl expose deployment api --port=80 --type=NodePort --name=api-np -n cka-lab
kubectl get svc api-np -n cka-lab
```

## Bài tập 4 — Headless Service (nâng cao)

Service `web-headless`, `clusterIP: None` — dùng cho StatefulSet.

File: `manifests/cka/headless-service.yaml`

## Verify

```bash
bash scripts/03-verify-lab.sh 03
```
