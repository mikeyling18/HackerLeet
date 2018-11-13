#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    steps = 0
    i = 0
    while i < len(c)-1:
        if i == len(c)-2:
            steps += 1
            return steps
        if c[i+2] == 0:
            i += 2
        else:
            i += 1
        steps += 1
    return steps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
