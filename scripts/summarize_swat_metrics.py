#!/usr/bin/env python3
"""Print the SWaT aggregate structural-pilot metrics included in the repository.

Raw SWaT data are controlled by iTrust and are not redistributed in this repository.
This script summarizes the derived aggregate outputs only.
"""
from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "derived_results" / "swat" / "SWAT_NORMAL_AGGREGATE_METRICS.csv"
OUT = ROOT / "derived_results" / "swat" / "swat_metric_summary_check.json"

def main() -> None:
    row = pd.read_csv(DATA).iloc[0].to_dict()
    result = {
        "normal_complete_60s_windows": int(row["n_complete_60s_windows"]),
        "fixed_external_coefficient": float(row["fixed_coefficient"]),
        "normal_R2": float(row["R2_about_observed_mean"]),
        "median_absolute_residual": float(row["median_absolute_residual_level_units_per_s"]),
        "mean_absolute_residual": float(row["mean_absolute_residual_level_units_per_s"]),
        "normal_95th_percentile_abs_residual": float(row["absolute_residual_q95"]),
        "claim_boundary": "Structural-admission/state-consistency residual only; not attack detection or PV-model external validation.",
        "raw_swat_included": False,
    }
    OUT.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
