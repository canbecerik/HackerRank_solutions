from itertools import combinations_with_replacement

S, k = [i for i in input().split(" ")]
k = int(k)


combs = list(combinations_with_replacement(sorted(S), k))
combs.sort()
[print("".join(i)) for i in combs]