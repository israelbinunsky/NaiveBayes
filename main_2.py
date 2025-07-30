from classifier import Classifier
from validator import Validator
from fastapi import FastAPI
import uvicorn
import httpx
import time
import os
import json
import requests

app = FastAPI()
classifier = None

def split_params(cols, rows):
    global classifier
    cols_lst = cols.split('.')
    rows_lst = rows.split('.')
    final_result = 0
    global classifier
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

# def wait_for_file(filepath, timeout=10):
#     start = time.time()
#     while not os.path.exists(filepath):
#         if time.time() - start > timeout:
#             raise FileNotFoundError(f"{filepath} not found after {timeout} seconds")
#         time.sleep(0.5)
#     with open(filepath, "r") as f:
#         return json.load(f)

@app.get('/{cols}/{rows}')
async def root(cols: str, rows: str):
    global classifier
    json_trainer = ''
    # json_trainer = wait_for_file("/shared/trained_model.json")
    response = requests.get("http://main_1:8000")
    if response.status_code == 200:
        json_trainer = response.json()
    else:
        print(response.status_code)

    validator = Validator(json_trainer)
    classifier = Classifier(validator)
    final_result = split_params(cols, rows)
    result = classifier.printing(final_result)
    return result

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)