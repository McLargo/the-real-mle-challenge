import numpy as np
import pandas as pd
from helpers.loaders import CSVDataLoader
from helpers.savers import CSVDataSaver

from .interface import DataPreprocessor


class AirbnbDataPreprocessor(CSVDataLoader, CSVDataSaver, DataPreprocessor):
    """
    Class for preprocessing Airbnb data.
    """

    def __init__(self, input_filename: str, output_filename: str):
        """
        Initializes the AirbnbDataPreprocessor class.

        Args:
            input_filename (str): The name of the input file.
            output_filename (str): The name of the output file.
        """

        CSVDataLoader.__init__(self, input_filename)
        CSVDataSaver.__init__(self, output_filename)

        # Custom attributes
        self.keep_columns = [
            "id",
            "neighbourhood_group_cleansed",
            "property_type",
            "room_type",
            "latitude",
            "longitude",
            "accommodates",
            "bathrooms",
            "bedrooms",
            "beds",
            "amenities",
            "price",
        ]
        self.remove_price_under = 10
        self.price_bins = [10, 90, 180, 400, np.inf]
        self.category_labels = [0, 1, 2, 3]

    def clean_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Cleans the data by removing unnecessary columns, renaming columns,
        and preprocessing the data.

        Args:
            data (pd.DataFrame): The data to be preprocessed.

        Returns:
            pd.DataFrame: The cleaned data.

        Raises:
            ValueError: If the data is not set.
        """
        if data is None:
            raise ValueError(
                "Data not set. Please set the data before cleaning.",
            )

        self.data_raw = data
        self.data_cleaned = None

        self.preprocess_bathrooms_column()
        self.preprocess_data_cleaned()
        self.preprocess_price_column()
        self.preprocess_category_column()
        self.preprocess_amenities_column()

        return self.data_cleaned

    def preprocess_bathrooms_column(self):
        """
        Preprocesses the bathrooms column by extracting
        the number of bathrooms from the text and removing the original column.
        """
        self.data_raw.drop(columns=["bathrooms"], inplace=True)
        self.data_raw["bathrooms"] = self.data_raw["bathrooms_text"].apply(
            self.num_bathroom_from_text,
        )

    @staticmethod
    def num_bathroom_from_text(text):
        """
        Extracts the number of bathrooms from the text."
        """
        try:
            if isinstance(text, str):
                bath_num = text.split(" ")[0]
                return float(bath_num)
            return np.nan
        except ValueError:
            return np.nan

    def preprocess_data_cleaned(self):
        self.data_cleaned = self.data_raw[self.keep_columns].copy()
        self.data_cleaned.rename(
            columns={"neighbourhood_group_cleansed": "neighbourhood"},
            inplace=True,
        )

        # Q -? Remove rows with missing values. Could be common?
        self.data_cleaned = self.data_cleaned.dropna(axis=0)

    def preprocess_price_column(self):
        """
        Preprocesses the price column by removing converting it to an integer.
        Also, removes rows with price under certain price.
        """
        self.data_cleaned["price"] = self.data_cleaned["price"].str.extract(
            r"(\d+).",
        )
        self.data_cleaned["price"] = self.data_cleaned["price"].astype(int)

        if self.remove_price_under > 0:
            self.data_cleaned = self.data_cleaned[
                self.data_cleaned["price"] >= self.remove_price_under
            ]

    def preprocess_amenities_column(self):
        """
        "Preprocesses the amenities column by
        extracting the amenities and creating binary columns for each amenity."
        """
        self.data_cleaned["TV"] = self.data_cleaned["amenities"].str.contains(
            "TV",
        )
        self.data_cleaned["TV"] = self.data_cleaned["TV"].astype(int)
        self.data_cleaned["Internet"] = self.data_cleaned[
            "amenities"
        ].str.contains("Internet")
        self.data_cleaned["Internet"] = self.data_cleaned["Internet"].astype(
            int,
        )
        self.data_cleaned["Air_conditioning"] = self.data_cleaned[
            "amenities"
        ].str.contains("Air conditioning")
        self.data_cleaned["Air_conditioning"] = self.data_cleaned[
            "Air_conditioning"
        ].astype(int)
        self.data_cleaned["Kitchen"] = self.data_cleaned[
            "amenities"
        ].str.contains("Kitchen")
        self.data_cleaned["Kitchen"] = self.data_cleaned["Kitchen"].astype(int)
        self.data_cleaned["Heating"] = self.data_cleaned[
            "amenities"
        ].str.contains("Heating")
        self.data_cleaned["Heating"] = self.data_cleaned["Heating"].astype(int)
        self.data_cleaned["Wifi"] = self.data_cleaned["amenities"].str.contains(
            "Wifi",
        )
        self.data_cleaned["Wifi"] = self.data_cleaned["Wifi"].astype(int)
        self.data_cleaned["Elevator"] = self.data_cleaned[
            "amenities"
        ].str.contains("Elevator")
        self.data_cleaned["Elevator"] = self.data_cleaned["Elevator"].astype(
            int,
        )
        self.data_cleaned["Breakfast"] = self.data_cleaned[
            "amenities"
        ].str.contains("Breakfast")
        self.data_cleaned["Breakfast"] = self.data_cleaned["Breakfast"].astype(
            int,
        )

        self.data_cleaned.drop("amenities", axis=1, inplace=True)

    def preprocess_category_column(self):
        """
        Preprocesses the category column by binning the price into categories.
        """
        self.data_cleaned["category"] = pd.cut(
            self.data_cleaned["price"],
            bins=self.price_bins,
            labels=self.category_labels,
        )
