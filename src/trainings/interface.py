from abc import ABC, abstractmethod
from typing import Any

from pandas import DataFrame


class Training(ABC):
    """
    Generic class for training a model.
    """

    @abstractmethod
    def train(self, data: DataFrame) -> Any:
        """
        Trains the model.
        Other classes should implement this method.
        Args:
            data (pd.DataFrame): The data to be used for training.
        """
        pass
