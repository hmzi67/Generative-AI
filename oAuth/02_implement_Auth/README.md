## Authentication

The password "flow" is one of the ways ("flows") defined in OAuth2, to handle security and authentication.

Here we will learn how to build Login System that can take username/email and returns Bearer token - yes access_token. 

We will be using the code from last step as starter code. 

## FormData - What is it?

FormData and JSON are both used to send data to an API. Just like we learned to pass data in JSON format in Body to APIs. FormData is a way to send data to an API.

- Format: FormData is a set of key/value pairs that can be sent using the multipart/form-data encoding type.
- Usage: When you submit a form in a web page, the browser automatically encodes the form data as FormData and sends it to the server.

https://chat.openai.com/share/dc922c6e-10cd-4423-9c7a-621755d42787
https://fastapi.tiangolo.com/tutorial/request-forms/

## OAuth2PasswordRequestForm - A BuiltIn FastAPI Class Dependency

OAuth2PasswordRequestForm is a class dependency that declares a form body with:

- The username.
- The password.
- Some Optional Fields...

We can import it 
`from fastapi.security import OAuth2PasswordRequestForm`

It is just a class dependency that you could have written yourself, or you could have declared Form parameters directly. But as it's a common use case, it is provided by FastAPI directly.

## Coding Time

1. Take your code from last step or clone this step code.

2. Import OAuth2PasswordRequestForm class 

```
from fastapi.security import OAuth2PasswordRequestForm
```

3. Some Other Necessary imports

```
from fastapi import Depends
from typing import Annotated
```

4. Create a Login API Route and use OAuth2PasswordRequestForm in Dependency Injection. 

```
@app.post("/login")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends(OAuth2PasswordRequestForm)]):
    """
    Understanding the login system
    -> Takes form_data that have username and password
    """
    
    # We will add Logic here to check the username/email and password
    # If they are valid we will return the access token
    # If they are invalid we will return the error message

    return {"username": form_data.username, "password": form_data.password}
```

Now when calling this API Route we can pass username/email and password and get them in the response. So here we can add logic to check them in database and then generate access token.

5. Let's create a users object and use it as fake_db to authenticate the user in /login endpoint.

```
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
```

Next update our login function to check if given username and password matches or else raise an HttpException

```
from fastapi import HTTPException

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
```

Now play with this updated endpoint with valid and invalid usernames.

6. Let's add 2 new Routes
    - One that returns the list of all users
    - Other that takes access_token and return user all details

```
@app.get('/all-users')
def get_all_users():
    # Note: We never return passwords in a real application
    return fake_db
```

```
@app.get("/users/me")
def read_users_me(token: str):
    user_token_data = decode_access_token(token)
    
    user_in_db = fake_db.get(user_token_data["sub"])
    
    return user_in_db
```

Now there are 2 security considerations

1. We need a secure way to send token to backend
2. I want to safeguard these 2 api routes so only privileged/allowed users can assess these 2 api routes.

-> Here comes the concept of Authorization. In next step we will learn how to safeguard and secure our apis and authorize them.