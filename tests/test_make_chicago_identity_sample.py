# tests/test_make_chicago_identity_sample.py

from pathlib import Path

import pandas as pd

from civic_data_identity_us_il.make_chicago_identity_sample import main


def test_make_sample_creates_expected_rows(tmp_path: Path) -> None:
    """Basic sanity check: script writes a CSV with the requested number of rows."""

    # Arrange: build a small input CSV in a temp directory
    input_path = tmp_path / "chicago_contracts_test.csv"
    output_path = tmp_path / "chicago_sample.csv"

    # Minimal columns; script keeps all columns as-is
    df_in = pd.DataFrame(
        {
            "Vendor Name": ["A", "B", "C", "D"],
            "Department": ["X", "Y", "Z", "W"],
            "Award Amount": ["100", "200", "300", "400"],
        }
    )
    df_in.to_csv(input_path, index=False)

    # Act: request 2 rows, allow overwrite just in case
    argv = [
        "--input",
        str(input_path),
        "--output",
        str(output_path),
        "--n-rows",
        "2",
        "--overwrite",
    ]
    exit_code = main(argv)

    # Assert: script succeeded and wrote the expected rows
    assert exit_code == 0
    assert output_path.exists()

    df_out = pd.read_csv(output_path, dtype=str)
    assert len(df_out) == 2
    # Check that we preserved the first N rows in order
    assert list(df_out["Vendor Name"]) == ["A", "B"]
    assert list(df_out["Department"]) == ["X", "Y"]
    assert list(df_out["Award Amount"]) == ["100", "200"]


def test_make_sample_truncates_when_requested_more_than_available(tmp_path: Path) -> None:
    """Request more rows than exist and ensure it falls back to the available count."""

    input_path = tmp_path / "chicago_contracts_small.csv"
    output_path = tmp_path / "chicago_sample_small.csv"

    df_in = pd.DataFrame(
        {
            "Vendor Name": ["A", "B", "C"],
        }
    )
    df_in.to_csv(input_path, index=False)

    # Request 10 rows from a 3-row file
    argv = [
        "--input",
        str(input_path),
        "--output",
        str(output_path),
        "--n-rows",
        "10",
        "--overwrite",
    ]
    exit_code = main(argv)

    assert exit_code == 0
    assert output_path.exists()

    df_out = pd.read_csv(output_path, dtype=str)
    # We only have 3 rows available; sample should not invent more
    assert len(df_out) == 3
    assert list(df_out["Vendor Name"]) == ["A", "B", "C"]
