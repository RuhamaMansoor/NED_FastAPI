from fastapi import FastAPI, Depends, Query
from typing import Union
from pydantic import BaseModel # pydantic for validation
from typing import Any


app= FastAPI()


 #----------index function:----------
@app.get('/') 
def index():
    return{'Hello':'World'}

# -----------get_users function:--------

users_data = {
                "user1": {"name": "Ruhama", "email": "ruhamamansoor96@gmail.com"},
                "user2": {"name": "Jazzy", "email": "jazzy98@gmail.com"}
} 
@app.get('/user/') 
def get_users():
    return users_data

# ----------fn_items function:-----------

@app.get('/items/{name}')
def fn_items(name):
    return{"purchase item":name}

# ------------read_item function:---------

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


# --------------create_item------------
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    
@app.post("/items/")
async def create_item(item: Item):
    return item


# ------------user_dep--------------5
# The Dependency Function:

users_get :list[dict[Any,Any]] = [
    {'name':'Ruhama','password': '123'},
    {'name':'Jazzy','password': '000'}
    ]



def user_dep(name: str = Query(...), password: str =Query(...)): # Validate user or perform any othere required operations here.
                                                                 # The ellipsis '...' makes the query parameters required
    for d in users_get:
        if d.get('name') == name and d.get('password') ==password:
         return{"name":name,
                "valid": True,
                "message":f"hello{d.get('name')}"
                }         
         
        else:
            return{"message": f"sorry, {d.get('name')} is not a valid user"}                   

# The path function:
@app.get("/user")
def get_user(user:dict = Depends(user_dep)):
    return user