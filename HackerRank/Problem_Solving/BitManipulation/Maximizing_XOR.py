#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximizingXor function below.
# This function is making XOR operator
# In computer science, We can make XOR with NOT, AND, OR operator
# a XOR b = (NOT a AND b) OR (a AND NOT b)

def maximizingXor(l, r):
    ans =[]
    for i in range(l,r+1):
        for j in range(l,r+1):
            ans.append(~i & j | i & ~j)

    return max(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input())

    r = int(input())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
