from fastapi import FastAPI
from sqlmodel import SQLModel
from contextlib import asynccontextmanager
from reg.db import engine
from reg.router import user_route

def create_tables():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables ...")
    create_tables()
    print("Tables created successfully")

app = FastAPI(
    lifespan= lifespan,
    title= "Sign up",
    version="1.0.0"
)

@app.get('/')
def root():
    return "HEllo World"

app.include_router(router=user_route.router)