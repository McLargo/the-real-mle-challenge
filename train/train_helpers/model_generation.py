from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

import joblib


class ModelGeneration(ABC):
    """
    Generic class for training a model.
    """

    @abstractmethod
    def store_model(self, model: object) -> None:
        """
        Stores the model.
        Other classes should implement this method.

        Args:
            model (object): The model to be stored.
        """
        pass


class PickleModelGeneration(ModelGeneration):
    """
    Class for storing a model using pickle.
    """

    def __init__(self, output_filename: str, *args, **kwargs) -> None:
        """
        Initializes the PickleModelGeneration class.
        Sets the output file to store the model.
        Args:
            output_filename (str): The name of the output file.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.
        """

        self.output_filename = Path(output_filename)

    def store_model(self, model: Any) -> None:
        """
        Stores the model using pickle.

        Args:
            model (object): The model to be stored.
        """
        if self.output_filename.suffix != ".pkl":
            raise ValueError(
                f"File {self.output_filename} is not a pickle file",
            )

        with open(self.output_filename, "wb") as f:
            joblib.dump(model, f)
