# Module 12: Python cho DevOps & DevSecOps

Học Python thực chiến cho **DevOps Engineer** và **DevSecOps Engineer** — automation, CI/CD scripts, security scanning, infrastructure monitoring.

## Mục tiêu

- Viết script automation với `subprocess`, `argparse`, `pathlib`
- Parse YAML/JSON config, log analysis
- Health check services, deploy scripts
- DevSecOps: scan secrets, file permissions, dependency audit
- Hoàn thành CLI tool **DevOps Toolkit** qua 6 bước tuần tự

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

## Bài tập

→ [exercises/bai_tap.md](exercises/bai_tap.md)

## Liên kết

Sau module này → [MLOps Labs](../../labs/) để thực hành trên Kubernetes thật.
