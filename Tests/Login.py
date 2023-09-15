import pytest
import requests

# API endpoint for user login
LOGIN_URL = "http://127.0.0.1:8000/api/core/user/login/"

def test_valid_user_login():
    # Define valid user login data
    login_data = {
        "employee_id": "PSI-2345",
        "email": "john.doe1@gmail.com",
        "password": "P@ssw1rd"
    }

    # Make a POST request to the login endpoint
    response = requests.post(LOGIN_URL, json=login_data)
    print(response.status_code)

    # Assertions
    assert response.status_code == 200

def test_invalid_user_login1():
    # Define invalid user login data (e.g., incorrect credentials)
    login_data = {
        "employee_id": "PSI-563",
        "email":"ajayk@gmail.com",
        "password": "Ajay@1kr"
    }
    response = requests.post(LOGIN_URL, json=login_data)
    assert response.status_code == 200
    print(response)

def test_invalid_user_login2():
    # Define invalid user login data (e.g., incorrect credentials)
    login_data = {
        "employee_id": "PSI-563",
        "email":"ajaykgmail.com",
        "password": "Ajay@1kr"
    }
    response = requests.post(LOGIN_URL, json=login_data)
    assert response.status_code == 200


