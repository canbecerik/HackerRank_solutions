#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the isBalanced function below.


def isBalanced(s):
    open_bracket = "({["

    # If not even number of parantheses, fail
    if len(s) % 2:
        return "NO"

    # Fill queue
    char_queue = collections.deque()
    for char in s:
        if char in open_bracket:
            char_queue.append(char)
        elif not char_queue:
            return "NO"
        elif char == ")" and char_queue.pop() == "(":
            continue
        elif char == "]" and char_queue.pop() == "[":
            continue
        elif char == "}" and char_queue.pop() == "{":
            continue
        else:
            return "NO"
    if len(char_queue) != 0:
        return "NO"
    return "YES"


if __name__ == '__main__':
    print(isBalanced("}][}}(}][))]"))
'''if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
'''
