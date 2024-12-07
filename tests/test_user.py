import pytest
import requests

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
