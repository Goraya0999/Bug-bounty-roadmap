from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


# -------------------- Routes --------------------

@app.get("/")
def home():
    return {"message": "Hello from my API"}


@app.get("/hello/{name}")
def greet(name: str):
    return {"message": f"Hello {name}!"}


# -------------------- Models --------------------

class Item(BaseModel):
    name: str
    price: float


class User(BaseModel):
    name: str
    email: str
    age: Optional[int] = None
    score: float = Field(default=0.0, ge=0.0, le=100.0)


# -------------------- POST APIs --------------------

@app.post("/items")
def create_item(item: Item):
    return {
        "received": item.name,
        "cost": item.price
    }


@app.post("/users")
def create_user(user: User):
    return {
        "message": f"User {user.name} created successfully",
        "user": user.dict()
    }