from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import SQLModel, Field, create_engine, Session
from sign_up import setting
from contextlib import asynccontextmanager
from typing import Annotated

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, min_length=3, max_length=22)
    email: str = Field(min_length=11, max_length=54)
    password: str = Field(min_length=8)

# creating engine
# engine is one for whole application
connection_string: str = str(setting.DATABASE_URL).replace("postgresql", "postgresql+psycopg") 
engine = create_engine(connection_string, connect_args= {"sslmode": "require"}, pool_recycle=300, pool_size=8) 

# Creating Tables
async def create_table():
    SQLModel.metadata.create_all(engine)

# Creating generator function
def get_session():
    with Session(engine) as session:
        yield session

# When app with start then
@asynccontextmanager
async def lifeSpan(app: FastAPI):
    print("Creating Tables in Database")
    create_table()
    print("Tables are created successfully")
    yield

app: FastAPI = FastAPI(
    lifespan= lifeSpan,
    title= "User Registration API",
    version= "1.0",
    servers= [
        {
            "url": "http://127.0.0.0:8000", # ADD NGROK URL Here Before Creating GPT Action
            "description": "Development Server"
        }
    ]
)

@app.get('/')
def root():
    return({
        "Message": "Welcome to sign up api"
    })

@app.post('/sign-up', response_model= User)
async def register_user(user: User, session: Annotated[Session, Depends(get_session)]):
    # Creating User
    session.add(user)
    session.commit()
    session.refresh(user)
    if user:
        return user
    else:
        return HTTPException(status_code= 404, detail= "No user found")



