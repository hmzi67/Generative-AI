from typing import AsyncGenerator
from fastapi import FastAPI
from sqlmodel import SQLModel
from contextlib import asynccontextmanager
from app.router import user
from app.db import engine
from aiokafka import AIOKafkaConsumer
import asyncio
# Step 1: Import the generated protobuf code - Review todo post api route next.
from app import user_pb2

def create_tables():
    SQLModel.metadata.create_all(engine)

async def consume_messages(topic, bootstrap_servers):
    # Create a consumer instance.
    consumer = AIOKafkaConsumer(
        topic,
        bootstrap_servers=bootstrap_servers,
        group_id="my-group",
        auto_offset_reset='earliest'
    )
    # Start the consumer.

    await consumer.start()
    try:
        # Continuously listen for messages.
        
        async for message in consumer:
            print(f"Consumer raw message value: {message.value}")
            # Here you can add code to process each message.
            # Example: parse the message, store it in a database, etc.

            new_user = user_pb2.User()
            new_user.ParseFromString(message.value)
            print(f"\n\n Consumer Deserialized data: {new_user}")
    finally:
        # Ensure to close the consumer when done.
        await consumer.stop()

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    print('Creating Tables...')
    task = asyncio.create_task(consume_messages('user-data', 'broker:19092'))
    # create_tables()
    print("Tables Created")
    yield


app: FastAPI = FastAPI(
    lifespan=lifespan, 
    title="Sign up api", 
    version='1.0.0', 
)

@app.get('/')
def root():
    return "HEllo World"

app.include_router(router=user.router)


