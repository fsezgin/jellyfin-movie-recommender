from typing import List, Dict, Any

from engine.base import RecommendationType

class GenresAndTagBasedRecommendation(RecommendationType):

    def __init__(self):
        super().__init__("Genres and Tag Based Recommendation")

    def get_candidates(self, user_id: int) -> List[Dict[str, Any]]:
        pass

    def rank_candidates(self, candidates: List[Dict[str, Any]], user_id: int) -> List[dict[str, Any]]:
        pass

    def get_row(self, user_id: int) -> Dict[str, Any]:
        pass