# fastapi_neon/main.py

from fastapi import FastAPI

app = FastAPI(title="Hello World API", 
    version="0.0.1",
    servers=[
        {
            "url": "http://127.0.0.0:8000", # ADD NGROK URL Here Before Creating GPT Action
            "description": "Development Server"
        }
        ])


@app.get("/")       # Decorator  Function to Define Route Handler
def read_root():
    return (
        {
            "Name": "Hamza Waheed Abbasi",
            "Title": "Welcome to the Hello World API",
            "Description": "This is a simple Hello",
        }
    )