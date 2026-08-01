# Hướng dẫn chạy Manual — Module 16: K8s Security

> Copy từng lệnh và chạy **tuần tự**. Mỗi phần tương ứng script trong `scripts/`.

## Điều kiện

- Docker Desktop + Kubernetes
- NGINX Ingress
- `/etc/hosts`: `127.0.0.1 secure-api.local`

---

## Phần A — Setup Python (tương ứng `scripts/setup.sh`)

```bash
cd learn-python-ai
source .venv/bin/activate
pip install fastapi uvicorn pyyaml httpx
```

---

## Phần B — Ví dụ Python (tương ứng `scripts/run_all_examples.sh`)

```bash
cd learn-python-ai
source .venv/bin/activate
python 16-k8s-security/examples/01_detect_sql_injection.py
python 16-k8s-security/examples/02_rate_limiter.py
python 16-k8s-security/examples/03_phishing_url_checker.py
python 16-k8s-security/examples/04_port_scan_detector.py
python 16-k8s-security/examples/06_k8s_security_scanner.py
```

WAF middleware (terminal riêng):

```bash
cd learn-python-ai
source .venv/bin/activate
uvicorn 16-k8s-security.examples.05_waf_middleware:app --port 8080
```

---

## Phần C — Dự án CLI (tương ứng `scripts/run_project.sh`)

```bash
cd learn-python-ai
source .venv/bin/activate
python 16-k8s-security/project/step01_sql_guard.py --demo
python 16-k8s-security/project/step02_rate_limit.py --demo
python 16-k8s-security/project/step03_phishing_check.py --demo
python 16-k8s-security/project/step04_port_scan_detect.py --demo
python 16-k8s-security/project/step05_k8s_manifests.py --demo
python 16-k8s-security/project/step06_final.py --demo
```

---

## Phần D — Kiểm tra K8s (tương ứng `scripts/01-check-prerequisites.sh`)

```bash
kubectl get nodes
kubectl get pods -n ingress-nginx
```

---

## Phần E — Deploy lab (tương ứng `scripts/02-deploy-lab.sh`)

```bash
cd learn-python-ai/16-k8s-security
K8S=k8s
kubectl apply -f $K8S/namespace.yaml
kubectl apply -f $K8S/configmap-app.yaml
kubectl apply -f $K8S/deployment.yaml
kubectl apply -f $K8S/service.yaml
kubectl apply -f $K8S/networkpolicy.yaml
kubectl apply -f $K8S/ingress-secure.yaml
kubectl apply -f $K8S/hpa.yaml
kubectl wait --for=condition=ready pod -l app=secure-api -n security-lab --timeout=180s
```

Thêm hosts (macOS):

```bash
echo "127.0.0.1 secure-api.local" | sudo tee -a /etc/hosts
```

---

## Phần F — Test tấn công (tương ứng `scripts/03-test-attacks.sh`)

```bash
BASE=http://secure-api.local
curl -sf "$BASE/health"
curl -s -o /dev/null -w "%{http_code}\n" "$BASE/search?q=%27%20OR%201%3D1--"
curl -s -o /dev/null -w "%{http_code}\n" "$BASE/search?q=hello"
for i in $(seq 1 15); do curl -s -o /dev/null -w "%{http_code} " "$BASE/search?q=test$i"; done; echo
curl -sI "$BASE/health" | grep -i x-frame-options
curl -s -o /dev/null -w "%{http_code}\n" -A "sqlmap/1.0" "$BASE/search?q=test"
```

**Fallback port-forward:**

```bash
kubectl port-forward svc/secure-api 8080:80 -n security-lab
export BASE=http://localhost:8080
curl -sf "$BASE/health"
```

---

## Bản đồ script ↔ manual

| Script | Phần |
|--------|------|
| `setup.sh` | A |
| `run_all_examples.sh` | B |
| `run_project.sh` | C |
| `01-check-prerequisites.sh` | D |
| `02-deploy-lab.sh` | E |
| `03-test-attacks.sh` | F |

## Gỡ / dọn dẹp

```bash
kubectl delete namespace security-lab
```
