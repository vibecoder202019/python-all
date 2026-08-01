# Hướng dẫn chạy Manual — Module 12: DevOps & DevSecOps

> Lệnh trích từ `scripts/setup.sh`, `run_all_examples.sh`, `run_project.sh`, `demo_infra.sh`.

## Phần 0 — Kiểm tra

```bash
python3 --version
command -v docker && docker --version || echo "Docker tùy chọn (example 05)"
```

## Phần A — Cài đặt (`scripts/setup.sh`)

```bash
cd learn-python-ai
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install pyyaml httpx python-dotenv
mkdir -p 12-python-devops-devsecops/data
```

**Kiểm tra:**

```bash
python -c "import yaml, httpx, dotenv; print('OK')"
test -f 12-python-devops-devsecops/data/sample.log || echo "Chạy setup.sh để tạo sample data"
```

*(Script tự tạo `data/sample.log`, `config.yaml`, `.env.example` — nếu thiếu, chạy `bash 12-python-devops-devsecops/scripts/setup.sh` một lần.)*

## Phần B — Ví dụ (`scripts/run_all_examples.sh`)

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

## Phần C — Dự án (`scripts/run_project.sh`)

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

## Phần D — Demo infra (`scripts/demo_infra.sh`)

```bash
cd learn-python-ai
source .venv/bin/activate
python 12-python-devops-devsecops/project/step06_final.py disk-usage --path 12-python-devops-devsecops
python 12-python-devops-devsecops/project/step06_final.py parse-log --file 12-python-devops-devsecops/data/sample.log
python 12-python-devops-devsecops/project/step06_final.py security-scan --path 12-python-devops-devsecops/data/
```

## Bản đồ script ↔ manual

| Script | Phần |
|--------|------|
| `setup.sh` | A |
| `run_all_examples.sh` | B |
| `run_project.sh` | C |
| `demo_infra.sh` | D |
