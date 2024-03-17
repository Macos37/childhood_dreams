from sqlalchemy import Column, Integer, String
from src.database import Base
from sqlalchemy.orm import relationship


class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(100), nullable=False)