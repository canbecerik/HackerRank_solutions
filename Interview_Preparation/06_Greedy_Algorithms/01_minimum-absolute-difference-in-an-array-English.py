#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.


def minimumAbsoluteDifference(arr):
    # Sort first
    arr.sort()
    # Init case
    min_diff = abs(arr[1] - arr[0])
    # Iter thru array
    for i in range(2, len(arr)):
        min_diff = min(min_diff, abs(arr[i] - arr[i - 1]))

    return min_diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
