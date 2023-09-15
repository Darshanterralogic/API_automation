import pytest
import requests

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


    Logout_url = "http://127.0.0.1:8000/api/core/user/logout/"


    response = requests.post(Logout_url)