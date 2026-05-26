import json
from dataclasses import asdict
from typing import List
from src.intrefaces.exporter import IDataExporter
from src.models.search_result import SearchResult


class JsonExporter(IDataExporter):

    def export(self, data):
        return json.dumps([item.model_dump() for item in data], indent=1)
