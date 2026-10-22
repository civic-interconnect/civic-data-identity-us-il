# Changelog

All notable changes to this project will be documented in this file.

The format follows **[Keep a Changelog](https://keepachangelog.com/en/1.1.0/)**
and this project adheres to **[Semantic Versioning](https://semver.org/spec/v2.0.0.html)**.

---

## [Unreleased]

---

## [0.1.2] - 2026-10-22

### Updated

- Updated development tooling using `uvx pup-up`
- Updated README.md, CITATION.cff, pyproject.toml, and docs/index.md
- Clarified that normalized identifiers support candidate record matching
  but do not independently establish real-world entity identity.
- Corrected project documentation to distinguish normalization,
  identifier generation, and candidate grouping from identity validation.

---

## [0.1.1] - 2025-12-11

### Minor

- Update CITATION.cff

---

## [0.1.0] - 2025-12-11

### Added

- Initial release of the Chicago identity dataset package.
- Raw Chicago contracts CSV (2025-12-11 snapshot).
- Processed vendor-name identity sample (20k rows).
- Manifest and index metadata under `data-out/`.
- Sample-generation script (`make_chicago_identity_sample.py`).
- PROV and citation metadata.
- Documentation and project scaffolding.

---

## Notes on versioning and releases

- We use **SemVer**:
  - **MAJOR** - breaking changes
  - **MINOR** - backward-compatible changes
  - **PATCH** - fixes, documentation, tooling
- Versions are driven by git tags.
- Tag `vX.Y.Z` to release.

## Release Procedure (Required)

Follow these steps exactly when creating a new release.

### Task 1. Update release metadata (manual edits)

1.1. CITATION.cff: update version and date-released
1.2. CHANGELOG.md: add section, move unreleased entries, update links

### Task 2. Validate

From PowerShell at the repository root:

```pwsh
# set up or update Python environment
.\sit.ps1

# Update GitHub Actions and pin all action references to immutable SHAs.
uvx gha-tools autoupdate --pin=all --write .github/workflows

# Audit the resulting GitHub configuration for security findings.
uvx zizmor@latest .github/
# one informational notice is okay

# Validate.
uvx cffconvert --validate

uv build
uvx twine check dist/*
```

When Python version changes, validate as follows:

```shell
# Verify the Python tests under Python 3.14.
uv run --python 3.14 python -m pytest

# Generate a separate sample using Python 3.14.
uv run --python 3.14 python src/civic_data_identity_us_il/make_chicago_identity_sample.py --input data/raw/chicago_contracts_2025-12-11.csv --output .verify-py314/chicago_sample.csv --n-rows 20000

# Verify that the generated sample is the first 20,000 source records.
uv run --python 3.14 python -c 'import pandas as pd; from pandas.testing import assert_frame_equal; source = pd.read_csv("data/raw/chicago_contracts_2025-12-11.csv", dtype=str, low_memory=False); sample = pd.read_csv(".verify-py314/chicago_sample.csv", dtype=str, low_memory=False); assert_frame_equal(source.head(20000), sample); print("Sample verification passed")'

# Remove the temporary verification output.
Remove-Item .verify-py314 -Recurse -Force

# Check what changed before committing.
git status --short
```

### Task 3. Commit, push, and tag

```shell
git add -A
git commit -m "Prepare X.Y.Z"
git push -u origin main
```

Verify actions run on GitHub. After success:

```shell
git tag vX.Y.Z -m "X.Y.Z"
git push origin vX.Y.Z
```

## Links

[Unreleased]: https://github.com/civic-interconnect/civic-data-identity-us-il/compare/v0.1.2...HEAD
[0.1.2]: https://github.com/civic-interconnect/civic-data-identity-us-il/tag/v0.1.2
[0.1.1]: https://github.com/civic-interconnect/civic-data-identity-us-il/tag/v0.1.1
[0.1.0]: https://github.com/civic-interconnect/civic-data-identity-us-il/releases/tag/v0.1.0
