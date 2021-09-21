'''
This module contains the database model.
'''

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


from model.database import Base




class User(Base):

    __tablename__ = "users"


    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")



class Item(Base):

    __tablename__ = "items"


    id = Column(Integer, primary_key=True, index=True)
    random_password = Column(String, index=True)
    user_name_or_email = Column(String, index=True)
    website_name = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
