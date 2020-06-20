#!/bin/python3

import math
import os
import random
import re
import sys
# got 20 points must fix it
# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    ans = 0
    i = 0
    '''
    for i in range(len(arr)):
        if arr[i] != i+1:
            ans+=1
            c = arr.index(i+1)
            arr[i], arr[c] = i+1, arr[i]
    '''
    while i <len(arr)-1:
        if arr[i] != i+1:
            ans+=1
            temp =arr[i]
            arr[i], arr[temp-1] = arr[temp-1], arr[i]
        else:
            i+=1

    return (ans)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
