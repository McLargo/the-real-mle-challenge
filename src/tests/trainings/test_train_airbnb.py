from pathlib import Path
from sklearn.ensemble import RandomForestClassifier

from trainings.airbnb import AirbnbTraining


def test_train_airbnb():
    dir = Path.cwd()
    input_filename = Path.joinpath(dir, "tests", "data", "cleaned.csv")

    train = AirbnbTraining(
        input_filename=input_filename.__str__(),
        output_filename="model.pkl",
    )
    data = train.load_data()
    model = train.train(data)
    assert model is not None
    assert isinstance(model, RandomForestClassifier)
    # TODO: avoid magic numbers
    assert model.n_estimators == 500
