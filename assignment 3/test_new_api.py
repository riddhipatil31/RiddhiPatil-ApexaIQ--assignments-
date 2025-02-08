import json
import requests
import pytest
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# API Endpoint for Open-Meteo
URL = "https://api.open-meteo.com/v1/forecast?latitude=37.7749&longitude=-122.4194&current_weather=true"

# Test API response and create JSON file
def test_weather_api_response():
    try:
        response = requests.get(URL)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.RequestException as e:
        logging.error("Request failed: %s", e)
        pytest.fail("API request failed")

    # Check if the response is successful
    assert response.status_code == 200, "API response was not successful"
    
    data = response.json()
    
    # Save the data to a JSON file
    with open("weather_data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

    # Check if the expected fields are present in the response
    assert "current_weather" in data, "Current weather data not found in response"
    
    # Debugging output
    logging.info("Weather Data: %s", data)


if __name__ == "__main__":
    pytest.main()
