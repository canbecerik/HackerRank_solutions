#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the checkMagazine function below.

def checkMagazine(magazine, note):

    # Parse magazine and number of occurences into dictionary

    magazine_store = {}

    for word in magazine:
        # Add word or increase occurences if already added
        if word in magazine_store:
            magazine_store[word] += 1
        else:
            magazine_store[word] = 1

    # Try to write the note
    for word in note:
        if word in magazine_store:
            # Decrease if more than one instance of the word exists in magazine
            if magazine_store[word] > 1:
                magazine_store[word] -= 1
            # Remove if only one instance exists in magazine
            elif magazine_store[word] == 1:
                del magazine_store[word]
        # Fail if cannot find in magazine
        else:
            print("No")
            return False

    print("Yes")
    return True


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
