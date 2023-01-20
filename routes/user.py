from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config.db import get_db
from models.index import users
from schemas.user import *
from services.index import *

router = APIRouter(
    prefix='/api',
    tags=["USER"]
)


@router.get("/users/list")
async def read_user_all(db: Session = Depends(get_db)):
    return user_all(db=db)


@router.get("/user/get/{id}")
async def read_user_byId(id: int, db: Session = Depends(get_db)):
    return db.query(users).filter(users.id == id).first()


@router.post("/user/add", status_code=status.HTTP_201_CREATED)
async def create_user(user: RequestUser, db: Session = Depends(get_db)):
    db_user = users(
        email=user.email,
        username=user.username,
        password=user.password,)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"status": "success", "data": db_user}


@router.put("/user/update/{id}")
async def update_user(id: int, user: RequestUser, db: Session = Depends(get_db)):
    if id is None:
        raise HTTPException(status_code=400, detail="id is required")
    db_user = db.query(users).filter(users.id == id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail=f'User id {id} not found')
    if db.query(users).filter(users.email == user.email).first() and user.email != db_user.email:
        raise HTTPException(status_code=400, detail="Email already exists")
    db_user.username = user.username
    db_user.email = user.email
    db_user.password = user.password
    db_user.role = user.role
    db.commit()
    db.refresh(db_user)
    return {"status": "success", "data": db_user}


@router.delete("/user/delete/{id}")
async def delete_user(id: int, db: Session = Depends(get_db)):
    if id is None:
        raise HTTPException(status_code=400, detail="id is required")
    db_user = db.query(users).filter(users.id == id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail=f'User id {id} not found')
    db.delete(db_user)
    db.commit()
    return {"status": "success"}
