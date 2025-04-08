import logging
from datetime import datetime
from pathlib import Path

import joblib
from fastapi import Depends, FastAPI, HTTPException

from models.enums import NeighbourhoodEnum, PriceCategoryEnum, RoomTypeEnum
from models.inference import ListingInput
from models.responses import HealthcheckOutput, ListingOutput

api = FastAPI()


# TODO: common logging config shared by all modules
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

logger = logging.getLogger("fastapi-app")


def get_model():
    if not hasattr(api.state, "model"):
        dir = Path.cwd().parent
        # Load the model
        model = Path.joinpath(dir, "models", "v2.pkl")
        with open(model, "rb") as f:
            api.state.model = joblib.load(f)
    return api.state.model


@api.get("/health", tags=["Health"], response_model=HealthcheckOutput)
async def healthcheck():
    """
    Healthcheck endpoint
    """
    return HealthcheckOutput(
        status="ok",
        timestamp=datetime.now(datetime.UTC).isoformat(),
    )


@api.post("/inference", tags=["Inference"], response_model=ListingOutput)
def predict(input_data: ListingInput, model=Depends(get_model)):
    try:
        mapped_room_type = RoomTypeEnum.from_str(input_data.room_type).value
    except ValueError:
        logger.error(
            f"Invalid room type: {input_data.room_type}",
        )
        raise HTTPException(
            status_code=400,
            detail=f"{input_data.room_type} is not a valid room type",
        )

    try:
        mapped_neighbourhood = NeighbourhoodEnum.from_str(
            input_data.neighbourhood,
        ).value
    except ValueError:
        logger.error(
            f"Invalid neighbourhood: {input_data.neighbourhood}",
        )
        raise HTTPException(
            status_code=400,
            detail=f"{input_data.neighbourhood} is not a valid neighbourhood",
        )

    features = [
        [
            input_data.accommodates,
            mapped_room_type,
            input_data.bedrooms,
            input_data.bathrooms,
            mapped_neighbourhood,
        ],
    ]

    inference = model.predict(features)
    try:
        price_category = PriceCategoryEnum.from_value(int(inference[0]))
    except ValueError:
        logger.error(
            f"Predict is not a valid price category: {inference[0]}",
        )
        raise HTTPException(
            status_code=400,
            detail=f"Prediction {inference[0]} is not a valid price category",
        )

    except IndexError:
        logger.error("Prediction is empty")
        raise HTTPException(
            status_code=400,
            detail="Prediction is empty",
        )

    return ListingOutput(
        id=input_data.id,
        price_category=price_category.to_str(),
    )
