from datetime import datetime, timedelta
import bcrypt
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy import select, or_
from src.repositories.abstract_items import AbstractItemService
from src.models.user import User
from src.schemas.auth import AuthUserModel, AuthModel, CreateAuthModel
import re
from jose import jwt
from config import SECRET_KEY,ALGORITHM


class AuthService(AbstractItemService):

    def __init__(self, session) -> None:
        self.session = session

    def get_by_id(self, user_id: int) -> AuthModel:
        pass

    async def get_user_auth(self, data: AuthUserModel):
        db_user = await self.session.execute(
            select(User).where(User.phone == data.phone))
        db_user = db_user.scalars().first()
        if db_user and bcrypt.checkpw(data.password.encode('utf-8'),
                                      db_user.hash_password.encode('utf-8')):
            expiration = datetime.utcnow() + timedelta(minutes=60)
            token = {
                'sub': db_user.id,
                'phone': db_user.phone,
                'exp': expiration
            }
            token = jwt.encode(token, SECRET_KEY, algorithm=ALGORITHM)
            content = {'token': token}
            response = JSONResponse(content=content)
            response.set_cookie(key='jwt_token',
                                value=token,
                                httponly=True,
                                samesite='lax')
            return response

        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Вы ввели неправильные данные")

    async def create(self, data: CreateAuthModel) -> AuthModel:
        self.validate_data(data)
        user = await self.session.execute(
            select(User).where(or_(User.phone == data.phone, 
                                   User.email == data.email))
        )
        user = user.scalars().first()
        if user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Пользователь с такими данными уже существует"
            )

        hashed_password = bcrypt.hashpw(data.password.encode('utf-8'),
                                        bcrypt.gensalt()).decode('utf-8')
        db_user = User(
            name=data.name,
            surname=data.surname,
            email=data.email,
            phone=data.phone,
            hash_password=hashed_password
        )
        self.session.add(db_user)
        await self.session.commit()
        await self.session.refresh(db_user)
        return db_user

    def update(self, data: AuthModel) -> AuthModel:
        pass

    def delete(self, user_id: int) -> None:
        pass

    def get_all(self) -> list[AuthModel]:
        pass

    def validate_data(self, data: CreateAuthModel) -> bool:
        if not data.surname and not data.name and not data.phone:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Необходимо указать имя, фамилию и телефон"
            )

        phone = re.match(r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$', 
                         data.phone)
        if not phone:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Некорректный номер телефона"
            )

        if len(data.password) < 5:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Пароль должен содержать не менее 6 символов"
            )

        return True
