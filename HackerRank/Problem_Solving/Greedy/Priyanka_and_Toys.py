#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the toys function below.
def toys(w): 
    w.sort();
    c = w[0];
    ans=0;
    for i in w:
        if i <= c+4:
            continue;
        else:
            c=i;
            ans+=1;
    return (ans+1)        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()

