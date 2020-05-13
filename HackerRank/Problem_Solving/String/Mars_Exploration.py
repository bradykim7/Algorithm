#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    ans=0;
    # 0 1 2  3 4 5  6 
    for i in range(len(s)):
        print(i,s[i])
        if i%3==2:
            if s[i]!='S':
                ans+=1;

        elif i%3==1:
            if s[i]!='O':
                ans+=1;

        else:
            if s[i]!='S':
                ans+=1;
    return ans;



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()

