# Lab 03 — Search integrity & recovery

**Mục tiêu:** Khi organic traffic giảm, triage đúng nhánh: security / manual / technical / core update.

## Bước

```bash
python3 examples/05_seo_integrity_audit.py
python3 examples/06_search_penalty_triage.py
bash scripts/03-run-project.sh
cat data/last_audit_report.json
```

## Việc cần làm

1. So sánh `gsc_fixture_compromised.json` vs `gsc_fixture_core_update.json` — branch triage khác nhau thế nào?
2. Viết checklist 5 bước cleanup nếu CMS bị inject spam page (đổi pass, quét plugin, xóa URL, Removals, Request Review).
3. Giải thích vì sao “làm đối thủ rớt top” **không** phải nội dung module / không hợp pháp.

## Kết quả kỳ vọng

`triage` = `security_compromise` với fixture compromised; `quality_update` với core update fixture.
