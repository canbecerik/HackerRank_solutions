#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.


def maxSubsetSum(arr):
    # First cases
    max_cache = [arr[0], (arr[1] if arr[0] < arr[1] else arr[0])]

    max_sum = max(max_cache)

    for i in range(2, len(arr)):
        max_sum = max(arr[i] + max_cache[0], max_sum, arr[i])
        max_cache = max_cache[1:] + [max_sum]

    return max_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
