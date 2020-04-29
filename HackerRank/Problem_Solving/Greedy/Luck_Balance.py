#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    # contests : [luck , importance]
    ans =0;
    # add all
    for i in contests:
        ans += i[0]
    # find and make array   
    c=[];
    for i in contests:
        if i[1] == 0:
            continue;
        else:
            c.append(i[0]);
    c.sort();
    # after sorting, submit the number 
    for i in range(0,len(c)-k):
        
        ans -= c[i]*2;
    
    return ans;        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()

