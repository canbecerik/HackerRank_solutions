#!/bin/python3

import os
from collections import Counter
from math import ceil

# Complete the repeatedString function below.


def repeatedString(s, n):
    # Check if a exists in s, avoid computation if not
    if 'a' not in s:
        return 0
    # Compute how many times the whole string needs to be repeated
    repNumber = ceil(n // len(s))
    # Compute the length of partial string
    extraChar = n % len(s)
    # Count 'a' in single string
    singleCount = Counter(s[:n])['a']
    # Count 'a' in partial string
    extraCount = Counter(s[:extraChar])['a']
    return (singleCount * repNumber + extraCount)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
