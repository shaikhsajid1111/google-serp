import json
from dataclasses import asdict
from typing import List
from src.intrefaces.exporter import IDataExporter
from src.models.search_result import SearchResult


class JsonExporter(IDataExporter):

    def export_to_json(self, data):
        return json.dumps([asdict(item) for item in data], indent=1)
