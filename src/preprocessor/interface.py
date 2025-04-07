from abc import ABC, abstractmethod

import pandas as pd


class DataPreprocessor(ABC):
    """
    Generic class for preprocessing data from files.
    """

    @abstractmethod
    def clean_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Cleans the data.
        Other classes should implement this method.

        Args:
            data (pd.DataFrame): The data to be preprocessed.

        Returns:
            pd.DataFrame: The cleaned data.
        """
        pass
