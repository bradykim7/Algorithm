#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    nn = str(n);
    ans=0;

    for i in range(len(nn)):
        if int(nn[i])==0:
            continue;
        elif n%int(nn[i])==0:
            ans+=1;
    return ans;        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

