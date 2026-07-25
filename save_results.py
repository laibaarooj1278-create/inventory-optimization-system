import pandas as pd
import os


def save_results(results):

    folder = "results"

    os.makedirs(folder, exist_ok=True)

    file_path = os.path.join(
        folder,
        "optimized_inventory.csv"
    )

    df = pd.DataFrame(results)

    df.to_csv(
        file_path,
        index=False
    )

    print("\n")
    print("=" * 60)
    print("Results Saved Successfully")
    print(file_path)
    print("=" * 60)