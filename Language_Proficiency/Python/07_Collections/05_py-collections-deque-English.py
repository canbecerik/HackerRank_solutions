from collections import deque

N = int(input())
d = deque()

for _ in range(N):
    method, *vals = input().split()
    getattr(d, method)(*vals)

print(*d)