from pydantic import BaseModel,EmailStr

class UserRegisterIn(BaseModel):
    email: EmailStr
    password: str
    
class UserRegisterOut(BaseModel):
    id: int
    email: EmailStr
    username: str|None
    
class LoginIn(UserRegisterIn):
    pass
    
class LoginOut(BaseModel):
    refresh_token: str
    access_token: str
    token_type: str
    
class RefreshTokenIn(BaseModel):
    refresh_token: str
    
class AccessTokenOut(BaseModel):
    access_token: str
    token_type: str
    
    