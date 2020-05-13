#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    dif=[];
    f=0;
    for i in range(len(s)-1):
        dif.append(abs(ord(s[i])-ord(s[i+1])));
    j=0;
    for i in range(len(s)-1,0,-1):
        if dif[j] == abs(ord(s[i])-ord(s[i-1])):
            j+=1;
            continue;
        else:
            f=1;
            break;

    if f ==0:
        return 'Funny'
    else:
        return 'Not Funny'
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()

