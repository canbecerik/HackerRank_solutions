# Use 2 empty sets, get rooms as a list. If room is not in first set, add to first set. Else, add to second set. The difference will give captain's room.

K = int(input())
unord_rooms = [int(i) for i in input().split(' ')]
set_first = set()
set_second = set()

for i in unord_rooms:
    if i in set_first:
        set_second.add(i)
    else:
        set_first.add(i)

print(str(set_first.difference(set_second)).strip('{}'))