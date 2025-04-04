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

    def __init__(self, input_file: str, *args, **kwargs) -> None:
        """
        Initializes the CSVDataLoader class.
        Sets the input file path in the raw data directory.
        Raises:
            FileNotFoundError: If the output path does not exist.
        """

        dir = Path.cwd().parent
        input_path = Path.joinpath(dir, "data", "raw")

        if not input_path.exists():
            raise FileNotFoundError(f"Directory {input_path} not found")

        self.input_filepath = Path.joinpath(input_path, input_file)

    def load_data(self) -> pd.DataFrame:
        """
        Loads the data from a CSV file and stores it in a DataFrame.

        Returns:
            pd.DataFrame: The loaded data.

        Raises:
            ValueError: If the file is not a CSV file.
            FileNotFoundError: If the file is not found.
        """

        if self.input_filepath.suffix != ".csv":
            raise ValueError(f"File {self.input_filepath} is not a CSV file")

        if not self.input_filepath.exists():
            raise FileNotFoundError(f"File {self.input_filepath} not found")

        return pd.read_csv(self.input_filepath, dtype=str)


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

    def __init__(self, output_file: str, *args, **kwargs) -> None:
        """
        Initializes the CSVDataSaver class.
        Sets the output path to the processed data directory.

        Raises:
            FileNotFoundError: If the output path does not exist.
        """

        dir = Path.cwd().parent
        output_path = Path.joinpath(dir, "data", "processed")

        if not output_path.exists():
            raise FileNotFoundError(f"Directory {output_path} not found")

        self.output_filepath = Path.joinpath(output_path, output_file)

    def save_data(self, data: pd.DataFrame) -> None:
        """
        Saves the cleaned data to a CSV file.

        Args:
            data (pd.DataFrame): The cleaned data.

        Raises:
            ValueError: If the file is not a CSV file.
        """

        if self.output_filepath.suffix != ".csv":
            raise ValueError(f"File {self.output_filepath} is not a CSV file")

        data.to_csv(self.output_filepath)


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
