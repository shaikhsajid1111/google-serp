from abc import ABC, abstractmethod
from src.intrefaces.parser_confg import ParserConfig


class IhtmlParser(ABC):
    @abstractmethod
    def parse(self, parser_config: ParserConfig):
        pass
