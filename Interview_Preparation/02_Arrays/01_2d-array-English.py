#!/bin/python3

import os

# Complete the hourglassSum function below.


def hourglassSum(arr):
    maxSum = -64
    iterable = range(1, 5)
    for i in iterable:
        for j in iterable:
            currentSum = arr[i - 1][j - 1] + arr[i - 1][j] + arr[i - 1][j + 1] + \
                arr[i][j] + arr[i + 1][j - 1] + \
                arr[i + 1][j] + arr[i + 1][j + 1]
            if currentSum > maxSum:
                maxSum = currentSum
    return maxSum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
