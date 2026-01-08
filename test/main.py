from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
items = []

# create item
@app.post('/items')
def create_item(item: Item):
    items.append(item)
    return{"message":"Item added","item":item}

# get items
@app.get('/items')
def get_items():
    return {"message":"Items fetched successfully","items":items}

# update items
@app.put('/items/{item_id}')
def update_item(item_id:int,item:Item):
    if item_id > len(items):
        return {"error":"Invalid id"}
    items[item_id] = item
    print(items[item_id])
    return {"message":'Items successfully updated',"item":items[item_id]}

# delete items
@app.delete('/items/{item_id}')
def delete_item(item_id:int):
    if item_id > len(items):
        return {
            "error":"Invalid id"
        }
    item = items.pop(item_id)
    return {
        'message':'Item successfully deleted',
        'item':item
    }

# Initial Route
@app.get('/')
def start_server():
    return {"message":"server started"}