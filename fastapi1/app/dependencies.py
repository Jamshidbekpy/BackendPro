import os
from pathlib import Path
from dotenv import load_dotenv
from fastapi import Depends
from typing import Annotated
from app.database import SessionLocal
from sqlalchemy.orm import Session
from fastapi import Request, HTTPException
from app.models import User
from jose import jwt, JWTError

load_dotenv(dotenv_path=Path(__name__).resolve().parent / ".env")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]



SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

def get_current_user(
    request: Request,
    db: db_dependency
):
    auth_header = request.headers.get("Authorization")
    is_bearer = auth_header.startswith("Bearer") if auth_header else False
    token = auth_header.split(" ")[1] if is_bearer else ""

    if not auth_header or not is_bearer:
        raise HTTPException(
            status_code=401,
            detail="You are not authenticated."
        )

    try:
        decoded_jwt = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        if decoded_jwt.get("type") != "access":
            raise HTTPException(status_code=401, detail="Invalid token.")
        
        user_id = decoded_jwt.get("user_id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token.")

        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found.")

        return db_user

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token."
        )

current_user_dependency = Annotated[User, Depends(get_current_user)]