#!/bin/python3
# trash problem
import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    n = len(c);
    ans = 100;
    i=0; nxt=0;
    while i==0 or nxt != 0:
        nxt =(i+k)%n;
        if c[nxt]==0:
            ans-=1;
        else :
            ans-=3;
        i = i+k;    

    return ans;        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()

