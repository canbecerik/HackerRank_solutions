#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.


def stepPerms(n):
    cache = {}
    cache[1], cache[2], cache[3] = 1, 2, 4
    for i in range(4, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2] + cache[i - 3]
    return cache[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
