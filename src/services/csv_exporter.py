import csv
from src.intrefaces.exporter import IDataExporter
from src.models.search_result import SearchResult
from typing import List
import io
from dataclasses import asdict


class CSVExporter(IDataExporter):
    def export(self, data: List[SearchResult]) -> str:
        headers = ["title", "url"]

        string_buffer = io.StringIO()
        writer = csv.DictWriter(string_buffer, fieldnames=headers)

        writer.writeheader()
        dict_data = [item.model_dump() for item in data]
        writer.writerows(dict_data)

        csv_string = string_buffer.getvalue()
        return csv_string
