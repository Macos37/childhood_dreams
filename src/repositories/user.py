from datetime import datetime, timedelta
import bcrypt
from pydantic import ValidationError
from fastapi import File, HTTPException, UploadFile, status
from fastapi.responses import JSONResponse
from sqlalchemy import select, or_, update
from src.repositories.abstract_items import AbstractItemService
from src.models.user import User
from src.schemas.user import UserModel, UpdateUserModel, ReadUserModel
from src.services.depends.user import get_current_user


class UserService(AbstractItemService):

    def __init__(self, session):
        self.session = session

    async def get_by_id(self, user_id: int) -> UserModel:
        user = self.session.execute(select(User).where(User.id == user_id))
        user = user.scalars().first()
        if user:
            return user
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Пользователь не найден")

    def create(self, data: UserModel) -> UserModel:
        pass

    async def update(self, 
                     data: UpdateUserModel, 
                     user: UserModel,
                     ) -> UserModel:
        #TODO load photo: UploadFile = File(...)
        data = data.model_dump(exclude_none=True)
        try:
            UpdateUserModel.model_validate(data)
        except ValidationError as e:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=e.errors()
            )
        update_query = update(User).filter(User.phone == user.phone).values(
            data
        ).returning(
            User
        )

        result = await self.session.execute(update_query)
        result = result.scalars().first()
        await self.session.commit()

        return UserModel.model_validate(result)

    def delete(self, user_id: int) -> None:
        pass

    def get_all(self) -> list[UserModel]:
        pass