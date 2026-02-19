import pytest
from utils.api_client import APIClient

def test_get_users_returns_200(api_client):
    response = api_client.get_users()
    assert response.status_code == 200

def test_get_users_returns_list(api_client):
    response = api_client.get_users()
    data = response.json()
    assert len(data["data"]) > 0

def test_get_single_user_returns_200(api_client):
    response = api_client.get_user(1)
    assert response.status_code == 200

def test_single_user_not_found(api_client):
    response = api_client.get_user(9999)
    assert response.status_code == 404

def test_create_user_returns_201(api_client):
    response = api_client.create_user("John", "Engineer")
    assert response.status_code == 201

def test_create_user_returns_name_and_job(api_client):
    response = api_client.create_user("John", "Engineer")
    data = response.json()
    assert data["name"] == "John"
    assert data["job"] == "Engineer"

def test_update_user_returns_200(api_client):
    response = api_client.update_user(1, "John", "Senior Engineer")
    assert response.status_code == 200

def test_update_user_returns_updated_job(api_client):
    response = api_client.update_user(1, "John", "Senior Engineer")
    data = response.json()
    assert data["job"] == "Senior Engineer"

def test_delete_user_returns_204(api_client):
    response = api_client.delete_user(1)
    assert response.status_code == 204

def test_get_users_page_two(api_client):
    response = api_client.get_users(page=2)
    data = response.json()
    assert response.status_code == 200
    assert data["page"] == 2

