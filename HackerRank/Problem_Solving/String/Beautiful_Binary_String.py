#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.
def beautifulBinaryString(b):
    ans=0;
    temp=''
    for i in b:
        temp+=i;
        if '010' in temp:
            temp=''
            ans+=1;

    return ans;


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()

