#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
# Once again dealing with Dictionary in python3 is quite useful and must know how to use it !
def countSort(arr):
    for i in range(len(arr)//2):
        arr[i][1] ='-'
    c ={}
    for i in range(int(max(arr)[0])+1):
        c[i] = []

    for i in arr:
        c[int(i[0])].append(i[1])

    ans=''
    for x,y in c.items():
        for i in y:
            ans+=i+' ';
    print(ans)


if __name__ == '__main__':
    n = int(input().strip())

    arr = []
    ans = [0]*n;

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
