#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    ans =0;
    page=1;
    for j in range(n):
        for i in range(1,arr[j]+1):
            if page == i:
                ans+=1;
            if i % k==0 or i==arr[j]:
                page+=1;    
    return ans;   


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

