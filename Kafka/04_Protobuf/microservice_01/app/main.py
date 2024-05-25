from fastapi import FastAPI
from sqlmodel import SQLModel, Field
from contextlib import asynccontextmanager
from typing import Optional
from app import settings
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
import asyncio
import json

class Order(SQLModel):
    id: Optional[int] = Field(default=None)
    username: str
    product_id: str
    product_name: str
    product_price: str

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Creating Tables')
    task = asyncio.create_task(consume_messages('todos', 'broker:19092'))
    yield

app: FastAPI = FastAPI(
    lifespan=lifespan, 
    title="Kafka UI with python", 
    version='1.0.0'
)

@app.get('/')
def root():
    return "HEllo World"

@app.post('/create_order')
async def read_product(order: Order):
    producer = AIOKafkaProducer(bootstrap_servers= "broker:19092")
    await producer.start()
    order_JSON = json.dumps(order.__dict__).encode('utf-8')
    print(order_JSON)
    # Get cluster layout and initial topic/partition leadership information
    try:
        # Produce message
        await producer.send_and_wait("order", order_JSON)
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()

    return order_JSON


async def consume_messages(topic, bootstrap_servers):
    # Create a consumer instance.
    consumer = AIOKafkaConsumer(
        topic,
        bootstrap_servers=bootstrap_servers,
        group_id="my-todos-group",
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
