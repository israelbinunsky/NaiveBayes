from loader import Loader
from  cleaner import Cleaner
from trainer import Trainer
from fastapi import FastAPI
import uvicorn
import json

app = FastAPI()
classifier = None

@app.get('/')
async def root():
    global classifier
    loader = Loader("data for NB buys computer.csv")
    cleaner = Cleaner(loader.table)
    trainer = Trainer(cleaner.df, "Buy_Computer")
    response_json = trainer.get_json()
    # with open("/shared/trained_model.json", "w") as f:
    #     json.dump(trainer.get_json(), f)
    #     f.close()

    # response_json  = { 'check_col': trainer.check_col,
    #         'check_col_rows_list': trainer.check_col_rows_list,
    #         'nums': trainer.nums,
    #         'cms': trainer.cms,
    #         'dicts': trainer.dicts
    #         }
    return response_json

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

# loader = Loader("phishing.csv")
# cleaner = Cleaner(loader.table)
# trainer = Trainer(cleaner.df, "HTTPS")
# trainer.get_json()
