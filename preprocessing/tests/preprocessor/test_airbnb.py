from pathlib import Path

from pandas import DataFrame
from preprocessor.airbnb import AirbnbDataPreprocessor


def test_airbnb_data_preprocessor():
    dir = Path.cwd()
    input_filename = Path.joinpath(dir, "tests", "data", "raw.csv")

    preprocessing = AirbnbDataPreprocessor(
        input_filename=input_filename.__str__(),
        output_filename="test.csv",
    )
    data_raw = preprocessing.load_data()
    data_cleaned = preprocessing.clean_data(data_raw)
    assert data_cleaned is not None
    assert isinstance(data_cleaned, DataFrame)
