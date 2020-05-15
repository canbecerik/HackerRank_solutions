#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):

    # Split names
    names = s.split(' ')
    # Capitalize using list comprehension & Join
    s = (' '.join((word.capitalize() for word in names)))
    # Return result
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
