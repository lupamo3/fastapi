
from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import settings


# Connect to the PostgreSQL database
engine = create_engine(settings.DATABASE_URL)
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)


Base = declarative_base()
# Base.metadata.create_all(engine)


def get_db():
    # Instantiating the local database session, which is a dependency
    session = Session()
    try:
        yield session
    finally:
        session.close()