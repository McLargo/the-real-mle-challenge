from abc import ABC, abstractmethod
from pathlib import Path

import pandas as pd


class DataSaver(ABC):
    """
    Generic class for saving data.
    """

    @abstractmethod
    def save_data(self, data: pd.DataFrame) -> None:
        """
        Save the cleaned data.
        Other classes should implement this method.

        Args:
            data (pd.DataFrame): The cleaned data.

        """
        pass


class CSVDataSaver(DataSaver):
    """
    Class for saving data to a CSV file.
    """

    def __init__(self, output_filename: str, *args, **kwargs) -> None:
        """
        Initializes the CSVDataSaver class.
        Sets the output file to store the processed data.

        Args:
            output_filename (str): The name of the output file.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.
        """

        self.output_filename = Path(output_filename)

    def save_data(self, data: pd.DataFrame) -> None:
        """
        Saves the cleaned data to a CSV file.

        Args:
            data (pd.DataFrame): The cleaned data.

        Raises:
            ValueError: If the file is not a CSV file.
        """

        if self.output_filename.suffix != ".csv":
            raise ValueError(f"File {self.output_filename} is not a CSV file")

        data.to_csv(self.output_filename)
