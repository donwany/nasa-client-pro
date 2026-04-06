from nasa_client_pro import NASAClient
from dotenv import load_dotenv
import os
from loguru import logger

load_dotenv(".env", override=True)

NASA_API_KEY = os.getenv("NASA_API_KEY")

if __name__ == "__main__":
    # --- Usage (Clean and simple) ---
    nasa = NASAClient(api_key=NASA_API_KEY)

    # 1. Get the cool space photo of the day
    logger.info("Fetching APOD...")
    photo = nasa.get_apod()
    print(f"Today's Title: {photo['title']}")
    print(f"Today's URL: {photo['url']}")
    print(f"Today's Explanation: {photo['explanation']}")

    print("-" * 100)
    # 2. Check for "Space Rocks" near us
    logger.info("Searching for asteroids...")
    asteroids = nasa.search_asteroids("2026-04-01", "2026-04-02")
    print(f"Found {asteroids['element_count']} asteroids this week!")
