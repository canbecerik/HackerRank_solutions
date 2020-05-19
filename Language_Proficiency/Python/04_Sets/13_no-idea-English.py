m, n = map(int, input().split(' '))
n_arr = map(int, input().split(' '))
A = set([int(i) for i in input().split(' ')])
B = set([int(i) for i in input().split(' ')])
happy = 0

for i in n_arr:
    if i in A:
        happy += 1
    elif i in B:
        happy -= 1

print(happy)