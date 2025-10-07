from etl.extract import fetch_pages
from etl.transform import normalize_feefo_pages
from etl.load import save_to_duckdb, save_to_parquet
import pandas as pd

def main():
    pages = fetch_pages(max_pages=3)
    df = normalize_feefo_pages(pages)
    save_to_duckdb(df)
    save_to_parquet(df)

    avg_rating = df.groupby("product_sku")["rating"].mean().reset_index().sort_values("rating", ascending=False)
    top5 = df["product_sku"].value_counts().head(5).reset_index()
    top5.columns = ["product_sku", "review_count"]

    print("\nAverage Rating per Product:")
    print(avg_rating.head(10))
    print("\nTop 5 Products by Review Count:")
    print(top5)

    avg_rating.to_csv("data/avg_rating.csv", index=False)
    top5.to_csv("data/top5.csv", index=False)

if __name__ == "__main__":
    main()
