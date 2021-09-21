from sqlalchemy.orm import Session
from model import db_model, schemas
from logic.pgenx import PGenX


def get_user(db: Session, user_id: int):

    return db.query(db_model.User).filter(db_model.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):

    return db.query(db_model.User).filter(db_model.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):

    return db.query(db_model.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "*37#"
    db_user = db_model.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):

    return db.query(db_model.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    item.random_password = PGenX().password_generator()
    db_item = db_model.Item(random_password=item.random_password,user_name_or_email= item.user_name_or_email,
                            website_name=item.website_name, owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
