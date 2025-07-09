class Stats:
    def __init__(self, data):
        self.d = data

    def add_one(self, dict):
        for col in dict:
            for row in col:
                dict[col][row] += 1

    def check(self,col,row):
        l = dict()
        y = 0
        n = 0
        if row in self.d.yes_dict[col] and row in self.d.no_dict[col]:
            y = self.d.yes_dict[col][row]
            n = self.d.no_dict[col][row]
        elif row in self.d.yes_dict[col] and row not in self.d.no_dict[col]:
            y = self.d.yes_dict[col][row]
            n = 1
            self.add_one(self.d.no_dict)
            self.d.no_num += 1
        elif row not in self.d.yes_dict[col] and row in self.d.no_dict[col]:
            y = 1
            n = self.d.no_dict[col][row]
            self.add_one(self.d.yes_dict)
            self.d.yes_num += 1
        l["y"] = y
        l["n"] = n
        return l

    def statistics(self,col,row):
        l = self.check(col,row)
        y = l["y"]
        n = l["n"]
        yes_result = y / self.d.yes_num
        no_result = n / self.d.no_num
        result = {"yes": yes_result, "no": no_result}
        return result

