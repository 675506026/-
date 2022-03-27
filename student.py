class student:
    name = ''
    scores = []

    def __init__(self, name, scores):
        name = name
        scores = scores

    def average_and_sum(self,):
        sum = 0
        for i in range(0, 99):
            sum = sum + student.scores[i]
        average_num = sum/100
        return sum,average_num