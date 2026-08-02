# Module 16: Kubernetes Security — Anti-Phishing, DDoS, Port Scan, SQL Injection

Học bảo mật thực chiến trên **Kubernetes** bằng Python + manifest YAML — dành cho DevOps/Security Engineer.

## Mục tiêu

| Mối đe dọa | Giải pháp trong module |
|------------|--------------------------|
| **SQL Injection** | WAF Python + regex pattern + parameterized query |
| **DDoS** | Rate limiter + NGINX Ingress limit-rps + HPA |
| **Port Scan** | NetworkPolicy + Falco rules + log detector Python |
| **Phishing** | URL analyzer + security headers (HSTS, CSP, X-Frame-Options) |

---

## Lý thuyết nền tảng

### Defense in Depth (Bảo vệ nhiều lớp)

```
Internet
   │
   ▼
┌─────────────────────────────────────┐
│ Lớp 1: Ingress NGINX                │  Rate limit, block scanner UA, headers
├─────────────────────────────────────┤
│ Lớp 2: WAF Application (FastAPI)    │  SQLi detection, rate limit per IP
├─────────────────────────────────────┤
│ Lớp 3: NetworkPolicy              │  Chặn port scan nội bộ cluster
├─────────────────────────────────────┤
│ Lớp 4: Falco (Runtime)            │  Phát hiện shell, đọc file nhạy cảm
├─────────────────────────────────────┤
│ Lớp 5: Pod Security               │  Non-root, drop capabilities
└─────────────────────────────────────┘
   │
   ▼
  App Pod
```

### SQL Injection

Attacker chèn SQL vào input: `' OR 1=1--` → bypass login.

**Chống:**
- **Parameterized query** (luôn dùng `%s` / `?`, không nối chuỗi)
- **WAF** regex chặn pattern nguy hiểm ở edge

### DDoS

Flooding request làm server quá tải.

**Chống trên K8s:**
- `limit-rps` trên Ingress NGINX
- Rate limiter Python (token bucket)
- HPA scale thêm pod khi CPU cao

### Port Scan

Attacker quét nhiều port tìm dịch vụ mở.

**Chống:**
- **NetworkPolicy** — pod chỉ expose port cần thiết
- **Falco** — alert khi kết nối port lạ
- Python phân tích log: N port trong T giây → alert

### Phishing

Giả mạo trang login đánh cắp credential.

**Chống:**
- Security headers: `X-Frame-Options`, `CSP`, `HSTS`
- Python phân tích URL: IP thay domain, TLD lạ, keyword `login-verify`
- User training (ngoài phạm vi lab)

> Mở rộng sâu hơn (email phishing + **khôi phục ranking Google khi site bị hack**): [Module 25](../25-web-security-phishing-seo/README.md).

---

## Yêu cầu

- Module 01–05, 12 (Python + DevOps)
- Docker Desktop K8s (8 GB RAM)
- NGINX Ingress Controller

---

## Chạy nhanh

```bash
# 1. Setup Python
bash 16-k8s-security/scripts/setup.sh

# 2. Chạy examples (không cần K8s)
bash 16-k8s-security/scripts/run_all_examples.sh

# 3. Deploy lab lên K8s
bash 16-k8s-security/scripts/01-check-prerequisites.sh
bash 16-k8s-security/scripts/02-deploy-lab.sh

# 4. Test tấn công mô phỏng
echo "127.0.0.1 secure-api.local" | sudo tee -a /etc/hosts
bash 16-k8s-security/scripts/03-test-attacks.sh
```

---

## Lộ trình

| Bước | File | Nội dung |
|------|------|----------|
| 01 | `examples/01_detect_sql_injection.py` | Regex SQLi WAF |
| 02 | `examples/02_rate_limiter.py` | Token bucket anti-DDoS |
| 03 | `examples/03_phishing_url_checker.py` | Phân tích URL phishing |
| 04 | `examples/04_port_scan_detector.py` | Detect scan từ log |
| 05 | `examples/05_waf_middleware.py` | FastAPI WAF middleware |
| 06 | `examples/06_k8s_security_scanner.py` | Scan manifest K8s |
| 🎯 | `project/step06_final.py` | Security CLI |

---

## Kubernetes manifests (`k8s/`)

| File | Mục đích |
|------|----------|
| `namespace.yaml` | Namespace + Pod Security baseline |
| `deployment.yaml` | App FastAPI WAF, non-root |
| `configmap-app.yaml` | Mã Python WAF |
| `ingress-secure.yaml` | Rate limit + security headers + block scanner |
| `networkpolicy.yaml` | Chặn port scan nội bộ |
| `falco-rules.yaml` | Runtime detection rules |
| `hpa.yaml` | Auto-scale khi bị DDoS |

---

## Security CLI

```bash
python 16-k8s-security/project/step06_final.py sqli "admin"
python 16-k8s-security/project/step06_final.py sqli "' OR 1=1"
python 16-k8s-security/project/step06_final.py phishing "https://evil-login.xyz"
python 16-k8s-security/project/step06_final.py ratelimit --count 10 --limit 5
python 16-k8s-security/project/step06_final.py check-all
```

---

## Giải thích Ingress annotations

```yaml
# Chống DDoS — 10 request/giây, burst x3
nginx.ingress.kubernetes.io/limit-rps: "10"

# Chống phishing — không cho nhúng iframe
more_set_headers "X-Frame-Options: DENY";

# Chống scanner tự động
if ($http_user_agent ~* (sqlmap|nmap|nikto)) { return 403; }
```

---

## FAQ

**Hỏi:** WAF regex có đủ an toàn không?  
**Đáp:** Không — production cần ModSecurity OWASP CRS + parameterized query. Regex là lớp đầu tiên cho lab.

**Hỏi:** NetworkPolicy không hoạt động trên Docker Desktop?  
**Đáp:** Docker Desktop hỗ trợ NetworkPolicy hạn chế — test trên minikube `--cni=calico` hoặc EKS.

**Hỏi:** Falco bắt buộc?  
**Đáp:** Không — file `falco-rules.yaml` là tham khảo. Cài Falco khi học runtime security nâng cao.

---

## Liên kết

- [Module 12 — DevOps](../12-python-devops-devsecops/README.md)
- [Module 15 — AWX + MinIO + K8s](../15-ansible-awx-minio-k8s/README.md)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Kubernetes Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
