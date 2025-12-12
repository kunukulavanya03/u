from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from app.database import Session
from app.models import User
from app.routers.auth import oauth2_scheme

router = APIRouter()

@router.get("/users")
def get_users(token: str = Depends(oauth2_scheme)):
    users = Session.query(User).all()
    return {"users": users}

@router.get("/users/{id}")
def get_user(id: int, token: str = Depends(oauth2_scheme)):
    user = Session.query(User).filter_by(id=id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": user}