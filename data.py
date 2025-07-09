import pandas as pd
class Data:
    def __init__(self,path = "data for NB buys computer.xlsx - Sheet1.csv",skip_rows =3):
        table = pd.read_csv(path, skiprows=skip_rows)
        self.table = table.loc[:, ~table.columns.str.contains('^Unnamed')]

        self.check_param = ''

        self.yes_num = self.table[self.check_param].value_counts().get('yes', 0)
        self.no_num = self.table[self.check_param].value_counts().get('no', 0)

        self.yes_table = table[table[self.check_param] == 'yes']
        self.no_table = table[table[self.check_param] == 'no']

        self.yes_dict = dict()
        self.no_dict = dict()

        for column in table.columns:
            if column == self.check_param:
                break
            if column != 'id':
                yes_by_age = self.yes_table.groupby(column).size()
                yes = yes_by_age.to_dict()
                self.yes_dict[column] = yes

                no_by_age = self.no_table.groupby(column).size()
                no = no_by_age.to_dict()
                self.no_dict[column] = no
