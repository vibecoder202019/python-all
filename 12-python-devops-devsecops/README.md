# Module 12: Python cho DevOps & DevSecOps

Học Python thực chiến cho **DevOps Engineer** và **DevSecOps Engineer** — automation, CI/CD scripts, security scanning, infrastructure monitoring.

## Mục tiêu

- Viết script automation với `subprocess`, `argparse`, `pathlib`
- Parse YAML/JSON config, log analysis
- Health check services, deploy scripts
- DevSecOps: scan secrets, file permissions, dependency audit
- Hoàn thành CLI tool **DevOps Toolkit** qua 6 bước tuần tự

---

## Lý thuyết nền tảng — DevOps là gì?

**DevOps** = **Dev**elopment + **Op**erations — phá bỏ silo giữa team code và team vận hành.

```
Trước DevOps:
  Dev viết code → ném qua tường → Ops deploy + fix lỗi

Sau DevOps:
  Dev tự automate: test, build, deploy, monitor
  Ops viết code: infrastructure as code, CI/CD
```

### DevOps Engineer làm gì?

- Viết script **automation** (Python, Bash)
- Xây **CI/CD pipeline** (GitHub Actions, Jenkins)
- Quản lý **infrastructure** (Docker, Kubernetes, AWS)
- **Monitor** hệ thống (logs, metrics, alerts)

### DevSecOps — Security trong DevOps

**Shift-left security** = kiểm tra bảo mật **sớm** trong quy trình dev, không đợi production:

```
Code → SAST scan → Build → Container scan → Deploy → Runtime monitor
         ↑ secrets          ↑ vulnerabilities
         detection
```

### Python trong DevOps

| Task | Công cụ Python |
|------|----------------|
| Gọi shell command | `subprocess` |
| Parse config | `yaml`, `json` |
| HTTP health check | `httpx`, `requests` |
| Log analysis | `re`, `collections.Counter` |
| CLI tool | `argparse` |
| AWS automation | `boto3` |

### Infrastructure as Code (IaC)

Thay vì click AWS Console → **viết code** mô tả infrastructure:
- **Reproducible** — tạo lại môi trường giống hệt
- **Version controlled** — git track mọi thay đổi
- **Reviewable** — team review trước khi apply

---

## Chạy nhanh (1 lệnh)

```bash
# Cài môi trường (chạy 1 lần)
bash scripts/setup.sh

# Chạy TẤT CẢ ví dụ tuần tự
bash scripts/run_all_examples.sh

# Chạy dự án DevOps Toolkit (6 bước → CLI hoàn chỉnh)
bash scripts/run_project.sh
```

---

## Lộ trình

| Bước | File | Nội dung | Level |
|------|------|----------|-------|
| 01 | `examples/01_subprocess_bash.py` | Chạy lệnh shell từ Python | Cơ bản |
| 02 | `examples/02_pathlib_config.py` | File system, YAML/JSON config | Cơ bản |
| 03 | `examples/03_log_analyzer.py` | Phân tích log, metrics | Trung bình |
| 04 | `examples/04_health_check.py` | Health check HTTP/services | Trung bình |
| 05 | `examples/05_docker_script.py` | Docker automation | Nâng cao |
| 06 | `examples/06_security_scan.py` | DevSecOps: secrets, permissions | DevSecOps |
| 🎯 | `project/` | **DevOps Toolkit CLI** (6 step) | Dự án |

---

## DevOps vs DevSecOps

```
DevOps                          DevSecOps
──────                          ─────────
Deploy automation        +      Security scanning
CI/CD scripts            +      Secrets detection
Monitoring/alerting      +      Compliance checks
Infrastructure as Code   +      SAST/DAST integration
Log analysis             +      Audit trails
```

---

## Dự án tuần tự: DevOps Toolkit CLI

CLI tool tích hợp các chức năng DevOps/DevSecOps:

```
project/
├── step01_cli_skeleton.py    # argparse CLI cơ bản
├── step02_file_ops.py        # + quét file, disk usage
├── step03_log_parser.py      # + phân tích log
├── step04_health_monitor.py  # + health check endpoints
├── step05_security_audit.py  # + security scan
└── step06_final.py           # CLI hoàn chỉnh (devops-toolkit)
```

```bash
# Sau khi hoàn thành step06:
python project/step06_final.py --help
python project/step06_final.py disk-usage --path .
python project/step06_final.py parse-log --file sample.log
python project/step06_final.py health-check --url http://localhost:8000/health
python project/step06_final.py security-scan --path .
```

---

## Bash scripts trong module

| Script | Mục đích |
|--------|---------|
| `scripts/setup.sh` | Cài venv + dependencies (chạy 1 lần) |
| `scripts/run_all_examples.sh` | Chạy examples 01→06 tuần tự |
| `scripts/run_project.sh` | Chạy project steps 01→06 tuần tự |
| `scripts/demo_infra.sh` | Demo môi trường giả lập infra |

---

---

## Giải thích chi tiết (Tự học)

### File `examples/01_subprocess_bash.py`

```python
subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
```

| Tham số | Ý nghĩa |
|---------|---------|
| `shell=True` | Chạy qua shell — hỗ trợ pipe `\|` , redirect |
| `capture_output=True` | Bắt stdout/stderr vào biến |
| `text=True` | Output dạng string (không phải bytes) |
| `check=True` | Ném exception nếu returncode ≠ 0 |

```python
code, out, err = run_command_safe("git status")
```
- Không crash script — tự xử lý lỗi qua returncode

**DevOps use case:** Chạy deploy script, git, docker, kubectl từ Python orchestrator.

---

### File `examples/03_log_analyzer.py`

```python
LOG_PATTERN = re.compile(r"\[(?P<timestamp>...)\] (?P<level>\w+): (?P<message>.+)")
match = LOG_PATTERN.match(line.strip())
```

- `(?P<name>...)` — **named group** → `match.group("level")`
- Parse log structured → đếm ERROR, tính error rate

---

### File `examples/04_health_check.py`

```python
@dataclass
class HealthResult:
    name: str
    status: str
    response_time_ms: float
```

```python
response = httpx.get(url, timeout=5)
healthy = response.status_code < 400
```
- Pattern **health check** dùng trong K8s liveness/readiness probe

---

### File `examples/06_security_scan.py`

```python
SECRET_PATTERNS = [
    (r"AKIA[0-9A-Z]{16}", "AWS Access Key"),
    (r"ghp_[a-zA-Z0-9]{36}", "GitHub Token"),
]
```
- Quét file tìm secret hardcoded — **DevSecOps shift-left**
- Scan permission `0o002` (world-writable) — rủi ro bảo mật

---

### Dự án DevOps Toolkit — từng step

| Step | CLI command | Code học |
|------|-------------|----------|
| `step01` | `--help`, `--version` | `argparse` cơ bản |
| `step02` | `disk-usage --path .` | `pathlib.rglob`, tính size |
| `step03` | `parse-log --file sample.log` | regex + Counter |
| `step04` | `health-check --url URL` | httpx + dataclass |
| `step05` | `security-scan --path .` | secret patterns |
| `step06` | `report`, subcommands | argparse subparsers |

```python
sub = parser.add_subparsers(dest="command")
sub.add_parser("disk-usage", help="...")
```
- **Subcommands** — 1 CLI nhiều lệnh như `git commit`, `git push`

```python
if args.command == "disk-usage":
    cmd_disk_usage(args.path)
```
- Router pattern — giống FastAPI nhưng cho CLI

---

## Câu hỏi thường gặp (FAQ)

**Q: DevOps vs SRE vs Platform Engineer?**  
A: DevOps — automation + culture. SRE — focus reliability (Google). Platform — xây nền tảng cho dev team.

**Q: Python vs Bash cho automation?**  
A: Bash — task shell đơn giản. Python — logic phức tạp, API, data processing.

**Q: Script scan secret có đủ cho production?**  
A: Không — production cần thêm: SAST tool (Bandit), pre-commit hook, vault cho secrets.

> Pipeline CI/CD đầy đủ (Gitleaks → Trivy → SBOM → gate): học tiếp [Module 26](../26-devsecops-cicd-security/README.md).


---

## Bài tập

→ [exercises/bai_tap.md](exercises/bai_tap.md)

## Liên kết

Sau module này → [MLOps Labs](../../labs/) để thực hành trên Kubernetes thật.
