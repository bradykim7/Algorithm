#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    ans = -1
    arr = sorted(arr)
    for i in range(len(arr)-1):
        if ans == -1:
            ans = abs(arr[i]-arr[i+1]);

        if ans > abs(arr[i]-arr[i+1]):
            ans = abs(arr[i]-arr[i+1])

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
