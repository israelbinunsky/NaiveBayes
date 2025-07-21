import log_project
class Stats:
    def __init__(self, model):
        self.m = model

    def check_numerator(self,col,row):
        result = dict()
        is_exist = False
        if col not in self.m.d.cms:
            log_project.log(f"'{self.m.check_col}' parameter: column not in the table.\n")
            raise Exception('column not exist')
        for p in self.m.check_col_rows_list:
            if col in self.m.dicts[p] and row in self.m.dicts[p][col]:
                num = self.m.dicts[p][col][row]
                result[p] = num
                is_exist = True
            else:
                a = 1
                self.add_one_to_all(self.m.dicts[p])
                self.m.nums[p] += 1
                result[p] = a
        if not is_exist:
            return None
        return result

    def add_one_to_all(self, dict):
        for col in dict:
            for row in dict[col]:
                dict[col][row] += 1

    def calculation(self,col,row):
        dict_results = self.check_numerator(col,row)
        if not dict_results:
            return None
        final_dict_results = dict()
        for i in dict_results:
            final_dict_results[i] = dict_results[i] / self.m.nums[i]
        return final_dict_results



