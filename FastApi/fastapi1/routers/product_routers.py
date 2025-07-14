from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import Product
from main import db_dependency

router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def products(db: Session = Depends(get_db)):
    return db.query(Product).all()