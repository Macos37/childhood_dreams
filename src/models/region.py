from sqlalchemy import Column, ForeignKey, Integer, String
from src.database import Base
from sqlalchemy.orm import relationship
from src.models import Country


class Region(Base):
    __tablename__ = "regions"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(100), nullable=False)
    country_id = Column(Integer, ForeignKey("countries.id", 
                                            ondelete="CASCADE"))