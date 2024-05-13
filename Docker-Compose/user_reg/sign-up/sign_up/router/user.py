from typing import Annotated
from passlib.context import CryptContext
from fastapi import APIRouter, Depends
from sqlmodel import Session
from sign_up.db import get_session, User




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