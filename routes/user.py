from fastapi import APIRouter
from config.db import conn
from models.index import *

user = APIRouter()

@user.get("/list")
async def read_data():
    return conn.execute(user.select()).fetchall()