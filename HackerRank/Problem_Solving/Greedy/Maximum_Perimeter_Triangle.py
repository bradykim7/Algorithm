#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumPerimeterTriangle function below.
def maximumPerimeterTriangle(sticks):
    # a + b > c(longest line )
    # a+b != c
    # 0 1 2 
    sticks.sort();
    ans =-2;
    # start number at the end of list -2 
    for i in range(len(sticks)-3,-1,-1):
        print(i)
        if sticks[i+2] >= sticks[i] + sticks[i+1] :
            continue;
        else:
            ans =i;
            break;

    if ans == -2:
        return -1;
    else:
        return sticks[ans],sticks[ans+1],sticks[ans+2]; 

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    if result == -1:
        fptr.write('-1');
    else:
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

