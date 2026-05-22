from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Item Management API",
    description="Simple CRUD API using FastAPI",
    version="1.0.0"
)

# DATA MODEL

class Item(BaseModel):
    id: int
    name: str
    price: float

# IN-MEMORY DATABASE

items = []


# HOME ROUTE

@app.get("/")
def home():
    return {"message": "FastAPI CRUD is running"}

# CREATE ITEM

@app.post("/items")
def create_item(item: Item):

    # check duplicate ID
    for i in items:
        if i.id == item.id:
            raise HTTPException(
                status_code=400,
                detail="Item ID already exists"
            )

    items.append(item)
    return {"message": "Item created", "item": item}

# GET ALL ITEMS

@app.get("/items")
def get_items():
    return items

# GET SINGLE ITEM

@app.get("/items/{item_id}")
def get_item(item_id: int):

    for item in items:
        if item.id == item_id:
            return item

    raise HTTPException(
        status_code=404,
        detail="Item not found"
    )

# UPDATE ITEM

@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):

    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = updated_item
            return {
                "message": "Item updated",
                "item": updated_item
            }

    raise HTTPException(
        status_code=404,
        detail="Item not found"
    )

# DELETE ITEM

@app.delete("/items/{item_id}")
def delete_item(item_id: int):

    for index, item in enumerate(items):
        if item.id == item_id:
            deleted = items.pop(index)
            return {
                "message": "Item deleted",
                "item": deleted
            }
        
    raise HTTPException(
        status_code=404,
        detail="Item not found"
    )