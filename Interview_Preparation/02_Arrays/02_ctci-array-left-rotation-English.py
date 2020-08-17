#!/bin/python3

import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    arrLen = len(a)
    # disregard unnecessary rotations
    rotNum = d % arrLen
    toRotArray = a[:rotNum]
    newArr = a[len(toRotArray):]
    newArr.extend(toRotArray)
    return newArr    

if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)
    # result = rotLeft([1, 2, 3, 4, 5], 4)
    print(result)

