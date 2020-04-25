#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    ans = 0;
    on=0;
    for i in range(len(B)):
        if B[i]%2 ==1:
            on+=1;
    if on%2 != 0:
        return 'NO'

    for i in range(len(B)):
        if i == len(B)-1:
            continue;

        if B[i]%2 ==1:
            B[i]+=1;
            B[i+1]+=1;
            ans+=2;
    print(B)

    return ans;      



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()

