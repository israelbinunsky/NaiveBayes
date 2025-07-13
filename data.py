import pandas as pd
class Data:
    def __init__(self,path, skip_rows =0):
        table = pd.read_csv(path, skiprows=skip_rows)
        self.table = table.loc[:, ~table.columns.str.contains('^Unnamed')]
        cms = self.table.columns.tolist()
        self.cms = [c for c in cms if c != 'id' and c and not c.startswith('Unnamed')]
        self.show_cms()

    def show_cms(self):
        print('________________________________________________')
        print('columns:')
        cnt = 0
        str = ''
        for c in self.cms:
            cnt += 1
            if cnt % 4 == 0:
                str += c
                print(str)
                str = ''
            else:
                str += f'{c}  |  '
        print('________________________________________________')


