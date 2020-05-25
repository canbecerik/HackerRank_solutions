from collections import OrderedDict

N = int(input())

items = OrderedDict()

for i in range(N):
    transaction = input().split()
    product = " ".join(transaction[:-1])
    price = int(*transaction[-1:])
    if items.get(product):
        items[product] += price
    else:
        items[product] = price

for i, j in items.items():
    print(i, j)