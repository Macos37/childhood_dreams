from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic import BaseModel, ConfigDict


class AuthUserModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    phone: str
    password: str


class CreateAuthModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    surname: str
    phone: str
    email: EmailStr | None
    password: str


class AuthModel(AuthUserModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    surname: str
    phone: str