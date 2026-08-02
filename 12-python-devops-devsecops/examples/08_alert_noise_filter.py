#!/usr/bin/env python3
"""
Module 12 — Ví dụ 08: Alert noise filter (tránh nhiễu)

Chạy: python examples/08_alert_noise_filter.py

═══════════════════════════════════════════════════════════════════════════
YÊU CẦU:
  1. Mô phỏng stream alert thô (flapping / info spam / maintenance).
  2. Filter: severity, exclude, consecutive failures, cooldown, state-change.
  3. In SEND vs DROP kèm lý do — thấy nhiễu bị loại.
═══════════════════════════════════════════════════════════════════════════
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "project"))

from monitoring import AlertEvent, AlertFilterConfig, AlertNoiseFilter


def demo_stream() -> list[AlertEvent]:
    """Stream giả lập: 1 site flap 2 lần rồi die thật; spam info; maintenance."""
    base = time.time()
    events: list[AlertEvent] = []

    # Flapping — 2 lần fail rồi recover → không đủ consecutive=3 → DROP
    for i in range(2):
        events.append(AlertEvent(
            alertname="WebsiteDown",
            severity="critical",
            status="firing",
            instance="shop.example.com",
            ts=base + i,
            message=f"flap fail #{i+1}",
        ))
    events.append(AlertEvent(
        alertname="WebsiteDown",
        severity="critical",
        status="resolved",
        instance="shop.example.com",
        ts=base + 2,
        message="recovered quickly",
    ))

    # Die thật — 3 lần firing liên tiếp → SEND lần thứ 3
    for i in range(3):
        events.append(AlertEvent(
            alertname="WebsiteDown",
            severity="critical",
            status="firing",
            instance="api.example.com",
            ts=base + 10 + i,
            message=f"real outage #{i+1}",
        ))

    # Spam cùng state trong cooldown → DROP
    events.append(AlertEvent(
        alertname="WebsiteDown",
        severity="critical",
        status="firing",
        instance="api.example.com",
        ts=base + 20,
        message="still down — should cooldown",
    ))

    # Severity quá thấp → DROP
    events.append(AlertEvent(
        alertname="HighLatency",
        severity="info",
        status="firing",
        instance="cdn.example.com",
        ts=base + 30,
        message="p99 slightly high",
    ))

    # Maintenance window (label) → DROP
    events.append(AlertEvent(
        alertname="WebsiteDown",
        severity="critical",
        status="firing",
        instance="legacy.example.com",
        labels={"maintenance": "true"},
        ts=base + 40,
        message="planned maintenance",
    ))

    # Recovery sau outage → SEND (state change)
    events.append(AlertEvent(
        alertname="WebsiteDown",
        severity="critical",
        status="resolved",
        instance="api.example.com",
        ts=base + 50,
        message="back online",
    ))

    return events


def main() -> None:
    print("=== Alert Noise Filter ===\n")

    cfg = AlertFilterConfig(
        min_severity="warning",
        consecutive_failures=3,
        cooldown_seconds=300.0,
        exclude_alertnames=("Watchdog",),
        exclude_label_pairs=(("maintenance", "true"),),
        state_change_only=True,
    )
    # Lab: cooldown ngắn để demo spam ngay sau SEND
    cfg.cooldown_seconds = 60.0

    filt = AlertNoiseFilter(cfg)
    decisions = filt.process_batch(demo_stream())

    sent = drop = 0
    for d in decisions:
        mark = "📣 SEND" if d.action == "SEND" else "🔇 DROP"
        if d.action == "SEND":
            sent += 1
        else:
            drop += 1
        a = d.alert
        print(
            f"{mark:8s}  [{a.severity:8s}] {a.alertname}@{a.instance or '-':20s} "
            f"status={a.status:8s}  reason={d.reason}"
        )
        if a.message:
            print(f"          └─ {a.message}")

    print(f"\nNoise reduction: SEND={sent}  DROP={drop}  "
          f"(giữ {sent}/{sent+drop} = {100*sent/max(sent+drop,1):.0f}% alerts)")

    # Optional: dump JSON summary
    out = Path(__file__).resolve().parents[1] / "data" / "generated" / "alert_filter_report.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "sent": sent,
        "dropped": drop,
        "decisions": [
            {
                "action": d.action,
                "reason": d.reason,
                "alertname": d.alert.alertname,
                "instance": d.alert.instance,
                "status": d.alert.status,
            }
            for d in decisions
        ],
    }
    out.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Wrote {out}")
    print("\n✓ Done")


if __name__ == "__main__":
    main()
