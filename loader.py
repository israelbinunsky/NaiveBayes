import pandas as pd
class Loader:
    def __init__(self,path, skip_rows =0):
        table = pd.read_csv(path, skiprows=skip_rows)

        # מנקה רווחים מיותרים
        table.columns = table.columns.str.strip()

        # מוחק עמודות מיותרות שנקראות 'Unnamed'
        table = table.loc[:, ~table.columns.str.contains('^Unnamed')]

        # מוחק שורות ריקות לחלוטין
        table.dropna(how='all', inplace=True)

        # table = table.sample(frac=1).reset_index(drop=True)
        self.table = table
        cms = self.table.columns.tolist()
        self.cms = [c for c in cms if c != 'id' and c and not c.startswith('Unnamed')]
        self.show_cms()

    def show_cms(self):
        print('________________________________________________')
        print('columns:')
        if len(self.cms) > 8:
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
        else:
            str = ''
            for c in self.cms:
                if c == self.cms[-1]:
                    str += c
                    print(str)
                else:
                    str += f'{c}  |  '
        print('________________________________________________')


