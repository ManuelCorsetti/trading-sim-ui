import pandas as pd
import os
import sqlite3
from utils import get_data_dir


data_dir = get_data_dir()
db_dir = data_dir / 'stock_data.db'
tickers_dir = data_dir / 'raw_data'
# Connect to SQLite database (this will create the database file if it does not exist)
conn = sqlite3.connect(db_dir)

# Create a cursor object
cur = conn.cursor()
# cur.execute("DROP TABLE IF EXISTS daily_ohlcv")
# Create table
cur.execute('''
    CREATE TABLE IF NOT EXISTS daily_ohlcv (
        ticker TEXT NOT NULL,
        date TEXT NOT NULL,
        open REAL NOT NULL,
        high REAL NOT NULL,
        low REAL NOT NULL,
        close REAL NOT NULL,
        adj_close REAL NOT NULL,
        volume INTEGER NOT NULL,
        PRIMARY KEY (ticker, date)
    )
''')

conn.commit()

for filename in os.listdir(tickers_dir):
    if filename.endswith('.csv'):
        filepath = os.path.join(tickers_dir, filename)
        ticker = filename.replace('.csv', '')
        df = pd.read_csv(filepath)
        df.rename(columns={'Adj Close':'adj_close'}, inplace=True)
        df['ticker'] = ticker  # Add ticker column
        
        # Convert DataFrame to SQL
        df.to_sql('daily_ohlcv', conn, if_exists='append', index=False)
        print(ticker)