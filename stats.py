import log_project
class Stats:
    def __init__(self, param):
        self.p = param

    def check_numerator(self,col,row):
        result = dict()
        is_exist = False
        if col not in self.p.d.cms:
            log_project.log(f"'{self.p.check_param}' parameter: column not in the table.\n")
            raise Exception('column not exist')
        for p in self.p.check_params_list:
            if col in self.p.dicts[p] and row in self.p.dicts[p][col]:
                num = self.p.dicts[p][col][row]
                result[p] = num
                is_exist = True
            else:
                a = 1
                self.add_one_to_all(self.p.dicts[p])
                self.p.nums[p] += 1
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
            final_dict_results[i] = dict_results[i] / self.p.nums[i]
        return final_dict_results



