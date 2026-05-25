
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

# Default to a local SQLite database for simplicity and testing
SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./test.db")

if SQLALCHEMY_DATABASE_URL.startswith("postgres"):
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
else:
    # SQLite requires a specific connect_args setting for FastAPI
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
