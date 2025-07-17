import os
from pathlib import Path
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from app.dependencies import db_dependency, current_user_dependency
from app.schemas.auth_schemas import UserRegisterIn, UserRegisterOut, LoginIn, LoginOut, RefreshTokenIn, AccessTokenOut
from app.models import User
from app.utils import hash_password, verify_password, create_jwt_token, get_new_access_token
router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)
load_dotenv(dotenv_path=Path(__name__).resolve().parent / ".env")

REFRESH_TOKEN_EXPIRE_MINUTES = int(os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES"))
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
@router.post("/register/", response_model = UserRegisterOut)
async def register(db:db_dependency, user_in: UserRegisterIn):
    user = User(
        email = user_in.email,
        hashed_password = hash_password(user_in.password),
    )
    
    is_user_exist = db.query(User).count()
    
    if not is_user_exist:
        user.is_admin = True

    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user
    

@router.post("/login/", response_model=LoginOut)
async def login(db:db_dependency, user_in: LoginIn):
    user = db.query(User).filter(User.email == user_in.email).first()
    
    if not user:
        raise HTTPException(
            status_code=404, 
            detail="User not found"
        )
    # print(verify_password(user_in.password, user.hashed_password), "##########################")
    if not verify_password(user_in.password, user.hashed_password):
        raise HTTPException(
            status_code=403,
            detail="Invalid password"
        )
    
    access_token = create_jwt_token(
        data = {
            "user_id":user.id,
            "expires_delta":ACCESS_TOKEN_EXPIRE_MINUTES,  
            "type":"access"
    }
        )
    refresh_token = create_jwt_token(
        data = {
            "user_id":user.id,
            "expires_delta":REFRESH_TOKEN_EXPIRE_MINUTES,
            "type":"refresh"
        }
    )
    
    return {
        "refresh_token": refresh_token,
        "access_token": access_token,
        "token_type": "bearer"
    }
    
       
@router.post("/refresh/", response_model=AccessTokenOut)
def refresh_token(refresh_token: RefreshTokenIn):
    new_access = get_new_access_token(refresh_token.refresh_token)
    
    return new_access

@router.post("/logout/")
async def logout():
    pass


@router.get("/me/", response_model=UserRegisterOut)
async def me(current_user:current_user_dependency):
    return current_user

