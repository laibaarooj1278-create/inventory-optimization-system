import pandas as pd
import os

# Dataset folder path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_PATH = os.path.join(BASE_DIR, "Dataset")


def load_csv(filename):
    file_path = os.path.join(DATASET_PATH, filename)

    try:
        data = pd.read_csv(file_path)
        print(f"✓ {filename} loaded successfully.")
        return data

    except FileNotFoundError:
        print(f"✗ {filename} not found.")
        return None

    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return None


def load_all_data():

    datasets = {

        "products": load_csv("products.csv"),
        "inventory": load_csv("inventory.csv"),
        "forecast": load_csv("forecast.csv"),
        "categories": load_csv("categories.csv"),
        "suppliers": load_csv("suppliers.csv"),
        "purchases": load_csv("purchases.csv"),
        "sales": load_csv("sales.csv")

    }

    return datasets


def show_dataset_info(datasets):

    print("\n" + "=" * 60)
    print("DATASET SUMMARY")
    print("=" * 60)

    for name, data in datasets.items():

        if data is not None:

            print(f"\n{name.upper()}")

            print(f"Rows    : {data.shape[0]}")
            print(f"Columns : {data.shape[1]}")

            print("Column Names")

            print(list(data.columns))

        else:

            print(f"\n{name.upper()} : Dataset Missing")


if __name__ == "__main__":

    datasets = load_all_data()

    show_dataset_info(datasets)