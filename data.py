import pandas as pd
class Data:
    def __init__(self,path, skip_rows =0):



        table = pd.read_csv(path, skiprows=skip_rows)
        self.table = table.loc[:, ~table.columns.str.contains('^Unnamed')]
        cms = self.table.columns.tolist()
        self.cms = [c for c in cms if c != 'id' and c and not c.startswith('Unnamed')]
        print(self.cms)


        # self.yes_num = self.table[self.check_param].value_counts().get('yes', 0)
        # self.no_num = self.table[self.check_param].value_counts().get('no', 0)
        #
        # self.yes_table = table[table[self.check_param] == 'yes']
        # self.no_table = table[table[self.check_param] == 'no']
        #
        # self.yes_dict = dict()
        # self.no_dict = dict()



        # for column in self.table.columns:
        #     if column == self.check_param:
        #         break
        #     if column != 'id':
        #         yes_by_age = self.yes_table.groupby(column).size()
        #         yes = yes_by_age.to_dict()
        #         self.yes_dict[column] = yes
        #
        #         no_by_age = self.no_table.groupby(column).size()
        #         no = no_by_age.to_dict()
        #         self.no_dict[column] = no
