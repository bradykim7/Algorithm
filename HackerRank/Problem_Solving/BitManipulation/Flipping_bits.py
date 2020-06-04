#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    # change integer to binary
    # '032b' means that set the 32 bit
    c = format(n,'032b')
    ans=''
    for i in c:
        if i == '0':
            ans +='1';
        else:
            ans+='0'
    return (int(ans,2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
