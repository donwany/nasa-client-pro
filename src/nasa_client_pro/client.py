import requests
import os
from tenacity import retry, stop_after_attempt, wait_exponential


class NASAClient:
    """A client to explore the universe via NASA APIs."""

    BASE_URL = "https://api.nasa.gov"

    def __init__(self, api_key="DEMO_KEY"):
        self.api_key = api_key

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1))
    def get_apod(self, start_date, end_date):
        """Astronomy Picture of the Day (APOD)."""
        endpoint = f"{self.BASE_URL}/planetary/apod"
        params = {
            "api_key": self.api_key,
            "start_date": start_date,
            "end_date": end_date
        }
        try:
            response = requests.get(endpoint, params=params, timeout=60)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            raise RuntimeError("NASA API request timed out")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Request failed: {e}")

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1))
    def search_asteroids(self, start_date, end_date):
        """NeoWs (Near Earth Object Web Service) - find asteroids near Earth."""
        endpoint = f"{self.BASE_URL}/neo/rest/v1/feed"
        params = {
            "start_date": start_date,
            "end_date": end_date,
            "api_key": self.api_key,
        }
        try:
            response = requests.get(endpoint, params=params, timeout=60)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            raise RuntimeError("NASA API request timed out")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Request failed: {e}")
