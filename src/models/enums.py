from enum import Enum


class PriceCategoryEnum(Enum):
    LOW = 0
    MID = 1
    HIGH = 2
    LUX = 3

    @classmethod
    def from_value(cls, value: int):
        try:
            return cls(value)
        except ValueError:
            raise ValueError(f"{value} is not a valid price category value")

    def to_str(self):
        reverse_mapping = {
            self.LOW: "low",
            self.MID: "mid",
            self.HIGH: "high",
            self.LUX: "lux",
        }
        return reverse_mapping[self]


class RoomTypeEnum(Enum):
    SHARED_ROOM = 1
    PRIVATE_ROOM = 2
    ENTIRE_HOME_APT = 3
    HOTEL_ROOM = 4

    @classmethod
    def from_str(cls, label: str):
        mapping = {
            "Shared room": cls.SHARED_ROOM,
            "Private room": cls.PRIVATE_ROOM,
            "Entire home/apt": cls.ENTIRE_HOME_APT,
            "Hotel room": cls.HOTEL_ROOM,
        }
        try:
            return mapping[label]
        except KeyError:
            raise ValueError(f"{label} is not a valid room type")


class NeighbourhoodEnum(Enum):
    BRONX = 1
    QUEENS = 2
    STATEN_ISLAND = 3
    BROOKLYN = 4
    MANHATTAN = 5

    @classmethod
    def from_str(cls, label: str):
        mapping = {
            "Bronx": cls.BRONX,
            "Queens": cls.QUEENS,
            "Staten Island": cls.STATEN_ISLAND,
            "Brooklyn": cls.BROOKLYN,
            "Manhattan": cls.MANHATTAN,
        }
        try:
            return mapping[label]
        except KeyError:
            raise ValueError(f"{label} is not a valid neighbourhood")
