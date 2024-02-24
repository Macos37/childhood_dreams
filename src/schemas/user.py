from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict

class CityModel(BaseModel):
    id: int
    name: str
    
class ReadUserModel(BaseModel):
    id: int
    name: str
    surname: str
    phone: str
    city: Optional[CityModel] = None


class AuthUserModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    phone: str
    password: str


class CreateUserModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    surname: str = None
    email: str = None
    phone: str
    password: str


class UserModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    surname: str
    phone: str