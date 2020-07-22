#!/bin/python3

import os

# Complete the sockMerchant function below.


def sockMerchant(n, ar):
    pairs = 0
    # Convert to set for distinct vals, then reconvert set to list
    list_set = list(set(ar))
    for i in list_set:
        # Count for each unique element
        count = ar.count(i)
        # If has more than one, use floor div to determine how many pairs
        if (count > 1):
            pairs += count // 2
    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
