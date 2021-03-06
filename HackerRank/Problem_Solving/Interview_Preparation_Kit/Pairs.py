#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    s= sorted(arr)
    ans=0
    c=set()

    # dict is more faster than list when search !
    for i in s:
        if i-k in c:
            ans+=1
        c.add(i)

    return ans



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
