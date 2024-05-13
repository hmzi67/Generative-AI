from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def mian():
    return { 
            "Name": "Hamza Waheed Abbasi", 
            "Email": "hamzawaheed057@gmail.com",
            "Age" : "23",
            "Occupation": "Web Developer"
        }
