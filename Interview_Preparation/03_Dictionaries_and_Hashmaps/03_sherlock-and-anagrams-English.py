#!/bin/python3

import math
import os
import random
import re
import sys
import collections
# Complete the sherlockAndAnagrams function below.


def sherlockAndAnagrams(s):
    anagram_dict = collections.defaultdict(int)
    count = 0
    for i in range(1, len(s)):
        for j in range(len(s) - i + 1):
            current_sorted = str(sorted(s[j:j + i]))
            count += anagram_dict[current_sorted]
            anagram_dict[current_sorted] += 1
    return count


def test():
    s = "kkkk"
    print(f"{sherlockAndAnagrams(s)}")
    s = "cdcd"
    print(f"{sherlockAndAnagrams(s)}")
    s = "abba"
    print(f"{sherlockAndAnagrams(s)}")
    s = "abcd"
    print(f"{sherlockAndAnagrams(s)}")


test()
