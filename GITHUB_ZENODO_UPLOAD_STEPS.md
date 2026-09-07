# GitHub / Zenodo upload steps for R6R1

## Recommended path

1. Keep this bundle private/anonymized during double-blind review unless the conference explicitly permits a public named repository.
2. After acceptance or after confirming the venue policy, create a GitHub repository. Suggested repository name: `pv-ffls-digital-twin-admission`.
3. Upload the contents of this directory as the repository root, not as a nested ZIP.
4. Add final author names, affiliations, ORCID identifiers, and accepted-paper citation when allowed.
5. Replace `LICENSE_PENDING.txt` with an approved license file. Do not assume public-domain/open-source status before institutional approval.
6. Check that no raw SWaT spreadsheet or controlled iTrust file is present. Only hashes, aggregate derived metrics, code, and figures should be included.
7. Create a tagged GitHub release, for example `v1.0.0-r6r1`.
8. Enable GitHub archiving in Zenodo or manually upload the repository ZIP to Zenodo.
9. After Zenodo creates the record DOI, add the DOI badge and citation to `README.md`, update `.zenodo.json` if needed, and preserve the released ZIP/manifest.

## If a DOI is needed before a GitHub release

Use a manual Zenodo upload rather than GitHub integration. Update the metadata in `.zenodo.json`, reserve or publish the DOI according to the Zenodo workflow, then add the DOI to the manuscript Data Availability statement only when the record is stable and policy-compliant.

## What not to upload

- Raw SWaT July 2019 spreadsheet or any redistributed controlled iTrust data.
- Non-anonymized author metadata before double-blind review if the conference forbids it.
- A public license until author/institution approval is obtained.
- Draft reviewer comments or internal ChatGPT development logs.
