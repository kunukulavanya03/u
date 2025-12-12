from sqlalchemy import create_engine
from app.config import settings
from app.models import Base

engine = create_engine(settings.DATABASE_URL)

Base.metadata.create_all(engine)