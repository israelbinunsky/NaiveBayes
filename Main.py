from classifier import Classifier
from loader import Loader
from cleaner import Cleaner
from trainer import Trainer
from fastapi import FastAPI
import uvicorn
import log_project
import pprint



app = FastAPI()
opened = False
classifier1 = None
l = None


def input_check_col():
    check_col = input('The parameter you want to check: ')
    return check_col

@app.get('/{check_col}/{col}/{row}')
async def root(check_col: str, col: str, row: str):
    global opened
    global classifier1
    if not opened:
        loader = Loader("phishing.csv")
        cleaner = Cleaner(loader.table)
        model = Trainer(cleaner.df, check_col)
        classifier1 = Classifier(model)
    if row.isdigit():
        row = int(row)
    result = classifier1.main(col, row)
    json = classifier1.printing(result)
    return json

def Menu():
    choice = input('to print in terminal enter 1\nto upload on the server enter 2\nto show logs enter 3\nto test the model enter 4\nto exit enter 5: ')
    global opened
    global classifier1
    if choice == '1':
        if not opened:
            loader = Loader("phishing.csv")
            # print(loader.table["Buy_Computer"].unique())
            cleaner = Cleaner(loader.table)
            print(cleaner.df.head(10))

            check_col = input_check_col()
            trainer = Trainer(cleaner.df, check_col)
            # pprint.pprint(trainer.dicts)
            classifier1 = Classifier(trainer)
            opened = True
        l = classifier1.inputs()
        result = classifier1.main_inputs(l[0], l[1])
        classifier1.printing(result)
        Menu()
    elif choice == '2':
        uvicorn.run(app, host='127.0.0.1', port=8000)
    elif choice == '3':
        log_project.show_log()
        Menu()
    elif choice == '4':
        if classifier1:
            classifier1.v.test()
        else:
            print('not name of column to check. please make 1 step before.')
            Menu()


if __name__ == '__main__':
    Menu()
