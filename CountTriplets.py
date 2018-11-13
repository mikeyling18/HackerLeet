#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


# Complete the countTriplets function below.
def countTriplets(arr, r):
    two = defaultdict(int)
    one = defaultdict(int)
    count = 0

    for k in arr:
        count += two[k / r]
        two[k] += one[k / r]
        one[k] += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
