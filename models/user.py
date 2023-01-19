from sqlalchemy import Table, Column, Integer, String, Enum
from config.db import meta
import enum


class Role(str, enum.Enum):
    admin = "Admin"
    user = "User"


users = Table(
    'users', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('username', String, unique=True),
    Column('email', String),
    Column('password', String),
    Column('role', Enum(Role), default=Role.user),
)
