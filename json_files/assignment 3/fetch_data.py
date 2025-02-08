import requests
import json

# API Endpoint
URL = "https://jsonplaceholder.typicode.com/todos/1"

# Fetch data from API
response = requests.get(URL)

if response.status_code == 200:
    data = response.json()

    # Save data to a JSON file
    with open("api_data.json", "w") as file:
        json.dump(data, file, indent=4)

    print("JSON file created successfully.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
