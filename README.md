# API TESTING PROJECT ReRes.in

A python-based API test suite built with pytest and requests, testing the ReqRes.in REST API.

## Tech Stack

- Python 3.12
- pytest
- requests

## Project Structure
```
api-tests/
├── tests/
│   ├── test_users.py
│   ├── test_auth.py
├── utils/
│   └── api_client.py
├── conftest.py
├── requirements.txt
└── README.md
```

## Test Coverage

### User Tests (`tests/test_users.py`)
- GET all users returns 200
- GET all users returns a list of users
- GET single user returns 200
- GET single user not found returns 404
- POST create user returns 201
- POST create user returns correct name and job
- PUT update user returns 200
- PUT update user returns updated job
- DELETE user returns 204
- GET users page two returns correct page


### Auth Tests (`tests/test_auth.py`)
- POST successful login returns 200
- POST successful login returns token
- POST failed login returns 400
- POST failed login returns error message

## Setup & Installation

1. Clone the repository
2. Create a virtual environment
```
python -m venv venv
```
3. Activate the virtual environment
```
venv\Scripts\activate
```
4. Install dependencies
```
pip install -r requirements.txt
```
5. Add your ReqRes API key to `utils/api_client.py`

## Running the Tests
```
pytest
```

## Notes
- Covers positive and negative test cases
- API client abstracted into `utils/api_client.py` for reusability
- Fixtures managed via `conftest.py` to avoid code repetition