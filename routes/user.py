from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.db import conn, get_db
from models.index import users
from schemas.index import User

user = APIRouter()


@user.get("/list")
async def read_data(db: Session = Depends(get_db)):
    rows = db.query(users).order_by(users.id.desc()).all()
    return rows


@user.get("/user/{id}")
async def read_data(id: int, db: Session = Depends(get_db)):
    return conn.execute(users.select().where(users.c.id == id).fetchall())


@user.post("/add", response_model=users)
async def write_data(user: User, db: Session = Depends(get_db)):
    db_user = users(username=user.username,
                    email=user.email,
                    password=user.password,)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@user.put("/update/{id")
async def update_data(id: int, user: User, db: Session = Depends(get_db)):
    conn.execute(user.update().values(
        username=user.username,
        email=user.email,
        password=user.password,
    ).where(user.c.id == id))

    return conn.execute(users.select()).fetchall()


@user.delete("/delete/{id")
async def delete_data(id: int, db: Session = Depends(get_db)):
    conn.execute(users.delete().where(users.c.id == id))

    return conn.execute(users.select()).fetchall()
