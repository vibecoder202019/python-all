# Hướng dẫn chạy Manual — Module 18: CKA / CKS

> Lệnh trích từ `01-setup-lab.sh`, `02-run-lab.sh`, `03-verify-lab.sh`.

## Phần A — Cài đặt cluster (`scripts/01-setup-lab.sh`)

**minikube:**

```bash
minikube start --memory=8192 --cpus=4
minikube addons enable ingress
minikube addons enable metrics-server
minikube status
```

**Hoặc Docker Desktop K8s:**

```bash
kubectl get nodes
```

**Alias kubectl (tùy chọn):**

```bash
mkdir -p learn-python-ai/18-cka-cks-kubernetes/.lab
echo 'alias k=kubectl' >> learn-python-ai/18-cka-cks-kubernetes/.lab/bashrc-snippet
source learn-python-ai/18-cka-cks-kubernetes/.lab/bashrc-snippet
```

**Kiểm tra:**

```bash
kubectl get nodes
kubectl get pods -A | head -10
kubectl get ingressclass
```

---

## Phần B — Làm lab (`scripts/02-run-lab.sh`)

Ví dụ lab 01:

```bash
ls learn-python-ai/18-cka-cks-kubernetes/labs/basic/lab01-pods-labels.md
head -40 learn-python-ai/18-cka-cks-kubernetes/labs/basic/lab01-pods-labels.md
```

Làm theo hướng dẫn trong file markdown bằng `kubectl`.

---

## Phần C — Verify (`scripts/03-verify-lab.sh`)

```bash
bash learn-python-ai/18-cka-cks-kubernetes/scripts/03-verify-lab.sh 01
```

**Kiểm tra tay lab 01:**

```bash
kubectl get ns cka-lab
kubectl get pod -n cka-lab -l app=web
```

Lab 02:

```bash
bash learn-python-ai/18-cka-cks-kubernetes/scripts/03-verify-lab.sh 02
kubectl get deploy web -n cka-lab -o jsonpath='{.status.readyReplicas}'
```

---

## Bản đồ script ↔ manual

| Script | Phần |
|--------|------|
| `01-setup-lab.sh` | A |
| `02-run-lab.sh` | B (đọc + kubectl) |
| `03-verify-lab.sh` | C |

## Teardown

```bash
minikube delete
```
