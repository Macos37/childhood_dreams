from datetime import datetime
import re
from pydantic import BaseModel, ConfigDict, EmailStr, validator
from typing import Optional


class ReadUserModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    surname: str
    city_id: Optional[int] = None
    email: Optional[EmailStr] = None
    city: Optional[str] = None
    phone: str


class UpdateUserModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: Optional[str] = None
    surname: Optional[str] = None
    email: Optional[EmailStr] = None
    city_id: Optional[int] = None
    #phone: str
    #password: str

    @validator('name', 'surname')
    def check_name(cls, value):
        if not value or re.search(r'[a-zA-Z]', value):
            raise ValueError("Данное поле не должно содержать латинские буквы")
        return value

    # @validator('phone')
    # def check_phone(cls, value):
    #     if not value or re.match(r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$', value):
    #         raise ValueError("Некорректный номер телефона")
    #     return value


class UserModel(ReadUserModel):
    id: int
    photo: str
    created_at: datetime
