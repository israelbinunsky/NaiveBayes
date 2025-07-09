from stats import Stats
class Manager:
    def __init__(self,data):
        self.s = Stats(data)

    def param(self):
        p = input('The parameter you want to check:')
        param = p.replace(' ', '_')
        self.s.d.check_param = param

    def inputs(self):
        c = input('category: ')
        col = c.replace(' ', '_')
        r = input('sort: ')
        row = r.replace(' ', '_')
        l = list()
        l[0] = col
        l[1] = row
        return l

    def main(self):
        self.param()
        l = self.inputs()
        result = self.s.statistics(l[0],l[1])
        more = input('more details? ')
        if more == 'yes':
            l = self.inputs()
            r2 = self.s.statistics(l[0],l[1])
            result = {"yes": result["yes"] * r2["yes"], "no": result["no"] * r2["no"]}
            self.printing(result)


    def printing(self, result):
        if result["yes"] > result["no"]:
            print("result: yes.")
        elif result["no"] > result["yes"]:
            print("result: no.")
        else:
            print("result: equal.")
        print(f"yes: {result["yes"]}. no: {result["no"]}.")
