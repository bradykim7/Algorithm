#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the misereNim function below.
def misereNim(s):
    # because, where all values '1'
    c=1
    n=0
    for i in s:
        if i > 1:
            c =0
        n^=i
    return "Second" if n == c else "First"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        s = list(map(int, input().rstrip().split()))

        result = misereNim(s)

        fptr.write(result + '\n')

    fptr.close()
