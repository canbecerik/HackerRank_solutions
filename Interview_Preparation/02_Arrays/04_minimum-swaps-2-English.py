#!/bin/python3

import os


# Complete the minimumSwaps function below.
def minimumSwaps(arr):

    # Init result
    res = 0

    # Get array length
    n = len(arr)

    # Track array elements and their positions in (position, element) format
    # Sort array by elements in asc order to put them in correct position
    pos_track = sorted([*enumerate(arr)], key=lambda i: i[1])

    # Record if element is already visited, init to false

    visited = {i: False for i in range(n)}

    # Start iteration over each element
    for i in range(n):
        # Check if already swapped or in sorted position
        if pos_track[i][0] == i or visited[i]:
            continue

        # Init cycle size
        cycle = 0

        # New variable to iterate over nodes for current element
        j = i

        while not visited[j]:
            # Node is now visited
            visited[j] = True

            # Add to cycle
            cycle += 1
            # Go to next node after this
            j = pos_track[j][0]

        # Update answer if swaps are made for this element
        res += (cycle - 1) if cycle > 0 else 0

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
