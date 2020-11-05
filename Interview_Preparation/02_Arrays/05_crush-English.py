#!/bin/python3

import os

# Complete the arrayManipulation function below.


def arrayManipulation(n, queries):
    array = [0 for x in range(n * 2)]
    # print("Init Array:")
    # print(array)
    max_value = 0
    # print(f"Begin iteration over {queries}")
    for query in queries:
        a = query[0] - 1
        b = query[1]
        k = query[2]

        # Track changes over array
        array[a] += k
        array[b] -= k

    # Track current count to compare with max val
    curr_count = 0
    # Get final result
    for i in array:
        curr_count += i
        if curr_count > max_value:
            max_value = curr_count

    return max_value


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
