from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from config.db import conn, get_db
from models.index import users
from schemas.user import *
from services.index import *

router = APIRouter()


@router.get("/list")
async def read_user_all(db: Session = Depends(get_db)):
    rows = db.query(users).order_by(users.id.desc()).all()
    return rows


@router.get("/user/{id}")
async def read_user_byId(id: int, db: Session = Depends(get_db)):
    return db.query(users).filter(users.id == id).first()


@router.post("/add", status_code=status.HTTP_201_CREATED)
async def create_user(user: RequestUser, db: Session = Depends(get_db)):
    db_user = users(
        email=user.email,
        username=user.username,
        password=user.password,)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"status": "success", "data": db_user}


@router.put("/update/{id")
async def update_user(id: int, user: RequestUser, db: Session = Depends(get_db)):
    if id is None:
        raise HTTPException(status_code=400, detail="id is required")
    db_user = db.query(user).filter(user.id == id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.username = user.username
    db_user.email = user.email
    db_user.password = user.password
    db.commit()
    db.refresh(db_user)
    return db_user


@router.delete("/delete/{id")
async def delete_user(id: int, db: Session = Depends(get_db)):
    conn.execute(users.delete().where(users.c.id == id))

    return conn.execute(users.select()).fetchall()
