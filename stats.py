class Stats:
    def __init__(self, param):
        self.p = param

    def add_one(self, dict):
        for col in dict:
            for row in dict[col]:
                dict[col][row] += 1

    def check(self,col,row):
        result = dict()
        is_exist = False
        for p in self.p.check_params_list:
            if col in self.p.dicts[p] and row in self.p.dicts[p][col]:
                num = self.p.dicts[p][col][row]
                result[p] = num
                is_exist = True
            else:
                a = 1
                self.add_one(self.p.dicts[p])
                self.p.nums[p] += 1
                result[p] = a
        if not is_exist:
            return None
        return result

        # y = 0
        # n = 0
        # if row in self.d.yes_dict[col] and row in self.d.no_dict[col]:
        #     y = self.d.yes_dict[col][row]
        #     n = self.d.no_dict[col][row]
        # elif row in self.d.yes_dict[col] and row not in self.d.no_dict[col]:
        #     y = self.d.yes_dict[col][row]
        #     n = 1
        #     self.add_one(self.d.no_dict)
        #     self.d.no_num += 1
        # elif row not in self.d.yes_dict[col] and row in self.d.no_dict[col]:
        #     y = 1
        #     n = self.d.no_dict[col][row]
        #     self.add_one(self.d.yes_dict)
        #     self.d.yes_num += 1
        # l["y"] = y
        # l["n"] = n
        # return l

    def statistics(self,col,row):
        dict_results = self.check(col,row)
        if not dict_results:
            return None
        final_dict_results = dict()
        for i in dict_results:
            final_dict_results[i] = dict_results[i] / self.p.nums[i]

        return final_dict_results
        # y = l["y"]
        # n = l["n"]
        # yes_result = y / self.d.yes_num
        # no_result = n / self.d.no_num
        # result = {"yes": yes_result, "no": no_result}



