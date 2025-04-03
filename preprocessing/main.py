import argparse

from utils.preprocessing import AirbnbDataPreprocessor

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Ejemplo de script con argumentos.")
    parser.add_argument("--input", type=str, help="Input file name")
    parser.add_argument("--output", type=str, help="Output file name")

    args = parser.parse_args()

    try:
        print("Preprocessing Airbnb data")
        preprocessing = AirbnbDataPreprocessor(
            input_filename=args.input,
            output_filename=args.output,
        )
        data_raw = preprocessing.load_data()
        data_cleaned = preprocessing.clean_data(data_raw)
        preprocessing.save_data(data_cleaned)
        print("Data preprocessing completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Data preprocessing failed.")
        raise e
