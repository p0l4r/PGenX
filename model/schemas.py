from typing import List, Optional
from pydantic import BaseModel


class ItemBase(BaseModel):
    random_password: Optional[str] = None
    user_name_or_email: str
    website_name: str


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []
    class Config:
        orm_mode = True
