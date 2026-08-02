# Lab 04 — Self-assessment toolkit (site của bạn)

**Phạm vi:** Chỉ domain/staging **bạn sở hữu**.

## Mục tiêu

Chạy một vòng: headers → Lighthouse (nếu có Node) → heuristics Module 25 → (tuỳ chọn) ZAP/Nuclei nếu đã cài.

## Bước 1 — Scope

```bash
export TARGET="https://staging.YOUR_DOMAIN"   # đổi thành site của bạn
echo "I own or am authorized to test: $TARGET"
```

## Bước 2 — Headers + Module 25

```bash
curl -sI "$TARGET" | tee /tmp/headers.txt
bash scripts/02-run-all-examples.sh
```

Đối chiếu header thiếu với `examples/03_security_headers_check.py` (fixture) — liệt kê 3 header cần thêm lên site thật.

## Bước 3 — Lighthouse (nếu có)

```bash
command -v lighthouse && lighthouse "$TARGET" --quiet --chrome-flags="--headless" --output json --output-path /tmp/lh.json \
  && python3 -c "import json;d=json.load(open('/tmp/lh.json'));print({k:round(d['categories'][k]['score']*100) for k in d['categories']})"
```

Ghi 3 cơ hội tối ưu Performance/SEO.

## Bước 4 — (Tuỳ chọn) ZAP baseline / Nuclei

Xem lệnh đầy đủ: [docs/03-authorized-self-assessment.md](../docs/03-authorized-self-assessment.md)

## Báo cáo nộp (memo ngắn)

1. Scope URL  
2. Top 5 findings (severity mật + perf/SEO)  
3. P0 đã sửa / kế hoạch sửa  
4. Xác nhận không scan site ngoài scope  

## Không làm

Scan domain không thuộc quyền bạn; DoS production; negative SEO.
