import requests
from typing import List, Dict, Any
from utils.logger import get_logger

logger = get_logger("extract")

BASE_URL = "https://api.feefo.com/api/20/reviews/all?merchant_identifier=notonthehighstreet-com"

def fetch_pages(max_pages: int = 3, page_size: int = 50) -> List[Dict[str, Any]]:
    results = []
    params = {"pageSize": page_size, "page": 1}
    for page in range(1, max_pages + 1):
        params["page"] = page
        try:
            logger.info(f"Fetching page {page}")
            resp = requests.get(BASE_URL, params=params, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            results.append(data)
            meta = data.get("summary", {}).get("meta", {})
            if meta and page >= meta.get("pages", page):
                break
        except Exception as e:
            logger.error(f"Error fetching page {page}: {e}")
            break
    logger.info(f"Fetched {len(results)} pages")
    return results
