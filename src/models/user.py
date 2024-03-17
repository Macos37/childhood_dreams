from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from src.database import Base
from sqlalchemy_utils.types.url import URLType
from sqlalchemy.orm import relationship
from src.models.product import Product
from src.models.city import City


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)
    email = Column(String, unique=True)
    phone = Column(String, unique=True, nullable=False)
    city_id = Column(Integer, ForeignKey("cities.id", ondelete="CASCADE"))
    address = Column(String(255))
    hash_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    photo = Column(URLType, nullable=True,
                   default='/static/photo_user/avatar_default.png')

    products = relationship("Product", back_populates="users")
    cities = relationship("City", back_populates="users")