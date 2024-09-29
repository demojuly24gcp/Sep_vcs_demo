import requests
import json

# URL of the Flask API
url = 'http://127.0.0.1:5000/predict'

# Sample input data
data = {
    "features":[5.5, 2.5, 4.0, 1.3]
}

# Send POST request
response = requests.post(url, json=data)

# Print response
if response.status_code == 200:
    print('Prediction:', response.json())
else:
    print(f'Error: {response.status_code}, {response.text}')
