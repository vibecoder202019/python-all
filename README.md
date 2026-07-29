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
| Làm DevOps Engineer | 01 → 05 → 12 → 13 → **15** |
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

## Lộ trình học (15 module)

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

**Tổng thời gian:** khoảng 5-7 tháng (học 1-2 giờ/ngày)

## Cách học hiệu quả

1. **Đọc lý thuyết** trong `README.md` của từng module
2. **Chạy ví dụ** trong thư mục `examples/` — sửa và thử nghiệm
3. **Làm bài tập** trong `exercises/bai_tap.md`
4. **Đối chiếu đáp án** trong `exercises/solutions/` (chỉ xem sau khi đã cố gắng)
5. **Ghi chú** những phần chưa hiểu, quay lại ôn tập

## Cấu trúc mỗi module

```
module/
├── README.md          # Lý thuyết chi tiết (tiếng Việt)
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
Đọc lý thuyết → Chạy examples → Đọc "Giải thích chi tiết" → Sửa/thử code → Làm bài tập → Chạy project
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
