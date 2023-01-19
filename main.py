from fastapi import FastAPI
from routes.index import *

app = FastAPI()

app.include_router(user)
