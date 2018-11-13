#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = list(alphabet)
    for letter in alphabet:
        if(s1.find(letter) > -1) and (s2.find(letter) > -1):
            return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
