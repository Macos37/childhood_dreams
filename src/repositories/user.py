from datetime import datetime, timedelta
import os
import bcrypt
import aiofiles
from pydantic import ValidationError
from fastapi import File, HTTPException, UploadFile, status
from sqlalchemy import select, or_, update
from src.repositories.abstract_items import AbstractItemService
from src.models.user import User
from src.schemas.user import UserModel, UpdateUserModel, ReadUserModel
from src.services.validate.validate_photo import validate_file_size_type


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

    async def update_photo(self, 
                           user: UserModel,
                           photo: UploadFile = File(...)) -> UserModel:
        validate_file_size_type(photo)
        path_img = '/static/photo_user/'
        user_folder_path = f"{os.getcwd()}{path_img}"
        data = {"photo": path_img + photo.filename}
        update_query = update(User).filter(User.phone == user.phone).values(
            data
        ).returning(
            User
        )

        async with aiofiles.open(user_folder_path + photo.filename, "wb")as buffer:
            buffer.write(await photo.read())

        result = await self.session.execute(update_query)
        result = result.scalars().first()
        await self.session.commit()
        return UserModel.model_validate(result)