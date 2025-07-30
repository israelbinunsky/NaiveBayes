import log_project
import json
import pandas as pd
class Trainer:
    def __init__(self, df ,check_col):
        self.df = df.sample(frac=0.7, random_state=42)
        self.test_df = df.drop(self.df.index)

        self.is_check_col_exist(check_col)
        self.check_col = check_col
        self.check_col_rows_list = list(self.df[self.check_col].unique())
        self.check_col_rows_list = [str(x) for x in self.check_col_rows_list if pd.notna(x)]
        self.cms = [str(x) for x in self.df.columns]

        self.nums = dict()
        self.tables = dict()
        self.dicts = dict()
        for p in self.check_col_rows_list:
            self.nums[p] = float(self.df[self.check_col].value_counts().get(p, 0))
            filtered_df = self.df[self.df[self.check_col] == p]
            self.tables[p] =  self.df[self.df[self.check_col] == p]
            self.dicts[p] = dict()

            for column in self.df.columns:
                param_by_col = self.tables[p].groupby(column).size()
                d = param_by_col.to_dict()
                for k in d.keys():
                    d[k] = float(d[k] / self.nums[p])
                self.dicts[p][column] = d


    def is_check_col_exist(self, check_col):
        if check_col not in self.df.columns:
            log_project.log(f"invalid parameter entered.\n")
            raise Exception("invalid parameter.")

    def get_json(self):
        json_r = {'check_col': str(self.check_col),
                # 'df':  self.df.to_json(orient='records'),
                # 'test_df':  self.test_df.to_json(orient='records'),
                'check_col_rows_list': self.check_col_rows_list,
                'nums': self.nums,
                'cms': list(self.cms),
                'dicts': self.dicts
                }
        return json_r


    # def get_json(self):
    #     def convert(obj):
    #         if isinstance(obj, dict):
    #             new_dict = {}
    #             for k, v in obj.items():
    #                 if hasattr(k, 'item'):
    #                     new_key = k.item()
    #                 else:
    #                     new_key = k
    #                 new_dict[new_key] = convert(v)
    #             return new_dict
    #         elif isinstance(obj, list):
    #             return [convert(i) for i in obj]
    #         elif hasattr(obj, 'item'):
    #             return obj.item()
    #         else:
    #             return obj
    #
    #     return convert(self.dicts)  # ← מחזיר dict, לא מחרוזת JSON




