from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from config.db import get_db
from models.index import users
from schemas.index import *


def get_user_all(db: Session = Depends(get_db)):
    rows = db.query(users).order_by(users.id.asc()).all()
    return {"status": "success", "payload": rows}


def get_user_byId(id: int, db: Session = Depends(get_db)):
    rows = db.query(users).filter(users.id == id).first()
    return {"status": "success", "payload": rows}


def create_user(user: RequestUser, db: Session = Depends(get_db)):
    payload = users(
        email=user.email,
        username=user.username,
        password=user.password,)
    db.add(payload)
    db.commit()
    db.refresh(payload)
    return {"status": "success", "data": payload}

def update_user(id: int, user: RequestUser, db: Session = Depends(get_db)):
    if id is None:
        raise HTTPException(status_code=400, detail="id is required")
    payload = db.query(users).filter(users.id == id).first()
    if payload is None:
        raise HTTPException(status_code=404, detail=f'User id {id} not found')
    if db.query(users).filter(users.email == user.email).first() and user.email != payload.email:
        raise HTTPException(status_code=400, detail="Email already exists")
    payload.username = user.username
    payload.email = user.email
    payload.password = user.password
    payload.role = user.role
    db.commit()
    db.refresh(payload)
    return {"status": "success", "payload": payload}

def delete_user(id: int, db: Session = Depends(get_db)):
    if id is None:
        raise HTTPException(status_code=400, detail="id is required")
    payload = db.query(users).filter(users.id == id).first()
    if payload is None:
        raise HTTPException(status_code=404, detail=f'User id {id} not found')
    db.delete(payload)
    db.commit()
    return {"status": "success"}