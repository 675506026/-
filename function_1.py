import xlrd
from student import student


def openfile():
    data = xlrd.open_workbook('score.xls')
    sheet = data.sheet_by_index(0)
    return sheet


def readstuscores(sheet, row, student):
    score = []
    for i in range(1, 100):
        score.append(sheet.row(row)[i].value)
    student.scores = score
    return student


def readstuname(sheet, row, student):
    student.name = sheet.row(row)[0]
    return student


def createstu(x):
    sheet = openfile()
    stu = student
    stu = readstuname(sheet, x, student)
    for i in range(1, 100):
        stu = readstuscores(sheet, i, stu)
    return stu


def sum_and_average(student):
    sum, array = student.average_and_sum(student)
    return sum, array


def main_1():
    x = int(input('你想查询第几名学生的信息？\n'))
    stu = createstu(x)
    sum, average = sum_and_average(stu)
    print('第' + str(x) + '名学生的总分是' + str(sum))
    print('第' + str(x) + '名学生的平均分是' + str(average))


main_1()