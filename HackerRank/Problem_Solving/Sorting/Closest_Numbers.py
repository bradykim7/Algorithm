#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    sarr= sorted(arr);

    ans=[];
    for i in range(len(sarr)-1):
        if i != 0:
            if m > sarr[i+1]-sarr[i]:
                ans.clear()
                m = sarr[i+1]-sarr[i]
                ans.append(sarr[i])
                ans.append(sarr[i+1])
            elif m == sarr[i+1]-sarr[i]:
                ans.append(sarr[i])
                ans.append(sarr[i+1])
        else:
            m = sarr[i+1]-sarr[i]

    return (ans)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
