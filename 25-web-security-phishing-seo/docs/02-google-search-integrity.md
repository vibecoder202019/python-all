# Google Search Integrity — lý thuyết cho chủ site (người mới)

> Mục tiêu: khi organic traffic giảm, bạn **triage đúng** thay vì đoán “bị đối thủ đánh SEO”.

## 1. Google xếp hạng — hình dung đơn giản

Google cố gắng đưa người dùng tới trang:

1. **Liên quan** đến câu hỏi, và  
2. **Đáng tin / hữu ích / an toàn**

Nhiều tín hiệu (hàng trăm) — bạn không cần thuộc hết. Chủ site cần nắm:

| Nhóm tín hiệu | Ví dụ |
|---------------|--------|
| Nội dung | Độ sâu, độc đáo, E-E-A-T |
| Kỹ thuật | Index được không, tốc độ, mobile |
| An toàn | Không malware, không phishing host trên domain bạn |
| Liên kết / danh tiếng | Backlink tự nhiên, thương hiệu |

Khi site **bị hack gắn spam**, tín hiệu “an toàn” vỡ → có thể mất hạng hoặc hiện cảnh báo.

## 2. Công cụ trung tâm: Google Search Console (GSC)

GSC là “bảng điều khiển” chủ site với Google:

- URL nào được index  
- Có **Security Issues** không  
- Có **Manual Actions** không  
- Lỗi coverage / sitemap  
- Hiệu suất truy vấn (click, impression)

Lab dùng file JSON **giả lập** báo cáo GSC — không cần API để học logic triage.

## 3. Bốn nhánh triage (học thuộc)

### Nhánh A — `security_compromise` (P0)

**Dấu hiệu:** Security Issues; URL lạ (`/cheap-...`, web shell); redirect lạ; GSC báo hacked.

**Ý nghĩa:** Ai đó đã ghi được file độc / spam lên server bạn (plugin cũ, mật khẩu yếu, RCE…).

**Việc làm (thứ tự gợi ý):**

1. Tạm offline / chặn URL độc nếu cần  
2. Đổi toàn bộ mật khẩu hosting, CMS, DB, FTP, token CI  
3. Quét backdoor, xóa plugin theme lạ, so sánh với backup sạch  
4. Removals các URL spam trên GSC  
5. Request Review sau khi sạch  

### Nhánh B — `manual_action`

**Dấu hiệu:** Có mục Manual Actions (spam, cloaking, scraped content…).

**Ý nghĩa:** Reviewer/Google hệ thống kết luận site vi phạm chính sách.

**Việc làm:** Đọc đúng loại vi phạm → gỡ triệt để → nộp reconsideration (thành thật, có bằng chứng đã sửa).

### Nhánh C — `technical_indexing`

**Dấu hiệu:** Coverage errors lớn; `noindex` nhầm; `Disallow: /` trên production; canonical/redirect loop.

**Ý nghĩa:** Google không đọc/index đúng — không nhất thiết bị phạt bảo mật.

**Việc làm:** Sửa robots, sitemap, status code, rồi Request indexing có chọn lọc.

### Nhánh D — `quality_update`

**Dấu hiệu:** Traffic giảm sau Core Update / Spam Update; GSC không có Security/Manual.

**Ý nghĩa:** Hệ thống xếp hạng đánh giá lại chất lượng toàn cục.

**Việc làm:** Cải thiện nội dung thật, giảm thin/AI-spam, củng cố tác giả/nguồn — **không panic** đổi domain mỗi tuần.

## 4. E-E-A-T giải thích dễ hiểu

| Chữ | Ý |
|-----|---|
| **E**xperience | Có trải nghiệm thực không (review sản phẩm đã dùng…) |
| **E**xpertise | Người viết có chuyên môn không |
| **A**uthoritativeness | Site/thương hiệu có được coi là nguồn đáng tham khảo không |
| **T**rust | Minh bạch, an toàn, chính sách rõ, không lừa đảo |

Chủ đề YMYL (sức khỏe, tiền bạc, pháp lý) cần Trust/Expertise cao hơn blog giải trí.

## 5. Liên hệ Module 25 code

- `audit_seo_integrity` — cộng điểm rủi ro khi thấy path spam, Security Issues, outbound spam  
- `triage_ranking_drop` — chọn nhánh A/B/C/D ở trên  

Chạy:

```bash
python3 examples/05_seo_integrity_audit.py
python3 examples/06_search_penalty_triage.py
```

## 6. Hiểu sai phổ biến

| Hiểu sai | Thực tế |
|----------|---------|
| “Đối thủ negative SEO làm mình rớt” | Thường hiếm hơn bị hack/self-spam/kỹ thuật/update; hãy mở GSC trước |
| “Cần tool mật để đẩy lại top” | Cần cleanup + nội dung + kỹ thuật đúng |
| “Core Update = bị phạt tay” | Không phải Manual Action; là điều chỉnh thuật toán |

## 7. Bài tự kiểm tra

1. Phân biệt Security Issues vs Manual Actions.  
2. Vì sao đổi mật khẩu ngay sau khi bị hack?  
3. Khi nào nên “chờ 2–4 tuần” thay vì đập đi xây lại site?
