import pandas as pd
class Data:
    def __init__(self,path, skip_rows =0):
        table = pd.read_csv(path, skiprows=skip_rows)
        self.table = table.loc[:, ~table.columns.str.contains('^Unnamed')]
        cms = self.table.columns.tolist()
        self.cms = [c for c in cms if c != 'id' and c and not c.startswith('Unnamed')]
        print(self.cms)

