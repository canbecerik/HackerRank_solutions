from itertools import permutations

S, k = [i for i in input().split(" ")]
k = int(k)

perms = list(permutations(S, k))
perms.sort()

[print("".join(i)) for i in perms]