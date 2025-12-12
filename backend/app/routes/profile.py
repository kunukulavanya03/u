from fastapi import APIRouter, Depends
from app.config import settings
from app.models import User
from app.utils import get_user

router = APIRouter()

@router.get("/profile")
def get_profile(user: User = Depends(get_user)):
    return {"user_id": user.id, "username": user.username, "email": user.email}