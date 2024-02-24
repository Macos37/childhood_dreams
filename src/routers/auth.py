from fastapi.routing import APIRouter
from fastapi import Depends, Response
from fastapi.security import OAuth2PasswordBearer
from src.schemas.user import CreateUserModel, AuthUserModel, UserModel
from src.database import get_async_session
from sqlalchemy.orm import Session

from src.repositories.auth import AuthService

router = APIRouter(tags=["Auth router"])


@router.post('/auth')
async def auth(user: AuthUserModel, db: Session = Depends(get_async_session)):
    user_db = AuthService(db)
    auth_user = await user_db.get_user_auth(user)
    return auth_user


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth")


@router.post('/register', response_model=UserModel)
async def register(user: CreateUserModel, db: Session = Depends(get_async_session)):
    user_db = AuthService(db)
    created_user = await user_db.create(user)
    return created_user


@router.get('/logout', response_class=Response)
async def logout(
        response: Response,
) -> Response:
    response = Response()
    response.delete_cookie(key="jwt_token", httponly=True, secure=True)
    return response
