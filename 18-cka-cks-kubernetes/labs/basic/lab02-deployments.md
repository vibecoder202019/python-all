# Lab 02 — Deployment & Scaling (Basic | CKA)

**Thời gian:** 30 phút | **Namespace:** `cka-lab`

## Mục tiêu

- Deployment, scale, rolling update, rollback

## Bài tập 1 — Tạo Deployment

**Yêu cầu:** Deployment `web`, image `nginx:1.25`, **3 replicas**, label `app=web`.

```bash
kubectl create deployment web --image=nginx:1.25 --replicas=3 -n cka-lab
kubectl get deploy,rs,pods -n cka-lab
```

## Bài tập 2 — Scale

Scale lên **5 replicas**, sau đó xuống **2**:

```bash
kubectl scale deployment web --replicas=5 -n cka-lab
kubectl scale deployment web --replicas=2 -n cka-lab
```

## Bài tập 3 — Rolling update

```bash
kubectl set image deployment/web nginx=nginx:1.26 -n cka-lab
kubectl rollout status deployment/web -n cka-lab
kubectl rollout history deployment/web -n cka-lab
```

## Bài tập 4 — Rollback

```bash
kubectl rollout undo deployment/web -n cka-lab
kubectl rollout history deployment/web -n cka-lab
```

## Bài tập 5 — Resource limits

Thêm vào deployment:
```yaml
resources:
  requests: { cpu: 50m, memory: 64Mi }
  limits:   { cpu: 100m, memory: 128Mi }
```

```bash
kubectl edit deployment web -n cka-lab
# hoặc patch / apply YAML mới
```

## Verify

```bash
bash scripts/03-verify-lab.sh 02
```
