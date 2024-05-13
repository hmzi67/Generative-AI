# Kafka
## **Introduction:**
### What is event Streaming?

Event is basically any  any change in logs of your app. When we share our logs to anyone live that is known as event streaming.

**i.e:** When we use youtube streaming. Our streaming is avaliable for public so they can watch our streaming to see what we are doing etc? So If we are sharing our gameplay with public. In this example any change in the stream is a event and we are sharing our every event with public is a event streaming.

Technically speaking, event streaming is the practice of capturing data in real-time from event sources like databases, sensors, mobile devices, cloud services, and software applications in the form of streams of events; storing these event streams durably for later retrieval; manipulating, processing, and reacting to the event streams in real-time as well as retrospectively; and routing the event streams to different destination technologies as needed. Event streaming thus ensures a continuous flow and interpretation of data so that the right information is at the right place, at the right time. 

## What is EDA?
- <b>Loose coupling:</b> Components are independent and communicate through events, making them easier to develop, maintain, and update.
- <b>Scalability:</b> EDA can handle more consumer as you want to process events.
- <b>Real-time processing:</b> Event can trigger action as it happens enabling real-time applications

## Advantages of EDA
- <b>Flexibility: </b> EDA can accomodate changing business needs by adding events type
- <b>Resilience: </b> If one part of your system fails, other parts of your system will continue processing events
- <b>Concurrency:</b> Multiple consumer can process events at a time

## Disadvantages of EDA
- <b>Complexity:</b> Designing and debugging EDA systems can be more complex than traditional architecture
- <b>Monitoring:</b> Troublesshooting issues can be challenging due to asynchronous communication
- <b>Testing:</b> Testing event-driven system require specilized tools and techiniques

EDA is a powerfull approach for building scalableand responsive apps

# Synchronous Inter Services Messages between Microservices
There are two main approaches to inter-service communication in a microservices architecture:
1. **Synchronous:** This method involves a direct call between services, typically using an API exposed by one service that another service can interact with. Protocols like HTTP are commonly used for this purpose. The calling service waits for a response from the other service before proceeding.   
2. **Asynchronous Messaging:** In this approach, services don't directly call each other. Instead, they send messages to a queue or message broker. The receiving service then processes the message independently. This allows for looser coupling between services and improved scalability. Message brokers like Kafka or RabbitMQ are popular choices for asynchronous communication.

Both synchronous and asynchronous communication have their advantages and disadvantages:

1. **Synchronous communication:** is simpler to implement and easier to debug, but it can lead to tight coupling between services and performance bottlenecks if not designed carefully.
2. **Asynchronous communication:** offers better scalability and looser coupling, but it can be more complex to implement and reason about.

The best choice for your microservices communication will depend on the specific needs of your application. Consider factors like latency requirements, message volume, and desired level of coupling between services when making your decision.

## Synchronous Communication with FastAPI, Docker, and Poetry
Code Examples: FastAPI, Docker, and Poetry
Here are some code snippets to get you started:

1. FastAPI - Simple Hello World Endpoint:
```py
Python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}
```

This code defines a basic FastAPI application with an endpoint (/). The async def root function is an asynchronous handler, but it can be used for synchronous communication as well.
2. Dockerfile (Basic):
Dockerfile
```py
FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```
Use code with caution.
content_copy
This Dockerfile defines a container based on the Python 3.9 image. It copies the requirements.txt file (which would list your FastAPI dependencies) and installs them. Then, it copies your application code and finally runs the uvicorn command to start the FastAPI app.

3. Database Model:
```py
from sqlmodel import Field, SQLModel

class User(SQLModel):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)
```
This code defines a basic User model for a database. The id field is the primary key and the name field is a string.

https://sweltering-memory-bcc.notion.site/Apache-Kafka-7d9bdb1ca8fb402ababfbd10e1083a28