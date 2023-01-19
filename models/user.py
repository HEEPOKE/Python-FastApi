from sqlalchemy import Table, Column, Integer, String
from config.db import meta

users = Table(
    'users', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('username', String, unique=True),
    Column('email', String),
    Column('password', String),
)
