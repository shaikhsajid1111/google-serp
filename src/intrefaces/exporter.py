from abc import ABC, abstractmethod
from typing import List
from src.models.search_result import SearchResult


class IDataExporter(ABC):
    @abstractmethod
    def export_to_json(self, data: List[SearchResult]) -> str:
        pass
