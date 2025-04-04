from pathlib import Path

import pytest
from pandas import DataFrame
from utils import CSVDataLoader


def test_csv_data_loader() -> None:
    dir = Path.cwd()
    input_filename = Path.joinpath(dir, "tests", "data", "raw.csv")
    loader = CSVDataLoader(input_filename=input_filename.__str__())
    data = loader.load_data()
    assert data is not None
    assert isinstance(data, DataFrame)
    assert len(data) > 0


def test_csv_data_loader_not_found() -> None:
    loader = CSVDataLoader(input_filename="test.csv")
    with pytest.raises(FileNotFoundError, match="File test.csv not found"):
        loader.load_data()


def test_csv_data_loader_not_csv() -> None:
    loader = CSVDataLoader(input_filename="test.txt")
    with pytest.raises(ValueError, match="File test.txt is not a CSV file"):
        loader.load_data()
