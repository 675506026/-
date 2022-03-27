import pandas as pd
import xlrd
from xlutils.copy import copy
import openpyxl
def sum_stu(x):
    data = xlrd.open_workbook('score.xls')
    sheet = data.sheet_by_index(0)
    sum = 0
    for i in range(1, 100):
        sum = sum + sheet.row(x)[i].value
    return sum


def sum_all_stu():
    file = 'score.xls'
    data = xlrd.open_workbook(file)
    w_data = copy(data)
    w_sheet = w_data.get_sheet(0)
    for i in range(0, 100):
        if i == 0:
            w_sheet.write(i, 101, 'sum')
            w_sheet.write(i, 102, 'average')
        else:
            sum = sum_stu(i)
            w_sheet.write(i, 102, sum)
            average = sum/100
            w_sheet.write(i, 102,average)
    w_data.save(file)


def sort(x):
    stexcel = pd.read_excel('score.xls')
    stexcel.sort_values(by='sum', inplace=True, ascending=False)
    print(stexcel[0:x])
    df = pd.DataFrame(stexcel[0:x])
    df.to_excel('Function_2_Detailed_results.xlsx')

def main_2():
    x = input('显示总成绩前X名学生信息\nx的值是')
    sum_all_stu()
    sort(int(x))


main_2()