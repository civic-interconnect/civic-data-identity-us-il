# Illinois Identity Dataset (Chicago Contracts)

This repository provides raw and sampled data from the
City of Chicago Contracts dataset for use in
[Civic Interconnect](https://github.com/civic-interconnect/civic-interconnect).

Its purpose is to support testing of vendor-name normalization,
deterministic SNFEI identifier generation,
procurement adapters, and candidate record grouping.

The data and metadata allow users to:

- Reproduce a sample from a fixed snapshot of a public dataset.
- Evaluate the consistency of legal-name normalization.
- Examine changes in candidate record grouping.
- Test procurement adapters against real-world source data.
- Inspect source provenance and dataset metadata.

**Scope:** Matching normalized names or generated identifiers
identifies candidate record matches.
It does not establish that the records refer to the same real-world vendor.
Such a conclusion requires independently justified entity-identity criteria
and supporting evidence.

## Repository Contents

```text
data/
  raw/
    chicago_contracts_2025-12-11.csv
  identity/
    chicago_contracts_vendors_sample_20k.csv

data-out/
  index.json
  manifest.json

docs/
  provenance/
    chicago_contracts.prov.yaml

src/
  civic_data_identity_us_il/
    make_chicago_identity_sample.py
```

The repository includes:

- **Raw data:** A snapshot of the Chicago Contracts dataset.
- **Sample data:** A reproducible subset of procurement records.
- **Dataset metadata:** An index and manifest describing
  the dataset and its provenance.
- **Source provenance:** A PROV-style record of the
  source dataset and retrieval activity.
- **Python utility:** A script for selecting and exporting sample records.

The data can be used for normalization tests,
identifier-generation experiments,
adapter development, and analysis of candidate record matches.

## Why Chicago Contracts?

The Chicago Contracts dataset contains numerous procurement records with:

- Repeated vendor-name entries.
- Variations in capitalization, punctuation, abbreviations, and corporate suffixes.
- Misspellings and other data-entry inconsistencies.
- Attributes such as departments, contract amounts, dates, and vendor information.

These characteristics make the dataset useful for testing:

- Organization-name normalization.
- Deterministic identifier generation.
- Candidate grouping under declared normalization rules.
- Detection of normalization collisions.
- Procurement adapter behavior.

A normalization collision occurs when distinct raw names
produce the same normalized value.
Such a collision does not necessarily represent either a correct entity match or an incorrect merge.

## How the 20k Identity Sample Was Generated

The sample-generation script is:

`src/civic_data_identity_us_il/make_chicago_identity_sample.py`

From the repository root, run:

```powershell
uv run python src/civic_data_identity_us_il/make_chicago_identity_sample.py
```

By default, the script:

1. Finds the latest matching Chicago contracts CSV in `data/raw/`.
2. Reads the source CSV.
3. Selects the first 20,000 rows, or all available rows if fewer exist.
4. Preserves the selected records and their columns without normalization or deduplication.
5. Writes the sample to `data/identity/chicago_contracts_vendors_sample_20k.csv`.

The script also supports explicit input and output paths,
a different row count, and an `--overwrite` option.

For example:

```powershell
uv run python src/civic_data_identity_us_il/make_chicago_identity_sample.py --n-rows 5000 --overwrite
```

Given the same input, row count, and configuration,
the selection procedure is deterministic.

The script generates the CSV sample only.
The dataset index, manifest, and provenance records are maintained separately.

## Provenance & Reproducibility

The repository provides metadata for identifying
the original data source and documenting the dataset snapshot.

### Dataset Manifest

`data-out/manifest.json`

The manifest records:

- The dataset identifier and version.
- The source dataset and publisher.
- Source and output path declarations.
- Generator information.
- A recorded creation timestamp.

These are metadata declarations. The sample-generation script does not automatically update the manifest.

### Dataset Index

`data-out/index.json`

The index describes the registered dataset sample,
including its title, intended purpose, record count, and citation information.

### Source Provenance

`docs/provenance/chicago_contracts.prov.yaml`

The PROV-style metadata identifies:

- The City of Chicago Contracts dataset.
- The City of Chicago as the source publisher.
- A recorded retrieval activity.
- The source dataset used by that activity.

This record describes source provenance.
It does not independently establish the identities of
vendors in the dataset or document every operation used to produce the sample.

## Citation

If you use the dataset in research, software, testing, or documentation,
cite both the original publisher and this repository.

Original data source:

City of Chicago. _Contracts Dataset._
https://data.cityofchicago.org/Administration-Finance/Contracts/rsxa-ify5

Repository:

Civic Interconnect. _civic-data-identity-us-il_. Version 0.1.2.
https://github.com/civic-interconnect/civic-data-identity-us-il

Machine-readable citation and dataset metadata are available in:

- `CITATION.cff`
- `data-out/index.json`

## Relationship to Civic Interconnect

This repository is a companion dataset for
[Civic Interconnect](https://github.com/civic-interconnect/civic-interconnect).
It is not part of the Civic Exchange Protocol (CEP) specification itself.

It supports:

- SNFEI implementation testing.
- Procurement adapter testing.
- Legal-name normalization experiments.
- Candidate record matching and collision analysis.
- Reproducible examples for CEP documentation.

The dataset and its sample-generation utility do not constitute
an independent validation of a general theory of entity identity.

## Contributing

Contributions welcome, including:

- Additional source datasets and test cases.
- Domain-specific normalization tests.
- Improvements to the sample-generation script.
- Corrections to source metadata and provenance.
- Documentation improvements.

Please open an issue or pull request in the
[GitHub repository](https://github.com/civic-interconnect/civic-data-identity-us-il).

## License: Upstream Data

The original Chicago Contracts dataset is published through the
[Chicago Open Data Portal](https://data.cityofchicago.org/Administration-Finance/Contracts/rsxa-ify5).

The source dataset is described as public-domain data in the repository metadata.
Its reuse remains subject to the applicable terms of the original publisher.

## License: This Repository

The code and original project documentation in `civic-data-identity-us-il`
are released under the
[MIT License](https://github.com/civic-interconnect/civic-data-identity-us-il/blob/main/LICENSE).

The MIT License permits reuse, modification, and redistribution subject to its terms.
It does not replace or override the rights and conditions governing the original City of Chicago data.
