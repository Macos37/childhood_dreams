from fastapi.routing import APIRouter
from fastapi import Depends, Request, Response, UploadFile, File
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
    print('===============')
    print('user', user)
    print(type(user))
    print('===============')
    return user


@router.put('/me', response_model=UserModel)
async def update_user(update_user: UpdateUserModel, phone: str = Depends(get_current_user),
                      db: Session = Depends(get_async_session)):
    user_db = UserService(db)
    updated_user = await user_db.update(update_user, phone)
    return updated_user


@router.put('/me/photo', response_model=UserModel)
async def update_photo_user(
    phone: str = Depends(get_current_user),
    photo: UploadFile = File(...),
        db: Session = Depends(get_async_session)):
    user_db = UserService(db)
    updated_photo = await user_db.update_photo(phone, photo)
    return updated_photo

# @router.delete('/me', response_model=UserModel)
# async def delete_user(db: Session = Depends(get_async_session)):
#     user_db = UserService(db)
#     deleted_user = await user_db.delete()
#     return deleted_user


# @router.get('/all', response_model=list[UserModel])
# async def getall_user(db: Session = Depends(get_async_session)):
#     user_db = UserService(db)
#     users = await user_db.get_all()
#     return users


# @router.get('/{user_id}', response_model=UserModel)
# async def get_by_id(user_id: int, db: Session = Depends(get_async_session)):
#     user_db = UserService(db)
#     user = await user_db.get_by_id(user_id)
#     return user
