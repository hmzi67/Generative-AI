from fastapi import FastAPI

app = FastAPI(
    title="Hello World",
    version= "1.0.0",
    servers=[
        {
            "url": "http://0.0.0.0:8000", 
            "description": "Development Server"
        }
    ]
)

@app.get('/')
def get_root():
    return "Hamza Waheed abbasi"

@app.get('/hello/')
def post_name():
    return "Muhammad Naveed Cto at code hunts"