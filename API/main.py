# first > "pip3 install fastapi" or "python.exe -m pip install --upgrade pip"
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}