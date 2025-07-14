from manager import Manager
from data import Data
from param import Param
from fastapi import FastAPI
import uvicorn
import log_project

data = Data("phishing.csv")
param = Param(data)
manager = Manager(param)

app = FastAPI()

@app.get('/{col}/{row}')
async def root(col: str, row: int):
    result = manager.main_for_server(col, row)
    json = manager.printing(result)
    return json

def Menu():
    choice = input('to print in terminal enter 1\nto upload on the server enter 2\nto show logs enter 3: ')
    if choice == '1':
        l = manager.inputs()
        result = manager.main(l[0], l[1])
        manager.printing(result)
    elif choice == '2':
        uvicorn.run(app, host='127.0.0.1', port=8000)
    elif choice == '3':
        log_project.show_log()

if __name__ == '__main__':
    Menu()
