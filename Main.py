from manager import Manager
from data import Data
from param import Param
import requests
from pprint import pprint
import uvicorn
from fastapi import FastAPI

data = Data("phishing.csv")
param = Param(data)
manager = Manager(param)
result = manager.main()
txt = manager.printing(result)

app = FastAPI()
@app.get('/')
async def root():
    return txt
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
