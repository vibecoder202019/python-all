# Lab 01 — Pod, Label, Namespace (Basic | CKA)

**Thời gian:** 30 phút | **Namespace lab:** `cka-lab`

## Mục tiêu

- Tạo namespace, pod, label/selector
- Dùng `kubectl run`, `--dry-run=client -o yaml`

## Bước 0 — Chuẩn bị

```bash
kubectl create namespace cka-lab
kubectl config set-context --current --namespace=cka-lab
```

## Bài tập 1 — Tạo Pod nginx

**Yêu cầu:** Pod tên `web-pod`, image `nginx:1.25`, label `app=web`, namespace `cka-lab`.

<details>
<summary>Gợi ý</summary>

```bash
kubectl run web-pod --image=nginx:1.25 --labels=app=web -n cka-lab
kubectl get pod web-pod -n cka-lab --show-labels
```
</details>

## Bài tập 2 — Tạo Pod từ YAML

**Yêu cầu:** Pod `api-pod`, image `httpd:2.4-alpine`, label `tier=backend`, thêm annotation `owner=lab01`.

Tạo bằng dry-run:

```bash
kubectl run api-pod --image=httpd:2.4-alpine --dry-run=client -o yaml > /tmp/api-pod.yaml
```

Sửa file: thêm `labels`, `annotations`, `namespace: cka-lab`, rồi apply.

## Bài tập 3 — Lọc pod bằng label

```bash
kubectl get pods -l app=web -n cka-lab
kubectl get pods -l tier=backend -n cka-lab
```

## Bài tập 4 — Multi-container pod

**Yêu cầu:** Pod `multi-pod` với 2 container: `nginx` + `redis:7-alpine`.

```bash
kubectl explain pod.spec.containers
# Tạo YAML 2 containers, apply
```

File mẫu: `manifests/cka/multi-container-pod.yaml`

## Verify

```bash
bash scripts/03-verify-lab.sh 01
```

## Checkpoint

- [ ] Giải thích difference Pod vs Deployment?
- [ ] `-l` selector hoạt động thế nào?
