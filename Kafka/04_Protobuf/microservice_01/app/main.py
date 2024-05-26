from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Field
from contextlib import asynccontextmanager
from typing import Optional
from app import settings
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
import asyncio
import json
from typing import Annotated
from app import order_pb2

class Order(SQLModel):
    id: Optional[int] = Field(default=None)
    username: str
    product_id: str
    product_name: str
    product_price: str

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Creating Tables')
    task = asyncio.create_task(consume_messages("order", 'broker:19092'))
    yield

app: FastAPI = FastAPI(
    lifespan=lifespan, 
    title="Kafka UI with python", 
    version='1.0.0'
)

async def get_kafka_producer():
    producer = AIOKafkaProducer(bootstrap_servers= 'broker:19092')
    await producer.start()
    try:
        yield producer
    finally:
        await producer.stop()





@app.get('/')
def root():
    return "HEllo World"

@app.post('/create_order')
async def read_product(order: Order, producer: Annotated[AIOKafkaProducer, Depends(get_kafka_producer)]):

    order_protobuf = order_pb2.Order(id=order.id, username=order.username, product_id=order.product_id, product_name=order.product_name, product_price=order.product_price)
    print(f"Protobuf order data: {order_protobuf}")

    serialized_order = order_protobuf.SerializeToString()
    print(f"Serialized ordere data: {serialized_order}")

    # Get cluster layout and initial topic/partition leadership information
    try:
        # Produce message
        await producer.send_and_wait("order", serialized_order)
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()

    return serialized_order


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
            new_order = order_pb2.Order()
            new_order.ParseFromString(message.value)
            print(f"\n\n Consumer Deserialized data: {new_order}")
    finally:
        # Ensure to close the consumer when done.
        await consumer.stop()
