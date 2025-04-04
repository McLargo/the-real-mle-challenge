import argparse
import logging

from preprocessor.airbnb import AirbnbDataPreprocessor

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Preprocess Airbnb data",
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
        logging.info("Preprocessing Airbnb data")
        preprocessing = AirbnbDataPreprocessor(
            input_filename=args.input,
            output_filename=args.output,
        )
        data_raw = preprocessing.load_data()
        data_cleaned = preprocessing.clean_data(data_raw)
        preprocessing.save_data(data_cleaned)
        logging.info("Data preprocessing completed successfully.")
    except Exception as e:
        logging.info(f"An error occurred: {e}")
        logging.info("Data preprocessing failed.")
        raise e
