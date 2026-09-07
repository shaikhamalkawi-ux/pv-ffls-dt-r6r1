#!/usr/bin/env python3
"""Reproduce the empirical 95% width summaries used in the mechanism audit.

Run from the repository root:
    python scripts/reproduce_mechanism_widths.py
"""
from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "derived_results" / "pv" / "mechanism_audit_replicates.csv"
OUT = ROOT / "derived_results" / "pv" / "mechanism_width_reproduction_check.json"
EXPECTED = {
    "joint paired vectors": 0.1109595,
    "closure-only (p,1-p; b independently permuted)": 0.1091016,
    "fully independent marginal elements": 1.0253667,
}

def main() -> None:
    df = pd.read_csv(DATA)
    rows = []
    for construction, d in df.groupby("construction", sort=False):
        q = d[["coef_low_partition", "coef_high_partition"]].quantile([0.025, 0.975])
        width = float((q.loc[0.975] - q.loc[0.025]).sum())
        max_err = float(d["max_row_sum_error"].max())
        rows.append({
            "construction": construction,
            "valid_replicates": int(len(d)),
            "combined_empirical_95pct_width": width,
            "max_row_sum_error": max_err,
            "abs_error_vs_manuscript_rounded": abs(width - EXPECTED[construction]),
        })
    by_name = {r["construction"]: r for r in rows}
    dwidth = by_name["fully independent marginal elements"]["combined_empirical_95pct_width"] / by_name["joint paired vectors"]["combined_empirical_95pct_width"]
    result = {"rows": rows, "D_width": float(dwidth), "pass_rounded_values": all(r["abs_error_vs_manuscript_rounded"] < 5e-7 for r in rows)}
    OUT.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
