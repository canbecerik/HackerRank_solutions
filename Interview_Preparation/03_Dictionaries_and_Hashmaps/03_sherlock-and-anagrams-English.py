#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.


def sherlockAndAnagrams(s):
    anagrams = []
    # Get all substrings
    substrings = [s[i:j]
                  for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
    # Check if they are anagrams
    for substring in substrings:
        for i in range(len(substrings)):
            if sorted(substrings[i]) == sorted(substring):
                if substrings[i] != substring:
                    anagrams.append(substring)
                    anagrams.append(substrings[i])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
