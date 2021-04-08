#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the makeAnagram function below.
def makeAnagram(a, b):

    deletions = 0

    count_a, count_b = Counter(a), Counter(b)

    count_a.subtract(count_b)

    deletions = sum(abs(i) for i in count_a.values())

    return deletions

def test():
    a = 'cde'
    b = 'abc'
    print(f"{makeAnagram(a, b)}")

test()



'''if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
'''