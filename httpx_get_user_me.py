import httpx

# Данные для входа в систему
login_payload = {
    "email": "dimakud@example.com",
    "password": "dimakud"
}

# Выполняем post запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print(login_response_data)
access_token = login_response_data["token"]["accessToken"]
print(access_token)

# Выполняем get запрос к /api/v1/users/me

headers = {"Authorization": f"Bearer {access_token}"}

users_response = httpx.get(url="http://localhost:8000/api/v1/users/me", headers=headers)
users_response_data = users_response.json()
users_response_status_code = users_response.status_code
print(users_response_data)
print(users_response_status_code)