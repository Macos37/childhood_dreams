from fastapi.routing import APIRouter
from fastapi import Depends, Request, UploadFile, File
from src.schemas.user import UserModel, UpdateUserModel, ReadUserModel
from src.database import get_async_session
from sqlalchemy.orm import Session

from src.repositories.user import UserService
from src.services.depends.user import get_current_user


router = APIRouter(
    prefix='/user',
    tags=["User router"])


@router.get('/me', response_model=UserModel)
async def get_user(request: Request, user: ReadUserModel = Depends(get_current_user),
                   db: Session = Depends(get_async_session)):
    user_db = UserService(db)
    user = await user_db.get_me(user)
    return user


@router.put('/me', response_model=UserModel)
async def update_user(update_user: UpdateUserModel, phone: str = Depends(get_current_user),
                      db: Session = Depends(get_async_session)):
    user_db = UserService(db)
    updated_user = await user_db.update(update_user, phone)
    return updated_user


@router.get('/id{user_id}', response_model=UserModel)
async def get_by_id(user_id: int, db: Session = Depends(get_async_session),
                    phone: str = Depends(get_current_user)):
    user_db = UserService(db)
    user = await user_db.get_by_id(user_id)
    return user


@router.put('/me/photo', response_model=UserModel)
async def update_photo_user(
    phone: str = Depends(get_current_user),
    photo: UploadFile = File(...),
        db: Session = Depends(get_async_session)):
    user_db = UserService(db)
    updated_photo = await user_db.update_photo(phone, photo)
    return updated_photo

