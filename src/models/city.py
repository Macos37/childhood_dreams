from sqlalchemy import Column, ForeignKey, Integer, String
from src.database import Base
from sqlalchemy.orm import relationship


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(100), nullable=False)
    region_id = Column(Integer, ForeignKey("regions.id", ondelete="CASCADE"))
    users = relationship("User", back_populates="cities")