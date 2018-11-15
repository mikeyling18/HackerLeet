#!/bin/python3

import math
import os
import random
import re
import sys
import time
import bisect

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    def get_median(arr):
        if d % 2 == 1:
            median = arr[int(d / 2)]
        else:
            median = (arr[int(d / 2) - 1] + arr[int(d / 2)]) / 2.0
        return median

    count = 0
    l = expenditure[0:d].copy()
    l.sort()
    for i in range(0, len(expenditure) - d, 1):
        med = get_median(l)
        newTerm = expenditure[i+d]
        if newTerm >= 2*med:
            count += 1
        l.remove(expenditure[i])
        l.insert(bisect.bisect(l, newTerm), newTerm)
    return count


if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))
    startTime = time.time()
    print(activityNotifications(expenditure, d))
    print(time.time() - startTime)

