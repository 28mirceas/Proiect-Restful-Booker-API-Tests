import requests

def get_booking_ids(base_url):
    endpoint = f"{base_url}/booking"
    response = requests.get(endpoint)
    return response


def get_booking(base_url, booking_id):
    endpoint = f"{base_url}/booking/"+f"{booking_id}"
    response = requests.get(endpoint)
    return response


def create_booking(base_url, headers_params, request_body):
    endpoint = f"{base_url}/booking"
    response = requests.post(endpoint, json=request_body, headers=headers_params)
    return response


def update_booking(base_url, headers_params, request_body, booking_id):
    endpoint = f"{base_url}/booking/"+f"{booking_id}"
    response = requests.put(endpoint, json=request_body, headers=headers_params)
    return response


def partial_update_booking(base_url, headers_params, request_body, booking_id):
    endpoint = f"{base_url}/booking/" + f"{booking_id}"
    response = requests.patch(endpoint, json=request_body, headers=headers_params)
    return response


def delete_booking(base_url, headers_params, booking_id):
    endpoint = f"{base_url}/booking/" + f"{booking_id}"
    response = requests.delete(endpoint, headers=headers_params)
    return response





