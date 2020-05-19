T = int(input())
for i in range(T):
    n_A = int(input())
    A = set([int(j) for j in input().split(' ')])
    n_B = int(input())
    B = set([int(j) for j in input().split(' ')])
    if not A.difference(B):
        print("True")
    else:
        print("False")