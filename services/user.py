from fastapi import Depends
from sqlalchemy.orm import Session
from config.db import conn, get_db
from models.index import users
from schemas.index import *


# def create_user(user: , db: Session = Depends(get_db)):
#     db_user = users(
#         email=user.email,
#         username=user.username,
#         password=user.password,)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
