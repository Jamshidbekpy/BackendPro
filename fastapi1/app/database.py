import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import DateTime, func
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path=Path(__name__).resolve().parent / ".env")

DATABASE_URL = os.getenv("DATABASE_URL")

# engine = create_engine(url=DATABASE_URL, connect_args={"check_same_thread": False}, echo=True)
engine = create_engine(url=DATABASE_URL, echo=True)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SessionLocal = sessionmaker(autocommit=False, bind=engine)


class Base(DeclarativeBase):
    pass


class TimestampMixin:
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now()
    )
