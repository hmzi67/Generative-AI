from fastapi import FastAPI
from jose import jwt, JWTError
from datetime import datetime, timedelta

ALGORITHM = "HS256"
SECRET_KEY = "Hello Hamza Waheed Abbasi"

def create_access_token(subject: str, expires_delta: timedelta) -> str :
    expire = datetime.utcnow() + expires_delta
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

app = FastAPI()

@app.get('/')
def index():
    return {"Hello" : "Hamza"}

@app.get('/get-token')
def get_access_token(name: str):
    try:
        access_token_expiry = timedelta(minutes= 1)
        print(f"Access token expirey: {access_token_expiry}")
        generated_token = create_access_token(subject=name, expires_delta= access_token_expiry)
        return { "access_token": generated_token }
    except JWTError as e:
        return {"Error": str(e)}

def decode_access_token(token: str):
    decoded_data = jwt.decode(token, SECRET_KEY, ALGORITHM)
    return decoded_data

@app.get('/decode-token')
def decode_token(token: str):
    try:
        decoded_data = decode_access_token(token)
        return decoded_data
    except JWTError as e:
        return {"Error": str(e)}