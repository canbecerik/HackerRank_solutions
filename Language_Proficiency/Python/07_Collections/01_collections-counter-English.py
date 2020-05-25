from collections import Counter

X = int(input())
sizes = Counter([int(i) for i in input().split(" ")])
N = int(input())
balance = 0

for i in range(N):
    cust_size, cust_cash = list(map(int, input().split(" ")))
    if sizes[cust_size]:
        sizes[cust_size] -= 1
        balance += cust_cash
    else:
        next

print(balance)