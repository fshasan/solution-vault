#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pcount = 0
    ncount = 0
    zcount = 0
    
    for i in range(len(arr)):
        if(arr[i]>0):
            pcount+=1
        elif (arr[i]<0):
            ncount+=1
        elif (arr[i] == 0):
            zcount+=1
    p = pcount / len(arr)
    n = ncount / len(arr)
    z = zcount / len(arr)
    
    ret = [p,n,z]
    for i in range(len(ret)):
        print(ret[i])
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
