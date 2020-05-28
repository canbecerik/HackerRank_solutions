N = int(input())
ints = list(map(int, input().split()))
print(all([i > 0 for i in ints]) and any([str(j) == str(j)[::-1] for j in ints]))