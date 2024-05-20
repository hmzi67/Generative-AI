
from contextlib import asynccontextmanager
from time import sleep 
from json import dumps
from fastapi import FastAPI
from sqlmodel import SQLModel



@asynccontextmanager
async def lifespan(app: FastAPI):
    print("event_consumer started")
    yield
    
app = FastAPI(lifespan = lifespan, title="Event Consumer",
            #   servers=[
            #       {
            #           "url": "http://127.0.0.1:8000",
            #           "description": "Development server"
            #         },
            #   ]
              )

@app.get("/")
def root():
    return {"message": "Hello from consumer!"}

@app.post('/create_request')
async def create_request():
    producer = AIOKafkaProducer(bootstrap_servers='localhost:19092')
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        # Produce message
        await producer.send_and_wait("ride", b"book a ride for me")
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()
    return {"": ""}
