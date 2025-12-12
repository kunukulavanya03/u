from fastapi import FastAPI
from dotenv import load_dotenv
from app.config import settings
from app.routes import auth_routes, profile_routes, resource_routes

load_dotenv()
app = FastAPI()

app.include_router(auth_routes.router)
app.include_router(profile_routes.router)
app.include_router(resource_routes.router)