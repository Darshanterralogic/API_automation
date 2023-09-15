import pytest
import requests


SIGNUP_URL = "http://127.0.0.1:8000/api/core/user/create/"


def test_invalid_user_registration1():


    invalid_user_data = {
        "first_name": "darshan",
        "last_name": "sohan",
        "employee_id": "IN-123",  # Invalid employee ID format
        "email": "darshan1@gmail.com",
        "password": "Darshan@1m",
        "re_password": "Darshan@1m"
    }

    # Make a POST request to the registration endpoint
    response = requests.post(SIGNUP_URL, json=invalid_user_data)

    # Assertions
    assert response.status_code == 200

def test_invalid_user_registration2():
    invalid_user_data = {
        "first_name": "darshan",
        "last_name": "sohan",
        "employee_id": "PSI-123",
        "email": "2344qrrr",  # Invalid email format
        "password": "Darshan@1m",
        "re_password": "Darshan@1m"
    }

    # Make a POST request to the registration endpoint
    response = requests.post(SIGNUP_URL, json=invalid_user_data)

    # Assertions
    assert response.status_code == 200

def test_invalid_user_registration3():
    invalid_user_data = {
        "first_name": "darshan",
        "last_name": "sohan",
        "employee_id": "PSI-1237",
        "email": "darshan@gmail.com",
        "password": "Darshan@1m",
        "re_password": "Daarrshan@1m"  # Passwords don't match
    }

    # Make a POST request to the registration endpoint
    response = requests.post(SIGNUP_URL, json=invalid_user_data)

    # Assertions
    assert response.status_code == 200

def test_invalid_user_registration4():
    invalid_user_data = {
        "first_name": "darshan",
        "last_name": "sohan",
        "employee_id": "PSI-1236",
        "email": "darshan@gmail.com",
        "password": "Darshansohan@1m",  # Password doesn't meet requirements
        "re_password": "Darshansohan@1m"
    }

    # Make a POST request to the registration endpoint
    response = requests.post(SIGNUP_URL, json=invalid_user_data)

    # Assertions
    assert response.status_code == 200

def test_invalid_user_registration5():
    invalid_user_data = {
        "first_name": "darshan",
        "last_name": "sohan",
        "employee_id": "PSI-1239",
        "email": " ",  # blank email format
        "password": "Darshan@1m",
        "re_password": "Darshan@1m"
    }

    # Make a POST request to the registration endpoint
    response = requests.post(SIGNUP_URL, json=invalid_user_data)

    # Assertions
    assert response.status_code == 200

def test_invalid_user_registration():
    invalid_user_data = {
        "first_name": "darshan",
        "last_name": "sohan",
        "employee_id": " ",
        "email": "!@#gmail.com",
        "password": "Darshan@1m",
        "re_password": "Darshan@1m"
    }

    # Make a POST request to the registration endpoint
    response = requests.post(SIGNUP_URL,json=invalid_user_data)
    print(response)

    # Assertions
    assert response.status_code == 200






