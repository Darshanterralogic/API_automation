import pytest
import requests

headers = {}
headers['User-Agent'] = "Mozilla/5.0"
LOGIN_URL = "http://127.0.0.1:8000/api/core/user/login/"
login_data = {
        "emp_id": "PSI-2345",
        "email": "john.doe1@gmail.com",
        "password": "P@ssw1rd"
    }

response = requests.post(url=LOGIN_URL,json=login_data)
responseJson = response.json()
headers['Authorization'] = "Bearer " + responseJson['tokens']['access']



DASHBOARD_URL = "http://127.0.0.1:8000/api/core/"

def test_dashboard_tool_counts3():
    # Make a GET request to the dashboard
    response = requests.get(DASHBOARD_URL,headers=headers)

    # Assertions
    assert response.status_code == 404


    # Parse the JSON response
    data = response.json()

    # Verify that the 'tool_counts' field exists in the response
    assert 'tool_counts' in data

    # Replace these tool names with your actual tool names
    tools_to_check = ["pyATS", "Xpresso", "Earms", "Trade", "LaaS", "ADSRSVP", "SSR"]

    for tool in tools_to_check:
        # Check if the tool is present in the response
        assert tool in data['tool_counts'], f"Tool '{tool}' not found in tool counts"

        # Add assertions to verify the count
    assert isinstance(data['tool_counts'][tool], int), f"Count for '{tool}' is not an integer"
    assert data['tool_counts'][tool] >= 0, f"Count for '{tool}' is negative"

def test_dashboard_kb_docs_table2():
    # Make a GET request to the dashboard
    response = requests.get(DASHBOARD_URL,headers=headers)

    # Assertions
    assert response.status_code == 404

    # Parse the JSON response
    data = response.json()

    # Verify that the 'kb_docs' field exists in the response
    assert 'kb_docs' in data

    # Verify that 'kb_docs' is a list
    assert isinstance(data['kb_docs'], list), "kb_docs is not a list"

    # Check if the 'kb_docs' list is not empty
    assert len(data['kb_docs']) > 0, "No KB docs found in the response"

def test_dashboard_search_kb_docs1():
    # Define a search query (e.g., search for KB Docs by title/summary)
    search_query = "Critical Bug"

    # Make a GET request to search for KB Docs
    response = requests.get(f"{DASHBOARD_URL}?search={search_query}headers=headers")

    # Assertions
    assert response.status_code == 404

    # Parse the JSON response
    data = response.json()

    # Verify that the 'kb_docs' field exists in the response
    assert 'kb_docs' in data

    # Verify that 'kb_docs' is a list
    assert isinstance(data['kb_docs'], list), "kb_docs is not a list"

    # Check if the 'kb_docs' list is not empty
    assert len(data['kb_docs']) > 0, f"No KB docs found for search query '{search_query}'"
