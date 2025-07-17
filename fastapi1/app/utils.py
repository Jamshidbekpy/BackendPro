import os
from pathlib import Path
from dotenv import load_dotenv
from fastapi import HTTPException
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta,UTC

load_dotenv(dotenv_path=Path(__name__).resolve().parent / ".env")
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


#ALGORITHM, SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES, PAYLOAD
def create_jwt_token(data: dict, expires_delta: float | None = None):
    """
    - Creates a new JWT token for logging-in user
    """

    # Access tokenni nima bilan generatsiya qilaman?
    # Access token qanaqa token o'zi?
    delta = (
        timedelta(minutes=expires_delta)
        if expires_delta
        else timedelta(days=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    expire_time = datetime.now(UTC) + delta
    data.update({"exp": expire_time})

    # data = {"username": <>, "password": <>, "role": <>, "exp": <>}

    jwt_token = jwt.encode(data, SECRET_KEY, ALGORITHM)

    return jwt_token


def get_new_access_token(refresh: str):
    try:
        payload = jwt.decode(refresh, SECRET_KEY, algorithms=[ALGORITHM])
        if payload.get("type") != "refresh":
            raise HTTPException(status_code=401, detail="Invalid token type")

        user_id = payload.get("user_id")
        new_access_token = create_jwt_token(
            data={
                "user_id": user_id,
                "type": "access"
            },
            expires_delta=ACCESS_TOKEN_EXPIRE_MINUTES
        )
        return {"access_token": new_access_token, "token_type": "bearer"}

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
