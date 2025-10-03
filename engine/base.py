from abc import ABC, abstractmethod
from typing import List, Dict, Any

class RecommendationType(ABC):

    def __init__(self, title: str = None):
        self.title = title

    @abstractmethod
    def get_candidates(self, user_id: int) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def rank_candidates(self, candidates: List[Dict[str, Any]], user_id: int) -> List[dict[str, Any]]:
        pass

    def get_row(self, user_id: int) -> Dict[str, Any]:
        candidates = self.get_candidates(user_id)
        ranked = self.rank_candidates(candidates, user_id)
        return {"title": self.title, "items": ranked}