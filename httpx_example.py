"""
В данном примере используются флакующие ресурсы, поэтому сервер возвращает не то, что нужно и код валится.
"""

import httpx


# 3. Основные функции HTTPX
# 3.1 Отправка GET-запроса
response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

print(response.status_code)  # 200
print(response.json())       # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}

# 3.2 тправка POST-запроса
data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
print(response.status_code)  # 201 (Created)
print(response.json())  # Ответ с созданной записью

# 3.3 Отправка данных в application/x-www-form-urlencoded
data = {"username": "test_user", "password": "123456"}
url_1 = "https://httpbin.org/"
url_2 = "https://postman-echo.com"

response = httpx.post(url_2, data=data, verify=False)
print(response.status_code)
print(response.json())  # {'form': {'username': 'test_user', 'password': '123456'}, ...}

# 3.4 Передача заголовков
headers = {"Authorization": "Bearer my_secret_token"}

response = httpx.get("https://httpbin.org/get", headers=headers)

print(response.json())  # Заголовки включены в ответ

# 3.5 Работа с параметрами запроса
params = {"userId": 1}

response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)

print(response.url)    # https://jsonplaceholder.typicode.com/todos?userId=1
print(response.json()) # Фильтрованный список задач

# 3.6 Отправка файлов

files = {"file": ("example.txt", open("example.txt", "rb"))}

response = httpx.post("https://httpbin.org/post", files=files)

print(response.json())  # Ответ с данными о загруженном файле

# 4. Работа с сессиями (httpx.Client)
# 4.1 Использование httpx.Client
with httpx.Client() as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

print(response1.json())  # Данные первой задачи
print(response2.json())  # Данные второй задачи

# 4.2 обавление базовых заголовков в Client
client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})

response = client.get("https://httpbin.org/get")

print(response.json())  # Заголовки включены в ответ
client.close()

# 5. Работа с ошибками
# 5.1 Проверка статуса ответа (raise_for_status)
try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()  # Вызовет исключение при 4xx/5xx
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")

# 5.2 Обработка таймаутов
try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")
