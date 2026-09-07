# GitHub Upload Status — R6R1

Repository: `shaikhamalkawi-ux/pv-ffls-dt-r6r1`

Status checked from the GitHub connector on 2026-09-07.

## Current status

The repository has been initialized and contains the lightweight reproducibility/control files that can be safely written through the connector:

- `README.md`
- `CITATION.cff`
- `.zenodo.json`
- `DATA_AVAILABILITY_AND_BOUNDARIES.md`
- `GITHUB_ZENODO_UPLOAD_STEPS.md`
- `LICENSE_PENDING.txt`
- `NO_RAW_SWAT_DATA_NOTICE.txt`
- `RELEASE_NOTES_R6R1.md`
- `environment/ENVIRONMENT_LOCK.txt`
- `environment/requirements.txt`
- `evidence/SOURCE_BOUNDARY_NOTES.md`
- `scripts/reproduce_alpha_certificate.py`
- `scripts/reproduce_mechanism_widths.py`
- `scripts/reproduce_pv_state.py`
- `scripts/summarize_swat_metrics.py`

## Not yet uploaded through the connector

The connector route used here does not reliably push the full ZIP payload or binary/large artifact directories. The following upload-ready package remains the authoritative complete bundle for manual upload or Zenodo deposit:

`PV_FFLS_DT_R6R1_GitHub_Zenodo_UploadReady_20260907.zip`

Expected complete bundle contents include:

- `paper/` PDFs
- `figures/` PNGs
- `manuscript_source/` LaTeX files
- `derived_results/pv/`
- `derived_results/closure/`
- `derived_results/swat/`
- `MANIFEST_SHA256.txt`

## Required manual completion step

To make GitHub fully complete, unzip the upload-ready package locally and drag/upload the remaining folders into this repository, or use GitHub Desktop / command-line `git push`.

Do not add raw SWaT historian data. Only aggregate SWaT outputs and source-boundary notes belong in this repository.
