from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel



class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.get('/') 
def index():
    return{'Hello':'World'}

@app.post("/items/")
async def create_item(item: Item):
    return item