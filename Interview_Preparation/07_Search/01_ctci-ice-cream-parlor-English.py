def whatFlavors(cost, money):
    remains = dict()
    for index, c in enumerate(cost):
        if c not in remains:
            remains[money - c] = index + 1
        else:
            print(remains[c], index + 1)
            return


def main():
    cost = [2, 1, 3, 5, 6]
    money = 5
    whatFlavors(cost, money)


main()
