from statistics import mean

N, X = map(int, input().split())
students = [[float(0)] * X for i in range(N)]

for i in range(X):
    subject = [float(j) for j in input().split()]
    for j in range(N):
        students[j][i] = subject[j]

for i in range(N):
    print("%.1f" % mean(students[i]))