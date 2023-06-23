#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    m = len(apples)
    n = len(oranges)
    a_count = 0
    o_count = 0
    
    for i in range(m):
        apples[i] = apples[i] + a
        if(apples[i] >= s and apples[i] <= t):
            a_count += 1
    for i in range(n):
        oranges[i] = oranges[i] + b
        if(oranges[i] >= s and oranges[i] <= t):
            o_count += 1
    print(a_count)
    print(o_count)
        

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
