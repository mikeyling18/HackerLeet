import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    swaps = 0
    for i in range(len(q)):
        if q[i] > i+3:
            print('Too chaotic')
            return
    for k in range(len(q)-1):
        for i in range(len(q)-1):
            # print(q)
            current_value = q[i]
            if current_value > q[i+1]:
                temp = q[i]
                q[i] = q[i+1]
                q[i+1] = temp
                swaps += 1
    print(swaps)
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)