#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0
    for k in range(len(q)):
        if q[k] - (k + 1) > 2:
            print('Too chaotic')
            return
    for j in range(len(q) - 1, -1, -1):
        leftmost = max(0, q[j] - 2 - 1)
        rightmost = j
        interval = q[leftmost:rightmost + 1]
        current_shirt_value = interval[len(interval) - 1]
        bribes += sum(shirt_value > current_shirt_value for shirt_value in interval)
    print(bribes)
    return


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
