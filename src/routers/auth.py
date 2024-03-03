from fastapi.routing import APIRouter
from fastapi import Depends, Response
from src.schemas.auth import CreateAuthModel, AuthUserModel, AuthModel
from src.database import get_async_session
from sqlalchemy.orm import Session

from src.repositories.auth import AuthService

router = APIRouter(tags=["Auth router"])


@router.post('/auth', response_model=AuthModel)
async def auth(user: AuthUserModel, db: Session = Depends(get_async_session)):
    user_db = AuthService(db)
    auth_user = await user_db.get_user_auth(user)
    return auth_user


@router.post('/register')
async def register(user: CreateAuthModel, db: Session = Depends(get_async_session)):
    user_db = AuthService(db)
    created_user = await user_db.create(user)
    return created_user


@router.get('/logout', response_class=Response)
async def logout(
        response: Response,
) -> Response:
    response = Response()
    response.delete_cookie(key="jwt_token", httponly=True)
    return response
