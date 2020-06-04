#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sumXor function below.
def sumXor(n):
    '''
    ans = 0
    # this method meet time limits
    for i in range(n+1):
        if n+i == n^i:
            ans+=1;
    '''

    if n == 0:
        return 1
    else:
        return 2**(bin(n).count('0')-1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
