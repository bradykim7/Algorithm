#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    start = a[-1:][0];
    finish = b[0]+1;
    member =[];
    for i in range(start, finish):
        member.append(i);
    result = 0;

    for i in range(start, finish):
        for j in range(len(a)):
            if i%a[j] !=0 :
                member.remove(i);
                break;

    for i in range(len(member)):
        index = 0;
        for j in range(len(b)):
            if b[j]%member[i] != 0:
                index= 1;
                break;

        if index == 0:
            result +=1;              

    return result;                       

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()

