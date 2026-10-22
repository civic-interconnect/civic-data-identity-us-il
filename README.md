# civic-data-identity-us-il

[![PyPI](https://img.shields.io/pypi/v/civic-data-identity-us-il.svg)](https://pypi.org/project/civic-data-identity-us-il/)
[![Docs Site](https://img.shields.io/badge/docs-site-blue?logo=github)](https://civic-interconnect.github.io/civic-data-identity-us-il/)
[![Repo](https://img.shields.io/badge/repo-GitHub-black?logo=github)](https://github.com/civic-interconnect/civic-data-identity-us-il)
[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](./LICENSE)

[![CI](https://github.com/civic-interconnect/civic-data-identity-us-il/actions/workflows/ci-python-zensical.yml/badge.svg?branch=main)](https://github.com/civic-interconnect/civic-data-identity-us-il/actions/workflows/ci-python-zensical.yml)
[![Docs-Deploy](https://github.com/civic-interconnect/civic-data-identity-us-il/actions/workflows/deploy-zensical.yml/badge.svg?branch=main)](https://github.com/civic-interconnect/civic-data-identity-us-il/actions/workflows/deploy-zensical.yml)
[![Pre-Release](https://github.com/civic-interconnect/civic-data-identity-us-il/actions/workflows/pre-release.yml/badge.svg?branch=main)](https://github.com/civic-interconnect/civic-data-identity-us-il/actions/workflows/pre-release.yml)
[![Release](https://github.com/civic-interconnect/civic-data-identity-us-il/actions/workflows/release-pypi.yml/badge.svg)](https://github.com/civic-interconnect/civic-data-identity-us-il/actions/workflows/release-pypi.yml)
[![Links](https://github.com/civic-interconnect/civic-data-identity-us-il/actions/workflows/links.yml/badge.svg?branch=main)](https://github.com/civic-interconnect/civic-data-identity-us-il/actions/workflows/links.yml)
[![Dependabot](https://img.shields.io/badge/Dependabot-enabled-brightgreen.svg)](https://github.com/civic-interconnect/civic-data-identity-us-il/security)

This repository hosts **raw and processed Illinois datasets**
used for testing normalization, deterministic identifier generation, and
candidate record consolidation in the
[Civic Interconnect](https://github.com/civic-interconnect/civic-interconnect)
project.

The primary dataset is the **City of Chicago Contracts Dataset**, which provides
182,000+ procurement records suitable for testing:

- Vendor-name normalization across capitalization, punctuation, and abbreviations.
- Deterministic identifier generation from canonicalized inputs.
- Procurement adapter behavior with real-world source data.
- Candidate record grouping and normalization collision detection.
- Reproducible data extraction and provenance documentation.

This repository contains both the full raw dataset and curated subsets
designed as identity test fixtures.

## Repository Organization

### data/raw/

Unmodified raw datasets retrieved directly from official public sources.
Contains large files (up to ~50 MB).
These files are **not** stored in the main Civic Interconnect repo to avoid
repository bloat.

### data/identity/

Curated, size-limited datasets (~5k–20k rows) used for:

- testing consistency of generated identifiers for equivalent canonical inputs
- evaluating string normalization
- testing adapters against realistic naming variations

These subsets are suitable for inclusion as examples in the main CEP spec repo.

### docs/provenance/

Contains PROV-YAML metadata files describing dataset lineage, publishers, and
retrieval activities. These files follow **W3C PROV-DM** conventions.

### src/civic_data_identity_us_il/

Utility code for extracting and shaping subsets from raw data.
The provided Python tool generates deterministic vendor-name samples.

## Data Source

### City of Chicago – Contracts Dataset

- URL: https://data.cityofchicago.org/Administration-Finance/Contracts/rsxa-ify5
- Publisher: City of Chicago
- License: Public Domain
- Fields include procurement descriptions, award amounts, departments, vendor
  names, addresses, and contract timeline fields.
- Used to test:
  - identity resolution
  - canonicalization
  - adapters for procurement verticals

Full provenance is provided in
[`docs/provenance/chicago_contracts.prov.yaml`](docs/provenance/chicago_contracts.prov.yaml).

## Relationship to `civic-interconnect`

This repository serves as a data companion to the main specification and
implementation in:

https://github.com/civic-interconnect/civic-interconnect

Only smaller derived files (e.g., 5k–20k row identity samples) are copied into
the main repository under `examples/identity/`.

The separation keeps CEP maintainable and free of large artifacts
while preserving full reproducibility.

## Changelog

[CHANGELOG.md](./CHANGELOG.md)

## Citation

If you use this repository, please cite **both**:

1. [CITATION.cff](CITATION.cff)
2. The original City of Chicago dataset (included in references)

## Documentation

[Documentation Site](https://civic-interconnect.github.io/civic-data-identity-us-il/)

## License

Raw public datasets retain their original license (Public Domain for Chicago
Open Data).

All derived outputs, scripts, and documentation in this repository are licensed
under the [MIT Licence](./LICENSE) unless otherwise noted.
