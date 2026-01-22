# Restful Booker API – Automated Testing (Python)

## Project Overview
This project contains automated API tests for the Restful Booker application (public demo API).
The tests are implemented in Python, using Pytest and Requests, and cover positive, negative, and edge case scenarios.

The goal of this project is to demonstrate:
- API Automation Testing skills
- Clear and maintainable project structure
- Token-based authentication handling
- Negative testing and real defect identification
- QA best practices

---

## Technologies Used
- Python 3
- Pytest
- Requests
- REST API
- Postman
- JSON

---

## Tested API
- **Base URL:** `https://restful-booker.herokuapp.com`

---

## Project Structure
```
Proiect-Restful-Booker-API-Tests/
│
├── api/
│   ├── create_token.py
│   └── restful_booker_requests.py
│
├── tests/
│   ├── test_restful_booking.py
│   └── negative_test_restful_booking.py
│
├── conftest.py
├── requirements.txt
└── README.md
```

---

## Authentication
Authentication is performed using the endpoint:
```
POST /auth
```

The token is:
- generated once per session using a Pytest fixture
- sent in requests via header:
```
Cookie: token=<auth_token>
```

---

## Test Coverage

### Positive Tests
- Retrieve booking IDs list
- Create booking
- Retrieve booking by ID
- Update booking (PUT)
- Partial update booking (PATCH)
- Delete booking (DELETE)

### Negative Tests
- Get booking with non-existing ID → 404
- Create booking with empty body → BUG (500 instead of 400)
- Create booking without mandatory fields → BUG (500 instead of 400)
- Update booking without authentication → 403
- Delete booking without authentication → 403
- Delete non-existing booking → 404 / 405

---

## Identified Defects (Known Issues)

| Scenario | Actual Response | Expected Response |
|--------|---------------|-----------------|
| Create booking with empty body | 500 Internal Server Error | 400 Bad Request |
| Missing mandatory fields | 500 Internal Server Error | 400 Bad Request |

---

## ▶Test Execution

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run All Tests
```bash
pytest -v
```

---

## Postman Collection
Included file:
```
Restful_Booker.postman_collection.json
```
---

## Author
**QA Tester**
