import logging
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.schemas.user import UserModel
from src.models.user import User

logger = logging.getLogger(__name__)


async def get_by_phone(phone: str, db: Session) -> UserModel:
    user = await db.execute(select(User).where(User.phone == phone))
    user = user.scalars().first()
    user = UserModel.model_validate(user)
    return user