#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    # a00 b01 c02
    #     d11
    # e20 f21 g22
    ans = []
    for j in range(len(arr)-2):
        for i in range(len(arr)-2):
            res = 0
            res += arr[i][j]
            res += arr[i][j+1]
            res += arr[i][j+2]
            res += arr[i+1][j+1]
            res += arr[i+2][j]
            res += arr[i+2][j+1]
            res += arr[i+2][j+2]
            ans.append(res)

    return max(ans)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
