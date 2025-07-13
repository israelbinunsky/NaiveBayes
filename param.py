import log_project
class Param:
    def __init__(self, data,):
        self.d = data
        self.check_param = self.input_param()
        self.check_params_list = list(self.d.table[self.check_param].unique())

        self.nums = dict()
        self.tables = dict()
        self.dicts = dict()
        for p in self.check_params_list:
            self.nums[p] = self.d.table[self.check_param].value_counts().get(p, 0)
            self.tables[p] = self.d.table[self.d.table[self.check_param] == p]
            self.dicts[p] = dict()

            for column in self.d.cms:
                param_by_col = self.tables[p].groupby(column).size()
                d = param_by_col.to_dict()
                self.dicts[p][column] = d

    def input_param(self):
        check_param = input('The parameter you want to check: ')
        self.is_check_param_exist(check_param)
        return check_param

    def is_check_param_exist(self, param):
        if param not in self.d.cms:
            log_project.log(f"invalid parameter entered.\n")
            raise Exception("invalid parameter.")