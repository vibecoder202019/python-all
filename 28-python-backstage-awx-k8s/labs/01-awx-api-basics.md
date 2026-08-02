# Lab 01 — AWX API với Python

## Mục tiêu

List job templates và launch (tạo task) ở **demo mode**.

```bash
bash scripts/setup.sh
python3 examples/01_awx_list_job_templates.py
python3 examples/02_awx_launch_job.py
python3 project/run_launch.py --demo list
python3 project/run_launch.py --demo launch --template-id 7 \
  --extra-vars '{"app_name":"lab01","replicas":2}'
```

## Live AWX

Sửa `data/.env`, bỏ demo:

```bash
export AWX_DEMO=false
set -a; source data/.env; set +a
python3 project/run_launch.py list
```
