import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://reqres.in/api"
API_KEY = os.getenv("API_KEY")
HEADERS = {"x-api-key": API_KEY}

class APIClient:

    def get_users(self, page=1):
        return requests.get(f"{BASE_URL}/users", params={"page": page}, headers=HEADERS)

    def get_user(self, user_id):
        return requests.get(f"{BASE_URL}/users/{user_id}", headers=HEADERS)

    def create_user(self, name, job):
        return requests.post(f"{BASE_URL}/users", json={"name": name, "job": job}, headers=HEADERS)
    
    def update_user(self, user_id, name, job):
        return requests.put(f"{BASE_URL}/users/{user_id}", json={"name": name, "job": job}, headers=HEADERS)
    
    def delete_user(self, user_id):
        return requests.delete(f"{BASE_URL}/users/{user_id}", headers=HEADERS)
    
    def login(self, email, password):
        return requests.post(f"{BASE_URL}/login", json={"email": email, "password": password}, headers=HEADERS)
    
