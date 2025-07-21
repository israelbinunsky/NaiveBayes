from manager import Manager
from data import Data
from model import Model
from fastapi import FastAPI
import uvicorn
import log_project


app = FastAPI()
opened = False
manager = None
l = None


def input_check_col():
    check_col = input('The parameter you want to check: ')
    return check_col

@app.get('/{check_col}/{col}/{row}')
async def root(check_col: str, col: str, row: str):
    global opened
    global manager
    if not opened:
        data = Data("data for NB buys computer.xlsx - Sheet1.csv",3)
        model = Model(data, check_col)
        manager = Manager(model)
    if row.isdigit():
        row = int(row)
    result = manager.main_for_server(col, row)
    json = manager.printing(result)
    return json

def Menu():
    choice = input('to print in terminal enter 1\nto upload on the server enter 2\nto show logs enter 3\nto exit enter 4: ')
    global opened
    global manager
    if choice == '1':
        if not opened:
            data = Data("data for NB buys computer.xlsx - Sheet1.csv",3)
            check_col = input_check_col()
            model = Model(data, check_col)
            manager = Manager(model)
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
