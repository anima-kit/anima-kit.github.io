### searxng_utils
## Defines functions needed to setup and query SearXNG server.

import time
import requests
from langchain_community.utilities import SearxSearchWrapper

## Define constants
# URL | SearXNG server url from Docker setup
url = 'http://localhost:8080'

# Query | Default query to search
query = 'Python programming'

# Number of results | Default number of results for `results` method
num_results = 2

## Ensure SearXNG server can be reached
def _test_searxng(
    self
):
    max_retries = 5    # Maximum number of retry attempts
    retry_delay = 10   # Delay in seconds between retries

    # Test the response
    for attempt in range(max_retries):
        try:
            # Send HTTP GET request with a timeout of 30 seconds
            response = requests.get(self.url, timeout=30)
            # Success if 200 status code
            if response.status_code == 200:
                return  # Exit successfully

        except requests.exceptions.RequestException as e:
            raise

        # Retry logic: Delay before next attempt, unless it's the last one
        if attempt < max_retries - 1:
            time.sleep(retry_delay)

    # Final failure case after all retries
    exit(1)

## Get search results using Requests
def requests_search(
    self, 
    query = query
):
    # Send a GET request with the search query as a parameter
    params = {'q': query}
    timeout = 30 # How long in seconds to wait for a response
    # Get results
    response = requests.get(
        self.url, 
        params=params, 
        timeout=timeout
    )
    return response.text

## Get search result summary using 
## LangChain's `SearxSearchWrapper.run` method
def run(
    self, 
    query = query
):         
    # Get results
    results = self.client.run(
        query=query
    )
    return results

## Get search results using 
## LangChain's `SearxSearchWrapper.results` method
def results(
    self, 
    query = query, 
    num_results = num_results
):
    # Get results
    results = self.client.results(
        query=query,
        num_results=num_results
    )
    return results