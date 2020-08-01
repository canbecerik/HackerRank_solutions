#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    # Keep track of valleyNo and elevation
    elevation = 0
    valleyNo = 0
    for i in range(n):
        # If above MSL
        if elevation > 0:
            # Track elevation
            if s[i] == 'U':
                elevation += 1
            else:
                elevation -= 1
        else:
            # Below MSL, track elevation and detect end of valley
            if s[i] == 'D':
                elevation -= 1
            else:
                elevation +=1
                if elevation == 0:
                    valleyNo += 1
        print(f"s[i]={s[i]}, elevation={elevation}")
    return valleyNo




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
