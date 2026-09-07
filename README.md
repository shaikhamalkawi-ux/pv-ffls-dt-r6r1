# PV FFLS Digital-Twin Data-Admission Repository Materials (R6R1)

This repository bundle accompanies the double-blind conference manuscript:

**Physically Invalid Uncertainty from Valid PV Channels: Closure-Preserving Fuzzy Data Admission for Digital Twins**


## Upload status

This is the **R6R1 GitHub/Zenodo upload-ready repository bundle (2026-09-07 checked copy)**. It is prepared for either: (i) a private/anonymized review-support archive during double-blind review, or (ii) a public post-acceptance repository after author/institution approval.

Do **not** publish a named repository before checking the target venue's double-blind policy. Add final author names, affiliations, ORCID identifiers, accepted-paper citation, DOI, and an approved license only when appropriate.

## Scientific scope

R6R1 is a notation-closure cleanup of R6. It adds spread-scaling definitions, the explicit width functional, support-function definition, SWaT notation definitions, and derivative closure in the Supplement. It does **not** change any scientific result, dataset, model structure, title, conclusion, or claim boundary.

Locked manuscript results include:

- PV paired days: `2447`
- Width distortion: `D_width = 9.2409066`
- Independent-marginal admissible area: `1.8365%`
- Active boundary: `lambda_A,max = 0.036729764`
- Maximum row-closure error: `0.1713120512`
- Shared-latent alpha-cut certificate: positive over full support
- SWaT structural pilot: `R^2 = 0.9846948322` over 133 complete attack-free 60-s windows

The SWaT result is a bounded structural-admission/state-consistency demonstration. It is **not** a cyberattack detector and does **not** externally validate the PV fuzzy/FFLS alpha-cut model.

## Directory structure

```text
paper/                         Final R6R1 PDFs
manuscript_source/             LaTeX sources for main and supplement
figures/                       Publication figures used by the paper
derived_results/pv/            PV derived reproducibility tables and checks
derived_results/closure/       Closure-preserving fuzzy alpha-cut outputs
derived_results/swat/          SWaT aggregate outputs only; no raw data
environment/                   Python requirements and environment notes
scripts/                       Reproduction scripts for derived checks
evidence/                      Source-boundary notes
```

## Reproduction

Install dependencies:

```bash
python -m pip install -r environment/requirements.txt
```

Run checks:

```bash
python scripts/reproduce_pv_state.py
python scripts/reproduce_alpha_certificate.py
python scripts/reproduce_mechanism_widths.py
python scripts/summarize_swat_metrics.py
```

Expected checks include exact or tolerance-controlled reproduction of the center state, alpha-cut certificate, mechanism-width ratio, and SWaT aggregate metrics.

## Data availability boundaries

The PV derived daily table and derived result files are included. The package does not redistribute raw SWaT historian data. Reproducing the SWaT component from raw data requires an independently authorized copy from iTrust, Centre for Research in Cyber Security, Singapore University of Technology and Design.

See `DATA_AVAILABILITY_AND_BOUNDARIES.md` and `NO_RAW_SWAT_DATA_NOTICE.txt`.

## Citation and Zenodo metadata

The repository includes:

- `CITATION.cff`
- `.zenodo.json`
- `RELEASE_NOTES_R6R1.md`
- `MANIFEST_SHA256.txt`

Before public release, update author metadata, license, accepted-paper citation, and DOI according to the final venue policy.
