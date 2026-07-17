import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker , Session
from collections.abc import Generator

load_dotenv()


db_url:str = os.getenv("DATABASE_URL")  # pyright: ignore[reportAssignmentType]


engine = create_engine(db_url)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
def get_db() -> Generator[Session, None, None]:

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

class Base(DeclarativeBase):
    pass
