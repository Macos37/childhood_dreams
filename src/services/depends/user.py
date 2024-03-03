from fastapi import HTTPException, status, Request , Depends
import jwt
from pytest import Session
from config import SECRET_KEY, ALGORITHM
from src.database import get_async_session
from src.schemas.user import UserModel
from src.repositories.misc.user import get_by_phone


async def get_current_user(request: Request,
                           db: Session = Depends(get_async_session)) -> UserModel:
    
    token = request.cookies.get("jwt_token")
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        phone: int = payload.get("phone")
        if phone is None:
            raise credentials_exception
        return await get_by_phone(phone=phone, db=db)
    except jwt.ExpiredSignatureError:
        raise credentials_exception
    except Exception as e:
        credentials_exception
        # raise HTTPException(
        #     status_code=status.HTTP_401_UNAUTHORIZED,
        #     detail=e.errors()
        # )