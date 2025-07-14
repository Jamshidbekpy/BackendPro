from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: int
    description: str
    price: int
    is_active: bool

class ProductInfo(ProductCreate):
    id: int
    name: str
    class Config:
        orm_mode = True
        
    

        
    