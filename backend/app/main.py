from fastapi import FastAPI
from app.database import engine
from app.routers import auth, users, items
from app.settings import Settings

app = FastAPI()

@app.on_event("startup")
def startup_event():
    engine.connect()

@app.on_event("shutdown")
def shutdown_event():
    engine.dispose()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(items.router)