from app import models, schemas
from app.database import SessionLocal
from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import sessionmaker

pwd_context = CryptContext(schemes=['bcrypt'], default='bcrypt')

def get_user(db, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db):
    return db.query(models.User).all()


def get_user_by_username(db, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def create_user(db, user: schemas.UserCreate):
    db_user = models.User(username=user.username, email=user.email, password=pwd_context.hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db, db_user, user: schemas.UserUpdate):
    if user.username:
        db_user.username = user.username
    if user.email:
        db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db, db_user):
    db.delete(db_user)
    db.commit()


def get_user_by_username(db, username: str):
    return db.query(models.User).filter(models.User.username == username).first()