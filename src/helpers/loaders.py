from abc import ABC, abstractmethod
from pathlib import Path

import pandas as pd


class DataLoader(ABC):
    """
    Generic class for loading data.
    """

    @abstractmethod
    def load_data(self) -> pd.DataFrame:
        """
        Load the data and returns it as a DataFrame.
        Other classes should implement this method.

        Returns:
            pd.DataFrame: The loaded data.
        """
        pass


class CSVDataLoader(DataLoader):
    """
    Class for loading data from a CSV file.
    """

    def __init__(self, input_filename: str, dropna: bool = False, *args, **kwargs) -> None:
        """
        Initializes the CSVDataLoader class.
        Sets the input file path for the data in CSV file.
        Args:
            input_filename (str): The path to the input file.
            dropna (bool): If True, drop rows with NaN values.
                Defaults to False.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.
        """

        self.input_filename = Path(input_filename)
        self.dropna = dropna

    def load_data(self) -> pd.DataFrame:
        """
        Loads the data from a CSV file and stores it in a DataFrame.

        Returns:
            pd.DataFrame: The loaded data.

        Raises:
            ValueError: If the file is not a CSV file.
            FileNotFoundError: If the file is not found.
        """

        if self.input_filename.suffix != ".csv":
            raise ValueError(f"File {self.input_filename} is not a CSV file")

        if not self.input_filename.exists():
            raise FileNotFoundError(f"File {self.input_filename} not found")

        data =  pd.read_csv(self.input_filename, dtype=str)
        if self.dropna:
            return data.dropna(axis=0)
        return data
