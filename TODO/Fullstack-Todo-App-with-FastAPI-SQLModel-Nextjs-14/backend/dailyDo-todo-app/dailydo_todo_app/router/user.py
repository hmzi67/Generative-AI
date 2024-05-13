from fastapi import APIRouter, Depends
from dailydo_todo_app.db import get_session
from dailydo_todo_app.db import User
from typing import Annotated
from sqlmodel import Session
from passlib.context import CryptContext

router = APIRouter(
    prefix='/user'
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.get("/user/")
def user_root():
    return {"User"}

@router.post("/user/register")
def create_user(user: User, session: Annotated[Session, Depends(get_session)]):
    # hashPassword = pwd_context.hash(user.password)
    # newUser = User(email=user.email, password=hashPassword)
    # session.add(newUser)

    user.password = pwd_context.hash(user.password)
    session.add(user)
    session.commit()
    session.refresh(user)
    return {"message": f"${user.email} successfully registered" }