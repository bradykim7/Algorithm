#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    # n = budget;
    # c = chocolate cost 
    # m = the number of wrapper 
    ans=0;
    ans+= n//c
    p = ans;
    while p//m != 0:
        a= p // m;
        b= p % m;
        p= a+b;
        ans+= a;


    return ans;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()

