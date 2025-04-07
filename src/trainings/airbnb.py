from typing import Any

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from helpers.loaders import CSVDataLoader
from helpers.model_generation import PickleModelGeneration
from trainings.interface import Training


class AirbnbTraining(CSVDataLoader, PickleModelGeneration, Training):
    """
    Class for training a model using Airbnb data.
    """

    def __init__(self, input_filename: str, output_filename: str) -> None:
        """
        Initializes the AirbnbTraining class.

        Args:
            input_filename (str): The name of the input CSV file.
            output_filename (str): The name of the output pickle file.
        """
        CSVDataLoader.__init__(self, input_filename, dropna=True)
        PickleModelGeneration.__init__(self, output_filename)

        self.room_type = {
            "Shared room": 1,
            "Private room": 2,
            "Entire home/apt": 3,
            "Hotel room": 4,
        }
        self.neighbourhood = {
            "Bronx": 1,
            "Queens": 2,
            "Staten Island": 3,
            "Brooklyn": 4,
            "Manhattan": 5,
        }
        self.features = [
            "neighbourhood",
            "room_type",
            "accommodates",
            "bathrooms",
            "bedrooms",
        ]

        self.classifier = None

    def train(self, data: pd.DataFrame) -> Any:
        self.data = data

        self.map_room_type()
        self.map_neighbourhood()

        return self.split_and_train_random_forest_classifier()

    def map_room_type(self):
        """
        Maps the room type to an integer.
        """
        self.data["room_type"] = self.data["room_type"].map(self.room_type)

    def map_neighbourhood(self):
        """
        Maps the neighbourhood to an integer.
        """
        self.data["neighbourhood"] = self.data["neighbourhood"].map(
            self.neighbourhood,
        )

    def split_and_train_random_forest_classifier(
        self,
    ) -> RandomForestClassifier:
        """
        Splits the data into training and testing sets and trains
        a Random Forest classifier.
        """
        features = self.data[self.features]
        categories = self.data["category"]

        x_train, x_test, y_train, y_test = train_test_split(
            features,
            categories,
            test_size=0.15,
            random_state=1,
        )

        classifier = RandomForestClassifier(
            n_estimators=500,
            random_state=0,
            class_weight="balanced",
            n_jobs=4,
        )
        classifier.fit(x_train, y_train)

        return classifier
