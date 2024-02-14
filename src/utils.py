import os
from pathlib import Path
import pandas as pd
import sqlite3

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
    env_path = os.getenv('MY_PROJECT_DATA_DIR')
    if env_path:
        return Path(env_path)
    else:
        base_dir = Path(__file__).resolve().parent.parent
        return base_dir / 'data'

def load_ticker_data(ticker, conn):
    db_dir = get_data_dir() / 'stock_data.db'

    # Instantiate connection
    conn = sqlite3.connect(db_dir)
    query = f"SELECT * FROM STOCK_DATA WHERE ticker = '{ticker}'"
    df = pd.read_sql_query(query, conn)
    
    return df