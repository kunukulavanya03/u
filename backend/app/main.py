from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from app import models, schemas, crud, database, settings
from app.database import SessionLocal, engine
from sqlalchemy.orm import sessionmaker
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext
from app.dependencies import get_db

app = FastAPI()

pwd_context = CryptContext(schemes=['bcrypt'], default='bcrypt')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

@app.on_event('startup')
async def startup_event():
    await database.database_connect()

@app.on_event('shutdown')
async def shutdown_event():
    await database.database_disconnect()

@app.get('/health')
def get_health():
    return {'status': 'ok', 'timestamp': datetime.now().isoformat()}

@app.post('/token', response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = crud.user.get_user_by_username(form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail='Incorrect username or password')
    if not pwd_context.verify(form_data.password, user.password):
        raise HTTPException(status_code=400, detail='Incorrect username or password')
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = jwt.encode({'sub': user.username, 'exp': datetime.utcnow() + access_token_expires}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return {'access_token': access_token, 'token_type': 'bearer'}

@app.get('/users', response_model=schemas.Users)
def get_users(db: SessionLocal = Depends(get_db), token: str = Depends(oauth2_scheme)):
    users = crud.user.get_users(db)
    return {'users': users, 'total': len(users)}

@app.post('/users', response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: SessionLocal = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_user = crud.user.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail='Username already registered')
    return crud.user.create_user(db, user)

@app.get('/users/{user_id}', response_model=schemas.User)
def get_user(user_id: int, db: SessionLocal = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_user = crud.user.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return db_user

@app.put('/users/{user_id}', response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserUpdate, db: SessionLocal = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_user = crud.user.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return crud.user.update_user(db, db_user, user)

@app.delete('/users/{user_id}')
def delete_user(user_id: int, db: SessionLocal = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_user = crud.user.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')
    crud.user.delete_user(db, db_user)
    return {'message': 'User deleted'}