import pandas as pd
from typing import List, Dict
from utils.logger import get_logger

logger = get_logger("transform")

def normalize_feefo_pages(pages: List[Dict]) -> pd.DataFrame:
    rows = []
    for page in pages:
        for review in page.get("reviews", []):
            for product in review.get("products", []):
                prod_data = product.get("product", {})
                rating = product.get("rating", {})
                rows.append({
                    "product_sku": prod_data.get("sku"),
                    "product_title": prod_data.get("title"),
                    "rating": rating.get("rating"),
                    "review_text": product.get("review"),
                    "helpful_votes": product.get("helpful_votes"),
                })
    df = pd.DataFrame(rows)
    logger.info(f"Normalized {len(df)} rows")
    return df
