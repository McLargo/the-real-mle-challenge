from pathlib import Path

import pytest
from utils import CSVDataSaver


def test_csv_data_saver(df) -> None:
    saver = CSVDataSaver(
        output_filename="test.csv",
    )
    saver.save_data(df)

    output_file = Path("test.csv")
    assert output_file.exists()
    assert output_file.is_file()
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
