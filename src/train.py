import argparse
import logging

from trainings.airbnb import AirbnbTraining

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Train Airbnb model",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--input", type=str, help="Input file name")
    parser.add_argument("--output", type=str, help="Output file name")

    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] %(message)s",
    )

    try:
        logging.info("Train Airbnb model")
        training = AirbnbTraining(
            input_filename=args.input,
            output_filename=args.output,
        )
        data = training.load_data()
        model = training.train(data)
        training.store_model(model)
        logging.info("Airbnb Training completed successfully.")
    except Exception as e:
        logging.info(f"An error occurred: {e}")
        logging.info("Training model failed.")
        raise e
