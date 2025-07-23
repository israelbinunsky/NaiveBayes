import log_project
import pandas as pd
class Trainer:
    def __init__(self, df ,check_col):
        self.df = df.sample(frac=0.7, random_state=42)
        self.test_df = df.drop(self.df.index)

        self.is_check_col_exist(check_col)
        self.check_col = check_col
        self.check_col_rows_list = list(self.df[self.check_col].unique())
        self.check_col_rows_list = [x for x in self.check_col_rows_list if pd.notna(x)]

        self.nums = dict()
        self.tables = dict()
        self.dicts = dict()
        for p in self.check_col_rows_list:
            self.nums[p] = self.df[self.check_col].value_counts().get(p, 0)
            self.tables[p] = self.df[self.df[self.check_col] == p]
            self.dicts[p] = dict()

            for column in self.df.columns:
                param_by_col = self.tables[p].groupby(column).size()
                d = param_by_col.to_dict()
                for k in d.keys():
                    d[k] = d[k] / self.nums[p]
                self.dicts[p][column] = d


    def is_check_col_exist(self, check_col):
        if check_col not in self.df.columns:
            log_project.log(f"invalid parameter entered.\n")
            raise Exception("invalid parameter.")