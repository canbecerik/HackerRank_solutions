from collections import namedtuple

N = int(input())
columns = input().split()
marks_sum = 0

for i in range(N):
    students = namedtuple('Student', columns)
    data = input().split()
    student = students(*data)
    marks_sum += int(student.MARKS)
print('{:.2f}'.format(marks_sum / N))