import requests

BASE_URL = "https://restful-booker.herokuapp.com"

def create_token():
    endpoint = f"{BASE_URL}/auth"
    request_body = {
                     "username" : "admin",
                     "password" : "password123"
    }
    response = requests.post(endpoint, json=request_body)
    #verifica status code al token
    response.raise_for_status()
    token = response.json()['token']
    return token

