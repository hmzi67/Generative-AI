from fastapi import FastAPI
from sqlmodel import SQLModel, Field
from contextlib import asynccontextmanager

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, min_length=3, max_length=22)
    email: str = Field(min_length=11, max_length=54)
    password: str = Field(min_length=8)


# When app with start then
@asynccontextmanager
async def lifeSpan(app: FastAPI):
    print("Creating Tables in Database")
    yield

app: FastAPI = FastAPI(
    lifespan= lifeSpan,
    title= "User Registration API",
    version= "1.0",
    servers= [
        {
            "url": "http://0.0.0.0:8000", # ADD NGROK URL Here Before Creating GPT Action
            "description": "Development Server"
        }
    ]
)

@app.get('/')
def root():
    return{
        "Message": "Welcome to sign up api"
    }

@app.post('/sign-up')
async def register_user():
   return {"Post": "Product"}



