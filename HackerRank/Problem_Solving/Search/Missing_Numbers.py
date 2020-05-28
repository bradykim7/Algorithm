#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
# Have Two solutions, just choose what you want
    '''
    ans=[]
    c={}
    for i in brr:
        c[i]=0;
    for i in arr:
        c[i]+=1;
    for i in brr:
        c[i]-=1;
    for i in sorted(c.items(), key=lambda x : x[0]):
        if i[1] < 0:
            ans.append(i[0])
    return ans
    '''
    ac = {}
    bc = {}
    ans=[];
    for i in arr:
        ac[i]=0;
    for i in arr:
        ac[i]+=1
    for i in brr:
        bc[i]=0;
    for i in brr:
        bc[i]+=1

    for x,y in bc.items():
        if x not in ac:
            ans.append(x)
        elif ac[x] != y:
            ans.append(x)

    return sorted(ans)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
