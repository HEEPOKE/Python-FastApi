from fastapi import Depends
from sqlalchemy.orm import Session
from config.db import get_db
from models.index import users
from schemas.index import *


def user_all(db: Session = Depends(get_db)):
    rows = db.query(users).order_by(users.id.desc()).all()
    return {"status": "success", "data": rows}
