from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from src.database import Base
from sqlalchemy_utils.types.url import URLType
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String)
    price = Column(String, nullable=False, default='Бесплатно')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    image = relationship("Image", back_populates="products")
    users = relationship("User", back_populates="products")

class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"))
    image_url = Column(URLType, nullable=False)

    products = relationship("Product", back_populates="image")
