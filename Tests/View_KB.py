import pytest
import requests

#API endpoint for viewing KB Docs
VIEW_KB_DOCS_URL = "http://127.0.0.1:8000/kbdocs/"

def test_view_kb_docs():
    # Make a GET request to view KB Docs
    response = requests.get(VIEW_KB_DOCS_URL)

    # Assertions
    assert response.status_code == 200
    assert "kb_docs" in response.json()

def test_search_kb_docs():
    # Define a search query (e.g., search for KB Docs by title/summary)
    search_query = "Critical Bug"

    # Make a GET request to search for KB Docs
    response = requests.get(f"{VIEW_KB_DOCS_URL}?search={search_query}")

    # Assertions
    assert response.status_code == 200
    assert "kb_docs" in response.json()
    # Add further assertions based on search results

# Add more test cases for different scenarios, e.g., specific KB Doc view, search, etc.
