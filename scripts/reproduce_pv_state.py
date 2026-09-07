#!/usr/bin/env python3
"""Reproduce the PV two-row state construction reported in the R6 manuscript.

Run from the repository root:
    python scripts/reproduce_pv_state.py
"""
from pathlib import Path
import json
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "derived_results" / "pv" / "PVDAQ2107_processed_daily_paired_pr.csv"
OUT = ROOT / "derived_results" / "pv" / "pv_state_reproduction_check.json"

EXPECTED_A = np.array([[0.5829181333, 0.4170818667], [0.3413565221, 0.6586434779]])
EXPECTED_B = np.array([0.9561783139, 0.9638788903])
EXPECTED_X = np.array([0.9428824480, 0.9747607600])
TOL = 5e-9

def main() -> None:
    df = pd.read_csv(DATA)
    construction = df[df["year"].between(2018, 2022)].copy()
    tau = float(construction["inverter_pr"].median())
    blocks = [("row1_2018_2020", [2018, 2019, 2020]), ("row2_2021_2022", [2021, 2022])]
    rows = []
    for name, years in blocks:
        d = construction[construction["year"].isin(years)].copy()
        denom = d["inverter_ac_energy_kwh"].sum()
        low = d[d["inverter_pr"] <= tau]["inverter_ac_energy_kwh"].sum()
        a1 = float(low / denom)
        a2 = float(1.0 - a1)
        b = float(d["meter_ac_energy_kwh"].sum() / denom)
        rows.append({"block": name, "years": years, "n_days": int(len(d)), "A_r1": a1, "A_r2": a2, "b_r": b})
    A = np.array([[r["A_r1"], r["A_r2"]] for r in rows])
    b = np.array([r["b_r"] for r in rows])
    x = np.linalg.solve(A, b)
    result = {
        "rows_total": int(len(df)),
        "construction_rows_2018_2022": int(len(construction)),
        "tau_median_inverter_pr": tau,
        "row_definitions": rows,
        "A": A.tolist(),
        "b": b.tolist(),
        "x": x.tolist(),
        "max_abs_A_error_vs_manuscript": float(np.max(np.abs(A - EXPECTED_A))),
        "max_abs_b_error_vs_manuscript": float(np.max(np.abs(b - EXPECTED_B))),
        "max_abs_x_error_vs_manuscript": float(np.max(np.abs(x - EXPECTED_X))),
        "pass": bool(np.max(np.abs(A - EXPECTED_A)) <= TOL and np.max(np.abs(b - EXPECTED_B)) <= TOL and np.max(np.abs(x - EXPECTED_X)) <= TOL),
    }
    OUT.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
