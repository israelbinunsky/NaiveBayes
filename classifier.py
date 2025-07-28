from validator import Validator
import log_project
class Classifier:
    def __init__(self,trainer_json):
        self.v = Validator(trainer_json)

    def inputs(self):
        col = input('category: ')
        row = input('sort: ')
        if row.isdigit():
            row = int(row)
        l = list()
        l.append(col)
        l.append(row)
        return l

    def main_inputs(self,col, row):
        result = self.v.check_validator(col,row)
        if not result:
            print("not exist.")
        more = input('more details? ')
        if more == 'yes':
            l = self.inputs()
            result2 = self.main_inputs(l[0], l[1])
            if result and result2:
                for p in self.v.check_col_rows_list:
                    result[p] = result[p] * result2[p]
            elif result2:
                result = result2
        return result

    def main(self,col, row):
        result = self.v.check_validator(col,row)
        if not result:
            print("not exist.")
        return result


    def printing(self, result):
        mx = 0
        mx_key = ''
        if result:
            for i in result.keys():
                if result[i] > mx:
                    mx = result[i]
                    mx_key = i
            txt = f"The highest percentage is: '{mx_key}'\n{mx} % of all '{mx_key}' in '{self.v.check_col}' parameter are matching your settings.\nall options:"
            for p in self.v.check_col_rows_list:
                txt += f"\n{p}: {result[p]} %"
            print(txt)
            d = self.create_json_format(result,mx,mx_key)
            log_project.log(f"'{self.v.check_col}' parameter: calculated successfully.\n")
            return d
        else:
            print('no valid parameter to check.')
            log_project.log(f"'{self.v.check_col}' parameter: stats parameters are not in the table.\n")

    def create_json_format(self,result, mx, mx_key):
        d = dict()
        d['max'] = str(mx_key)
        d['max percentage'] = float(mx)
        for p in self.v.check_col_rows_list:
            d[str(p)] = float(result[p])
        return d
