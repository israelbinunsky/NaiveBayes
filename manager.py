from stats import Stats

class Manager:
    def __init__(self,param):
        self.s = Stats(param)

    def inputs(self):
        c = input('category: ')
        col = c.replace(' ', '_')
        r = input('sort: ')
        row = int(r)
        l = list()
        l.append(col)
        l.append(row)
        return l

    def main(self,col, row):
        result = self.s.calculation(col,row)
        if not result:
            print("not exist.")
        more = input('more details? ')
        if more == 'yes':
            result2 = self.main()
            if result and result2:
                for p in self.s.p.check_params_list:
                    result[p] = result[p] * result2[p]
            elif result2:
                result = result2
            # result = {"yes": result["yes"] * r2["yes"], "no": result["no"] * r2["no"]}
        return result


    def printing(self, result):
        # if result["yes"] > result["no"]:
        #     print("result: yes.")
        # elif result["no"] > result["yes"]:
        #     print("result: no.")
        # else:
        #     print("result: equal.")
        # print(f"yes: {result["yes"]}. no: {result["no"]}.")

        mx = 0
        mx_key = ''
        if result:
            for i in result.keys():
                if result[i] > mx:
                    mx = result[i]
                    mx_key = i

            txt = f"The highest percentage is: '{mx_key}'\n{mx} % of all '{mx_key}' in '{self.s.p.check_param}' parameter are matching your settings.\nall options:"
            for p in self.s.p.check_params_list:
                txt += f"\n{p}: {result[p]} %"
            print(txt)
            d = self.create_json_format(result,mx,mx_key)
            return d
        else:
            print('no valid parameter to check.')


    def create_json_format(self,result, mx, mx_key):
        d = dict()

        d['max'] = str(mx_key)
        d['max percentage'] = float(mx)
        for p in self.s.p.check_params_list:
            d[str(p)] = float(result[p])

        return d
