from typing import final
import  loader
import trainer
import log_project
class Validator:
    def __init__(self, trainer_json):
        # self.df = trainer_json['df']
        # self.test_df = trainer_json['test_df']
        self.check_col = trainer_json['check_col']
        self.check_col_rows_list = trainer_json['check_col_rows_list']
        self.nums = trainer_json['nums']
        self.cms = trainer_json['cms']
        self.dicts = trainer_json['dicts']

    def check_validator(self,col,row, training=True):
        result = dict()
        is_exist = False
        if col not in self.cms:
            log_project.log(f"'{self.check_col}' parameter: column not in the table.\n")
            raise Exception('column not exist')
        for p in self.check_col_rows_list:
            if col in self.dicts[p] and row in self.dicts[p][col]:
                num = self.dicts[p][col][row]
                result[p] = num
                is_exist = True
            else:
                if training:
                    self.add_one_to_all(self.dicts[p])
                    self.nums[p] += 1
                result[p] = 1
        if not is_exist:
            return None
        return result

    def add_one_to_all(self, dict):
        for col in dict:
            for row in dict[col]:
                dict[col][row] += 1

    def test(self, test_df):
        final_lst = list()
        for index, row in test_df.iterrows():
            row_dict_result = dict()
            for col in test_df.columns:
                if col != 'id' and col != self.check_col:
                    dict_result = self.check_validator(col, row[col],training=False)
                    if dict_result is None:
                        continue
                    if row_dict_result:
                        for p in row_dict_result.keys():
                            row_dict_result[p] *= dict_result[p]
                    else:
                        row_dict_result = dict_result
            mx = 0
            mx_key = ''
            for k in row_dict_result.keys():
                if row_dict_result[k] > mx:
                    mx = row_dict_result[k]
                    mx_key = k
            if mx_key == row[self.check_col]:
                final_lst.append(True)
            else:
                final_lst.append(False)
        percent_true = sum(final_lst) / len(final_lst) * 100
        print(f"test result: {percent_true}%")




    # def calculation(self,col,row):
    #     dict_results = self.check_numerator(col,row)
    #     if not dict_results:
    #         return None
    #     final_dict_results = dict()
    #     for i in dict_results:
    #         final_dict_results[i] = dict_results[i] / self.m.nums[i]
    #     return final_dict_results

# loader = loader.Loader("phishing.csv")
# trainer = trainer.Trainer(loader.table, 'class')
# v = Validator(trainer)
# v.test()

