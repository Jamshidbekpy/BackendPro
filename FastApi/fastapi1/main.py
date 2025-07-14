from fastapi import FastAPI, Depends, APIRouter

from db import engine, Base, SessionLocal
from models import User
from typing import Annotated
from sqlalchemy.orm import Session


app = FastAPI()
