from fastapi import FastAPI, Depends, HTTPException
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from typing import Annotated

ALGORITHM = "HS256"
SECRET_KEY = "Hello Hamza Waheed Abbasi"

def create_access_token(subject: str, expires_delta: timedelta) -> str :
    expire = datetime.utcnow() + expires_delta
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl= "/login")

fake_db : dict[str, dict[str, str]] = {
    "hmzi67": {
        "username": "hmzi67",
        "full_name": "Hamza Waheed",
        "email": "hamzawaheed@codehuntspk.com",
        "password": "hmzi_password",
    },
    "uxlabspk": {
        "username": "uxlabspk",
        "full_name": "Muhammad Naveed",
        "email": "muhammadnaveed@codehuntspk.com",
        "password": "uxlabs_password",
    },
}

@app.post('/login')
def login_request(form_data: Annotated[OAuth2PasswordRequestForm, Depends(OAuth2PasswordRequestForm)]):

    # step 01: username or email exist in db
    user_in_fakeDB = fake_db.get(form_data.username)
    if (user_in_fakeDB is None):
        raise HTTPException(status_code= 404, detail= "Incorrect username")

    # step 02: check password
    if (user_in_fakeDB["password"] != form_data.password):
        raise HTTPException(status_code=400, detail="Incorrect password")
    
    # step 03: create access token
    acccess_token_expiry = timedelta(minutes=1)
    generated_access_token = create_access_token(subject= form_data.username, expires_delta= acccess_token_expiry)

    return {"username": form_data.username, "access token": generated_access_token}

@app.get('/all-users')
def get_all_users(token: Annotated[str, Depends(oauth2_scheme)]):
    return fake_db

@app.get('/special-items')
def get_specia_items(token: Annotated[str, Depends(oauth2_scheme)]):
    decoded_data = jwt.decode(token, SECRET_KEY, ALGORITHM)
    return {"Special": "Item", "decoded_data": decoded_data}

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


# Multiple microservice - 1 Auth Microservice

# step 1: Wrapper endpoint that takes formdata and call auth service login auth service login endpoint

# step 2: Import oAuthPasswordBearer - tokenUrl = Wrapper endpoint api path

# step 3: oauth2_scheme = pass all endpoints in dependency