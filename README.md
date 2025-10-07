# Notonthehighstreet - Feefo ETL 

## Overview
This project fetches Feefo review data for merchant `notonthehighstreet-com`, normalizes it (one row per product review), stores it locally (DuckDB and Parquet), and produces simple analysis:
- Average rating per product
- Top 5 products by number of reviews

## How to run
1. Create a virtualenv and install:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt


By default it fetches up to 3 pages. Change max_pages in main.py or call python -m main after editing.

Outputs:

•	data/feefo.duckdb (DuckDB DB)

•	data/feefo_reviews.parquet

•	data/avg_rating_per_product.csv

•	data/top5_products_by_reviews.csv

Design notes

•	Pagination: uses page and pageSize params and stops after max_pages or when API indicates last page.

•	Schema decisions: data is flattened so each product entry in a review becomes its own row (this makes product-level metrics trivial).

•	Storage: DuckDB chosen for lightweight embedded analytics and a Parquet file for portability.

•	Testing: basic unit test on transform logic under tests/.

Extend / Next steps

Add incremental ingestion (keep cursor/state)

Add richer unit tests and schema validation

Deploy with Docker and schedule as a CI job or Databricks job
