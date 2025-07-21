import log_project
class Model:
    def __init__(self, data ,check_col):
        self.d = data
        self.is_check_col_exist(check_col)
        self.check_col = check_col
        self.check_col_rows_list = list(self.d.table[self.check_col].unique())

        self.nums = dict()
        self.tables = dict()
        self.dicts = dict()
        for p in self.check_col_rows_list:
            self.nums[p] = self.d.table[self.check_col].value_counts().get(p, 0)
            self.tables[p] = self.d.table[self.d.table[self.check_col] == p]
            self.dicts[p] = dict()

            for column in self.d.cms:
                param_by_col = self.tables[p].groupby(column).size()
                d = param_by_col.to_dict()
                self.dicts[p][column] = d

    def is_check_col_exist(self, check_col):
        if check_col not in self.d.cms:
            log_project.log(f"invalid parameter entered.\n")
            raise Exception("invalid parameter.")