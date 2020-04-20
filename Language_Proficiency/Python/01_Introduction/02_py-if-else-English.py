#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 1:
        print ("Weird")
    else:
        if (n % 2 == 0):
            if (n <= 5 and n >= 2) or n > 20:
                print ("Not Weird")
            elif n <= 20 and n >= 6:
                print ("Weird")
