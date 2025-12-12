from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from app.database import Session
from app.models import User
from app.settings import Settings
from passlib.context import CryptContext
from jose import jwt

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], default="bcrypt")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

@router.post("/auth/login")
def login(username: str, password: str):
    user = Session.query(User).filter_by(username=username).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    if not pwd_context.verify(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = jwt.encode({"sub": user.id}, Settings().SECRET_KEY, algorithm="HS256")
    return {"token": token, "user": user}

@router.post("/auth/register")
def register(name: str, email: str, password: str):
    user = Session.query(User).filter_by(email=email).first()
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = User(username=name, email=email, password=pwd_context.hash(password))
    Session.add(new_user)
    Session.commit()
    token = jwt.encode({"sub": new_user.id}, Settings().SECRET_KEY, algorithm="HS256")
    return {"token": token, "user": new_user}