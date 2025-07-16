from manager import Manager
from data import Data
from param import Param
from fastapi import FastAPI
import uvicorn
import log_project


app = FastAPI()
opened = False
manager = None
l = None


def input_param():
    check_param = input('The parameter you want to check: ')
    return check_param

@app.get('/{par}/{col}/{row}')
async def root(par: str, col: str, row: str):
    global opened
    global manager
    if not opened:
        data = Data("data for NB buys computer.xlsx - Sheet1.csv",3)
        param = Param(data, par)
        manager = Manager(param)
    result = manager.main_for_server(col, row)
    if row.isdigit():
        row = int(row)
    json = manager.printing(result)
    return json

def Menu():
    choice = input('to print in terminal enter 1\nto upload on the server enter 2\nto show logs enter 3\nto exit enter 4: ')
    global opened
    global manager
    if choice == '1':
        if not opened:
            data = Data("data for NB buys computer.xlsx - Sheet1.csv",3)
            p = input_param()
            param = Param(data, p)
            manager = Manager(param)
            opened = True
        l = manager.inputs()
        result = manager.main(l[0], l[1])
        manager.printing(result)
        Menu()
    elif choice == '2':
        uvicorn.run(app, host='127.0.0.1', port=8000)
    elif choice == '3':
        log_project.show_log()
        Menu()


if __name__ == '__main__':
    Menu()
