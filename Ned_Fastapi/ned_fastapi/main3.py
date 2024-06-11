from fastapi import FastAPI


app= FastAPI()

@app.get('/items/{name}')
def fn_items(name):
    return{"purchase item":name}