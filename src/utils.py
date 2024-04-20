import os
from pathlib import Path
import pandas as pd
import sqlite3

# with open('config.yaml')


def get_data_dir() -> Path:
    """
    Retrieves the absolute path to the data directory.

    This function first checks for an environment variable 'MY_PROJECT_DATA_DIR' to determine the path to the data directory.
    If the environment variable is set, it uses this value as the path, ensuring it is converted to a Path object before returning.
    If the environment variable is not set, the function calculates the path based on the assumption that the data directory is
    located two levels up from the current file and then under a directory named 'data'.

    Returns:
        pathlib.Path: The absolute path to the data directory. This path can be based on an environment variable or
                      determined programmatically from the location of this script.

    Example:
        To set the environment variable on a Unix-like system:
        export MY_PROJECT_DATA_DIR="/path/to/your/data"

        To use this function in your code:
        data_dir_path = get_data_dir()
        print(data_dir_path)  # Outputs: Path object representing the data directory's absolute path
    """
    env_path = os.getenv("MY_PROJECT_DATA_DIR")
    if env_path:
        return Path(env_path)
    else:
        base_dir = Path(__file__).resolve().parent.parent
        return base_dir / "data"


class DB:
    def __init__(self, db_name: str = "stock_data.db") -> None:

        db_dir = get_data_dir() / db_name
        self.con = sqlite3.connect(db_dir)

    def run_query(self, query) -> pd.DataFrame:
        df = pd.read_sql_query(query, con=self.con, parse_dates=["date"])

        return df

    def load_ticker_data(self, ticker: str):
        query = f"SELECT * FROM STOCK_DATA WHERE ticker = '{ticker}'"
        return self.run_query(query)


import pickle


def convert_to_pickle(obj, file_path):
    """
    This function takes an object and a file path, then serializes the object
    and saves it to a pickle file at the specified file path.

    :param obj: The object to be pickled (serialized).
    :param file_path: The path of the file where the object will be saved.
    """
    with open(file_path, "wb") as file:
        pickle.dump(obj, file)
        print(f"Object successfully pickled to {file_path}")


# Example usage:
# my_object = {'key': 'value', 'number': 42}
# convert_to_pickle(my_object, 'my_object.pkl')
