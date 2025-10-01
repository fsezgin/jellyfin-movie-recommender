"""
Criteris: For popularity-based recommendation:
1. Movies with the highest rating
2. Number of views
"""

from typing import List, Dict, Any

from base import RecommendationType

class PopularityBasedRecommendation(RecommendationType):

    def __init__(self):
        super().__init__()

    def get_candidates(self, user_id: int) -> List[Dict[str, Any]]:
        pass

    def rank_candidates(self, candidates: List[Dict[str, Any]], user_id: int) -> List[dict[str, Any]]:



        pass
