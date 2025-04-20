from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from app.config import settings
from fastapi import Depends

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency para obtener una sesión de base de datos
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
