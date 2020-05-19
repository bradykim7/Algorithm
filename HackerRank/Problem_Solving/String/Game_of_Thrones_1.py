#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    # aaabbbb
    # bab a bab
    c={};
    for i in s:
        c[i]=0;
    for i in s:
        c[i]+=1;

    count =0;
    one =0;
    if len(s) % 2 ==0:
        for x,y in c.items():
            if y%2 == 1:
                return 'NO';
        return 'YES'
    else:
        for x,y in c.items():
            if y ==1:
                one+=1;
            if y %2== 1:
                count+=1;
        if one >1:
            return 'NO'
        elif count % 2 == 0:
            return 'NO';
        else:
            return 'YES'



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
