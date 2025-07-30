from classifier import Classifier
from loader import Loader
from  cleaner import Cleaner
from trainer import Trainer
from validator import Validator
from fastapi import FastAPI
import uvicorn

app = FastAPI()
opened = False
classifier = None
l = None

def split_params(cols, rows):
    cols_lst = cols.split('.')
    rows_lst = rows.split('.')
    final_result = 0
    for i in range(len(cols_lst)):
        if rows_lst[i].isdigit():
            rows_lst[i] = int(rows_lst[i])
        result = classifier.main(cols_lst[i], rows_lst[i])
        if final_result:
            for k in final_result.keys():
                final_result[k] *= result[k]
        else:
            final_result = result
    return final_result


@app.get('/{check_col}/{cols}/{rows}')
async def root(check_col: str, cols: str, rows: str):
    global classifier
    loader = Loader("data for NB buys computer.csv")
    cleaner = Cleaner(loader.table)
    print(cleaner.df.head(10))
    trainer = Trainer(cleaner.df, check_col)
    trainer_json = trainer.get_json()
    validator = Validator(trainer_json)
    classifier = Classifier(validator)
    final_result = split_params(cols, rows)
    json = classifier.printing(final_result)
    return json

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)