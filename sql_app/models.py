from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from sql_app.database import Base

class User(Base):
    __tablename__ ="users"

    id = Column(Integer, primary_key=True, index = True)
    email = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(50))
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index= True)
    description = Column(String(50), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User",back_populates="items")