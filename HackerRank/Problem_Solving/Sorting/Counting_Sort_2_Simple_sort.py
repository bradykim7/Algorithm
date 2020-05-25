#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    c = [0]*100
    ans=[]
    for i in arr:
        c[i]+=1;

    for i in range(len(c)):
        for j in range(c[i]):
            ans.append(i)
    return (ans)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
