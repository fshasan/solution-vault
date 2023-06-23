#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if(grades[i]<38):
            grades[i] = grades[i]
        else:
            if((grades[i]) % 5 == 0):
                grades[i] = grades[i]
            elif((grades[i] + 1) % 5 == 0):
                grades[i] = grades[i] + 1
            elif((grades[i] + 2) % 5 == 0):
                grades[i] = grades[i] + 2
            elif((grades[i] + 3) % 5 == 0):
                grades[i] = grades[i]
 
    return grades
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
