#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    
    # if there's least one '_' and No just one word 
    if '_' in b :
        for i in b:
            if i != '_' and b.count(i) == 1 :
                return 'NO'
        return 'YES'

    # If there's no '_' 
    else :
        for i in range(len(b)):
            if b.count(b[i]) ==1:
                return 'NO'
            if i == 0:
                if b[i] != b[i+1]:
                    return 'NO'
                else:
                    continue
            elif i == len(b)-1:
                if b[i] != b[i-1]:
                    return 'NO'
                else:
                    continue;
            elif (b[i] != b[i+1] and b[i] != b[i-1]):
                return 'NO'
        #if it is happy case 
        return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()

