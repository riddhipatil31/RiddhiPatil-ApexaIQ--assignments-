import json
import requests
import pytest

# Load JSON file data
with open("api_data.json", "r") as file:
    sample_data = json.load(file)

# API Endpoint
URL = "https://jsonplaceholder.typicode.com/todos/1"

# Test API response
def test_api_response():
    response = requests.get(URL)
    assert response.status_code == 200  # Check if request is successful
    api_data = response.json()

    # Assertions to compare API response with JSON file
    assert api_data == sample_data

if __name__ == "__main__":
    pytest.main()
