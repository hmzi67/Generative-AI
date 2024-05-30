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

@app.get("/todos")
def mian_root():
    return { 
            "01": "Coding", 
            "02": "Study",
            "03" : "Sleep",
            "04": "Cricket",
            "05": "Coding"
        }