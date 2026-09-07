#!/usr/bin/env python3
"""Reproduce the closure-preserving alpha-cut endpoint certificate.

Run from the repository root:
    python scripts/reproduce_alpha_certificate.py
"""
from itertools import product
from pathlib import Path
import json
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
PARAMS = ROOT / "derived_results" / "closure" / "DEPENDENT_FUZZY_PARAMETERS.csv"
OUT = ROOT / "derived_results" / "closure" / "alpha_certificate_reproduction_check.json"
EXPECTED = {
    "x1_L": 0.923811712136270,
    "x1_U": 0.955432206914232,
    "x2_L": 0.963844112653004,
    "x2_U": 0.990058439312868,
    "center_x1": 0.942882447973436,
    "center_x2": 0.974760759988893,
}
TOL = 5e-12

def alpha_interval(row, alpha: float) -> tuple[float, float]:
    lower = row["center_alpha1"] - (1.0 - alpha) * row["left_spread"]
    upper = row["center_alpha1"] + (1.0 - alpha) * row["right_spread"]
    return float(lower), float(upper)

def solve_one(p1: float, p2: float, b1: float, b2: float) -> tuple[float, float]:
    den = p1 - p2
    x1 = ((1.0 - p2) * b1 - (1.0 - p1) * b2) / den
    x2 = (p1 * b2 - p2 * b1) / den
    return float(x1), float(x2)

def extrema(alpha: float, params: pd.DataFrame) -> dict:
    vals = {}
    for _, row in params.iterrows():
        vals[row["latent_variable"]] = alpha_interval(row, alpha)
    xs = [solve_one(p1, p2, b1, b2) for p1, p2, b1, b2 in product(vals["p1"], vals["p2"], vals["b1"], vals["b2"])]
    x1 = [v[0] for v in xs]
    x2 = [v[1] for v in xs]
    return {"alpha": alpha, "x1_L": min(x1), "x1_U": max(x1), "x2_L": min(x2), "x2_U": max(x2)}

def main() -> None:
    params = pd.read_csv(PARAMS)
    a0 = extrema(0.0, params)
    a1 = extrema(1.0, params)
    result = {
        "alpha0": a0,
        "alpha1": a1,
        "minimum_lower_endpoint": min(a0["x1_L"], a0["x2_L"]),
        "max_abs_error_alpha0_vs_manuscript": max(abs(a0[k] - EXPECTED[k]) for k in ["x1_L", "x1_U", "x2_L", "x2_U"]),
        "max_abs_error_center_vs_manuscript": max(abs(a1["x1_L"] - EXPECTED["center_x1"]), abs(a1["x2_L"] - EXPECTED["center_x2"])),
    }
    result["pass"] = result["max_abs_error_alpha0_vs_manuscript"] <= TOL and result["max_abs_error_center_vs_manuscript"] <= TOL
    OUT.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
