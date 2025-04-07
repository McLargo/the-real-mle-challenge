from pathlib import Path

import pytest

from helpers.savers import CSVDataSaver


def test_csv_data_saver(df) -> None:
    output_filename = "test.csv"
    # Assert no file exists before saving
    output_file = Path(output_filename)
    assert output_file.exists() is False

    # Save the DataFrame to a CSV file
    saver = CSVDataSaver(
        output_filename=output_filename,
    )
    saver.save_data(df)

    # Assert the file exists after saving
    assert output_file.exists()
    assert output_file.is_file()

    # clean up the created file after the test
    output_file.unlink()
    assert output_file.exists() is False


def test_csv_data_saver_invalid_file_type(df) -> None:
    saver = CSVDataSaver(
        output_filename="test.txt",
    )
    with pytest.raises(ValueError):
        saver.save_data(df)


def test_csv_data_saver_invalid_file_path(df) -> None:
    saver = CSVDataSaver(
        output_filename="invalid_path/test.csv",
    )
    with pytest.raises(OSError):
        saver.save_data(df)
