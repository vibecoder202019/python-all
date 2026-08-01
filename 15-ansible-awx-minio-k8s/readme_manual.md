# Hướng dẫn chạy Manual — Module 15: AWX + MinIO + K8s

> Mọi lệnh trích từ `scripts/*.sh`. Chạy **Cài đặt → Kiểm tra → Deploy → Verify** theo thứ tự.

## Phần 0 — Chuẩn bị `/etc/hosts`

```bash
grep awx.local /etc/hosts || echo "127.0.0.1 minio.local minio-api.local awx.local" | sudo tee -a /etc/hosts
```

---

## Phần A — Cài đặt Python (`scripts/setup.sh`)

```bash
cd learn-python-ai
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install requests boto3 pyyaml
mkdir -p 15-ansible-awx-minio-k8s/data
```

**Kiểm tra:**

```bash
python -c "import requests, boto3, yaml; print('OK')"
test -f 15-ansible-awx-minio-k8s/data/awx.env.example && echo "config OK"
```

---

## Phần B — Kiểm tra K8s (`scripts/01-check-prerequisites.sh`)

```bash
kubectl version --client -o yaml | grep gitVersion | head -1
kubectl get nodes
kubectl get nodes -o jsonpath='{.items[0].status.conditions[?(@.type=="Ready")].status}'
kubectl get storageclass
kubectl get storageclass --no-headers | wc -l
helm version --short
command -v mc && mc --version || echo "mc optional"
kubectl get pods -n ingress-nginx
kubectl get pods -n ingress-nginx -l app.kubernetes.io/component=controller -o jsonpath='{.items[0].status.phase}'
grep awx.local /etc/hosts
```

**Kỳ vọng:** Node `Ready`, StorageClass ≥ 1, Ingress `Running`.

**Cài Ingress nếu thiếu:**

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.11.3/deploy/static/provider/cloud/deploy.yaml
```

---

## Phần C — Deploy MinIO (`scripts/02-deploy-minio.sh`)

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

**Kiểm tra:**

```bash
kubectl get pvc minio-data -n minio -o jsonpath='{.status.phase}'
kubectl get pods -l app=minio -n minio
```

---

## Phần D — AWX Operator (`scripts/03-deploy-awx-operator.sh`)

```bash
kubectl apply -f learn-python-ai/15-ansible-awx-minio-k8s/k8s/awx/namespace.yaml
helm repo add awx-operator https://ansible.github.io/awx-operator/
helm repo update
helm install awx-operator awx-operator/awx-operator -n awx --create-namespace
kubectl wait --for=condition=ready pod -l app.kubernetes.io/name=awx-operator -n awx --timeout=180s
kubectl get pods -n awx
```

---

## Phần E — AWX instance (`scripts/04-deploy-awx-instance.sh`)

```bash
kubectl apply -f learn-python-ai/15-ansible-awx-minio-k8s/k8s/awx/awx-instance.yaml
kubectl apply -f learn-python-ai/15-ansible-awx-minio-k8s/k8s/awx/ingress.yaml
kubectl wait --for=condition=ready pod -l app.kubernetes.io/name=awx-web -n awx --timeout=900s
kubectl get secret awx-admin-password -n awx -o jsonpath='{.data.password}' | base64 -d; echo
```

---

## Phần F — Verify all (`scripts/05-verify-all.sh`)

```bash
kubectl get namespace minio
kubectl get pods -l app=minio -n minio -o jsonpath='{.items[0].status.phase}'
kubectl get pvc minio-data -n minio -o jsonpath='{.status.phase}'
kubectl exec -n minio deploy/minio -- curl -sf http://localhost:9000/minio/health/live
kubectl get namespace awx
kubectl get pods -l app.kubernetes.io/name=awx-web -n awx -o jsonpath='{.items[0].status.phase}'
kubectl get secret awx-admin-password -n awx
```

---

## Phần G — AWX CLI (`scripts/06-setup-awx-cli.sh`)

```bash
cd learn-python-ai && source .venv/bin/activate
pip install --upgrade pip awxkit
awx --version
kubectl port-forward svc/awx-service 8052:80 -n awx
```

Terminal khác:

```bash
export AWX_HOST=http://localhost:8052
export AWX_TOKEN=PASTE_TOKEN
export AWX_VERIFY_SSL=false
awx ping
awx job_templates list -f json | head -c 500
```

---

## Phần H — Terraform (`scripts/07-terraform-awx-client.sh`)

```bash
cp learn-python-ai/15-ansible-awx-minio-k8s/terraform/awx-client/terraform.tfvars.example \
   learn-python-ai/15-ansible-awx-minio-k8s/terraform/awx-client/terraform.tfvars
cd learn-python-ai/15-ansible-awx-minio-k8s/terraform/awx-client
terraform init -input=false
terraform plan -input=false
terraform apply -input=false
```

---

## Phần I — Python demo (`scripts/run_all_examples.sh --demo`)

```bash
cd learn-python-ai && source .venv/bin/activate
python 15-ansible-awx-minio-k8s/examples/04_python_script_for_ansible.py --name Module15
python 15-ansible-awx-minio-k8s/examples/02_launch_job.py --demo
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
