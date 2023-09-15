import pytest
import requests

headers = {}
headers['User-Agent'] = "Mozilla/5.0"
LOGIN_URL = "http://127.0.0.1:8000/api/core/user/login/"
login_data = {
        "emp_id": "PSI-9878",
        "email": "Rina2@gmail.com",
        "password": "Rina@1raa"
    }

response = requests.post(url=LOGIN_URL,json=login_data)
responseJson = response.json()
headers['Authorization'] = "Bearer " + responseJson['tokens']['access']


#API endpoint for adding KB Docs
ADD_KB_DOCS_URL = "http://127.0.0.1:8000/api/core/kbdocs/"

def test_add_kb_docs():
    # Define valid KB Docs data
    kb_docs_data = {
            "tools": "pyATS",
            "reporter": "raghava",
            "created_datetime": "2023-09-15T10:00:00Z",
            "closed_datetime": "2023-09-16T12:00:00Z",
            "source_of_ticket": "STS",
            "ticket_link": "https://example.com/ticket/123",
            "issue_type": "Bug",
            "issue_title": "Critical Bug",
            "issue_description": "This is a critical bug.",
            "category": "bug fix",
            "help_links": "The bug was caused by...",
            "resolutions": "Resolved by...",
            "workaround" : "sdsfg",
            "others": "Additional information..."
    }

    # Make a POST request to add KB Docs
    response = requests.post(ADD_KB_DOCS_URL, json=kb_docs_data,headers=headers)

    # Assertions
    assert response.status_code == 200

def test_add_kb_docs1():
    # Define valid KB Docs data
    kb_docs_data = {
            "tools": "Earms",
            "reporter": "Raghava",
            "created_datetime": "2023-09-15T10:00:00Z",
            "closed_datetime": "2023-09-16T12:00:00Z",
            "source_of_ticket": "STS",
            "ticket_link": "https://example.com/ticket/123",
            "issue_type": "Bug",
            "issue_title": "Critical Bug",
            "issue_description": "This is a critical bug.",
            "category": "bug fix",
            "help_links": "The bug was caused by...",
            "resolutions": "Resolved by...",
            "workaround" : "sdsfg",
            "others": "Additional information..."
    }

    # Make a POST request to add KB Docs
    response = requests.post(ADD_KB_DOCS_URL, json=kb_docs_data,headers=headers)

    # Assertions
    assert response.status_code == 200


