import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class NASAClient:
    BASE_URL = "https://api.nasa.gov"

    def __init__(self, api_key, timeout=60):
        self.api_key = api_key
        self.timeout = timeout

        # 🔥 Add retry logic
        self.session = requests.Session()
        retries = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        self.session.mount("https://", HTTPAdapter(max_retries=retries))

    def get_apod(self):
        endpoint = f"{self.BASE_URL}/planetary/apod"
        params = {"api_key": self.api_key}

        try:
            response = self.session.get(endpoint, params=params, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            raise RuntimeError("NASA API request timed out")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Request failed: {e}")

    def search_asteroids(self, start_date, end_date):
        endpoint = f"{self.BASE_URL}/neo/rest/v1/feed"
        params = {
            "start_date": start_date,
            "end_date": end_date,
            "api_key": self.api_key,
        }

        try:
            response = self.session.get(endpoint, params=params, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            raise RuntimeError("Asteroid request timed out")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Request failed: {e}")
