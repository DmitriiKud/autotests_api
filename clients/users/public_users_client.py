from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient


class CreateUserDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """

    def create_user_api(self, request: CreateUserDict) -> Response:
        """
        Метод для создания пользователя.

        :param request: Словарь с телом для создания пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)
