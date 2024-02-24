from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from src.database import Base
from sqlalchemy_utils.types.url import URLType


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)
    email = Column(String, unique=True)
    phone = Column(String, unique=True, nullable=False)
    photo = Column(String)
    city = Column(Integer, ForeignKey("cities.id", ondelete="CASCADE"))
    hash_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)


class UserPhoto(Base):
    __tablename__ = "user_photos"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    photo_url = Column(URLType, nullable=False)
