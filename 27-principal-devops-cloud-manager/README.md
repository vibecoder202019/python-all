# Module 27: Principal DevOps Engineer & Cloud Manager

Lộ trình **tự học + thực hành** để tiến tới vai trò **Principal DevOps Engineer** và **Cloud Manager** (quản lý nền tảng cloud / nền tảng kỹ thuật ở quy mô tổ chức).

> **Không phải** khóa “học thuộc tool”. Principal = **thiết kế hệ thống + lãnh đạo kỹ thuật + quản trị rủi ro/chi phí/con người** trên nền tảng đã học ở Module 12–26.

**Tiên quyết khuyến nghị:** Module **12, 13, 15–19, 22, 26** (và nên biết Module 16, 25 ở mức đọc hiểu).  
**Thời gian:** 4–8 tuần (1–2 giờ/ngày) hoặc 2–3 tuần full-time project.

---

## Mục tiêu

Sau module này bạn sẽ:

1. Phân biệt Junior → Mid → Senior → **Principal** DevOps / Cloud Manager  
2. Viết được **ADR**, landing zone outline, SLO/SLI, runbook, postmortem  
3. Thiết kế **operating model** (platform team vs product teams)  
4. Làm **FinOps** cơ bản: nhìn cost, tag, anomaly, budget guardrail  
5. Chấm **governance scorecard** (IAM, logging, backup, CI gate…)  
6. Hoàn thành **capstone portfolio** trình bày được trong phỏng vấn Principal / Cloud Manager  

---

## Cách tự học

1. Đọc hết **Lý thuyết nền tảng** trong README này  
2. Đọc docs `01` → `04`  
3. Làm labs **theo thứ tự** — mỗi lab ra **artifact** (Markdown/JSON) bỏ vào `portfolio/`  
4. Chạy scripts chấm scorecard  
5. Viết capstone 1 pager + sơ đồ kiến trúc  

```bash
cd learn-python-ai
bash 27-principal-devops-cloud-manager/scripts/setup.sh
bash 27-principal-devops-cloud-manager/scripts/01-check-prerequisites.sh
bash 27-principal-devops-cloud-manager/scripts/02-init-portfolio.sh
bash 27-principal-devops-cloud-manager/scripts/03-run-governance-scorecard.sh
```

Manual: [readme_manual.md](readme_manual.md)

---

## Lý thuyết nền tảng (đọc kỹ)

### 1. Principal DevOps / Cloud Manager làm gì?

| Vai trò gần | Trọng tâm |
|-------------|-----------|
| **Senior DevOps** | Làm sâu pipeline, K8s, IaC cho 1–vài sản phẩm |
| **Principal DevOps** | Chuẩn hóa **platform**, quyết định kiến trúc, mentor, giảm rủi ro toàn org |
| **Cloud Manager / Cloud Platform Manager** | Quản trị **multi-account/cloud**, ngân sách, compliance, vendor, SLA với business |

**Ví von:** Senior là thợ cả giỏi sửa máy; Principal thiết kế **xưởng** và quy trình để 10 đội sản xuất an toàn, rẻ, nhanh; Cloud Manager giữ **nhà máy + hóa đơn điện + giấy phép**.

Principal **không** phải người merge mọi PR hay on-call 24/7 một mình. Họ:

- Đặt **chuẩn** (golden path): CI template, landing zone, observability  
- Ra **quyết định có ghi nhận** (ADR) khi trade-off lớn  
- Nói chuyện được với CTO (rủi ro) và CFO (chi phí)  
- Xây đội / cộng đồng thực hành (guild), không biến thành bottleneck  

---

### 2. Thang năng lực (tự đánh giá)

| Cấp | Bạn làm được |
|-----|----------------|
| L1 | Chạy pipeline, deploy 1 app, đọc CloudWatch |
| L2 | Terraform module, multi-env, on-call theo runbook |
| L3 | Thiết kế CI org-wide, multi-account cơ bản, dẫn dắt incident vừa |
| L4 **Principal track** | Platform strategy, FinOps + security governance, mentorship, roadmap 2–4 quý |
| L5 | Org design cloud, M&A integration, multi-cloud policy, board-level risk |

Module này tập trung **L3 → L4**. Checklist tự chấm: [docs/01-career-ladder.md](docs/01-career-ladder.md)

---

### 3. Bốn trụ cột Principal phải nắm

```
┌─────────────────────────────────────────────────────────┐
│                 PRINCIPAL / CLOUD MANAGER                 │
├──────────────┬──────────────┬──────────────┬────────────┤
│  Platform    │  Reliability │  Security &  │  FinOps &  │
│  Engineering │  (SRE)      │  Governance  │  Vendor    │
├──────────────┼──────────────┼──────────────┼────────────┤
│ Golden paths │ SLO/SLI/Error│ IAM, SCP,    │ Cost, tag, │
│ Self-service │   budget     │ secrets, CI  │ budget,    │
│ IDP / portal │ Incident mgmt│ compliance   │ RI/Savings │
└──────────────┴──────────────┴──────────────┴────────────┘
```

| Trụ | Câu hỏi bạn phải trả lời được | Module liên quan |
|-----|-------------------------------|------------------|
| **Platform** | Dev tự phục vụ được gì trong 15 phút? | 15, 17, 21, 24 |
| **Reliability** | User chịu downtime bao nhiêu? ai gọi khi cháy? | 18, runbook lab |
| **Security/Gov** | Ai vào prod? secret ở đâu? CI có gate không? | 16, 19, 22, 26 |
| **FinOps** | Tháng này burn bao nhiêu? anomaly vì sao? | 13, 22 + lab FinOps |

---

### 4. Platform Engineering (golden path)

**Anti-pattern:** Mỗi team tự chế CI/CD, VPC, monitoring → 20 cách khác nhau, không ai support nổi.

**Principal approach:**

1. Cung cấp **golden path** (mặc định tốt): template repo + workflow Module 26 + Terraform module  
2. Cho **escape hatch** có kiểm soát (không cấm tuyệt đối mọi thứ)  
3. Đo adoption: % service đi golden path  

**Internal Developer Platform (IDP)** ý tưởng: portal/self-service tạo namespace, DB, pipeline — không cần ticket 2 tuần.

Lab 02: bạn viết “Platform catalog” 1 trang cho công ty giả lập.

---

### 5. SRE tối thiểu cho Principal

| Khái niệm | Nghĩa đơn giản |
|-----------|----------------|
| **SLI** | Chỉ số đo được (latency p99, availability) |
| **SLO** | Mục tiêu (vd availability 99.9%) |
| **Error budget** | Phần trăm được “hỏng”; hết budget → dừng feature, ưu tiên reliability |
| **Incident** | Sự cố ảnh hưởng user; cần commander + comms + postmortem không đổ lỗi |

Principal đảm bảo org **có** SLO cho dịch vụ quan trọng — không phải tự viết mọi Prometheus rule.

---

### 6. Cloud governance & multi-account

Cloud Manager sống với:

```
Management account
 ├── Security / Log archive
 ├── Shared services (CI, DNS, images)
 └── Workloads OU
      ├── Dev / Staging / Prod (tách blast radius)
```

Nguyên tắc: **least privilege**, SCP chặn vùng nguy hiểm, không human long-lived admin trên prod, OIDC từ CI (Module 26), Vault/SSM cho secret (Module 19).

Chi tiết: [docs/02-cloud-operating-model.md](docs/02-cloud-operating-model.md)

---

### 7. FinOps — quản lý chi phí như sản phẩm

| Việc | Mục đích |
|------|----------|
| Tag bắt buộc (`env`, `owner`, `cost-center`) | Quy trách nhiệm |
| Budget + alert | Không “hết tháng mới biết” |
| Anomaly detection | Spot instance/leak |
| Rightsizing | Máy/to lớn so với dùng |
| Showback/chargeback | Team thấy bill của mình |

Principal không cần là accountant — cần **ngôn ngữ chung** với finance và guardrail kỹ thuật (SCP deny regions đắt không dùng, bắt tag…).

---

### 8. Quyết định kiến trúc = ADR

Khi chọn “EKS vs ECS”, “multi-region active-active vs warm standby”:

1. Viết **Architecture Decision Record** (context, options, decision, consequences)  
2. Review với stakeholders  
3. Lưu git — 6 tháng sau biết *vì sao*  

Lab 01 bắt buộc viết ≥ 2 ADR.

---

### 9. Lãnh đạo kỹ thuật (soft skills cứng)

- **Mentoring:** senior grow bằng cặp ADR/review, không chỉ “merge giúp”  
- **Stakeholder:** dịch rủi ro kỹ thuật → ngôn ngữ business (“mất 2h checkout = mất $X”)  
- **Roadmap:** quý này platform; quý sau FinOps; không đổi tool mỗi tuần  
- **Hiring bar:** phỏng vấn Principal nhìn system design + incident leadership  

[docs/03-leadership-and-communication.md](docs/03-leadership-and-communication.md)

---

## Lộ trình lab (thực hành)

| Lab | Artifact trong `portfolio/` | Thời gian |
|-----|----------------------------|-----------|
| [01](labs/01-adr-and-system-design.md) | 2 ADR + sơ đồ 1 service | 3–5h |
| [02](labs/02-platform-golden-path.md) | Platform catalog + golden path CI | 3–5h |
| [03](labs/03-slo-runbook-postmortem.md) | SLO sheet + runbook + postmortem giả | 4–6h |
| [04](labs/04-finops-governance.md) | Cost policy + governance score JSON | 3–4h |
| [05](labs/05-capstone-portfolio.md) | 1-pager Principal + demo narrative | 6–10h |

Docs: [01 career](docs/01-career-ladder.md) · [02 operating model](docs/02-cloud-operating-model.md) · [03 leadership](docs/03-leadership-and-communication.md) · [04 interview](docs/04-interview-and-portfolio.md)

---

## Cấu trúc

```
27-principal-devops-cloud-manager/
├── templates/          # ADR, runbook, SLO, postmortem, 1-pager
├── examples/           # Mẫu đã điền (tham khảo sau khi tự làm)
├── data/               # Fixture cost/governance lab
├── project/            # scorecard Python
├── portfolio/          # Bạn tạo bằng script (gitignore nội dung cá nhân tùy chọn)
├── labs/
├── docs/
├── scripts/
├── cheatsheet/
├── README.md
└── readme_manual.md
```

---

## Map kiến thức từ module trước → Principal

| Bạn đã học | Principal dùng để |
|------------|-------------------|
| 12 DevOps scripts | Chuẩn automation org |
| 13 + 22 AWS | Landing zone, IAM, Org |
| 15–18 K8s/CKA | Platform runtime chuẩn |
| 19 Vault/TF | Secret + IaC module governance |
| 21 Terrakube | Self-service IaC UI |
| 26 DevSecOps CI | Golden path security gates |
| 23–24 AI/n8n | Tự động hóa vận hành (không thay governance) |

---

## FAQ

**Tôi chưa đủ Senior có học được không?**  
Có — học lý thuyết + làm lab portfolio. Xin việc Principal thì cần thêm năm kinh nghiệm thực tế; module giúp **định hướng và chứng minh tư duy**.

**Cloud Manager có cần code không?**  
Cần đọc được IaC/CI và ra quyết định; lab vẫn thực hành ADR/scorecard bằng Markdown + Python nhẹ.

**Multi-cloud bắt buộc?**  
Không. Principal giỏi **một cloud sâu + mô hình portable** tốt hơn “ba cloud nông”. Lab mặc định AWS-centric (Module 22).

**Teardown**

```bash
bash scripts/06-teardown.sh
```

---

[readme_manual.md](readme_manual.md) | [cheatsheet/principal-cloud.md](cheatsheet/principal-cloud.md)
