import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

import snowflake
from  snowflake.connector import connection

# Load environment variables from .env file
load_dotenv()

tickers = ["AMZN", "IGLB", "SPY"]

fetch_and_clean = lambda ticker: (
    yf.download(ticker, period="2y")
    [['Open', 'High', 'Low', 'Close']]
    .droplevel(1, axis=1)  # Remove MultiIndex level if present
    .reset_index()  # Make Date a column
    .rename(columns={'index': 'Date'})
    .assign(Date=lambda x: x['Date'].dt.strftime('%Y-%m-%d'))
    .rename_axis(None, axis=1)  # <-- THIS REMOVES THE COLUMN NAME ("Price")
)

df_amzn, df_iglb, df_spy = map(fetch_and_clean, tickers)

conn = snowflake.connector.connect(
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    account=os.getenv('ACCOUNT'),
    warehouse=os.getenv('WAREHOUSE'),
    database=os.getenv('DATABASE'),
    schema=os.getenv('SCHEMA')
)

def full_refresh_table(conn,
                      df: pd.DataFrame, 
                      table_name: str) -> None:
    """
    Fully refreshes a Snowflake table with DataFrame contents
    - Drops all existing data
    - Writes new data from DataFrame
    - Requires active connection passed as argument
    
    Parameters:
        conn: Active Snowflake connection
        df: DataFrame with data to load (must match table schema)
        table_name: Target table name (e.g., "AMAZON")
    """
    cursor = conn.cursor()
    
    try:
        # 1. Fast truncate (preserves table structure)
        cursor.execute(f"TRUNCATE TABLE {table_name}")
        
        # 2. Bulk insert (optimized for DataFrames)
        if len(df) > 0:
            cursor.executemany(
                f"INSERT INTO {table_name} ({','.join(df.columns)}) VALUES ({','.join(['%s']*len(df.columns))})",
                df.to_records(index=False).tolist()
            )
        
        conn.commit()
        print(f"Successfully refreshed {table_name} with {len(df)} records")
        
    except Exception as e:
        conn.rollback()
        raise RuntimeError(f"Failed to refresh {table_name}: {str(e)}")
        
    finally:
        cursor.close()

full_refresh_table(conn, df_amzn, "AMAZON")
full_refresh_table(conn, df_iglb, "IGLB") 
full_refresh_table(conn, df_spy, "SPY")