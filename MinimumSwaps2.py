#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    i = 0
    while i < len(arr):
        if arr[i] == i + 1:
            i += 1
            continue
        else:
            temp = arr[i]
            arr[i] = arr[arr[i] - 1]
            arr[temp - 1] = temp
            swaps += 1
            i = max(0, i - 1)
    return swaps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
