# API Tests - REST API Automation Suite

Self-built API automation suite targeting the [ReqRes.in](https://reqres.in) public REST API using **Python, pytest, and requests**.

Built as part of my self-training for **Junior QA Automation Engineer** roles while transitioning from running a small business.

## About This Project

This suite demonstrates clean, reusable API testing across user management and authentication endpoints, covering both positive and negative scenarios.

## Technologies Used

- **Python 3.12**
- **pytest** (test framework + fixtures)
- **requests** (HTTP client)
- **GitHub Actions** (CI/CD)

## Testing Coverage

**Users** (`tests/test_users.py`)
- GET all users with pagination
- GET single user (success + 404 not found)
- POST create user
- PUT update user
- DELETE user

**Authentication** (`tests/test_auth.py`)
- Successful login — returns token
- Failed login — returns 400 and error message

## Key Features & Design Patterns

- **Reusable API client** (`utils/api_client.py`) for clean, DRY HTTP calls
- Shared **pytest fixtures** via `conftest.py` to reduce duplication
- Comprehensive positive and negative test cases
- Parameterization where appropriate
- Automated CI pipeline that runs the full suite on every push

## Project Structure
```
api-tests/
├── .github/workflows/      # GitHub Actions CI
├── tests/
│   ├── test_users.py
│   └── test_auth.py
├── utils/
│   └── api_client.py
├── conftest.py
└── requirements.txt
```

## Setup & Running Tests

1. Clone the repository
2. Create and activate a virtual environment:
```bash
python -m venv venv
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run tests:
```bash
# All tests
pytest

# Verbose + stop on first failure
pytest -v -x
```

## CI/CD

GitHub Actions workflow automatically runs the full test suite on every push.

## Why This Matters for QA Roles

This project demonstrates strong API testing fundamentals — abstraction of HTTP calls into a reusable client, proper status code and response body validation, and maintainable test structure across positive and negative scenarios.