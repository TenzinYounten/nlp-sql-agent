# app/db/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"charset": "utf8mb4"}
)
SessionLocal = sessionmaker(bind=engine)