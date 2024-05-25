from fastapi import FastAPI
from sqlmodel import SQLModel, Field
from contextlib import asynccontextmanager
from typing import Optional
from aiokafka import AIOKafkaProducer
from app import settings
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
    producer = AIOKafkaProducer(bootstrap_servers= "broker:9092")
    await producer.start()
    order_JSON = json.dumps(order.__dict__).encode('utf-8')
    print(order_JSON)
    # Get cluster layout and initial topic/partition leadership information
    try:
        # Produce message
        await producer.send_and_wait("order", b"Super message")
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()

    return {"Response": "Message send successfully"}
