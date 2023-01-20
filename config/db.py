from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

DATABASE_URL = "mysql+pymysql://root@127.0.0.1:3306/fastapi"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
meta = MetaData()
Base.metadata.create_all(bind=engine)
conn = engine.connect()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
