'poetry add fastapi uvicorn httpx httpie requests'

step1: create 'main.py' file in subdriectory (ned_fastapi)

''' 
from fastapi import FastAPI


app: FastAPI = FastAPI()

@app.get('/')
def index():
    return{'Hello':'World'}
'''

Run poetry Project:
'poetry run uvicorn ned_fastapi.main:app --reload'

## Moc server or Auto documentation of your application

'http://127.0.0.1:8000/docs'

## Refrences 
* https://fastapi.tiangolo.com/tutorial/first-steps/