from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()

users = {"1": "Имя: Example, возраст: 18"}

@app.get("/users")
async def get_users():
    return users


@app.post("/user/{username}/{age}")
async def post_user(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
                    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example='24')]):
    max_id = int(max(users, key=int))
    users[str(max_id + 1)] = f"Имя: {username}, возраст: {age}"
    return f"User {id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter ID", example='1')], 
                      username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanProfi")],
                      age: Annotated[int, Path(ge=18, le=120, description="Enter age", example='28')]):
    if str(user_id) not in users:
        return f"User {user_id} not found"
    users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter ID", example='2')]):
    if str(user_id) not in users:
        return f"User {user_id} not found"
    del users[str(user_id)]
    return f"The user {user_id} is deleted"
