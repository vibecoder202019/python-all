# Hướng dẫn chạy Manual — Module 18: CKA / CKS

> Copy từng lệnh và chạy **tuần tự**. Lab thực hành theo markdown; script chỉ mở hướng dẫn và verify.

## Điều kiện

- `kubectl` ≥ 1.28
- minikube **hoặc** Docker Desktop Kubernetes (≥ 8 GB RAM)

---

## Phần A — Setup cluster (tương ứng `scripts/01-setup-lab.sh`)

**Cách 1 — minikube:**

```bash
minikube start --memory=8192 --cpus=4
minikube addons enable ingress
minikube addons enable metrics-server
kubectl get nodes
```

**Cách 2 — Docker Desktop K8s:** bật Kubernetes trong Settings, rồi:

```bash
kubectl get nodes
```

Alias kubectl (tùy chọn):

```bash
echo 'alias k=kubectl' >> ~/.bashrc
source ~/.bashrc
```

---

## Phần B — Làm lab (tương ứng `scripts/02-run-lab.sh`)

Ví dụ Lab 01 (Pods & Labels):

```bash
cd learn-python-ai/18-cka-cks-kubernetes
cat labs/basic/lab01-pods-labels.md
```

Làm theo từng bước trong file markdown bằng `kubectl` (copy lệnh trong lab).

Các lab khác:

```bash
cat labs/basic/lab02-deployments.md
cat labs/intermediate/lab07-rbac.md
cat labs/advanced/lab12-etcd-backup.md
```

---

## Phần C — Verify lab (tương ứng `scripts/03-verify-lab.sh`)

Sau khi hoàn thành lab 01:

```bash
cd learn-python-ai/18-cka-cks-kubernetes
bash scripts/03-verify-lab.sh 01
```

Verify lab khác (thay số):

```bash
bash scripts/03-verify-lab.sh 05
bash scripts/03-verify-lab.sh 10
```

---

## Phần D — Apply manifest mẫu (nếu lab yêu cầu)

```bash
cd learn-python-ai/18-cka-cks-kubernetes
kubectl apply -f manifests/
kubectl get all -A
```

---

## Bản đồ script ↔ manual

| Script | Phần |
|--------|------|
| `01-setup-lab.sh` | A |
| `02-run-lab.sh` | B (đọc + làm lab markdown) |
| `03-verify-lab.sh` | C |

## Gỡ / dọn dẹp

```bash
minikube delete
# hoặc xóa namespace lab:
kubectl delete namespace cka-lab --ignore-not-found
```
