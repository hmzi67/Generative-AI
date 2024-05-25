from typing import AsyncGenerator
from fastapi import FastAPI
from sqlmodel import SQLModel
from contextlib import asynccontextmanager
from sign_up.router import user
from sign_up.db import engine
from aiokafka import AIOKafkaConsumer
import asyncio

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
            print(f"Received message: {message.value.decode()} on topic {message.topic}")
            # Here you can add code to process each message.
            # Example: parse the message, store it in a database, etc.
    finally:
        # Ensure to close the consumer when done.
        await consumer.stop()

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    print('Creating Tables...')
    task = asyncio.create_task(consume_messages('Users', 'broker:19092'))
    create_tables()
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


