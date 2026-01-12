import pytest
from api.create_token import create_token


@pytest.fixture(scope="session")
def base_url():
    return "https://restful-booker.herokuapp.com"


@pytest.fixture(scope="session")
def auth_token():
    return create_token()


@pytest.fixture
def headers_params(auth_token):
    return {
        "Cookie": f"token={auth_token}",
        "Content-Type": "application/json"
    }


@pytest.fixture
def request_body():
    return {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-10"
        },
        "additionalneeds": "Breakfast"
    }