import re
from pydantic import BaseModel, ConfigDict, EmailStr, validator


class ReadUserModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    surname: str
    email: EmailStr | None
    city: str | None
    phone: str


class UpdateUserModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    surname: str
    email: EmailStr | None
    #phone: str
    #password: str
    
    @validator('name', 'surname')
    def check_name(cls, value):
        if not value or re.search(r'[a-zA-Z]', value):
            raise ValueError("Field 'name' should not contain English letters")
        return value


class UserModel(ReadUserModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    
    # @model_validator(mode='after')
    # def check_email(cls, values):
    #     email = values.get('email')
    #     if email and 'example.com' in email:
    #         raise ValueError("Email must not contain 'example.com'")
    #     return values
