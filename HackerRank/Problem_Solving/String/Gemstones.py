#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gemstones function below.
def gemstones(arr):
    c=list('abcdefghijklmnopqrstuvwxyz');
    C={}
    ans=0;
    for i in c:
        C[i]=0;
    print(C)
    for i in arr:
        a=set(i);
        for j in a:
            C[j]+=1;
    for i in C:
        if C[i] >= len(arr):
            ans+=1;
    return ans;
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

