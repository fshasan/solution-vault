#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    temp = []
    sum = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if(i!=j):
               sum += arr[j] 
    
        temp.append(sum)
        sum=0
        
      
    a = min(temp)
    b = max(temp)
    print(a ,b)
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
