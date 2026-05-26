from config.settings import BASE_URL
from urllib.parse import urlencode


class UriUtils:
    @staticmethod
    def build_query_url(query):
        params = {"q": query}
        query_string = urlencode(params)
        full_url = f"{BASE_URL}/search?{query_string}"
        return full_url
