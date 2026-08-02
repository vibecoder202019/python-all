"""Governance scorecard — chấm điểm cloud governance (lab fixture hoặc JSON tự điền)."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def score(data: dict) -> dict:
    checks = data.get("checks") or []
    total_w = sum(float(c.get("weight", 1)) for c in checks) or 1.0
    earned = sum(float(c.get("weight", 1)) for c in checks if c.get("pass"))
    pct = round(100.0 * earned / total_w, 1)
    failed = [c for c in checks if not c.get("pass")]
    grade = (
        "A"
        if pct >= 90
        else "B"
        if pct >= 75
        else "C"
        if pct >= 60
        else "D"
        if pct >= 40
        else "F"
    )
    return {
        "org": data.get("org"),
        "score_pct": pct,
        "grade": grade,
        "passed": len(checks) - len(failed),
        "failed": len(failed),
        "failed_items": [
            {"id": c.get("id"), "title": c.get("title"), "weight": c.get("weight")}
            for c in failed
        ],
        "principal_actions": _actions(failed),
    }


def _actions(failed: list[dict]) -> list[str]:
    hints = {
        "scp_regions": "Draft SCP allow-list regions; ADR + change window",
        "oidc_ci": "Migrate deploy roles to GitHub OIDC (Module 26 pattern)",
        "backup_prod": "Schedule restore drill; document RPO/RTO",
        "budget_alert": "Create budgets per OU + anomaly detection",
        "slo_critical": "Pick top 3 journeys; publish SLO workbook",
        "patch_cadence": "Define base image rebuild cadence in platform catalog",
    }
    out = []
    for c in failed:
        out.append(hints.get(c.get("id", ""), f"Remediate: {c.get('title')}"))
    return out


def main() -> None:
    p = argparse.ArgumentParser(description="Cloud governance scorecard")
    p.add_argument(
        "-i",
        "--input",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "data" / "governance_fixture.json",
    )
    p.add_argument("-o", "--output", type=Path, default=None)
    args = p.parse_args()
    data = json.loads(args.input.read_text())
    # fix accidental space in id from fixture if present
    for c in data.get("checks", []):
        if c.get("id") == "prod_ Separated":
            c["id"] = "prod_separated"
    result = score(data)
    text = json.dumps(result, indent=2, ensure_ascii=False)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n")
        print(f"\n✓ Wrote {args.output}")


if __name__ == "__main__":
    main()
