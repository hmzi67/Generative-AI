from fastapi import APIRouter, Depends
from user_reg.db import Users, get_session
from typing import Annotated
from sqlmodel import Session
from passlib.context import CryptContext

router = APIRouter(
    prefix='/user'
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.get('/user/')
def user_root():
    return {
        'user': 'Hamza Waheed'
    }

@router.post('/user/signup')
def register_user(user:Users, session: Annotated[Session, Depends(get_session)]):
    user.password = pwd_context.hash(user.password)
    session.add(user)
    session.commit()
    session.refresh(user)
    return {
        "Message": f"{user.email} successfuly registered"
    }