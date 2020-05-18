n = int(input())
eng_subs = set(input().split(' '))
b = int(input())
fra_subs = set(input().split(' '))

print(len(eng_subs.union(fra_subs)))