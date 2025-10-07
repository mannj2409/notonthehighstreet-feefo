# Notonthehighstreet - Feefo ETL (Take-home task)

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
