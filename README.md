# Closure-Preserving Fuzzy Data Admission for AI-Ready PV Digital Twins

This repository supports the paper:

**Closure-Preserving Fuzzy Data Admission for AI-Ready PV Digital Twins**

Current manuscript package: **PV_FFLS_DT_R6R15_AuthorGitHub**.

## Data and code availability

The reproducibility archive, derived data tables, alpha-cut certificates, and scripts are publicly available in the project GitHub repository.

## Included materials

The repository/package is intended to provide:

- manuscript PDFs and LaTeX source;
- derived PV daily/reproducibility tables;
- closure-preserving alpha-cut certificate outputs;
- retained mechanism-audit replicate summaries;
- reproduction scripts;
- paper figures;
- source-boundary notes.

## Important data boundary

Raw SWaT historian data are **not** redistributed. Researchers who want to reproduce any SWaT-related source-boundary check must obtain their own authorized copy directly from iTrust, Centre for Research in Cyber Security, Singapore University of Technology and Design.

## Claim boundary

This repository supports a PV digital-twin data-admission layer. It does not claim a complete digital twin, AI benchmark, cyberattack detector, fault classifier, controller, or external numerical validation of the PV fuzzy/FFLS model from SWaT.

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
```

The expected checks reproduce the PV center state, the closure-preserving alpha-cut certificate, and the mechanism-width summaries from the included derived tables.
