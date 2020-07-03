#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.

def maxMin(k, arr):
    c= (sorted(arr))
    for i in range(0,len(c)-k+1):
        if i == 0:
            ans = c[i+k-1]- c[i]
        elif c[i+k-1]-c[i] <= ans:
            ans = c[i+k-1]- c[i]
    return (ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
