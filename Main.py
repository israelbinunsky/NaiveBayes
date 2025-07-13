from manager import Manager
from data import Data
from param import Param
import uvicorn
from fastapi import FastAPI

data = Data("phishing.csv")
param = Param(data)
manager = Manager(param)
# l = manager.inputs()
# result = manager.main(l[0],l[1])
# manager.printing(result)

app = FastAPI()
@app.get('/{col}/{row}')
async def root(col, row):
    col = str(col)
    row = int(row)
    result = manager.main(col, row)
    json = manager.printing(result)
    return json
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
