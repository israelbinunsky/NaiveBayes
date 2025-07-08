import pandas as pd
table = pd.read_csv("data for NB buys computer.xlsx - Sheet1.csv", skiprows=3)
table = table.loc[:, ~table.columns.str.contains('^Unnamed')]

yes_num = table['Buy_Computer'].value_counts().get('yes', 0)
no_num = table['Buy_Computer'].value_counts().get('no', 0)

yes_table = table[table['Buy_Computer'] == 'yes']
no_table = table[table['Buy_Computer'] == 'no']

yes_dict = dict()
no_dict = dict()

for column in table.columns:
    if column == 'Buy_Computer':
        break
    if column != 'id':
        yes_by_age = yes_table.groupby(column).size()
        yes = yes_by_age.to_dict()
        yes_dict[column] = yes

        no_by_age = no_table.groupby(column).size()
        no = no_by_age.to_dict()
        no_dict[column] = no

def statistics():
    col = input('category: ')
    row = input('sort: ')
    y = yes_dict[col][row]
    n = no_dict[col][row]
    yes_result = y / yes_num
    no_result = n / no_num
    result = {"yes": yes_result, "no": no_result}
    more = input('more details? ')
    if more == 'yes':
        r2 = statistics()
        result = {"yes": result["yes"] * r2["yes"], "no": result["no"] * r2["no"]}
    return result


def menue():
    result = statistics()
    if result["yes"] > result["no"]:
        print("yes")
    elif result["no"] > result["yes"]:
        print("no")
    else:
        print("equal")
    print(result["yes"], result["no"])

menue()
