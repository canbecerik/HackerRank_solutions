from itertools import combinations

S, k = [i for i in input().split(" ")]
k = int(k)

for i in range(1, k + 1):
    combs = list(combinations(sorted(S), i))
    combs.sort()
    [print("".join(j)) for j in combs]