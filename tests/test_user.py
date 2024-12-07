import pytest
import requests
#Prompt for Test 1:
# "Generate a Python pytest test that sends a GET request to the endpoint 'http://127.0.0.1:8000/users/?username=admin&password=qwerty'. The test should verify that the response has a status code of 200 and no other validation is required."

# Prompt for Test 2:
#"Generate a Python pytest test that sends a GET request to the endpoint 'http://127.0.0.1:8000/users/?username=admin&password=admin'. The test should verify that the response has a status code of 401 and no other validation is required."


def test_valid_credentials():
    """Test the /users endpoint with valid credentials."""
    response = requests.get('http://127.0.0.1:8000/users/?username=admin&password=qwerty')
    assert response.status_code == 200  # Validate status code is 200
    assert response.text == ""  # Ensure the response is empty

def test_invalid_credentials():
    """Test the /users endpoint with invalid credentials."""
    response = requests.get('http://127.0.0.1:8000/users/?username=admin&password=admin')
    assert response.status_code == 401  # Validate status code is 401
    assert response.text == ""  # Ensure the response is empty
