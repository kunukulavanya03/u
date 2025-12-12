from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from app.config import settings
from app.models import User
from pydantic import BaseModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

async def get_user(token: str = Depends(oauth2_scheme)):
    user_id = get_user_id_from_token(token)
    user = User.query.get(user_id)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user

def get_password_hash(password: str):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())