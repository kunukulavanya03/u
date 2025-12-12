from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from app.settings import Settings

engine = create_engine(Settings().DATABASE_URL)
Base = declarative_base()
Session = scoped_session(sessionmaker(bind=engine))