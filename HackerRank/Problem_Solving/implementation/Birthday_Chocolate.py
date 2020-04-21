#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    # d == sum
    # m == length
    ans = 0;

    for i in range(len(s)):
        index=0;
        n = 0;
        while n< m:
            index+= s[i+n];
            n +=1;
        if index == d:
            ans+=1;
        if i+n == len(s):
            break;
    
    return ans;




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()

