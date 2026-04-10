from tavily import TavilyClient
from pprint import pprint
from loguru import logger


if __name__ == "__main__":

    tavily_client = TavilyClient(api_key="tvly-dev-JKT6...")
    response = tavily_client.search("Who is Leo Messi?")
    logger.info("creating search results...")
    pprint(response["results"][0]["content"])
    logger.info("search successful...")
