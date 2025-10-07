from etl.transform import normalize_reviews

def test_normalize_reviews_structure(spark_session):
    sample_data = {
        "reviews": [
            {
                "products": [
                    {
                        "id": "p1",
                        "product": {"sku": "ABC123", "title": "Test Product"},
                        "rating": {"rating": 5},
                        "review": "Excellent!"
                    }
                ]
            }
        ]
    }
    df = normalize_reviews(sample_data)
    assert "product_sku" in df.columns
    assert "review_rating" in df.columns
