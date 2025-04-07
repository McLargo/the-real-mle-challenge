import pandas as pd
import pytest


@pytest.fixture
def df():
    data = {
        "column1": [1, 2, 3],
        "column2": ["A", "B", "C"],
        "column3": [4.5, 5.5, 6.5],
    }
    return pd.DataFrame(data)
