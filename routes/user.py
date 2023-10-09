from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from config.db import get_db
from schemas.user import *
from services.index import *

router = APIRouter(
    prefix='/apis',
    tags=["USER"]
)


@router.get("/users/list")
async def get_all(db: Session = Depends(get_db)):
    return get_user_all(db=db)


@router.get("/user/get/{id}")
async def get_byId(id: int, db: Session = Depends(get_db)):
    return get_user_byId(id=id, db=db)


@router.post("/user/add", status_code=status.HTTP_201_CREATED)
async def create(user: RequestUser, db: Session = Depends(get_db)):
    return create_user(user=user, db=db)


@router.put("/user/update/{id}")
async def update(id: int, user: RequestUser, db: Session = Depends(get_db)):
    return update_user(id=id, user=user, db=db)


@router.delete("/user/delete/{id}")
async def delete_user(id: int, db: Session = Depends(get_db)):
    return delete_user(id=id, db=db)
