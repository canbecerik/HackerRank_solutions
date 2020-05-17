import string

M = int(input())
set_m = set([int(i) for i in input().split()])
N = int(input())
set_n = set([int(i) for i in input().split()])

n_diff = set_n.difference(set_m)
m_diff = set_m.difference(set_n)

sym_diff_list = sorted(m_diff.union(n_diff))

for i in sym_diff_list:
    print(i)
 