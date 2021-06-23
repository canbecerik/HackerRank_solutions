#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.


def isValid(s):
    one_removed = False
    char_count = Counter(s)
    # Init to 0
    count_list = list(char_count)

    # Start filling the results array
    for index, char in enumerate(count_list[1:]):
        # If prev char count is zero and removed recently, compare with 2 prev chars
        if not char_count[count_list[index]] and one_removed:
            index -= 1
        # If equals to prev char, cont
        if char_count[char] == char_count[count_list[index]]:
            continue
        # If not equal, check if we already removed one character
        elif not one_removed:
            # If we did not, remove,
            one_removed = True
            # Then check if it is one more, decrease if so
            if char_count[char] == char_count[count_list[index]] + 1:
                char_count[char] -= 1
                continue
            # Else, check if it is a single occuring char
            elif char_count[char] == 1:
                # If we are at the last element, removing it fixes this
                if len(count_list) <= index + 2:
                    del char_count[char]
                # If the second next element is the same, removing it also fixes this
                elif char_count[count_list[index + 2]] == char_count[count_list[index]]:
                    del char_count[char]
                # If not, decrease the earlier char if that fixes it and if it is the first case
                elif char_count[count_list[index + 2]] == char_count[count_list[index]] - 1 and index == 0:
                    char_count[count_list[index]] -= 1
                else:
                    return "NO"
                continue

            else:
                return "NO"

        # If one less, try removing this character
        else:
            return "NO"

    return "YES"


def test():
    s = 'aabbc'
    print("Should be yes")
    print(isValid(s))
    s = 'aaaaabc'
    print("Should be no")
    print(isValid(s))


test()

'''if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()'''
