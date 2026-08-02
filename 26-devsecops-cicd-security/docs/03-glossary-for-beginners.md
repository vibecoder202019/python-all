# Bảng thuật ngữ DevSecOps — người mới

In hoặc để tab này mở khi đọc YAML / log CI.

| Thuật ngữ | Đọc là | Giải thích một câu |
|-----------|--------|---------------------|
| CI | Continuous Integration | Tự build/test khi có code mới |
| CD | Continuous Delivery/Deploy | Tự (hoặc bán tự động) đưa bản build lên môi trường |
| Pipeline | đường ống | Chuỗi bước tự động từ code → artifact/deploy |
| PR | Pull Request | Đề nghị merge nhánh; chỗ CI chạy và người review |
| Artifact | hiện vật build | File/image sinh ra từ CI (wheel, SBOM, docker image) |
| Secret | bí mật | Password, token, key — không được commit |
| CVE | Common Vulnerabilities and Exposures | Mã lỗ hổng công bố |
| SCA | Software Composition Analysis | Quét thư viện phụ thuộc |
| SAST | Static Application Security Testing | Quét mã nguồn tĩnh |
| DAST | Dynamic Application Security Testing | Quét ứng dụng đang chạy |
| SBOM | Software Bill of Materials | Danh sách thành phần phần mềm |
| SARIF | Static Analysis Results Interchange Format | Format báo cáo scan đưa vào GitHub Code Scanning |
| OIDC | OpenID Connect | Cách login/ủy quyền bằng token ngắn (dùng cho cloud từ GitHub) |
| Gate / Policy gate | cổng kiểm soát | Điều kiện bắt buộc phải đạt mới qua (merge/deploy) |
| Shift-left | dịch trái | Làm bảo mật sớm hơn trong vòng đời |
| Fail-closed | lỗi thì đóng | Không chắc an toàn → chặn |
| Fail-open | lỗi thì mở | Tool hỏng vẫn cho qua (nguy hiểm nếu lạm dụng) |
| Branch protection | bảo vệ nhánh | Luật trên `main`: cần review + CI xanh |
| Base image | ảnh nền | `FROM ...` trong Dockerfile |
| Registry | kho ảnh | Nơi lưu Docker image (GHCR, ECR…) |
| Pin (version/SHA) | ghim phiên bản | Không dùng `latest`/`v1` trôi nổi |
| Pre-commit | móc trước commit | Chạy check trên máy dev trước khi commit |
| Runtime | lúc chạy | Khác “lúc đọc code” (static) |
| Staging | môi trường thử | Giống prod nhưng không phải user thật toàn bộ |
| Production | môi trường thật | User thật — cẩn thận mọi thay đổi |

## Cặp dễ nhầm

| Nhầm | Nhớ |
|------|-----|
| SAST = DAST | SAST đọc code; DAST đánh URL sống |
| SCA = Trivy image | SCA nhìn lockfile; Trivy image nhìn cả OS trong image |
| SBOM = đã an toàn | SBOM chỉ inventory; vẫn cần scan CVE |
| Xóa file = hết lộ secret | Phải rotate key; git history còn |
| CI xanh = hết lỗ hổng | Chỉ hết lỗ hổng **tool đã che được** |

## Xem thêm

- [01-devsecops-pipeline.md](01-devsecops-pipeline.md)
- [02-tools-matrix.md](02-tools-matrix.md)
- README Module 26
