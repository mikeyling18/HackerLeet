import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    swaps = 0
    for k in range(len(a)):
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swaps += 1
    print('Array is sorted in {} swaps.'.format(swaps))
    print('First Element: {}'.format(a[0]))
    print('Last Element: {}'.format(a[-1]))

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
