# Google Search Integrity — vì sao site rớt hạng & cách khôi phục

> Góc nhìn **chủ sở hữu site**. Không mô tả kỹ thuật để phá ranking đối thủ.

## Các nhánh triage

| Nhánh | Khi nào | Việc làm |
|-------|---------|----------|
| `security_compromise` | Security Issues, URL spam lạ, malware | Cleanup hack → Removals → Request Review |
| `manual_action` | Manual Actions trong GSC | Sửa vi phạm → reconsideration |
| `technical_indexing` | Coverage errors lớn | robots, sitemap, canonical, soft-404 |
| `quality_update` | Sau Core/Spam update | Cải thiện nội dung / E-E-A-T |
| `monitor` | Chưa rõ | Kiểm tra tracking, seasonality |

## Liên hệ “rớt top Google”

- Site **bị hack** rồi bị dùng làm phishing/spam → Google hạ / cảnh báo → traffic organic sụt.  
- Lab fixture `gsc_fixture_compromised.json` mô phỏng case này.  
- Khôi phục = **bảo mật + tuân thủ chính sách** — không phải SEO đen.

## Tài liệu tham khảo (chính thức)

- Google Search Central — Security Issues  
- Google Search Central — Manual Actions  
- OWASP Top 10 (hiểu vector tấn công để harden)
