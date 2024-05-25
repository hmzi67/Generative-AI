from typing import Annotated
from passlib.context import CryptContext
from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db import get_session, User
from aiokafka import AIOKafkaProducer
import json

# Step 1: Import the generated protobuf code - Review todo post api route next.
from app import user_pb2

router = APIRouter(
    prefix='/user'
)

async def get_kafka_producer():
    producer = AIOKafkaProducer(bootstrap_servers= 'broker:19092')
    await producer.start()
    try:
        yield producer
    finally:
        await producer.stop()
    

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.get("/user/")
def user_root():
    return {"User"}

@router.post("/user/register", response_model= User)
async def create_user(user: User, session: Annotated[Session, Depends(get_session)], producer: Annotated[AIOKafkaProducer, Depends(get_kafka_producer)]):
    # user_dict = {field: getattr(user, field) for field in user.dict()}  # getting all fields of user
    # user_json = json.dumps(user_dict).encode("utf-8")
    # print("todoJSON: ", user_json)

    user_protobuf = user_pb2.User(id=user.id, name=user.name, email=user.email, password=user.password)
    print(f"User protobuf: {user_protobuf}")

    serialized_user = user_protobuf.SerializeToString()
    print(f"Serialized data: {serialized_user}")

    # producer message
    await producer.send_and_wait("user-data", serialized_user)

    # user.password = pwd_context.hash(user.password)
    # session.add(user)
    # session.commit()
    # session.refresh(user)
    return user