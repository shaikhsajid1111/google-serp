from dataclasses import dataclass


@dataclass(frozen=True)
class SearchResult:
    title: str
    url: str
