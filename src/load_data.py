import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    print("\nFirst 5 rows:\n", df.head())
    print("\nLast 5 rows:\n", df.tail())
    print("\nShape:", df.shape)
    print("\nColumns:", df.columns)
    print("\nData Types:\n", df.dtypes)

    return df