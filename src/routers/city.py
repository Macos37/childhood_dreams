from fastapi.routing import APIRouter
from fastapi import Depends, Request, UploadFile, File
from src.schemas.user import UserModel, UpdateUserModel, ReadUserModel
from src.database import get_async_session
from sqlalchemy.orm import Session

from src.repositories.user import UserService
from src.services.depends.user import get_current_user