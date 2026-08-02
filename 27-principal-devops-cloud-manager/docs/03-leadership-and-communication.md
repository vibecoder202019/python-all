# Leadership & communication — Principal track

## 1. Dịch rủi ro kỹ thuật → business

| Kỹ thuật | Business |
|----------|----------|
| Single AZ DB | 1 sự cố AZ = mất checkout |
| Không backup test restore | RPO/RTO trên giấy, thực tế mất data |
| Admin key trong CI | Rủi ro fraud / ransomware blast |
| Không tag cost | Không biết sản phẩm nào lời/lỗ infra |

Luyện: mỗi ADR có ≥ 1 câu “impact nếu không làm”.

## 2. Meeting mà Principal nên (và không nên) ngồi

**Nên:** architecture review, incident SEV1, quarterly platform roadmap, FinOps sync.  
**Không nên:** mọi sprint planning app — ủy quyền / guild.

## 3. Mentoring pattern

1. Học viên đề xuất ADR nháp  
2. Bạn hỏi “options nào bị loại vì lý do gì?”  
3. Pair review PR infra  
4. Họ lead SEV3 rồi SEV2 với bạn shadow  

## 4. Conflict: tốc độ vs an toàn

Dùng **error budget** và **risk acceptance** có chữ ký — không tranh cãi cảm tính trên Slack.

## 5. Template email status (incident)

Subject: `[SEV1] payments — investigating`  
Impact / since / next update in 30m / bridge link.
