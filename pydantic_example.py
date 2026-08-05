from pydantic import BaseModel


class Address(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address  # Вложенная модель

class ShortUserSchema(BaseModel):
    id: str
    email: str

class FullUserSchema(ShortUserSchema):
    last_name: str
    first_name: str
    middle_name: str

user = User(id=1, name="Alice", address={"city": "New York", "zip_code": "10001"})
print(user.address.city)  # "New York"

