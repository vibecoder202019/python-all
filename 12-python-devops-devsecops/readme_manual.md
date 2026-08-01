# Hướng dẫn chạy Manual — Module 12: DevOps & DevSecOps

> Copy từng lệnh và chạy **tuần tự**. Mỗi phần tương ứng một script trong `scripts/`.

## Điều kiện

- Python 3.10+
- Docker (tùy chọn, cho ví dụ 05)

---

## Phần A — Setup (tương ứng `scripts/setup.sh`)

```bash
cd learn-python-ai
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install pyyaml httpx python-dotenv
```

Tạo sample data (script tự tạo — bạn có thể bỏ qua nếu đã chạy `setup.sh`):

```bash
mkdir -p 12-python-devops-devsecops/data
```

---

## Phần B — Ví dụ (tương ứng `scripts/run_all_examples.sh`)

```bash
cd learn-python-ai
source .venv/bin/activate
python 12-python-devops-devsecops/examples/01_subprocess_bash.py
python 12-python-devops-devsecops/examples/02_pathlib_config.py
python 12-python-devops-devsecops/examples/03_log_analyzer.py
python 12-python-devops-devsecops/examples/04_health_check.py
python 12-python-devops-devsecops/examples/05_docker_script.py
python 12-python-devops-devsecops/examples/06_security_scan.py
```

---

## Phần C — Dự án 6 bước (tương ứng `scripts/run_project.sh`)

```bash
cd learn-python-ai
source .venv/bin/activate
python 12-python-devops-devsecops/project/step01_cli_skeleton.py --demo
python 12-python-devops-devsecops/project/step02_file_ops.py --demo
python 12-python-devops-devsecops/project/step03_log_parser.py --demo
python 12-python-devops-devsecops/project/step04_health_monitor.py --demo
python 12-python-devops-devsecops/project/step05_security_audit.py --demo
python 12-python-devops-devsecops/project/step06_final.py --demo
```

---

## Phần D — Demo infra (tương ứng `scripts/demo_infra.sh`, tùy chọn)

```bash
cd learn-python-ai
source .venv/bin/activate
python 12-python-devops-devsecops/project/step06_final.py disk-usage --path 12-python-devops-devsecops
python 12-python-devops-devsecops/project/step06_final.py parse-log --file 12-python-devops-devsecops/data/sample.log
python 12-python-devops-devsecops/project/step06_final.py security-scan --path 12-python-devops-devsecops/data/
```

---

## Bản đồ script ↔ manual

| Script | Phần |
|--------|------|
| `setup.sh` | A |
| `run_all_examples.sh` | B |
| `run_project.sh` | C |
| `demo_infra.sh` | D |

## Gỡ / dọn dẹp

Không cần.
