from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
from config import settings

app = FastAPI(
    title=settings.API_TITLE, 
    description=settings.API_DESCRIPTION, 
    version=settings.API_VERSION
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float

class ItemResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

# In-memory storage
items_db = []
next_id = 1

@app.get("/")
async def root():
    return {"message": "Welcome to Simple FastAPI!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/items", response_model=List[ItemResponse])
async def get_items():
    return items_db

@app.get("/items/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int):
    item = next((item for item in items_db if item["id"] == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items", response_model=ItemResponse)
async def create_item(item: Item):
    global next_id
    new_item = {
        "id": next_id,
        "name": item.name,
        "description": item.description,
        "price": item.price
    }
    items_db.append(new_item)
    next_id += 1
    return new_item

@app.put("/items/{item_id}", response_model=ItemResponse)
async def update_item(item_id: int, item: Item):
    existing_item = next((i for i in items_db if i["id"] == item_id), None)
    if not existing_item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    existing_item.update({
        "name": item.name,
        "description": item.description,
        "price": item.price
    })
    return existing_item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    global items_db
    items_db = [item for item in items_db if item["id"] != item_id]
    return {"message": "Item deleted successfully"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host=settings.HOST, 
        port=settings.PORT,
        reload=settings.DEBUG
    )