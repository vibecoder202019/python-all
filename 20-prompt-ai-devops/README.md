# Module 20: Tự học Prompt AI — Basic → Advanced cho DevOps & Code

Lộ trình **tự học prompt engineering** để làm việc hiệu quả với AI (Cursor, ChatGPT, Claude...) khi viết **Python**, vận hành **Kubernetes**, quản lý **Vault/Terraform**, **monitoring** và **logging**.

> **Triết lý module:** AI là **copilot**, không thay thế tư duy. Bạn học cách **đặt câu hỏi đúng**, **kiểm tra output**, và **không lộ secret**.

---

## Mục tiêu

| Kỹ năng | Kết quả |
|---------|---------|
| **Prompt cơ bản** | Role, context, constraint, output format — framework R-C-T-O |
| **Prompt nâng cao** | Chain-of-thought, few-shot, decomposition, iterative refine |
| **Python** | Debug, refactor, test, FastAPI, boto3 — prompt có file + lỗi cụ thể |
| **Kubernetes** | Troubleshoot Pod, viết YAML, NetworkPolicy, CKA-style task |
| **Vault & Terraform** | Policy HCL, plan review, secret-safe IaC |
| **Monitoring & Logging** | PromQL, alert rules, parse log, RCA (root cause) |
| **Workflow IDE** | Cursor Agent, @file, rules, review diff |

---

## Ai nên học module này?

- Đã học Module 01–05 (Python cơ bản) **hoặc** có kinh nghiệm code
- Đang học / làm Module 12–19 (DevOps, K8s, Vault)
- Muốn **tăng tốc** debug và viết infra code bằng AI **an toàn**

---

## Yêu cầu

| Công cụ | Mục đích |
|---------|----------|
| **Cursor** hoặc IDE có AI | Thực hành agent workflow |
| **Tài khoản LLM** (tùy chọn) | ChatGPT / Claude web |
| Module 15–19 (tham chiếu) | Context K8s, Vault lab |

Không cần GPU — module này dạy **cách prompt**, không train model.

---

## Lộ trình (4–6 tuần)

```
Tuần 1:  Prompt cơ bản + framework (docs 01–02, lab 01–03)
Tuần 2:  Python + code review (doc 03, lab 04–05)
Tuần 3:  Kubernetes (doc 04, lab 06–07)
Tuần 4:  Vault, Terraform (doc 05, lab 08)
Tuần 5:  Monitoring, logging (doc 06, lab 09–10)
Tuần 6:  Cursor workflow + capstone (doc 07–08, lab 11–12)
```

---

## Cấu trúc module

```
20-prompt-ai-devops/
├── README.md
├── docs/                 # Lý thuyết 00–08
├── prompts/              # Template copy-paste theo domain
├── examples/             # Prompt tệ → prompt tốt (before/after)
├── labs/                 # 12 lab thực hành
├── cheatsheet/           # Framework + checklist
├── scripts/              # Setup, mở lab
└── exercises/            # Bài tập + rubric chấm prompt
```

---

## Chạy nhanh

```bash
cd learn-python-ai

# Mở lab 01
bash 20-prompt-ai-devops/scripts/02-run-lab.sh 01

# Xem template Python debug
cat 20-prompt-ai-devops/prompts/python/debug-error.md

# Cheatsheet framework R-C-T-O
cat 20-prompt-ai-devops/cheatsheet/prompt-framework.md
```

---

## Lab (12 lab)

| # | Lab | Level |
|---|-----|-------|
| 01 | [Framework R-C-T-O](labs/basic/lab01-framework-rcto.md) | Basic |
| 02 | [Prompt tệ vs prompt tốt](labs/basic/lab02-before-after.md) | Basic |
| 03 | [Iterative refine](labs/basic/lab03-iterative-refine.md) | Basic |
| 04 | [Debug Python](labs/basic/lab04-python-debug.md) | Basic |
| 05 | [Viết test Python](labs/intermediate/lab05-python-tests.md) | Intermediate |
| 06 | [Troubleshoot K8s Pod](labs/intermediate/lab06-k8s-troubleshoot.md) | Intermediate |
| 07 | [Viết manifest K8s](labs/intermediate/lab07-k8s-manifests.md) | Intermediate |
| 08 | [Vault policy & Terraform review](labs/intermediate/lab08-vault-terraform.md) | Intermediate |
| 09 | [PromQL & alerts](labs/advanced/lab09-prometheus.md) | Advanced |
| 10 | [Log analysis RCA](labs/advanced/lab10-logging-rca.md) | Advanced |
| 11 | [Cursor Agent workflow](labs/advanced/lab11-cursor-agent.md) | Advanced |
| 12 | [Capstone incident response](labs/advanced/lab12-capstone.md) | Advanced |

---

## Tài liệu đọc theo thứ tự

1. [Lộ trình](docs/00-lo-trinh.md)
2. [Prompt cơ bản](docs/01-prompt-co-ban.md)
3. [Prompt nâng cao](docs/02-prompt-nang-cao.md)
4. [Python & code](docs/03-prompt-python-code.md)
5. [Kubernetes](docs/04-prompt-kubernetes.md)
6. [Vault & Terraform](docs/05-prompt-vault-terraform.md)
7. [Monitoring & Logging](docs/06-prompt-monitoring-logging.md)
8. [Cursor & Agent workflow](docs/07-cursor-agent-workflow.md)
9. [An toàn & chất lượng](docs/08-an-toan-va-chat-luong.md)

---

## Liên kết module

- [Module 12 — DevOps](../12-python-devops-devsecops/README.md)
- [Module 15–18 — K8s](../15-ansible-awx-minio-k8s/README.md)
- [Module 19 — Vault/Terraform](../19-vault-terraform/README.md)
