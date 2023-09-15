import pytest
import requests
import json

# API endpoint for user registration
SIGNUP_URL = "http://127.0.0.1:8000/api/core/user/create/"

def test_valid_user_registration():
    # Define valid user registration data
    user_data = {
        "first_name": "Darshan",
        "last_name": "Doe",
        "employee_id": "PSI-2345",
        "email": "john.doe1@gmail.com",
        "password": "P@ssw1rd",
        "re_password": "P@ssw1rd"
    }


    # Make a POST request to the registration endpoint
    response = requests.post(SIGNUP_URL,
                             json=user_data,
                )
    print(response.json)

    # # Assertions
    assert response.status_code == 200

