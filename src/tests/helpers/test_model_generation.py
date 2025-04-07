from pathlib import Path

import pytest

from helpers.model_generation import PickleModelGeneration


def test_pickle_model_generation(df) -> None:
    output_filename = "model.pkl"
    # Assert no file exists before saving
    output_file = Path(output_filename)
    assert output_file.exists() is False

    # Save the model to a pickle file
    model_gen = PickleModelGeneration(output_filename=output_filename)

    # Create a sample model (DataFrame in this case)
    # In practice, this would be a trained model
    model_gen.store_model(model=df)

    # Assert the file exists after saving
    assert output_file.exists()
    assert output_file.is_file()

    # clean up the created file after the test
    output_file.unlink()
    assert output_file.exists() is False


def test_pickle_model_generation_invalid_file_type(df) -> None:
    model_gen = PickleModelGeneration(
        output_filename="test.txt",
    )
    with pytest.raises(ValueError):
        model_gen.store_model(model=df)
