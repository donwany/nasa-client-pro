from src.nasa_client_pro import NASAClient
from dotenv import load_dotenv
import os
from loguru import logger


# load_dotenv(".env", override=True)
NASA_API_KEY = os.getenv("NASA_API_KEY")

def main():
    # --- Usage (Clean and simple) ---
    nasa = NASAClient(api_key=NASA_API_KEY)

    # 1. Get the cool space photo of the day
    logger.info("Fetching APOD...")
    pods = nasa.get_apod(start_date="2026-04-01", end_date="2026-04-06")
    # print(pod)
    for pod in pods:
        print(f"Today's Title: {pod['title']}")
        print(f"Today's URL: {pod['url']}")
        print(f"Today's Explanation: {pod['explanation']}")
        print(f"Date: {pod['date']}")
        print("-"*100)

    print("-" * 100)
    # 2. Check for "Space Rocks" near us
    logger.info("Searching for asteroids...")
    asteroids = nasa.search_asteroids("2026-04-01", "2026-04-06")
    print(f"Found: {asteroids['element_count']} asteroids this week!")

if __name__ == "__main__":
    main()

