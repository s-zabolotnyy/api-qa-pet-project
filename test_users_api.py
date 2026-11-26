import requests

class BaseApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        return requests.get(f"{self.base_url}{endpoint}")

    def post(self, endpoint, payload):
        return requests.post(f"{self.base_url}{endpoint}", json=payload)


class UserApiClient(BaseApiClient):
    def get_all_users(self):
        return self.get("/users")

    def get_user_by_id(self, user_id):
        return self.get(f"/users/{user_id}")

    def create_user(self, user_data):
        return self.post("/users", payload=user_data)


def test_get_users_list():
    client = UserApiClient("https://typicode.com")
    response = client.get_all_users()
    
    assert response.status_code == 200
    users = response.json()
    
    emails = [user["email"] for user in users if user["id"] > 5]
    assert len(emails) == 5


def test_user_not_found():
    client = UserApiClient("https://typicode.com")
    response = client.get_user_by_id(9999)
    
    assert response.status_code == 404


def test_create_user():
    client = UserApiClient("https://typicode.com")
    new_user = {
        "name": "Sergey Zabolotnyy",
        "username": "szabolotnyy",
        "email": "test@nstu.ru"
    }
    response = client.create_user(new_user)
    
    assert response.status_code == 201
    created_data = response.json()
    assert created_data["name"] == "Sergey Zabolotnyy"
    assert "id" in created_data

