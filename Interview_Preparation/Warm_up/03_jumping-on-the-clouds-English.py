#!/bin/python3

import math
import os
import random
import re
import sys

# 7
# 0 1 0 0 0 1 0
# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    cloud_number = len(c)
    result = 0
    # Use another variable to emulate C-style for loop with iterator control, init to init value of i
    j = 1

    # Boundary cond check, result is 1 for 2 clouds
    if cloud_number == 2:
        return 1

    for i in range(1, cloud_number - 1):
        # For C-style loop control, ignore iterations unless i == j
        if j != i:
            # Boundary check, add 1 step for last jump
            if i == cloud_number - 2:
                result += 1
            continue
        # Increment result and actual iterator
        result += 1
        j += 1       
        # Can jump 2 clouds if that cloud is 0
        if c[i + 1] == 0:
            # Allow skipping next iteration by increasing j again
            j += 1
                
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
