import pandas as pd
class Data:
    def __init__(self,path , param, skip_rows =0):
        self.check_param = param

        table = pd.read_csv(path, skiprows=skip_rows)
        self.table = table.loc[:, ~table.columns.str.contains('^Unnamed')]
        cms = table.columns.tolist()
        self.cms = [c for c in cms if c != 'id' and c != self.check_param and not c.startswith('Unnamed')]
        print(self.cms)


        self.check_params_list = list(self.table[self.check_param].unique())

        self.nums = dict()
        self.tables = dict()
        self.dicts = dict()


        for p in self.check_params_list:
            self.nums[p] = self.table[self.check_param].value_counts().get(p, 0)
            self.tables[p] = table[table[self.check_param] == p]
            self.dicts[p] = dict()

            for column in self.cms:
                param_by_col = self.tables[p].groupby(column).size()
                a = param_by_col.to_dict()
                self.dicts[p][column] = a


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
