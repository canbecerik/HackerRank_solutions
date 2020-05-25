from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)
B_list = []

for i in range(n):
    d[input()].append(str(i + 1))

for i in range(m):
    B_list.append(input())

for i in B_list: 
    if i in d:
        print(" ".join(d[i]))
    else:
        print("-1")