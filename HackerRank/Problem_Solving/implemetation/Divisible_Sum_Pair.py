#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    # n == len(ar)
    # k == divide number
    ans = 0;
    for i in range(n):
        index = 1;
        while index < n:
            if i+index == n:
                break;              
            if (ar[i]+ar[i+index]) % k ==0 :
                ans+=1;
                index+=1;
            else :
                index+=1;
                   

    return ans;


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

