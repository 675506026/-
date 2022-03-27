import xlrd
from xlutils.copy import copy


def get_file():
    data = xlrd.open_workbook('score.xls')
    sheet = data.sheet_by_index(0)
    return sheet


def get_average(x):
    sheet = get_file()
    subject_sum = 0
    for i in range(1, 100):
        subject_sum = subject_sum + sheet.row(x)[i].value
    average = subject_sum / 100
    return average


def get_eversubject_average():
    print('start calculating the average')
    file = 'score.xls'
    data = xlrd.open_workbook(file)
    w_data = copy(data)
    w_sheet = w_data.get_sheet(0)
    for i in range(0, 100):
        if i == 0:
            w_sheet.write(101, 0, 'subjec average')
        else:
            average = get_average(i)
            w_sheet.write(101, i, average)
            print(average)
    w_data.save(file)
    print('all averages of subjects calculate finished')


def Compare_sroces(inp):
    sheet = get_file()
    poor_stu = {}

    for x in range(1, 100):
        poor_sub = {}
        for y in range(1, 100):
            sub_score = sheet.row(x)[y].value
            sub_average = sheet.row(x)[101].value
            if sub_score < (sub_average * float(inp) / 100):
                stu = str(sheet.row(x)[0].value)
                sub = str(sheet.row(0)[y].value)
                less_score = str(sub_average - sub_score)
                poor_sub[sub] = str(less_score)
            poor_stu[stu] = poor_sub
    return poor_stu,poor_sub

if __name__ == '__main__':

    inp = input('偏科定义的Y%是多少？')
    get_eversubject_average()
    dic,poor_sub = Compare_sroces(inp)
    with open('function_3_result.txt','w') as obj:
        for k, v in dic.items():
            for m, n in poor_sub.items():
                str_1 = str('偏科学生是'+ k+ '偏科科目和与平均分相差分数是'+ m+ ':'+ n)
                obj.write(str_1+'\n')