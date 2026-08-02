# Học Python từ Cơ bản đến AI & Machine Learning

Repo tự học Python toàn diện — từ cú pháp cơ bản đến Machine Learning, Deep Learning và xây dựng API với FastAPI.

**GitHub:** [vibecoder202019/python-all](https://github.com/vibecoder202019/python-all)

## Triết lý học tập

Repo này thiết kế cho **người tự học** — không cần giáo viên, nhưng cần **kiên trì**:

1. **Hiểu trước, code sau** — đọc phần "Lý thuyết nền tảng" trước khi chạy ví dụ
2. **Chạy tay mọi ví dụ** — sửa thử 1 dòng, xem output thay đổi thế nào
3. **Làm bài tập trước khi xem đáp án** — não bộ ghi nhớ sâu hơn khi tự struggle
4. **Không vội sang module mới** — nắm ≥70% module hiện tại mới tiếp tục
5. **Dạy lại = học lại** — giải thích code cho người khác (hoặc viết note)

### Cấu trúc README mỗi module

| Phần | Mục đích |
|------|----------|
| **Mục tiêu** | Biết sẽ học được gì |
| **Lý thuyết nền tảng** | Hiểu "tại sao" — giải thích dễ hiểu, ví von |
| **Nội dung chính (1, 2, 3...)** | Kiến thức + code mẫu |
| **Giải thích chi tiết** | Giải thích từng lệnh, từng file code |
| **FAQ / Câu hỏi thường gặp** | Gỡ vướng nhanh |
| **Bài tập** | Tự thực hành |

### Lộ trình gợi ý theo mục tiêu

| Mục tiêu của bạn | Học module |
|------------------|------------|
| Viết Python cơ bản | 01 → 05 |
| Làm Data Analyst | 01 → 06 |
| Làm ML Engineer | 01 → 09 → 10 |
| Làm DevOps / K8s Engineer | 15 → 16 → 17 → 18 → **19** |
| **AI Agent free (Ollama) + AWX + n8n** | **15** → **23** → **24** |
| AWS Multi-Account & IAM | **13** → **22** → 19 |
| Thi chứng chỉ CKA / CKS | 15 → 16 → **18** |
| IaC + Secrets (Vault/Terraform) | 13 → **19** → **21** → 15 |
| Quản lý Terraform bằng UI (Terrakube) | **19** → **21** |
| Prompt AI cho DevOps / code | 01 → 12 → **20** (song song 15–19) |
| Làm Backend Engineer (Go) | 01 → 05 → **17** |
| Làm Security / DevSecOps | 01 → 05 → 12 → **16** → **25** → **26** |
| **Principal DevOps / Cloud Manager** | 12 → 13 → 15–19 → **22** → **26** → **27** |
| Làm game cho trẻ | 01 → 03 → 11 |
| Full-stack / Backend | 01 → 05 → 09 → 14 |
| DBA / Data Engineer | 01 → 06 → 14 |
| Full-stack AI | 01 → 10 → MLOps Labs |

## Yêu cầu

- Python 3.10 trở lên
- Trình soạn thảo code (VS Code, Cursor, PyCharm...)
- Terminal / Command line cơ bản

## Cài đặt môi trường

```bash
cd learn-python-ai
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate    # Windows

pip install -r requirements.txt
```

## Lộ trình học (27 module)

| # | Module | Nội dung | Thời gian ước tính |
|---|--------|----------|-------------------|
| 01 | [Python cơ bản](01-python-co-ban/README.md) | Biến, kiểu dữ liệu, vòng lập, hàm | 1-2 tuần |
| 02 | [Cấu trúc dữ liệu](02-cau-truc-du-lieu/README.md) | List, dict, set, tuple, stack, queue | 1 tuần |
| 03 | [Lập trình hướng đối tượng](03-oop/README.md) | Class, inheritance, polymorphism | 1-2 tuần |
| 04 | [File I/O & Module](04-xu-ly-file-va-module/README.md) | Đọc/ghi file, import, package | 3-5 ngày |
| 05 | [Thư viện Python](05-thu-vien-python/README.md) | requests, json, datetime, regex | 3-5 ngày |
| 06 | [Data Science](06-data-science/README.md) | NumPy, Pandas, Matplotlib | 2 tuần |
| 07 | [Machine Learning](07-machine-learning/README.md) | Scikit-learn, train/evaluate model | 2-3 tuần |
| 08 | [Deep Learning](08-deep-learning/README.md) | Neural network cơ bản, TensorFlow/Keras | 2-3 tuần |
| 09 | [FastAPI & REST API](09-fastapi/README.md) | Xây dựng API, deploy model | 1-2 tuần |
| 10 | [Dự án tổng hợp](10-du-an-tong-hop/README.md) | ML API end-to-end | 1-2 tuần |
| 11 | [Game cho Trẻ em](11-python-game-tre-em/README.md) | Pygame, game loop, dự án Catch the Stars | 2-3 tuần |
| 12 | [DevOps & DevSecOps](12-python-devops-devsecops/README.md) | Automation, security scan, CLI toolkit | 2-3 tuần |
| 13 | [Python & AWS Infra](13-python-aws-infra/README.md) | boto3, S3, EC2, SG, CloudWatch, IaC | 2-3 tuần |
| 14 | [PostgreSQL tự học](14-postgresql-tu-hoc/README.md) | SQL, PL/pgSQL, trigger, view, index, psycopg2 | 2-3 tuần |
| 15 | [AWX + MinIO + K8s](15-ansible-awx-minio-k8s/README.md) | Ansible AWX, MinIO, Kubernetes, Python API | 2-3 tuần |
| 16 | [K8s Security](16-k8s-security/README.md) | Anti-DDoS, SQLi, phishing, port scan trên K8s | 2-3 tuần |
| 17 | [Go + K8s + Helm](17-go-language-k8s/README.md) | Go từ cơ bản, REST API, Docker, Helm chart | 3-4 tuần |
| 18 | [CKA + CKS](18-cka-cks-kubernetes/README.md) | Tự học thi CKA/CKS, 14 lab hands-on | 8-12 tuần |
| 19 | [Vault + Terraform](19-vault-terraform/README.md) | IaC Terraform, HashiCorp Vault, 12 lab | 6-8 tuần |
| 20 | [Prompt AI DevOps](20-prompt-ai-devops/README.md) | Prompt engineering Python, K8s, Vault, monitoring | 4-6 tuần |
| 21 | [Terraform UI — Terrakube](21-terraform-ui-terrakube/README.md) | Quản lý Terraform qua UI open source, 10 lab | 2-3 tuần |
| 22 | [AWS Multi-Account](22-aws-multi-account/README.md) | Organizations, IAM roles, SCP — Console → Terraform | 3-4 tuần |
| 23 | [AI Agent + AWX (Ollama)](23-mcp-ai-agent-awx/README.md) | Ollama free AI, Agent Bridge, AWX automation | 1-2 tuần |
| 24 | [n8n + AI Automation](24-n8n-ai-automation/README.md) | n8n workflow, tích hợp Bridge + AWX capstone | 1-2 tuần |
| 25 | [Web Security / Phishing / Search](25-web-security-phishing-seo/README.md) | Phishing defense, OWASP harden, khôi phục ranking Google (chủ site) | 1-2 tuần |
| 26 | [DevSecOps CI/CD Security](26-devsecops-cicd-security/README.md) | Gitleaks, SAST, SCA, Trivy, SBOM, policy gate, GitHub Actions | 1-2 tuần |
| 27 | [Principal DevOps & Cloud Manager](27-principal-devops-cloud-manager/README.md) | Platform, SLO, FinOps, governance, ADR, portfolio Principal | 4-8 tuần |

**Capstone liên kết:** Module **15 → 23 → 24** — AWX + AI Agent + n8n orchestration. Xem [labs/capstone](24-n8n-ai-automation/labs/capstone/README.md).

**Bảo mật:** Module **16** (K8s WAF) + **25** (web/phishing) + **26** (CI/CD DevSecOps pipeline).

**Lộ trình lãnh đạo kỹ thuật cloud:** Module **22** (multi-account) + **26** (DevSecOps) + **27** (Principal / Cloud Manager portfolio).

**Tổng thời gian:** khoảng 6-8 tháng (học 1-2 giờ/ngày)

## Cách học hiệu quả

1. **Đọc lý thuyết** trong `README.md` của từng module
2. **Chạy manual từng bước** theo `readme_manual.md` — copy từng lệnh để hiểu script automation làm gì
3. **Chạy ví dụ** trong thư mục `examples/` — sửa và thử nghiệm
4. **Làm bài tập** trong `exercises/bai_tap.md`
5. **Đối chiếu đáp án** trong `exercises/solutions/` (chỉ xem sau khi đã cố gắng)
6. **Ghi chú** những phần chưa hiểu, quay lại ôn tập

## Cấu trúc mỗi module

```
module/
├── README.md          # Lý thuyết chi tiết (tiếng Việt)
├── readme_manual.md   # Hướng dẫn manual: Cài đặt + Kiểm tra (từ scripts/) + Chạy lab
├── examples/          # Code mẫu có comment giải thích
└── exercises/
    ├── bai_tap.md     # Bài tập thực hành
    └── solutions/     # Đáp án tham khảo
```

## Giải thích chi tiết lệnh Setup (Tự học)

### Tạo môi trường ảo

```bash
python3 -m venv .venv
source .venv/bin/activate
```

| Lệnh | Giải thích |
|------|------------|
| `python3 -m venv .venv` | Tạo thư mục `.venv` chứa Python + pip riêng — không ảnh hưởng system Python |
| `source .venv/bin/activate` | Kích hoạt venv — prompt hiện `(.venv)`, mọi `pip install` vào đây |
| `deactivate` | Thoát venv |

**Windows:** `.venv\Scripts\activate`

### Cài thư viện

```bash
pip install -r requirements.txt
```

- `-r` đọc danh sách package từ file
- Mỗi module có thể cần thêm package — chạy `bash scripts/setup.sh` hoặc `bash <module>/scripts/setup.sh`

### Clone repo

```bash
git clone git@github.com:vibecoder202019/python-all.git
cd python-all
```

---

## Cách đọc README mỗi module

Mỗi module README gồm:

1. **Lý thuyết** — khái niệm cần hiểu trước khi code
2. **Chạy ví dụ** — lệnh terminal để thực hành
3. **Giải thích chi tiết (Tự học)** — giải thích từng file code, từng lệnh bash
4. **Bài tập** — tự làm, đối chiếu `exercises/solutions/` sau

**Quy trình học 1 module:**
```
Đọc lý thuyết → readme_manual.md (chạy tay từng lệnh) → Chạy examples → Giải thích chi tiết → Bài tập → Project/script automation
```

---

## Setup & chạy nhanh

```bash
# Setup toàn bộ (chạy 1 lần)
bash scripts/setup.sh

# Module 1 — Python cơ bản
python 01-python-co-ban/examples/01_bien_va_kieu_du_lieu.py

# Module 9 — FastAPI
cd 09-fastapi && uvicorn app.main:app --reload

# Module 11 — Game (Pygame)
bash 11-python-game-tre-em/scripts/run_project.sh

# Module 12 — DevOps Toolkit
bash 12-python-devops-devsecops/scripts/run_project.sh

# Module 13 — AWS Infra (dry-run mặc định)
bash 13-python-aws-infra/scripts/setup.sh
bash 13-python-aws-infra/scripts/check_credentials.sh
bash 13-python-aws-infra/scripts/run_project.sh
bash 13-python-aws-infra/scripts/run_project.sh --apply   # tạo thật trên AWS
bash 13-python-aws-infra/scripts/destroy_infra.sh --apply  # xóa sau khi học

# Module 14 — PostgreSQL (Docker + psycopg2)
bash 14-postgresql-tu-hoc/scripts/setup.sh
bash 14-postgresql-tu-hoc/scripts/run_all_examples.sh
bash 14-postgresql-tu-hoc/scripts/run_project.sh
bash 14-postgresql-tu-hoc/scripts/psql_shell.sh   # psql tương tác

# Module 15 — AWX + MinIO + K8s (demo không cần cluster)
bash 15-ansible-awx-minio-k8s/scripts/setup.sh
bash 15-ansible-awx-minio-k8s/scripts/run_all_examples.sh --demo
bash 15-ansible-awx-minio-k8s/scripts/run_project.sh
# Triển khai K8s (cần Docker Desktop Kubernetes):
bash 15-ansible-awx-minio-k8s/scripts/02-deploy-minio.sh
bash 15-ansible-awx-minio-k8s/scripts/04-deploy-awx-instance.sh

# Module 16 — K8s Security (demo không cần cluster)
bash 16-k8s-security/scripts/setup.sh
bash 16-k8s-security/scripts/run_all_examples.sh
bash 16-k8s-security/scripts/run_project.sh
bash 16-k8s-security/scripts/02-deploy-lab.sh
bash 16-k8s-security/scripts/03-test-attacks.sh

# Module 17 — Go + K8s + Helm
bash 17-go-language-k8s/scripts/02-run-examples.sh
bash 17-go-language-k8s/scripts/03-run-project.sh --run
bash 17-go-language-k8s/scripts/04-build-docker.sh
bash 17-go-language-k8s/scripts/06-deploy-helm.sh

# Module 18 — CKA + CKS (cluster lab)
bash 18-cka-cks-kubernetes/scripts/01-setup-lab.sh
bash 18-cka-cks-kubernetes/scripts/02-run-lab.sh basic 01

# Module 19 — Vault + Terraform
bash 19-vault-terraform/scripts/01-install-tools.sh --check
bash 19-vault-terraform/scripts/02-setup-vault-dev.sh   # terminal 1
bash 19-vault-terraform/scripts/03-run-terraform.sh 01-hello --auto  # terminal 2

# Module 20 — Prompt AI DevOps
bash 20-prompt-ai-devops/scripts/01-setup.sh
bash 20-prompt-ai-devops/scripts/02-run-lab.sh 01

# Module 21 — Terrakube (Terraform UI open source)
bash 21-terraform-ui-terrakube/scripts/01-check-prerequisites.sh
bash 21-terraform-ui-terrakube/scripts/02-prepare-hosts.sh --print
bash 21-terraform-ui-terrakube/scripts/03-deploy-terrakube-compose.sh
# UI: https://terrakube.platform.local (admin@example.com / admin)

# Module 22 — AWS Multi-Account (Console → Terraform)
bash 22-aws-multi-account/scripts/01-check-prerequisites.sh
bash 22-aws-multi-account/scripts/02-run-lab.sh 01
bash 22-aws-multi-account/scripts/05-verify-org.sh

# Module 23 — MCP AI Agent + AWX Bridge
bash 23-mcp-ai-agent-awx/scripts/setup.sh
bash 23-mcp-ai-agent-awx/scripts/02-install-ollama.sh   # Ollama free AI
ollama serve   # terminal riêng
bash 23-mcp-ai-agent-awx/scripts/06-run-ollama-agent.sh  # chat agent
bash 23-mcp-ai-agent-awx/scripts/04-run-agent-bridge.sh

# Module 24 — n8n + capstone (15→23→24)
bash 24-n8n-ai-automation/scripts/02-deploy-n8n-compose.sh   # hoặc scripts/03-deploy-k8s.sh
bash 24-n8n-ai-automation/scripts/05-run-capstone-demo.sh
# Import workflows/04-capstone-ai-ops.json trên n8n UI

# Module 25 — Web security / phishing defense / search integrity (phòng thủ)
bash 25-web-security-phishing-seo/scripts/setup.sh
bash 25-web-security-phishing-seo/scripts/02-run-all-examples.sh
bash 25-web-security-phishing-seo/scripts/03-run-project.sh

# Module 26 — DevSecOps CI/CD security pipeline
bash 26-devsecops-cicd-security/scripts/setup.sh
bash 26-devsecops-cicd-security/scripts/02-run-local-pipeline.sh
# Workflow: .github/workflows/devsecops.yml

# Module 27 — Principal DevOps / Cloud Manager (portfolio)
bash 27-principal-devops-cloud-manager/scripts/setup.sh
bash 27-principal-devops-cloud-manager/scripts/02-init-portfolio.sh
bash 27-principal-devops-cloud-manager/scripts/03-run-governance-scorecard.sh
bash 27-principal-devops-cloud-manager/scripts/04-run-finops-summary.sh
# Làm labs 01–05 → bash scripts/05-validate-portfolio.sh
```

### Bash scripts mỗi module

| Script | Mục đích |
|--------|---------|
| `scripts/setup.sh` | Cài toàn bộ repo (1 lần) |
| `11-.../scripts/setup.sh` | Cài Pygame |
| `11-.../scripts/run_all_examples.sh` | Chạy ví dụ game tuần tự |
| `11-.../scripts/run_project.sh` | Dự án Catch the Stars (6 bước) |
| `12-.../scripts/setup.sh` | Cài DevOps deps + sample data |
| `12-.../scripts/run_all_examples.sh` | Chạy ví dụ DevOps tuần tự |
| `12-.../scripts/run_project.sh` | Dự án DevOps Toolkit (6 bước) |
| `12-.../scripts/demo_infra.sh` | Demo infra giả lập |
| `13-.../scripts/setup.sh` | Cài boto3 + config AWS |
| `13-.../scripts/check_credentials.sh` | Kiểm tra AWS credentials |
| `13-.../scripts/run_all_examples.sh` | Ví dụ AWS tuần tự |
| `13-.../scripts/run_project.sh` | Dự án AWS Infra (6 bước) |
| `13-.../scripts/destroy_infra.sh` | Xóa tài nguyên AWS đã tạo |
| `14-.../scripts/setup.sh` | Docker Postgres + psycopg2 |
| `14-.../scripts/run_all_examples.sh` | Ví dụ SQL/Python tuần tự |
| `14-.../scripts/run_project.sh` | Dự án Library DB (6 bước) |
| `14-.../scripts/psql_shell.sh` | Mở psql trong container |
| `14-.../scripts/teardown.sh` | Dừng container Postgres |
| `15-.../scripts/setup.sh` | Cài requests, boto3 cho AWX/MinIO |
| `15-.../scripts/run_all_examples.sh` | Ví dụ AWX API + MinIO (--demo) |
| `15-.../scripts/run_project.sh` | Dự án AWX Automation CLI (6 bước) |
| `15-.../scripts/02-deploy-minio.sh` | Deploy MinIO lên K8s |
| `15-.../scripts/04-deploy-awx-instance.sh` | Deploy AWX lên K8s |
| `15-.../scripts/06-setup-awx-cli.sh` | Cài AWX CLI (awxkit) |
| `15-.../scripts/07-terraform-awx-client.sh` | Terraform quản lý AWX resources (tùy chọn) |
| `16-.../scripts/setup.sh` | Cài fastapi, pyyaml cho security lab |
| `16-.../scripts/run_all_examples.sh` | Ví dụ SQLi, DDoS, phishing, port scan |
| `16-.../scripts/02-deploy-lab.sh` | Deploy security lab lên K8s |
| `16-.../scripts/03-test-attacks.sh` | Test tấn công mô phỏng |
| `17-.../scripts/02-run-examples.sh` | Chạy 7 ví dụ Go tuần tự |
| `17-.../scripts/03-run-project.sh` | Test + build Task API |
| `17-.../scripts/04-build-docker.sh` | Docker multi-stage build |
| `17-.../scripts/06-deploy-helm.sh` | Deploy Helm chart lên K8s |
| `18-.../scripts/01-setup-lab.sh` | Tạo cluster lab minikube/K8s |
| `18-.../scripts/02-run-lab.sh` | Mở hướng dẫn lab 01–14 |
| `18-.../scripts/03-verify-lab.sh` | Kiểm tra lab hoàn thành |
| `19-.../scripts/01-install-tools.sh` | Kiểm tra/cài Terraform + Vault |
| `19-.../scripts/02-setup-vault-dev.sh` | Vault dev mode + KV v2 |
| `19-.../scripts/03-run-terraform.sh` | Chạy example Terraform 01–project |
| `19-.../scripts/04-verify-lab.sh` | Verify lab Vault/Terraform |
| `20-.../scripts/01-setup.sh` | Setup thư mục notes + kiểm tra Python |
| `20-.../scripts/02-run-lab.sh` | Mở hướng dẫn lab 01–12 |
| `21-.../scripts/01-check-prerequisites.sh` | Kiểm tra Docker + mkcert |
| `21-.../scripts/03-deploy-terrakube-compose.sh` | Deploy Terrakube HTTPS local |
| `21-.../scripts/06-deploy-helm-minikube.sh` | Terrakube Helm trên minikube |
| `21-.../scripts/05-teardown-compose.sh` | Dọn stack Docker Compose |
| `22-.../scripts/01-check-prerequisites.sh` | AWS CLI + Terraform + credentials |
| `22-.../scripts/03-assume-role-demo.sh` | Demo STS assume-role cross-account |
| `22-.../scripts/04-terraform-plan.sh` | Plan Terraform management/dev-workload |

## Kiểm tra tiến độ

Sau mỗi module, tự trả lời:

- [ ] Tôi hiểu các khái niệm chính trong README?
- [ ] Tôi chạy được tất cả ví dụ?
- [ ] Tôi làm được ≥ 70% bài tập không cần xem đáp án?
- [ ] Tôi giải thích được code cho người khác?

Nếu chưa đạt → ôn lại module đó trước khi sang module tiếp theo.

## Liên kết với MLOps Labs

Sau khi hoàn thành repo này, bạn có thể chuyển sang [MLOps Labs](../labs/) trong cùng workspace để thực hành deploy model lên Kubernetes, CI/CD, v.v.

## Tài liệu tham khảo

- [Python Official Docs](https://docs.python.org/3/)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [Keras Documentation](https://keras.io/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [PL/pgSQL Guide](https://www.postgresql.org/docs/current/plpgsql.html)
