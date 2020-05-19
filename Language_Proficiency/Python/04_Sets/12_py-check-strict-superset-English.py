A = set([int(i) for i in input().split(' ')])
n = int(input())
for i in range(n):
    B = set([int(i) for i in input().split(' ')])
    if not B.difference(A):
        if A.difference(B):
            continue
    print("False")
    exit()
print("True")