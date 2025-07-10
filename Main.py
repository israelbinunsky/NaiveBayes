from manager import Manager
from data import Data
from param import Param

data = Data("phishing.csv")
param = Param(data)
manager = Manager(param)
result = manager.main()
manager.printing(result)