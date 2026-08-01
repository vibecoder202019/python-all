# Hướng dẫn chạy Manual — Module 15: AWX + MinIO + K8s

> Copy từng lệnh và chạy **tuần tự**. Mỗi phần tương ứng script trong `scripts/`.

## Điều kiện

- Docker Desktop + Kubernetes bật (≥ 8 GB RAM)
- `kubectl`, `helm`
- NGINX Ingress Controller trong cluster
- Thêm vào `/etc/hosts`:
  ```
  127.0.0.1 minio.local minio-api.local awx.local
  ```

---

## Phần A — Setup Python (tương ứng `scripts/setup.sh`)

```bash
cd learn-python-ai
python3 -m venv .venv
source .venv/bin/activate
pip install requests boto3 pyyaml
pip install awxkit
```

---

## Phần B — Kiểm tra K8s (tương ứng `scripts/01-check-prerequisites.sh`)

```bash
kubectl get nodes
kubectl get storageclass
kubectl get pods -n ingress-nginx
```

---

## Phần C — Deploy MinIO (tương ứng `scripts/02-deploy-minio.sh`)

```bash
cd learn-python-ai/15-ansible-awx-minio-k8s
K8S=k8s/minio
kubectl apply -f $K8S/namespace.yaml
kubectl apply -f $K8S/secret.yaml
kubectl apply -f $K8S/pvc.yaml
kubectl wait --for=jsonpath='{.status.phase}'=Bound pvc/minio-data -n minio --timeout=60s
kubectl apply -f $K8S/deployment.yaml
kubectl wait --for=condition=ready pod -l app=minio -n minio --timeout=120s
kubectl apply -f $K8S/service.yaml
kubectl apply -f $K8S/ingress.yaml
kubectl get all -n minio
```

**Fallback (không Ingress):**

```bash
kubectl port-forward svc/minio 9001:9001 -n minio
kubectl port-forward svc/minio 9000:9000 -n minio
```

Console: `minioadmin` / `minioadmin123`

---

## Phần D — Cài AWX Operator (tương ứng `scripts/03-deploy-awx-operator.sh`)

```bash
cd learn-python-ai/15-ansible-awx-minio-k8s
kubectl apply -f k8s/awx/namespace.yaml
helm repo add awx-operator https://ansible.github.io/awx-operator/
helm repo update
helm install awx-operator awx-operator/awx-operator -n awx --create-namespace
kubectl wait --for=condition=ready pod -l app.kubernetes.io/name=awx-operator -n awx --timeout=180s
kubectl get pods -n awx
```

---

## Phần E — Deploy AWX instance (tương ứng `scripts/04-deploy-awx-instance.sh`)

```bash
cd learn-python-ai/15-ansible-awx-minio-k8s
kubectl apply -f k8s/awx/awx-instance.yaml
kubectl apply -f k8s/awx/ingress.yaml
kubectl wait --for=condition=ready pod -l app.kubernetes.io/name=awx-web -n awx --timeout=900s
kubectl get secret awx-admin-password -n awx -o jsonpath='{.data.password}' | base64 -d; echo
```

---

## Phần F — Verify (tương ứng `scripts/05-verify-all.sh`)

```bash
kubectl exec -n minio deploy/minio -- curl -sf http://localhost:9000/minio/health/live
kubectl get pods -n awx
kubectl get pods -n minio
```

---

## Phần G — AWX CLI (tương ứng `scripts/06-setup-awx-cli.sh`)

Terminal 1 — port-forward AWX:

```bash
kubectl port-forward svc/awx-service 8052:80 -n awx
```

Terminal 2 — cấu hình và test:

```bash
export AWX_URL=http://localhost:8052
export AWX_HOST=http://localhost:8052
export AWX_VERIFY_SSL=false
export AWX_TOKEN=PASTE_TOKEN_FROM_AWX_UI
pip install awxkit
awx ping
```

---

## Phần H — Terraform AWX client (tương ứng `scripts/07-terraform-awx-client.sh`, tùy chọn)

```bash
cd learn-python-ai/15-ansible-awx-minio-k8s/terraform/awx-client
cp terraform.tfvars.example terraform.tfvars
terraform init -input=false
terraform plan -input=false
terraform apply -input=false
```

---

## Phần I — Python examples (tương ứng `scripts/run_all_examples.sh --demo`)

```bash
cd learn-python-ai
source .venv/bin/activate
python 15-ansible-awx-minio-k8s/examples/02_launch_job.py --demo
python 15-ansible-awx-minio-k8s/examples/04_python_script_for_ansible.py --name Demo
python 15-ansible-awx-minio-k8s/examples/05_minio_boto3.py --demo
python 15-ansible-awx-minio-k8s/examples/06_full_pipeline.py --demo
```

---

## Bản đồ script ↔ manual

| Script | Phần |
|--------|------|
| `setup.sh` | A |
| `01-check-prerequisites.sh` | B |
| `02-deploy-minio.sh` | C |
| `03-deploy-awx-operator.sh` | D |
| `04-deploy-awx-instance.sh` | E |
| `05-verify-all.sh` | F |
| `06-setup-awx-cli.sh` | G |
| `07-terraform-awx-client.sh` | H |
| `run_all_examples.sh` | I |

## Gỡ / dọn dẹp

```bash
helm uninstall awx-operator -n awx
kubectl delete namespace awx
kubectl delete namespace minio
```
