from classifier import Classifier
from loader import Loader
from trainer import Trainer
from fastapi import FastAPI
import uvicorn

app = FastAPI()
opened = False
classifier = None
l = None

@app.get('/{check_col}/{cols}/{rows}')
async def root(check_col: str, cols: str, rows: str):
    global classifier
    loader = Loader("phishing.csv")
    print(loader.table.head(10))
    trainer = Trainer(loader.table, check_col)
    classifier = Classifier(trainer)
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
    json = classifier.printing(final_result)
    return json

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)