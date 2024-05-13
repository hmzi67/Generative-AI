from fastapi import FastAPI
from sqlmodel import SQLModel
from contextlib import asynccontextmanager
from sign_up.router import user
from sign_up.db import engine

def create_tables():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Creating Tables')
    create_tables()
    print("Tables Created")
    yield

app: FastAPI = FastAPI(
    lifespan=lifespan, title="Sign up api", version='1.0.0')

@app.get('/')
def root():
    return "HEllo World"

app.include_router(router=user.router)