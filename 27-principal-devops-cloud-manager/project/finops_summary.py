"""FinOps helper — tóm tắt cost fixture + gợi ý hành động Principal."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def analyze(data: dict) -> dict:
    services = sorted(data.get("by_service") or [], key=lambda x: -x["amount"])
    top3 = services[:3]
    total = float(data.get("total") or 0)
    return {
        "org": data.get("org"),
        "month": data.get("month"),
        "total": total,
        "untagged_spend_pct": data.get("untagged_spend_pct"),
        "top3": [
            {
                "service": s["service"],
                "amount": s["amount"],
                "share_pct": round(100 * s["amount"] / total, 1) if total else 0,
                "mom_change_pct": s.get("mom_change_pct"),
            }
            for s in top3
        ],
        "anomalies": data.get("anomalies") or [],
        "actions": [
            "Enforce tag policy on new resources (env, owner, cost-center)",
            "Investigate highest MoM growth service first",
            "Set OU budgets at 80/90/100% thresholds",
            "Review NAT / data transfer architecture if networking spikes",
        ],
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument(
        "-i",
        "--input",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "data" / "cost_fixture.json",
    )
    p.add_argument("-o", "--output", type=Path, default=None)
    args = p.parse_args()
    result = analyze(json.loads(args.input.read_text()))
    text = json.dumps(result, indent=2, ensure_ascii=False)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n")


if __name__ == "__main__":
    main()
