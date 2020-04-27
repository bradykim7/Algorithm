#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
    i = 3;
    n = 1;

    while n < t:
        n += i;
        i*=2;
    if n == t: 
        return n+2;
    else:
        return n-i//2+2-(t-(n-i//2))
    print(n-i//2)
    print(n)
    

               

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()

