from api.restful_booker_requests import (get_booking_ids,get_booking,create_booking,
                                         update_booking,partial_update_booking,delete_booking)


def test_get_booking_ids(base_url):
    response = get_booking_ids(base_url)
    assert response.status_code == 200, "Unexpected status code"


def test_create_booking(base_url, headers_params, request_body):
    response = create_booking(base_url, headers_params, request_body)
    assert response.status_code == 200, "Unexpected status code"
    assert "bookingid" in response.json()


def test_get_booking(base_url, headers_params, request_body):
    create_response = create_booking(base_url, headers_params, request_body)
    booking_id = create_response.json()["bookingid"]
    response = get_booking(base_url, booking_id)
    assert response.status_code == 200
    assert response.json()["firstname"] == "Jim"


def test_update_booking(base_url, headers_params, request_body):
    create_response = create_booking(base_url, headers_params, request_body)
    booking_id = create_response.json()["bookingid"]

    updated_body = request_body.copy()
    updated_body["firstname"] = "John"
    updated_body["lastname"] = "Doe"
    updated_body["totalprice"] = 200

    response = update_booking(base_url, headers_params, updated_body, booking_id)
    assert response.status_code == 200
    assert response.json()["firstname"] == "John"


def test_partial_update_booking(base_url, headers_params, request_body):
    create_response = create_booking(base_url, headers_params, request_body)
    booking_id = create_response.json()["bookingid"]

    response = partial_update_booking(base_url, headers_params, {"firstname": "Dan"}, booking_id)

    assert response.status_code == 200
    assert response.json()["firstname"] == "Dan"


def test_delete_booking(base_url, headers_params, request_body):
    create_response = create_booking(base_url, headers_params, request_body)
    booking_id = create_response.json()["bookingid"]

    response = delete_booking(base_url, headers_params, booking_id)
    assert response.status_code == 201

