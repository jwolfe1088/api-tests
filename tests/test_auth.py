import pytest

def test_successful_login_returns_200(api_client):
    response = api_client.login("eve.holt@reqres.in", "cityslicka")
    assert response.status_code == 200

def test_successful_login_returns_token(api_client):
    response = api_client.login("eve.holt@reqres.in", "cityslicka")
    data = response.json()
    assert "token" in data

def test_failed_login_returns_400(api_client):
    response = api_client.login("eve.holt@reqres.in", "")
    assert response.status_code == 400

def test_failed_login_returns_error_message(api_client):
    response = api_client.login("eve.holt@reqres.in", "")
    data = response.json()
    assert "error" in data