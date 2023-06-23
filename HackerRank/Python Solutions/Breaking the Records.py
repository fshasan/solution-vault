#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    min_count = 0
    max_count = 0
    
    min_sc = scores[0]
    max_sc = scores[0]
    store = []
    
    for i in range(len(scores)):
        if(min_sc > scores[i]):
            min_sc = scores[i]
            min_count += 1
    for i in range(len(scores)):
        if(max_sc < scores[i]):
            max_sc = scores[i]
            max_count += 1
    
    store.append(max_count)
    store.append(min_count)
    
    return store

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
