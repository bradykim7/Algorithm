#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(arr):
    ans =0;
    for i in range(1,len(arr)):
        temp = arr[i]
        for j in range(i):
            if j >=0 and arr[j] > temp:
                arr[j],arr[i] = arr[i], arr[j]
                ans+=1;
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
