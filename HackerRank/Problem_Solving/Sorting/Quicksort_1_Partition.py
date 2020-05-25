#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    l=[]
    r=[]
    c= arr[0]
    for i in arr:
        if i == arr[0]:
            continue;
        if i > c:
            r.append(i)
        elif i < c:
            l.append(i)
    ans = l+[c]+r;
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
