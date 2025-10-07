import duckdb
import os
from utils.logger import get_logger

logger = get_logger("load")

def save_to_duckdb(df, db_path="data/feefo.duckdb", table_name="reviews"):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = duckdb.connect(db_path)
    conn.register("tmp_df", df)
    conn.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM tmp_df")
    conn.close()
    logger.info(f"Data saved to DuckDB at {db_path}")

def save_to_parquet(df, path="data/feefo_reviews.parquet"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_parquet(path, index=False)
    logger.info(f"Data saved to Parquet at {path}")
