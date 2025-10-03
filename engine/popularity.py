"""
Criteris: For popularity-based recommendation:
1. Movies with the highest rating
2. Number of views
"""

import pandas as pd
from typing import List, Dict, Any
from base import RecommendationType
from settings.config import Config

class PopularityBasedRecommendation(RecommendationType):

    def __init__(self, popularity_df: pd.DataFrame, avg_rating: int = Config.avg_rating, rating_counts: int = Config.rating_counts):
        super().__init__(title= "Most Popular Movies")
        self.popularity_df = popularity_df
        self.avg_rating = avg_rating
        self.rating_counts = rating_counts

    def get_candidates(self, user_id: int) -> List[Dict[str, Any]]:
        """ we will get movie data that we created in data_preprocessing.py """
        return self.popularity_df.to_dict(orient="records")

    def rank_candidates(self, candidates: List[Dict[str, Any]], user_id: int) -> List[dict[str, Any]]:
        ratings_df = pd.DataFrame(candidates)
        ratings_df = ratings_df[(ratings_df['avg_rating'] > 3) & (ratings_df['rating_counts'] > 100)]
        ratings_df = ratings_df.sort_values(by="avg_rating", ascending=False)
        top10 = ratings_df.head(10)
        return top10

    def get_row(self, user_id: int) -> Dict[str, Any]:
        pass
