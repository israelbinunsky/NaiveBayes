from manager import Manager
from data import Data
param = Manager.param()
data = Data("phishing.csv", param)
manager = Manager(data)
result = manager.main()
manager.printing(result)