# Interview & portfolio — Principal DevOps / Cloud Manager

## Portfolio tối thiểu (từ labs module này)

1. `portfolio/one-pager.md`  
2. 2 ADR  
3. 1 runbook + 1 postmortem  
4. SLO workbook  
5. `governance-scorecard.json` + giải thích điểm yếu  
6. Sơ đồ landing zone (ASCII/draw.io)  

## Câu hỏi phỏng vấn hay gặp — hướng trả lời

**“Design CI/CD for 50 microservices”**  
→ Golden path template, OIDC, progressive delivery, ownership per service, platform metrics.

**“AWS Organization bị shadow IT”**  
→ SSO, SCP, account vending, showback, exception process.

**“Kể 1 incident bạn lead”**  
→ Timeline, impact, mitigation, action items systemic (không đổ lỗi cá nhân).

**“Giảm 20% cloud bill”**  
→ Top services, idle, rightsizing, storage lifecycle, commit discount — đo trước/sau.

**“Platform team vs SRE vs DevOps”**  
→ DevOps văn hóa; SRE reliability empirics; Platform sản phẩm nội bộ cho eng.

## Red flags khi trả lời

- Chỉ liệt kê tool, không trade-off  
- “Tôi trực hết” thay vì xây hệ thống  
- Tắt security gate để “nhanh” không có risk acceptance  
