from api.restful_booker_requests import (get_booking_ids,get_booking,create_booking,
                                         update_booking,partial_update_booking,delete_booking)


def negative_test_get_booking(base_url):
    invalid_booking_id = 6000
    response = get_booking(base_url, invalid_booking_id)
    assert response.status_code == 404, "Expected 404 for non-existent booking ID"


def test_create_booking_with_empty_body(base_url, headers_params):
    response = create_booking(base_url, headers_params, {})
    """
    KNOWN ISSUE:
    API returns 500 Internal Server Error for empty request body.
    Expected behavior: 400 Bad Request.
    """
    assert response.status_code == 500  # BUG: should be 400 (client error)


def test_create_booking_missing_firstname_and_lastname(base_url, headers_params, request_body):
    """
    KNOWN ISSUE:
    API returns 500 Internal Server Error when mandatory fields
    (firstname, lastname) are missing.
    Expected behavior: 400 Bad Request.
    """
    new_body = request_body.copy()
    del new_body["firstname"]
    del new_body["lastname"]
    response = create_booking(base_url, headers_params, new_body)
    assert response.status_code == 500  # BUG: should be 400


def test_update_booking_without_auth(base_url, request_body):
    invalid_booking_id = 1
    response = update_booking(
        base_url,
        headers_params={},
        request_body=request_body,
        booking_id=invalid_booking_id
    )
    assert response.status_code == 403, "Expected 403 when auth token is missing"


def test_delete_booking_without_auth(base_url):
    booking_id = 1
    response = delete_booking(
        base_url,
        headers_params={},
        booking_id=booking_id
    )
    assert response.status_code == 403, "Expected 403 when auth token is missing"


def test_delete_nonexistent_booking(base_url, headers_params):
    invalid_booking_id = 999999
    response = delete_booking(
        base_url,
        headers_params=headers_params,
        booking_id=invalid_booking_id
    )
    assert response.status_code in [404, 405], "Expected error for non-existent booking"
